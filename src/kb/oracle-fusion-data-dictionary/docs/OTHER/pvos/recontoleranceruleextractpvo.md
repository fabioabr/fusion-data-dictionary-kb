---
id: DOC-OTHER-PVO-ReconToleranceRuleExtractPVO
doc_type: system-doc
title: "ReconToleranceRuleExtractPVO — PVO Cross-Module"
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
  - ReconToleranceRuleExtractPVO
  - recontoleranceruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReconToleranceRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Recon Tolerance Rule Extract. Acessa as tabelas: CE_RECON_TOLERANCE_RULES.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.ReconToleranceRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_recon_tolerance_rules|CE_RECON_TOLERANCE_RULES]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[ce_recon_tolerance_rules|CE_RECON_TOLERANCE_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconToleranceRuleActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ReconToleranceRuleAmountAbove | AMOUNT_ABOVE | — | ✅ |
| 3 | ReconToleranceRuleAmountBelow | AMOUNT_BELOW | — | ✅ |
| 4 | ReconToleranceRuleAmountEnabledFlag | AMOUNT_ENABLED_FLAG | — | ✅ |
| 5 | ReconToleranceRuleCreatedBy | CREATED_BY | — | ✅ |
| 6 | ReconToleranceRuleCreationDate | CREATION_DATE | — | ✅ |
| 7 | ReconToleranceRuleDateEnabledFlag | DATE_ENABLED_FLAG | — | ✅ |
| 8 | ReconToleranceRuleDaysAfter | DAYS_AFTER | — | ✅ |
| 9 | ReconToleranceRuleDaysBefore | DAYS_BEFORE | — | ✅ |
| 10 | ReconToleranceRuleDescription | DESCRIPTION | — | ✅ |
| 11 | ReconToleranceRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ReconToleranceRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ReconToleranceRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ReconToleranceRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | ReconToleranceRulePercentAbove | PERCENT_ABOVE | — | ✅ |
| 16 | ReconToleranceRulePercentBelow | PERCENT_BELOW | — | ✅ |
| 17 | ReconToleranceRuleReconToleranceRuleId | RECON_TOLERANCE_RULE_ID | 🔑 | ✅ |
| 18 | ReconToleranceRuleToleranceRuleName | TOLERANCE_RULE_NAME | — | ✅ |
| 19 | ReconToleranceRulesPercentEnabledFlag | PERCENT_ENABLED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
