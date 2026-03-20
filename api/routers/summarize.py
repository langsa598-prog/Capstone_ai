# ============================================================
# /summarize 엔드포인트 (GPT 연동 - Step 1에서 구현 예정)
# ============================================================

from fastapi import APIRouter, HTTPException
from api.schemas import EmailRequest, SummarizeResponse

router = APIRouter()


@router.post("/summarize", response_model=SummarizeResponse)
async def summarize_email(payload: EmailRequest):
    """
    GPT 이메일 요약 + 일정 추출 엔드포인트
    TODO: Step 1 - GPT API 연동 시 구현
    """
    # 임시 응답 (GPT 연동 전 테스트용)
    return SummarizeResponse(
        emailId=payload.emailId,
        summary="[GPT 연동 전 - 임시 응답]",
        schedule=None,
    )
