---
id: DOC-OTHER-PVO-AccountingMethodTLExtractPVO
doc_type: system-doc
title: "AccountingMethodTLExtractPVO — PVO Cross-Module"
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
  - AccountingMethodTLExtractPVO
  - accountingmethodtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountingMethodTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Accounting Method TLExtract. Acessa as tabelas: XLA_ACCTG_METHODS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.AccountingMethodTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[xla_acctg_methods_tl|XLA_ACCTG_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctgMethodTranslationAccountingMethodCode | ACCOUNTING_METHOD_CODE | 🔑 | ✅ |
| 2 | AcctgMethodTranslationAccountingMethodTypeCode | ACCOUNTING_METHOD_TYPE_CODE | 🔑 | ✅ |
| 3 | AcctgMethodTranslationCreatedBy | CREATED_BY | — | ✅ |
| 4 | AcctgMethodTranslationCreationDate | CREATION_DATE | — | ✅ |
| 5 | AcctgMethodTranslationDescription | DESCRIPTION | — | ✅ |
| 6 | AcctgMethodTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | AcctgMethodTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AcctgMethodTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AcctgMethodTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AcctgMethodTranslationName | NAME | — | ✅ |
| 11 | AcctgMethodTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | AcctgMethodTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
