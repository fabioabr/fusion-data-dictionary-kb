---
id: DOC-OTHER-PVO-TSRRuleSetDPVO
doc_type: system-doc
title: "TSRRuleSetDPVO — PVO Cross-Module"
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
  - TSRRuleSetDPVO
  - tsrrulesetdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TSRRuleSetDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de TSRRule Set D. Acessa as tabelas: HWM_RULE_SETS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.RulesCoreAM.TSRRuleSetDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 3 | 11 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_rule_sets_f|HWM_RULE_SETS_F]] — 23 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hwm_rule_sets_f|HWM_RULE_SETS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RuleSetDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | RuleSetDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | RuleSetDPEODescription | DESCRIPTION | — | ✅ |
| 4 | RuleSetDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | RuleSetDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | RuleSetDPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | RuleSetDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RuleSetDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | RuleSetDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RuleSetDPEOModuleId | MODULE_ID | — | — |
| 11 | RuleSetDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | RuleSetDPEORuleSetId | RULE_SET_ID | 🔑 | ✅ |
| 13 | RuleSetDPEORuleSetName | RULE_SET_NAME | — | ✅ |
| 14 | RuleSetDPEORuleSetUnqId | RULE_SET_UNQ_ID | — | ✅ |
| 15 | RuleSetDPEORuleType | RULE_TYPE | — | — |
| 16 | RuleSetDPEOSortAttribute1 | SORT_ATTRIBUTE1 | — | — |
| 17 | RuleSetDPEOSortAttribute2 | SORT_ATTRIBUTE2 | — | — |
| 18 | RuleSetDPEOSortAttribute3 | SORT_ATTRIBUTE3 | — | — |
| 19 | RuleSetDPEOSortAttribute4 | SORT_ATTRIBUTE4 | — | — |
| 20 | RuleSetDPEOSortAttribute5 | SORT_ATTRIBUTE5 | — | — |
| 21 | RuleSetDPEOSortAttribute6 | SORT_ATTRIBUTE6 | — | — |
| 22 | RuleSetDPEOSortDuration | SORT_DURATION | — | — |
| 23 | RuleSetDPEOSortEntryType | SORT_ENTRY_TYPE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
