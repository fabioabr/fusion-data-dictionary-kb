---
id: DOC-OTHER-PVO-RuleSetMemberPVO
doc_type: system-doc
title: "RuleSetMemberPVO — PVO Cross-Module"
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
  - RuleSetMemberPVO
  - rulesetmemberpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RuleSetMemberPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rule Set Member. Acessa as tabelas: HWM_RULES, HWM_RULE_SETS_F, HWM_RULE_SET_MBRS (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesCoreAM.RuleSetMemberPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 4 | 1 | 28 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rules|HWM_RULES]] — 2 atributos (1 BICC)
- [[hwm_rule_sets_f|HWM_RULE_SETS_F]] — 27 atributos (13 BICC)
- [[hwm_rule_set_mbrs|HWM_RULE_SET_MBRS]] — 16 atributos (1 PKs, 12 BICC)
- [[hwm_tcats_vl|HWM_TCATS_VL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_rules|HWM_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemberRulePEORuleId | RULE_ID | — | — |
| 2 | MemberRulePEORuleName | RULE_NAME | — | ✅ |

### [[hwm_rule_sets_f|HWM_RULE_SETS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MemberRuleSetDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | MemberRuleSetDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | MemberRuleSetDPEORuleSetId | RULE_SET_ID | — | — |
| 4 | MemberRuleSetDPEORuleSetName | RULE_SET_NAME | — | ✅ |
| 5 | RuleSetDPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | RuleSetDPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | RuleSetDPEODescription | DESCRIPTION | — | ✅ |
| 8 | RuleSetDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | RuleSetDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 10 | RuleSetDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | RuleSetDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | RuleSetDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | RuleSetDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | RuleSetDPEOModuleId | MODULE_ID | — | — |
| 15 | RuleSetDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | RuleSetDPEORuleSetId | RULE_SET_ID | — | ✅ |
| 17 | RuleSetDPEORuleSetName | RULE_SET_NAME | — | ✅ |
| 18 | RuleSetDPEORuleSetUnqId | RULE_SET_UNQ_ID | — | ✅ |
| 19 | RuleSetDPEORuleType | RULE_TYPE | — | ✅ |
| 20 | RuleSetDPEOSortAttribute1 | SORT_ATTRIBUTE1 | — | — |
| 21 | RuleSetDPEOSortAttribute2 | SORT_ATTRIBUTE2 | — | — |
| 22 | RuleSetDPEOSortAttribute3 | SORT_ATTRIBUTE3 | — | — |
| 23 | RuleSetDPEOSortAttribute4 | SORT_ATTRIBUTE4 | — | — |
| 24 | RuleSetDPEOSortAttribute5 | SORT_ATTRIBUTE5 | — | — |
| 25 | RuleSetDPEOSortAttribute6 | SORT_ATTRIBUTE6 | — | — |
| 26 | RuleSetDPEOSortDuration | SORT_DURATION | — | — |
| 27 | RuleSetDPEOSortEntryType | SORT_ENTRY_TYPE | — | — |

### [[hwm_rule_set_mbrs|HWM_RULE_SET_MBRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleSetMemberPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RuleSetMemberPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RuleSetMemberPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | RuleSetMemberPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RuleSetMemberPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RuleSetMemberPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RuleSetMemberPEOMbrCndlRuleId | MBR_CNDL_RULE_ID | — | — |
| 8 | RuleSetMemberPEOMbrRuleId | MBR_RULE_ID | — | ✅ |
| 9 | RuleSetMemberPEOMbrRuleSetId | MBR_RULE_SET_ID | — | ✅ |
| 10 | RuleSetMemberPEOMemberType | MEMBER_TYPE | — | ✅ |
| 11 | RuleSetMemberPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RuleSetMemberPEOProcessingOrder | PROCESSING_ORDER | — | ✅ |
| 13 | RuleSetMemberPEORuleSetId | RULE_SET_ID | — | ✅ |
| 14 | RuleSetMemberPEORuleSetMbrsId | RULE_SET_MBRS_ID | 🔑 | ✅ |
| 15 | RuleSetMemberPEORuleSetUnqId | RULE_SET_UNQ_ID | — | — |
| 16 | RuleSetMemberPEOTcatId | TCAT_ID | — | ✅ |

### [[hwm_tcats_vl|HWM_TCATS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryVLPEOTcatCd | TCAT_CD | — | ✅ |
| 2 | TimeCategoryVLPEOTcatId | TCAT_ID | — | — |
| 3 | TimeCategoryVLPEOTcatName | TCAT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
