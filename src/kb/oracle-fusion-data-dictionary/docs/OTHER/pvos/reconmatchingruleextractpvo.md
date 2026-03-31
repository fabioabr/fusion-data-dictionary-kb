---
id: DOC-OTHER-PVO-ReconMatchingRuleExtractPVO
doc_type: system-doc
title: "ReconMatchingRuleExtractPVO — PVO Cross-Module"
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
  - ReconMatchingRuleExtractPVO
  - reconmatchingruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReconMatchingRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Recon Matching Rule Extract. Acessa as tabelas: CE_RECON_MATCHING_RULES.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.ReconMatchingRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_recon_matching_rules|CE_RECON_MATCHING_RULES]] — 24 atributos (1 PKs, 24 BICC)

---

## ⚙️ Atributos

### [[ce_recon_matching_rules|CE_RECON_MATCHING_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReconMatchingRuleActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ReconMatchingRuleAmountMatchFlag | AMOUNT_MATCH_FLAG | — | ✅ |
| 3 | ReconMatchingRuleApSourceFlag | AP_SOURCE_FLAG | — | ✅ |
| 4 | ReconMatchingRuleArSourceFlag | AR_SOURCE_FLAG | — | ✅ |
| 5 | ReconMatchingRuleCreatedBy | CREATED_BY | — | ✅ |
| 6 | ReconMatchingRuleCreationDate | CREATION_DATE | — | ✅ |
| 7 | ReconMatchingRuleDateMatchFlag | DATE_MATCH_FLAG | — | ✅ |
| 8 | ReconMatchingRuleDescription | DESCRIPTION | — | ✅ |
| 9 | ReconMatchingRuleExtSourceFlag | EXT_SOURCE_FLAG | — | ✅ |
| 10 | ReconMatchingRuleGlSourceFlag | GL_SOURCE_FLAG | — | ✅ |
| 11 | ReconMatchingRuleJoinCondition | JOIN_CONDITION | — | ✅ |
| 12 | ReconMatchingRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | ReconMatchingRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | ReconMatchingRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ReconMatchingRuleMatchType | MATCH_TYPE | — | ✅ |
| 16 | ReconMatchingRuleMatchingRuleName | MATCHING_RULE_NAME | — | ✅ |
| 17 | ReconMatchingRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ReconMatchingRulePaySourceFlag | PAY_SOURCE_FLAG | — | ✅ |
| 19 | ReconMatchingRuleReconMatchingRuleId | RECON_MATCHING_RULE_ID | 🔑 | ✅ |
| 20 | ReconMatchingRuleReferenceIdMatchFlag | REFERENCE_ID_MATCH_FLAG | — | ✅ |
| 21 | ReconMatchingRuleSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 22 | ReconMatchingRuleStmtGroupby | STMT_GROUPBY | — | ✅ |
| 23 | ReconMatchingRuleTrxGroupby | TRX_GROUPBY | — | ✅ |
| 24 | ReconMatchingRuleTypeMatchFlag | TYPE_MATCH_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
