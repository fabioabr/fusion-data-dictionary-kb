---
id: DOC-PO-PVO-PeriodStatusExtractPVO
doc_type: system-doc
title: "PeriodStatusExtractPVO — PVO Purchasing"
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
  - PeriodStatusExtractPVO
  - periodstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PeriodStatusExtractPVO

## 📌 Visão Geral

Extrai o status de períodos contábeis (aberto, fechado, pendente) para o módulo de sustentabilidade. Essencial para controle de lançamentos e encerramento contábil de métricas ESG.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.PeriodStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_period_statuses|SUS_PERIOD_STATUSES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[sus_period_statuses|SUS_PERIOD_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjustmentPeriodFlag | ADJUSTMENT_PERIOD_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDate | END_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LedgerId | LEDGER_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PeriodId | PERIOD_ID | 🔑 | ✅ |
| 11 | PeriodName | PERIOD_NAME | — | ✅ |
| 12 | PeriodNum | PERIOD_NUM | — | ✅ |
| 13 | PeriodStatusCode | PERIOD_STATUS_CODE | — | ✅ |
| 14 | PeriodType | PERIOD_TYPE | — | ✅ |
| 15 | PeriodYear | PERIOD_YEAR | — | ✅ |
| 16 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
