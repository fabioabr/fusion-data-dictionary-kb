---
id: DOC-OTHER-PVO-EventAssignmentRecordPVO
doc_type: system-doc
title: "EventAssignmentRecordPVO — PVO Cross-Module"
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
  - EventAssignmentRecordPVO
  - eventassignmentrecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EventAssignmentRecordPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Event Assignment Record. Acessa as tabelas: WLF_ASSIGNMENT_RECORDS_F, WLF_ASSIGNMENT_RULES, WLF_EVENT_ASSIGNMENTS_F (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.EventAssignmentRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 104 | 4 | 3 | 60 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_assignment_records_f|WLF_ASSIGNMENT_RECORDS_F]] — 45 atributos (3 PKs, 36 BICC)
- [[wlf_assignment_rules|WLF_ASSIGNMENT_RULES]] — 26 atributos (15 BICC)
- [[wlf_event_assignments_f|WLF_EVENT_ASSIGNMENTS_F]] — 18 atributos (6 BICC)
- [[wlf_event_assignments_f_tl|WLF_EVENT_ASSIGNMENTS_F_TL]] — 15 atributos (3 BICC)

---

## ⚙️ Atributos

### [[wlf_assignment_records_f|WLF_ASSIGNMENT_RECORDS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentRecordDEOAssignedOnDate | ASSIGNED_ON_DATE | — | ✅ |
| 2 | AssignmentRecordDEOAssignmentRecordId | ASSIGNMENT_RECORD_ID | 🔑 | ✅ |
| 3 | AssignmentRecordDEOAssignmentRecordNumber | ASSIGNMENT_RECORD_NUMBER | — | ✅ |
| 4 | AssignmentRecordDEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | ✅ |
| 5 | AssignmentRecordDEOAttachmentId | ATTACHMENT_ID | — | ✅ |
| 6 | AssignmentRecordDEOAttributionId | ATTRIBUTION_ID | — | ✅ |
| 7 | AssignmentRecordDEOAttributionLookupCode | ATTRIBUTION_LOOKUP_CODE | — | — |
| 8 | AssignmentRecordDEOAttributionType | ATTRIBUTION_TYPE | — | ✅ |
| 9 | AssignmentRecordDEOCalculatedDueDate | CALCULATED_DUE_DATE | — | ✅ |
| 10 | AssignmentRecordDEOCompletionDate | COMPLETION_DATE | — | ✅ |
| 11 | AssignmentRecordDEOCreatedBy | CREATED_BY | — | ✅ |
| 12 | AssignmentRecordDEOCreationDate | CREATION_DATE | — | ✅ |
| 13 | AssignmentRecordDEODateStatusChanged | DATE_STATUS_CHANGED | — | ✅ |
| 14 | AssignmentRecordDEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 15 | AssignmentRecordDEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 16 | AssignmentRecordDEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 17 | AssignmentRecordDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | — | ✅ |
| 18 | AssignmentRecordDEOEventCreatedById | EVENT_CREATED_BY_ID | — | — |
| 19 | AssignmentRecordDEOEventSubType | EVENT_SUB_TYPE | — | — |
| 20 | AssignmentRecordDEOEventType | EVENT_TYPE | — | — |
| 21 | AssignmentRecordDEOExpirationDate | EXPIRATION_DATE | — | ✅ |
| 22 | AssignmentRecordDEOIsHistoryFlag | IS_HISTORY_FLAG | — | ✅ |
| 23 | AssignmentRecordDEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | AssignmentRecordDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | AssignmentRecordDEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | AssignmentRecordDEOLearnerId | LEARNER_ID | — | ✅ |
| 27 | AssignmentRecordDEOLearningItemId | LEARNING_ITEM_ID | — | — |
| 28 | AssignmentRecordDEOLiEffectiveDate | LI_EFFECTIVE_DATE | — | ✅ |
| 29 | AssignmentRecordDEONotificationStatus | NOTIFICATION_STATUS | — | ✅ |
| 30 | AssignmentRecordDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 31 | AssignmentRecordDEOPreAssignmentRecordId | PRE_ASSIGNMENT_RECORD_ID | — | — |
| 32 | AssignmentRecordDEOPricingRuleId | PRICING_RULE_ID | — | — |
| 33 | AssignmentRecordDEOReasonCode | REASON_CODE | — | ✅ |
| 34 | AssignmentRecordDEORequestDetailId | REQUEST_DETAIL_ID | — | — |
| 35 | AssignmentRecordDEOSourceId | SOURCE_ID | — | ✅ |
| 36 | AssignmentRecordDEOSourceInfo | SOURCE_INFO | — | ✅ |
| 37 | AssignmentRecordDEOSourceType | SOURCE_TYPE | — | ✅ |
| 38 | AssignmentRecordDEOStatus | STATUS | — | ✅ |
| 39 | AssignmentRecordDEOStatusChangeComment | STATUS_CHANGE_COMMENT | — | ✅ |
| 40 | AssignmentRecordDEOStatusChangeType | STATUS_CHANGE_TYPE | — | ✅ |
| 41 | AssignmentRecordDEOSubStatus | SUB_STATUS | — | ✅ |
| 42 | AssignmentRecordDEOSuccAssignmentRecordId | SUCC_ASSIGNMENT_RECORD_ID | — | — |
| 43 | AssignmentRecordDEOTotalLearningTime | TOTAL_LEARNING_TIME | — | ✅ |
| 44 | AssignmentRecordDEOTransactionDetailsRuleId | TRANSACTION_DETAILS_RULE_ID | — | ✅ |
| 45 | AssignmentRecordDEOValidityDate | VALIDITY_DATE | — | ✅ |

### [[wlf_assignment_rules|WLF_ASSIGNMENT_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentRulePEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | ✅ |
| 2 | AssignmentRulePEOCreatedBy | CREATED_BY | — | — |
| 3 | AssignmentRulePEOCreationDate | CREATION_DATE | — | — |
| 4 | AssignmentRulePEODynDueDate | DYN_DUE_DATE | — | — |
| 5 | AssignmentRulePEODynDueDateOption | DYN_DUE_DATE_OPTION | — | — |
| 6 | AssignmentRulePEODynDueInDays | DYN_DUE_IN_DAYS | — | — |
| 7 | AssignmentRulePEODynEnabled | DYN_ENABLED | — | ✅ |
| 8 | AssignmentRulePEODynStopNewDate | DYN_STOP_NEW_DATE | — | — |
| 9 | AssignmentRulePEODynStopWithdrawDate | DYN_STOP_WITHDRAW_DATE | — | — |
| 10 | AssignmentRulePEODynWithdrawOption | DYN_WITHDRAW_OPTION | — | ✅ |
| 11 | AssignmentRulePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 12 | AssignmentRulePEOExpiryDate | EXPIRY_DATE | — | ✅ |
| 13 | AssignmentRulePEOExpiryInDays | EXPIRY_IN_DAYS | — | ✅ |
| 14 | AssignmentRulePEOExpiryInNumYrs | EXPIRY_IN_NUM_YRS | — | ✅ |
| 15 | AssignmentRulePEOExpiryOption | EXPIRY_OPTION | — | ✅ |
| 16 | AssignmentRulePEOInitialDueDate | INITIAL_DUE_DATE | — | ✅ |
| 17 | AssignmentRulePEOInitialDueDateOption | INITIAL_DUE_DATE_OPTION | — | ✅ |
| 18 | AssignmentRulePEOInitialDueInDays | INITIAL_DUE_IN_DAYS | — | ✅ |
| 19 | AssignmentRulePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 20 | AssignmentRulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 21 | AssignmentRulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 22 | AssignmentRulePEOLearningItemEffectivity | LEARNING_ITEM_EFFECTIVITY | — | ✅ |
| 23 | AssignmentRulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | AssignmentRulePEORenewalBeforeExpiryDays | RENEWAL_BEFORE_EXPIRY_DAYS | — | ✅ |
| 25 | AssignmentRulePEORenewalOptions | RENEWAL_OPTIONS | — | ✅ |
| 26 | AssignmentRulePEOValidityOption | VALIDITY_OPTION | — | ✅ |

### [[wlf_event_assignments_f|WLF_EVENT_ASSIGNMENTS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAssignmentDEOAssignmentProfileNumber | ASSIGNMENT_PROFILE_NUMBER | — | ✅ |
| 2 | EventAssignmentDEOAssignmentRuleId | ASSIGNMENT_RULE_ID | — | ✅ |
| 3 | EventAssignmentDEOAssignmentStartDate | ASSIGNMENT_START_DATE | — | — |
| 4 | EventAssignmentDEOComments | COMMENTS | — | — |
| 5 | EventAssignmentDEOCreatedBy | CREATED_BY | — | — |
| 6 | EventAssignmentDEOCreationDate | CREATION_DATE | — | — |
| 7 | EventAssignmentDEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | EventAssignmentDEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | EventAssignmentDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | EventAssignmentDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | — | ✅ |
| 11 | EventAssignmentDEOEventId | EVENT_ID | — | ✅ |
| 12 | EventAssignmentDEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 13 | EventAssignmentDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | EventAssignmentDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 15 | EventAssignmentDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | EventAssignmentDEOProcessedDate | PROCESSED_DATE | — | ✅ |
| 17 | EventAssignmentDEORequestDetailId | REQUEST_DETAIL_ID | — | — |
| 18 | EventAssignmentDEOStatus | STATUS | — | ✅ |

### [[wlf_event_assignments_f_tl|WLF_EVENT_ASSIGNMENTS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventAssignmentTranslationDEOComments | COMMENTS | — | ✅ |
| 2 | EventAssignmentTranslationDEOCreatedBy | CREATED_BY | — | — |
| 3 | EventAssignmentTranslationDEOCreationDate | CREATION_DATE | — | — |
| 4 | EventAssignmentTranslationDEODescription | DESCRIPTION | — | ✅ |
| 5 | EventAssignmentTranslationDEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | EventAssignmentTranslationDEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 7 | EventAssignmentTranslationDEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | EventAssignmentTranslationDEOEventAssignmentId | EVENT_ASSIGNMENT_ID | — | — |
| 9 | EventAssignmentTranslationDEOLanguage | LANGUAGE | — | — |
| 10 | EventAssignmentTranslationDEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | EventAssignmentTranslationDEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | EventAssignmentTranslationDEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | EventAssignmentTranslationDEOName | NAME | — | ✅ |
| 14 | EventAssignmentTranslationDEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | EventAssignmentTranslationDEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
