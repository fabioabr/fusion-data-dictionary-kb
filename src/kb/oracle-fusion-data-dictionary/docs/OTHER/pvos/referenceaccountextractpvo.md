---
id: DOC-OTHER-PVO-ReferenceAccountExtractPVO
doc_type: system-doc
title: "ReferenceAccountExtractPVO — PVO Cross-Module"
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
  - ReferenceAccountExtractPVO
  - referenceaccountextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceAccountExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reference Account Extract. Acessa as tabelas: AR_REF_ACCOUNTS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ReferenceAccountExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 3 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_ref_accounts_all|AR_REF_ACCOUNTS_ALL]] — 22 atributos (3 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[ar_ref_accounts_all|AR_REF_ACCOUNTS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArRefAccountBrFactorCcid | BR_FACTOR_CCID | — | ✅ |
| 2 | ArRefAccountBrRemitCcid | BR_REMIT_CCID | — | ✅ |
| 3 | ArRefAccountBrUnpaidCcid | BR_UNPAID_CCID | — | ✅ |
| 4 | ArRefAccountBuId | BU_ID | 🔑 | ✅ |
| 5 | ArRefAccountClearingCcid | CLEARING_CCID | — | ✅ |
| 6 | ArRefAccountCreatedBy | CREATED_BY | — | ✅ |
| 7 | ArRefAccountCreationDate | CREATION_DATE | — | ✅ |
| 8 | ArRefAccountDistSetCcid | DIST_SET_CCID | — | ✅ |
| 9 | ArRefAccountDrcCcid | DRC_CCID | — | ✅ |
| 10 | ArRefAccountFreightCcid | FREIGHT_CCID | — | ✅ |
| 11 | ArRefAccountLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ArRefAccountLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ArRefAccountLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ArRefAccountLedgerId | LEDGER_ID | — | ✅ |
| 15 | ArRefAccountObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | ArRefAccountRecCcid | REC_CCID | — | ✅ |
| 17 | ArRefAccountRevCcid | REV_CCID | — | ✅ |
| 18 | ArRefAccountSourceRefAccountId | SOURCE_REF_ACCOUNT_ID | 🔑 | ✅ |
| 19 | ArRefAccountSourceRefTable | SOURCE_REF_TABLE | 🔑 | ✅ |
| 20 | ArRefAccountTaxCcid | TAX_CCID | — | ✅ |
| 21 | ArRefAccountUnbilledCcid | UNBILLED_CCID | — | ✅ |
| 22 | ArRefAccountUnearnedCcid | UNEARNED_CCID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
