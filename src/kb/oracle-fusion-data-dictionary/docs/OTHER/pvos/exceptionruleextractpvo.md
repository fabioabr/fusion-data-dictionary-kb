---
id: DOC-OTHER-PVO-ExceptionRuleExtractPVO
doc_type: system-doc
title: "ExceptionRuleExtractPVO — PVO Cross-Module"
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
  - ExceptionRuleExtractPVO
  - exceptionruleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExceptionRuleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Exception Rule Extract. Acessa as tabelas: AR_APP_EXCEPTION_RULES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ExceptionRuleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[ar_app_exception_rules|AR_APP_EXCEPTION_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAppExceptionRuleActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | ArAppExceptionRuleCreatedBy | CREATED_BY | — | ✅ |
| 3 | ArAppExceptionRuleCreationDate | CREATION_DATE | — | ✅ |
| 4 | ArAppExceptionRuleDescription | DESCRIPTION | — | ✅ |
| 5 | ArAppExceptionRuleEndDate | END_DATE | — | ✅ |
| 6 | ArAppExceptionRuleExceptionRuleId | EXCEPTION_RULE_ID | 🔑 | ✅ |
| 7 | ArAppExceptionRuleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ArAppExceptionRuleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ArAppExceptionRuleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ArAppExceptionRuleName | NAME | — | ✅ |
| 11 | ArAppExceptionRuleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | ArAppExceptionRuleSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | ArAppExceptionRuleSetId | SET_ID | — | ✅ |
| 14 | ArAppExceptionRuleStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
