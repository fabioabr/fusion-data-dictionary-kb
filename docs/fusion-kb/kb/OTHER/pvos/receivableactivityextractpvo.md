---
id: DOC-OTHER-PVO-ReceivableActivityExtractPVO
doc_type: system-doc
title: "ReceivableActivityExtractPVO — PVO Cross-Module"
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
  - ReceivableActivityExtractPVO
  - receivableactivityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivableActivityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receivable Activity Extract. Acessa as tabelas: AR_RECEIVABLES_TRX_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReceivableActivityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 1 | 2 | 26 | 41% |

---

## 🔗 Tabelas Relacionadas

- [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]] — 63 atributos (2 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[ar_receivables_trx_all|AR_RECEIVABLES_TRX_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArReceivablesTrxAccountingAffectFlag | ACCOUNTING_AFFECT_FLAG | — | ✅ |
| 2 | ArReceivablesTrxAssetTaxCode | ASSET_TAX_CODE | — | ✅ |
| 3 | ArReceivablesTrxAttribute1 | ATTRIBUTE1 | — | — |
| 4 | ArReceivablesTrxAttribute10 | ATTRIBUTE10 | — | — |
| 5 | ArReceivablesTrxAttribute11 | ATTRIBUTE11 | — | — |
| 6 | ArReceivablesTrxAttribute12 | ATTRIBUTE12 | — | — |
| 7 | ArReceivablesTrxAttribute13 | ATTRIBUTE13 | — | — |
| 8 | ArReceivablesTrxAttribute14 | ATTRIBUTE14 | — | — |
| 9 | ArReceivablesTrxAttribute15 | ATTRIBUTE15 | — | — |
| 10 | ArReceivablesTrxAttribute2 | ATTRIBUTE2 | — | — |
| 11 | ArReceivablesTrxAttribute3 | ATTRIBUTE3 | — | — |
| 12 | ArReceivablesTrxAttribute4 | ATTRIBUTE4 | — | — |
| 13 | ArReceivablesTrxAttribute5 | ATTRIBUTE5 | — | — |
| 14 | ArReceivablesTrxAttribute6 | ATTRIBUTE6 | — | — |
| 15 | ArReceivablesTrxAttribute7 | ATTRIBUTE7 | — | — |
| 16 | ArReceivablesTrxAttribute8 | ATTRIBUTE8 | — | — |
| 17 | ArReceivablesTrxAttribute9 | ATTRIBUTE9 | — | — |
| 18 | ArReceivablesTrxAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 19 | ArReceivablesTrxCodeCombinationId | CODE_COMBINATION_ID | — | ✅ |
| 20 | ArReceivablesTrxCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArReceivablesTrxCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArReceivablesTrxDefaultAcctgDistributionSet | DEFAULT_ACCTG_DISTRIBUTION_SET | — | ✅ |
| 23 | ArReceivablesTrxDescription | DESCRIPTION | — | ✅ |
| 24 | ArReceivablesTrxEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 25 | ArReceivablesTrxGlAccountSource | GL_ACCOUNT_SOURCE | — | ✅ |
| 26 | ArReceivablesTrxGlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 27 | ArReceivablesTrxGlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 28 | ArReceivablesTrxGlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 29 | ArReceivablesTrxGlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 30 | ArReceivablesTrxGlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 31 | ArReceivablesTrxGlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 32 | ArReceivablesTrxGlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 33 | ArReceivablesTrxGlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 34 | ArReceivablesTrxGlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 35 | ArReceivablesTrxGlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 36 | ArReceivablesTrxGlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 37 | ArReceivablesTrxGlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 38 | ArReceivablesTrxGlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 39 | ArReceivablesTrxGlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 40 | ArReceivablesTrxGlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 41 | ArReceivablesTrxGlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 42 | ArReceivablesTrxGlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 43 | ArReceivablesTrxGlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 44 | ArReceivablesTrxGlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 45 | ArReceivablesTrxGlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 46 | ArReceivablesTrxGlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 47 | ArReceivablesTrxInactiveDate | INACTIVE_DATE | — | ✅ |
| 48 | ArReceivablesTrxLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 49 | ArReceivablesTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 50 | ArReceivablesTrxLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 51 | ArReceivablesTrxLiabilityTaxCode | LIABILITY_TAX_CODE | — | ✅ |
| 52 | ArReceivablesTrxName | NAME | — | ✅ |
| 53 | ArReceivablesTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 54 | ArReceivablesTrxOrgId | ORG_ID | 🔑 | ✅ |
| 55 | ArReceivablesTrxReceivablesTrxId | RECEIVABLES_TRX_ID | 🔑 | ✅ |
| 56 | ArReceivablesTrxRiskEliminationDays | RISK_ELIMINATION_DAYS | — | ✅ |
| 57 | ArReceivablesTrxSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 58 | ArReceivablesTrxSetOfBooksId | SET_OF_BOOKS_ID | — | ✅ |
| 59 | ArReceivablesTrxStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 60 | ArReceivablesTrxStatus | STATUS | — | ✅ |
| 61 | ArReceivablesTrxTaxCodeSource | TAX_CODE_SOURCE | — | ✅ |
| 62 | ArReceivablesTrxTaxRecoverableFlag | TAX_RECOVERABLE_FLAG | — | ✅ |
| 63 | ArReceivablesTrxType | TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
