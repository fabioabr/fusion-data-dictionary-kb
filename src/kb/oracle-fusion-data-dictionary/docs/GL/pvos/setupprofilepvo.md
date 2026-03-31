---
id: DOC-GL-PVO-SetupProfilePVO
doc_type: system-doc
title: "SetupProfilePVO — PVO General Ledger"
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
  - SetupProfilePVO
  - setupprofilepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SetupProfilePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Setup Profile. Acessa as tabelas: HTS_LABOR_DEMAND_PRFL_DEFS, HTS_LABOR_DEMAND_PRFL_DEFSETS, HTS_LABOR_DEMAND_PRFL_VALS (+6).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.SetupOptionsAM.SetupProfilePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 519 | 9 | 1 | 173 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[hts_labor_demand_prfl_defs|HTS_LABOR_DEMAND_PRFL_DEFS]] — 1 atributos (1 BICC)
- [[hts_labor_demand_prfl_defsets|HTS_LABOR_DEMAND_PRFL_DEFSETS]] — 1 atributos (1 BICC)
- [[hts_labor_demand_prfl_vals|HTS_LABOR_DEMAND_PRFL_VALS]] — 14 atributos (7 BICC)
- [[hwm_grps_vl|HWM_GRPS_VL]] — 4 atributos (2 BICC)
- [[hxt_setup_option_vals|HXT_SETUP_OPTION_VALS]] — 475 atributos (147 BICC)
- [[hxt_setup_profiles_b|HXT_SETUP_PROFILES_B]] — 12 atributos (1 PKs, 9 BICC)
- [[hxt_setup_profiles_tl|HXT_SETUP_PROFILES_TL]] — 4 atributos (2 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 4 atributos (2 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 4 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hts_labor_demand_prfl_defs|HTS_LABOR_DEMAND_PRFL_DEFS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LbrDmdPrflDefPEOLbrDmdPrflDefId | LBR_DMD_PRFL_DEF_ID | — | ✅ |

### [[hts_labor_demand_prfl_defsets|HTS_LABOR_DEMAND_PRFL_DEFSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LbrDmdPrflDefSetDPEOLbrDmdPrflSetId | LBR_DMD_PRFL_SET_ID | — | ✅ |

### [[hts_labor_demand_prfl_vals|HTS_LABOR_DEMAND_PRFL_VALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LbrDmdPrflValPEO1Value | VALUE | — | ✅ |
| 2 | LbrDmdPrflValPEO1ValueId | VALUE_ID | — | — |
| 3 | LbrDmdPrflValPEO2Value | VALUE | — | ✅ |
| 4 | LbrDmdPrflValPEO2ValueId | VALUE_ID | — | — |
| 5 | LbrDmdPrflValPEO3Value | VALUE | — | ✅ |
| 6 | LbrDmdPrflValPEO3ValueId | VALUE_ID | — | — |
| 7 | LbrDmdPrflValPEO4Value | VALUE | — | ✅ |
| 8 | LbrDmdPrflValPEO4ValueId | VALUE_ID | — | — |
| 9 | LbrDmdPrflValPEO5Value | VALUE | — | ✅ |
| 10 | LbrDmdPrflValPEO5ValueId | VALUE_ID | — | — |
| 11 | LbrDmdPrflValPEO6Value | VALUE | — | ✅ |
| 12 | LbrDmdPrflValPEO6ValueId | VALUE_ID | — | — |
| 13 | LbrDmdPrflValPEOValue | VALUE | — | ✅ |
| 14 | LbrDmdPrflValPEOValueId | VALUE_ID | — | — |

### [[hwm_grps_vl|HWM_GRPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MgrGroupPEOGroupName | GROUP_NAME | — | ✅ |
| 2 | MgrGroupPEOGrpId | GRP_ID | — | — |
| 3 | SchGroupPEOGroupName | GROUP_NAME | — | ✅ |
| 4 | SchGroupPEOGrpId | GRP_ID | — | — |

### [[hxt_setup_option_vals|HXT_SETUP_OPTION_VALS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CorePrflValueDPEOCreatedBy | CREATED_BY | — | — |
| 2 | CorePrflValueDPEOCreationDate | CREATION_DATE | — | — |
| 3 | CorePrflValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 4 | CorePrflValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | CorePrflValueDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | CorePrflValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CorePrflValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | CorePrflValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | CorePrflValueDPEOModuleId | MODULE_ID | — | — |
| 10 | CorePrflValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CorePrflValueDPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | CorePrflValueDPEOSetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 13 | CorePrflValueDPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | ✅ |
| 14 | CorePrflValueDPEOSetupProfileId | SETUP_PROFILE_ID | — | — |
| 15 | CorePrflValueDPEOSguid | SGUID | — | — |
| 16 | CorePrflValueDPEOType | TYPE | — | — |
| 17 | CorePrflValueDPEOValue1 | VALUE1 | — | — |
| 18 | CorePrflValueDPEOValue10 | VALUE10 | — | — |
| 19 | CorePrflValueDPEOValue11 | VALUE11 | — | — |
| 20 | CorePrflValueDPEOValue12 | VALUE12 | — | — |
| 21 | CorePrflValueDPEOValue13 | VALUE13 | — | — |
| 22 | CorePrflValueDPEOValue14 | VALUE14 | — | — |
| 23 | CorePrflValueDPEOValue15 | VALUE15 | — | — |
| 24 | CorePrflValueDPEOValue16 | VALUE16 | — | — |
| 25 | CorePrflValueDPEOValue17 | VALUE17 | — | — |
| 26 | CorePrflValueDPEOValue18 | VALUE18 | — | — |
| 27 | CorePrflValueDPEOValue19 | VALUE19 | — | — |
| 28 | CorePrflValueDPEOValue2 | VALUE2 | — | — |
| 29 | CorePrflValueDPEOValue20 | VALUE20 | — | — |
| 30 | CorePrflValueDPEOValue21 | VALUE21 | — | — |
| 31 | CorePrflValueDPEOValue22 | VALUE22 | — | — |
| 32 | CorePrflValueDPEOValue23 | VALUE23 | — | — |
| 33 | CorePrflValueDPEOValue24 | VALUE24 | — | — |
| 34 | CorePrflValueDPEOValue25 | VALUE25 | — | — |
| 35 | CorePrflValueDPEOValue26 | VALUE26 | — | — |
| 36 | CorePrflValueDPEOValue27 | VALUE27 | — | — |
| 37 | CorePrflValueDPEOValue28 | VALUE28 | — | — |
| 38 | CorePrflValueDPEOValue29 | VALUE29 | — | — |
| 39 | CorePrflValueDPEOValue3 | VALUE3 | — | — |
| 40 | CorePrflValueDPEOValue30 | VALUE30 | — | ✅ |
| 41 | CorePrflValueDPEOValue31 | VALUE31 | — | ✅ |
| 42 | CorePrflValueDPEOValue32 | VALUE32 | — | ✅ |
| 43 | CorePrflValueDPEOValue33 | VALUE33 | — | ✅ |
| 44 | CorePrflValueDPEOValue34 | VALUE34 | — | ✅ |
| 45 | CorePrflValueDPEOValue35 | VALUE35 | — | — |
| 46 | CorePrflValueDPEOValue36 | VALUE36 | — | — |
| 47 | CorePrflValueDPEOValue37 | VALUE37 | — | — |
| 48 | CorePrflValueDPEOValue38 | VALUE38 | — | — |
| 49 | CorePrflValueDPEOValue39 | VALUE39 | — | — |
| 50 | CorePrflValueDPEOValue4 | VALUE4 | — | — |
| 51 | CorePrflValueDPEOValue40 | VALUE40 | — | — |
| 52 | CorePrflValueDPEOValue41 | VALUE41 | — | — |
| 53 | CorePrflValueDPEOValue42 | VALUE42 | — | — |
| 54 | CorePrflValueDPEOValue43 | VALUE43 | — | — |
| 55 | CorePrflValueDPEOValue44 | VALUE44 | — | — |
| 56 | CorePrflValueDPEOValue45 | VALUE45 | — | — |
| 57 | CorePrflValueDPEOValue46 | VALUE46 | — | — |
| 58 | CorePrflValueDPEOValue47 | VALUE47 | — | — |
| 59 | CorePrflValueDPEOValue48 | VALUE48 | — | — |
| 60 | CorePrflValueDPEOValue49 | VALUE49 | — | — |
| 61 | CorePrflValueDPEOValue5 | VALUE5 | — | — |
| 62 | CorePrflValueDPEOValue50 | VALUE50 | — | — |
| 63 | CorePrflValueDPEOValue51 | VALUE51 | — | — |
| 64 | CorePrflValueDPEOValue52 | VALUE52 | — | — |
| 65 | CorePrflValueDPEOValue53 | VALUE53 | — | — |
| 66 | CorePrflValueDPEOValue54 | VALUE54 | — | — |
| 67 | CorePrflValueDPEOValue55 | VALUE55 | — | — |
| 68 | CorePrflValueDPEOValue56 | VALUE56 | — | — |
| 69 | CorePrflValueDPEOValue57 | VALUE57 | — | — |
| 70 | CorePrflValueDPEOValue58 | VALUE58 | — | — |
| 71 | CorePrflValueDPEOValue59 | VALUE59 | — | — |
| 72 | CorePrflValueDPEOValue6 | VALUE6 | — | — |
| 73 | CorePrflValueDPEOValue60 | VALUE60 | — | — |
| 74 | CorePrflValueDPEOValue61 | VALUE61 | — | — |
| 75 | CorePrflValueDPEOValue62 | VALUE62 | — | — |
| 76 | CorePrflValueDPEOValue63 | VALUE63 | — | — |
| 77 | CorePrflValueDPEOValue64 | VALUE64 | — | — |
| 78 | CorePrflValueDPEOValue65 | VALUE65 | — | — |
| 79 | CorePrflValueDPEOValue66 | VALUE66 | — | — |
| 80 | CorePrflValueDPEOValue67 | VALUE67 | — | — |
| 81 | CorePrflValueDPEOValue68 | VALUE68 | — | — |
| 82 | CorePrflValueDPEOValue69 | VALUE69 | — | — |
| 83 | CorePrflValueDPEOValue7 | VALUE7 | — | — |
| 84 | CorePrflValueDPEOValue70 | VALUE70 | — | — |
| 85 | CorePrflValueDPEOValue71 | VALUE71 | — | — |
| 86 | CorePrflValueDPEOValue72 | VALUE72 | — | — |
| 87 | CorePrflValueDPEOValue73 | VALUE73 | — | — |
| 88 | CorePrflValueDPEOValue74 | VALUE74 | — | — |
| 89 | CorePrflValueDPEOValue75 | VALUE75 | — | — |
| 90 | CorePrflValueDPEOValue76 | VALUE76 | — | — |
| 91 | CorePrflValueDPEOValue77 | VALUE77 | — | — |
| 92 | CorePrflValueDPEOValue78 | VALUE78 | — | — |
| 93 | CorePrflValueDPEOValue79 | VALUE79 | — | — |
| 94 | CorePrflValueDPEOValue8 | VALUE8 | — | — |
| 95 | CorePrflValueDPEOValue9 | VALUE9 | — | — |
| 96 | HtsPrflValueDPEOCreatedBy | CREATED_BY | — | — |
| 97 | HtsPrflValueDPEOCreationDate | CREATION_DATE | — | — |
| 98 | HtsPrflValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 99 | HtsPrflValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 100 | HtsPrflValueDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 101 | HtsPrflValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 102 | HtsPrflValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 103 | HtsPrflValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 104 | HtsPrflValueDPEOModuleId | MODULE_ID | — | — |
| 105 | HtsPrflValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 106 | HtsPrflValueDPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 107 | HtsPrflValueDPEOSetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 108 | HtsPrflValueDPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | ✅ |
| 109 | HtsPrflValueDPEOSetupProfileId | SETUP_PROFILE_ID | — | — |
| 110 | HtsPrflValueDPEOSguid | SGUID | — | — |
| 111 | HtsPrflValueDPEOType | TYPE | — | — |
| 112 | HtsPrflValueDPEOValue1 | VALUE1 | — | — |
| 113 | HtsPrflValueDPEOValue10 | VALUE10 | — | — |
| 114 | HtsPrflValueDPEOValue11 | VALUE11 | — | ✅ |
| 115 | HtsPrflValueDPEOValue12 | VALUE12 | — | ✅ |
| 116 | HtsPrflValueDPEOValue13 | VALUE13 | — | — |
| 117 | HtsPrflValueDPEOValue14 | VALUE14 | — | ✅ |
| 118 | HtsPrflValueDPEOValue15 | VALUE15 | — | ✅ |
| 119 | HtsPrflValueDPEOValue16 | VALUE16 | — | ✅ |
| 120 | HtsPrflValueDPEOValue17 | VALUE17 | — | ✅ |
| 121 | HtsPrflValueDPEOValue18 | VALUE18 | — | — |
| 122 | HtsPrflValueDPEOValue19 | VALUE19 | — | — |
| 123 | HtsPrflValueDPEOValue2 | VALUE2 | — | — |
| 124 | HtsPrflValueDPEOValue20 | VALUE20 | — | — |
| 125 | HtsPrflValueDPEOValue21 | VALUE21 | — | — |
| 126 | HtsPrflValueDPEOValue22 | VALUE22 | — | — |
| 127 | HtsPrflValueDPEOValue23 | VALUE23 | — | — |
| 128 | HtsPrflValueDPEOValue24 | VALUE24 | — | — |
| 129 | HtsPrflValueDPEOValue25 | VALUE25 | — | — |
| 130 | HtsPrflValueDPEOValue26 | VALUE26 | — | — |
| 131 | HtsPrflValueDPEOValue27 | VALUE27 | — | — |
| 132 | HtsPrflValueDPEOValue28 | VALUE28 | — | — |
| 133 | HtsPrflValueDPEOValue29 | VALUE29 | — | — |
| 134 | HtsPrflValueDPEOValue3 | VALUE3 | — | — |
| 135 | HtsPrflValueDPEOValue30 | VALUE30 | — | — |
| 136 | HtsPrflValueDPEOValue31 | VALUE31 | — | — |
| 137 | HtsPrflValueDPEOValue32 | VALUE32 | — | — |
| 138 | HtsPrflValueDPEOValue33 | VALUE33 | — | — |
| 139 | HtsPrflValueDPEOValue34 | VALUE34 | — | — |
| 140 | HtsPrflValueDPEOValue35 | VALUE35 | — | — |
| 141 | HtsPrflValueDPEOValue36 | VALUE36 | — | — |
| 142 | HtsPrflValueDPEOValue37 | VALUE37 | — | — |
| 143 | HtsPrflValueDPEOValue38 | VALUE38 | — | — |
| 144 | HtsPrflValueDPEOValue39 | VALUE39 | — | — |
| 145 | HtsPrflValueDPEOValue4 | VALUE4 | — | — |
| 146 | HtsPrflValueDPEOValue40 | VALUE40 | — | — |
| 147 | HtsPrflValueDPEOValue41 | VALUE41 | — | — |
| 148 | HtsPrflValueDPEOValue42 | VALUE42 | — | — |
| 149 | HtsPrflValueDPEOValue43 | VALUE43 | — | — |
| 150 | HtsPrflValueDPEOValue44 | VALUE44 | — | — |
| 151 | HtsPrflValueDPEOValue45 | VALUE45 | — | — |
| 152 | HtsPrflValueDPEOValue46 | VALUE46 | — | — |
| 153 | HtsPrflValueDPEOValue47 | VALUE47 | — | — |
| 154 | HtsPrflValueDPEOValue48 | VALUE48 | — | — |
| 155 | HtsPrflValueDPEOValue49 | VALUE49 | — | — |
| 156 | HtsPrflValueDPEOValue5 | VALUE5 | — | — |
| 157 | HtsPrflValueDPEOValue50 | VALUE50 | — | ✅ |
| 158 | HtsPrflValueDPEOValue51 | VALUE51 | — | ✅ |
| 159 | HtsPrflValueDPEOValue52 | VALUE52 | — | ✅ |
| 160 | HtsPrflValueDPEOValue53 | VALUE53 | — | ✅ |
| 161 | HtsPrflValueDPEOValue54 | VALUE54 | — | ✅ |
| 162 | HtsPrflValueDPEOValue55 | VALUE55 | — | ✅ |
| 163 | HtsPrflValueDPEOValue56 | VALUE56 | — | — |
| 164 | HtsPrflValueDPEOValue57 | VALUE57 | — | — |
| 165 | HtsPrflValueDPEOValue58 | VALUE58 | — | — |
| 166 | HtsPrflValueDPEOValue59 | VALUE59 | — | — |
| 167 | HtsPrflValueDPEOValue6 | VALUE6 | — | — |
| 168 | HtsPrflValueDPEOValue60 | VALUE60 | — | — |
| 169 | HtsPrflValueDPEOValue61 | VALUE61 | — | — |
| 170 | HtsPrflValueDPEOValue62 | VALUE62 | — | — |
| 171 | HtsPrflValueDPEOValue63 | VALUE63 | — | — |
| 172 | HtsPrflValueDPEOValue64 | VALUE64 | — | — |
| 173 | HtsPrflValueDPEOValue65 | VALUE65 | — | — |
| 174 | HtsPrflValueDPEOValue66 | VALUE66 | — | — |
| 175 | HtsPrflValueDPEOValue67 | VALUE67 | — | — |
| 176 | HtsPrflValueDPEOValue68 | VALUE68 | — | — |
| 177 | HtsPrflValueDPEOValue69 | VALUE69 | — | — |
| 178 | HtsPrflValueDPEOValue7 | VALUE7 | — | — |
| 179 | HtsPrflValueDPEOValue70 | VALUE70 | — | — |
| 180 | HtsPrflValueDPEOValue72 | VALUE72 | — | — |
| 181 | HtsPrflValueDPEOValue73 | VALUE73 | — | — |
| 182 | HtsPrflValueDPEOValue74 | VALUE74 | — | — |
| 183 | HtsPrflValueDPEOValue75 | VALUE75 | — | — |
| 184 | HtsPrflValueDPEOValue76 | VALUE76 | — | — |
| 185 | HtsPrflValueDPEOValue77 | VALUE77 | — | — |
| 186 | HtsPrflValueDPEOValue78 | VALUE78 | — | — |
| 187 | HtsPrflValueDPEOValue79 | VALUE79 | — | — |
| 188 | HtsPrflValueDPEOValue8 | VALUE8 | — | — |
| 189 | HtsPrflValueDPEOValue9 | VALUE9 | — | — |
| 190 | HtsPrflValueDPEOalue71 | VALUE71 | — | — |
| 191 | MgrPrflValueDPEOCreatedBy | CREATED_BY | — | — |
| 192 | MgrPrflValueDPEOCreationDate | CREATION_DATE | — | — |
| 193 | MgrPrflValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 194 | MgrPrflValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 195 | MgrPrflValueDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 196 | MgrPrflValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 197 | MgrPrflValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 198 | MgrPrflValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 199 | MgrPrflValueDPEOModuleId | MODULE_ID | — | — |
| 200 | MgrPrflValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 201 | MgrPrflValueDPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 202 | MgrPrflValueDPEOSetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 203 | MgrPrflValueDPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | ✅ |
| 204 | MgrPrflValueDPEOSetupProfileId | SETUP_PROFILE_ID | — | — |
| 205 | MgrPrflValueDPEOSguid | SGUID | — | — |
| 206 | MgrPrflValueDPEOType | TYPE | — | — |
| 207 | MgrPrflValueDPEOValue1 | VALUE1 | — | ✅ |
| 208 | MgrPrflValueDPEOValue10 | VALUE10 | — | ✅ |
| 209 | MgrPrflValueDPEOValue11 | VALUE11 | — | ✅ |
| 210 | MgrPrflValueDPEOValue12 | VALUE12 | — | ✅ |
| 211 | MgrPrflValueDPEOValue13 | VALUE13 | — | ✅ |
| 212 | MgrPrflValueDPEOValue14 | VALUE14 | — | ✅ |
| 213 | MgrPrflValueDPEOValue15 | VALUE15 | — | — |
| 214 | MgrPrflValueDPEOValue16 | VALUE16 | — | ✅ |
| 215 | MgrPrflValueDPEOValue17 | VALUE17 | — | ✅ |
| 216 | MgrPrflValueDPEOValue18 | VALUE18 | — | ✅ |
| 217 | MgrPrflValueDPEOValue19 | VALUE19 | — | ✅ |
| 218 | MgrPrflValueDPEOValue2 | VALUE2 | — | ✅ |
| 219 | MgrPrflValueDPEOValue20 | VALUE20 | — | ✅ |
| 220 | MgrPrflValueDPEOValue21 | VALUE21 | — | — |
| 221 | MgrPrflValueDPEOValue22 | VALUE22 | — | — |
| 222 | MgrPrflValueDPEOValue23 | VALUE23 | — | — |
| 223 | MgrPrflValueDPEOValue24 | VALUE24 | — | — |
| 224 | MgrPrflValueDPEOValue25 | VALUE25 | — | — |
| 225 | MgrPrflValueDPEOValue26 | VALUE26 | — | — |
| 226 | MgrPrflValueDPEOValue27 | VALUE27 | — | — |
| 227 | MgrPrflValueDPEOValue28 | VALUE28 | — | — |
| 228 | MgrPrflValueDPEOValue29 | VALUE29 | — | — |
| 229 | MgrPrflValueDPEOValue3 | VALUE3 | — | — |
| 230 | MgrPrflValueDPEOValue30 | VALUE30 | — | ✅ |
| 231 | MgrPrflValueDPEOValue31 | VALUE31 | — | — |
| 232 | MgrPrflValueDPEOValue32 | VALUE32 | — | ✅ |
| 233 | MgrPrflValueDPEOValue33 | VALUE33 | — | ✅ |
| 234 | MgrPrflValueDPEOValue34 | VALUE34 | — | ✅ |
| 235 | MgrPrflValueDPEOValue35 | VALUE35 | — | ✅ |
| 236 | MgrPrflValueDPEOValue36 | VALUE36 | — | — |
| 237 | MgrPrflValueDPEOValue37 | VALUE37 | — | — |
| 238 | MgrPrflValueDPEOValue38 | VALUE38 | — | ✅ |
| 239 | MgrPrflValueDPEOValue39 | VALUE39 | — | ✅ |
| 240 | MgrPrflValueDPEOValue4 | VALUE4 | — | ✅ |
| 241 | MgrPrflValueDPEOValue40 | VALUE40 | — | ✅ |
| 242 | MgrPrflValueDPEOValue41 | VALUE41 | — | ✅ |
| 243 | MgrPrflValueDPEOValue42 | VALUE42 | — | ✅ |
| 244 | MgrPrflValueDPEOValue43 | VALUE43 | — | ✅ |
| 245 | MgrPrflValueDPEOValue44 | VALUE44 | — | ✅ |
| 246 | MgrPrflValueDPEOValue45 | VALUE45 | — | ✅ |
| 247 | MgrPrflValueDPEOValue46 | VALUE46 | — | ✅ |
| 248 | MgrPrflValueDPEOValue47 | VALUE47 | — | ✅ |
| 249 | MgrPrflValueDPEOValue48 | VALUE48 | — | — |
| 250 | MgrPrflValueDPEOValue49 | VALUE49 | — | — |
| 251 | MgrPrflValueDPEOValue5 | VALUE5 | — | ✅ |
| 252 | MgrPrflValueDPEOValue50 | VALUE50 | — | ✅ |
| 253 | MgrPrflValueDPEOValue51 | VALUE51 | — | ✅ |
| 254 | MgrPrflValueDPEOValue52 | VALUE52 | — | ✅ |
| 255 | MgrPrflValueDPEOValue53 | VALUE53 | — | ✅ |
| 256 | MgrPrflValueDPEOValue54 | VALUE54 | — | ✅ |
| 257 | MgrPrflValueDPEOValue55 | VALUE55 | — | ✅ |
| 258 | MgrPrflValueDPEOValue56 | VALUE56 | — | ✅ |
| 259 | MgrPrflValueDPEOValue57 | VALUE57 | — | ✅ |
| 260 | MgrPrflValueDPEOValue58 | VALUE58 | — | ✅ |
| 261 | MgrPrflValueDPEOValue59 | VALUE59 | — | ✅ |
| 262 | MgrPrflValueDPEOValue6 | VALUE6 | — | ✅ |
| 263 | MgrPrflValueDPEOValue60 | VALUE60 | — | — |
| 264 | MgrPrflValueDPEOValue61 | VALUE61 | — | — |
| 265 | MgrPrflValueDPEOValue62 | VALUE62 | — | ✅ |
| 266 | MgrPrflValueDPEOValue63 | VALUE63 | — | ✅ |
| 267 | MgrPrflValueDPEOValue64 | VALUE64 | — | ✅ |
| 268 | MgrPrflValueDPEOValue65 | VALUE65 | — | ✅ |
| 269 | MgrPrflValueDPEOValue66 | VALUE66 | — | ✅ |
| 270 | MgrPrflValueDPEOValue67 | VALUE67 | — | ✅ |
| 271 | MgrPrflValueDPEOValue68 | VALUE68 | — | ✅ |
| 272 | MgrPrflValueDPEOValue69 | VALUE69 | — | ✅ |
| 273 | MgrPrflValueDPEOValue7 | VALUE7 | — | ✅ |
| 274 | MgrPrflValueDPEOValue70 | VALUE70 | — | — |
| 275 | MgrPrflValueDPEOValue71 | VALUE71 | — | — |
| 276 | MgrPrflValueDPEOValue72 | VALUE72 | — | — |
| 277 | MgrPrflValueDPEOValue73 | VALUE73 | — | — |
| 278 | MgrPrflValueDPEOValue74 | VALUE74 | — | — |
| 279 | MgrPrflValueDPEOValue75 | VALUE75 | — | — |
| 280 | MgrPrflValueDPEOValue76 | VALUE76 | — | — |
| 281 | MgrPrflValueDPEOValue77 | VALUE77 | — | — |
| 282 | MgrPrflValueDPEOValue78 | VALUE78 | — | — |
| 283 | MgrPrflValueDPEOValue79 | VALUE79 | — | — |
| 284 | MgrPrflValueDPEOValue8 | VALUE8 | — | ✅ |
| 285 | MgrPrflValueDPEOValue9 | VALUE9 | — | — |
| 286 | TcdPrflValueDPEOCreatedBy | CREATED_BY | — | — |
| 287 | TcdPrflValueDPEOCreationDate | CREATION_DATE | — | — |
| 288 | TcdPrflValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 289 | TcdPrflValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 290 | TcdPrflValueDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 291 | TcdPrflValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 292 | TcdPrflValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 293 | TcdPrflValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 294 | TcdPrflValueDPEOModuleId | MODULE_ID | — | — |
| 295 | TcdPrflValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 296 | TcdPrflValueDPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 297 | TcdPrflValueDPEOSetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 298 | TcdPrflValueDPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | ✅ |
| 299 | TcdPrflValueDPEOSetupProfileId | SETUP_PROFILE_ID | — | — |
| 300 | TcdPrflValueDPEOSguid | SGUID | — | — |
| 301 | TcdPrflValueDPEOType | TYPE | — | — |
| 302 | TcdPrflValueDPEOValue1 | VALUE1 | — | — |
| 303 | TcdPrflValueDPEOValue10 | VALUE10 | — | ✅ |
| 304 | TcdPrflValueDPEOValue11 | VALUE11 | — | — |
| 305 | TcdPrflValueDPEOValue12 | VALUE12 | — | — |
| 306 | TcdPrflValueDPEOValue13 | VALUE13 | — | — |
| 307 | TcdPrflValueDPEOValue14 | VALUE14 | — | — |
| 308 | TcdPrflValueDPEOValue15 | VALUE15 | — | — |
| 309 | TcdPrflValueDPEOValue16 | VALUE16 | — | — |
| 310 | TcdPrflValueDPEOValue17 | VALUE17 | — | — |
| 311 | TcdPrflValueDPEOValue18 | VALUE18 | — | — |
| 312 | TcdPrflValueDPEOValue19 | VALUE19 | — | — |
| 313 | TcdPrflValueDPEOValue2 | VALUE2 | — | — |
| 314 | TcdPrflValueDPEOValue20 | VALUE20 | — | — |
| 315 | TcdPrflValueDPEOValue21 | VALUE21 | — | — |
| 316 | TcdPrflValueDPEOValue22 | VALUE22 | — | — |
| 317 | TcdPrflValueDPEOValue23 | VALUE23 | — | — |
| 318 | TcdPrflValueDPEOValue24 | VALUE24 | — | — |
| 319 | TcdPrflValueDPEOValue25 | VALUE25 | — | — |
| 320 | TcdPrflValueDPEOValue26 | VALUE26 | — | — |
| 321 | TcdPrflValueDPEOValue27 | VALUE27 | — | — |
| 322 | TcdPrflValueDPEOValue28 | VALUE28 | — | — |
| 323 | TcdPrflValueDPEOValue29 | VALUE29 | — | — |
| 324 | TcdPrflValueDPEOValue3 | VALUE3 | — | — |
| 325 | TcdPrflValueDPEOValue30 | VALUE30 | — | ✅ |
| 326 | TcdPrflValueDPEOValue31 | VALUE31 | — | ✅ |
| 327 | TcdPrflValueDPEOValue32 | VALUE32 | — | ✅ |
| 328 | TcdPrflValueDPEOValue33 | VALUE33 | — | ✅ |
| 329 | TcdPrflValueDPEOValue34 | VALUE34 | — | — |
| 330 | TcdPrflValueDPEOValue35 | VALUE35 | — | — |
| 331 | TcdPrflValueDPEOValue36 | VALUE36 | — | — |
| 332 | TcdPrflValueDPEOValue37 | VALUE37 | — | — |
| 333 | TcdPrflValueDPEOValue38 | VALUE38 | — | — |
| 334 | TcdPrflValueDPEOValue39 | VALUE39 | — | — |
| 335 | TcdPrflValueDPEOValue4 | VALUE4 | — | — |
| 336 | TcdPrflValueDPEOValue40 | VALUE40 | — | — |
| 337 | TcdPrflValueDPEOValue41 | VALUE41 | — | — |
| 338 | TcdPrflValueDPEOValue42 | VALUE42 | — | — |
| 339 | TcdPrflValueDPEOValue43 | VALUE43 | — | — |
| 340 | TcdPrflValueDPEOValue44 | VALUE44 | — | — |
| 341 | TcdPrflValueDPEOValue45 | VALUE45 | — | — |
| 342 | TcdPrflValueDPEOValue46 | VALUE46 | — | — |
| 343 | TcdPrflValueDPEOValue47 | VALUE47 | — | — |
| 344 | TcdPrflValueDPEOValue48 | VALUE48 | — | — |
| 345 | TcdPrflValueDPEOValue49 | VALUE49 | — | — |
| 346 | TcdPrflValueDPEOValue5 | VALUE5 | — | — |
| 347 | TcdPrflValueDPEOValue50 | VALUE50 | — | — |
| 348 | TcdPrflValueDPEOValue51 | VALUE51 | — | — |
| 349 | TcdPrflValueDPEOValue52 | VALUE52 | — | — |
| 350 | TcdPrflValueDPEOValue53 | VALUE53 | — | — |
| 351 | TcdPrflValueDPEOValue54 | VALUE54 | — | — |
| 352 | TcdPrflValueDPEOValue55 | VALUE55 | — | — |
| 353 | TcdPrflValueDPEOValue56 | VALUE56 | — | — |
| 354 | TcdPrflValueDPEOValue57 | VALUE57 | — | — |
| 355 | TcdPrflValueDPEOValue58 | VALUE58 | — | — |
| 356 | TcdPrflValueDPEOValue59 | VALUE59 | — | — |
| 357 | TcdPrflValueDPEOValue6 | VALUE6 | — | — |
| 358 | TcdPrflValueDPEOValue60 | VALUE60 | — | — |
| 359 | TcdPrflValueDPEOValue61 | VALUE61 | — | — |
| 360 | TcdPrflValueDPEOValue62 | VALUE62 | — | — |
| 361 | TcdPrflValueDPEOValue63 | VALUE63 | — | — |
| 362 | TcdPrflValueDPEOValue64 | VALUE64 | — | — |
| 363 | TcdPrflValueDPEOValue65 | VALUE65 | — | — |
| 364 | TcdPrflValueDPEOValue66 | VALUE66 | — | — |
| 365 | TcdPrflValueDPEOValue67 | VALUE67 | — | — |
| 366 | TcdPrflValueDPEOValue68 | VALUE68 | — | — |
| 367 | TcdPrflValueDPEOValue69 | VALUE69 | — | — |
| 368 | TcdPrflValueDPEOValue7 | VALUE7 | — | — |
| 369 | TcdPrflValueDPEOValue70 | VALUE70 | — | — |
| 370 | TcdPrflValueDPEOValue71 | VALUE71 | — | — |
| 371 | TcdPrflValueDPEOValue72 | VALUE72 | — | — |
| 372 | TcdPrflValueDPEOValue73 | VALUE73 | — | — |
| 373 | TcdPrflValueDPEOValue74 | VALUE74 | — | — |
| 374 | TcdPrflValueDPEOValue75 | VALUE75 | — | — |
| 375 | TcdPrflValueDPEOValue76 | VALUE76 | — | — |
| 376 | TcdPrflValueDPEOValue77 | VALUE77 | — | — |
| 377 | TcdPrflValueDPEOValue78 | VALUE78 | — | — |
| 378 | TcdPrflValueDPEOValue79 | VALUE79 | — | — |
| 379 | TcdPrflValueDPEOValue8 | VALUE8 | — | — |
| 380 | TcdPrflValueDPEOValue9 | VALUE9 | — | — |
| 381 | WkrPrflValueDPEOCreatedBy | CREATED_BY | — | — |
| 382 | WkrPrflValueDPEOCreationDate | CREATION_DATE | — | — |
| 383 | WkrPrflValueDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 384 | WkrPrflValueDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 385 | WkrPrflValueDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 386 | WkrPrflValueDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 387 | WkrPrflValueDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 388 | WkrPrflValueDPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 389 | WkrPrflValueDPEOModuleId | MODULE_ID | — | — |
| 390 | WkrPrflValueDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 391 | WkrPrflValueDPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 392 | WkrPrflValueDPEOSetupOptionValCd | SETUP_OPTION_VAL_CD | — | ✅ |
| 393 | WkrPrflValueDPEOSetupOptionValId | SETUP_OPTION_VAL_ID | — | ✅ |
| 394 | WkrPrflValueDPEOSetupProfileId | SETUP_PROFILE_ID | — | — |
| 395 | WkrPrflValueDPEOSguid | SGUID | — | — |
| 396 | WkrPrflValueDPEOType | TYPE | — | — |
| 397 | WkrPrflValueDPEOValue1 | VALUE1 | — | ✅ |
| 398 | WkrPrflValueDPEOValue10 | VALUE10 | — | ✅ |
| 399 | WkrPrflValueDPEOValue11 | VALUE11 | — | ✅ |
| 400 | WkrPrflValueDPEOValue12 | VALUE12 | — | ✅ |
| 401 | WkrPrflValueDPEOValue13 | VALUE13 | — | ✅ |
| 402 | WkrPrflValueDPEOValue14 | VALUE14 | — | ✅ |
| 403 | WkrPrflValueDPEOValue15 | VALUE15 | — | — |
| 404 | WkrPrflValueDPEOValue16 | VALUE16 | — | ✅ |
| 405 | WkrPrflValueDPEOValue17 | VALUE17 | — | ✅ |
| 406 | WkrPrflValueDPEOValue18 | VALUE18 | — | ✅ |
| 407 | WkrPrflValueDPEOValue19 | VALUE19 | — | ✅ |
| 408 | WkrPrflValueDPEOValue2 | VALUE2 | — | ✅ |
| 409 | WkrPrflValueDPEOValue20 | VALUE20 | — | ✅ |
| 410 | WkrPrflValueDPEOValue21 | VALUE21 | — | — |
| 411 | WkrPrflValueDPEOValue22 | VALUE22 | — | — |
| 412 | WkrPrflValueDPEOValue23 | VALUE23 | — | — |
| 413 | WkrPrflValueDPEOValue24 | VALUE24 | — | — |
| 414 | WkrPrflValueDPEOValue25 | VALUE25 | — | — |
| 415 | WkrPrflValueDPEOValue26 | VALUE26 | — | — |
| 416 | WkrPrflValueDPEOValue27 | VALUE27 | — | — |
| 417 | WkrPrflValueDPEOValue28 | VALUE28 | — | — |
| 418 | WkrPrflValueDPEOValue29 | VALUE29 | — | — |
| 419 | WkrPrflValueDPEOValue3 | VALUE3 | — | — |
| 420 | WkrPrflValueDPEOValue30 | VALUE30 | — | ✅ |
| 421 | WkrPrflValueDPEOValue31 | VALUE31 | — | — |
| 422 | WkrPrflValueDPEOValue32 | VALUE32 | — | ✅ |
| 423 | WkrPrflValueDPEOValue33 | VALUE33 | — | ✅ |
| 424 | WkrPrflValueDPEOValue34 | VALUE34 | — | ✅ |
| 425 | WkrPrflValueDPEOValue35 | VALUE35 | — | ✅ |
| 426 | WkrPrflValueDPEOValue36 | VALUE36 | — | — |
| 427 | WkrPrflValueDPEOValue37 | VALUE37 | — | — |
| 428 | WkrPrflValueDPEOValue38 | VALUE38 | — | ✅ |
| 429 | WkrPrflValueDPEOValue39 | VALUE39 | — | ✅ |
| 430 | WkrPrflValueDPEOValue4 | VALUE4 | — | ✅ |
| 431 | WkrPrflValueDPEOValue40 | VALUE40 | — | ✅ |
| 432 | WkrPrflValueDPEOValue41 | VALUE41 | — | ✅ |
| 433 | WkrPrflValueDPEOValue42 | VALUE42 | — | ✅ |
| 434 | WkrPrflValueDPEOValue43 | VALUE43 | — | ✅ |
| 435 | WkrPrflValueDPEOValue44 | VALUE44 | — | ✅ |
| 436 | WkrPrflValueDPEOValue45 | VALUE45 | — | ✅ |
| 437 | WkrPrflValueDPEOValue46 | VALUE46 | — | ✅ |
| 438 | WkrPrflValueDPEOValue47 | VALUE47 | — | ✅ |
| 439 | WkrPrflValueDPEOValue48 | VALUE48 | — | — |
| 440 | WkrPrflValueDPEOValue49 | VALUE49 | — | — |
| 441 | WkrPrflValueDPEOValue5 | VALUE5 | — | ✅ |
| 442 | WkrPrflValueDPEOValue50 | VALUE50 | — | ✅ |
| 443 | WkrPrflValueDPEOValue51 | VALUE51 | — | ✅ |
| 444 | WkrPrflValueDPEOValue52 | VALUE52 | — | ✅ |
| 445 | WkrPrflValueDPEOValue53 | VALUE53 | — | ✅ |
| 446 | WkrPrflValueDPEOValue54 | VALUE54 | — | ✅ |
| 447 | WkrPrflValueDPEOValue55 | VALUE55 | — | ✅ |
| 448 | WkrPrflValueDPEOValue56 | VALUE56 | — | ✅ |
| 449 | WkrPrflValueDPEOValue57 | VALUE57 | — | ✅ |
| 450 | WkrPrflValueDPEOValue58 | VALUE58 | — | ✅ |
| 451 | WkrPrflValueDPEOValue59 | VALUE59 | — | ✅ |
| 452 | WkrPrflValueDPEOValue6 | VALUE6 | — | ✅ |
| 453 | WkrPrflValueDPEOValue60 | VALUE60 | — | — |
| 454 | WkrPrflValueDPEOValue61 | VALUE61 | — | — |
| 455 | WkrPrflValueDPEOValue62 | VALUE62 | — | ✅ |
| 456 | WkrPrflValueDPEOValue63 | VALUE63 | — | ✅ |
| 457 | WkrPrflValueDPEOValue64 | VALUE64 | — | ✅ |
| 458 | WkrPrflValueDPEOValue65 | VALUE65 | — | ✅ |
| 459 | WkrPrflValueDPEOValue66 | VALUE66 | — | ✅ |
| 460 | WkrPrflValueDPEOValue67 | VALUE67 | — | ✅ |
| 461 | WkrPrflValueDPEOValue68 | VALUE68 | — | ✅ |
| 462 | WkrPrflValueDPEOValue69 | VALUE69 | — | ✅ |
| 463 | WkrPrflValueDPEOValue7 | VALUE7 | — | ✅ |
| 464 | WkrPrflValueDPEOValue70 | VALUE70 | — | — |
| 465 | WkrPrflValueDPEOValue71 | VALUE71 | — | — |
| 466 | WkrPrflValueDPEOValue72 | VALUE72 | — | — |
| 467 | WkrPrflValueDPEOValue73 | VALUE73 | — | — |
| 468 | WkrPrflValueDPEOValue74 | VALUE74 | — | — |
| 469 | WkrPrflValueDPEOValue75 | VALUE75 | — | — |
| 470 | WkrPrflValueDPEOValue76 | VALUE76 | — | — |
| 471 | WkrPrflValueDPEOValue77 | VALUE77 | — | — |
| 472 | WkrPrflValueDPEOValue78 | VALUE78 | — | — |
| 473 | WkrPrflValueDPEOValue79 | VALUE79 | — | — |
| 474 | WkrPrflValueDPEOValue8 | VALUE8 | — | ✅ |
| 475 | WkrPrflValueDPEOValue9 | VALUE9 | — | — |

### [[hxt_setup_profiles_b|HXT_SETUP_PROFILES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetupProfileBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | SetupProfileBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | SetupProfileBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | SetupProfileBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SetupProfileBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | SetupProfileBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | SetupProfileBPEOModuleId | MODULE_ID | — | — |
| 8 | SetupProfileBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SetupProfileBPEOPrecedence | PRECEDENCE | — | ✅ |
| 10 | SetupProfileBPEOProductArea | PRODUCT_AREA | — | ✅ |
| 11 | SetupProfileBPEOSetupProfileCd | SETUP_PROFILE_CD | — | ✅ |
| 12 | SetupProfileBPEOSetupProfileId | SETUP_PROFILE_ID | 🔑 | ✅ |

### [[hxt_setup_profiles_tl|HXT_SETUP_PROFILES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetupProfileTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | SetupProfileTLPEOLanguage | LANGUAGE | — | — |
| 3 | SetupProfileTLPEOName | NAME | — | ✅ |
| 4 | SetupProfileTLPEOSetupProfileId | SETUP_PROFILE_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MgrDetailsPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MgrDetailsPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MgrDetailsPEOPersonId | PERSON_ID | — | — |
| 4 | MgrDetailsPEOPersonNumber | PERSON_NUMBER | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MgrNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MgrNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MgrNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | MgrNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
