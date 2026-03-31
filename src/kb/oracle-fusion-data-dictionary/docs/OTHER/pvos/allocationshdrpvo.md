---
id: DOC-OTHER-PVO-AllocationsHdrPVO
doc_type: system-doc
title: "AllocationsHdrPVO — PVO Cross-Module"
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
  - AllocationsHdrPVO
  - allocationshdrpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocationsHdrPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Allocations Hdr. Acessa as tabelas: HWM_ALLOCATIONS_HDR_F, HWM_ALLOCATIONS_HDR_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeAllocationsAM.AllocationsHdrPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 3 | 10 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_allocations_hdr_f|HWM_ALLOCATIONS_HDR_F]] — 13 atributos (3 PKs, 9 BICC)
- [[hwm_allocations_hdr_tl|HWM_ALLOCATIONS_HDR_TL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hwm_allocations_hdr_f|HWM_ALLOCATIONS_HDR_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocHdrBPEOAllocationId | ALLOCATION_ID | 🔑 | ✅ |
| 2 | AllocHdrBPEOAllocationName | ALLOCATION_NAME | — | ✅ |
| 3 | AllocHdrBPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AllocHdrBPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AllocHdrBPEODataLevel | DATA_LEVEL | — | — |
| 6 | AllocHdrBPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | AllocHdrBPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | AllocHdrBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | AllocHdrBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AllocHdrBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | AllocHdrBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AllocHdrBPEOModuleId | MODULE_ID | — | — |
| 13 | AllocHdrBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hwm_allocations_hdr_tl|HWM_ALLOCATIONS_HDR_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocHdrTLPEOAllocationId | ALLOCATION_ID | — | — |
| 2 | AllocHdrTLPEODescription | DESCRIPTION | — | ✅ |
| 3 | AllocHdrTLPEOLanguage | LANGUAGE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
