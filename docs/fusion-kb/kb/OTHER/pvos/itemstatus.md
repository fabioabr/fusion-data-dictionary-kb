---
id: DOC-OTHER-PVO-ItemStatus
doc_type: system-doc
title: "ItemStatus — PVO Cross-Module"
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
  - ItemStatus
  - itemstatus
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemStatus

## 📌 Visão Geral

View Object para extração BICC de dados de Item Status. Acessa as tabelas: EGP_ITEM_STATUS_TL.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemStatus`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 2 | 11 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_status_tl|EGP_ITEM_STATUS_TL]] — 18 atributos (2 PKs, 11 BICC)

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
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 10 | Language | LANGUAGE | 🔑 | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 16 | ProgramName | PROGRAM_NAME | — | — |
| 17 | RequestId | REQUEST_ID | — | — |
| 18 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
