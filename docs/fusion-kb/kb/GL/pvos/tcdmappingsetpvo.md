---
id: DOC-GL-PVO-TcdMappingSetPVO
doc_type: system-doc
title: "TcdMappingSetPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TcdMappingSetPVO
  - tcdmappingsetpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TcdMappingSetPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tcd Mapping Set. Acessa as tabelas: HWM_TCD_MAPPING_SETS_B, HWM_TCD_MAPPING_SETS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.MappingAM.TcdMappingSetPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 2 | 1 | 9 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcd_mapping_sets_b|HWM_TCD_MAPPING_SETS_B]] — 11 atributos (1 PKs, 7 BICC)
- [[hwm_tcd_mapping_sets_tl|HWM_TCD_MAPPING_SETS_TL]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_tcd_mapping_sets_b|HWM_TCD_MAPPING_SETS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingSetBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TcdMappingSetBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TcdMappingSetBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | TcdMappingSetBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TcdMappingSetBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TcdMappingSetBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TcdMappingSetBPEOModuleId | MODULE_ID | — | — |
| 8 | TcdMappingSetBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | TcdMappingSetBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 10 | TcdMappingSetBPEOTcdMappingSetCd | TCD_MAPPING_SET_CD | — | ✅ |
| 11 | TcdMappingSetBPEOTcdMappingSetId | TCD_MAPPING_SET_ID | 🔑 | ✅ |

### [[hwm_tcd_mapping_sets_tl|HWM_TCD_MAPPING_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingSetTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TcdMappingSetTLPEOLanguage | LANGUAGE | — | — |
| 3 | TcdMappingSetTLPEOName | NAME | — | ✅ |
| 4 | TcdMappingSetTLPEOTcdMappingSetId | TCD_MAPPING_SET_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
