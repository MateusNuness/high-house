from eos.domain.contracts.base import AuditStatus
from eos.domain.state import GlobalState


class GuardianDecisionPolicy:
    """
    Policy de decisão do workflow pós-Brand Guardian.
    
    Responsabilidade única: decidir para qual nó o workflow deve transitar
    com base no resultado da auditoria e no número de revisões.
    
    O Guardian apenas JULGA. Quem decide o FLUXO é esta Policy.
    Isso mantém a separação entre domínio (BrandAuditReport) e 
    orquestração (routing do LangGraph).
    
    Regras:
        - APPROVED → human_approval
        - HUMAN_REVIEW_REQUIRED → human_approval
        - APPROVED_WITH_CHANGES (revisão < MAX) → designer (loop)
        - REJECTED (revisão < MAX) → designer (loop)
        - Qualquer status (revisão >= MAX) → human_approval (escalonamento)
    """
    
    MAX_REVISIONS = 3
    
    # Nomes dos nós no LangGraph
    NODE_HUMAN_APPROVAL = "agent_human_approval"
    NODE_DESIGNER = "agent_designer"
    NODE_CODER = "agent_coder"
    
    @classmethod
    def route(cls, state: GlobalState) -> str:
        """
        Determina o próximo nó do workflow com base no BrandAuditReport
        e no revision_count do state.
        
        Returns:
            Nome do nó LangGraph para onde transitar.
        """
        audit = state.get("audit")
        revision_count = state.get("revision_count", 0)
        
        # Sem audit report → fail-secure para human
        if audit is None:
            return cls.NODE_HUMAN_APPROVAL
        
        status = audit.status
        
        # Aprovação direta → coder
        if status == AuditStatus.APPROVED:
            return cls.NODE_CODER
        
        # Escalonamento explícito → human review
        if status == AuditStatus.HUMAN_REVIEW_REQUIRED:
            return cls.NODE_HUMAN_APPROVAL
        
        # Limite de revisões atingido → escalonar para human
        if revision_count >= cls.MAX_REVISIONS:
            return cls.NODE_HUMAN_APPROVAL
        
        # REJECTED ou APPROVED_WITH_CHANGES com revisões restantes → designer
        if status in (AuditStatus.REJECTED, AuditStatus.APPROVED_WITH_CHANGES):
            return cls.NODE_DESIGNER
        
        # Fallback seguro
        return cls.NODE_HUMAN_APPROVAL
