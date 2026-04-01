---
id: DOC-HCM-185
doc_type: system-doc
title: "HRQ_QSTNR_ANSWERS — Respostas de Questionários"
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
  - answers
aliases:
  - HRQ_QSTNR_ANSWERS
  - hrq_qstnr_answers
  - respostas-de-questionários
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTNR_ANSWERS

## 📌 Visão Geral

Armazena **respostas selecionadas** em questionários HCM.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de respostas:** Vincula participantes, questões e respostas.
- **Tabulação:** Resultados consolidados.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QSTNR_ANSWER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 90% |
| 3 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Questão | [[hrq_questions_b]] | 🟢 85% |
| 4 | ANSWER_ID | NUMBER(18) | NULL | FK | Resposta selecionada | [[hrq_qstn_answers_b]] | 🟢 85% |
| 5 | PARTICIPANT_ID | NUMBER(18) | NOT NULL | FK | Participante | [[hrq_qstnr_participants]] | 🟢 85% |
| 6 | FREE_TEXT | VARCHAR2(4000) | NULL | Texto livre | Resposta em texto livre | — | 🟡 70% |
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

### Respostas de um questionário
```sql
SELECT qa.QUESTION_ID, qa.ANSWER_ID, qa.FREE_TEXT
FROM   HRQ_QSTNR_ANSWERS qa
WHERE  qa.QUESTIONNAIRE_ID = :p_id;
```

---

## 🔒 Observações

- Suporta múltipla escolha (`ANSWER_ID`) e texto livre (`FREE_TEXT`).

---

## 🔗 PVOs Relacionados

### [[questionnaireanswerpvo|QuestionnaireAnswerPVO]] (HCM · BICC: 13/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_ID | QuestionnaireAnswerPEOAnswerId | ✅ |
| BUSINESS_GROUP_ID | QuestionnaireAnswerPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireAnswerPEOCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireAnswerPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | QuestionnaireAnswerPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireAnswerPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionnaireAnswerPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireAnswerPEOObjectVersionNumber | ✅ |
| QSTNR_ANSWER_ID | QuestionnaireAnswerPEOQstnrAnswerId | ✅ |
| QSTNR_QUESTION_ID | QuestionnaireAnswerPEOQstnrQuestionId | ✅ |
| RATING_LEVEL_ID | QuestionnaireAnswerPEORatingLevelId | ✅ |
| SCORE | QuestionnaireAnswerPEOScore | ✅ |
| SUB_QUESTION_ID | QuestionnaireAnswerPEOSubQuestionId | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
