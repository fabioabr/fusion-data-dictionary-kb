---
id: DOC-OTHER-PVO-OrgTreeBICVO
doc_type: system-doc
title: "OrgTreeBICVO — PVO Cross-Module"
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
  - OrgTreeBICVO
  - orgtreebicvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrgTreeBICVO

## 📌 Visão Geral

View Object para extração BICC de dados de Org Tree BICVO. Acessa as tabelas: FND_TREE_VERSION_VL, FND_TREE_VL, PER_ORG_TREE_NODE_CF.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrgTreeBICVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 269 | 3 | 5 | 14 | 5% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_tree_version_vl|FND_TREE_VERSION_VL]] — 23 atributos (5 BICC)
- [[fnd_tree_vl|FND_TREE_VL]] — 11 atributos (3 BICC)
- [[per_org_tree_node_cf|PER_ORG_TREE_NODE_CF]] — 235 atributos (5 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[fnd_tree_version_vl|FND_TREE_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndTreeVersionEffDateEOChangedSinceValidation | CHANGED_SINCE_VALIDATION | — | — |
| 2 | FndTreeVersionEffDateEOCreatedBy | CREATED_BY | — | — |
| 3 | FndTreeVersionEffDateEOCreationDate | CREATION_DATE | — | — |
| 4 | FndTreeVersionEffDateEODescription | DESCRIPTION | — | — |
| 5 | FndTreeVersionEffDateEOEffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | FndTreeVersionEffDateEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | FndTreeVersionEffDateEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | FndTreeVersionEffDateEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | FndTreeVersionEffDateEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | FndTreeVersionEffDateEOLastValidationDate | LAST_VALIDATION_DATE | — | — |
| 11 | FndTreeVersionEffDateEOLastValidationResult | LAST_VALIDATION_RESULT | — | — |
| 12 | FndTreeVersionEffDateEOLastValidationResultId | LAST_VALIDATION_RESULT_ID | — | — |
| 13 | FndTreeVersionEffDateEOLevelCount | LEVEL_COUNT | — | — |
| 14 | FndTreeVersionEffDateEOLockDate | LOCK_DATE | — | — |
| 15 | FndTreeVersionEffDateEOLockedBy | LOCKED_BY | — | — |
| 16 | FndTreeVersionEffDateEONodeCount | NODE_COUNT | — | — |
| 17 | FndTreeVersionEffDateEOSourceTreeVersionId | SOURCE_TREE_VERSION_ID | — | — |
| 18 | FndTreeVersionEffDateEOStatus | STATUS | — | ✅ |
| 19 | FndTreeVersionEffDateEOTreeCode | TREE_CODE | — | — |
| 20 | FndTreeVersionEffDateEOTreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 21 | FndTreeVersionEffDateEOTreeVersionId | TREE_VERSION_ID | — | — |
| 22 | FndTreeVersionEffDateEOTreeVersionName | TREE_VERSION_NAME | — | ✅ |
| 23 | FndTreeVersionEffDateEOVersionComment | VERSION_COMMENT | — | — |

### [[fnd_tree_vl|FND_TREE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndTreeEOCreatedBy | CREATED_BY | — | — |
| 2 | FndTreeEOCreationDate | CREATION_DATE | — | — |
| 3 | FndTreeEODescription | DESCRIPTION | — | — |
| 4 | FndTreeEOIconName | ICON_NAME | — | — |
| 5 | FndTreeEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | FndTreeEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | FndTreeEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | FndTreeEOSetId | SET_ID | — | — |
| 9 | FndTreeEOTreeCode | TREE_CODE | — | ✅ |
| 10 | FndTreeEOTreeName | TREE_NAME | — | ✅ |
| 11 | FndTreeEOTreeStructureCode | TREE_STRUCTURE_CODE | — | — |

### [[per_org_tree_node_cf|PER_ORG_TREE_NODE_CF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CfTreeNodeId | CF_TREE_NODE_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | Dep0DataSourceId | DEP0_DATA_SOURCE_ID | — | — |
| 5 | Dep0Pk1Value | DEP0_PK1_VALUE | — | — |
| 6 | Dep0Pk2Value | DEP0_PK2_VALUE | — | — |
| 7 | Dep0Pk3Value | DEP0_PK3_VALUE | — | — |
| 8 | Dep0Pk4Value | DEP0_PK4_VALUE | — | — |
| 9 | Dep0Pk5Value | DEP0_PK5_VALUE | — | — |
| 10 | Dep0TreeNodeId | DEP0_TREE_NODE_ID | — | — |
| 11 | Dep10DataSourceId | DEP10_DATA_SOURCE_ID | — | — |
| 12 | Dep10Pk1Value | DEP10_PK1_VALUE | — | — |
| 13 | Dep10Pk2Value | DEP10_PK2_VALUE | — | — |
| 14 | Dep10Pk3Value | DEP10_PK3_VALUE | — | — |
| 15 | Dep10Pk4Value | DEP10_PK4_VALUE | — | — |
| 16 | Dep10Pk5Value | DEP10_PK5_VALUE | — | — |
| 17 | Dep10TreeNodeId | DEP10_TREE_NODE_ID | — | — |
| 18 | Dep11DataSourceId | DEP11_DATA_SOURCE_ID | — | — |
| 19 | Dep11Pk1Value | DEP11_PK1_VALUE | — | — |
| 20 | Dep11Pk2Value | DEP11_PK2_VALUE | — | — |
| 21 | Dep11Pk3Value | DEP11_PK3_VALUE | — | — |
| 22 | Dep11Pk4Value | DEP11_PK4_VALUE | — | — |
| 23 | Dep11Pk5Value | DEP11_PK5_VALUE | — | — |
| 24 | Dep11TreeNodeId | DEP11_TREE_NODE_ID | — | — |
| 25 | Dep12DataSourceId | DEP12_DATA_SOURCE_ID | — | — |
| 26 | Dep12Pk1Value | DEP12_PK1_VALUE | — | — |
| 27 | Dep12Pk2Value | DEP12_PK2_VALUE | — | — |
| 28 | Dep12Pk3Value | DEP12_PK3_VALUE | — | — |
| 29 | Dep12Pk4Value | DEP12_PK4_VALUE | — | — |
| 30 | Dep12Pk5Value | DEP12_PK5_VALUE | — | — |
| 31 | Dep12TreeNodeId | DEP12_TREE_NODE_ID | — | — |
| 32 | Dep13DataSourceId | DEP13_DATA_SOURCE_ID | — | — |
| 33 | Dep13Pk1Value | DEP13_PK1_VALUE | — | — |
| 34 | Dep13Pk2Value | DEP13_PK2_VALUE | — | — |
| 35 | Dep13Pk3Value | DEP13_PK3_VALUE | — | — |
| 36 | Dep13Pk4Value | DEP13_PK4_VALUE | — | — |
| 37 | Dep13Pk5Value | DEP13_PK5_VALUE | — | — |
| 38 | Dep13TreeNodeId | DEP13_TREE_NODE_ID | — | — |
| 39 | Dep14DataSourceId | DEP14_DATA_SOURCE_ID | — | — |
| 40 | Dep14Pk1Value | DEP14_PK1_VALUE | — | — |
| 41 | Dep14Pk2Value | DEP14_PK2_VALUE | — | — |
| 42 | Dep14Pk3Value | DEP14_PK3_VALUE | — | — |
| 43 | Dep14Pk4Value | DEP14_PK4_VALUE | — | — |
| 44 | Dep14Pk5Value | DEP14_PK5_VALUE | — | — |
| 45 | Dep14TreeNodeId | DEP14_TREE_NODE_ID | — | — |
| 46 | Dep15DataSourceId | DEP15_DATA_SOURCE_ID | — | — |
| 47 | Dep15Pk1Value | DEP15_PK1_VALUE | — | — |
| 48 | Dep15Pk2Value | DEP15_PK2_VALUE | — | — |
| 49 | Dep15Pk3Value | DEP15_PK3_VALUE | — | — |
| 50 | Dep15Pk4Value | DEP15_PK4_VALUE | — | — |
| 51 | Dep15Pk5Value | DEP15_PK5_VALUE | — | — |
| 52 | Dep15TreeNodeId | DEP15_TREE_NODE_ID | — | — |
| 53 | Dep16DataSourceId | DEP16_DATA_SOURCE_ID | — | — |
| 54 | Dep16Pk1Value | DEP16_PK1_VALUE | — | — |
| 55 | Dep16Pk2Value | DEP16_PK2_VALUE | — | — |
| 56 | Dep16Pk3Value | DEP16_PK3_VALUE | — | — |
| 57 | Dep16Pk4Value | DEP16_PK4_VALUE | — | — |
| 58 | Dep16Pk5Value | DEP16_PK5_VALUE | — | — |
| 59 | Dep16TreeNodeId | DEP16_TREE_NODE_ID | — | — |
| 60 | Dep17DataSourceId | DEP17_DATA_SOURCE_ID | — | — |
| 61 | Dep17Pk1Value | DEP17_PK1_VALUE | — | — |
| 62 | Dep17Pk2Value | DEP17_PK2_VALUE | — | — |
| 63 | Dep17Pk3Value | DEP17_PK3_VALUE | — | — |
| 64 | Dep17Pk4Value | DEP17_PK4_VALUE | — | — |
| 65 | Dep17Pk5Value | DEP17_PK5_VALUE | — | — |
| 66 | Dep17TreeNodeId | DEP17_TREE_NODE_ID | — | — |
| 67 | Dep18DataSourceId | DEP18_DATA_SOURCE_ID | — | — |
| 68 | Dep18Pk1Value | DEP18_PK1_VALUE | — | — |
| 69 | Dep18Pk2Value | DEP18_PK2_VALUE | — | — |
| 70 | Dep18Pk3Value | DEP18_PK3_VALUE | — | — |
| 71 | Dep18Pk4Value | DEP18_PK4_VALUE | — | — |
| 72 | Dep18Pk5Value | DEP18_PK5_VALUE | — | — |
| 73 | Dep18TreeNodeId | DEP18_TREE_NODE_ID | — | — |
| 74 | Dep19DataSourceId | DEP19_DATA_SOURCE_ID | — | — |
| 75 | Dep19Pk1Value | DEP19_PK1_VALUE | — | — |
| 76 | Dep19Pk2Value | DEP19_PK2_VALUE | — | — |
| 77 | Dep19Pk3Value | DEP19_PK3_VALUE | — | — |
| 78 | Dep19Pk4Value | DEP19_PK4_VALUE | — | — |
| 79 | Dep19Pk5Value | DEP19_PK5_VALUE | — | — |
| 80 | Dep19TreeNodeId | DEP19_TREE_NODE_ID | — | — |
| 81 | Dep1DataSourceId | DEP1_DATA_SOURCE_ID | — | — |
| 82 | Dep1Pk1Value | DEP1_PK1_VALUE | — | — |
| 83 | Dep1Pk2Value | DEP1_PK2_VALUE | — | — |
| 84 | Dep1Pk3Value | DEP1_PK3_VALUE | — | — |
| 85 | Dep1Pk4Value | DEP1_PK4_VALUE | — | — |
| 86 | Dep1Pk5Value | DEP1_PK5_VALUE | — | — |
| 87 | Dep1TreeNodeId | DEP1_TREE_NODE_ID | — | — |
| 88 | Dep20DataSourceId | DEP20_DATA_SOURCE_ID | — | — |
| 89 | Dep20Pk1Value | DEP20_PK1_VALUE | — | — |
| 90 | Dep20Pk2Value | DEP20_PK2_VALUE | — | — |
| 91 | Dep20Pk3Value | DEP20_PK3_VALUE | — | — |
| 92 | Dep20Pk4Value | DEP20_PK4_VALUE | — | — |
| 93 | Dep20Pk5Value | DEP20_PK5_VALUE | — | — |
| 94 | Dep20TreeNodeId | DEP20_TREE_NODE_ID | — | — |
| 95 | Dep21DataSourceId | DEP21_DATA_SOURCE_ID | — | — |
| 96 | Dep21Pk1Value | DEP21_PK1_VALUE | — | — |
| 97 | Dep21Pk2Value | DEP21_PK2_VALUE | — | — |
| 98 | Dep21Pk3Value | DEP21_PK3_VALUE | — | — |
| 99 | Dep21Pk4Value | DEP21_PK4_VALUE | — | — |
| 100 | Dep21Pk5Value | DEP21_PK5_VALUE | — | — |
| 101 | Dep21TreeNodeId | DEP21_TREE_NODE_ID | — | — |
| 102 | Dep22DataSourceId | DEP22_DATA_SOURCE_ID | — | — |
| 103 | Dep22Pk1Value | DEP22_PK1_VALUE | — | — |
| 104 | Dep22Pk2Value | DEP22_PK2_VALUE | — | — |
| 105 | Dep22Pk3Value | DEP22_PK3_VALUE | — | — |
| 106 | Dep22Pk4Value | DEP22_PK4_VALUE | — | — |
| 107 | Dep22Pk5Value | DEP22_PK5_VALUE | — | — |
| 108 | Dep22TreeNodeId | DEP22_TREE_NODE_ID | — | — |
| 109 | Dep23DataSourceId | DEP23_DATA_SOURCE_ID | — | — |
| 110 | Dep23Pk1Value | DEP23_PK1_VALUE | — | — |
| 111 | Dep23Pk2Value | DEP23_PK2_VALUE | — | — |
| 112 | Dep23Pk3Value | DEP23_PK3_VALUE | — | — |
| 113 | Dep23Pk4Value | DEP23_PK4_VALUE | — | — |
| 114 | Dep23Pk5Value | DEP23_PK5_VALUE | — | — |
| 115 | Dep23TreeNodeId | DEP23_TREE_NODE_ID | — | — |
| 116 | Dep24DataSourceId | DEP24_DATA_SOURCE_ID | — | — |
| 117 | Dep24Pk1Value | DEP24_PK1_VALUE | — | — |
| 118 | Dep24Pk2Value | DEP24_PK2_VALUE | — | — |
| 119 | Dep24Pk3Value | DEP24_PK3_VALUE | — | — |
| 120 | Dep24Pk4Value | DEP24_PK4_VALUE | — | — |
| 121 | Dep24Pk5Value | DEP24_PK5_VALUE | — | — |
| 122 | Dep24TreeNodeId | DEP24_TREE_NODE_ID | — | — |
| 123 | Dep25DataSourceId | DEP25_DATA_SOURCE_ID | — | — |
| 124 | Dep25Pk1Value | DEP25_PK1_VALUE | — | — |
| 125 | Dep25Pk2Value | DEP25_PK2_VALUE | — | — |
| 126 | Dep25Pk3Value | DEP25_PK3_VALUE | — | — |
| 127 | Dep25Pk4Value | DEP25_PK4_VALUE | — | — |
| 128 | Dep25Pk5Value | DEP25_PK5_VALUE | — | — |
| 129 | Dep25TreeNodeId | DEP25_TREE_NODE_ID | — | — |
| 130 | Dep26DataSourceId | DEP26_DATA_SOURCE_ID | — | — |
| 131 | Dep26Pk1Value | DEP26_PK1_VALUE | — | — |
| 132 | Dep26Pk2Value | DEP26_PK2_VALUE | — | — |
| 133 | Dep26Pk3Value | DEP26_PK3_VALUE | — | — |
| 134 | Dep26Pk4Value | DEP26_PK4_VALUE | — | — |
| 135 | Dep26Pk5Value | DEP26_PK5_VALUE | — | — |
| 136 | Dep26TreeNodeId | DEP26_TREE_NODE_ID | — | — |
| 137 | Dep27DataSourceId | DEP27_DATA_SOURCE_ID | — | — |
| 138 | Dep27Pk1Value | DEP27_PK1_VALUE | — | — |
| 139 | Dep27Pk2Value | DEP27_PK2_VALUE | — | — |
| 140 | Dep27Pk3Value | DEP27_PK3_VALUE | — | — |
| 141 | Dep27Pk4Value | DEP27_PK4_VALUE | — | — |
| 142 | Dep27Pk5Value | DEP27_PK5_VALUE | — | — |
| 143 | Dep27TreeNodeId | DEP27_TREE_NODE_ID | — | — |
| 144 | Dep28DataSourceId | DEP28_DATA_SOURCE_ID | — | — |
| 145 | Dep28Pk1Value | DEP28_PK1_VALUE | — | — |
| 146 | Dep28Pk2Value | DEP28_PK2_VALUE | — | — |
| 147 | Dep28Pk3Value | DEP28_PK3_VALUE | — | — |
| 148 | Dep28Pk4Value | DEP28_PK4_VALUE | — | — |
| 149 | Dep28Pk5Value | DEP28_PK5_VALUE | — | — |
| 150 | Dep28TreeNodeId | DEP28_TREE_NODE_ID | — | — |
| 151 | Dep29DataSourceId | DEP29_DATA_SOURCE_ID | — | — |
| 152 | Dep29Pk1Value | DEP29_PK1_VALUE | — | — |
| 153 | Dep29Pk2Value | DEP29_PK2_VALUE | — | — |
| 154 | Dep29Pk3Value | DEP29_PK3_VALUE | — | — |
| 155 | Dep29Pk4Value | DEP29_PK4_VALUE | — | — |
| 156 | Dep29Pk5Value | DEP29_PK5_VALUE | — | — |
| 157 | Dep29TreeNodeId | DEP29_TREE_NODE_ID | — | — |
| 158 | Dep2DataSourceId | DEP2_DATA_SOURCE_ID | — | — |
| 159 | Dep2Pk1Value | DEP2_PK1_VALUE | — | — |
| 160 | Dep2Pk2Value | DEP2_PK2_VALUE | — | — |
| 161 | Dep2Pk3Value | DEP2_PK3_VALUE | — | — |
| 162 | Dep2Pk4Value | DEP2_PK4_VALUE | — | — |
| 163 | Dep2Pk5Value | DEP2_PK5_VALUE | — | — |
| 164 | Dep2TreeNodeId | DEP2_TREE_NODE_ID | — | — |
| 165 | Dep30DataSourceId | DEP30_DATA_SOURCE_ID | — | — |
| 166 | Dep30Pk1Value | DEP30_PK1_VALUE | — | — |
| 167 | Dep30Pk2Value | DEP30_PK2_VALUE | — | — |
| 168 | Dep30Pk3Value | DEP30_PK3_VALUE | — | — |
| 169 | Dep30Pk4Value | DEP30_PK4_VALUE | — | — |
| 170 | Dep30Pk5Value | DEP30_PK5_VALUE | — | — |
| 171 | Dep30TreeNodeId | DEP30_TREE_NODE_ID | — | — |
| 172 | Dep31DataSourceId | DEP31_DATA_SOURCE_ID | — | — |
| 173 | Dep31Pk1Value | DEP31_PK1_VALUE | — | — |
| 174 | Dep31Pk2Value | DEP31_PK2_VALUE | — | — |
| 175 | Dep31Pk3Value | DEP31_PK3_VALUE | — | — |
| 176 | Dep31Pk4Value | DEP31_PK4_VALUE | — | — |
| 177 | Dep31Pk5Value | DEP31_PK5_VALUE | — | — |
| 178 | Dep31TreeNodeId | DEP31_TREE_NODE_ID | — | — |
| 179 | Dep3DataSourceId | DEP3_DATA_SOURCE_ID | — | — |
| 180 | Dep3Pk1Value | DEP3_PK1_VALUE | — | — |
| 181 | Dep3Pk2Value | DEP3_PK2_VALUE | — | — |
| 182 | Dep3Pk3Value | DEP3_PK3_VALUE | — | — |
| 183 | Dep3Pk4Value | DEP3_PK4_VALUE | — | — |
| 184 | Dep3Pk5Value | DEP3_PK5_VALUE | — | — |
| 185 | Dep3TreeNodeId | DEP3_TREE_NODE_ID | — | — |
| 186 | Dep4DataSourceId | DEP4_DATA_SOURCE_ID | — | — |
| 187 | Dep4Pk1Value | DEP4_PK1_VALUE | — | — |
| 188 | Dep4Pk2Value | DEP4_PK2_VALUE | — | — |
| 189 | Dep4Pk3Value | DEP4_PK3_VALUE | — | — |
| 190 | Dep4Pk4Value | DEP4_PK4_VALUE | — | — |
| 191 | Dep4Pk5Value | DEP4_PK5_VALUE | — | — |
| 192 | Dep4TreeNodeId | DEP4_TREE_NODE_ID | — | — |
| 193 | Dep5DataSourceId | DEP5_DATA_SOURCE_ID | — | — |
| 194 | Dep5Pk1Value | DEP5_PK1_VALUE | — | — |
| 195 | Dep5Pk2Value | DEP5_PK2_VALUE | — | — |
| 196 | Dep5Pk3Value | DEP5_PK3_VALUE | — | — |
| 197 | Dep5Pk4Value | DEP5_PK4_VALUE | — | — |
| 198 | Dep5Pk5Value | DEP5_PK5_VALUE | — | — |
| 199 | Dep5TreeNodeId | DEP5_TREE_NODE_ID | — | — |
| 200 | Dep6DataSourceId | DEP6_DATA_SOURCE_ID | — | — |
| 201 | Dep6Pk1Value | DEP6_PK1_VALUE | — | — |
| 202 | Dep6Pk2Value | DEP6_PK2_VALUE | — | — |
| 203 | Dep6Pk3Value | DEP6_PK3_VALUE | — | — |
| 204 | Dep6Pk4Value | DEP6_PK4_VALUE | — | — |
| 205 | Dep6Pk5Value | DEP6_PK5_VALUE | — | — |
| 206 | Dep6TreeNodeId | DEP6_TREE_NODE_ID | — | — |
| 207 | Dep7DataSourceId | DEP7_DATA_SOURCE_ID | — | — |
| 208 | Dep7Pk1Value | DEP7_PK1_VALUE | — | — |
| 209 | Dep7Pk2Value | DEP7_PK2_VALUE | — | — |
| 210 | Dep7Pk3Value | DEP7_PK3_VALUE | — | — |
| 211 | Dep7Pk4Value | DEP7_PK4_VALUE | — | — |
| 212 | Dep7Pk5Value | DEP7_PK5_VALUE | — | — |
| 213 | Dep7TreeNodeId | DEP7_TREE_NODE_ID | — | — |
| 214 | Dep8DataSourceId | DEP8_DATA_SOURCE_ID | — | — |
| 215 | Dep8Pk1Value | DEP8_PK1_VALUE | — | — |
| 216 | Dep8Pk2Value | DEP8_PK2_VALUE | — | — |
| 217 | Dep8Pk3Value | DEP8_PK3_VALUE | — | — |
| 218 | Dep8Pk4Value | DEP8_PK4_VALUE | — | — |
| 219 | Dep8Pk5Value | DEP8_PK5_VALUE | — | — |
| 220 | Dep8TreeNodeId | DEP8_TREE_NODE_ID | — | — |
| 221 | Dep9DataSourceId | DEP9_DATA_SOURCE_ID | — | — |
| 222 | Dep9Pk1Value | DEP9_PK1_VALUE | — | — |
| 223 | Dep9Pk2Value | DEP9_PK2_VALUE | — | — |
| 224 | Dep9Pk3Value | DEP9_PK3_VALUE | — | — |
| 225 | Dep9Pk4Value | DEP9_PK4_VALUE | — | — |
| 226 | Dep9Pk5Value | DEP9_PK5_VALUE | — | — |
| 227 | Dep9TreeNodeId | DEP9_TREE_NODE_ID | — | — |
| 228 | Distance | DISTANCE | — | — |
| 229 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 230 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 231 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 232 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 233 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 234 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 235 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
