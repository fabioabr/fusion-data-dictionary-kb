---
id: DOC-OTHER-PVO-BankStatementLineChargesExtractPVO
doc_type: system-doc
title: "BankStatementLineChargesExtractPVO — PVO Cross-Module"
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
  - BankStatementLineChargesExtractPVO
  - bankstatementlinechargesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BankStatementLineChargesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bank Statement Line Charges Extract. Acessa as tabelas: CE_STMT_LINE_CHARGES.

**Caminho:** `FscmTopModelAM.FinExtractAM.CeBiccExtractAM.BankStatementLineChargesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ce_stmt_line_charges|CE_STMT_LINE_CHARGES]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[ce_stmt_line_charges|CE_STMT_LINE_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BankStatementLineChargesChargePercentRate | CHARGE_PERCENT_RATE | — | ✅ |
| 2 | BankStatementLineChargesChargeServiceCode | CHARGE_SERVICE_CODE | — | ✅ |
| 3 | BankStatementLineChargesChargesAmt | CHARGES_AMT | — | ✅ |
| 4 | BankStatementLineChargesChargesCurr | CHARGES_CURR | — | ✅ |
| 5 | BankStatementLineChargesCreatedBy | CREATED_BY | — | ✅ |
| 6 | BankStatementLineChargesCreationDate | CREATION_DATE | — | ✅ |
| 7 | BankStatementLineChargesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | BankStatementLineChargesLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | BankStatementLineChargesLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | BankStatementLineChargesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | BankStatementLineChargesStatementLineId | STATEMENT_LINE_ID | — | ✅ |
| 12 | BankStatementLineChargesStmtLineChargesId | STMT_LINE_CHARGES_ID | 🔑 | ✅ |
| 13 | BankStatementLineChargesTaxAmount | TAX_AMOUNT | — | ✅ |
| 14 | BankStatementLineChargesTaxCurr | TAX_CURR | — | ✅ |
| 15 | BankStatementLineChargesTaxId | TAX_ID | — | ✅ |
| 16 | BankStatementLineChargesTaxRate | TAX_RATE | — | ✅ |
| 17 | BankStatementLineChargesTrxChargeBearerCode | TRX_CHARGE_BEARER_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
