import uuid
from typing import TypedDict, Optional, Literal
from langgraph.graph import StateGraph, START, END

from eos.domain.contracts import (
    EditorialBrief,
    ResearchReport,
    CreativeDirection,
    VisualProposal,
    BrandAuditReport,
    PublicationPackage,
    AuditStatus
)

class GlobalState(TypedDict):
    execution_id: str
    current_phase: str
    audit_log: list[str]
    
    # Artifacts as separated states
    brief: Optional[EditorialBrief]
    research: Optional[ResearchReport]
    direction: Optional[CreativeDirection]
    proposal: Optional[VisualProposal]
    audit: Optional[BrandAuditReport]
    package: Optional[PublicationPackage]

def research_node(state: GlobalState) -> GlobalState:
    brief = state.get("brief")
    if not brief:
        raise ValueError("Research Node requires an EditorialBrief")
    
    # Mocking Research Agent
    report = ResearchReport(
        research_question=f"What is the cultural relevance of {brief.topic}?",
        methodology="Mocked Web Search",
        sources=["https://mock-underground-source.com"],
        cultural_hypotheses=["The theme resonates with rebellion."],
        key_findings=[f"{brief.topic} is trending in urban spaces."],
        cultural_relevance="High",
        limitations="Limited data on recent weeks.",
        confidence_score=0.85
    )
    
    state["research"] = report
    state["current_phase"] = "research_completed"
    state["audit_log"].append("Research completed")
    return state

def editorial_node(state: GlobalState) -> GlobalState:
    report = state.get("research")
    if not report:
        raise ValueError("Editorial Node requires a ResearchReport")
    
    # Mocking Editorial Agent
    direction = CreativeDirection(
        core_concept="Raw expression of urban life",
        editorial_intent="Agressive yet poetic",
        desired_emotion="Tension and awe",
        aesthetic_mood="Gritty, dark, chaotic",
        cultural_reference="90s graffiti culture",
        strategic_alignment="Aligns with High House subversive nature",
        references=["https://mock-moodboard.com/1"]
    )
    
    state["direction"] = direction
    state["current_phase"] = "editorial_completed"
    state["audit_log"].append("Creative Direction established")
    return state

def designer_node(state: GlobalState) -> GlobalState:
    direction = state.get("direction")
    if not direction:
        raise ValueError("Designer Node requires a CreativeDirection")
    
    # Mocking Designer Agent
    proposal = VisualProposal(
        grid_structure="Asymmetric brutalist grid",
        visual_elements=["Halftone textures", "Distorted typography"],
        color_palette=["#000000", "#FFFFFF", "#FF0033"],
        typography_spec="Space Grotesk primary, custom distortion secondary",
        generation_prompt="A gritty urban scene with high contrast and noise",
        implementation_notes="Apply noise filter overlay at 15% opacity"
    )
    
    state["proposal"] = proposal
    state["current_phase"] = "design_completed"
    state["audit_log"].append("Visual Proposal generated")
    return state

def brand_guardian_node(state: GlobalState) -> GlobalState:
    proposal = state.get("proposal")
    if not proposal:
        raise ValueError("Brand Guardian Node requires a VisualProposal")
    
    # Mocking Brand Guardian
    audit = BrandAuditReport(
        status=AuditStatus.APPROVED,
        evaluated_rules=["No SaaS aesthetics", "Must have tension"],
        violations=[],
        severity="None",
        justification="The proposal meets the gritty criteria.",
        audit_context="Initial design review",
        recommendations=[]
    )
    
    state["audit"] = audit
    state["current_phase"] = "audit_completed"
    state["audit_log"].append("Brand Audit completed")
    return state

def human_approval_node(state: GlobalState) -> GlobalState:
    audit = state.get("audit")
    if not audit:
        raise ValueError("Human Approval Node requires a BrandAuditReport")
    
    # Mocking Final Package Generation after "Human Approval"
    package = PublicationPackage(
        final_copy="Here is the final gritty copy.",
        image_assets=["/assets/final_render_1.png"],
        caption="Embracing the chaos. #HighHouse",
        metadata={"platform": "instagram"}
    )
    
    state["package"] = package
    state["current_phase"] = "publication_ready"
    state["audit_log"].append("Publication Package generated")
    return state


# Build the Graph
workflow = StateGraph(GlobalState)

workflow.add_node("agent_research", research_node)
workflow.add_node("agent_editorial", editorial_node)
workflow.add_node("agent_designer", designer_node)
workflow.add_node("agent_brand_guardian", brand_guardian_node)
workflow.add_node("agent_human_approval", human_approval_node)

workflow.add_edge(START, "agent_research")
workflow.add_edge("agent_research", "agent_editorial")
workflow.add_edge("agent_editorial", "agent_designer")
workflow.add_edge("agent_designer", "agent_brand_guardian")
workflow.add_edge("agent_brand_guardian", "agent_human_approval")
workflow.add_edge("agent_human_approval", END)

# Compile
app = workflow.compile()
