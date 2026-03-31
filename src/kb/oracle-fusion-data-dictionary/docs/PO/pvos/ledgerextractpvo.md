---
id: DOC-PO-PVO-LedgerExtractPVO
doc_type: system-doc
title: "LedgerExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - LedgerExtractPVO
  - ledgerextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerExtractPVO

## 📌 Visão Geral

Extrai dados de ledger (razão contábil) associados ao módulo de sustentabilidade em procurement, com configurações e períodos. Fundamental para contabilização e reporting financeiro de métricas ESG.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.LedgerExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_ledgers|SUS_LEDGERS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[sus_ledgers|SUS_LEDGERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | FirstLedgerPeriodName | FIRST_LEDGER_PERIOD_NAME | — | ✅ |
| 5 | GlCalendarId | GL_CALENDAR_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 10 | LedgerName | LEDGER_NAME | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
