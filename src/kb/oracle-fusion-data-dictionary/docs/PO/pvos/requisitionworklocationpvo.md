---
id: DOC-PO-PVO-RequisitionWorkLocationPVO
doc_type: system-doc
title: "RequisitionWorkLocationPVO — PVO Purchasing"
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
  - RequisitionWorkLocationPVO
  - requisitionworklocationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequisitionWorkLocationPVO

## 📌 Visão Geral

Extrai os locais de trabalho específicos associados a requisições de contratação, indicando endereço físico da vaga. Suporta análise de distribuição geográfica de demanda de pessoal.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecHiringRequisitionAM.RequisitionWorkLocationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 3 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[irc_req_work_locations|IRC_REQ_WORK_LOCATIONS]] — 8 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_req_work_locations|IRC_REQ_WORK_LOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | LocationId | LOCATION_ID | 🔑 | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | RequisitionId | REQUISITION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
