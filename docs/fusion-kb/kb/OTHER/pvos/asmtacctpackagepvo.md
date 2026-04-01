---
id: DOC-OTHER-PVO-AsmtAcctPackagePVO
doc_type: system-doc
title: "AsmtAcctPackagePVO — PVO Cross-Module"
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
  - AsmtAcctPackagePVO
  - asmtacctpackagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AsmtAcctPackagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asmt Acct Package. Acessa as tabelas: IRC_ASMT_ACCT_PACKAGES, IRC_TP_PARTNER_ACCOUNTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecAssessmentsAM.AsmtAcctPackagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 2 | 1 | 10 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[irc_asmt_acct_packages|IRC_ASMT_ACCT_PACKAGES]] — 12 atributos (1 PKs, 10 BICC)
- [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]] — 4 atributos

---

## ⚙️ Atributos

### [[irc_asmt_acct_packages|IRC_ASMT_ACCT_PACKAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccountPackageId | ACCOUNT_PACKAGE_ID | 🔑 | ✅ |
| 2 | AsmtAcctPackagePEOAccountId | ACCOUNT_ID | — | ✅ |
| 3 | AsmtAcctPackagePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AsmtAcctPackagePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AsmtAcctPackagePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AsmtAcctPackagePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | AsmtAcctPackagePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AsmtAcctPackagePEOObjectStatus | OBJECT_STATUS | — | ✅ |
| 9 | AsmtAcctPackagePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AsmtAcctPackagePEOPackageCode | PACKAGE_CODE | — | ✅ |
| 11 | AsmtAcctPackagePEOPackageDesc | PACKAGE_DESC | — | ✅ |
| 12 | AsmtAcctPackagePEOPackageName | PACKAGE_NAME | — | ✅ |

### [[irc_tp_partner_accounts|IRC_TP_PARTNER_ACCOUNTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartnerAccountPEOAccountId | ACCOUNT_ID | — | — |
| 2 | PartnerAccountPEODescription | DESCRIPTION | — | — |
| 3 | PartnerAccountPEOProvisioningId | PROVISIONING_ID | — | — |
| 4 | PartnerAccountPEOUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
