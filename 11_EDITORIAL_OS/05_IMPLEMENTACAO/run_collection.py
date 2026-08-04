import sys
import os
import argparse

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from eos.application.workflows.editorial_creation import EditorialWorkflow
from eos.application.workflows.collection_orchestrator import CollectionOrchestrator
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
from eos.domain.contracts.collection_brief import CollectionBrief
from dotenv import load_dotenv

def main():
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env"))
    load_dotenv(dotenv_path=env_path)
    
    parser = argparse.ArgumentParser(description="Executar Lote de Coleção - High House EOS")
    parser.add_argument("--collection", type=str, default="001_manifesto", help="O ID da coleção para gerar.")
    args = parser.parse_args()

    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("[ERRO FATAL] A variável de ambiente 'DEEPSEEK_API_KEY' não está configurada.")
        sys.exit(1)

    print("\n[INFO] Inicializando os Agentes Reais da High House (DeepSeek)...")
    
    research_agent = ResearchAgent()
    editorial_agent = EditorialAgent()
    art_director_agent = ArtDirectorAgent()
    designer_agent = DesignerAgent()
    brand_guardian_agent = BrandGuardianAgent()
    image_agent = ImageAgent()
    coder_agent = CoderAgent()
    vision_agent = VisionAgent()
    memory_stub = MemoryAgentStub()

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

    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "collections"))
    orchestrator = CollectionOrchestrator(editorial_workflow=workflow, output_dir=output_dir)
    
    if args.collection == "001_manifesto":
        collection_brief = CollectionBrief(
            collection_id="001_manifesto",
            name="Coleção 001: O Manifesto",
            description="A coleção fundacional da marca, focada na essência brutalista e material.",
            chapters=[
                EditorialBrief(
                    topic="Pôster 1: Impacto Visual (Textura de concreto ou tipografia bruta)",
                    objective="Afirmação estética e filosófica, estabelecendo a materialidade sem clichês.",
                    audience="Jovens criativos e cultura urbana",
                    cultural_context="Brutalismo, arquitetura urbana, ruído",
                    constraints=["Mínimo de interferência visual", "Uso estrito da tipografia oficial", "Nenhuma call to action"],
                    source_reference="Manifesto da High House",
                    created_by="CLI Batch Launcher"
                ),
                EditorialBrief(
                    topic="Pôster 2: O Contraste (Xarpi como arte premium)",
                    objective="Validar a cultura de rua através de uma ótica acadêmica/premium.",
                    audience="Jovens criativos e cultura urbana",
                    cultural_context="Pichação, xarpi, arte marginal, galeria",
                    constraints=["Texto denso e maduro", "Legitimar o xarpi", "Nenhum humor forçado"],
                    source_reference="Manifesto da High House",
                    created_by="CLI Batch Launcher"
                ),
                EditorialBrief(
                    topic="Pôster 3: O Objeto de Desejo (Hospitalidade material)",
                    objective="Introduzir a convivência e o ritual através de um objeto estético denso.",
                    audience="Jovens criativos e cultura urbana",
                    cultural_context="Hospitalidade, mesa, café, tempo",
                    constraints=["Foco na materialidade do objeto", "Tom provocador sobre o tempo"],
                    source_reference="Manifesto da High House",
                    created_by="CLI Batch Launcher"
                )
            ]
        )
    elif args.collection == "001_poster1":
        collection_brief = CollectionBrief(
            collection_id="001_poster1",
            name="Coleção 001 (Apenas Pôster 1)",
            description="A coleção fundacional da marca - Primeiro Pôster apenas.",
            chapters=[
                EditorialBrief(
                    topic="Pôster 1: Impacto Visual (Textura de concreto ou tipografia bruta)",
                    objective="Afirmação estética e filosófica, estabelecendo a materialidade sem clichês.",
                    audience="Jovens criativos e cultura urbana",
                    cultural_context="Brutalismo, arquitetura urbana, ruído",
                    constraints=["Mínimo de interferência visual", "Uso estrito da tipografia oficial", "Nenhuma call to action"],
                    source_reference="Manifesto da High House",
                    created_by="CLI Batch Launcher"
                )
            ]
        )
    else:
        print(f"[ERRO] A Coleção '{args.collection}' não está mapeada no launcher ainda.")
        sys.exit(1)

    print(f"\n[!] INICIANDO O MOTOR DE RENDERING EM LOTE PARA: {collection_brief.name}")
    print("[!] O processo iterará pelos pôsteres e salvará os PNGs finais. Isso vai demorar alguns minutos...\n")
    
    orchestrator.process_collection(collection_brief)

if __name__ == "__main__":
    main()
