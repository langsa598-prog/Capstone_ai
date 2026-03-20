# ============================================================
# /draft 엔드포인트 (Claude 연동 - Step 2에서 구현 예정)
# ============================================================

from fastapi import APIRouter, HTTPException
from api.schemas import EmailRequest, DraftResponse

router = APIRouter()


@router.post("/draft", response_model=DraftResponse)
async def draft_email(payload: EmailRequest):
    """
    Claude 답장 초안 생성 엔드포인트
    TODO: Step 2 - Claude API 연동 시 구현
    ragContext + mail_tone + category → 프롬프트 생성 → Claude 호출
    """
    # 임시 응답 (Claude 연동 전 테스트용)
    return DraftResponse(
        emailId=payload.emailId,
        draft="[Claude 연동 전 - 임시 응답]",
    )
