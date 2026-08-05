import os
import pytest
from unittest.mock import MagicMock
from eos.application.workflows.collection_orchestrator import CollectionOrchestrator
from eos.domain.contracts.collection_brief import CollectionBrief, ChapterBrief
from eos.domain.contracts.creative_direction import CreativeDirection
from eos.domain.contracts.publication_package import PublicationPackage
from eos.domain.contracts.rendered_code import RenderedCode
from eos.domain.collection_history import CollectionHistory

def test_process_collection_accumulates_previous_posters(tmp_path):
    # Arrange
    mock_workflow = MagicMock()
    mock_app = MagicMock()
    mock_workflow.build_app.return_value = mock_app

    # Set up mock final states for 3 iterations
    final_states = [
        {
            "package": PublicationPackage(caption="Caption 1", hashtags=["#test"], metadata={}),
            "direction": CreativeDirection(
                core_concept="Concept 1",
                editorial_intent="Intent 1",
                aesthetic_mood="Mood 1",
                references=[]
            ),
            "rendered_code": RenderedCode(html_content="<html>1</html>")
        },
        {
            "package": PublicationPackage(caption="Caption 2", hashtags=["#test"], metadata={}),
            "direction": CreativeDirection(
                core_concept="Concept 2",
                editorial_intent="Intent 2",
                aesthetic_mood="Mood 2",
                references=[]
            ),
            "rendered_code": RenderedCode(html_content="<html>2</html>")
        },
        {
            "package": PublicationPackage(caption="Caption 3", hashtags=["#test"], metadata={}),
            "direction": CreativeDirection(
                core_concept="Concept 3",
                editorial_intent="Intent 3",
                aesthetic_mood="Mood 3",
                references=[]
            ),
            "rendered_code": RenderedCode(html_content="<html>3</html>")
        }
    ]
    mock_app.invoke.side_effect = final_states

    collection_brief = CollectionBrief(
        collection_id="test_col_001",
        name="Test Collection",
        description="A test collection",
        chapters=[
            ChapterBrief(topic="Topic 1", objective="Obj 1", audience="Aud 1", constraints=[]),
            ChapterBrief(topic="Topic 2", objective="Obj 2", audience="Aud 2", constraints=[]),
            ChapterBrief(topic="Topic 3", objective="Obj 3", audience="Aud 3", constraints=[]),
        ]
    )

    orchestrator = CollectionOrchestrator(editorial_workflow=mock_workflow, output_dir=str(tmp_path))
    
    # Mock the exporter so we don't actually try to start Playwright
    orchestrator.exporter = MagicMock()
    orchestrator.exporter.export.return_value = ("mock_png.png", "mock_txt.txt")

    # Act
    results = orchestrator.process_collection(collection_brief)

    # Assert
    assert len(results) == 3
    assert mock_app.invoke.call_count == 3

    # Check the 1st call
    call_1_args = mock_app.invoke.call_args_list[0][0][0]
    history_1 = call_1_args["history"]
    assert len(history_1.posters) == 0

    # Check the 2nd call
    call_2_args = mock_app.invoke.call_args_list[1][0][0]
    history_2 = call_2_args["history"]
    assert len(history_2.posters) == 1
    assert history_2.posters[0].topic == "Topic 1"
    assert history_2.posters[0].caption == "Caption 1"
    assert history_2.posters[0].aesthetic_mood == "Mood 1"

    # Check the 3rd call
    call_3_args = mock_app.invoke.call_args_list[2][0][0]
    history_3 = call_3_args["history"]
    assert len(history_3.posters) == 2
    assert history_3.posters[1].topic == "Topic 2"
    assert history_3.posters[1].caption == "Caption 2"
    assert history_3.posters[1].aesthetic_mood == "Mood 2"
