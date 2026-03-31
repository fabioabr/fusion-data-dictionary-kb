---
id: DOC-OTHER-PVO-AutomatchRuleExtractPVO
doc_type: system-doc
title: "AutomatchRuleExtractPVO — PVO Cross-Module"
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
  - AutomatchRuleExtractPVO
  - automatchruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AutomatchRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Automatch Rule Extract. Acessa as tabelas: AR_AUTOMATCH_RULES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.AutomatchRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 1 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_automatch_rules|AR_AUTOMATCH_RULES]] — 27 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[ar_automatch_rules|AR_AUTOMATCH_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAutomationRuleActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ArAutomationRuleAmountWeight | AMOUNT_WEIGHT | — | ✅ |
| 3 | ArAutomationRuleAutomatchRuleId | AUTOMATCH_RULE_ID | 🔑 | ✅ |
| 4 | ArAutomationRuleCreatedBy | CREATED_BY | — | ✅ |
| 5 | ArAutomationRuleCreationDate | CREATION_DATE | — | ✅ |
| 6 | ArAutomationRuleCustomerThreshold | CUSTOMER_THRESHOLD | — | ✅ |
| 7 | ArAutomationRuleCustomerWeight | CUSTOMER_WEIGHT | — | ✅ |
| 8 | ArAutomationRuleDescription | DESCRIPTION | — | ✅ |
| 9 | ArAutomationRuleEndDate | END_DATE | — | ✅ |
| 10 | ArAutomationRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ArAutomationRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | ArAutomationRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ArAutomationRuleMinMatchThreshold | MIN_MATCH_THRESHOLD | — | ✅ |
| 14 | ArAutomationRuleName | NAME | — | ✅ |
| 15 | ArAutomationRuleNetFreightWeight | NET_FREIGHT_WEIGHT | — | ✅ |
| 16 | ArAutomationRuleNetTaxFreightWeight | NET_TAX_FREIGHT_WEIGHT | — | ✅ |
| 17 | ArAutomationRuleNetTaxWeight | NET_TAX_WEIGHT | — | ✅ |
| 18 | ArAutomationRuleNetUndiscWeight | NET_UNDISC_WEIGHT | — | ✅ |
| 19 | ArAutomationRuleNumberOfDaysClosed | NUMBER_OF_DAYS_CLOSED | — | ✅ |
| 20 | ArAutomationRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | ArAutomationRuleRemittanceRegexp | REMITTANCE_REGEXP | — | ✅ |
| 22 | ArAutomationRuleSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 23 | ArAutomationRuleSetId | SET_ID | — | ✅ |
| 24 | ArAutomationRuleStartDate | START_DATE | — | ✅ |
| 25 | ArAutomationRuleTransactionRegexp | TRANSACTION_REGEXP | — | ✅ |
| 26 | ArAutomationRuleTransactionThreshold | TRANSACTION_THRESHOLD | — | ✅ |
| 27 | ArAutomationRuleTransactionWeight | TRANSACTION_WEIGHT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
