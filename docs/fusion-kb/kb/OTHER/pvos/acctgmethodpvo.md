---
id: DOC-OTHER-PVO-AcctgMethodPVO
doc_type: system-doc
title: "AcctgMethodPVO — PVO Cross-Module"
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
  - AcctgMethodPVO
  - acctgmethodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AcctgMethodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Acctg Method. Acessa as tabelas: XLA_ACCTG_METHODS_B, XLA_ACCTG_METHODS_TL.

**Caminho:** `FscmTopModelAM.FinXlaAmsSetupSlamAM.AcctgMethodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 2 | 18 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acctg_methods_b|XLA_ACCTG_METHODS_B]] — 11 atributos (2 PKs, 11 BICC)
- [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]] — 12 atributos (7 BICC)

---

## ⚙️ Atributos

### [[xla_acctg_methods_b|XLA_ACCTG_METHODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountingMethodCode | ACCOUNTING_METHOD_CODE | 🔑 | ✅ |
| 2 | AccountingMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | 🔑 | ✅ |
| 3 | AcctgMethodBaseAccountingCoaId | ACCOUNTING_COA_ID | — | ✅ |
| 4 | AcctgMethodBaseCreatedBy | CREATED_BY | — | ✅ |
| 5 | AcctgMethodBaseCreationDate | CREATION_DATE | — | ✅ |
| 6 | AcctgMethodBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | AcctgMethodBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AcctgMethodBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AcctgMethodBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AcctgMethodBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | AcctgMethodBaseTransactionCoaId | TRANSACTION_COA_ID | — | ✅ |

### [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctgMethodTranslationAccountingMethodCode | ACCOUNTING_METHOD_CODE | — | ✅ |
| 2 | AcctgMethodTranslationAccountingMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | — | ✅ |
| 3 | AcctgMethodTranslationCreatedBy | CREATED_BY | — | — |
| 4 | AcctgMethodTranslationCreationDate | CREATION_DATE | — | — |
| 5 | AcctgMethodTranslationDescription | DESCRIPTION | — | ✅ |
| 6 | AcctgMethodTranslationLanguage | LANGUAGE | — | ✅ |
| 7 | AcctgMethodTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AcctgMethodTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AcctgMethodTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AcctgMethodTranslationName | NAME | — | ✅ |
| 11 | AcctgMethodTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AcctgMethodTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
