---
id: DOC-OTHER-PVO-CstExpensePoolTLExtractPVO
doc_type: system-doc
title: "CstExpensePoolTLExtractPVO — PVO Cross-Module"
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
  - CstExpensePoolTLExtractPVO
  - cstexpensepooltlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstExpensePoolTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Expense Pool TLExtract. Acessa as tabelas: CST_EXPENSE_POOLS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstExpensePoolTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_expense_pools_tl|CST_EXPENSE_POOLS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[cst_expense_pools_tl|CST_EXPENSE_POOLS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstExpensePoolTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | CstExpensePoolTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | CstExpensePoolTLPEOExpensePoolDesc | EXPENSE_POOL_DESC | — | ✅ |
| 4 | CstExpensePoolTLPEOExpensePoolId | EXPENSE_POOL_ID | 🔑 | ✅ |
| 5 | CstExpensePoolTLPEOExpensePoolName | EXPENSE_POOL_NAME | — | ✅ |
| 6 | CstExpensePoolTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CstExpensePoolTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CstExpensePoolTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CstExpensePoolTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CstExpensePoolTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
