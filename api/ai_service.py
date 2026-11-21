"""OpenAI Responses API 연동 - 컬러푸드 식생활 안내."""

import json
import os

from openai import AsyncOpenAI

from .config import AI_RESPONSE_SCHEMA, MODEL_NAME
from .prompt import build_prompt


async def call_openai(validated_input: dict) -> dict:
    """검증된 사용자 입력을 AI에 전달하고 JSON 객체를 반환한다."""
    api_key = os.getenv("AI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "AI_API_KEY 환경변수가 설정되어 있지 않습니다."
        )

    async with AsyncOpenAI(
        api_key=api_key,
        timeout=60.0,
        max_retries=0,
    ) as client:
        response = await client.responses.create(
            model=MODEL_NAME,
            input=build_prompt(validated_input),
            text={"format": AI_RESPONSE_SCHEMA},
            store=False,
        )

    if response.status != "completed":
        raise RuntimeError("AI 응답이 정상적으로 완료되지 않았습니다.")

    response_text = response.output_text
    if not response_text:
        raise ValueError("AI 응답에 결과 텍스트가 없습니다.")

    try:
        result = json.loads(response_text)
    except json.JSONDecodeError as error:
        raise ValueError("AI 응답을 JSON으로 해석할 수 없습니다.") from error

    if not isinstance(result, dict):
        raise ValueError("AI 응답이 JSON 객체 형식이 아닙니다.")

    return result
