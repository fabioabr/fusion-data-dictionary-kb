---
id: DOC-OTHER-PVO-RollupCreditRuleHierarchy
doc_type: system-doc
title: "RollupCreditRuleHierarchy — PVO Cross-Module"
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
  - RollupCreditRuleHierarchy
  - rollupcreditrulehierarchy
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RollupCreditRuleHierarchy

## 📌 Visão Geral

View Object para extração BICC de dados de Rollup Credit Rule Hierarchy. Acessa as tabelas: CN_RS_RULES_HIERARCHY_CF_ALL.

**Caminho:** `FscmTopModelAM.RuleAM.RollupCreditRuleHierarchy`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 2 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]] — 26 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[cn_rs_rules_hierarchy_cf_all|CN_RS_RULES_HIERARCHY_CF_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseRuleId | BASE_RULE_ID | — | — |
| 2 | BaseRuleUsageId | BASE_RULE_USAGE_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | Level01RuleId | LEVEL_01_RULE_ID | — | — |
| 9 | Level02RuleId | LEVEL_02_RULE_ID | — | — |
| 10 | Level03RuleId | LEVEL_03_RULE_ID | — | — |
| 11 | Level04RuleId | LEVEL_04_RULE_ID | — | — |
| 12 | Level05RuleId | LEVEL_05_RULE_ID | — | — |
| 13 | Level06RuleId | LEVEL_06_RULE_ID | — | — |
| 14 | Level07RuleId | LEVEL_07_RULE_ID | — | — |
| 15 | Level08RuleId | LEVEL_08_RULE_ID | — | — |
| 16 | Level09RuleId | LEVEL_09_RULE_ID | — | — |
| 17 | Level10RuleId | LEVEL_10_RULE_ID | — | — |
| 18 | Level11RuleId | LEVEL_11_RULE_ID | — | — |
| 19 | Level12RuleId | LEVEL_12_RULE_ID | — | — |
| 20 | Level13RuleId | LEVEL_13_RULE_ID | — | — |
| 21 | Level14RuleId | LEVEL_14_RULE_ID | — | — |
| 22 | Level15RuleId | LEVEL_15_RULE_ID | — | — |
| 23 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | OrgId | ORG_ID | — | — |
| 25 | RuleHierarchyCfId | RULE_HIERARCHY_CF_ID | 🔑 | ✅ |
| 26 | TopRuleId | TOP_RULE_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
