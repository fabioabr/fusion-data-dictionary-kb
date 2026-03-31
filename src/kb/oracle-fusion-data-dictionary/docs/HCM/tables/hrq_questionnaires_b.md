---
id: DOC-HCM-194
doc_type: system-doc
title: "HRQ_QUESTIONNAIRES_B — Questionários (Base)"
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
aliases:
  - HRQ_QUESTIONNAIRES_B
  - hrq_questionnaires_b
  - questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QUESTIONNAIRES_B

## 📌 Visão Geral

Tabela base dos **questionários** HCM. Configurações, status e período.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Definição:** Registro central de cada questionário.
- **Ciclo de vida:** Controle de status.
- **Período:** Datas de abertura e encerramento.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | QUESTIONNAIRE_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código | — | 🟢 85% |
| 3 | CATEGORY_ID | NUMBER(18) | NULL | FK | Categoria | [[hrq_categories_b]] | 🟡 80% |
| 4 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status (DRAFT, PUBLISHED, CLOSED) | — | 🟢 85% |
| 5 | START_DATE | DATE | NULL | Data | Abertura | — | 🟡 80% |
| 6 | END_DATE | DATE | NULL | Data | Encerramento | — | 🟡 80% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-filha

### Tabelas relacionadas

---

## 📎 Uso Típico

### Questionários publicados
```sql
SELECT q.QUESTIONNAIRE_ID, q.QUESTIONNAIRE_CODE, q.STATUS_CODE
FROM   HRQ_QUESTIONNAIRES_B q
WHERE  q.STATUS_CODE = 'PUBLISHED';
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_questionnaires_tl]].
Ciclo: DRAFT -> PUBLISHED -> CLOSED.
- Tabela central do módulo de questionários.

---

## 🔗 PVOs Relacionados

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 10/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CATEGORY_ID | CategoryId | — |
| CREATED_BY | CreatedBy4 | — |
| CREATION_DATE | CreationDate4 | — |
| IN_USE | InUse | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate4 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin4 | — |
| LAST_UPDATED_BY | LastUpdatedBy4 | — |
| LATEST_VERSION | LatestVersion | — |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber3 | — |
| OWNER | Owner | ✅ |
| PAGE_LAYOUT | PageLayout | — |
| PRIVACY_FLAG | PrivacyFlag | ✅ |
| QSTNR_TEMPLATE_ID | QstnrTemplateId | — |
| QSTNR_VERSION_NUM | QstnrVersionNum2 | — |
| QSTNS_PER_PAGE | QstnsPerPage | ✅ |
| QUESTIONNAIRE_CODE | QuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId2 | — |
| SECTION_ORDER | SectionOrder | ✅ |
| SECTION_PRESENTATION | SectionPresentation | ✅ |
| STATUS | Status | ✅ |
| SUBSCRIBER_ID | SubscriberId | — |
| TEMPLATE_FLAG | TemplateFlag | — |
| UPDATE_ALLOWED | UpdateAllowed | — |
| VERSION_DESCRIPTION | VersionDescription | ✅ |

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| IN_USE | QuestionnaireBPEOInUse | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | — |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| OWNER | QuestionnaireBPEOOwner | — |
| PAGE_LAYOUT | QuestionnaireBPEOPageLayout | — |
| PRIVACY_FLAG | QuestionnaireBPEOPrivacyFlag | — |
| QSTNR_TEMPLATE_ID | QuestionnaireBPEOQstnrTemplateId | — |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QSTNS_PER_PAGE | QuestionnaireBPEOQstnsPerPage | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| SECTION_ORDER | QuestionnaireBPEOSectionOrder | — |
| SECTION_PRESENTATION | QuestionnaireBPEOSectionPresentation | — |
| STATUS | QuestionnaireBPEOStatus | — |
| SUBSCRIBER_ID | QuestionnaireBPEOSubscriberId | — |
| TEMPLATE_FLAG | QuestionnaireBPEOTemplateFlag | — |
| UPDATE_ALLOWED | QuestionnaireBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionnaireBPEOVersionDescription | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 5/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | ✅ |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| IN_USE | QuestionnaireBPEOInUse | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | — |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| OWNER | QuestionnaireBPEOOwner | — |
| PAGE_LAYOUT | QuestionnaireBPEOPageLayout | — |
| PRIVACY_FLAG | QuestionnaireBPEOPrivacyFlag | — |
| QSTNR_TEMPLATE_ID | QuestionnaireBPEOQstnrTemplateId | — |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | ✅ |
| QSTNS_PER_PAGE | QuestionnaireBPEOQstnsPerPage | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | ✅ |
| SECTION_ORDER | QuestionnaireBPEOSectionOrder | — |
| SECTION_PRESENTATION | QuestionnaireBPEOSectionPresentation | — |
| STATUS | QuestionnaireBPEOStatus | ✅ |
| SUBSCRIBER_ID | QuestionnaireBPEOSubscriberId | — |
| TEMPLATE_FLAG | QuestionnaireBPEOTemplateFlag | — |
| UPDATE_ALLOWED | QuestionnaireBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionnaireBPEOVersionDescription | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| IN_USE | QuestionnaireBPEOInUse | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | — |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| OWNER | QuestionnaireBPEOOwner | — |
| PAGE_LAYOUT | QuestionnaireBPEOPageLayout | — |
| PRIVACY_FLAG | QuestionnaireBPEOPrivacyFlag | — |
| QSTNR_TEMPLATE_ID | QuestionnaireBPEOQstnrTemplateId | — |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QSTNS_PER_PAGE | QuestionnaireBPEOQstnsPerPage | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| SECTION_ORDER | QuestionnaireBPEOSectionOrder | — |
| SECTION_PRESENTATION | QuestionnaireBPEOSectionPresentation | — |
| STATUS | QuestionnaireBPEOStatus | — |
| SUBSCRIBER_ID | QuestionnaireBPEOSubscriberId | — |
| TEMPLATE_FLAG | QuestionnaireBPEOTemplateFlag | — |
| UPDATE_ALLOWED | QuestionnaireBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionnaireBPEOVersionDescription | — |

### [[participantquestionnairequestionresponselistpvo|ParticipantQuestionnaireQuestionResponseListPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireBPEOBusinessGroupId | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | AdditionalQuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireBPEOQuestionnaireId | — |

### [[questionanswerpvo|QuestionAnswerPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireBPEOBusinessGroupId | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | AdditionalQuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireBPEOQuestionnaireId | — |

### [[questionnaireallquestionsp1|QuestionnaireAllQuestionsP1]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | ✅ |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | ✅ |

### [[questionnairepvo|QuestionnairePVO]] (HCM · BICC: 6/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CATEGORY_ID | CategoryId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| IN_USE | InUse | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LATEST_VERSION | LatestVersion | — |
| MODULE_ID | ModuleId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNER | Owner | — |
| PAGE_LAYOUT | PageLayout | — |
| PRIVACY_FLAG | PrivacyFlag | — |
| QSTNR_TEMPLATE_ID | QstnrTemplateId | — |
| QSTNR_VERSION_NUM | QstnrVersionNum | ✅ |
| QSTNS_PER_PAGE | QstnsPerPage | — |
| QUESTIONNAIRE_CODE | QuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireId | ✅ |
| SECTION_ORDER | SectionOrder | — |
| SECTION_PRESENTATION | SectionPresentation | — |
| STATUS | Status | — |
| SUBSCRIBER_ID | SubscriberId | — |
| TEMPLATE_FLAG | TemplateFlag | — |
| UPDATE_ALLOWED | UpdateAllowed | — |
| VERSION_DESCRIPTION | VersionDescription | — |

### [[questionnairequestionresponselistpvo|QuestionnaireQuestionResponseListPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireBPEOBusinessGroupId | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | AdditionalQuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireBPEOQuestionnaireId | — |

### [[requisitionqstnrexternalviewallpvo|RequisitionQstnrExternalViewAllPVO]] (PO · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| CREATED_BY | QuestionnaireBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireBPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireBPEOLastUpdatedBy | — |
| MAX_POSSIBLE_SCORE | QuestionnaireBPEOMaxPossibleScore | ✅ |
| OWNER | QuestionnaireBPEOOwner | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| STATUS | QuestionnaireBPEOStatus | — |

### [[requisitionqstnrinternalviewallpvo|RequisitionQstnrInternalViewAllPVO]] (PO · BICC: 5/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| CREATED_BY | QuestionnaireBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireBPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireBPEOLastUpdatedBy | — |
| MAX_POSSIBLE_SCORE | QuestionnaireBPEOMaxPossibleScore | ✅ |
| OWNER | QuestionnaireBPEOOwner | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| STATUS | QuestionnaireBPEOStatus | — |

### [[requisitionqstnrinterviewviewallpvo|RequisitionQstnrInterviewViewAllPVO]] (PO · BICC: 4/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| CREATED_BY | QuestionnaireBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireBPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | QuestionnaireBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireBPEOLastUpdatedBy | — |
| MAX_POSSIBLE_SCORE | QuestionnaireBPEOMaxPossibleScore | — |
| OWNER | QuestionnaireBPEOOwner | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| STATUS | QuestionnaireBPEOStatus | — |

### [[submissionqstnrsviewallpvo|SubmissionQstnrsViewAllPVO]] (PO · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| MAX_POSSIBLE_SCORE | QuestionnaireBPEOMaxPossibleScore | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireBPEOBusinessGroupId | — |
| CATEGORY_ID | QuestionnaireBPEOCategoryId | — |
| IN_USE | QuestionnaireBPEOInUse | — |
| LAST_UPDATE_DATE | QuestionnaireParticipantPEOLastUpdateDate | — |
| LATEST_VERSION | QuestionnaireBPEOLatestVersion | — |
| OWNER | QuestionnaireBPEOOwner | — |
| PAGE_LAYOUT | QuestionnaireBPEOPageLayout | — |
| PRIVACY_FLAG | QuestionnaireBPEOPrivacyFlag | — |
| QSTNR_TEMPLATE_ID | QuestionnaireBPEOQstnrTemplateId | — |
| QSTNR_VERSION_NUM | QuestionnaireBPEOQstnrVersionNum | — |
| QSTNS_PER_PAGE | QuestionnaireBPEOQstnsPerPage | — |
| QUESTIONNAIRE_CODE | QuestionnaireBPEOQuestionnaireCode | — |
| QUESTIONNAIRE_ID | QuestionnaireBPEOQuestionnaireId | — |
| SECTION_ORDER | QuestionnaireBPEOSectionOrder | — |
| SECTION_PRESENTATION | QuestionnaireBPEOSectionPresentation | — |
| STATUS | QuestionnaireBPEOStatus | — |
| SUBSCRIBER_ID | QuestionnaireBPEOSubscriberId | — |
| TEMPLATE_FLAG | QuestionnaireBPEOTemplateFlag | — |
| UPDATE_ALLOWED | QuestionnaireBPEOUpdateAllowed | — |
| VERSION_DESCRIPTION | QuestionnaireBPEOVersionDescription | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
