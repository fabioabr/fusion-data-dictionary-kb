---
id: DOC-OTHER-PVO-TcdMappingPVO
doc_type: system-doc
title: "TcdMappingPVO — PVO Cross-Module"
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
  - TcdMappingPVO
  - tcdmappingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TcdMappingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tcd Mapping. Acessa as tabelas: HWM_TCD_MAPPINGS_B, HWM_TCD_MAPPINGS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.MappingAM.TcdMappingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 12 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcd_mappings_b|HWM_TCD_MAPPINGS_B]] — 14 atributos (1 PKs, 10 BICC)
- [[hwm_tcd_mappings_tl|HWM_TCD_MAPPINGS_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_tcd_mappings_b|HWM_TCD_MAPPINGS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TcdMappingBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TcdMappingBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | TcdMappingBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TcdMappingBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TcdMappingBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TcdMappingBPEOModuleId | MODULE_ID | — | — |
| 8 | TcdMappingBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | TcdMappingBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 10 | TcdMappingBPEOTcdEventCd | TCD_EVENT_CD | — | ✅ |
| 11 | TcdMappingBPEOTcdMappingCd | TCD_MAPPING_CD | — | ✅ |
| 12 | TcdMappingBPEOTcdMappingId | TCD_MAPPING_ID | 🔑 | ✅ |
| 13 | TcdMappingBPEOVendorCd | VENDOR_CD | — | ✅ |
| 14 | TcdMappingBPEOWfmEventInOut | WFM_EVENT_IN_OUT | — | ✅ |

### [[hwm_tcd_mappings_tl|HWM_TCD_MAPPINGS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TcdMappingTLPEOLanguage | LANGUAGE | — | — |
| 3 | TcdMappingTLPEOName | NAME | — | ✅ |
| 4 | TcdMappingTLPEOTcdMappingId | TCD_MAPPING_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
