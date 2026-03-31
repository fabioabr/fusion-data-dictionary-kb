---
id: DOC-OTHER-PVO-CashGenUnitExtractPVO
doc_type: system-doc
title: "CashGenUnitExtractPVO — PVO Cross-Module"
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
  - CashGenUnitExtractPVO
  - cashgenunitextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CashGenUnitExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cash Gen Unit Extract. Acessa as tabelas: FA_CASH_GEN_UNITS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.CashGenUnitExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_cash_gen_units|FA_CASH_GEN_UNITS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fa_cash_gen_units|FA_CASH_GEN_UNITS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CashGenUnitBookTypeCode | BOOK_TYPE_CODE | — | ✅ |
| 2 | CashGenUnitCashGeneratingUnit | CASH_GENERATING_UNIT | — | ✅ |
| 3 | CashGenUnitCashGeneratingUnitId | CASH_GENERATING_UNIT_ID | 🔑 | ✅ |
| 4 | CashGenUnitCreatedBy | CREATED_BY | — | ✅ |
| 5 | CashGenUnitCreationDate | CREATION_DATE | — | ✅ |
| 6 | CashGenUnitDescription | DESCRIPTION | — | ✅ |
| 7 | CashGenUnitDisabledFlag | DISABLED_FLAG | — | ✅ |
| 8 | CashGenUnitLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | CashGenUnitLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | CashGenUnitLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | CashGenUnitObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
