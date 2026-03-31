---
id: DOC-OTHER-PVO-ProcessActionItemPVO
doc_type: system-doc
title: "ProcessActionItemPVO — PVO Cross-Module"
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
  - ProcessActionItemPVO
  - processactionitempvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessActionItemPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Action Item. Acessa as tabelas: GRC_PROC_ACTITEM_B, GRC_PROC_ACTITEM_TL, GTG_SC_FRC_ACCESS_V (+2).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.ProcessActionItemPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 5 | 1 | 13 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[grc_proc_actitem_b|GRC_PROC_ACTITEM_B]] — 23 atributos (1 PKs, 8 BICC)
- [[grc_proc_actitem_tl|GRC_PROC_ACTITEM_TL]] — 11 atributos (3 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_proc_actitem_b|GRC_PROC_ACTITEM_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessActionBasePEOActionId | ACTION_ID | 🔑 | ✅ |
| 2 | ProcessActionBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 3 | ProcessActionBasePEOCompletedBy | COMPLETED_BY | — | — |
| 4 | ProcessActionBasePEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 5 | ProcessActionBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | ProcessActionBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | ProcessActionBasePEODueDate | DUE_DATE | — | ✅ |
| 8 | ProcessActionBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 9 | ProcessActionBasePEOEstimatedCompletionDate | ESTIMATED_COMPLETION_DATE | — | — |
| 10 | ProcessActionBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 11 | ProcessActionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ProcessActionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ProcessActionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ProcessActionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ProcessActionBasePEOPriorityCode | PRIORITY_CODE | — | — |
| 16 | ProcessActionBasePEOProcessId | PROCESS_ID | — | — |
| 17 | ProcessActionBasePEOProgressCode | PROGRESS_CODE | — | ✅ |
| 18 | ProcessActionBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 19 | ProcessActionBasePEORevisionDate | REVISION_DATE | — | — |
| 20 | ProcessActionBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 21 | ProcessActionBasePEOStartDate | START_DATE | — | — |
| 22 | ProcessActionBasePEOStateCode | STATE_CODE | — | — |
| 23 | ProcessActionBasePEOStateDate | STATE_DATE | — | — |

### [[grc_proc_actitem_tl|GRC_PROC_ACTITEM_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProcessActionTranslationPEOActionId | ACTION_ID | — | — |
| 2 | ProcessActionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | ProcessActionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | ProcessActionTranslationPEODescription | DESCRIPTION | — | — |
| 5 | ProcessActionTranslationPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 6 | ProcessActionTranslationPEOLanguage | LANGUAGE | — | — |
| 7 | ProcessActionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ProcessActionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ProcessActionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ProcessActionTranslationPEOName | NAME | — | ✅ |
| 11 | ProcessActionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrAcPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | PrAcPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PrAcPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PrAcPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PrAcPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PrAcPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | PrAcPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PrAcPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PrAcPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PrAcPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrAcCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | PrAcCreatedByPersonId | PERSON_ID | — | — |
| 3 | PrAcCreatedByUserGuid | USER_GUID | — | — |
| 4 | PrAcCreatedByUserId | USER_ID | — | — |
| 5 | PrAcCreatedByUsername | USERNAME | — | — |
| 6 | PrAcUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | PrAcUpdatedByPersonId | PERSON_ID | — | — |
| 8 | PrAcUpdatedByUserGuid | USER_GUID | — | — |
| 9 | PrAcUpdatedByUserId | USER_ID | — | — |
| 10 | PrAcUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
