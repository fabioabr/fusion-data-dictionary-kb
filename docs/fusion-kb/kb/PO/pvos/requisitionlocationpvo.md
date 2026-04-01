---
id: DOC-PO-PVO-RequisitionLocationPVO
doc_type: system-doc
title: "RequisitionLocationPVO — PVO Purchasing"
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
  - RequisitionLocationPVO
  - requisitionlocationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionLocationPVO

## 📌 Visão Geral

Extrai os locais de trabalho associados a requisições de contratação, indicando onde a vaga será preenchida. Suporta análise de demanda por localidade e planejamento de workforce.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionLocationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[irc_req_locations|IRC_REQ_LOCATIONS]] — 9 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_req_locations|IRC_REQ_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | GeographyId | GEOGRAPHY_ID | 🔑 | ✅ |
| 4 | GeographyNodeId | GEOGRAPHY_NODE_ID | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
