---
id: DOC-OTHER-PVO-ElementEntryPVO
doc_type: system-doc
title: "ElementEntryPVO — PVO Cross-Module"
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
  - ElementEntryPVO
  - elemententrypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementEntryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Element Entry. Acessa as tabelas: PAY_ELEMENT_ENTRIES_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementEntryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 1 | 1 | 29 | 85% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_entries_vl|PAY_ELEMENT_ENTRIES_VL]] — 34 atributos (1 PKs, 29 BICC)

---

## ⚙️ Atributos

### [[pay_element_entries_vl|PAY_ELEMENT_ENTRIES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdditionalFlag | ADDITIONAL_FLAG | — | — |
| 2 | AdjustFlag | ADJUST_FLAG | — | — |
| 3 | AssignmentId | ASSIGNMENT_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | CreatorTypeLookupPEOCreatorType | CREATOR_TYPE | — | ✅ |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 9 | ElementEntryDPEOReasonCode | REASON | — | ✅ |
| 10 | ElementEntryId | ELEMENT_ENTRY_ID | 🔑 | ✅ |
| 11 | ElementEntryPEOCreatorId | CREATOR_ID | — | — |
| 12 | ElementEntryPEOCreatorTypeCode | CREATOR_TYPE_CODE | — | ✅ |
| 13 | ElementEntryPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 14 | ElementEntryPEOEntryTypeCode | ENTRY_TYPE_CODE | — | ✅ |
| 15 | ElementEntryPEOPersonId | PERSON_ID | — | ✅ |
| 16 | ElementEntryPEOSubpriority | SUBPRIORITY | — | ✅ |
| 17 | ElementEntryUsagesPEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | — | ✅ |
| 18 | ElementEntryUsagesPEODateFrom | DATE_FROM | — | ✅ |
| 19 | ElementEntryUsagesPEODateTo | DATE_TO | — | ✅ |
| 20 | ElementEntryUsagesPEOPayrollAssignmentId | PAYROLL_ASSIGNMENT_ID | — | ✅ |
| 21 | ElementEntryUsagesPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | ✅ |
| 22 | ElementEntryUsagesPEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 23 | ElementEntryUsagesPEOUsageLevelCode | USAGE_LEVEL_CODE | — | ✅ |
| 24 | EntryReasonLookupPEOReason | REASON_LOOKUP_MEANING | — | ✅ |
| 25 | EntrySequenceNumber | MULTIPLE_ENTRY_COUNT | — | ✅ |
| 26 | EntryTypeLookupPEOEntryType | ENTRY_TYPE | — | ✅ |
| 27 | EntryUsagesLookupPEOUsageLevel | USAGE_LEVEL | — | ✅ |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 31 | PayAssignedPayrollPEOPayrollId | PAYROLL_ID | — | ✅ |
| 32 | ProcessedFlag | PROCESSED_FLAG | — | ✅ |
| 33 | RetroFlag | RETRO_FLAG | — | ✅ |
| 34 | StandardLinkFlag | STANDARD_LINK_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
