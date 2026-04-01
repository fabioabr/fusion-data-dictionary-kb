---
id: DOC-OTHER-PVO-KanbanCardActivityExtractPVO
doc_type: system-doc
title: "KanbanCardActivityExtractPVO — PVO Cross-Module"
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
  - KanbanCardActivityExtractPVO
  - kanbancardactivityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KanbanCardActivityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Kanban Card Activity Extract. Acessa as tabelas: WIE_KANBAN_CARD_ACTIVITY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.KanbanCardActivityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_kanban_card_activity|WIE_KANBAN_CARD_ACTIVITY]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[wie_kanban_card_activity|WIE_KANBAN_CARD_ACTIVITY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KanbanCardActivityPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | KanbanCardActivityPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | KanbanCardActivityPEODocRef1 | DOC_REF1 | — | ✅ |
| 4 | KanbanCardActivityPEODocRef2 | DOC_REF2 | — | ✅ |
| 5 | KanbanCardActivityPEODocRef3 | DOC_REF3 | — | ✅ |
| 6 | KanbanCardActivityPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 7 | KanbanCardActivityPEOFromSupplyStatus | FROM_SUPPLY_STATUS | — | ✅ |
| 8 | KanbanCardActivityPEOInventoryItemId | INVENTORY_ITEM_ID | — | ✅ |
| 9 | KanbanCardActivityPEOKanbanActivityId | KANBAN_ACTIVITY_ID | 🔑 | ✅ |
| 10 | KanbanCardActivityPEOKanbanCardId | KANBAN_CARD_ID | — | ✅ |
| 11 | KanbanCardActivityPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | KanbanCardActivityPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | KanbanCardActivityPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | KanbanCardActivityPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | KanbanCardActivityPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | KanbanCardActivityPEOPullSequenceId | PULL_SEQUENCE_ID | — | ✅ |
| 17 | KanbanCardActivityPEOReplenishmentCycleId | REPLENISHMENT_CYCLE_ID | — | ✅ |
| 18 | KanbanCardActivityPEOToSupplyStatus | TO_SUPPLY_STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
