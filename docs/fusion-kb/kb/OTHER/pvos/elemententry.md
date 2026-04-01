---
id: DOC-OTHER-PVO-ElementEntry
doc_type: system-doc
title: "ElementEntry — PVO Cross-Module"
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
  - ElementEntry
  - elemententry
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementEntry

## 📌 Visão Geral

View Object para extração BICC de dados de Element Entry. Acessa as tabelas: PAY_ELEMENT_ENTRIES_VL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementEntry`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 3 | 28 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_entries_vl|PAY_ELEMENT_ENTRIES_VL]] — 36 atributos (3 PKs, 28 BICC)

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
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | EffectiveEndDate1 | EFFECTIVE_END_DATE1 | — | — |
| 9 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | EffectiveStartDate1 | EFFECTIVE_START_DATE1 | — | — |
| 11 | ElementEntryDPEOCreatorId | CREATOR_ID | — | — |
| 12 | ElementEntryDPEOCreatorTypeCode | CREATOR_TYPE_CODE | — | ✅ |
| 13 | ElementEntryDPEOElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 14 | ElementEntryDPEOEntryTypeCode | ENTRY_TYPE_CODE | — | ✅ |
| 15 | ElementEntryDPEOPersonId | PERSON_ID | — | ✅ |
| 16 | ElementEntryDPEOReasonCode | REASON | — | ✅ |
| 17 | ElementEntryDPEOSubpriority | SUBPRIORITY | — | ✅ |
| 18 | ElementEntryId | ELEMENT_ENTRY_ID | 🔑 | ✅ |
| 19 | ElementEntryUsagesPEOAssignedPayrollId | ASSIGNED_PAYROLL_ID | — | ✅ |
| 20 | ElementEntryUsagesPEODateFrom | DATE_FROM | — | ✅ |
| 21 | ElementEntryUsagesPEODateTo | DATE_TO | — | ✅ |
| 22 | ElementEntryUsagesPEOPayrollAssignmentId | PAYROLL_ASSIGNMENT_ID | — | ✅ |
| 23 | ElementEntryUsagesPEOPayrollRelationshipId | PAYROLL_RELATIONSHIP_ID | — | ✅ |
| 24 | ElementEntryUsagesPEOPayrollTermId | PAYROLL_TERM_ID | — | ✅ |
| 25 | ElementEntryUsagesPEOUsageLevelCode | USAGE_LEVEL_CODE | — | ✅ |
| 26 | EntryReasonLookupPEOReason | REASON_LOOKUP_MEANING | — | — |
| 27 | EntrySequenceNumber | MULTIPLE_ENTRY_COUNT | — | ✅ |
| 28 | EntryTypeLookupPEOEntryType | ENTRY_TYPE | — | ✅ |
| 29 | EntryUsagesLookupPEOUsageLevel | USAGE_LEVEL | — | ✅ |
| 30 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 31 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 33 | PayAssignedPayrollPEOPayrollId | PAYROLL_ID | — | ✅ |
| 34 | ProcessedFlag | PROCESSED_FLAG | — | ✅ |
| 35 | RetroFlag | RETRO_FLAG | — | ✅ |
| 36 | StandardLinkFlag | STANDARD_LINK_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
