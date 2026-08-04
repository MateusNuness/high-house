import sys
import os

# Ajustando o PYTHONPATH para encontrar o pacote 'eos' e 'tests'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../11_EDITORIAL_OS/05_IMPLEMENTACAO/src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../11_EDITORIAL_OS/05_IMPLEMENTACAO")))

from eos.application.workflows.editorial_creation import EditorialWorkflow
from eos.application.agents.memory_agent import MemoryAgentStub
from tests.fixtures.mock_research_agent import MockResearchAgent
from tests.fixtures.mock_editorial_agent import MockEditorialAgent
from tests.fixtures.mock_art_director_agent import MockArtDirectorAgent
from tests.fixtures.mock_designer_agent import MockDesignerAgent
from tests.fixtures.mock_brand_guardian_agent import MockBrandGuardianAgent
from tests.fixtures.mock_coder_agent import MockCoderAgent
from tests.fixtures.mock_vision_agent import MockVisionAgent
from tests.fixtures.mock_image_agent import MockImageAgent

def main():
    print("Instanciando Mocks...")
    research_mock = MockResearchAgent()
    editorial_mock = MockEditorialAgent()
    art_mock = MockArtDirectorAgent()
    designer_mock = MockDesignerAgent()
    guardian_mock = MockBrandGuardianAgent(scenario="approved")
    image_mock = MockImageAgent()
    coder_mock = MockCoderAgent()
    vision_mock = MockVisionAgent(scenario="approved")
    memory_stub = MemoryAgentStub()

    print("Instanciando Workflow...")
    workflow = EditorialWorkflow(
        research_agent=research_mock,
        editorial_agent=editorial_mock,
        art_director_agent=art_mock,
        designer_agent=designer_mock,
        brand_guardian_agent=guardian_mock,
        memory_agent=memory_stub,
        coder_agent=coder_mock,
        vision_agent=vision_mock,
        image_agent=image_mock
    )

    print("Compilando Grafo...")
    app = workflow.build_app()
    print("Grafo compilado com sucesso!")
    print(app)

if __name__ == "__main__":
    main()
