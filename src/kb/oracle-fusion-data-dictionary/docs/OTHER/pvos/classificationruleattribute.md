---
id: DOC-OTHER-PVO-ClassificationRuleAttribute
doc_type: system-doc
title: "ClassificationRuleAttribute — PVO Cross-Module"
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
  - ClassificationRuleAttribute
  - classificationruleattribute
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ClassificationRuleAttribute

## 📌 Visão Geral

View Object para extração BICC de dados de Classification Rule Attribute. Acessa as tabelas: CN_RS_ATTRIBUTES_ALL_VL, CN_RS_ATTR_USAGES_ALL, CN_RS_RULE_ATTRIBUTES_ALL (+1).

**Caminho:** `FscmTopModelAM.RuleAM.ClassificationRuleAttribute`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 93 | 4 | 1 | 36 | 39% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rs_attributes_all_vl|CN_RS_ATTRIBUTES_ALL_VL]] — 14 atributos (4 BICC)
- [[cn_rs_attr_usages_all|CN_RS_ATTR_USAGES_ALL]] — 47 atributos (16 BICC)
- [[cn_rs_rule_attributes_all|CN_RS_RULE_ATTRIBUTES_ALL]] — 10 atributos (1 PKs, 7 BICC)
- [[cn_rs_rule_attr_values_all|CN_RS_RULE_ATTR_VALUES_ALL]] — 22 atributos (9 BICC)

---

## ⚙️ Atributos

### [[cn_rs_attributes_all_vl|CN_RS_ATTRIBUTES_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeId1 | ATTRIBUTE_ID | — | — |
| 2 | AttributeUsage | ATTRIBUTE_USAGE | — | — |
| 3 | CreatedBy3 | CREATED_BY | — | — |
| 4 | CreationDate3 | CREATION_DATE | — | — |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | EnabledFlag1 | ENABLED_FLAG | — | — |
| 7 | LastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 10 | LovType | LOV_TYPE | — | ✅ |
| 11 | ModuleId1 | MODULE_ID | — | — |
| 12 | Name | NAME | — | ✅ |
| 13 | ObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 14 | OrgId3 | ORG_ID | — | — |

### [[cn_rs_attr_usages_all|CN_RS_ATTR_USAGES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AliasRule1 | ALIAS_RULE1 | — | — |
| 2 | AttrRelationFactor | ATTR_RELATION_FACTOR | — | — |
| 3 | AttrUsageId1 | ATTR_USAGE_ID | — | — |
| 4 | AttributeId | ATTRIBUTE_ID | — | — |
| 5 | BatchOpBetween | BATCH_OP_BETWEEN | — | — |
| 6 | BatchOpCommonWhere | BATCH_OP_COMMON_WHERE | — | — |
| 7 | BatchOpEql | BATCH_OP_EQL | — | — |
| 8 | BatchOpLike | BATCH_OP_LIKE | — | — |
| 9 | BetweenFlag | BETWEEN_FLAG | — | ✅ |
| 10 | ComparisonOperatorCn | COMPARISON_OPERATOR_CN | — | ✅ |
| 11 | ConvertToIdFlag | CONVERT_TO_ID_FLAG | — | ✅ |
| 12 | CreatedBy2 | CREATED_BY | — | — |
| 13 | CreationDate2 | CREATION_DATE | — | — |
| 14 | CurrencyCodeCn | CURRENCY_CODE_CN | — | — |
| 15 | DisplayType | DISPLAY_TYPE | — | ✅ |
| 16 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 17 | EqualFlag | EQUAL_FLAG | — | ✅ |
| 18 | FirstCharCn | FIRST_CHAR_CN | — | — |
| 19 | HierarchyType | HIERARCHY_TYPE | — | ✅ |
| 20 | HighValueCharCn | HIGH_VALUE_CHAR_CN | — | — |
| 21 | HighValueNumberCn | HIGH_VALUE_NUMBER_CN | — | — |
| 22 | HtmlLovSql1 | HTML_LOV_SQL1 | — | — |
| 23 | HtmlLovSql2 | HTML_LOV_SQL2 | — | — |
| 24 | HtmlLovSql3 | HTML_LOV_SQL3 | — | — |
| 25 | IndexedColName | INDEXED_COL_NAME | — | ✅ |
| 26 | InsertAttrValStmt | INSERT_ATTR_VAL_STMT | — | ✅ |
| 27 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 29 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 30 | LikeFlag | LIKE_FLAG | — | ✅ |
| 31 | LowValueCharCn | LOW_VALUE_CHAR_CN | — | ✅ |
| 32 | LowValueCharIdCn | LOW_VALUE_CHAR_ID_CN | — | — |
| 33 | LowValueNumberCn | LOW_VALUE_NUMBER_CN | — | — |
| 34 | ModuleId | MODULE_ID | — | — |
| 35 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 36 | OrgId2 | ORG_ID | — | — |
| 37 | RealTimeFrom | REAL_TIME_FROM | — | — |
| 38 | RealTimeSelect | REAL_TIME_SELECT | — | — |
| 39 | RealTimeWhere | REAL_TIME_WHERE | — | — |
| 40 | SeededFlag | SEEDED_FLAG | — | ✅ |
| 41 | SourceColumnName | SOURCE_COLUMN_NAME | — | ✅ |
| 42 | UpdateAttrValStmt | UPDATE_ATTR_VAL_STMT | — | ✅ |
| 43 | UsageId | USAGE_ID | — | ✅ |
| 44 | Value1IdCn | VALUE1_ID_CN | — | — |
| 45 | Value2IdCn | VALUE2_ID_CN | — | — |
| 46 | Value3IdCn | VALUE3_ID_CN | — | — |
| 47 | Value4IdCn | VALUE4_ID_CN | — | — |

### [[cn_rs_rule_attributes_all|CN_RS_RULE_ATTRIBUTES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttrUsageId | ATTR_USAGE_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | OrgId | ORG_ID | — | ✅ |
| 9 | RuleAttributeId | RULE_ATTRIBUTE_ID | 🔑 | ✅ |
| 10 | RuleId | RULE_ID | — | ✅ |

### [[cn_rs_rule_attr_values_all|CN_RS_RULE_ATTR_VALUES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComparisonOperator | COMPARISON_OPERATOR | — | ✅ |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 5 | FirstChar | FIRST_CHAR | — | — |
| 6 | HighValueChar | HIGH_VALUE_CHAR | — | ✅ |
| 7 | HighValueNumber | HIGH_VALUE_NUMBER | — | ✅ |
| 8 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 11 | LowValueChar | LOW_VALUE_CHAR | — | ✅ |
| 12 | LowValueCharCode | LOW_VALUE_CHAR_CODE | — | — |
| 13 | LowValueCharId | LOW_VALUE_CHAR_ID | — | ✅ |
| 14 | LowValueNumber | LOW_VALUE_NUMBER | — | ✅ |
| 15 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 16 | OrgId1 | ORG_ID | — | — |
| 17 | RuleAttrValueId | RULE_ATTR_VALUE_ID | — | ✅ |
| 18 | RuleAttributeId1 | RULE_ATTRIBUTE_ID | — | — |
| 19 | Value1Id | VALUE1_ID | — | — |
| 20 | Value2Id | VALUE2_ID | — | — |
| 21 | Value3Id | VALUE3_ID | — | — |
| 22 | Value4Id | VALUE4_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
