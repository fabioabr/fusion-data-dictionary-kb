---
id: DOC-OTHER-PVO-LedgerSetAssignmentExtractPVO
doc_type: system-doc
title: "LedgerSetAssignmentExtractPVO — PVO Cross-Module"
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
  - LedgerSetAssignmentExtractPVO
  - ledgersetassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LedgerSetAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ledger Set Assignment Extract. Acessa as tabelas: GL_LEDGER_SET_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.LedgerSetAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_ledger_set_assignments|GL_LEDGER_SET_ASSIGNMENTS]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gl_ledger_set_assignments|GL_LEDGER_SET_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LedgerSetAsgmtCreatedBy | CREATED_BY | — | ✅ |
| 2 | LedgerSetAsgmtCreationDate | CREATION_DATE | — | ✅ |
| 3 | LedgerSetAsgmtEndDate | END_DATE | — | ✅ |
| 4 | LedgerSetAsgmtLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LedgerSetAsgmtLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LedgerSetAsgmtLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LedgerSetAsgmtLedgerId | LEDGER_ID | 🔑 | ✅ |
| 8 | LedgerSetAsgmtLedgerSetId | LEDGER_SET_ID | 🔑 | ✅ |
| 9 | LedgerSetAsgmtObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | LedgerSetAsgmtStartDate | START_DATE | — | ✅ |
| 11 | LedgerSetAsgmtStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
