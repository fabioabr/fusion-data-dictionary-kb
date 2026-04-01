---
id: DOC-GL-PVO-BalanceValidationPVO
doc_type: system-doc
title: "BalanceValidationPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BalanceValidationPVO
  - balancevalidationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceValidationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Validation. Acessa as tabelas: PAY_BALANCE_VALIDATION.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBalancesSetupAM.BalanceValidationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[pay_balance_validation|PAY_BALANCE_VALIDATION]] — 11 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_balance_validation|PAY_BALANCE_VALIDATION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceValidationPEOBalanceLoadDate | BALANCE_LOAD_DATE | — | — |
| 2 | BalanceValidationPEOBalanceValidationId | BALANCE_VALIDATION_ID | 🔑 | ✅ |
| 3 | BalanceValidationPEOCreatedBy | CREATED_BY | — | — |
| 4 | BalanceValidationPEOCreationDate | CREATION_DATE | — | — |
| 5 | BalanceValidationPEODefinedBalanceId | DEFINED_BALANCE_ID | — | — |
| 6 | BalanceValidationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BalanceValidationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | BalanceValidationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | BalanceValidationPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 10 | BalanceValidationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BalanceValidationPEORunBalanceStatus | RUN_BALANCE_STATUS | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
