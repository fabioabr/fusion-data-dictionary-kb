---
id: DOC-HCM-196
doc_type: system-doc
title: "HRQ_QUESTIONS_B — Questões de Questionários (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - questionnaires
  - questions
aliases:
  - HRQ_QUESTIONS_B
  - hrq_questions_b
  - questões-de-questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QUESTIONS_B

## 📌 Visão Geral

Tabela base das **questões (perguntas)** do módulo de questionários. Reutilizáveis em múltiplos questionários.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Banco de questões:** Perguntas reutilizáveis.
- **Tipificação:** Tipos de questão (texto, múltipla escolha, escala).

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | QUESTION_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟡 80% |
| 3 | QUESTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (TEXT, SINGLE_CHOICE, MULTI_CHOICE, SCALE) | — | 🟡 80% |
| 4 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[hrq_categories_b]] | 🟡 70% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Questões por tipo
```sql
SELECT q.QUESTION_ID, q.QUESTION_CODE, q.QUESTION_TYPE
FROM   HRQ_QUESTIONS_B q
WHERE  q.QUESTION_TYPE = 'SINGLE_CHOICE';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_questions_tl]].
`QUESTION_TYPE` determina formato de resposta.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
