---
id: DOC-OTHER-PVO-SubledgerApplicationExtractPVO
doc_type: system-doc
title: "SubledgerApplicationExtractPVO — PVO Cross-Module"
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
  - SubledgerApplicationExtractPVO
  - subledgerapplicationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerApplicationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Application Extract. Acessa as tabelas: XLA_SUBLEDGERS, XLA_SUBLEDGERS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerApplicationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_subledgers|XLA_SUBLEDGERS]] — 19 atributos (1 PKs, 19 BICC)
- [[xla_subledgers_tl|XLA_SUBLEDGERS_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[xla_subledgers|XLA_SUBLEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerApplicationSetupAccountingEnabled | ACCOUNTING_ENABLED | — | ✅ |
| 2 | SubledgerApplicationSetupAlcEnabledFlag | ALC_ENABLED_FLAG | — | ✅ |
| 3 | SubledgerApplicationSetupApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 4 | SubledgerApplicationSetupApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 5 | SubledgerApplicationSetupApplicationTypeCode | APPLICATION_TYPE_CODE | — | ✅ |
| 6 | SubledgerApplicationSetupControlAccountTypeCode | CONTROL_ACCOUNT_TYPE_CODE | — | ✅ |
| 7 | SubledgerApplicationSetupCreatedBy | CREATED_BY | — | ✅ |
| 8 | SubledgerApplicationSetupCreationDate | CREATION_DATE | — | ✅ |
| 9 | SubledgerApplicationSetupDrilldownProcedureName | DRILLDOWN_PROCEDURE_NAME | — | ✅ |
| 10 | SubledgerApplicationSetupImplementationModeCode | IMPLEMENTATION_MODE_CODE | — | ✅ |
| 11 | SubledgerApplicationSetupJeSourceName | JE_SOURCE_NAME | — | ✅ |
| 12 | SubledgerApplicationSetupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | SubledgerApplicationSetupLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | SubledgerApplicationSetupLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | SubledgerApplicationSetupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | SubledgerApplicationSetupRemoteUrl | REMOTE_URL | — | ✅ |
| 17 | SubledgerApplicationSetupRowLockingFlag | ROW_LOCKING_FLAG | — | ✅ |
| 18 | SubledgerApplicationSetupSecurityFunctionName | SECURITY_FUNCTION_NAME | — | ✅ |
| 19 | SubledgerApplicationSetupValuationMethodFlag | VALUATION_METHOD_FLAG | — | ✅ |

### [[xla_subledgers_tl|XLA_SUBLEDGERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SubledgerAppTransApplicationId | APPLICATION_ID | — | ✅ |
| 2 | SubledgerAppTransApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | SubledgerAppTransCreatedBy | CREATED_BY | — | ✅ |
| 4 | SubledgerAppTransCreationDate | CREATION_DATE | — | ✅ |
| 5 | SubledgerAppTransDescription | DESCRIPTION | — | ✅ |
| 6 | SubledgerAppTransLanguage | LANGUAGE | — | ✅ |
| 7 | SubledgerAppTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | SubledgerAppTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | SubledgerAppTransLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | SubledgerAppTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SubledgerAppTransSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
