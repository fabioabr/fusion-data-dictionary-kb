---
id: DOC-PO-053
doc_type: system-doc
title: "POQ_QUESTION_SCORES — Regras de Pontuação de Perguntas de Qualificação"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - qualificacao
  - scoring
  - pontuacao
aliases:
  - POQ_QUESTION_SCORES
  - poq_question_scores
  - pontuacao-perguntas-qualificacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTION_SCORES

## 📌 Visão Geral

Armazena as **regras de pontuação** (scoring rules) associadas às perguntas de questionários de qualificação de fornecedores. Define como cada resposta possível deve ser pontuada, estabelecendo os critérios para avaliação automática. Cada registro mapeia um valor ou faixa de resposta a uma pontuação específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Pontuação automática:** Definição de scores por resposta para cálculo automático de notas.
- **Critérios de qualificação:** Estabelecimento de pontuações mínimas para aprovação/reprovação de fornecedores.
- **Ranking de fornecedores:** Comparação objetiva entre fornecedores com base em pontuações padronizadas.
- **Configuração de avaliações:** Setup das regras de scoring durante a criação de questionários.
- **Auditoria de processo:** Rastreabilidade dos critérios aplicados em cada avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_SCORE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da regra de pontuação | — | 🟡 75% |
| 2 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Pergunta à qual a regra de pontuação se aplica | [[poq_questions_vl]] | 🟡 75% |
| 3 | RESPONSE_VALUE | VARCHAR2(4000) | NULL | Dados | Valor de resposta que aciona esta pontuação | — | 🟡 70% |
| 4 | SCORE | NUMBER | NOT NULL | Pontuação | Pontuação atribuída quando a resposta corresponde | — | 🟡 75% |
| 5 | MIN_VALUE | NUMBER | NULL | Dados | Valor mínimo da faixa (para respostas numéricas) | — | 🟡 60% |
| 6 | MAX_VALUE | NUMBER | NULL | Dados | Valor máximo da faixa (para respostas numéricas) | — | 🟡 60% |
| 7 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição das opções de pontuação | — | 🟡 65% |
| 8 | SCORE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de regra: EXACT_MATCH, RANGE, CONTAINS | — | 🟡 60% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questions_vl]] — via `QUESTION_ID` (pergunta associada)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Regras de pontuação por pergunta
```sql
SELECT qs.QUESTION_SCORE_ID,
       qs.RESPONSE_VALUE,
       qs.SCORE,
       qs.MIN_VALUE,
       qs.MAX_VALUE,
       qs.SCORE_TYPE
FROM   POQ_QUESTION_SCORES qs
WHERE  qs.QUESTION_ID = :p_question_id
ORDER BY qs.DISPLAY_ORDER;
```

### Perguntas com pontuação máxima alta
```sql
SELECT qs.QUESTION_ID,
       MAX(qs.SCORE) AS max_score_possivel,
       COUNT(*) AS total_regras
FROM   POQ_QUESTION_SCORES qs
GROUP BY qs.QUESTION_ID
HAVING MAX(qs.SCORE) > 10;
```

---

## 🔒 Observações

- O campo `SCORE_TYPE` determina como a resposta é comparada: **EXACT_MATCH** (correspondência exata), **RANGE** (faixa numérica via `MIN_VALUE`/`MAX_VALUE`), **CONTAINS** (contém substring).
- Para perguntas do tipo SINGLE_CHOICE ou MULTI_CHOICE, cada opção de resposta terá um registro com seu `RESPONSE_VALUE` e `SCORE` correspondente.
- Para perguntas numéricas (NUMBER), as faixas `MIN_VALUE`/`MAX_VALUE` definem intervalos de pontuação.
- O score final de uma qualificação é tipicamente calculado como média ponderada dos scores individuais, usando o `WEIGHT` definido em [[poq_questions_vl]].

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
