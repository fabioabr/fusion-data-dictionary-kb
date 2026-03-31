---
id: DOC-OTHER-PVO-ActionOccurrencesPVO
doc_type: system-doc
title: "ActionOccurrencesPVO — PVO Cross-Module"
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
  - ActionOccurrencesPVO
  - actionoccurrencespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionOccurrencesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Occurrences. Acessa as tabelas: PER_ACTIONS_B, PER_ACTION_OCCURRENCES, PER_ACTION_REASONS_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionOccurrencesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 70 | 4 | 1 | 7 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[per_actions_b|PER_ACTIONS_B]] — 16 atributos (1 BICC)
- [[per_action_occurrences|PER_ACTION_OCCURRENCES]] — 32 atributos (1 PKs, 4 BICC)
- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 12 atributos (1 BICC)
- [[per_action_types_b|PER_ACTION_TYPES_B]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[per_actions_b|PER_ACTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionsPEOActInformation1 | ACT_INFORMATION1 | — | — |
| 2 | ActionsPEOActInformation2 | ACT_INFORMATION2 | — | — |
| 3 | ActionsPEOActionCode | ACTION_CODE | — | — |
| 4 | ActionsPEOActionId | ACTION_ID | — | — |
| 5 | ActionsPEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 6 | ActionsPEOActionTypeId | ACTION_TYPE_ID | — | — |
| 7 | ActionsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | ActionsPEOCreatedBy | CREATED_BY | — | — |
| 9 | ActionsPEOCreationDate | CREATION_DATE | — | — |
| 10 | ActionsPEOEndDate | END_DATE | — | — |
| 11 | ActionsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ActionsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | ActionsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | ActionsPEOModuleId | MODULE_ID | — | — |
| 15 | ActionsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | ActionsPEOStartDate | START_DATE | — | — |

### [[per_action_occurrences|PER_ACTION_OCCURRENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | 🔑 | ✅ |
| 2 | ActionOccurrencesPEOActionDate | ACTION_DATE | — | — |
| 3 | ActionOccurrencesPEOActionId | ACTION_ID | — | ✅ |
| 4 | ActionOccurrencesPEOActionReasonId | ACTION_REASON_ID | — | ✅ |
| 5 | ActionOccurrencesPEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 6 | ActionOccurrencesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | ActionOccurrencesPEOCreatedBy | CREATED_BY | — | — |
| 8 | ActionOccurrencesPEOCreationDate | CREATION_DATE | — | — |
| 9 | ActionOccurrencesPEOEntityId | ENTITY_ID | — | — |
| 10 | ActionOccurrencesPEOEntityType | ENTITY_TYPE | — | — |
| 11 | ActionOccurrencesPEOFreezeStartDate | FREEZE_START_DATE | — | — |
| 12 | ActionOccurrencesPEOFreezeUntilDate | FREEZE_UNTIL_DATE | — | — |
| 13 | ActionOccurrencesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ActionOccurrencesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ActionOccurrencesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ActionOccurrencesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 17 | ActionOccurrencesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | ActionOccurrencesPEOParentEntityKeyId | PARENT_ENTITY_KEY_ID | — | — |
| 19 | ActionOccurrencesPEOParentEntityType | PARENT_ENTITY_TYPE | — | — |
| 20 | ActionOccurrencesPEOProposedActionId | PROPOSED_ACTION_ID | — | — |
| 21 | ActionOccurrencesPEOProposedActionType | PROPOSED_ACTION_TYPE | — | — |
| 22 | ActionOccurrencesPEOProposedReasonId | PROPOSED_REASON_ID | — | — |
| 23 | ActionOccurrencesPEOProposedStartDate | PROPOSED_START_DATE | — | — |
| 24 | ActionOccurrencesPEOProposedWorkerType | PROPOSED_WORKER_TYPE | — | — |
| 25 | ActionOccurrencesPEORefActionOccurrenceId | REF_ACTION_OCCURRENCE_ID | — | — |
| 26 | ActionOccurrencesPEOSubmittedBy | SUBMITTED_BY | — | — |
| 27 | SourceAOPEOActionDate | ACTION_DATE | — | — |
| 28 | SourceAOPEOActionId | ACTION_ID | — | — |
| 29 | SourceAOPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 30 | SourceAOPEOActionReasonId | ACTION_REASON_ID | — | — |
| 31 | SourceAOPEOEntityId | ENTITY_ID | — | — |
| 32 | SourceAOPEOEntityType | ENTITY_TYPE | — | — |

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsPEOActionReasonCode | ACTION_REASON_CODE | — | — |
| 2 | ActionReasonsPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionReasonsPEOCreatedBy | CREATED_BY | — | — |
| 5 | ActionReasonsPEOCreationDate | CREATION_DATE | — | — |
| 6 | ActionReasonsPEOEndDate | END_DATE | — | — |
| 7 | ActionReasonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionReasonsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActionReasonsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ActionReasonsPEOModuleId | MODULE_ID | — | — |
| 11 | ActionReasonsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ActionReasonsPEOStartDate | START_DATE | — | — |

### [[per_action_types_b|PER_ACTION_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionTypesPEOActionTypeCode | ACTION_TYPE_CODE | — | — |
| 2 | ActionTypesPEOActionTypeId | ACTION_TYPE_ID | — | — |
| 3 | ActionTypesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionTypesPEOCreatedBy | CREATED_BY | — | — |
| 5 | ActionTypesPEOCreationDate | CREATION_DATE | — | — |
| 6 | ActionTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ActionTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ActionTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ActionTypesPEOModuleId | MODULE_ID | — | — |
| 10 | ActionTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
