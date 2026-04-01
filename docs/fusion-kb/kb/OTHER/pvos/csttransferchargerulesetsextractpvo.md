---
id: DOC-OTHER-PVO-CstTransferChargeRuleSetsExtractPVO
doc_type: system-doc
title: "CstTransferChargeRuleSetsExtractPVO — PVO Cross-Module"
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
  - CstTransferChargeRuleSetsExtractPVO
  - csttransferchargerulesetsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstTransferChargeRuleSetsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Transfer Charge Rule Sets Extract. Acessa as tabelas: CST_STD_TXFR_COST_RULE_SETS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstTransferChargeRuleSetsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_std_txfr_cost_rule_sets|CST_STD_TXFR_COST_RULE_SETS]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_std_txfr_cost_rule_sets|CST_STD_TXFR_COST_RULE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstTransferChargeRuleSetsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CstTransferChargeRuleSetsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CstTransferChargeRuleSetsPEODescription | DESCRIPTION | — | ✅ |
| 4 | CstTransferChargeRuleSetsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CstTransferChargeRuleSetsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | CstTransferChargeRuleSetsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | CstTransferChargeRuleSetsPEORuleSetName | RULE_SET_NAME | — | ✅ |
| 8 | CstTransferChargeRuleSetsPEOStdTxfrCostRuleSetId | STD_TXFR_COST_RULE_SET_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
