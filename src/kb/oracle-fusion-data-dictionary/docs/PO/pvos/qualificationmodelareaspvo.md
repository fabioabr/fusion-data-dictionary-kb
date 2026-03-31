---
id: DOC-PO-PVO-QualificationModelAreasPVO
doc_type: system-doc
title: "QualificationModelAreasPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QualificationModelAreasPVO
  - qualificationmodelareaspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualificationModelAreasPVO

## 📌 Visão Geral

Extrai as áreas dentro de cada modelo de qualificação, com pesos e critérios de aprovação atribuídos. Permite análise da estrutura avaliativa e calibração de processos de homologação.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QualificationModelAreasPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 3 | 1 | 67 | 94% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]] — 39 atributos (36 BICC)
- [[poq_qual_models|POQ_QUAL_MODELS]] — 20 atributos (19 BICC)
- [[poq_qual_model_areas|POQ_QUAL_MODEL_AREAS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[poq_qual_areas_vl|POQ_QUAL_AREAS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | QualAreaAutoAcceptResponsesFlag | AUTO_ACCEPT_RESPONSES_FLAG | — | ✅ |
| 3 | QualAreaAutoEvaluateQualFlag | AUTO_EVALUATE_QUAL_FLAG | — | ✅ |
| 4 | QualAreaAutoPopulateResponsesFlag | AUTO_POPULATE_RESPONSES_FLAG | — | ✅ |
| 5 | QualAreaCreatedBy | CREATED_BY | — | ✅ |
| 6 | QualAreaCreationDate | CREATION_DATE | — | ✅ |
| 7 | QualAreaDefaultQualOwnerFlag | DEFAULT_QUAL_OWNER_FLAG | — | — |
| 8 | QualAreaEnableScoringFlag | ENABLE_SCORING_FLAG | — | ✅ |
| 9 | QualAreaExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 10 | QualAreaExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 11 | QualAreaGlobalFlag | GLOBAL_FLAG | — | ✅ |
| 12 | QualAreaInformationOnlyFlag | INFORMATION_ONLY_FLAG | — | ✅ |
| 13 | QualAreaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | QualAreaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | QualAreaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | QualAreaLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 17 | QualAreaNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 18 | QualAreaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | QualAreaOriginalQualAreaId | ORIGINAL_QUAL_AREA_ID | — | ✅ |
| 20 | QualAreaOwnerId | OWNER_ID | — | ✅ |
| 21 | QualAreaPrcBuId | PRC_BU_ID | — | ✅ |
| 22 | QualAreaQualAreaDescription | QUAL_AREA_DESCRIPTION | — | ✅ |
| 23 | QualAreaQualAreaId | QUAL_AREA_ID | — | ✅ |
| 24 | QualAreaQualAreaLevel | QUAL_AREA_LEVEL | — | ✅ |
| 25 | QualAreaQualAreaName | QUAL_AREA_NAME | — | ✅ |
| 26 | QualAreaQualAreaStatus | QUAL_AREA_STATUS | — | ✅ |
| 27 | QualAreaQualificationDuration | QUALIFICATION_DURATION | — | ✅ |
| 28 | QualAreaQualificationDurationType | QUALIFICATION_DURATION_TYPE | — | ✅ |
| 29 | QualAreaQualificationOwnerId | QUALIFICATION_OWNER_ID | — | — |
| 30 | QualAreaRequalifyExpirationFlag | REQUALIFY_EXPIRATION_FLAG | — | ✅ |
| 31 | QualAreaRequalifyResponseFlag | REQUALIFY_RESPONSE_FLAG | — | ✅ |
| 32 | QualAreaRevisionNumber | REVISION_NUMBER | — | ✅ |
| 33 | QualAreaShowQualInterRespFlag | SHOW_QUAL_INTER_RESP_FLAG | — | ✅ |
| 34 | QualAreaShowQualSuppRespFlag | SHOW_QUAL_SUPP_RESP_FLAG | — | ✅ |
| 35 | QualAreaShowQualToSupplierFlag | SHOW_QUAL_TO_SUPPLIER_FLAG | — | ✅ |
| 36 | QualAreaSingleQualAutoInitFlag | SINGLE_QUAL_AUTO_INIT_FLAG | — | — |
| 37 | QualAreaStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 38 | QualAreaSubjectCode | SUBJECT_CODE | — | ✅ |
| 39 | QualAreaSurveyFlag | QUAL_AREA_SURVEY_FLAG | — | ✅ |

### [[poq_qual_models|POQ_QUAL_MODELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualModelCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualModelCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualModelGlobalFlag | GLOBAL_FLAG | — | ✅ |
| 4 | QualModelLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | QualModelLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | QualModelLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | QualModelLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 8 | QualModelObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QualModelOriginalQualModelId | ORIGINAL_QUAL_MODEL_ID | — | ✅ |
| 10 | QualModelOwnerId | OWNER_ID | — | ✅ |
| 11 | QualModelPrcBuId | PRC_BU_ID | — | ✅ |
| 12 | QualModelQualModelDescription | QUAL_MODEL_DESCRIPTION | — | ✅ |
| 13 | QualModelQualModelId | QUAL_MODEL_ID | — | ✅ |
| 14 | QualModelQualModelLevel | QUAL_MODEL_LEVEL | — | ✅ |
| 15 | QualModelQualModelName | QUAL_MODEL_NAME | — | ✅ |
| 16 | QualModelQualModelStatus | QUAL_MODEL_STATUS | — | ✅ |
| 17 | QualModelRevisionNumber | REVISION_NUMBER | — | ✅ |
| 18 | QualModelStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 19 | QualModelSubjectCode | SUBJECT_CODE | — | ✅ |
| 20 | QualModelUsageCode | QUAL_MODEL_USAGE_CODE | — | — |

### [[poq_qual_model_areas|POQ_QUAL_MODEL_AREAS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualModelAreaId | QUAL_MODEL_AREA_ID | 🔑 | ✅ |
| 2 | QualificationModelAreaCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualificationModelAreaCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualificationModelAreaDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | QualificationModelAreaKnockoutScore | KNOCKOUT_SCORE | — | ✅ |
| 6 | QualificationModelAreaLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualificationModelAreaLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QualificationModelAreaLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QualificationModelAreaObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | QualificationModelAreaQualAreaId | QUAL_AREA_ID | — | ✅ |
| 11 | QualificationModelAreaQualModelId | QUAL_MODEL_ID | — | ✅ |
| 12 | QualificationModelAreaWeight | WEIGHT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
