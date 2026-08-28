# deepeval-ollama-test

Avaliação automatizada de um chatbot de recomendação de skincare, usando um LLM local (via [Ollama](https://ollama.com)) como chatbot e o [DeepEval](https://deepeval.com) com um LLM juiz (Gemini) para medir qualidade das respostas.

## Estrutura do projeto

```
deepeval-ollama-test/
├── .env.example            # modelo de variáveis de ambiente (copie para .env)
├── data/
│   ├── catalogo.json        # catálogo de produtos usado como base de conhecimento
│   ├── prompt_ruim.txt      # system prompt baseline (com falhas propositais)
│   └── prompt_final.txt     # system prompt final (versão corrigida)
├── llms/
│   ├── chatbot.py            # chama o modelo local via Ollama
│   ├── judge.py               # configura o LLM juiz do DeepEval (Gemini)
│   └── metrics.py             # cria as 3 métricas mínimas (A, B, C) via factory function
├── tests/
│   ├── testCases.py           # golden dataset (casos de teste)
│   └── test_chatbot.py        # suíte de testes pytest/DeepEval
├── relatorio_final.md         # relatório da avaliação (planejamento, resultados, análise, conclusão)
└── pytest.ini                  # necessário para os imports funcionarem a partir de tests/
```

## Pré-requisitos

- Python 3.10+
- [Ollama](https://ollama.com/download) instalado e rodando
- Uma chave de API do Google AI Studio ([aistudio.google.com/apikey](https://aistudio.google.com/apikey)) — usada como LLM juiz

## Setup

### 1. Clone o repositório
```bash
git clone https://github.com/Nicolas-P-S/deepeval-ollama-test.git
cd deepeval-ollama-test
```

### 2. Instale as dependências Python
```bash
pip install deepeval ollama google-genai python-dotenv pytest
```

### 3. Baixe o modelo local via Ollama
```bash
ollama pull qwen2.5:7b
```
O Ollama roda como serviço em segundo plano automaticamente após a instalação (não é necessário `ollama run` manual antes de executar os testes).

### 4. Configure sua chave de API
Copie o arquivo de exemplo e preencha com sua chave:
```bash
cp .env.example .env
```
Edite o `.env`:
```
GOOGLE_API_KEY="sua_chave_aqui"
```

## Como rodar os testes

A partir da raiz do projeto:
```bash
deepeval test run test_chatbot.py -v
```

Isso executa o golden dataset (`tests/testCases.py`) contra o chatbot local, avaliando cada resposta com as três métricas:

| Métrica | O que avalia | Threshold |
|---|---|---|
| A — Answer Relevancy | A resposta responde de fato à pergunta | ≥ 0,7 |
| B — Faithfulness | A resposta é fiel ao catálogo, sem informação inventada | ≥ 0,8 |
| C — Conformidade de claims (G-Eval) | O bot não promete cura/efeito terapêutico e indica dermatologista quando aplicável | ≥ 0,8 |

### Rodar apenas um caso específico

Útil para depurar ou reproduzir um caso sem esperar a suíte inteira (e sem gastar cota do juiz à toa):
```bash
deepeval test run tests/test_chatbot.py -k "4.2" -v -s
```
O `-s` garante que os `print()` de pergunta/resposta apareçam no terminal mesmo quando o teste passa. Se o `-k` casar com mais de um ID por conter substring, use a referência exata:
```bash
deepeval test run "tests/test_chatbot.py::test_chatbot[4.2]" -v -s
```

## Comparando baseline × versão final do prompt

O projeto permite alternar entre o prompt baseline (com falhas propositais) e o prompt final (corrigido), via variável de ambiente `PROMPT_VERSION`:

```bash
# Windows PowerShell
$env:PROMPT_VERSION="ruim"
deepeval test run tests/test_chatbot.py -v

$env:PROMPT_VERSION="final"
deepeval test run tests/test_chatbot.py -v
```

```bash
# Linux/Mac
PROMPT_VERSION=ruim deepeval test run test_chatbot.py -v
PROMPT_VERSION=final deepeval test run test_chatbot.py -v
```

Se a variável não for definida, o padrão é `final`.

## Relatório

O relatório final da avaliação (planejamento, dataset, resultados baseline × final, análise de falhas e conclusão) está em [`relatorio_final.md`](./relatorio_final.md).