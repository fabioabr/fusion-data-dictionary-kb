---
id: DOC-HCM-181
doc_type: system-doc
title: "HRQ_ALL_QSTN_RESPONSES_V — Todas as Respostas de Questionários — Visão"
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
  - responses
aliases:
  - HRQ_ALL_QSTN_RESPONSES_V
  - hrq_all_qstn_responses_v
  - todas-as-respostas-de-questionáriosvisão
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_ALL_QSTN_RESPONSES_V

## 📌 Visão Geral

View consolidada de **todas as respostas de questionários** HCM.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Análise:** Todas as respostas em uma view.
- **Relatórios:** Resultados de questionários.
- **BI/Analytics:** Dashboards de feedback.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 85% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Questão | [[hrq_questions_b]] | 🟢 85% |
| 4 | PARTICIPANT_ID | NUMBER(18) | NOT NULL | FK | Participante | [[hrq_qstnr_participants]] | 🟢 85% |
| 5 | ANSWER_VALUE | VARCHAR2(4000) | NULL | Dados | Valor da resposta | — | 🟡 75% |
| 6 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa | [[per_all_people_f]] | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai

---

## 📎 Uso Típico

### Respostas de um questionário
```sql
SELECT r.QUESTION_ID, r.ANSWER_VALUE, r.PERSON_ID
FROM   HRQ_ALL_QSTN_RESPONSES_V r
WHERE  r.QUESTIONNAIRE_ID = :p_id;
```

---

## 🔒 Observações

- View consolidada (sufixo `_V`).

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
