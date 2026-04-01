---
id: DOC-OTHER-PVO-ItemStatusExtractPVO
doc_type: system-doc
title: "ItemStatusExtractPVO — PVO Cross-Module"
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
  - ItemStatusExtractPVO
  - itemstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Status Extract. Acessa as tabelas: EGP_ITEM_STATUS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_status_tl|EGP_ITEM_STATUS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[egp_item_status_tl|EGP_ITEM_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | DisableDate | DISABLE_DATE | — | ✅ |
| 5 | InventoryItemStatusCode | INVENTORY_ITEM_STATUS_CODE | 🔑 | ✅ |
| 6 | InventoryItemStatusId | INVENTORY_ITEM_STATUS_ID | — | ✅ |
| 7 | InventoryItemStatusName | INVENTORY_ITEM_STATUS_NAME | — | ✅ |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
