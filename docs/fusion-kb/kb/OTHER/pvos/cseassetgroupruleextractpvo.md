---
id: DOC-OTHER-PVO-CseAssetGroupRuleExtractPVO
doc_type: system-doc
title: "CseAssetGroupRuleExtractPVO — PVO Cross-Module"
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
  - CseAssetGroupRuleExtractPVO
  - cseassetgroupruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetGroupRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Group Rule Extract. Acessa as tabelas: CSE_GROUP_RULES_B, CSE_GROUP_RULES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetGroupRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 2 | 3 | 63 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_group_rules_b|CSE_GROUP_RULES_B]] — 52 atributos (1 PKs, 52 BICC)
- [[cse_group_rules_tl|CSE_GROUP_RULES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_group_rules_b|CSE_GROUP_RULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 3 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 4 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 5 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 6 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 7 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 8 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 9 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 10 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 11 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 12 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 13 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 14 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 15 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 16 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 17 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 18 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 19 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 20 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 21 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 22 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 23 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 28 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 29 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 30 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 31 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 32 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 33 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 34 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 35 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 36 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 37 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 38 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 39 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 40 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 41 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 42 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 43 | CreatedBy | CREATED_BY | — | ✅ |
| 44 | CreationDate | CREATION_DATE | — | ✅ |
| 45 | GroupingModeCode | GROUPING_MODE_CODE | — | ✅ |
| 46 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 47 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 48 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 49 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 50 | RuleCode | RULE_CODE | — | ✅ |
| 51 | RuleId | RULE_ID | 🔑 | ✅ |
| 52 | UniqueAssignmentFlag | UNIQUE_ASSIGNMENT_FLAG | — | ✅ |

### [[cse_group_rules_tl|CSE_GROUP_RULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetGroupRuleTranslationAna1CreatedBy | CREATED_BY | — | ✅ |
| 2 | AssetGroupRuleTranslationAna1CreationDate | CREATION_DATE | — | ✅ |
| 3 | AssetGroupRuleTranslationAna1Language | LANGUAGE | 🔑 | ✅ |
| 4 | AssetGroupRuleTranslationAna1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AssetGroupRuleTranslationAna1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | AssetGroupRuleTranslationAna1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | AssetGroupRuleTranslationAna1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | AssetGroupRuleTranslationAna1RuleDescription | RULE_DESCRIPTION | — | ✅ |
| 9 | AssetGroupRuleTranslationAna1RuleId | RULE_ID | 🔑 | ✅ |
| 10 | AssetGroupRuleTranslationAna1RuleName | RULE_NAME | — | ✅ |
| 11 | AssetGroupRuleTranslationAna1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
