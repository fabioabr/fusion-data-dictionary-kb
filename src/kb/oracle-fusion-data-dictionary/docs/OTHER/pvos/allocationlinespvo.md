---
id: DOC-OTHER-PVO-AllocationLinesPVO
doc_type: system-doc
title: "AllocationLinesPVO — PVO Cross-Module"
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
  - AllocationLinesPVO
  - allocationlinespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllocationLinesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Allocation Lines. Acessa as tabelas: HWM_ALLOCATIONS_HDR_F, HWM_ALLOCATIONS_HDR_TL, HWM_ALLOCATION_LINES_F (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeAllocationsAM.AllocationLinesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 291 | 6 | 3 | 211 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_allocations_hdr_f|HWM_ALLOCATIONS_HDR_F]] — 13 atributos (7 BICC)
- [[hwm_allocations_hdr_tl|HWM_ALLOCATIONS_HDR_TL]] — 3 atributos (1 BICC)
- [[hwm_allocation_lines_f|HWM_ALLOCATION_LINES_F]] — 15 atributos (3 PKs, 11 BICC)
- [[hwm_allocation_ln_atrbs_f|HWM_ALLOCATION_LN_ATRBS_F]] — 240 atributos (180 BICC)
- [[hwm_allocation_rules_f|HWM_ALLOCATION_RULES_F]] — 17 atributos (10 BICC)
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

### [[hwm_allocation_lines_f|HWM_ALLOCATION_LINES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocLinesPEOAllocationLineId | ALLOCATION_LINE_ID | 🔑 | ✅ |
| 2 | AllocLinesPEOAllocationLinePriority | ALLOCATION_LINE_PRIORITY | — | ✅ |
| 3 | AllocLinesPEOAllocationRuleId | ALLOCATION_RULE_ID | — | ✅ |
| 4 | AllocLinesPEOAllocationValue | ALLOCATION_VALUE | — | ✅ |
| 5 | AllocLinesPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | AllocLinesPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | AllocLinesPEODataLevel | DATA_LEVEL | — | — |
| 8 | AllocLinesPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 9 | AllocLinesPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | AllocLinesPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | AllocLinesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | AllocLinesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | AllocLinesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | AllocLinesPEOModuleId | MODULE_ID | — | — |
| 15 | AllocLinesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[hwm_allocation_ln_atrbs_f|HWM_ALLOCATION_LN_ATRBS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocLnAtrbsPEO10AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 2 | AllocLnAtrbsPEO10AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 3 | AllocLnAtrbsPEO10AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 4 | AllocLnAtrbsPEO10AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 5 | AllocLnAtrbsPEO10AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 6 | AllocLnAtrbsPEO10EffEndDt | EFFECTIVE_END_DATE | — | — |
| 7 | AllocLnAtrbsPEO10EffStartDt | EFFECTIVE_START_DATE | — | — |
| 8 | AllocLnAtrbsPEO10TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 9 | AllocLnAtrbsPEO11AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 10 | AllocLnAtrbsPEO11AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 11 | AllocLnAtrbsPEO11AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 12 | AllocLnAtrbsPEO11AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 13 | AllocLnAtrbsPEO11AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 14 | AllocLnAtrbsPEO11EffEndDt | EFFECTIVE_END_DATE | — | — |
| 15 | AllocLnAtrbsPEO11EffStartDt | EFFECTIVE_START_DATE | — | — |
| 16 | AllocLnAtrbsPEO11TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 17 | AllocLnAtrbsPEO12AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 18 | AllocLnAtrbsPEO12AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 19 | AllocLnAtrbsPEO12AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 20 | AllocLnAtrbsPEO12AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 21 | AllocLnAtrbsPEO12AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 22 | AllocLnAtrbsPEO12EffEndDt | EFFECTIVE_END_DATE | — | — |
| 23 | AllocLnAtrbsPEO12EffStartDt | EFFECTIVE_START_DATE | — | — |
| 24 | AllocLnAtrbsPEO12TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 25 | AllocLnAtrbsPEO13AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 26 | AllocLnAtrbsPEO13AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 27 | AllocLnAtrbsPEO13AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 28 | AllocLnAtrbsPEO13AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 29 | AllocLnAtrbsPEO13AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 30 | AllocLnAtrbsPEO13EffEndDt | EFFECTIVE_END_DATE | — | — |
| 31 | AllocLnAtrbsPEO13EffStartDt | EFFECTIVE_START_DATE | — | — |
| 32 | AllocLnAtrbsPEO13TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 33 | AllocLnAtrbsPEO14AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 34 | AllocLnAtrbsPEO14AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 35 | AllocLnAtrbsPEO14AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 36 | AllocLnAtrbsPEO14AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 37 | AllocLnAtrbsPEO14AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 38 | AllocLnAtrbsPEO14EffEndDt | EFFECTIVE_END_DATE | — | — |
| 39 | AllocLnAtrbsPEO14EffStartDt | EFFECTIVE_START_DATE | — | — |
| 40 | AllocLnAtrbsPEO14TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 41 | AllocLnAtrbsPEO15AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 42 | AllocLnAtrbsPEO15AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 43 | AllocLnAtrbsPEO15AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 44 | AllocLnAtrbsPEO15AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 45 | AllocLnAtrbsPEO15AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 46 | AllocLnAtrbsPEO15EffEndDt | EFFECTIVE_END_DATE | — | — |
| 47 | AllocLnAtrbsPEO15EffStartDt | EFFECTIVE_START_DATE | — | — |
| 48 | AllocLnAtrbsPEO15TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 49 | AllocLnAtrbsPEO16AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 50 | AllocLnAtrbsPEO16AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 51 | AllocLnAtrbsPEO16AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 52 | AllocLnAtrbsPEO16AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 53 | AllocLnAtrbsPEO16AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 54 | AllocLnAtrbsPEO16EffEndDt | EFFECTIVE_END_DATE | — | — |
| 55 | AllocLnAtrbsPEO16EffStartDt | EFFECTIVE_START_DATE | — | — |
| 56 | AllocLnAtrbsPEO16TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 57 | AllocLnAtrbsPEO17AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 58 | AllocLnAtrbsPEO17AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 59 | AllocLnAtrbsPEO17AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 60 | AllocLnAtrbsPEO17AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 61 | AllocLnAtrbsPEO17AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 62 | AllocLnAtrbsPEO17EffEndDt | EFFECTIVE_END_DATE | — | — |
| 63 | AllocLnAtrbsPEO17EffStartDt | EFFECTIVE_START_DATE | — | — |
| 64 | AllocLnAtrbsPEO17TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 65 | AllocLnAtrbsPEO18AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 66 | AllocLnAtrbsPEO18AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 67 | AllocLnAtrbsPEO18AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 68 | AllocLnAtrbsPEO18AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 69 | AllocLnAtrbsPEO18AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 70 | AllocLnAtrbsPEO18EffEndDt | EFFECTIVE_END_DATE | — | — |
| 71 | AllocLnAtrbsPEO18EffStartDt | EFFECTIVE_START_DATE | — | — |
| 72 | AllocLnAtrbsPEO18TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 73 | AllocLnAtrbsPEO19AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 74 | AllocLnAtrbsPEO19AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 75 | AllocLnAtrbsPEO19AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 76 | AllocLnAtrbsPEO19AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 77 | AllocLnAtrbsPEO19AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 78 | AllocLnAtrbsPEO19EffEndDt | EFFECTIVE_END_DATE | — | — |
| 79 | AllocLnAtrbsPEO19EffStartDt | EFFECTIVE_START_DATE | — | — |
| 80 | AllocLnAtrbsPEO19TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 81 | AllocLnAtrbsPEO1AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 82 | AllocLnAtrbsPEO1AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 83 | AllocLnAtrbsPEO1AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 84 | AllocLnAtrbsPEO1AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 85 | AllocLnAtrbsPEO1AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 86 | AllocLnAtrbsPEO1EffEndDt | EFFECTIVE_END_DATE | — | — |
| 87 | AllocLnAtrbsPEO1EffStartDt | EFFECTIVE_START_DATE | — | — |
| 88 | AllocLnAtrbsPEO1TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 89 | AllocLnAtrbsPEO20AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 90 | AllocLnAtrbsPEO20AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 91 | AllocLnAtrbsPEO20AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 92 | AllocLnAtrbsPEO20AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 93 | AllocLnAtrbsPEO20AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 94 | AllocLnAtrbsPEO20EffEndDt | EFFECTIVE_END_DATE | — | — |
| 95 | AllocLnAtrbsPEO20EffStartDt | EFFECTIVE_START_DATE | — | — |
| 96 | AllocLnAtrbsPEO20TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 97 | AllocLnAtrbsPEO21AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 98 | AllocLnAtrbsPEO21AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 99 | AllocLnAtrbsPEO21AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 100 | AllocLnAtrbsPEO21AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 101 | AllocLnAtrbsPEO21AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 102 | AllocLnAtrbsPEO21EffEndDt | EFFECTIVE_END_DATE | — | — |
| 103 | AllocLnAtrbsPEO21EffStartDt | EFFECTIVE_START_DATE | — | — |
| 104 | AllocLnAtrbsPEO21TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 105 | AllocLnAtrbsPEO22AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 106 | AllocLnAtrbsPEO22AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 107 | AllocLnAtrbsPEO22AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 108 | AllocLnAtrbsPEO22AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 109 | AllocLnAtrbsPEO22AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 110 | AllocLnAtrbsPEO22EffEndDt | EFFECTIVE_END_DATE | — | — |
| 111 | AllocLnAtrbsPEO22EffStartDt | EFFECTIVE_START_DATE | — | — |
| 112 | AllocLnAtrbsPEO22TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 113 | AllocLnAtrbsPEO23AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 114 | AllocLnAtrbsPEO23AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 115 | AllocLnAtrbsPEO23AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 116 | AllocLnAtrbsPEO23AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 117 | AllocLnAtrbsPEO23AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 118 | AllocLnAtrbsPEO23EffEndDt | EFFECTIVE_END_DATE | — | — |
| 119 | AllocLnAtrbsPEO23EffStartDt | EFFECTIVE_START_DATE | — | — |
| 120 | AllocLnAtrbsPEO23TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 121 | AllocLnAtrbsPEO24AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 122 | AllocLnAtrbsPEO24AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 123 | AllocLnAtrbsPEO24AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 124 | AllocLnAtrbsPEO24AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 125 | AllocLnAtrbsPEO24AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 126 | AllocLnAtrbsPEO24EffEndDt | EFFECTIVE_END_DATE | — | — |
| 127 | AllocLnAtrbsPEO24EffStartDt | EFFECTIVE_START_DATE | — | — |
| 128 | AllocLnAtrbsPEO24TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 129 | AllocLnAtrbsPEO25AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 130 | AllocLnAtrbsPEO25AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 131 | AllocLnAtrbsPEO25AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 132 | AllocLnAtrbsPEO25AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 133 | AllocLnAtrbsPEO25AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 134 | AllocLnAtrbsPEO25EffEndDt | EFFECTIVE_END_DATE | — | — |
| 135 | AllocLnAtrbsPEO25EffStartDt | EFFECTIVE_START_DATE | — | — |
| 136 | AllocLnAtrbsPEO25TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 137 | AllocLnAtrbsPEO26AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 138 | AllocLnAtrbsPEO26AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 139 | AllocLnAtrbsPEO26AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 140 | AllocLnAtrbsPEO26AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 141 | AllocLnAtrbsPEO26AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 142 | AllocLnAtrbsPEO26EffEndDt | EFFECTIVE_END_DATE | — | — |
| 143 | AllocLnAtrbsPEO26EffStartDt | EFFECTIVE_START_DATE | — | — |
| 144 | AllocLnAtrbsPEO26TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 145 | AllocLnAtrbsPEO27AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 146 | AllocLnAtrbsPEO27AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 147 | AllocLnAtrbsPEO27AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 148 | AllocLnAtrbsPEO27AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 149 | AllocLnAtrbsPEO27AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 150 | AllocLnAtrbsPEO27EffEndDt | EFFECTIVE_END_DATE | — | — |
| 151 | AllocLnAtrbsPEO27EffStartDt | EFFECTIVE_START_DATE | — | — |
| 152 | AllocLnAtrbsPEO27TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 153 | AllocLnAtrbsPEO28AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 154 | AllocLnAtrbsPEO28AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 155 | AllocLnAtrbsPEO28AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 156 | AllocLnAtrbsPEO28AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 157 | AllocLnAtrbsPEO28AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 158 | AllocLnAtrbsPEO28EffEndDt | EFFECTIVE_END_DATE | — | — |
| 159 | AllocLnAtrbsPEO28EffStartDt | EFFECTIVE_START_DATE | — | — |
| 160 | AllocLnAtrbsPEO28TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 161 | AllocLnAtrbsPEO29AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 162 | AllocLnAtrbsPEO29AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 163 | AllocLnAtrbsPEO29AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 164 | AllocLnAtrbsPEO29AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 165 | AllocLnAtrbsPEO29AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 166 | AllocLnAtrbsPEO29EffEndDt | EFFECTIVE_END_DATE | — | — |
| 167 | AllocLnAtrbsPEO29EffStartDt | EFFECTIVE_START_DATE | — | — |
| 168 | AllocLnAtrbsPEO29TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 169 | AllocLnAtrbsPEO2AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 170 | AllocLnAtrbsPEO2AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 171 | AllocLnAtrbsPEO2AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 172 | AllocLnAtrbsPEO2AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 173 | AllocLnAtrbsPEO2AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 174 | AllocLnAtrbsPEO2EffEndDt | EFFECTIVE_END_DATE | — | — |
| 175 | AllocLnAtrbsPEO2EffStartDt | EFFECTIVE_START_DATE | — | — |
| 176 | AllocLnAtrbsPEO2TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 177 | AllocLnAtrbsPEO30AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 178 | AllocLnAtrbsPEO30AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 179 | AllocLnAtrbsPEO30AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 180 | AllocLnAtrbsPEO30AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 181 | AllocLnAtrbsPEO30AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 182 | AllocLnAtrbsPEO30EffEndDt | EFFECTIVE_END_DATE | — | — |
| 183 | AllocLnAtrbsPEO30EffStartDt | EFFECTIVE_START_DATE | — | — |
| 184 | AllocLnAtrbsPEO30TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 185 | AllocLnAtrbsPEO3AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 186 | AllocLnAtrbsPEO3AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 187 | AllocLnAtrbsPEO3AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 188 | AllocLnAtrbsPEO3AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 189 | AllocLnAtrbsPEO3AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 190 | AllocLnAtrbsPEO3EffEndDt | EFFECTIVE_END_DATE | — | — |
| 191 | AllocLnAtrbsPEO3EffStartDt | EFFECTIVE_START_DATE | — | — |
| 192 | AllocLnAtrbsPEO3TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 193 | AllocLnAtrbsPEO4AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 194 | AllocLnAtrbsPEO4AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 195 | AllocLnAtrbsPEO4AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 196 | AllocLnAtrbsPEO4AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 197 | AllocLnAtrbsPEO4AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 198 | AllocLnAtrbsPEO4EffEndDt | EFFECTIVE_END_DATE | — | — |
| 199 | AllocLnAtrbsPEO4EffStartDt | EFFECTIVE_START_DATE | — | — |
| 200 | AllocLnAtrbsPEO4TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 201 | AllocLnAtrbsPEO5AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 202 | AllocLnAtrbsPEO5AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 203 | AllocLnAtrbsPEO5AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 204 | AllocLnAtrbsPEO5AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 205 | AllocLnAtrbsPEO5AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 206 | AllocLnAtrbsPEO5EffEndDt | EFFECTIVE_END_DATE | — | — |
| 207 | AllocLnAtrbsPEO5EffStartDt | EFFECTIVE_START_DATE | — | — |
| 208 | AllocLnAtrbsPEO5TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 209 | AllocLnAtrbsPEO6AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 210 | AllocLnAtrbsPEO6AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 211 | AllocLnAtrbsPEO6AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 212 | AllocLnAtrbsPEO6AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 213 | AllocLnAtrbsPEO6AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 214 | AllocLnAtrbsPEO6EffEndDt | EFFECTIVE_END_DATE | — | — |
| 215 | AllocLnAtrbsPEO6EffStartDt | EFFECTIVE_START_DATE | — | — |
| 216 | AllocLnAtrbsPEO6TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 217 | AllocLnAtrbsPEO7AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 218 | AllocLnAtrbsPEO7AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 219 | AllocLnAtrbsPEO7AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 220 | AllocLnAtrbsPEO7AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 221 | AllocLnAtrbsPEO7AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 222 | AllocLnAtrbsPEO7EffEndDt | EFFECTIVE_END_DATE | — | — |
| 223 | AllocLnAtrbsPEO7EffStartDt | EFFECTIVE_START_DATE | — | — |
| 224 | AllocLnAtrbsPEO7TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 225 | AllocLnAtrbsPEO8AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 226 | AllocLnAtrbsPEO8AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 227 | AllocLnAtrbsPEO8AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 228 | AllocLnAtrbsPEO8AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 229 | AllocLnAtrbsPEO8AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 230 | AllocLnAtrbsPEO8EffEndDt | EFFECTIVE_END_DATE | — | — |
| 231 | AllocLnAtrbsPEO8EffStartDt | EFFECTIVE_START_DATE | — | — |
| 232 | AllocLnAtrbsPEO8TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |
| 233 | AllocLnAtrbsPEO9AllocLnAtrbId | ALLOCATION_LN_ATRB_ID | — | ✅ |
| 234 | AllocLnAtrbsPEO9AtrbDataType | ATRB_DATA_TYPE | — | ✅ |
| 235 | AllocLnAtrbsPEO9AtrbValueDttm | ATRB_VALUE_TIMESTAMP | — | ✅ |
| 236 | AllocLnAtrbsPEO9AtrbValueNum | ATRB_VALUE_NUMBER | — | ✅ |
| 237 | AllocLnAtrbsPEO9AtrbValueText | ATRB_VALUE_TEXT | — | ✅ |
| 238 | AllocLnAtrbsPEO9EffEndDt | EFFECTIVE_END_DATE | — | — |
| 239 | AllocLnAtrbsPEO9EffStartDt | EFFECTIVE_START_DATE | — | — |
| 240 | AllocLnAtrbsPEO9TmAtrbFldId | TM_ATRB_FLD_ID | — | ✅ |

### [[hwm_allocation_rules_f|HWM_ALLOCATION_RULES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllocRulesPEOAllocationId | ALLOCATION_ID | — | ✅ |
| 2 | AllocRulesPEOAllocationRuleId | ALLOCATION_RULE_ID | — | — |
| 3 | AllocRulesPEOAllocationType | ALLOCATION_TYPE | — | ✅ |
| 4 | AllocRulesPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AllocRulesPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AllocRulesPEODataLevel | DATA_LEVEL | — | — |
| 7 | AllocRulesPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | AllocRulesPEOEffectiveStartDt | EFFECTIVE_START_DATE | — | — |
| 9 | AllocRulesPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 10 | AllocRulesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | AllocRulesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | AllocRulesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | AllocRulesPEOModuleId | MODULE_ID | — | — |
| 14 | AllocRulesPEOObjectVersionNum | OBJECT_VERSION_NUMBER | — | — |
| 15 | AllocRulesPEORulePriority | ALLOCATION_RULE_PRIORITY | — | ✅ |
| 16 | AllocRulesPEORunSummationLvl | RUN_SUMMATION_LEVEL | — | ✅ |
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
