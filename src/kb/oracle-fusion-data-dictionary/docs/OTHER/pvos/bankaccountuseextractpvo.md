---
id: DOC-OTHER-PVO-BankAccountUseExtractPVO
doc_type: system-doc
title: "BankAccountUseExtractPVO — PVO Cross-Module"
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
  - BankAccountUseExtractPVO
  - bankaccountuseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankAccountUseExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Account Use Extract. Acessa as tabelas: CE_BANK_ACCT_USES_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankAccountUseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ce_bank_acct_uses_all|CE_BANK_ACCT_USES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankAccountUsePEOApUseEnableFlag | AP_USE_ENABLE_FLAG | — | ✅ |
| 2 | BankAccountUsePEOArUseEnableFlag | AR_USE_ENABLE_FLAG | — | ✅ |
| 3 | BankAccountUsePEOBankAccountId | BANK_ACCOUNT_ID | — | ✅ |
| 4 | BankAccountUsePEOBankAcctUseId | BANK_ACCT_USE_ID | 🔑 | ✅ |
| 5 | BankAccountUsePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | BankAccountUsePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | BankAccountUsePEOEndDate | END_DATE | — | ✅ |
| 8 | BankAccountUsePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | BankAccountUsePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | BankAccountUsePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | BankAccountUsePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | BankAccountUsePEOOrgId | ORG_ID | — | ✅ |
| 13 | BankAccountUsePEOPayUseEnableFlag | PAY_USE_ENABLE_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
