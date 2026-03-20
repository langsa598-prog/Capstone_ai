# ============================================================
# Request / Response 스키마 정의
# ============================================================

from pydantic import BaseModel
from typing import Optional, List


# ── /classify ───────────────────────────────────────────────
class EmailRequest(BaseModel):
    emailId: str
    threadId: Optional[str] = None
    from_addr: str           # 'from' 은 예약어라 from_addr 사용
    subject: str
    body: str

    # 온보딩 값 (백엔드에서 같이 넘겨줌 / 없으면 None)
    mail_tone: Optional[str] = None    # 예: "정중체"
    category: Optional[str] = None    # 예: "Finance"
    ragContext: Optional[str] = None  # 예: "저희 회사는 에코랩입니다."


class Top2Domain(BaseModel):
    domain: str
    confidence: float


class ClassifyResponse(BaseModel):
    emailId: str
    domain: str
    domain_confidence: float
    intent: str
    intent_confidence: float
    low_confidence: bool
    top2_domains: List[Top2Domain]
    domain_source: str             # "onboarding" or "classifier"


# ── /summarize (GPT) ────────────────────────────────────────
class SummarizeResponse(BaseModel):
    emailId: str
    summary: str
    schedule: Optional[dict] = None  # 일정 정보 추출 결과


# ── /draft (Claude) ─────────────────────────────────────────
class DraftResponse(BaseModel):
    emailId: str
    draft: str
