---
id: DOC-OTHER-PVO-StatementCycleExtractPVO
doc_type: system-doc
title: "StatementCycleExtractPVO — PVO Cross-Module"
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
  - StatementCycleExtractPVO
  - statementcycleextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatementCycleExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Statement Cycle Extract. Acessa as tabelas: AR_STATEMENT_CYCLES.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.StatementCycleExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 1 | 1 | 13 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[ar_statement_cycles|AR_STATEMENT_CYCLES]] — 29 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ar_statement_cycles|AR_STATEMENT_CYCLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArStatementCycleAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ArStatementCycleAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ArStatementCycleAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ArStatementCycleAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ArStatementCycleAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ArStatementCycleAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ArStatementCycleAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ArStatementCycleAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ArStatementCycleAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ArStatementCycleAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ArStatementCycleAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ArStatementCycleAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ArStatementCycleAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ArStatementCycleAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ArStatementCycleAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ArStatementCycleAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ArStatementCycleCreatedBy | CREATED_BY | — | ✅ |
| 18 | ArStatementCycleCreationDate | CREATION_DATE | — | ✅ |
| 19 | ArStatementCycleDay | DAY | — | ✅ |
| 20 | ArStatementCycleDescription | DESCRIPTION | — | ✅ |
| 21 | ArStatementCycleInterval | INTERVAL | — | ✅ |
| 22 | ArStatementCycleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 23 | ArStatementCycleLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 24 | ArStatementCycleLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 25 | ArStatementCycleName | NAME | — | ✅ |
| 26 | ArStatementCycleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | ArStatementCycleRequestId | REQUEST_ID | — | ✅ |
| 28 | ArStatementCycleStatementCycleId | STATEMENT_CYCLE_ID | 🔑 | ✅ |
| 29 | ArStatementCycleStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
