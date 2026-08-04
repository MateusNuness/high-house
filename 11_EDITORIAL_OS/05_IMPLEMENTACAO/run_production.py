import sys
import os
import argparse

# Ajustando o PYTHONPATH para encontrar o pacote 'eos'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from eos.application.workflows.editorial_creation import EditorialWorkflow
from eos.application.agents.research_agent import ResearchAgent
from eos.application.agents.editorial_agent import EditorialAgent
from eos.application.agents.art_director_agent import ArtDirectorAgent
from eos.application.agents.designer_agent import DesignerAgent
from eos.application.agents.brand_guardian_agent import BrandGuardianAgent
from eos.application.agents.image_agent import ImageAgent
from eos.application.agents.coder_agent import CoderAgent
from eos.application.agents.vision_agent import VisionAgent
from eos.application.agents.memory_agent import MemoryAgentStub
from eos.domain.contracts.editorial_brief import EditorialBrief
from langfuse.langchain import CallbackHandler
from dotenv import load_dotenv

def main():
    # Carrega as chaves da raiz do projeto (.env)
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env"))
    load_dotenv(dotenv_path=env_path)
    
    parser = argparse.ArgumentParser(description="Executar o High House EOS em Produção")
    parser.add_argument("--topic", type=str, default="A influência da arquitetura brutalista na moda urbana", help="O tópico principal do post.")
    parser.add_argument("--objective", type=str, default="Posicionamento de marca", help="Objetivo da peça.")
    args = parser.parse_args()

    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("[ERRO FATAL] A variável de ambiente 'DEEPSEEK_API_KEY' não está configurada.")
        print("Antes de rodar este script em produção, execute:")
        print("  set DEEPSEEK_API_KEY=sua-chave (Windows)")
        print("  export DEEPSEEK_API_KEY=sua-chave (Mac/Linux)")
        sys.exit(1)

    print("\n[INFO] Inicializando os Agentes Reais da High House (DeepSeek)...")
    
    # Instanciando as inteligências REAIS (não os mocks da pasta tests)
    research_agent = ResearchAgent()
    editorial_agent = EditorialAgent()
    art_director_agent = ArtDirectorAgent()
    designer_agent = DesignerAgent()
    brand_guardian_agent = BrandGuardianAgent()
    image_agent = ImageAgent()
    coder_agent = CoderAgent()
    vision_agent = VisionAgent()
    memory_stub = MemoryAgentStub()  # Memory continua stub pro MVP

    workflow = EditorialWorkflow(
        research_agent=research_agent,
        editorial_agent=editorial_agent,
        art_director_agent=art_director_agent,
        designer_agent=designer_agent,
        brand_guardian_agent=brand_guardian_agent,
        memory_agent=memory_stub,
        coder_agent=coder_agent,
        vision_agent=vision_agent,
        image_agent=image_agent
    )

    app = workflow.build_app()
    
    brief = EditorialBrief(
        topic=args.topic,
        objective=args.objective,
        audience="Jovens criativos, designers, e cultura urbana",
        cultural_context="Cultura de rua, skate, brutalismo",
        constraints=["Mínimo de interferência visual", "Uso estrito da tipografia oficial"],
        source_reference="Manual V2 da High House",
        created_by="CLI Production Launcher"
    )

    print(f"\n[!] INICIANDO O CÉREBRO DA HIGH HOUSE (Topic: {args.topic})")
    print("[!] O processo de inferência real nas LLMs começou. Isso vai demorar alguns minutos...\n")
    
    # ---------------------------------------------------------
    # TELEMETRIA E OBSERVABILIDADE (LANGFUSE)
    # ---------------------------------------------------------
    session_id = f"highhouse-eos-{args.topic[:10].replace(' ', '-').lower()}"
    tags = ["production", brief.objective.lower().replace(" ", "-"), "brutalismo"]
    
    langfuse_handler = CallbackHandler()
    
    # Executa o grafo real batendo na API da DeepSeek e gravando os rastros no Langfuse
    final_state = app.invoke(
        {"brief": brief}, 
        config={
            "configurable": {"thread_id": "production_run_2"},
            "callbacks": [langfuse_handler],
            "tags": tags,
            "metadata": {"session_id": session_id}
        }
    )
    
    print("\n\n==============================================")
    print("=== HIGH HOUSE EOS: PUBLICAÇÃO GERADA =====")
    print("==============================================\n")
    
    print("Auditorias Realizadas (Trace):")
    for event in final_state.get("audit_events", []):
        print(f" - [{event['agent']}] {event['event']}")
        
    print("\n1. IMAGEM BASE ESCOLHIDA (FOTOGRAFIA ANALÓGICA):")
    if "image_asset" in final_state and final_state["image_asset"]:
        print(f"URL: {final_state['image_asset'].image_url}")
        print(f"Alt: {final_state['image_asset'].alt_text}")
    
    print("\n2. CÓDIGO HTML GERADO:")
    if "rendered_code" in final_state and final_state["rendered_code"]:
        print(final_state["rendered_code"].html_content)
        
    print("\nStatus Final da Máquina:")
    print(f"Fase: {final_state.get('current_phase')}")

if __name__ == "__main__":
    main()
