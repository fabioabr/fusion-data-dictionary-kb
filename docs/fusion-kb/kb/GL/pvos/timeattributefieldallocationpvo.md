---
id: DOC-GL-PVO-TimeAttributeFieldAllocationPVO
doc_type: system-doc
title: "TimeAttributeFieldAllocationPVO — PVO General Ledger"
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
  - TimeAttributeFieldAllocationPVO
  - timeattributefieldallocationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeAttributeFieldAllocationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Attribute Field Allocation. Acessa as tabelas: FND_VS_VALUE_SETS, HWM_DATA_SOURCE_USAGES_V, HWM_TCSMRS_VL (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DataDictionaryAM.TimeAttributeFieldAllocationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 6 | 1 | 9 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos
- [[hwm_data_source_usages_v|HWM_DATA_SOURCE_USAGES_V]] — 22 atributos
- [[hwm_tcsmrs_vl|HWM_TCSMRS_VL]] — 3 atributos
- [[hwm_tm_atrb_flds_b|HWM_TM_ATRB_FLDS_B]] — 23 atributos (1 PKs, 7 BICC)
- [[hwm_tm_atrb_flds_tl|HWM_TM_ATRB_FLDS_TL]] — 4 atributos (2 BICC)
- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 6 atributos

---

## ⚙️ Atributos

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetsBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 2 | ValueSetsBPEOValueSetCode | VALUE_SET_CODE | — | — |
| 3 | ValueSetsBPEOValueSetId | VALUE_SET_ID | — | — |

### [[hwm_data_source_usages_v|HWM_DATA_SOURCE_USAGES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminDataSrcUsgsPEOAdminDsFlag | ADMIN_DS_FLAG | — | — |
| 2 | AdminDataSrcUsgsPEODataSourceCode | DATA_SOURCE_CODE | — | — |
| 3 | AdminDataSrcUsgsPEODataSourceId | DATA_SOURCE_ID | — | — |
| 4 | AdminDataSrcUsgsPEODataSourceUsageId | DATA_SOURCE_USAGE_ID | — | — |
| 5 | AdminDataSrcUsgsPEODisplayName | DISPLAY_NAME | — | — |
| 6 | AdminDefaultDataSrcUsgsPEOAdminDsFlag | ADMIN_DS_FLAG | — | — |
| 7 | AdminDefaultDataSrcUsgsPEODataSourceCode | DATA_SOURCE_CODE | — | — |
| 8 | AdminDefaultDataSrcUsgsPEODataSourceId | DATA_SOURCE_ID | — | — |
| 9 | AdminDefaultDataSrcUsgsPEODataSourceUsageId | DATA_SOURCE_USAGE_ID | — | — |
| 10 | AdminDefaultDataSrcUsgsPEODefaultFlag | DEFAULT_FLAG | — | — |
| 11 | AdminDefaultDataSrcUsgsPEODisplayName | DISPLAY_NAME | — | — |
| 12 | UserDataSrcUsgsPEODataSourceCode | DATA_SOURCE_CODE | — | — |
| 13 | UserDataSrcUsgsPEODataSourceId | DATA_SOURCE_ID | — | — |
| 14 | UserDataSrcUsgsPEODataSourceUsageId | DATA_SOURCE_USAGE_ID | — | — |
| 15 | UserDataSrcUsgsPEODisplayName | DISPLAY_NAME | — | — |
| 16 | UserDataSrcUsgsPEOUserDsFlag | USER_DS_FLAG | — | — |
| 17 | UserDefaultDataSrcUsgsPEODataSourceCode | DATA_SOURCE_CODE | — | — |
| 18 | UserDefaultDataSrcUsgsPEODataSourceId | DATA_SOURCE_ID | — | — |
| 19 | UserDefaultDataSrcUsgsPEODataSourceUsageId | DATA_SOURCE_USAGE_ID | — | — |
| 20 | UserDefaultDataSrcUsgsPEODefaultFlag | DEFAULT_FLAG | — | — |
| 21 | UserDefaultDataSrcUsgsPEODisplayName | DISPLAY_NAME | — | — |
| 22 | UserDefaultDataSrcUsgsPEOUserDsFlag | USER_DS_FLAG | — | — |

### [[hwm_tcsmrs_vl|HWM_TCSMRS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeConsumerVLPEOName | NAME | — | — |
| 2 | TimeConsumerVLPEOTcsmrsCode | TCSMRS_CODE | — | — |
| 3 | TimeConsumerVLPEOTcsmrsId | TCSMRS_ID | — | — |

### [[hwm_tm_atrb_flds_b|HWM_TM_ATRB_FLDS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowedScope | ALLOWED_SCOPE | — | — |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | AttributeGroup | ATTRIBUTE_GROUP | — | — |
| 4 | AttributeType | ATTRIBUTE_TYPE | — | — |
| 5 | Class11 | CLASS | — | — |
| 6 | ComponentDisplayCode | COMP_DISP_CODE | — | — |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | EnterpriseId | ENTERPRISE_ID | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | MandatoryForTimeConsumers | MANDATORY_FOR_TCSMRS | — | — |
| 14 | ModuleId | MODULE_ID | — | — |
| 15 | Name | NAME | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ParentTimeAttributeFieldId | PARENT_TM_ATRB_FLD_ID | — | — |
| 18 | TimeAttributeFieldId | TM_ATRB_FLD_ID | 🔑 | ✅ |
| 19 | TimeAttributeFieldPEOBaseUnit | BASE_UNIT | — | — |
| 20 | TimeAttributeFieldPEOGlobalTmAtrbFldId | GLOBAL_TM_ATRB_FLD_ID | — | — |
| 21 | TimeConsumersId | TCSMRS_ID | — | — |
| 22 | ValueLocation | VALUE_LOCATION | — | — |
| 23 | ValueSetId | VALUE_SET_ID | — | — |

### [[hwm_tm_atrb_flds_tl|HWM_TM_ATRB_FLDS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAttributeFieldId1 | TM_ATRB_FLD_ID | — | ✅ |
| 2 | TimeAttributeFieldTranslationPEOLanguage | LANGUAGE | — | — |
| 3 | TmAtrbFldTLPEODescription | DESCRIPTION | — | — |
| 4 | TmAtrbFldTLPEODisplayName | DISPLAY_NAME | — | ✅ |

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlobalTmAtrbFldVLPEODisplayName | DISPLAY_NAME | — | — |
| 2 | GlobalTmAtrbFldVLPEOName | NAME | — | — |
| 3 | GlobalTmAtrbFldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | — |
| 4 | ParentTmAtrbFldVLPEODisplayName | DISPLAY_NAME | — | — |
| 5 | ParentTmAtrbFldVLPEOName | NAME | — | — |
| 6 | ParentTmAtrbFldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
