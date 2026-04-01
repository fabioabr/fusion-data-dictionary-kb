---
id: DOC-OTHER-PVO-ChangeLineExtractPVO
doc_type: system-doc
title: "ChangeLineExtractPVO — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ChangeLineExtractPVO
  - changelineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Line Extract. Acessa as tabelas: EGO_CHANGE_LINES_B, EGO_CHANGE_LINES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 92 | 2 | 1 | 87 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_lines_b|EGO_CHANGE_LINES_B]] — 87 atributos (1 PKs, 87 BICC)
- [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]] — 5 atributos

---

## ⚙️ Atributos

### [[ego_change_lines_b|EGO_CHANGE_LINES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineBasePEOAssigneeId | ASSIGNEE_ID | — | ✅ |
| 2 | ChangeLineBasePEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 3 | ChangeLineBasePEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 4 | ChangeLineBasePEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 5 | ChangeLineBasePEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 6 | ChangeLineBasePEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 7 | ChangeLineBasePEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 8 | ChangeLineBasePEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 9 | ChangeLineBasePEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 10 | ChangeLineBasePEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 11 | ChangeLineBasePEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 12 | ChangeLineBasePEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 13 | ChangeLineBasePEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 14 | ChangeLineBasePEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 15 | ChangeLineBasePEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 16 | ChangeLineBasePEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 17 | ChangeLineBasePEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 18 | ChangeLineBasePEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 19 | ChangeLineBasePEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 20 | ChangeLineBasePEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 21 | ChangeLineBasePEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 22 | ChangeLineBasePEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 23 | ChangeLineBasePEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 24 | ChangeLineBasePEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 25 | ChangeLineBasePEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 26 | ChangeLineBasePEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 27 | ChangeLineBasePEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 28 | ChangeLineBasePEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 29 | ChangeLineBasePEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 30 | ChangeLineBasePEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 31 | ChangeLineBasePEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 32 | ChangeLineBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | ChangeLineBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 34 | ChangeLineBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 35 | ChangeLineBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 36 | ChangeLineBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 37 | ChangeLineBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 38 | ChangeLineBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 39 | ChangeLineBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 40 | ChangeLineBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 41 | ChangeLineBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 42 | ChangeLineBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 43 | ChangeLineBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 44 | ChangeLineBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 45 | ChangeLineBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 46 | ChangeLineBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 47 | ChangeLineBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 48 | ChangeLineBasePEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 49 | ChangeLineBasePEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 50 | ChangeLineBasePEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 51 | ChangeLineBasePEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 52 | ChangeLineBasePEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 53 | ChangeLineBasePEOBatchId | BATCH_ID | — | ✅ |
| 54 | ChangeLineBasePEOCancelationDate | CANCELATION_DATE | — | ✅ |
| 55 | ChangeLineBasePEOChangeId | CHANGE_ID | — | ✅ |
| 56 | ChangeLineBasePEOChangeLineId | CHANGE_LINE_ID | 🔑 | ✅ |
| 57 | ChangeLineBasePEOCompleteBeforeStatusCode | COMPLETE_BEFORE_STATUS_CODE | — | ✅ |
| 58 | ChangeLineBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 59 | ChangeLineBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 60 | ChangeLineBasePEODependencyFlag | DEPENDENCY_FLAG | — | ✅ |
| 61 | ChangeLineBasePEOEffectivityOnApprovalFlag | EFFECTIVITY_ON_APPROVAL_FLAG | — | ✅ |
| 62 | ChangeLineBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 63 | ChangeLineBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 64 | ChangeLineBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 65 | ChangeLineBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 66 | ChangeLineBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 67 | ChangeLineBasePEOLifecycleStateId | LIFECYCLE_STATE_ID | — | ✅ |
| 68 | ChangeLineBasePEOLineTypeId | LINE_TYPE_ID | — | ✅ |
| 69 | ChangeLineBasePEONeedByDate | NEED_BY_DATE | — | ✅ |
| 70 | ChangeLineBasePEONewItemRevision | NEW_ITEM_REVISION | — | ✅ |
| 71 | ChangeLineBasePEONewItemRevisionId | NEW_ITEM_REVISION_ID | — | ✅ |
| 72 | ChangeLineBasePEONewRevisionReason | NEW_REVISION_REASON | — | ✅ |
| 73 | ChangeLineBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 74 | ChangeLineBasePEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 75 | ChangeLineBasePEOPk1Value | PK1_VALUE | — | ✅ |
| 76 | ChangeLineBasePEOPk2Value | PK2_VALUE | — | ✅ |
| 77 | ChangeLineBasePEOPk3Value | PK3_VALUE | — | ✅ |
| 78 | ChangeLineBasePEOPk4Value | PK4_VALUE | — | ✅ |
| 79 | ChangeLineBasePEOPk5Value | PK5_VALUE | — | ✅ |
| 80 | ChangeLineBasePEORequestId | REQUEST_ID | — | ✅ |
| 81 | ChangeLineBasePEOScheduledDate | SCHEDULED_DATE | — | ✅ |
| 82 | ChangeLineBasePEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 83 | ChangeLineBasePEOStartAfterStatusCode | START_AFTER_STATUS_CODE | — | ✅ |
| 84 | ChangeLineBasePEOStatusCode | STATUS_CODE | — | ✅ |
| 85 | ChangeLineBasePEOStatusType | STATUS_TYPE | — | ✅ |
| 86 | ChangeLineBasePEOSubjectInternalName | SUBJECT_INTERNAL_NAME | — | ✅ |
| 87 | ChangeLineBasePEOThreadNumber | THREAD_NUMBER | — | ✅ |

### [[ego_change_lines_tl|EGO_CHANGE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeLineTLPEOCancelComments | CANCEL_COMMENTS | — | — |
| 2 | ChangeLineTLPEOChangeLineId | CHANGE_LINE_ID | — | — |
| 3 | ChangeLineTLPEODescription | DESCRIPTION | — | — |
| 4 | ChangeLineTLPEOLanguage | LANGUAGE | — | — |
| 5 | ChangeLineTLPEOName | NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
