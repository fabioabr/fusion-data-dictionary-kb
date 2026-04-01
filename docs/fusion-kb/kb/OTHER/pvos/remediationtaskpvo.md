---
id: DOC-OTHER-PVO-RemediationTaskPVO
doc_type: system-doc
title: "RemediationTaskPVO — PVO Cross-Module"
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
  - RemediationTaskPVO
  - remediationtaskpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RemediationTaskPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Remediation Task. Acessa as tabelas: GRC_ISSU_RMTASK_B, GRC_ISSU_RMTASK_TL, GTG_SC_FRC_ACCESS_V (+2).

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.RemediationTaskPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 130 | 5 | 1 | 17 | 13% |

---

## 🔗 Tabelas Relacionadas

- [[grc_issu_rmtask_b|GRC_ISSU_RMTASK_B]] — 96 atributos (1 PKs, 12 BICC)
- [[grc_issu_rmtask_tl|GRC_ISSU_RMTASK_TL]] — 11 atributos (3 BICC)
- [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]] — 3 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos (2 BICC)
- [[per_users|PER_USERS]] — 10 atributos

---

## ⚙️ Atributos

### [[grc_issu_rmtask_b|GRC_ISSU_RMTASK_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RemediationTaskBasePEOApproveCompleteDate | APPROVE_COMPLETE_DATE | — | — |
| 2 | RemediationTaskBasePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | RemediationTaskBasePEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 4 | RemediationTaskBasePEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 5 | RemediationTaskBasePEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 6 | RemediationTaskBasePEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 7 | RemediationTaskBasePEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 8 | RemediationTaskBasePEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 9 | RemediationTaskBasePEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 10 | RemediationTaskBasePEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | — |
| 11 | RemediationTaskBasePEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | — |
| 12 | RemediationTaskBasePEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | — |
| 13 | RemediationTaskBasePEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | — |
| 14 | RemediationTaskBasePEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 15 | RemediationTaskBasePEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | — |
| 16 | RemediationTaskBasePEOAttributeChar21 | ATTRIBUTE_CHAR21 | — | — |
| 17 | RemediationTaskBasePEOAttributeChar22 | ATTRIBUTE_CHAR22 | — | — |
| 18 | RemediationTaskBasePEOAttributeChar23 | ATTRIBUTE_CHAR23 | — | — |
| 19 | RemediationTaskBasePEOAttributeChar24 | ATTRIBUTE_CHAR24 | — | — |
| 20 | RemediationTaskBasePEOAttributeChar25 | ATTRIBUTE_CHAR25 | — | — |
| 21 | RemediationTaskBasePEOAttributeChar26 | ATTRIBUTE_CHAR26 | — | — |
| 22 | RemediationTaskBasePEOAttributeChar27 | ATTRIBUTE_CHAR27 | — | — |
| 23 | RemediationTaskBasePEOAttributeChar28 | ATTRIBUTE_CHAR28 | — | — |
| 24 | RemediationTaskBasePEOAttributeChar29 | ATTRIBUTE_CHAR29 | — | — |
| 25 | RemediationTaskBasePEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 26 | RemediationTaskBasePEOAttributeChar30 | ATTRIBUTE_CHAR30 | — | — |
| 27 | RemediationTaskBasePEOAttributeChar31 | ATTRIBUTE_CHAR31 | — | — |
| 28 | RemediationTaskBasePEOAttributeChar32 | ATTRIBUTE_CHAR32 | — | — |
| 29 | RemediationTaskBasePEOAttributeChar33 | ATTRIBUTE_CHAR33 | — | — |
| 30 | RemediationTaskBasePEOAttributeChar34 | ATTRIBUTE_CHAR34 | — | — |
| 31 | RemediationTaskBasePEOAttributeChar35 | ATTRIBUTE_CHAR35 | — | — |
| 32 | RemediationTaskBasePEOAttributeChar36 | ATTRIBUTE_CHAR36 | — | — |
| 33 | RemediationTaskBasePEOAttributeChar37 | ATTRIBUTE_CHAR37 | — | — |
| 34 | RemediationTaskBasePEOAttributeChar38 | ATTRIBUTE_CHAR38 | — | — |
| 35 | RemediationTaskBasePEOAttributeChar39 | ATTRIBUTE_CHAR39 | — | — |
| 36 | RemediationTaskBasePEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 37 | RemediationTaskBasePEOAttributeChar40 | ATTRIBUTE_CHAR40 | — | — |
| 38 | RemediationTaskBasePEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 39 | RemediationTaskBasePEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 40 | RemediationTaskBasePEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 41 | RemediationTaskBasePEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 42 | RemediationTaskBasePEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 43 | RemediationTaskBasePEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 44 | RemediationTaskBasePEOAttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 45 | RemediationTaskBasePEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 46 | RemediationTaskBasePEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 47 | RemediationTaskBasePEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 48 | RemediationTaskBasePEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 49 | RemediationTaskBasePEOAttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 50 | RemediationTaskBasePEOAttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 51 | RemediationTaskBasePEOAttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 52 | RemediationTaskBasePEOAttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 53 | RemediationTaskBasePEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 54 | RemediationTaskBasePEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 55 | RemediationTaskBasePEOAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 56 | RemediationTaskBasePEOAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 57 | RemediationTaskBasePEOAttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 58 | RemediationTaskBasePEOAttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 59 | RemediationTaskBasePEOAttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 60 | RemediationTaskBasePEOAttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 61 | RemediationTaskBasePEOAttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 62 | RemediationTaskBasePEOAttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 63 | RemediationTaskBasePEOAttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 64 | RemediationTaskBasePEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 65 | RemediationTaskBasePEOAttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 66 | RemediationTaskBasePEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 67 | RemediationTaskBasePEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 68 | RemediationTaskBasePEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 69 | RemediationTaskBasePEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 70 | RemediationTaskBasePEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 71 | RemediationTaskBasePEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 72 | RemediationTaskBasePEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 73 | RemediationTaskBasePEOCategoryCode | CATEGORY_CODE | — | — |
| 74 | RemediationTaskBasePEOCompletedBy | COMPLETED_BY | — | — |
| 75 | RemediationTaskBasePEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 76 | RemediationTaskBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 77 | RemediationTaskBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 78 | RemediationTaskBasePEODueDate | DUE_DATE | — | ✅ |
| 79 | RemediationTaskBasePEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 80 | RemediationTaskBasePEOEstimatedCompletionDate | ESTIMATED_COMPLETION_DATE | — | ✅ |
| 81 | RemediationTaskBasePEOLastStateCode | LAST_STATE_CODE | — | — |
| 82 | RemediationTaskBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 83 | RemediationTaskBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 84 | RemediationTaskBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 85 | RemediationTaskBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 86 | RemediationTaskBasePEOPriorityCode | PRIORITY_CODE | — | — |
| 87 | RemediationTaskBasePEOProgressCode | PROGRESS_CODE | — | ✅ |
| 88 | RemediationTaskBasePEORemedPlanId | REMED_PLAN_ID | — | — |
| 89 | RemediationTaskBasePEORemedTaskId | REMED_TASK_ID | 🔑 | ✅ |
| 90 | RemediationTaskBasePEOReviewStartDate | REVIEW_START_DATE | — | — |
| 91 | RemediationTaskBasePEORevisionDate | REVISION_DATE | — | — |
| 92 | RemediationTaskBasePEORevisionNumber | REVISION_NUMBER | — | — |
| 93 | RemediationTaskBasePEOStartDate | START_DATE | — | ✅ |
| 94 | RemediationTaskBasePEOStateCode | STATE_CODE | — | ✅ |
| 95 | RemediationTaskBasePEOStateDate | STATE_DATE | — | — |
| 96 | RemediationTaskBasePEOStatus | STATUS | — | ✅ |

### [[grc_issu_rmtask_tl|GRC_ISSU_RMTASK_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RemediationTaskTransPEOCreatedBy | CREATED_BY | — | — |
| 2 | RemediationTaskTransPEOCreationDate | CREATION_DATE | — | — |
| 3 | RemediationTaskTransPEODescription | DESCRIPTION | — | — |
| 4 | RemediationTaskTransPEODetailedDescription | DETAILED_DESCRIPTION | — | ✅ |
| 5 | RemediationTaskTransPEOLanguage | LANGUAGE | — | — |
| 6 | RemediationTaskTransPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RemediationTaskTransPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | RemediationTaskTransPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | RemediationTaskTransPEOName | NAME | — | ✅ |
| 10 | RemediationTaskTransPEORemedTaskId | REMED_TASK_ID | — | — |
| 11 | RemediationTaskTransPEOSourceLang | SOURCE_LANG | — | — |

### [[gtg_sc_frc_access_v|GTG_SC_FRC_ACCESS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FRCSecurityPEOSecurableId | SECURABLE_ID | — | — |
| 2 | FRCSecurityPEOSecurableType | SECURABLE_TYPE | — | — |
| 3 | FRCSecurityPEOUserId | USER_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RmTkPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | RmTkPersonCreatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | RmTkPersonCreatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | RmTkPersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | RmTkPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | RmTkPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | RmTkPersonUpdatedByEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | RmTkPersonUpdatedByEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | RmTkPersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | RmTkPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RmTkCreatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | RmTkCreatedByPersonId | PERSON_ID | — | — |
| 3 | RmTkCreatedByUserGuid | USER_GUID | — | — |
| 4 | RmTkCreatedByUserId | USER_ID | — | — |
| 5 | RmTkCreatedByUsername | USERNAME | — | — |
| 6 | RmTkUpdatedByObjectVerNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | RmTkUpdatedByPersonId | PERSON_ID | — | — |
| 8 | RmTkUpdatedByUserGuid | USER_GUID | — | — |
| 9 | RmTkUpdatedByUserId | USER_ID | — | — |
| 10 | RmTkUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
