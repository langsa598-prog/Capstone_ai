# ============================================================
# /classify 엔드포인트
# inference.py의 predict_email() 을 FastAPI에 연결
# ============================================================

from fastapi import APIRouter, HTTPException, Request

from api.schemas import EmailRequest, ClassifyResponse

router = APIRouter()


def preprocess_email(subject: str, body: str) -> str:
    """subject + body 합쳐서 email_text 생성"""
    return f"{subject}\n{body}".strip()


@router.post("/classify", response_model=ClassifyResponse)
async def classify_email(payload: EmailRequest, request: Request):
    """
    이메일 분류 엔드포인트

    - SBERT 임베딩 → Domain 분류 → Intent 분류
    - 온보딩 category 있으면 Domain 분류 스킵
    """
    try:
        # app.state에서 파이프라인 꺼내기 (main.py에서 로드됨)
        pipeline = request.app.state.pipeline

        # 1. 전처리
        email_text = preprocess_email(payload.subject, payload.body)

        # 2. 추론 (inference.py의 predict_email 호출)
        result = pipeline["predict"](
            email_text=email_text,
            pipeline=pipeline["model"],
            user_domain=payload.category,  # 온보딩 카테고리 전달
        )

        return ClassifyResponse(
            emailId=payload.emailId,
            **result
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
