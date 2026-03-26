---
id: DOC-HCM-187
doc_type: system-doc
title: "HRQ_QSTNR_QUESTIONS — Questões de Questionários"
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
  - HRQ_QSTNR_QUESTIONS
  - hrq_qstnr_questions
  - questões-de-questionários
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTNR_QUESTIONS

## 📌 Visão Geral

Tabela de relacionamento: **questões vinculadas a questionários**.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Composição:** Quais perguntas em cada questionário.
- **Ordenação:** Sequência das questões.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QSTNR_QUESTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 90% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Questão | [[hrq_questions_b]] | 🟢 90% |
| 4 | SECTION_ID | NUMBER(18) | NULL | FK | Seção | [[hrq_qstnr_sections_b]] | 🟡 80% |
| 5 | SEQUENCE_NUMBER | NUMBER | NULL | Ordenação | Ordem | — | 🟡 75% |
| 6 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Controle | Obrigatória (Y/N) | — | 🟡 70% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai

---

## 📎 Uso Típico

### Questões de um questionário
```sql
SELECT qq.QUESTION_ID, qq.SEQUENCE_NUMBER, qq.MANDATORY_FLAG
FROM   HRQ_QSTNR_QUESTIONS qq
WHERE  qq.QUESTIONNAIRE_ID = :p_id
ORDER BY qq.SEQUENCE_NUMBER;
```

---

## 🔒 Observações

- Relacionamento N:N.
- `MANDATORY_FLAG = 'Y'` = resposta obrigatória.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
