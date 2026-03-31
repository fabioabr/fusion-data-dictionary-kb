---
id: DOC-HCM-191
doc_type: system-doc
title: "HRQ_QSTN_ANSWERS_B — Opções de Resposta de Questões (Base)"
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
  - HRQ_QSTN_ANSWERS_B
  - hrq_qstn_answers_b
  - opções-de-resposta-de-questões-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTN_ANSWERS_B

## 📌 Visão Geral

Tabela base das **opções de resposta** para questões (múltipla escolha, escala).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Opções:** Alternativas para questões.
- **Escalas:** Valores de escalas de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ANSWER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | QUESTION_ID | NUMBER(18) | NOT NULL | FK | Questão | [[hrq_questions_b]] | 🟢 90% |
| 3 | ANSWER_CODE | VARCHAR2(30) | NULL | Identificação | Código | — | 🟡 75% |
| 4 | SCORE | NUMBER | NULL | Métrica | Pontuação | — | 🟡 70% |
| 5 | DISPLAY_SEQUENCE | NUMBER | NULL | Ordenação | Ordem | — | 🟡 75% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrq_questions_b]] — via `QUESTION_ID` (pergunta da resposta do questionario)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Opções de uma questão
```sql
SELECT a.ANSWER_ID, a.ANSWER_CODE, a.SCORE
FROM   HRQ_QSTN_ANSWERS_B a
WHERE  a.QUESTION_ID = :p_id
ORDER BY a.DISPLAY_SEQUENCE;
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_qstn_answers_tl]].
`SCORE` permite cálculo automático de pontuação.

---

## 🔗 PVOs Relacionados

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |

### [[participantquestionnairequestionresponselistpvo|ParticipantQuestionnaireQuestionResponseListPVO]] (HCM · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_QSTNR_ID | QuestionAnswerBPEOAddlQstnrId | — |
| ADDL_QSTNR_VERSION_NUM | QuestionAnswerBPEOAddlQstnrVersionNum | — |
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | QuestionAnswerBPEOBusinessGroupId | ✅ |
| QSTN_ANSWER_ID | QuestionAnswerBPEOQstnAnswerId | ✅ |
| QUESTION_ID | QuestionAnswerBPEOQuestionId | — |
| RATING_LEVEL_ID | QuestionAnswerBPEORatingLevelId | — |
| SEQ_NUM | QuestionAnswerBPEOSeqNum | ✅ |

### [[questionanswerpvo|QuestionAnswerPVO]] (HCM · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_QSTNR_ID | QuestionAnswerBPEOAddlQstnrId | — |
| ADDL_QSTNR_VERSION_NUM | QuestionAnswerBPEOAddlQstnrVersionNum | — |
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | QuestionAnswerBPEOBusinessGroupId | ✅ |
| CORRECT_FLAG | QuestionAnswerBPEOCorrectFlag | — |
| CREATED_BY | QuestionAnswerBPEOCreatedBy | — |
| CREATION_DATE | QuestionAnswerBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionAnswerBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionAnswerBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionAnswerBPEOLastUpdatedBy | — |
| MODULE_ID | QuestionAnswerBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionAnswerBPEOObjectVersionNumber | — |
| QSTN_ANSWER_ID | QuestionAnswerBPEOQstnAnswerId | ✅ |
| QSTN_VERSION_NUM | QuestionAnswerBPEOQstnVersionNum | — |
| QUESTION_ID | QuestionAnswerBPEOQuestionId | — |
| RATING_LEVEL_ID | QuestionAnswerBPEORatingLevelId | — |
| SCORE | QuestionAnswerBPEOScore | ✅ |
| SCORE_WEIGHT | QuestionAnswerBPEOScoreWeight | — |
| SEED_DATA_SOURCE | QuestionAnswerBPEOSeedDataSource | — |
| SEQ_NUM | QuestionAnswerBPEOSeqNum | ✅ |

### [[questionnaireallquestionsp1|QuestionnaireAllQuestionsP1]] (HCM · BICC: 4/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_QSTNR_ID | QuestionAnswerBPEOAddlQstnrId | — |
| ADDL_QSTNR_VERSION_NUM | QuestionAnswerBPEOAddlQstnrVersionNum | — |
| ANSWER_CODE | AnswerCode | — |
| ANSWER_CODE | QuestionAnswerBPEOAnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionAnswerBPEOBusinessGroupId | — |
| CORRECT_FLAG | QuestionAnswerBPEOCorrectFlag | — |
| CREATED_BY | QuestionAnswerBPEOCreatedBy | — |
| CREATION_DATE | QuestionAnswerBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionAnswerBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionAnswerBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionAnswerBPEOLastUpdatedBy | — |
| MODULE_ID | QuestionAnswerBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionAnswerBPEOObjectVersionNumber | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |
| QSTN_ANSWER_ID | QuestionAnswerBPEOQstnAnswerId | ✅ |
| QSTN_VERSION_NUM | QuestionAnswerBPEOQstnVersionNum | — |
| QUESTION_ID | QuestionAnswerBPEOQuestionId | — |
| RATING_LEVEL_ID | QuestionAnswerBPEORatingLevelId | — |
| SCORE | QuestionAnswerBPEOScore | ✅ |
| SCORE_WEIGHT | QuestionAnswerBPEOScoreWeight | — |
| SEED_DATA_SOURCE | QuestionAnswerBPEOSeedDataSource | — |
| SEQ_NUM | QuestionAnswerBPEOSeqNum | ✅ |

### [[questionnairequestionpvo|QuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |

### [[questionnairequestionresponselistpvo|QuestionnaireQuestionResponseListPVO]] (HCM · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_QSTNR_ID | QuestionAnswerBPEOAddlQstnrId | — |
| ADDL_QSTNR_VERSION_NUM | QuestionAnswerBPEOAddlQstnrVersionNum | — |
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | QuestionAnswerBPEOBusinessGroupId | ✅ |
| QSTN_ANSWER_ID | QuestionAnswerBPEOQstnAnswerId | ✅ |
| QUESTION_ID | QuestionAnswerBPEOQuestionId | — |
| RATING_LEVEL_ID | QuestionAnswerBPEORatingLevelId | — |
| SEQ_NUM | QuestionAnswerBPEOSeqNum | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANSWER_CODE | AnswerCode | — |
| BUSINESS_GROUP_ID | ConditionQstnAnswerBPEOBusinessGroupId | — |
| QSTN_ANSWER_ID | ConditionQstnAnswerBPEOQstnAnswerId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
