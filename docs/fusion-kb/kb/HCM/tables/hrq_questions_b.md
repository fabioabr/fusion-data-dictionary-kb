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

## 🔗 PVOs Relacionados

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM · BICC: 3/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ATTACHMENT_ALLOWED | QuestionBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CLASSIFICATION_CODE | QuestionBPEOClassificationCode | — |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| CREATED_BY | QuestionBPEOCreatedBy | — |
| CREATION_DATE | QuestionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionBPEOLastUpdatedBy | — |
| LATEST_VERSION | QuestionBPEOLatestVersion | — |
| MAX_LENGTH | QuestionBPEOMaxLength | — |
| MAX_SELECTIONS | QuestionBPEOMaxSelections | — |
| MIN_LENGTH | QuestionBPEOMinLength | — |
| MIN_SELECTIONS | QuestionBPEOMinSelections | — |
| MODULE_ID | QuestionBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | — |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | — |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | — |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionBPEOQuestionCode | — |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | ✅ |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionBPEOResponseTypeId | — |
| STATUS | QuestionBPEOStatus | — |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionBPEOVersionDescription | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 10/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ATTACHMENT_ALLOWED | QuestionBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CLASSIFICATION_CODE | QuestionBPEOClassificationCode | ✅ |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| CREATED_BY | QuestionBPEOCreatedBy | — |
| CREATION_DATE | QuestionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionBPEOLastUpdatedBy | — |
| LATEST_VERSION | QuestionBPEOLatestVersion | — |
| MAX_LENGTH | QuestionBPEOMaxLength | — |
| MAX_SELECTIONS | QuestionBPEOMaxSelections | — |
| MIN_LENGTH | QuestionBPEOMinLength | — |
| MIN_SELECTIONS | QuestionBPEOMinSelections | — |
| MODULE_ID | QuestionBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | ✅ |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | ✅ |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | ✅ |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionBPEOQuestionCode | ✅ |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | ✅ |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionBPEOResponseTypeId | — |
| STATUS | QuestionBPEOStatus | ✅ |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionBPEOVersionDescription | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM · BICC: 2/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ATTACHMENT_ALLOWED | QuestionBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CLASSIFICATION_CODE | QuestionBPEOClassificationCode | — |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| CREATED_BY | QuestionBPEOCreatedBy | — |
| CREATION_DATE | QuestionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionBPEOLastUpdatedBy | — |
| LATEST_VERSION | QuestionBPEOLatestVersion | — |
| MAX_LENGTH | QuestionBPEOMaxLength | — |
| MAX_SELECTIONS | QuestionBPEOMaxSelections | — |
| MIN_LENGTH | QuestionBPEOMinLength | — |
| MIN_SELECTIONS | QuestionBPEOMinSelections | — |
| MODULE_ID | QuestionBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | — |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | — |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | — |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionBPEOQuestionCode | — |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | — |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionBPEOResponseTypeId | — |
| STATUS | QuestionBPEOStatus | — |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionBPEOVersionDescription | — |

### [[questionnaireallquestionsp1|QuestionnaireAllQuestionsP1]] (HCM · BICC: 7/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ALL_JOB_FAMILIES_FLAG | QuestionBPEOAllJobFamiliesFlag | — |
| ALL_JOB_FUNCTIONS_FLAG | QuestionBPEOAllJobFunctionsFlag | — |
| ALL_LOCATIONS_FLAG | QuestionBPEOAllLocationsFlag | — |
| ALL_ORGANIZATIONS_FLAG | QuestionBPEOAllOrganizationsFlag | — |
| ATTACHMENT_ALLOWED | QuestionBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | — |
| CANDIDATE_CODE | QuestionBPEOCandidateCode | — |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CLASSIFICATION_CODE | QuestionBPEOClassificationCode | ✅ |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| LATEST_VERSION | QuestionBPEOLatestVersion | — |
| MAX_LENGTH | QuestionBPEOMaxLength | — |
| MAX_POSSIBLE_SCORE | QuestionBPEOMaxPossibleScore | — |
| MAX_SELECTIONS | QuestionBPEOMaxSelections | — |
| MAX_THRESHOLD_SCORE | QuestionBPEOMaxThresholdScore | ✅ |
| MIN_LENGTH | QuestionBPEOMinLength | — |
| MIN_SELECTIONS | QuestionBPEOMinSelections | — |
| MIN_THRESHOLD_SCORE | QuestionBPEOMinThresholdScore | ✅ |
| MODULE_ID | QuestionBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | — |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | — |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | ✅ |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionBPEOQuestionCode | — |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | ✅ |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionBPEOResponseTypeId | — |
| SCORED_FLAG | QuestionBPEOScoredFlag | — |
| SEED_DATA_SOURCE | QuestionBPEOSeedDataSource | — |
| STATUS | QuestionBPEOStatus | ✅ |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionBPEOVersionDescription | — |

### [[questionnairequestionpvo|QuestionnaireQuestionPVO]] (HCM · BICC: 8/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ATTACHMENT_ALLOWED | QuestionnaireBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| CREATED_BY | QuestionnaireBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireBPEOLastUpdatedBy | — |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| MAX_LENGTH | QuestionnaireBPEOMaxLength | — |
| MAX_SELECTIONS | QuestionnaireBPEOMaxSelections | — |
| MIN_LENGTH | QuestionnaireBPEOMinLength | — |
| MIN_SELECTIONS | QuestionnaireBPEOMinSelections | — |
| MODULE_ID | QuestionnaireBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionnaireBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionnaireBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | ✅ |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | ✅ |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | ✅ |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionnaireBPEOQuestionCode | — |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | ✅ |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionnaireBPEOResponseTypeId | — |
| STATUS | QuestionBPEOStatus | ✅ |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionnaireBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionnaireBPEOVersionDescription | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM · BICC: 3/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADHOC_FLAG | QuestionBPEOAdhocFlag | — |
| ATTACHMENT_ALLOWED | QuestionBPEOAttachmentAllowed | — |
| BUSINESS_GROUP_ID | ConditionQuestionBPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionBPEOCategoryId | — |
| CLASSIFICATION_CODE | QuestionBPEOClassificationCode | — |
| CONDITION_ANSWER_ID | QuestionBPEOConditionAnswerId | — |
| CONDITION_DISPLAY | QuestionBPEOConditionDisplay | — |
| CONDITION_QSTN_VERSION_NUM | QuestionBPEOConditionQstnVersionNum | — |
| CONDITION_QUESTION_ID | QuestionBPEOConditionQuestionId | — |
| CREATED_BY | QuestionBPEOCreatedBy | — |
| CREATION_DATE | QuestionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionBPEOLastUpdatedBy | — |
| LATEST_VERSION | QuestionBPEOLatestVersion | — |
| MAX_LENGTH | QuestionBPEOMaxLength | — |
| MAX_SELECTIONS | QuestionBPEOMaxSelections | — |
| MIN_LENGTH | QuestionBPEOMinLength | — |
| MIN_SELECTIONS | QuestionBPEOMinSelections | — |
| MODULE_ID | QuestionBPEOModuleId | — |
| OBJECT_VERSION_NUMBER | QuestionBPEOObjectVersionNumber | — |
| OVERRIDE_DESC_FLAG | QuestionBPEOOverrideDescFlag | — |
| OWNER | QuestionBPEOOwner | — |
| PRIVACY_FLAG | QuestionBPEOPrivacyFlag | — |
| QSTN_VERSION_NUM | ConditionQuestionBPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionBPEOQstnVersionNum | — |
| QUESTION_CODE | ConditionQuestionBPEOQuestionCode | — |
| QUESTION_CODE | QuestionBPEOQuestionCode | — |
| QUESTION_ID | ConditionQuestionBPEOQuestionId | — |
| QUESTION_ID | QuestionBPEOQuestionId | ✅ |
| QUESTION_TYPE | QuestionBPEOQuestionType | ✅ |
| RATING_MODEL_ID | QuestionBPEORatingModelId | — |
| RESPONSE_TYPE_ID | QuestionBPEOResponseTypeId | — |
| STATUS | QuestionBPEOStatus | — |
| SUBSCRIBER_ID | QuestionBPEOSubscriberId | — |
| UPDATE_ALLOWED | QuestionBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionBPEOVersionDescription | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
