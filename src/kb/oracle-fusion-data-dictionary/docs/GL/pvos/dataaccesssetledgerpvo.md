---
id: DOC-GL-PVO-DataAccessSetLedgerPVO
doc_type: system-doc
title: "DataAccessSetLedgerPVO — PVO General Ledger"
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
  - DataAccessSetLedgerPVO
  - dataaccesssetledgerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DataAccessSetLedgerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Data Access Set Ledger. Acessa as tabelas: GL_ACCESS_SETS, GL_ACCESS_SET_LEDGERS.

**Caminho:** `FscmTopModelAM.FinGlSharedSetupDASAM.DataAccessSetLedgerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 2 | 4 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[gl_access_sets|GL_ACCESS_SETS]] — 17 atributos (1 BICC)
- [[gl_access_set_ledgers|GL_ACCESS_SET_LEDGERS]] — 10 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[gl_access_sets|GL_ACCESS_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DataAccessSetAccessSetId | ACCESS_SET_ID | — | — |
| 2 | DataAccessSetAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 3 | DataAccessSetAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 4 | DataAccessSetChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 5 | DataAccessSetCreatedBy | CREATED_BY | — | — |
| 6 | DataAccessSetCreationDate | CREATION_DATE | — | — |
| 7 | DataAccessSetDefaultLedgerId | DEFAULT_LEDGER_ID | — | — |
| 8 | DataAccessSetDescription | DESCRIPTION | — | — |
| 9 | DataAccessSetEnabledFlag | ENABLED_FLAG | — | — |
| 10 | DataAccessSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DataAccessSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DataAccessSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | DataAccessSetName | NAME | — | — |
| 14 | DataAccessSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DataAccessSetPeriodSetName | PERIOD_SET_NAME | — | — |
| 16 | DataAccessSetSecuredSegValueSetId | SECURED_SEG_VALUE_SET_ID | — | — |
| 17 | DataAccessSetSecuritySegmentCode | SECURITY_SEGMENT_CODE | — | — |

### [[gl_access_set_ledgers|GL_ACCESS_SET_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessSetId | ACCESS_SET_ID | 🔑 | ✅ |
| 2 | DasLedgerAccessPrivilegeCode | ACCESS_PRIVILEGE_CODE | — | — |
| 3 | DasLedgerCreatedBy | CREATED_BY | — | — |
| 4 | DasLedgerCreationDate | CREATION_DATE | — | — |
| 5 | DasLedgerEndDate | END_DATE | — | — |
| 6 | DasLedgerLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DasLedgerLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DasLedgerLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DasLedgerStartDate | START_DATE | — | — |
| 10 | LedgerId | LEDGER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
