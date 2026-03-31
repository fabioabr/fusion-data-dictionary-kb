---
id: DOC-OTHER-PVO-DirectCreditRuleHierarchyCF
doc_type: system-doc
title: "DirectCreditRuleHierarchyCF — PVO Cross-Module"
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
  - DirectCreditRuleHierarchyCF
  - directcreditrulehierarchycf
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DirectCreditRuleHierarchyCF

## 📌 Visão Geral

View Object para extração BICC de dados de Direct Credit Rule Hierarchy CF. Acessa as tabelas: CN_RS_DENORM_RULES_ALL, CN_RS_RULES_ALL_B, CN_RS_RULES_ALL_TL (+2).

**Caminho:** `FscmTopModelAM.RuleAM.DirectCreditRuleHierarchyCF`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 306 | 5 | 4 | 267 | 87% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rs_denorm_rules_all|CN_RS_DENORM_RULES_ALL]] — 4 atributos (1 BICC)
- [[cn_rs_rules_all_b|CN_RS_RULES_ALL_B]] — 199 atributos (199 BICC)
- [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]] — 72 atributos (36 BICC)
- [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]] — 26 atributos (1 PKs, 26 BICC)
- [[cn_rs_usages_all_tl|CN_RS_USAGES_ALL_TL]] — 5 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[cn_rs_denorm_rules_all|CN_RS_DENORM_RULES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleHierPEOLevelFromParent | LEVEL_FROM_PARENT | — | — |
| 2 | RuleHierPEOLevelFromRoot | LEVEL_FROM_ROOT | — | ✅ |
| 3 | RuleHierPEORelatedRuleId | RELATED_RULE_ID | — | — |
| 4 | RuleHierPEORuleId | RULE_ID | — | — |

### [[cn_rs_rules_all_b|CN_RS_RULES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseParentRuleCreatedBy | CREATED_BY | — | ✅ |
| 2 | BaseParentRuleCreationDate | CREATION_DATE | — | ✅ |
| 3 | BaseParentRuleEnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | BaseParentRuleEndDate | END_DATE | — | ✅ |
| 5 | BaseParentRuleId | RULE_ID | — | ✅ |
| 6 | BaseParentRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BaseParentRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | BaseParentRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | BaseParentRuleNumWinners | NUM_WINNERS | — | ✅ |
| 10 | BaseParentRuleNumber | RULE_NUMBER | — | ✅ |
| 11 | BaseParentRuleRank | RANK | — | ✅ |
| 12 | BaseParentRuleStartDate | START_DATE | — | ✅ |
| 13 | BaseRuleCreatedBy | CREATED_BY | — | ✅ |
| 14 | BaseRuleCreationDate | CREATION_DATE | — | ✅ |
| 15 | BaseRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | BaseRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | BaseRuleNumber | RULE_NUMBER | — | ✅ |
| 18 | CreatedBy1 | CREATED_BY | — | ✅ |
| 19 | CreatedBy10 | CREATED_BY | — | ✅ |
| 20 | CreatedBy11 | CREATED_BY | — | ✅ |
| 21 | CreatedBy12 | CREATED_BY | — | ✅ |
| 22 | CreatedBy13 | CREATED_BY | — | ✅ |
| 23 | CreatedBy14 | CREATED_BY | — | ✅ |
| 24 | CreatedBy15 | CREATED_BY | — | ✅ |
| 25 | CreatedBy16 | CREATED_BY | — | ✅ |
| 26 | CreatedBy2 | CREATED_BY | — | ✅ |
| 27 | CreatedBy3 | CREATED_BY | — | ✅ |
| 28 | CreatedBy4 | CREATED_BY | — | ✅ |
| 29 | CreatedBy5 | CREATED_BY | — | ✅ |
| 30 | CreatedBy6 | CREATED_BY | — | ✅ |
| 31 | CreatedBy7 | CREATED_BY | — | ✅ |
| 32 | CreatedBy8 | CREATED_BY | — | ✅ |
| 33 | CreatedBy9 | CREATED_BY | — | ✅ |
| 34 | CreationDate1 | CREATION_DATE | — | ✅ |
| 35 | CreationDate10 | CREATION_DATE | — | ✅ |
| 36 | CreationDate11 | CREATION_DATE | — | ✅ |
| 37 | CreationDate12 | CREATION_DATE | — | ✅ |
| 38 | CreationDate13 | CREATION_DATE | — | ✅ |
| 39 | CreationDate14 | CREATION_DATE | — | ✅ |
| 40 | CreationDate15 | CREATION_DATE | — | ✅ |
| 41 | CreationDate16 | CREATION_DATE | — | ✅ |
| 42 | CreationDate2 | CREATION_DATE | — | ✅ |
| 43 | CreationDate3 | CREATION_DATE | — | ✅ |
| 44 | CreationDate4 | CREATION_DATE | — | ✅ |
| 45 | CreationDate5 | CREATION_DATE | — | ✅ |
| 46 | CreationDate6 | CREATION_DATE | — | ✅ |
| 47 | CreationDate7 | CREATION_DATE | — | ✅ |
| 48 | CreationDate8 | CREATION_DATE | — | ✅ |
| 49 | CreationDate9 | CREATION_DATE | — | ✅ |
| 50 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 51 | EnabledFlag1 | ENABLED_FLAG | — | ✅ |
| 52 | EnabledFlag10 | ENABLED_FLAG | — | ✅ |
| 53 | EnabledFlag11 | ENABLED_FLAG | — | ✅ |
| 54 | EnabledFlag12 | ENABLED_FLAG | — | ✅ |
| 55 | EnabledFlag13 | ENABLED_FLAG | — | ✅ |
| 56 | EnabledFlag14 | ENABLED_FLAG | — | ✅ |
| 57 | EnabledFlag15 | ENABLED_FLAG | — | ✅ |
| 58 | EnabledFlag16 | ENABLED_FLAG | — | ✅ |
| 59 | EnabledFlag2 | ENABLED_FLAG | — | ✅ |
| 60 | EnabledFlag3 | ENABLED_FLAG | — | ✅ |
| 61 | EnabledFlag4 | ENABLED_FLAG | — | ✅ |
| 62 | EnabledFlag5 | ENABLED_FLAG | — | ✅ |
| 63 | EnabledFlag6 | ENABLED_FLAG | — | ✅ |
| 64 | EnabledFlag7 | ENABLED_FLAG | — | ✅ |
| 65 | EnabledFlag8 | ENABLED_FLAG | — | ✅ |
| 66 | EnabledFlag9 | ENABLED_FLAG | — | ✅ |
| 67 | EndDate | END_DATE | — | ✅ |
| 68 | EndDate1 | END_DATE | — | ✅ |
| 69 | EndDate10 | END_DATE | — | ✅ |
| 70 | EndDate11 | END_DATE | — | ✅ |
| 71 | EndDate12 | END_DATE | — | ✅ |
| 72 | EndDate13 | END_DATE | — | ✅ |
| 73 | EndDate14 | END_DATE | — | ✅ |
| 74 | EndDate15 | END_DATE | — | ✅ |
| 75 | EndDate16 | END_DATE | — | ✅ |
| 76 | EndDate2 | END_DATE | — | ✅ |
| 77 | EndDate3 | END_DATE | — | ✅ |
| 78 | EndDate4 | END_DATE | — | ✅ |
| 79 | EndDate5 | END_DATE | — | ✅ |
| 80 | EndDate6 | END_DATE | — | ✅ |
| 81 | EndDate7 | END_DATE | — | ✅ |
| 82 | EndDate8 | END_DATE | — | ✅ |
| 83 | EndDate9 | END_DATE | — | ✅ |
| 84 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 85 | LastUpdateDate10 | LAST_UPDATE_DATE | — | ✅ |
| 86 | LastUpdateDate11 | LAST_UPDATE_DATE | — | ✅ |
| 87 | LastUpdateDate12 | LAST_UPDATE_DATE | — | ✅ |
| 88 | LastUpdateDate13 | LAST_UPDATE_DATE | — | ✅ |
| 89 | LastUpdateDate14 | LAST_UPDATE_DATE | — | ✅ |
| 90 | LastUpdateDate15 | LAST_UPDATE_DATE | — | ✅ |
| 91 | LastUpdateDate16 | LAST_UPDATE_DATE | — | ✅ |
| 92 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 93 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 94 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 95 | LastUpdateDate5 | LAST_UPDATE_DATE | — | ✅ |
| 96 | LastUpdateDate6 | LAST_UPDATE_DATE | — | ✅ |
| 97 | LastUpdateDate7 | LAST_UPDATE_DATE | — | ✅ |
| 98 | LastUpdateDate8 | LAST_UPDATE_DATE | — | ✅ |
| 99 | LastUpdateDate9 | LAST_UPDATE_DATE | — | ✅ |
| 100 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 101 | LastUpdatedBy10 | LAST_UPDATED_BY | — | ✅ |
| 102 | LastUpdatedBy11 | LAST_UPDATED_BY | — | ✅ |
| 103 | LastUpdatedBy12 | LAST_UPDATED_BY | — | ✅ |
| 104 | LastUpdatedBy13 | LAST_UPDATED_BY | — | ✅ |
| 105 | LastUpdatedBy14 | LAST_UPDATED_BY | — | ✅ |
| 106 | LastUpdatedBy15 | LAST_UPDATED_BY | — | ✅ |
| 107 | LastUpdatedBy16 | LAST_UPDATED_BY | — | ✅ |
| 108 | LastUpdatedBy2 | LAST_UPDATED_BY | — | ✅ |
| 109 | LastUpdatedBy3 | LAST_UPDATED_BY | — | ✅ |
| 110 | LastUpdatedBy4 | LAST_UPDATED_BY | — | ✅ |
| 111 | LastUpdatedBy5 | LAST_UPDATED_BY | — | ✅ |
| 112 | LastUpdatedBy6 | LAST_UPDATED_BY | — | ✅ |
| 113 | LastUpdatedBy7 | LAST_UPDATED_BY | — | ✅ |
| 114 | LastUpdatedBy8 | LAST_UPDATED_BY | — | ✅ |
| 115 | LastUpdatedBy9 | LAST_UPDATED_BY | — | ✅ |
| 116 | NumWinners | NUM_WINNERS | — | ✅ |
| 117 | NumWinners1 | NUM_WINNERS | — | ✅ |
| 118 | NumWinners10 | NUM_WINNERS | — | ✅ |
| 119 | NumWinners11 | NUM_WINNERS | — | ✅ |
| 120 | NumWinners12 | NUM_WINNERS | — | ✅ |
| 121 | NumWinners13 | NUM_WINNERS | — | ✅ |
| 122 | NumWinners14 | NUM_WINNERS | — | ✅ |
| 123 | NumWinners15 | NUM_WINNERS | — | ✅ |
| 124 | NumWinners16 | NUM_WINNERS | — | ✅ |
| 125 | NumWinners2 | NUM_WINNERS | — | ✅ |
| 126 | NumWinners3 | NUM_WINNERS | — | ✅ |
| 127 | NumWinners4 | NUM_WINNERS | — | ✅ |
| 128 | NumWinners5 | NUM_WINNERS | — | ✅ |
| 129 | NumWinners6 | NUM_WINNERS | — | ✅ |
| 130 | NumWinners7 | NUM_WINNERS | — | ✅ |
| 131 | NumWinners8 | NUM_WINNERS | — | ✅ |
| 132 | NumWinners9 | NUM_WINNERS | — | ✅ |
| 133 | Rank | RANK | — | ✅ |
| 134 | Rank1 | RANK | — | ✅ |
| 135 | Rank10 | RANK | — | ✅ |
| 136 | Rank11 | RANK | — | ✅ |
| 137 | Rank12 | RANK | — | ✅ |
| 138 | Rank13 | RANK | — | ✅ |
| 139 | Rank14 | RANK | — | ✅ |
| 140 | Rank15 | RANK | — | ✅ |
| 141 | Rank16 | RANK | — | ✅ |
| 142 | Rank2 | RANK | — | ✅ |
| 143 | Rank3 | RANK | — | ✅ |
| 144 | Rank4 | RANK | — | ✅ |
| 145 | Rank5 | RANK | — | ✅ |
| 146 | Rank6 | RANK | — | ✅ |
| 147 | Rank7 | RANK | — | ✅ |
| 148 | Rank8 | RANK | — | ✅ |
| 149 | Rank9 | RANK | — | ✅ |
| 150 | RuleId | RULE_ID | — | ✅ |
| 151 | RuleId1 | RULE_ID | — | ✅ |
| 152 | RuleId10 | RULE_ID | — | ✅ |
| 153 | RuleId11 | RULE_ID | — | ✅ |
| 154 | RuleId12 | RULE_ID | — | ✅ |
| 155 | RuleId13 | RULE_ID | — | ✅ |
| 156 | RuleId14 | RULE_ID | — | ✅ |
| 157 | RuleId15 | RULE_ID | — | ✅ |
| 158 | RuleId16 | RULE_ID | — | ✅ |
| 159 | RuleId2 | RULE_ID | — | ✅ |
| 160 | RuleId3 | RULE_ID | — | ✅ |
| 161 | RuleId4 | RULE_ID | — | ✅ |
| 162 | RuleId5 | RULE_ID | — | ✅ |
| 163 | RuleId6 | RULE_ID | — | ✅ |
| 164 | RuleId7 | RULE_ID | — | ✅ |
| 165 | RuleId8 | RULE_ID | — | ✅ |
| 166 | RuleId9 | RULE_ID | — | ✅ |
| 167 | RuleNumber1 | RULE_NUMBER | — | ✅ |
| 168 | RuleNumber10 | RULE_NUMBER | — | ✅ |
| 169 | RuleNumber11 | RULE_NUMBER | — | ✅ |
| 170 | RuleNumber12 | RULE_NUMBER | — | ✅ |
| 171 | RuleNumber13 | RULE_NUMBER | — | ✅ |
| 172 | RuleNumber14 | RULE_NUMBER | — | ✅ |
| 173 | RuleNumber15 | RULE_NUMBER | — | ✅ |
| 174 | RuleNumber16 | RULE_NUMBER | — | ✅ |
| 175 | RuleNumber2 | RULE_NUMBER | — | ✅ |
| 176 | RuleNumber3 | RULE_NUMBER | — | ✅ |
| 177 | RuleNumber4 | RULE_NUMBER | — | ✅ |
| 178 | RuleNumber5 | RULE_NUMBER | — | ✅ |
| 179 | RuleNumber6 | RULE_NUMBER | — | ✅ |
| 180 | RuleNumber7 | RULE_NUMBER | — | ✅ |
| 181 | RuleNumber8 | RULE_NUMBER | — | ✅ |
| 182 | RuleNumber9 | RULE_NUMBER | — | ✅ |
| 183 | StartDate | START_DATE | — | ✅ |
| 184 | StartDate1 | START_DATE | — | ✅ |
| 185 | StartDate10 | START_DATE | — | ✅ |
| 186 | StartDate11 | START_DATE | — | ✅ |
| 187 | StartDate12 | START_DATE | — | ✅ |
| 188 | StartDate13 | START_DATE | — | ✅ |
| 189 | StartDate14 | START_DATE | — | ✅ |
| 190 | StartDate15 | START_DATE | — | ✅ |
| 191 | StartDate16 | START_DATE | — | ✅ |
| 192 | StartDate2 | START_DATE | — | ✅ |
| 193 | StartDate3 | START_DATE | — | ✅ |
| 194 | StartDate4 | START_DATE | — | ✅ |
| 195 | StartDate5 | START_DATE | — | ✅ |
| 196 | StartDate6 | START_DATE | — | ✅ |
| 197 | StartDate7 | START_DATE | — | ✅ |
| 198 | StartDate8 | START_DATE | — | ✅ |
| 199 | StartDate9 | START_DATE | — | ✅ |

### [[cn_rs_rules_all_tl|CN_RS_RULES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Description1 | DESCRIPTION | — | ✅ |
| 3 | Description10 | DESCRIPTION | — | ✅ |
| 4 | Description11 | DESCRIPTION | — | ✅ |
| 5 | Description12 | DESCRIPTION | — | ✅ |
| 6 | Description13 | DESCRIPTION | — | ✅ |
| 7 | Description14 | DESCRIPTION | — | ✅ |
| 8 | Description15 | DESCRIPTION | — | ✅ |
| 9 | Description16 | DESCRIPTION | — | ✅ |
| 10 | Description2 | DESCRIPTION | — | ✅ |
| 11 | Description3 | DESCRIPTION | — | ✅ |
| 12 | Description4 | DESCRIPTION | — | ✅ |
| 13 | Description5 | DESCRIPTION | — | ✅ |
| 14 | Description6 | DESCRIPTION | — | ✅ |
| 15 | Description7 | DESCRIPTION | — | ✅ |
| 16 | Description8 | DESCRIPTION | — | ✅ |
| 17 | Description9 | DESCRIPTION | — | ✅ |
| 18 | Language1 | LANGUAGE | — | — |
| 19 | Language10 | LANGUAGE | — | — |
| 20 | Language11 | LANGUAGE | — | — |
| 21 | Language12 | LANGUAGE | — | — |
| 22 | Language13 | LANGUAGE | — | — |
| 23 | Language14 | LANGUAGE | — | — |
| 24 | Language15 | LANGUAGE | — | — |
| 25 | Language16 | LANGUAGE | — | — |
| 26 | Language17 | LANGUAGE | — | — |
| 27 | Language2 | LANGUAGE | — | — |
| 28 | Language3 | LANGUAGE | — | — |
| 29 | Language4 | LANGUAGE | — | — |
| 30 | Language5 | LANGUAGE | — | — |
| 31 | Language6 | LANGUAGE | — | — |
| 32 | Language7 | LANGUAGE | — | — |
| 33 | Language8 | LANGUAGE | — | — |
| 34 | Language9 | LANGUAGE | — | — |
| 35 | Name | NAME | — | ✅ |
| 36 | Name1 | NAME | — | ✅ |
| 37 | Name10 | NAME | — | ✅ |
| 38 | Name11 | NAME | — | ✅ |
| 39 | Name12 | NAME | — | ✅ |
| 40 | Name13 | NAME | — | ✅ |
| 41 | Name14 | NAME | — | ✅ |
| 42 | Name15 | NAME | — | ✅ |
| 43 | Name17 | NAME | — | ✅ |
| 44 | Name2 | NAME | — | ✅ |
| 45 | Name3 | NAME | — | ✅ |
| 46 | Name4 | NAME | — | ✅ |
| 47 | Name5 | NAME | — | ✅ |
| 48 | Name6 | NAME | — | ✅ |
| 49 | Name7 | NAME | — | ✅ |
| 50 | Name8 | NAME | — | ✅ |
| 51 | Name9 | NAME | — | ✅ |
| 52 | RuleId17 | RULE_ID | — | — |
| 53 | RuleId18 | RULE_ID | — | — |
| 54 | RuleId19 | RULE_ID | — | — |
| 55 | RuleId20 | RULE_ID | — | — |
| 56 | RuleId21 | RULE_ID | — | — |
| 57 | RuleId22 | RULE_ID | — | — |
| 58 | RuleId23 | RULE_ID | — | — |
| 59 | RuleId24 | RULE_ID | — | — |
| 60 | RuleId25 | RULE_ID | — | — |
| 61 | RuleId26 | RULE_ID | — | — |
| 62 | RuleId27 | RULE_ID | — | — |
| 63 | RuleId28 | RULE_ID | — | — |
| 64 | RuleId29 | RULE_ID | — | — |
| 65 | RuleId30 | RULE_ID | — | — |
| 66 | RuleId31 | RULE_ID | — | — |
| 67 | RuleId32 | RULE_ID | — | — |
| 68 | RuleId33 | RULE_ID | — | — |
| 69 | RuleTLPEOBaseParentRuleDesc | DESCRIPTION | — | ✅ |
| 70 | RuleTLPEOBaseParentRuleId | RULE_ID | — | — |
| 71 | RuleTLPEOBaseParentRuleLang | LANGUAGE | — | — |
| 72 | RuleTLPEOBaseParentRuleName | NAME | — | ✅ |

### [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseRuleId | BASE_RULE_ID | — | ✅ |
| 2 | BaseRuleUsageId | BASE_RULE_USAGE_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | Level01RuleId | LEVEL_01_RULE_ID | — | ✅ |
| 9 | Level02RuleId | LEVEL_02_RULE_ID | — | ✅ |
| 10 | Level03RuleId | LEVEL_03_RULE_ID | — | ✅ |
| 11 | Level04RuleId | LEVEL_04_RULE_ID | — | ✅ |
| 12 | Level05RuleId | LEVEL_05_RULE_ID | — | ✅ |
| 13 | Level06RuleId | LEVEL_06_RULE_ID | — | ✅ |
| 14 | Level07RuleId | LEVEL_07_RULE_ID | — | ✅ |
| 15 | Level08RuleId | LEVEL_08_RULE_ID | — | ✅ |
| 16 | Level09RuleId | LEVEL_09_RULE_ID | — | ✅ |
| 17 | Level10RuleId | LEVEL_10_RULE_ID | — | ✅ |
| 18 | Level11RuleId | LEVEL_11_RULE_ID | — | ✅ |
| 19 | Level12RuleId | LEVEL_12_RULE_ID | — | ✅ |
| 20 | Level13RuleId | LEVEL_13_RULE_ID | — | ✅ |
| 21 | Level14RuleId | LEVEL_14_RULE_ID | — | ✅ |
| 22 | Level15RuleId | LEVEL_15_RULE_ID | — | ✅ |
| 23 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 24 | OrgId | ORG_ID | — | ✅ |
| 25 | RuleHierarchyCfId | RULE_HIERARCHY_CF_ID | 🔑 | ✅ |
| 26 | TopRuleId | TOP_RULE_ID | — | ✅ |

### [[cn_rs_usages_all_tl|CN_RS_USAGES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | Name16 | NAME | — | ✅ |
| 3 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |
| 4 | OrgId1 | ORG_ID | 🔑 | ✅ |
| 5 | UsageId | USAGE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
