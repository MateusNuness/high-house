from enum import Enum
from pydantic import BaseModel

class AuditStatus(str, Enum):
    APPROVED = 'APPROVED'
    APPROVED_WITH_CHANGES = 'APPROVED_WITH_CHANGES'
    REJECTED = 'REJECTED'
    HUMAN_REVIEW_REQUIRED = 'HUMAN_REVIEW_REQUIRED'
