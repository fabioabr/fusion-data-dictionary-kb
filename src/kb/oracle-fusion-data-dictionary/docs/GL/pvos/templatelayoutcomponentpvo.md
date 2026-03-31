---
id: DOC-GL-PVO-TemplateLayoutComponentPVO
doc_type: system-doc
title: "TemplateLayoutComponentPVO — PVO General Ledger"
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
  - TemplateLayoutComponentPVO
  - templatelayoutcomponentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateLayoutComponentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Layout Component. Acessa as tabelas: HWM_TE_ALT_NAMES, HWM_TE_ALT_NAME_VALS_VL, HWM_TM_ATRB_FLDS_VL (+5).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TemplateLayoutComponentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 286 | 8 | 1 | 203 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_te_alt_names|HWM_TE_ALT_NAMES]] — 3 atributos (3 BICC)
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
| 3 | TeAltNamesPEOTeAltNameId | TE_ALT_NAME_ID | — | ✅ |

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
| 9 | TclayfldBPEOObjVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TclayfldBPEOPTclayfldDefnsId | P_TCLAYFLD_DEFNS_ID | — | ✅ |
| 11 | TclayfldBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | TclayfldBPEOSguid | SGUID | — | — |
| 13 | TclayfldBPEOTclayId | TCLAY_ID | — | ✅ |
| 14 | TclayfldBPEOTclayfldAtrbCat | TCLAYFLD_ATTRIBUTE_CATEGORY | — | — |
| 15 | TclayfldBPEOTclayfldAtrbChar1 | TCLAYFLD_ATTRIBUTE_CHAR1 | — | ✅ |
| 16 | TclayfldBPEOTclayfldAtrbChar10 | TCLAYFLD_ATTRIBUTE_CHAR10 | — | ✅ |
| 17 | TclayfldBPEOTclayfldAtrbChar11 | TCLAYFLD_ATTRIBUTE_CHAR11 | — | ✅ |
| 18 | TclayfldBPEOTclayfldAtrbChar12 | TCLAYFLD_ATTRIBUTE_CHAR12 | — | ✅ |
| 19 | TclayfldBPEOTclayfldAtrbChar13 | TCLAYFLD_ATTRIBUTE_CHAR13 | — | ✅ |
| 20 | TclayfldBPEOTclayfldAtrbChar14 | TCLAYFLD_ATTRIBUTE_CHAR14 | — | ✅ |
| 21 | TclayfldBPEOTclayfldAtrbChar15 | TCLAYFLD_ATTRIBUTE_CHAR15 | — | ✅ |
| 22 | TclayfldBPEOTclayfldAtrbChar16 | TCLAYFLD_ATTRIBUTE_CHAR16 | — | ✅ |
| 23 | TclayfldBPEOTclayfldAtrbChar17 | TCLAYFLD_ATTRIBUTE_CHAR17 | — | ✅ |
| 24 | TclayfldBPEOTclayfldAtrbChar18 | TCLAYFLD_ATTRIBUTE_CHAR18 | — | ✅ |
| 25 | TclayfldBPEOTclayfldAtrbChar19 | TCLAYFLD_ATTRIBUTE_CHAR19 | — | ✅ |
| 26 | TclayfldBPEOTclayfldAtrbChar2 | TCLAYFLD_ATTRIBUTE_CHAR2 | — | ✅ |
| 27 | TclayfldBPEOTclayfldAtrbChar20 | TCLAYFLD_ATTRIBUTE_CHAR20 | — | ✅ |
| 28 | TclayfldBPEOTclayfldAtrbChar21 | TCLAYFLD_ATTRIBUTE_CHAR21 | — | ✅ |
| 29 | TclayfldBPEOTclayfldAtrbChar22 | TCLAYFLD_ATTRIBUTE_CHAR22 | — | ✅ |
| 30 | TclayfldBPEOTclayfldAtrbChar23 | TCLAYFLD_ATTRIBUTE_CHAR23 | — | ✅ |
| 31 | TclayfldBPEOTclayfldAtrbChar24 | TCLAYFLD_ATTRIBUTE_CHAR24 | — | ✅ |
| 32 | TclayfldBPEOTclayfldAtrbChar25 | TCLAYFLD_ATTRIBUTE_CHAR25 | — | ✅ |
| 33 | TclayfldBPEOTclayfldAtrbChar26 | TCLAYFLD_ATTRIBUTE_CHAR26 | — | — |
| 34 | TclayfldBPEOTclayfldAtrbChar27 | TCLAYFLD_ATTRIBUTE_CHAR27 | — | — |
| 35 | TclayfldBPEOTclayfldAtrbChar28 | TCLAYFLD_ATTRIBUTE_CHAR28 | — | — |
| 36 | TclayfldBPEOTclayfldAtrbChar29 | TCLAYFLD_ATTRIBUTE_CHAR29 | — | — |
| 37 | TclayfldBPEOTclayfldAtrbChar3 | TCLAYFLD_ATTRIBUTE_CHAR3 | — | ✅ |
| 38 | TclayfldBPEOTclayfldAtrbChar30 | TCLAYFLD_ATTRIBUTE_CHAR30 | — | — |
| 39 | TclayfldBPEOTclayfldAtrbChar4 | TCLAYFLD_ATTRIBUTE_CHAR4 | — | ✅ |
| 40 | TclayfldBPEOTclayfldAtrbChar5 | TCLAYFLD_ATTRIBUTE_CHAR5 | — | — |
| 41 | TclayfldBPEOTclayfldAtrbChar6 | TCLAYFLD_ATTRIBUTE_CHAR6 | — | — |
| 42 | TclayfldBPEOTclayfldAtrbChar7 | TCLAYFLD_ATTRIBUTE_CHAR7 | — | — |
| 43 | TclayfldBPEOTclayfldAtrbChar8 | TCLAYFLD_ATTRIBUTE_CHAR8 | — | — |
| 44 | TclayfldBPEOTclayfldAtrbChar9 | TCLAYFLD_ATTRIBUTE_CHAR9 | — | — |
| 45 | TclayfldBPEOTclayfldAtrbDate1 | TCLAYFLD_ATTRIBUTE_DATE1 | — | ✅ |
| 46 | TclayfldBPEOTclayfldAtrbDate10 | TCLAYFLD_ATTRIBUTE_DATE10 | — | — |
| 47 | TclayfldBPEOTclayfldAtrbDate11 | TCLAYFLD_ATTRIBUTE_DATE11 | — | — |
| 48 | TclayfldBPEOTclayfldAtrbDate12 | TCLAYFLD_ATTRIBUTE_DATE12 | — | — |
| 49 | TclayfldBPEOTclayfldAtrbDate13 | TCLAYFLD_ATTRIBUTE_DATE13 | — | — |
| 50 | TclayfldBPEOTclayfldAtrbDate14 | TCLAYFLD_ATTRIBUTE_DATE14 | — | — |
| 51 | TclayfldBPEOTclayfldAtrbDate15 | TCLAYFLD_ATTRIBUTE_DATE15 | — | — |
| 52 | TclayfldBPEOTclayfldAtrbDate2 | TCLAYFLD_ATTRIBUTE_DATE2 | — | — |
| 53 | TclayfldBPEOTclayfldAtrbDate3 | TCLAYFLD_ATTRIBUTE_DATE3 | — | — |
| 54 | TclayfldBPEOTclayfldAtrbDate4 | TCLAYFLD_ATTRIBUTE_DATE4 | — | — |
| 55 | TclayfldBPEOTclayfldAtrbDate5 | TCLAYFLD_ATTRIBUTE_DATE5 | — | — |
| 56 | TclayfldBPEOTclayfldAtrbDate6 | TCLAYFLD_ATTRIBUTE_DATE6 | — | — |
| 57 | TclayfldBPEOTclayfldAtrbDate7 | TCLAYFLD_ATTRIBUTE_DATE7 | — | — |
| 58 | TclayfldBPEOTclayfldAtrbDate8 | TCLAYFLD_ATTRIBUTE_DATE8 | — | — |
| 59 | TclayfldBPEOTclayfldAtrbDate9 | TCLAYFLD_ATTRIBUTE_DATE9 | — | — |
| 60 | TclayfldBPEOTclayfldAtrbNum1 | TCLAYFLD_ATTRIBUTE_NUMBER1 | — | ✅ |
| 61 | TclayfldBPEOTclayfldAtrbNum10 | TCLAYFLD_ATTRIBUTE_NUMBER10 | — | ✅ |
| 62 | TclayfldBPEOTclayfldAtrbNum11 | TCLAYFLD_ATTRIBUTE_NUMBER11 | — | ✅ |
| 63 | TclayfldBPEOTclayfldAtrbNum12 | TCLAYFLD_ATTRIBUTE_NUMBER12 | — | ✅ |
| 64 | TclayfldBPEOTclayfldAtrbNum13 | TCLAYFLD_ATTRIBUTE_NUMBER13 | — | ✅ |
| 65 | TclayfldBPEOTclayfldAtrbNum14 | TCLAYFLD_ATTRIBUTE_NUMBER14 | — | ✅ |
| 66 | TclayfldBPEOTclayfldAtrbNum15 | TCLAYFLD_ATTRIBUTE_NUMBER15 | — | — |
| 67 | TclayfldBPEOTclayfldAtrbNum16 | TCLAYFLD_ATTRIBUTE_NUMBER16 | — | ✅ |
| 68 | TclayfldBPEOTclayfldAtrbNum17 | TCLAYFLD_ATTRIBUTE_NUMBER17 | — | ✅ |
| 69 | TclayfldBPEOTclayfldAtrbNum18 | TCLAYFLD_ATTRIBUTE_NUMBER18 | — | ✅ |
| 70 | TclayfldBPEOTclayfldAtrbNum19 | TCLAYFLD_ATTRIBUTE_NUMBER19 | — | — |
| 71 | TclayfldBPEOTclayfldAtrbNum2 | TCLAYFLD_ATTRIBUTE_NUMBER2 | — | ✅ |
| 72 | TclayfldBPEOTclayfldAtrbNum20 | TCLAYFLD_ATTRIBUTE_NUMBER20 | — | ✅ |
| 73 | TclayfldBPEOTclayfldAtrbNum3 | TCLAYFLD_ATTRIBUTE_NUMBER3 | — | ✅ |
| 74 | TclayfldBPEOTclayfldAtrbNum4 | TCLAYFLD_ATTRIBUTE_NUMBER4 | — | ✅ |
| 75 | TclayfldBPEOTclayfldAtrbNum5 | TCLAYFLD_ATTRIBUTE_NUMBER5 | — | ✅ |
| 76 | TclayfldBPEOTclayfldAtrbNum6 | TCLAYFLD_ATTRIBUTE_NUMBER6 | — | ✅ |
| 77 | TclayfldBPEOTclayfldAtrbNum7 | TCLAYFLD_ATTRIBUTE_NUMBER7 | — | ✅ |
| 78 | TclayfldBPEOTclayfldAtrbNum8 | TCLAYFLD_ATTRIBUTE_NUMBER8 | — | ✅ |
| 79 | TclayfldBPEOTclayfldAtrbNum9 | TCLAYFLD_ATTRIBUTE_NUMBER9 | — | ✅ |
| 80 | TclayfldBPEOTclayfldDefInsFlag | TCLAYFLD_DEFNS_INSTANCE_FLAG | — | ✅ |
| 81 | TclayfldBPEOTclayfldDefnsCd | TCLAYFLD_DEFNS_CD | — | ✅ |
| 82 | TclayfldBPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | 🔑 | ✅ |
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
| 1 | ParentTclayfldVLPEODefnsCd | TCLAYFLD_DEFNS_CD | — | ✅ |
| 2 | ParentTclayfldVLPEODefnsId | TCLAYFLD_DEFNS_ID | — | — |
| 3 | ParentTclayfldVLPEOLabel | LABEL | — | ✅ |
| 4 | ParentTclayfldVLPEOName | NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
