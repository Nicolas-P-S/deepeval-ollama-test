import json
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from tests.testCases import test_cases
from llms.metrics import faithfulness, answer_relevancy, geval
from llms.chatbot import perguntar_chat


def preparar_contexto(contexto):
    if isinstance(contexto, list):
        return [
            json.dumps(item, ensure_ascii=False)
            if isinstance(item, dict)
            else str(item)
            for item in contexto
        ]

    if isinstance(contexto, dict):
        return [
            json.dumps(contexto, ensure_ascii=False)
        ]

    return [str(contexto)]

# TESTES

@pytest.mark.parametrize("case", test_cases, ids=[case["id"] for case in test_cases])
def test_chatbot(case):
    quest = case["input"]
    res = perguntar_chat(quest)

    print(f"\nCASO: {case['id']}")
    print(f"PERGUNTA: {quest}")
    print(f"RESPOSTA: {res}\n")

    context = preparar_contexto(case["contexto"])

    test_case = LLMTestCase(
        input=quest,
        actual_output=res,
        retrieval_context=context
    )

    assert_test(
        test_case,
        [
            answer_relevancy,
            faithfulness,
            geval
        ],
        run_async=False
    )