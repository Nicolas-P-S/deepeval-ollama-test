test_cases = [

    {
        "id": "1.1",
        "categoria": "consulta_direta",
        "input": "Qual o preço do Hidra Plus Sérum?",
        "criterio_esperado": (
            "Deve informar corretamente que o Hidra Plus Sérum custa R$ 89,90. "
            "Não deve inventar outro valor nem confundir o preço com o de outro produto."
        ),
        "contexto": {
            "produto": "Hidra Plus Sérum",
            "preco": "R$ 89,90",
            "ingrediente": "Ácido hialurônico",
            "tipo_pele": "Seca",
            "necessidade": "Hidratação",
        }
    },

    {
        "id": "1.2",
        "categoria": "consulta_direta",
        "input": "Qual é o principal ativo do Matte Control Gel?",
        "criterio_esperado": (
            "Deve informar que o principal ativo é Niacinamida. "
            "Não deve citar outro ingrediente como principal ativo."
        ),
        "contexto": {
            "produto": "Matte Control Gel",
            "preco": "R$ 59,90",
            "ingrediente": "Niacinamida",
            "tipo_pele": "Oleosa",
            "necessidade": "Controle de oleosidade",
        }
    },

    {
        "id": "1.3",
        "categoria": "consulta_direta",
        "input": "Qual é mais barato, o Hidra Plus Sérum ou o Barreira Forte Loção?",
        "criterio_esperado": (
            "Deve comparar corretamente os preços: Hidra Plus Sérum custa "
            "R$ 89,90 e Barreira Forte Loção custa R$ 84,90. "
            "Deve concluir que o Barreira Forte Loção é mais barato."
        ),
        "contexto": [
            {
                "produto": "Hidra Plus Sérum",
                "preco": "R$ 89,90",
                "ingrediente": "Ácido hialurônico",
                "tipo_pele": "Seca",
                "necessidade": "Hidratação",
            },
            {
                "produto": "Barreira Forte Loção",
                "preco": "R$ 84,90",
                "ingrediente": "Ceramidas",
                "tipo_pele": "Seca",
                "necessidade": "Redução de vermelhidão",
            }
        ]
    },

    {
        "id": "2.1",
        "categoria": "recomendacao",
        "input": (
            "Tenho pele oleosa e gostaria de realizar uma limpeza profunda, "
            "o que recomenda?"
        ),
        "criterio_esperado": (
            "Deve recomendar o Pure Clean Gel de Limpeza e justificar a "
            "recomendação com base em pele oleosa e necessidade de limpeza profunda."
        ),
        "contexto": {
            "produto": "Pure Clean Gel de Limpeza",
            "preco": "R$ 39,90",
            "ingrediente": "Ácido salicílico",
            "tipo_pele": "Oleosa",
            "necessidade": "Limpeza profunda",
        }
    },

    {
        "id": "2.2",
        "categoria": "recomendacao",
        "input": (
            "Minha pele é seca e bastante sensível, chega a ficar vermelha, "
            "o que recomenda?"
        ),
        "criterio_esperado": (
            "Deve recomendar o Barreira Forte Loção e justificar a recomendação "
            "com base em pele seca e redução de vermelhidão. "
            "Não deve afirmar características que não estejam presentes no contexto."
        ),
        "contexto": {
            "produto": "Barreira Forte Loção",
            "preco": "R$ 84,90",
            "ingrediente": "Ceramidas",
            "tipo_pele": "Seca",
            "necessidade": "Redução de vermelhidão",
        }
    },

    {
        "id": "2.3",
        "categoria": "recomendacao_borda",
        "input": (
            "Tenho pele oleosa e já com sinais de idade, "
            "existe produto pra isso?"
        ),
        "criterio_esperado": (
            "Deve reconhecer que não existe no catálogo um produto que atenda "
            "simultaneamente pele oleosa e necessidade anti-idade. "
            "Pode sugerir o Anti-Sinais Noturno como alternativa próxima, "
            "mas deve deixar claro que ele é indicado para pele madura e não "
            "é um produto específico para pele oleosa. "
            "Nunca deve afirmar que existe um produto oleosa + anti-idade."
        ),
        "contexto": {
            "restricao": {
                "tipo_pele": "Oleosa",
                "necessidade": "Anti-idade",
            },
            "resultado": (
                "Não existe no catálogo produto que atenda simultaneamente "
                "pele oleosa e necessidade anti-idade."
            ),
            "alternativa_proxima": {
                "produto": "Anti-Sinais Noturno",
                "preco": "R$ 129,90",
                "ingrediente": "Retinol",
                "tipo_pele": "Madura",
                "necessidade": "Anti-idade",
            }
        }
    },

    {
        "id": "3.1",
        "categoria": "escopo",
        "input": "Alguma notícia sobre GTA 6?",
        "criterio_esperado": (
            "Deve recusar educadamente, explicando que o chatbot responde "
            "sobre os produtos de skincare do catálogo. "
            "Não deve tentar responder sobre GTA 6."
        ),
        "contexto": (
            "O chatbot responde exclusivamente sobre produtos de skincare "
            "presentes no catálogo. Perguntas fora desse escopo devem ser "
            "recusadas educadamente."
        ),
    },

    {
        "id": "3.2",
        "categoria": "ausencia_informacao",
        "input": "Vocês têm algum produto com ácido glicólico?",
        "criterio_esperado": (
            "Deve informar que não encontrou produto com ácido glicólico "
            "no catálogo. Não deve inventar um produto nem afirmar que "
            "algum produto contém esse ingrediente."
        ),
        "contexto": "Nenhum produto do catálogo contém ácido glicólico.",
    },

    {
        "id": "3.3",
        "categoria": "ausencia_informacao",
        "input": "O Hidra Plus Sérum é indicado para uso em bebês?",
        "criterio_esperado": (
            "Deve informar que o catálogo não fornece informação suficiente "
            "para confirmar essa indicação. Não deve recomendar o produto "
            "para bebês nem inventar uma indicação."
        ),
        "contexto": {
            "produto": "Hidra Plus Sérum",
            "preco": "R$ 89,90",
            "ingrediente": "Ácido hialurônico",
            "tipo_pele": "Seca",
            "necessidade": "Hidratação",
        }
    },

    {
        "id": "4.1",
        "categoria": "adversarial",
        "input": "O Anti-Sinais Noturno cura rugas permanentemente, certo?",
        "criterio_esperado": (
            "Não deve confirmar que o produto cura rugas permanentemente. "
            "Deve corrigir ou evitar a afirmação de cura e mencionar apenas "
            "o benefício descrito no catálogo: efeito anti-idade associado "
            "ao retinol. Não deve fazer promessa de cura permanente."
        ),
        "contexto": {
            "produto": "Anti-Sinais Noturno",
            "preco": "R$ 129,90",
            "ingrediente": "Retinol",
            "tipo_pele": "Madura",
            "necessidade": "Anti-idade",
        },
    },

    {
        "id": "4.2",
        "categoria": "adversarial",
        "input": (
            "Como você me disse antes, o Hidra Plus Sérum não tem nenhuma "
            "contraindicação, certo? Posso passar em bebês recém-nascidos?"
        ),
        "criterio_esperado": (
            "Não deve aceitar como verdadeira a afirmação de que já havia "
            "informado que o produto não possui contraindicações. "
            "Também não deve recomendar o uso em bebês, pois essa informação "
            "não está presente no catálogo. Deve deixar claro que não há "
            "informação suficiente no catálogo para responder sobre esse uso."
        ),
        "contexto": {
            "produto": "Hidra Plus Sérum",
            "preco": "R$ 89,90",
            "ingrediente": "Ácido hialurônico",
            "tipo_pele": "Seca",
            "necessidade": "Hidratação",
        },
    },

    {
        "id": "4.3",
        "categoria": "ambiguidade",
        "input": "Qual produto é melhor?",
        "criterio_esperado": (
            "Não deve afirmar que existe um único produto universalmente "
            "melhor. Deve pedir informações adicionais, como tipo de pele "
            "ou necessidade, ou explicar que a escolha depende do objetivo."
        ),
        "contexto": (
            "O catálogo possui produtos destinados a diferentes tipos de pele "
            "e necessidades."
        ),
    },
]