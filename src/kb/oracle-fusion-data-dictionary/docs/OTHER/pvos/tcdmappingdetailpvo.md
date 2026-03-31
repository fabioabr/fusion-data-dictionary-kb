---
id: DOC-OTHER-PVO-TcdMappingDetailPVO
doc_type: system-doc
title: "TcdMappingDetailPVO — PVO Cross-Module"
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
  - TcdMappingDetailPVO
  - tcdmappingdetailpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TcdMappingDetailPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tcd Mapping Detail. Acessa as tabelas: HWM_TCD_MAPPINGS_B, HWM_TCD_MAPPINGS_TL, HWM_TCD_MAPPING_DTLS (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.MappingAM.TcdMappingDetailPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 44 | 4 | 1 | 32 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcd_mappings_b|HWM_TCD_MAPPINGS_B]] — 14 atributos (10 BICC)
- [[hwm_tcd_mappings_tl|HWM_TCD_MAPPINGS_TL]] — 4 atributos (2 BICC)
- [[hwm_tcd_mapping_dtls|HWM_TCD_MAPPING_DTLS]] — 20 atributos (1 PKs, 16 BICC)
- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 6 atributos (4 BICC)

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
| 12 | TcdMappingBPEOTcdMappingId | TCD_MAPPING_ID | — | ✅ |
| 13 | TcdMappingBPEOVendorCd | VENDOR_CD | — | ✅ |
| 14 | TcdMappingBPEOWfmEventInOut | WFM_EVENT_IN_OUT | — | ✅ |

### [[hwm_tcd_mappings_tl|HWM_TCD_MAPPINGS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TcdMappingTLPEOLanguage | LANGUAGE | — | — |
| 3 | TcdMappingTLPEOName | NAME | — | ✅ |
| 4 | TcdMappingTLPEOTcdMappingId | TCD_MAPPING_ID | — | — |

### [[hwm_tcd_mapping_dtls|HWM_TCD_MAPPING_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcdMappingDetailPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TcdMappingDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TcdMappingDetailPEODateValue | DATE_VALUE | — | ✅ |
| 4 | TcdMappingDetailPEODispValue | DISP_VALUE | — | ✅ |
| 5 | TcdMappingDetailPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | TcdMappingDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TcdMappingDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | TcdMappingDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | TcdMappingDetailPEONumberValue | NUMBER_VALUE | — | ✅ |
| 10 | TcdMappingDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | TcdMappingDetailPEOOrderNumber | ORDER_NUMBER | — | ✅ |
| 12 | TcdMappingDetailPEOParentTmAtrbFldId | PARENT_TM_ATRB_FLD_ID | — | ✅ |
| 13 | TcdMappingDetailPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 14 | TcdMappingDetailPEOStringValue | STRING_VALUE | — | ✅ |
| 15 | TcdMappingDetailPEOTcdMappingDtlId | TCD_MAPPING_DTL_ID | 🔑 | ✅ |
| 16 | TcdMappingDetailPEOTcdMappingId | TCD_MAPPING_ID | — | ✅ |
| 17 | TcdMappingDetailPEOTimestampValue | TIMESTAMP_VALUE | — | ✅ |
| 18 | TcdMappingDetailPEOTmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 19 | TcdMappingDetailPEOValueType | VALUE_TYPE | — | — |
| 20 | TcdMappingDetailPEOWfmEventCd | WFM_EVENT_CD | — | ✅ |

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentTmAtrbFldVLPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ParentTmAtrbFldVLPEOName | NAME | — | ✅ |
| 3 | ParentTmAtrbFldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | — |
| 4 | TmAtrbFldVLPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | TmAtrbFldVLPEOName | NAME | — | ✅ |
| 6 | TmAtrbFldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
