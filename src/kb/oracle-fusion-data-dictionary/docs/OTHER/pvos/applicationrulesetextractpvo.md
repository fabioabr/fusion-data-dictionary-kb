---
id: DOC-OTHER-PVO-ApplicationRuleSetExtractPVO
doc_type: system-doc
title: "ApplicationRuleSetExtractPVO — PVO Cross-Module"
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
  - ApplicationRuleSetExtractPVO
  - applicationrulesetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplicationRuleSetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Application Rule Set Extract. Acessa as tabelas: AR_APP_RULE_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.ApplicationRuleSetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[ar_app_rule_sets|AR_APP_RULE_SETS]] — 29 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ar_app_rule_sets|AR_APP_RULE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArAppRuleSetAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ArAppRuleSetAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ArAppRuleSetAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ArAppRuleSetAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ArAppRuleSetAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ArAppRuleSetAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ArAppRuleSetAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ArAppRuleSetAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ArAppRuleSetAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ArAppRuleSetAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ArAppRuleSetAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ArAppRuleSetAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ArAppRuleSetAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ArAppRuleSetAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ArAppRuleSetAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ArAppRuleSetAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ArAppRuleSetCreatedBy | CREATED_BY | — | ✅ |
| 18 | ArAppRuleSetCreationDate | CREATION_DATE | — | ✅ |
| 19 | ArAppRuleSetDescription | DESCRIPTION | — | ✅ |
| 20 | ArAppRuleSetFreezeFlag | FREEZE_FLAG | — | ✅ |
| 21 | ArAppRuleSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 22 | ArAppRuleSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 23 | ArAppRuleSetLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 24 | ArAppRuleSetModuleId | MODULE_ID | — | ✅ |
| 25 | ArAppRuleSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 26 | ArAppRuleSetRuleSetId | RULE_SET_ID | 🔑 | ✅ |
| 27 | ArAppRuleSetRuleSetName | RULE_SET_NAME | — | ✅ |
| 28 | ArAppRuleSetRuleSource | RULE_SOURCE | — | ✅ |
| 29 | ArAppRuleSetSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
