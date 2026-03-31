---
id: DOC-PO-PVO-QualificationModelPVO
doc_type: system-doc
title: "QualificationModelPVO — PVO Purchasing"
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
  - QualificationModelPVO
  - qualificationmodelpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualificationModelPVO

## 📌 Visão Geral

Extrai os modelos de qualificação configurados, com estrutura de áreas, pesos e critérios de aprovação/reprovação. Define o framework de avaliação utilizado na homologação de fornecedores.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QualificationModelPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 1 | 27 | 84% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qual_models|POQ_QUAL_MODELS]] — 32 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[poq_qual_models|POQ_QUAL_MODELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualModelId | QUAL_MODEL_ID | 🔑 | ✅ |
| 2 | QualModelUsageCode | QUAL_MODEL_USAGE_CODE | — | — |
| 3 | QualificationModelActivationDate | ACTIVATION_DATE | — | ✅ |
| 4 | QualificationModelAssessmentOwnerId | ASSESSMENT_OWNER_ID | — | — |
| 5 | QualificationModelAutoEvalAssessmentFlag | AUTO_EVAL_ASSESSMENT_FLAG | — | ✅ |
| 6 | QualificationModelCreatedBy | CREATED_BY | — | ✅ |
| 7 | QualificationModelCreationDate | CREATION_DATE | — | ✅ |
| 8 | QualificationModelDefaultAssessmtOwnerFlag | DEFAULT_ASSESSMT_OWNER_FLAG | — | — |
| 9 | QualificationModelEnableScoringFlag | ENABLE_SCORING_FLAG | — | ✅ |
| 10 | QualificationModelExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 11 | QualificationModelExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 12 | QualificationModelGlobalFlag | GLOBAL_FLAG | — | ✅ |
| 13 | QualificationModelLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | QualificationModelLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | QualificationModelLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | QualificationModelLatestRevisionFlag | LATEST_REVISION_FLAG | — | ✅ |
| 17 | QualificationModelNoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 18 | QualificationModelObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | QualificationModelOriginalQualModelId | ORIGINAL_QUAL_MODEL_ID | — | ✅ |
| 20 | QualificationModelOwnerId | OWNER_ID | — | ✅ |
| 21 | QualificationModelPrcBuId | PRC_BU_ID | — | ✅ |
| 22 | QualificationModelQualModelDescription | QUAL_MODEL_DESCRIPTION | — | ✅ |
| 23 | QualificationModelQualModelLevel | QUAL_MODEL_LEVEL | — | ✅ |
| 24 | QualificationModelQualModelName | QUAL_MODEL_NAME | — | ✅ |
| 25 | QualificationModelQualModelStatus | QUAL_MODEL_STATUS | — | ✅ |
| 26 | QualificationModelRevisionNumber | REVISION_NUMBER | — | ✅ |
| 27 | QualificationModelShowAssessmentQualFlag | SHOW_ASSESSMENT_QUAL_FLAG | — | ✅ |
| 28 | QualificationModelShowAssessmtToSuppFlag | SHOW_ASSESSMT_TO_SUPP_FLAG | — | ✅ |
| 29 | QualificationModelSourcingEligibleFlag | SOURCING_ELIGIBLE_FLAG | — | — |
| 30 | QualificationModelSourcingShareEligFlag | SOURCING_SHARE_ELIG_FLAG | — | — |
| 31 | QualificationModelStdsOrgCode | STDS_ORG_CODE | — | ✅ |
| 32 | QualificationModelSubjectCode | SUBJECT_CODE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
