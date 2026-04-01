---
id: DOC-PO-PVO-AssessmentExtractPVO
doc_type: system-doc
title: "AssessmentExtractPVO — PVO Purchasing"
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
  - AssessmentExtractPVO
  - assessmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssessmentExtractPVO

## 📌 Visão Geral

Extrai avaliações de fornecedores para carga BICC, incluindo critérios, datas e resultados. Alimenta o data warehouse para análises de desempenho e qualificação da base de fornecedores.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.AssessmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 1 | 1 | 53 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[poq_assessments|POQ_ASSESSMENTS]] — 104 atributos (1 PKs, 53 BICC)

---

## ⚙️ Atributos

### [[poq_assessments|POQ_ASSESSMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentComments | ASSESSMENT_COMMENTS | — | ✅ |
| 2 | AssessmentId | ASSESSMENT_ID | 🔑 | ✅ |
| 3 | AssessmentName | ASSESSMENT_NAME | — | ✅ |
| 4 | AssessmentNumber | ASSESSMENT_NUMBER | — | ✅ |
| 5 | AssessmentOutcome | ASSESSMENT_OUTCOME | — | ✅ |
| 6 | AssessmentScore | ASSESSMENT_SCORE | — | ✅ |
| 7 | Attribute1 | ATTRIBUTE1 | — | — |
| 8 | Attribute10 | ATTRIBUTE10 | — | — |
| 9 | Attribute11 | ATTRIBUTE11 | — | — |
| 10 | Attribute12 | ATTRIBUTE12 | — | — |
| 11 | Attribute13 | ATTRIBUTE13 | — | — |
| 12 | Attribute14 | ATTRIBUTE14 | — | — |
| 13 | Attribute15 | ATTRIBUTE15 | — | — |
| 14 | Attribute16 | ATTRIBUTE16 | — | — |
| 15 | Attribute17 | ATTRIBUTE17 | — | — |
| 16 | Attribute18 | ATTRIBUTE18 | — | — |
| 17 | Attribute19 | ATTRIBUTE19 | — | — |
| 18 | Attribute2 | ATTRIBUTE2 | — | — |
| 19 | Attribute20 | ATTRIBUTE20 | — | — |
| 20 | Attribute3 | ATTRIBUTE3 | — | — |
| 21 | Attribute4 | ATTRIBUTE4 | — | — |
| 22 | Attribute5 | ATTRIBUTE5 | — | — |
| 23 | Attribute6 | ATTRIBUTE6 | — | — |
| 24 | Attribute7 | ATTRIBUTE7 | — | — |
| 25 | Attribute8 | ATTRIBUTE8 | — | — |
| 26 | Attribute9 | ATTRIBUTE9 | — | — |
| 27 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 28 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 29 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 30 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 31 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 32 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 33 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 34 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 35 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 36 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 37 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 38 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 39 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 40 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 41 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 42 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 43 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 44 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 45 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 46 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 47 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 48 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 49 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 50 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 51 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 52 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 53 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 54 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 55 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 56 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 57 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 58 | AutoEvaluatedFlag | AUTO_EVALUATED_FLAG | — | ✅ |
| 59 | CanceledBy | CANCELED_BY | — | ✅ |
| 60 | CanceledDate | CANCELED_DATE | — | ✅ |
| 61 | CanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 62 | CompletedDate | COMPLETED_DATE | — | ✅ |
| 63 | CreatedBy | CREATED_BY | — | ✅ |
| 64 | CreationDate | CREATION_DATE | — | ✅ |
| 65 | CreationSource | CREATION_SOURCE | — | ✅ |
| 66 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 67 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 68 | EvalReadyDate | EVAL_READY_DATE | — | ✅ |
| 69 | EvaluatedBy | EVALUATED_BY | — | ✅ |
| 70 | EvaluationDate | EVALUATION_DATE | — | ✅ |
| 71 | EvaluationDueDate | EVALUATION_DUE_DATE | — | ✅ |
| 72 | ExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 73 | ExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 74 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 75 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 76 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 77 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 78 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 79 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 80 | LatestFlag | LATEST_FLAG | — | ✅ |
| 81 | MergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 82 | NoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 83 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 84 | OrigAssessmentOutcome | ORIG_ASSESSMENT_OUTCOME | — | ✅ |
| 85 | OrigAssessmentScore | ORIG_ASSESSMENT_SCORE | — | ✅ |
| 86 | OverrideDate | OVERRIDE_DATE | — | ✅ |
| 87 | OverrideReason | OVERRIDE_REASON | — | ✅ |
| 88 | OverridenBy | OVERRIDEN_BY | — | ✅ |
| 89 | OwnerId | OWNER_ID | — | ✅ |
| 90 | PrcBuId | PRC_BU_ID | — | ✅ |
| 91 | QualModelId | QUAL_MODEL_ID | — | ✅ |
| 92 | ReassessExecutedFlag | REASSESS_EXECUTED_FLAG | — | ✅ |
| 93 | ReassessQualificationFlag | REASSESS_QUALIFICATION_FLAG | — | ✅ |
| 94 | ReassessRequestId | REASSESS_REQUEST_ID | — | ✅ |
| 95 | RequestId | REQUEST_ID | — | ✅ |
| 96 | SendIntQnnaireFlag | SEND_INT_QNNAIRE_FLAG | — | ✅ |
| 97 | SendSuppQnnaireFlag | SEND_SUPP_QNNAIRE_FLAG | — | ✅ |
| 98 | ShowAssessmentQualFlag | SHOW_ASSESSMENT_QUAL_FLAG | — | ✅ |
| 99 | ShowAssessmtToSuppFlag | SHOW_ASSESSMT_TO_SUPP_FLAG | — | ✅ |
| 100 | SourcingEligibilityCode | SOURCING_ELIGIBILITY_CODE | — | ✅ |
| 101 | Status | STATUS | — | ✅ |
| 102 | SuppContactPartyId | SUPP_CONTACT_PARTY_ID | — | ✅ |
| 103 | SupplierId | SUPPLIER_ID | — | ✅ |
| 104 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
