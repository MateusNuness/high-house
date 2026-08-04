import os
from typing import List, Dict, Any
from eos.domain.contracts.collection_brief import CollectionBrief
from eos.application.workflows.editorial_creation import EditorialWorkflow
from eos.infrastructure.renderer import PlaywrightRenderer
from langfuse.langchain import CallbackHandler

class CollectionOrchestrator:
    """
    Orquestra a geração de múltiplos pôsteres em lote (batch processing) 
    para uma coleção e gerencia a exportação dos artefatos finais (PNG + TXT).
    """

    def __init__(self, editorial_workflow: EditorialWorkflow, output_dir: str):
        self.editorial_workflow = editorial_workflow
        self.output_dir = output_dir
        self.renderer = PlaywrightRenderer()

    def process_collection(self, collection_brief: CollectionBrief) -> List[Dict[str, Any]]:
        collection_path = os.path.join(self.output_dir, collection_brief.collection_id)
        os.makedirs(collection_path, exist_ok=True)
        
        app = self.editorial_workflow.build_app()
        results = []
        previous_posters = []

        print(f"\n[ORCHESTRATOR] Iniciando o lote para a Coleção: {collection_brief.name} ({len(collection_brief.chapters)} Pôsteres)")

        for index, chapter_brief in enumerate(collection_brief.chapters):
            poster_num = str(index + 1).zfill(2)
            print(f"\n[ORCHESTRATOR] === Processando Pôster {poster_num}: {chapter_brief.topic} ===")
            
            # Setup Langfuse
            session_id = f"collection-{collection_brief.collection_id}-poster-{poster_num}"
            tags = ["batch_collection", collection_brief.collection_id]
            langfuse_handler = CallbackHandler()

            final_state = app.invoke(
                {"brief": chapter_brief, "previous_posters": previous_posters}, 
                config={
                    "configurable": {"thread_id": session_id},
                    "callbacks": [langfuse_handler],
                    "tags": tags,
                    "metadata": {"session_id": session_id}
                }
            )
            
            rendered_code = final_state.get("rendered_code")
            package = final_state.get("package")
            audit = final_state.get("audit")
            
            if not rendered_code or not rendered_code.html_content:
                print(f"[ORCHESTRATOR] ERRO: Pôster {poster_num} falhou na geração do HTML.")
                if audit:
                    print(f"[ORCHESTRATOR] Audit Status: {audit.status}")
                    print(f"[ORCHESTRATOR] Justification: {audit.justification}")
                    print(f"[ORCHESTRATOR] Violations: {audit.violations}")
                continue

            caption = package.caption if package else ""
            direction = final_state.get("direction")
            
            poster_summary = {
                "topic": chapter_brief.topic,
                "caption": caption,
                "aesthetic_mood": direction.aesthetic_mood if direction else "",
                "core_concept": direction.core_concept if direction else ""
            }
            previous_posters.append(poster_summary)

            # Save PNG via Renderer
            png_path = os.path.join(collection_path, f"poster_{poster_num}.png")
            
            # Assuming design_system path for resolving CSS tokens
            # Na arquitetura atual o design_system fica em 05_IMPLEMENTACAO/design_system
            base_dir = os.path.abspath(os.path.join(self.output_dir, "../design_system"))
            
            print(f"[ORCHESTRATOR] Renderizando {png_path} via Playwright...")
            self.renderer.render_to_png(rendered_code.html_content, png_path, base_dir=base_dir)
            
            # Save Caption
            txt_path = os.path.join(collection_path, f"poster_{poster_num}_caption.txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(caption)

            print(f"[ORCHESTRATOR] Pôster {poster_num} finalizado e salvo.")
            results.append({
                "poster_num": poster_num,
                "png_path": png_path,
                "txt_path": txt_path,
                "state": final_state
            })
            
        print(f"\n[ORCHESTRATOR] Coleção {collection_brief.collection_id} concluída com sucesso.")
        return results
