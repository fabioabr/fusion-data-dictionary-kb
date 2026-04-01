---
id: DOC-OTHER-PVO-AllocationRulesPVO
doc_type: system-doc
title: "AllocationRulesPVO — PVO Cross-Module"
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
  - AllocationRulesPVO
  - allocationrulespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocationRulesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Allocation Rules. Acessa as tabelas: HWM_ALLOCATIONS_HDR_F, HWM_ALLOCATIONS_HDR_TL, HWM_ALLOCATION_RULES_F (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeAllocationsAM.AllocationRulesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 4 | 3 | 23 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_allocations_hdr_f|HWM_ALLOCATIONS_HDR_F]] — 13 atributos (7 BICC)
- [[hwm_allocations_hdr_tl|HWM_ALLOCATIONS_HDR_TL]] — 3 atributos (1 BICC)
- [[hwm_allocation_rules_f|HWM_ALLOCATION_RULES_F]] — 17 atributos (3 PKs, 13 BICC)
- [[hwm_tcats_vl|HWM_TCATS_VL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_allocations_hdr_f|HWM_ALLOCATIONS_HDR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocHdrBPEOAllocationId | ALLOCATION_ID | — | — |
| 2 | AllocHdrBPEOAllocationName | ALLOCATION_NAME | — | ✅ |
| 3 | AllocHdrBPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AllocHdrBPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AllocHdrBPEODataLevel | DATA_LEVEL | — | — |
| 6 | AllocHdrBPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | AllocHdrBPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | AllocHdrBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | AllocHdrBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AllocHdrBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | AllocHdrBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AllocHdrBPEOModuleId | MODULE_ID | — | — |
| 13 | AllocHdrBPEOObjectVersionNum | OBJECT_VERSION_NUMBER | — | — |

### [[hwm_allocations_hdr_tl|HWM_ALLOCATIONS_HDR_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocHdrTLPEOAllocationId | ALLOCATION_ID | — | — |
| 2 | AllocHdrTLPEODescription | DESCRIPTION | — | ✅ |
| 3 | AllocHdrTLPEOLanguage | LANGUAGE | — | — |

### [[hwm_allocation_rules_f|HWM_ALLOCATION_RULES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocRulesPEOAllocationId | ALLOCATION_ID | — | ✅ |
| 2 | AllocRulesPEOAllocationRuleId | ALLOCATION_RULE_ID | 🔑 | ✅ |
| 3 | AllocRulesPEOAllocationRulePriority | ALLOCATION_RULE_PRIORITY | — | ✅ |
| 4 | AllocRulesPEOAllocationType | ALLOCATION_TYPE | — | ✅ |
| 5 | AllocRulesPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | AllocRulesPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | AllocRulesPEODataLevel | DATA_LEVEL | — | — |
| 8 | AllocRulesPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 9 | AllocRulesPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | AllocRulesPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | AllocRulesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AllocRulesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | AllocRulesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AllocRulesPEOModuleId | MODULE_ID | — | — |
| 15 | AllocRulesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | AllocRulesPEORunSummationLevel | RUN_SUMMATION_LEVEL | — | ✅ |
| 17 | AllocRulesPEOTimeCategoryId | TCAT_ID | — | ✅ |

### [[hwm_tcats_vl|HWM_TCATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryVLPEOTcatCd | TCAT_CD | — | ✅ |
| 2 | TimeCategoryVLPEOTcatId | TCAT_ID | — | — |
| 3 | TimeCategoryVLPEOTcatName | TCAT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
