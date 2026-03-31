---
id: DOC-OTHER-PVO-MaintenanceConditionEvent
doc_type: system-doc
title: "MaintenanceConditionEvent — PVO Cross-Module"
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
  - MaintenanceConditionEvent
  - maintenanceconditionevent
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MaintenanceConditionEvent

## 📌 Visão Geral

View Object para extração BICC de dados de Maintenance Condition Event. Acessa as tabelas: CSE_CONDITION_EVENT_CODES_B, CSE_CONDITION_EVENT_CODES_TL, MNT_WR_CONDITION_EVENTS.

**Caminho:** `FscmTopModelAM.MaintProgramAM.MaintenanceConditionEvent`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 3 | 1 | 9 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]] — 13 atributos (3 BICC)
- [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]] — 11 atributos (3 BICC)
- [[mnt_wr_condition_events|MNT_WR_CONDITION_EVENTS]] — 13 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[cse_condition_event_codes_b|CSE_CONDITION_EVENT_CODES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventCodePEOActiveEndDate | ACTIVE_END_DATE | — | — |
| 2 | EventCodePEOConditionEventCode | CONDITION_EVENT_CODE | — | ✅ |
| 3 | EventCodePEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | — |
| 4 | EventCodePEOConditionEventTypeCode | CONDITION_EVENT_TYPE_CODE | — | ✅ |
| 5 | EventCodePEOCreatedBy | CREATED_BY | — | — |
| 6 | EventCodePEOCreationDate | CREATION_DATE | — | — |
| 7 | EventCodePEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 8 | EventCodePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 9 | EventCodePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | EventCodePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | EventCodePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | EventCodePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | EventCodePEORequestId | REQUEST_ID | — | — |

### [[cse_condition_event_codes_tl|CSE_CONDITION_EVENT_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventCodeTLPEOConditionEventCodeDesc | CONDITION_EVENT_CODE_DESC | — | ✅ |
| 2 | EventCodeTLPEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | — |
| 3 | EventCodeTLPEOConditionEventCodeName | CONDITION_EVENT_CODE_NAME | — | ✅ |
| 4 | EventCodeTLPEOCreatedBy | CREATED_BY | — | — |
| 5 | EventCodeTLPEOCreationDate | CREATION_DATE | — | — |
| 6 | EventCodeTLPEOLanguage | LANGUAGE | — | — |
| 7 | EventCodeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | EventCodeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | EventCodeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | EventCodeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | EventCodeTLPEOSourceLang | SOURCE_LANG | — | — |

### [[mnt_wr_condition_events|MNT_WR_CONDITION_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EventPEOConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | — |
| 2 | EventPEOCreatedBy | CREATED_BY | — | — |
| 3 | EventPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | EventPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 5 | EventPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 6 | EventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | EventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | EventPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | EventPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | EventPEOOrganizationId | ORGANIZATION_ID | — | — |
| 11 | EventPEORequestId | REQUEST_ID | — | — |
| 12 | EventPEORequirementConditionEventId | REQUIREMENT_CONDITION_EVENT_ID | 🔑 | ✅ |
| 13 | EventPEORequirementId | REQUIREMENT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
