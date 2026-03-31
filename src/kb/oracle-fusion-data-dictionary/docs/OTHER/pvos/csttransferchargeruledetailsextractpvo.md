---
id: DOC-OTHER-PVO-CstTransferChargeRuleDetailsExtractPVO
doc_type: system-doc
title: "CstTransferChargeRuleDetailsExtractPVO — PVO Cross-Module"
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
  - CstTransferChargeRuleDetailsExtractPVO
  - csttransferchargeruledetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransferChargeRuleDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transfer Charge Rule Details Extract. Acessa as tabelas: CST_STD_TXFR_COST_RULES, CST_STD_TXFR_COST_RULE_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransferChargeRuleDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 2 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_std_txfr_cost_rules|CST_STD_TXFR_COST_RULES]] — 7 atributos (7 BICC)
- [[cst_std_txfr_cost_rule_dtls|CST_STD_TXFR_COST_RULE_DTLS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_std_txfr_cost_rules|CST_STD_TXFR_COST_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferChargeRulesPEODestinationOrgId | DESTINATION_ORG_ID | — | ✅ |
| 2 | CstTransferChargeRulesPEOEndDate | END_DATE | — | ✅ |
| 3 | CstTransferChargeRulesPEOLastUsedDate | LAST_USED_DATE | — | ✅ |
| 4 | CstTransferChargeRulesPEOSourceOrgId | SOURCE_ORG_ID | — | ✅ |
| 5 | CstTransferChargeRulesPEOStartDate | START_DATE | — | ✅ |
| 6 | CstTransferChargeRulesPEOStdTxfrCostRuleId | STD_TXFR_COST_RULE_ID | — | ✅ |
| 7 | CstTransferChargeRulesPEOStdTxfrCostRuleSetId | STD_TXFR_COST_RULE_SET_ID | — | ✅ |

### [[cst_std_txfr_cost_rule_dtls|CST_STD_TXFR_COST_RULE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferChargeRuleDetailsPEOChargeType | CHARGE_TYPE | — | ✅ |
| 2 | CstTransferChargeRuleDetailsPEOCostElementId | COST_ELEMENT_ID | — | ✅ |
| 3 | CstTransferChargeRuleDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstTransferChargeRuleDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstTransferChargeRuleDetailsPEOExpensePoolId | EXPENSE_POOL_ID | — | ✅ |
| 6 | CstTransferChargeRuleDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | CstTransferChargeRuleDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | CstTransferChargeRuleDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | CstTransferChargeRuleDetailsPEOStdTxfrCostRuleDtlId | STD_TXFR_COST_RULE_DTL_ID | 🔑 | ✅ |
| 10 | CstTransferChargeRuleDetailsPEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
