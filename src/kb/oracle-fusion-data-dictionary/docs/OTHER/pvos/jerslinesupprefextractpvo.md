---
id: DOC-OTHER-PVO-JersLineSuppRefExtractPVO
doc_type: system-doc
title: "JersLineSuppRefExtractPVO — PVO Cross-Module"
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
  - JersLineSuppRefExtractPVO
  - jerslinesupprefextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JersLineSuppRefExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Jers Line Supp Ref Extract. Acessa as tabelas: XLA_JERS_SR_LINE_ASSGNS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.JersLineSuppRefExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 10 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_jers_sr_line_assgns|XLA_JERS_SR_LINE_ASSGNS]] — 18 atributos (10 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[xla_jers_sr_line_assgns|XLA_JERS_SR_LINE_ASSGNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JersLineSuppRefAccountingLineCode | ACCOUNTING_LINE_CODE | 🔑 | ✅ |
| 2 | JersLineSuppRefAccountingLineTypeCode | ACCOUNTING_LINE_TYPE_CODE | 🔑 | ✅ |
| 3 | JersLineSuppRefAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 4 | JersLineSuppRefAnalyticalCriterionCode | ANALYTICAL_CRITERION_CODE | 🔑 | ✅ |
| 5 | JersLineSuppRefAnalyticalCriterionTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | 🔑 | ✅ |
| 6 | JersLineSuppRefApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 7 | JersLineSuppRefCreatedBy | CREATED_BY | — | ✅ |
| 8 | JersLineSuppRefCreationDate | CREATION_DATE | — | ✅ |
| 9 | JersLineSuppRefEventClassCode | EVENT_CLASS_CODE | 🔑 | ✅ |
| 10 | JersLineSuppRefEventTypeCode | EVENT_TYPE_CODE | 🔑 | ✅ |
| 11 | JersLineSuppRefJersCode | JERS_CODE | 🔑 | ✅ |
| 12 | JersLineSuppRefJersTypeCode | JERS_TYPE_CODE | 🔑 | ✅ |
| 13 | JersLineSuppRefLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | JersLineSuppRefLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | JersLineSuppRefLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | JersLineSuppRefLnSrAssgnId | LN_SR_ASSGN_ID | — | ✅ |
| 17 | JersLineSuppRefObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | JersLineSuppRefSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
