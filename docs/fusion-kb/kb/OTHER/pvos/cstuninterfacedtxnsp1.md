---
id: DOC-OTHER-PVO-CstUninterfacedTxnsP1
doc_type: system-doc
title: "CstUninterfacedTxnsP1 — PVO Cross-Module"
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
  - CstUninterfacedTxnsP1
  - cstuninterfacedtxnsp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstUninterfacedTxnsP1

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Uninterfaced Txns P1. Acessa as tabelas: CST_UNINTF_TXNS_PIVOT_V.

**Caminho:** `FscmTopModelAM.CstPeriodStatusAM.CstUninterfacedTxnsP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 4 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_unintf_txns_pivot_v|CST_UNINTF_TXNS_PIVOT_V]] — 8 atributos (4 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_unintf_txns_pivot_v|CST_UNINTF_TXNS_PIVOT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CostBookId | COST_BOOK_ID | 🔑 | ✅ |
| 2 | CostOrgId | COST_ORG_ID | 🔑 | ✅ |
| 3 | CstUninterfacedTxnsPEOPendingApIntfCount | PENDING_AP_INTF_COUNT | — | ✅ |
| 4 | CstUninterfacedTxnsPEOPendingInvIntfCount | PENDING_INV_INTF_COUNT | — | ✅ |
| 5 | CstUninterfacedTxnsPEOPendingMfgIntfCount | PENDING_MFG_INTF_COUNT | — | ✅ |
| 6 | CstUninterfacedTxnsPEOPendingRevIntfCount | PENDING_REV_INTF_COUNT | — | ✅ |
| 7 | PeriodName | PERIOD_NAME | 🔑 | ✅ |
| 8 | RequestId | REQUEST_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
