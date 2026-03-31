---
id: DOC-OTHER-PVO-TemplateLayoutCompDisplayValuePVO
doc_type: system-doc
title: "TemplateLayoutCompDisplayValuePVO — PVO Cross-Module"
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
  - TemplateLayoutCompDisplayValuePVO
  - templatelayoutcompdisplayvaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateLayoutCompDisplayValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Layout Comp Display Value. Acessa as tabelas: HWM_TE_ALT_NAMES, HWM_TE_ALT_NAME_VALS_B, HWM_TE_ALT_NAME_VALS_TL (+7).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TemplateLayoutCompDisplayValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 339 | 10 | 3 | 245 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_te_alt_names|HWM_TE_ALT_NAMES]] — 3 atributos (1 PKs, 3 BICC)
- [[hwm_te_alt_name_vals_b|HWM_TE_ALT_NAME_VALS_B]] — 50 atributos (1 PKs, 41 BICC)
- [[hwm_te_alt_name_vals_tl|HWM_TE_ALT_NAME_VALS_TL]] — 3 atributos (1 BICC)
- [[hwm_te_alt_name_vals_vl|HWM_TE_ALT_NAME_VALS_VL]] — 2 atributos (1 BICC)
- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 36 atributos (24 BICC)
- [[hwm_tm_atrb_fld_mstr_ref_vl|HWM_TM_ATRB_FLD_MSTR_REF_VL]] — 3 atributos (2 BICC)
- [[hwm_tm_atrb_fld_set_cmps|HWM_TM_ATRB_FLD_SET_CMPS]] — 150 atributos (117 BICC)
- [[hxt_tclayfld_defns_b|HXT_TCLAYFLD_DEFNS_B]] — 83 atributos (1 PKs, 50 BICC)
- [[hxt_tclayfld_defns_tl|HXT_TCLAYFLD_DEFNS_TL]] — 5 atributos (3 BICC)
- [[hxt_tclayfld_defns_vl|HXT_TCLAYFLD_DEFNS_VL]] — 4 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hwm_te_alt_names|HWM_TE_ALT_NAMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TeAltNamesPEODescription | DESCRIPTION | — | ✅ |
| 2 | TeAltNamesPEOName | NAME | — | ✅ |
| 3 | TeAltNamesPEOTeAltNameId | TE_ALT_NAME_ID | 🔑 | ✅ |

### [[hwm_te_alt_name_vals_b|HWM_TE_ALT_NAME_VALS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltNameValsBPEOAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | AltNameValsBPEOAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | AltNameValsBPEOAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | AltNameValsBPEOAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | AltNameValsBPEOAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | AltNameValsBPEOAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | AltNameValsBPEOAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | AltNameValsBPEOAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | AltNameValsBPEOAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | AltNameValsBPEOAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | AltNameValsBPEOAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | AltNameValsBPEOAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | AltNameValsBPEOAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | AltNameValsBPEOAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | AltNameValsBPEOAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | AltNameValsBPEOAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | AltNameValsBPEOAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | AltNameValsBPEOAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | AltNameValsBPEOAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | AltNameValsBPEOAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | AltNameValsBPEOAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | AltNameValsBPEOAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | AltNameValsBPEOAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | AltNameValsBPEOAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | AltNameValsBPEOAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | AltNameValsBPEOAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | AltNameValsBPEOAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | AltNameValsBPEOAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | AltNameValsBPEOAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | AltNameValsBPEOAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | AltNameValsBPEOCreatedBy | CREATED_BY | — | ✅ |
| 32 | AltNameValsBPEOCreationDate | CREATION_DATE | — | ✅ |
| 33 | AltNameValsBPEODateFrom | DATE_FROM | — | — |
| 34 | AltNameValsBPEODateTo | DATE_TO | — | — |
| 35 | AltNameValsBPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 36 | AltNameValsBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 37 | AltNameValsBPEOExistingFlag | EXISTING_FLAG | — | — |
| 38 | AltNameValsBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | AltNameValsBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 40 | AltNameValsBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 41 | AltNameValsBPEOModuleId | MODULE_ID | — | — |
| 42 | AltNameValsBPEOName | NAME | — | — |
| 43 | AltNameValsBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 44 | AltNameValsBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 45 | AltNameValsBPEOTeAltNameId | TE_ALT_NAME_ID | — | — |
| 46 | AltNameValsBPEOTeAltNameValId | TE_ALT_NAME_VAL_ID | 🔑 | ✅ |
| 47 | AltNameValsBPEOWfmEventInOut | WFM_EVENT_IN_OUT | — | ✅ |
| 48 | TeAltNameValsBPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 49 | TeAltNameValsBPEOManagerActionCd | MANAGER_ACTION_CD | — | ✅ |
| 50 | TeAltNameValsBPEOWorkerActionCd | WORKER_ACTION_CD | — | ✅ |

### [[hwm_te_alt_name_vals_tl|HWM_TE_ALT_NAME_VALS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AltNameValsTLPEOAltNameValue | ALT_NAME_VALUE | — | ✅ |
| 2 | AltNameValsTLPEOLanguage | LANGUAGE | — | — |
| 3 | AltNameValsTLPEOTeAltNameValId | TE_ALT_NAME_VAL_ID | — | — |

### [[hwm_te_alt_name_vals_vl|HWM_TE_ALT_NAME_VALS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DflAltNameValsPEOAltNameValue | ALT_NAME_VALUE | — | ✅ |
| 2 | DflAltNameValsPEOTeAltNameValId | TE_ALT_NAME_VAL_ID | — | — |

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepTCFParentAtrbPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | DepTCFParentAtrbPEOName | NAME | — | ✅ |
| 3 | DepTCFParentAtrbPEOTmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 4 | DflParamTimeAtrbPEODisplayName | DISPLAY_NAME | — | ✅ |
| 5 | DflParamTimeAtrbPEOName | NAME | — | ✅ |
| 6 | DflParamTimeAtrbPEOTmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 7 | FilterAtrbPEO10DisplayName | DISPLAY_NAME | — | ✅ |
| 8 | FilterAtrbPEO10Name | NAME | — | ✅ |
| 9 | FilterAtrbPEO10TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 10 | FilterAtrbPEO1DisplayName | DISPLAY_NAME | — | ✅ |
| 11 | FilterAtrbPEO1Name | NAME | — | ✅ |
| 12 | FilterAtrbPEO1TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 13 | FilterAtrbPEO2DisplayName | DISPLAY_NAME | — | ✅ |
| 14 | FilterAtrbPEO2Name | NAME | — | ✅ |
| 15 | FilterAtrbPEO2TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 16 | FilterAtrbPEO3DisplayName | DISPLAY_NAME | — | ✅ |
| 17 | FilterAtrbPEO3Name | NAME | — | ✅ |
| 18 | FilterAtrbPEO3TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 19 | FilterAtrbPEO4DisplayName | DISPLAY_NAME | — | ✅ |
| 20 | FilterAtrbPEO4Name | NAME | — | ✅ |
| 21 | FilterAtrbPEO4TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 22 | FilterAtrbPEO5DisplayName | DISPLAY_NAME | — | ✅ |
| 23 | FilterAtrbPEO5Name | NAME | — | ✅ |
| 24 | FilterAtrbPEO5TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 25 | FilterAtrbPEO6DisplayName | DISPLAY_NAME | — | ✅ |
| 26 | FilterAtrbPEO6Name | NAME | — | ✅ |
| 27 | FilterAtrbPEO6TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 28 | FilterAtrbPEO7DisplayName | DISPLAY_NAME | — | ✅ |
| 29 | FilterAtrbPEO7Name | NAME | — | ✅ |
| 30 | FilterAtrbPEO7TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 31 | FilterAtrbPEO8DisplayName | DISPLAY_NAME | — | ✅ |
| 32 | FilterAtrbPEO8Name | NAME | — | ✅ |
| 33 | FilterAtrbPEO8TmAtrbFldId | TM_ATRB_FLD_ID | — | — |
| 34 | FilterAtrbPEO9DisplayName | DISPLAY_NAME | — | ✅ |
| 35 | FilterAtrbPEO9Name | NAME | — | ✅ |
| 36 | FilterAtrbPEO9TmAtrbFldId | TM_ATRB_FLD_ID | — | — |

### [[hwm_tm_atrb_fld_mstr_ref_vl|HWM_TM_ATRB_FLD_MSTR_REF_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DepTCFMasterRefPEODIDispName | DET_INS_DISPLAY_NAME | — | ✅ |
| 2 | DepTCFMasterRefPEOMasterInsId | MASTER_INSTANCE_IDENTIFIER | — | ✅ |
| 3 | DepTCFMasterRefPEOMstrRefId | TM_ATRB_FLD_MSTR_REF_ID | — | — |

### [[hwm_tm_atrb_fld_set_cmps|HWM_TM_ATRB_FLD_SET_CMPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TmAtrbFldSetCmpsPEO10CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 2 | TmAtrbFldSetCmpsPEO10DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 3 | TmAtrbFldSetCmpsPEO10ReqFlag | REQUIRED_FLAG | — | ✅ |
| 4 | TmAtrbFldSetCmpsPEO10TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 5 | TmAtrbFldSetCmpsPEO10UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 6 | TmAtrbFldSetCmpsPEO11CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 7 | TmAtrbFldSetCmpsPEO11DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 8 | TmAtrbFldSetCmpsPEO11ReqFlag | REQUIRED_FLAG | — | ✅ |
| 9 | TmAtrbFldSetCmpsPEO11TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 10 | TmAtrbFldSetCmpsPEO11UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 11 | TmAtrbFldSetCmpsPEO12CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 12 | TmAtrbFldSetCmpsPEO12DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 13 | TmAtrbFldSetCmpsPEO12ReqFlag | REQUIRED_FLAG | — | ✅ |
| 14 | TmAtrbFldSetCmpsPEO12TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 15 | TmAtrbFldSetCmpsPEO12UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 16 | TmAtrbFldSetCmpsPEO13CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 17 | TmAtrbFldSetCmpsPEO13DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 18 | TmAtrbFldSetCmpsPEO13ReqFlag | REQUIRED_FLAG | — | ✅ |
| 19 | TmAtrbFldSetCmpsPEO13TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 20 | TmAtrbFldSetCmpsPEO13UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 21 | TmAtrbFldSetCmpsPEO14CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 22 | TmAtrbFldSetCmpsPEO14DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 23 | TmAtrbFldSetCmpsPEO14ReqFlag | REQUIRED_FLAG | — | ✅ |
| 24 | TmAtrbFldSetCmpsPEO14TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 25 | TmAtrbFldSetCmpsPEO14UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 26 | TmAtrbFldSetCmpsPEO15CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 27 | TmAtrbFldSetCmpsPEO15DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 28 | TmAtrbFldSetCmpsPEO15ReqFlag | REQUIRED_FLAG | — | ✅ |
| 29 | TmAtrbFldSetCmpsPEO15TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 30 | TmAtrbFldSetCmpsPEO15UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 31 | TmAtrbFldSetCmpsPEO16CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 32 | TmAtrbFldSetCmpsPEO16DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 33 | TmAtrbFldSetCmpsPEO16ReqFlag | REQUIRED_FLAG | — | ✅ |
| 34 | TmAtrbFldSetCmpsPEO16TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 35 | TmAtrbFldSetCmpsPEO16UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 36 | TmAtrbFldSetCmpsPEO17CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 37 | TmAtrbFldSetCmpsPEO17DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 38 | TmAtrbFldSetCmpsPEO17ReqFlag | REQUIRED_FLAG | — | ✅ |
| 39 | TmAtrbFldSetCmpsPEO17TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 40 | TmAtrbFldSetCmpsPEO17UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 41 | TmAtrbFldSetCmpsPEO18CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 42 | TmAtrbFldSetCmpsPEO18DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 43 | TmAtrbFldSetCmpsPEO18ReqFlag | REQUIRED_FLAG | — | ✅ |
| 44 | TmAtrbFldSetCmpsPEO18TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 45 | TmAtrbFldSetCmpsPEO18UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 46 | TmAtrbFldSetCmpsPEO19CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 47 | TmAtrbFldSetCmpsPEO19DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 48 | TmAtrbFldSetCmpsPEO19ReqFlag | REQUIRED_FLAG | — | ✅ |
| 49 | TmAtrbFldSetCmpsPEO19TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 50 | TmAtrbFldSetCmpsPEO19UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 51 | TmAtrbFldSetCmpsPEO1CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 52 | TmAtrbFldSetCmpsPEO1DSUsgId | DATA_SOURCE_USAGE_ID | — | — |
| 53 | TmAtrbFldSetCmpsPEO1ReqFlag | REQUIRED_FLAG | — | ✅ |
| 54 | TmAtrbFldSetCmpsPEO1TAFldId | TM_ATRB_FLD_ID | — | — |
| 55 | TmAtrbFldSetCmpsPEO1UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | — |
| 56 | TmAtrbFldSetCmpsPEO20CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 57 | TmAtrbFldSetCmpsPEO20DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 58 | TmAtrbFldSetCmpsPEO20ReqFlag | REQUIRED_FLAG | — | ✅ |
| 59 | TmAtrbFldSetCmpsPEO20TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 60 | TmAtrbFldSetCmpsPEO20UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 61 | TmAtrbFldSetCmpsPEO21CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 62 | TmAtrbFldSetCmpsPEO21DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 63 | TmAtrbFldSetCmpsPEO21ReqFlag | REQUIRED_FLAG | — | ✅ |
| 64 | TmAtrbFldSetCmpsPEO21TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 65 | TmAtrbFldSetCmpsPEO21UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 66 | TmAtrbFldSetCmpsPEO22CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 67 | TmAtrbFldSetCmpsPEO22DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 68 | TmAtrbFldSetCmpsPEO22ReqFlag | REQUIRED_FLAG | — | ✅ |
| 69 | TmAtrbFldSetCmpsPEO22TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 70 | TmAtrbFldSetCmpsPEO22UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 71 | TmAtrbFldSetCmpsPEO23CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 72 | TmAtrbFldSetCmpsPEO23DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 73 | TmAtrbFldSetCmpsPEO23ReqFlag | REQUIRED_FLAG | — | ✅ |
| 74 | TmAtrbFldSetCmpsPEO23TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 75 | TmAtrbFldSetCmpsPEO23UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 76 | TmAtrbFldSetCmpsPEO24CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 77 | TmAtrbFldSetCmpsPEO24DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 78 | TmAtrbFldSetCmpsPEO24ReqFlag | REQUIRED_FLAG | — | ✅ |
| 79 | TmAtrbFldSetCmpsPEO24TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 80 | TmAtrbFldSetCmpsPEO24UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 81 | TmAtrbFldSetCmpsPEO25CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 82 | TmAtrbFldSetCmpsPEO25DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 83 | TmAtrbFldSetCmpsPEO25ReqFlag | REQUIRED_FLAG | — | ✅ |
| 84 | TmAtrbFldSetCmpsPEO25TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 85 | TmAtrbFldSetCmpsPEO25UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 86 | TmAtrbFldSetCmpsPEO26CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 87 | TmAtrbFldSetCmpsPEO26DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 88 | TmAtrbFldSetCmpsPEO26ReqFlag | REQUIRED_FLAG | — | ✅ |
| 89 | TmAtrbFldSetCmpsPEO26TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 90 | TmAtrbFldSetCmpsPEO26UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 91 | TmAtrbFldSetCmpsPEO27CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 92 | TmAtrbFldSetCmpsPEO27DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 93 | TmAtrbFldSetCmpsPEO27ReqFlag | REQUIRED_FLAG | — | ✅ |
| 94 | TmAtrbFldSetCmpsPEO27TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 95 | TmAtrbFldSetCmpsPEO27UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 96 | TmAtrbFldSetCmpsPEO28CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 97 | TmAtrbFldSetCmpsPEO28DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 98 | TmAtrbFldSetCmpsPEO28ReqFlag | REQUIRED_FLAG | — | ✅ |
| 99 | TmAtrbFldSetCmpsPEO28TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 100 | TmAtrbFldSetCmpsPEO28UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 101 | TmAtrbFldSetCmpsPEO29CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 102 | TmAtrbFldSetCmpsPEO29DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 103 | TmAtrbFldSetCmpsPEO29ReqFlag | REQUIRED_FLAG | — | ✅ |
| 104 | TmAtrbFldSetCmpsPEO29TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 105 | TmAtrbFldSetCmpsPEO29UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 106 | TmAtrbFldSetCmpsPEO2CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 107 | TmAtrbFldSetCmpsPEO2DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 108 | TmAtrbFldSetCmpsPEO2ReqFlag | REQUIRED_FLAG | — | ✅ |
| 109 | TmAtrbFldSetCmpsPEO2TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 110 | TmAtrbFldSetCmpsPEO2UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 111 | TmAtrbFldSetCmpsPEO30CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 112 | TmAtrbFldSetCmpsPEO30DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 113 | TmAtrbFldSetCmpsPEO30ReqFlag | REQUIRED_FLAG | — | ✅ |
| 114 | TmAtrbFldSetCmpsPEO30TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 115 | TmAtrbFldSetCmpsPEO30UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 116 | TmAtrbFldSetCmpsPEO3CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 117 | TmAtrbFldSetCmpsPEO3DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 118 | TmAtrbFldSetCmpsPEO3ReqFlag | REQUIRED_FLAG | — | ✅ |
| 119 | TmAtrbFldSetCmpsPEO3TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 120 | TmAtrbFldSetCmpsPEO3UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 121 | TmAtrbFldSetCmpsPEO4CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 122 | TmAtrbFldSetCmpsPEO4DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 123 | TmAtrbFldSetCmpsPEO4ReqFlag | REQUIRED_FLAG | — | ✅ |
| 124 | TmAtrbFldSetCmpsPEO4TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 125 | TmAtrbFldSetCmpsPEO4UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 126 | TmAtrbFldSetCmpsPEO5CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 127 | TmAtrbFldSetCmpsPEO5DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 128 | TmAtrbFldSetCmpsPEO5ReqFlag | REQUIRED_FLAG | — | ✅ |
| 129 | TmAtrbFldSetCmpsPEO5TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 130 | TmAtrbFldSetCmpsPEO5UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 131 | TmAtrbFldSetCmpsPEO6CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 132 | TmAtrbFldSetCmpsPEO6DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 133 | TmAtrbFldSetCmpsPEO6ReqFlag | REQUIRED_FLAG | — | ✅ |
| 134 | TmAtrbFldSetCmpsPEO6TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 135 | TmAtrbFldSetCmpsPEO6UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 136 | TmAtrbFldSetCmpsPEO7CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 137 | TmAtrbFldSetCmpsPEO7DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 138 | TmAtrbFldSetCmpsPEO7ReqFlag | REQUIRED_FLAG | — | ✅ |
| 139 | TmAtrbFldSetCmpsPEO7TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 140 | TmAtrbFldSetCmpsPEO7UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 141 | TmAtrbFldSetCmpsPEO8CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 142 | TmAtrbFldSetCmpsPEO8DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 143 | TmAtrbFldSetCmpsPEO8ReqFlag | REQUIRED_FLAG | — | ✅ |
| 144 | TmAtrbFldSetCmpsPEO8TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 145 | TmAtrbFldSetCmpsPEO8UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |
| 146 | TmAtrbFldSetCmpsPEO9CmpId | TM_ATRB_FLD_SET_CMP_ID | — | — |
| 147 | TmAtrbFldSetCmpsPEO9DSUsgId | DATA_SOURCE_USAGE_ID | — | ✅ |
| 148 | TmAtrbFldSetCmpsPEO9ReqFlag | REQUIRED_FLAG | — | ✅ |
| 149 | TmAtrbFldSetCmpsPEO9TAFldId | TM_ATRB_FLD_ID | — | ✅ |
| 150 | TmAtrbFldSetCmpsPEO9UDSUsgId | USER_DATA_SOURCE_USAGE_ID | — | ✅ |

### [[hxt_tclayfld_defns_b|HXT_TCLAYFLD_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclayfldBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TclayfldBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TclayfldBPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | TclayfldBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | TclayfldBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TclayfldBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TclayfldBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TclayfldBPEOModuleId | MODULE_ID | — | — |
| 9 | TclayfldBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TclayfldBPEOPTclayfldDefnsId | P_TCLAYFLD_DEFNS_ID | — | ✅ |
| 11 | TclayfldBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | TclayfldBPEOSguid | SGUID | — | — |
| 13 | TclayfldBPEOTclayId | TCLAY_ID | — | ✅ |
| 14 | TclayfldBPEOTclayfldAttributeCategory | TCLAYFLD_ATTRIBUTE_CATEGORY | — | — |
| 15 | TclayfldBPEOTclayfldAttributeChar1 | TCLAYFLD_ATTRIBUTE_CHAR1 | — | ✅ |
| 16 | TclayfldBPEOTclayfldAttributeChar10 | TCLAYFLD_ATTRIBUTE_CHAR10 | — | ✅ |
| 17 | TclayfldBPEOTclayfldAttributeChar11 | TCLAYFLD_ATTRIBUTE_CHAR11 | — | ✅ |
| 18 | TclayfldBPEOTclayfldAttributeChar12 | TCLAYFLD_ATTRIBUTE_CHAR12 | — | ✅ |
| 19 | TclayfldBPEOTclayfldAttributeChar13 | TCLAYFLD_ATTRIBUTE_CHAR13 | — | ✅ |
| 20 | TclayfldBPEOTclayfldAttributeChar14 | TCLAYFLD_ATTRIBUTE_CHAR14 | — | ✅ |
| 21 | TclayfldBPEOTclayfldAttributeChar15 | TCLAYFLD_ATTRIBUTE_CHAR15 | — | ✅ |
| 22 | TclayfldBPEOTclayfldAttributeChar16 | TCLAYFLD_ATTRIBUTE_CHAR16 | — | ✅ |
| 23 | TclayfldBPEOTclayfldAttributeChar17 | TCLAYFLD_ATTRIBUTE_CHAR17 | — | ✅ |
| 24 | TclayfldBPEOTclayfldAttributeChar18 | TCLAYFLD_ATTRIBUTE_CHAR18 | — | ✅ |
| 25 | TclayfldBPEOTclayfldAttributeChar19 | TCLAYFLD_ATTRIBUTE_CHAR19 | — | ✅ |
| 26 | TclayfldBPEOTclayfldAttributeChar2 | TCLAYFLD_ATTRIBUTE_CHAR2 | — | ✅ |
| 27 | TclayfldBPEOTclayfldAttributeChar20 | TCLAYFLD_ATTRIBUTE_CHAR20 | — | ✅ |
| 28 | TclayfldBPEOTclayfldAttributeChar21 | TCLAYFLD_ATTRIBUTE_CHAR21 | — | ✅ |
| 29 | TclayfldBPEOTclayfldAttributeChar22 | TCLAYFLD_ATTRIBUTE_CHAR22 | — | ✅ |
| 30 | TclayfldBPEOTclayfldAttributeChar23 | TCLAYFLD_ATTRIBUTE_CHAR23 | — | ✅ |
| 31 | TclayfldBPEOTclayfldAttributeChar24 | TCLAYFLD_ATTRIBUTE_CHAR24 | — | ✅ |
| 32 | TclayfldBPEOTclayfldAttributeChar25 | TCLAYFLD_ATTRIBUTE_CHAR25 | — | ✅ |
| 33 | TclayfldBPEOTclayfldAttributeChar26 | TCLAYFLD_ATTRIBUTE_CHAR26 | — | — |
| 34 | TclayfldBPEOTclayfldAttributeChar27 | TCLAYFLD_ATTRIBUTE_CHAR27 | — | — |
| 35 | TclayfldBPEOTclayfldAttributeChar28 | TCLAYFLD_ATTRIBUTE_CHAR28 | — | — |
| 36 | TclayfldBPEOTclayfldAttributeChar29 | TCLAYFLD_ATTRIBUTE_CHAR29 | — | — |
| 37 | TclayfldBPEOTclayfldAttributeChar3 | TCLAYFLD_ATTRIBUTE_CHAR3 | — | ✅ |
| 38 | TclayfldBPEOTclayfldAttributeChar30 | TCLAYFLD_ATTRIBUTE_CHAR30 | — | — |
| 39 | TclayfldBPEOTclayfldAttributeChar4 | TCLAYFLD_ATTRIBUTE_CHAR4 | — | ✅ |
| 40 | TclayfldBPEOTclayfldAttributeChar5 | TCLAYFLD_ATTRIBUTE_CHAR5 | — | — |
| 41 | TclayfldBPEOTclayfldAttributeChar6 | TCLAYFLD_ATTRIBUTE_CHAR6 | — | — |
| 42 | TclayfldBPEOTclayfldAttributeChar7 | TCLAYFLD_ATTRIBUTE_CHAR7 | — | — |
| 43 | TclayfldBPEOTclayfldAttributeChar8 | TCLAYFLD_ATTRIBUTE_CHAR8 | — | — |
| 44 | TclayfldBPEOTclayfldAttributeChar9 | TCLAYFLD_ATTRIBUTE_CHAR9 | — | — |
| 45 | TclayfldBPEOTclayfldAttributeDate1 | TCLAYFLD_ATTRIBUTE_DATE1 | — | ✅ |
| 46 | TclayfldBPEOTclayfldAttributeDate10 | TCLAYFLD_ATTRIBUTE_DATE10 | — | — |
| 47 | TclayfldBPEOTclayfldAttributeDate11 | TCLAYFLD_ATTRIBUTE_DATE11 | — | — |
| 48 | TclayfldBPEOTclayfldAttributeDate12 | TCLAYFLD_ATTRIBUTE_DATE12 | — | — |
| 49 | TclayfldBPEOTclayfldAttributeDate13 | TCLAYFLD_ATTRIBUTE_DATE13 | — | — |
| 50 | TclayfldBPEOTclayfldAttributeDate14 | TCLAYFLD_ATTRIBUTE_DATE14 | — | — |
| 51 | TclayfldBPEOTclayfldAttributeDate15 | TCLAYFLD_ATTRIBUTE_DATE15 | — | — |
| 52 | TclayfldBPEOTclayfldAttributeDate2 | TCLAYFLD_ATTRIBUTE_DATE2 | — | — |
| 53 | TclayfldBPEOTclayfldAttributeDate3 | TCLAYFLD_ATTRIBUTE_DATE3 | — | — |
| 54 | TclayfldBPEOTclayfldAttributeDate4 | TCLAYFLD_ATTRIBUTE_DATE4 | — | — |
| 55 | TclayfldBPEOTclayfldAttributeDate5 | TCLAYFLD_ATTRIBUTE_DATE5 | — | — |
| 56 | TclayfldBPEOTclayfldAttributeDate6 | TCLAYFLD_ATTRIBUTE_DATE6 | — | — |
| 57 | TclayfldBPEOTclayfldAttributeDate7 | TCLAYFLD_ATTRIBUTE_DATE7 | — | — |
| 58 | TclayfldBPEOTclayfldAttributeDate8 | TCLAYFLD_ATTRIBUTE_DATE8 | — | — |
| 59 | TclayfldBPEOTclayfldAttributeDate9 | TCLAYFLD_ATTRIBUTE_DATE9 | — | — |
| 60 | TclayfldBPEOTclayfldAttributeNumber1 | TCLAYFLD_ATTRIBUTE_NUMBER1 | — | ✅ |
| 61 | TclayfldBPEOTclayfldAttributeNumber10 | TCLAYFLD_ATTRIBUTE_NUMBER10 | — | ✅ |
| 62 | TclayfldBPEOTclayfldAttributeNumber11 | TCLAYFLD_ATTRIBUTE_NUMBER11 | — | ✅ |
| 63 | TclayfldBPEOTclayfldAttributeNumber12 | TCLAYFLD_ATTRIBUTE_NUMBER12 | — | ✅ |
| 64 | TclayfldBPEOTclayfldAttributeNumber13 | TCLAYFLD_ATTRIBUTE_NUMBER13 | — | ✅ |
| 65 | TclayfldBPEOTclayfldAttributeNumber14 | TCLAYFLD_ATTRIBUTE_NUMBER14 | — | ✅ |
| 66 | TclayfldBPEOTclayfldAttributeNumber15 | TCLAYFLD_ATTRIBUTE_NUMBER15 | — | — |
| 67 | TclayfldBPEOTclayfldAttributeNumber16 | TCLAYFLD_ATTRIBUTE_NUMBER16 | — | ✅ |
| 68 | TclayfldBPEOTclayfldAttributeNumber17 | TCLAYFLD_ATTRIBUTE_NUMBER17 | — | ✅ |
| 69 | TclayfldBPEOTclayfldAttributeNumber18 | TCLAYFLD_ATTRIBUTE_NUMBER18 | — | ✅ |
| 70 | TclayfldBPEOTclayfldAttributeNumber19 | TCLAYFLD_ATTRIBUTE_NUMBER19 | — | — |
| 71 | TclayfldBPEOTclayfldAttributeNumber2 | TCLAYFLD_ATTRIBUTE_NUMBER2 | — | ✅ |
| 72 | TclayfldBPEOTclayfldAttributeNumber20 | TCLAYFLD_ATTRIBUTE_NUMBER20 | — | ✅ |
| 73 | TclayfldBPEOTclayfldAttributeNumber3 | TCLAYFLD_ATTRIBUTE_NUMBER3 | — | ✅ |
| 74 | TclayfldBPEOTclayfldAttributeNumber4 | TCLAYFLD_ATTRIBUTE_NUMBER4 | — | ✅ |
| 75 | TclayfldBPEOTclayfldAttributeNumber5 | TCLAYFLD_ATTRIBUTE_NUMBER5 | — | ✅ |
| 76 | TclayfldBPEOTclayfldAttributeNumber6 | TCLAYFLD_ATTRIBUTE_NUMBER6 | — | ✅ |
| 77 | TclayfldBPEOTclayfldAttributeNumber7 | TCLAYFLD_ATTRIBUTE_NUMBER7 | — | ✅ |
| 78 | TclayfldBPEOTclayfldAttributeNumber8 | TCLAYFLD_ATTRIBUTE_NUMBER8 | — | ✅ |
| 79 | TclayfldBPEOTclayfldAttributeNumber9 | TCLAYFLD_ATTRIBUTE_NUMBER9 | — | ✅ |
| 80 | TclayfldBPEOTclayfldDefnsCd | TCLAYFLD_DEFNS_CD | — | ✅ |
| 81 | TclayfldBPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | 🔑 | ✅ |
| 82 | TclayfldBPEOTclayfldDefnsInstanceFlag | TCLAYFLD_DEFNS_INSTANCE_FLAG | — | ✅ |
| 83 | TclayfldBPEOTclayfldTmplId | TCLAYFLD_TMPL_ID | — | — |

### [[hxt_tclayfld_defns_tl|HXT_TCLAYFLD_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclayfldTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TclayfldTLPEOLabel | LABEL | — | ✅ |
| 3 | TclayfldTLPEOLanguage | LANGUAGE | — | — |
| 4 | TclayfldTLPEOName | NAME | — | ✅ |
| 5 | TclayfldTLPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | — | — |

### [[hxt_tclayfld_defns_vl|HXT_TCLAYFLD_DEFNS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ParentTclayfldVLPEOLabel | LABEL | — | ✅ |
| 2 | ParentTclayfldVLPEOName | NAME | — | ✅ |
| 3 | ParentTclayfldVLPEOTclayfldDefnsCd | TCLAYFLD_DEFNS_CD | — | ✅ |
| 4 | ParentTclayfldVLPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
