---
id: DOC-PO-PVO-PurchasingDocumentActionHistoryExtractPVO
doc_type: system-doc
title: "PurchasingDocumentActionHistoryExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentActionHistoryExtractPVO
  - purchasingdocumentactionhistoryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentActionHistoryExtractPVO

## 📌 Visão Geral

Extrai o histórico completo de ações em documentos de compra (aprovações, rejeições, cancelamentos, revisões) para carga BICC. Permite auditoria do ciclo de vida e análise de gargalos no fluxo de aprovação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentActionHistoryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 5 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_action_history|PO_ACTION_HISTORY]] — 22 atributos (5 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[po_action_history|PO_ACTION_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionCode | ACTION_CODE | 🔑 | ✅ |
| 2 | ActionDate | ACTION_DATE | — | ✅ |
| 3 | AssignmentDate | ASSIGNMENT_DATE | — | ✅ |
| 4 | CorrelationId | CORRELATION_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | IdentificationKey | IDENTIFICATION_KEY | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | Note | NOTE | — | ✅ |
| 12 | ObjectId | OBJECT_ID | 🔑 | ✅ |
| 13 | ObjectRevisionNum | OBJECT_REVISION_NUM | — | ✅ |
| 14 | ObjectSubTypeCode | OBJECT_SUB_TYPE_CODE | 🔑 | ✅ |
| 15 | ObjectTypeCode | OBJECT_TYPE_CODE | 🔑 | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | OfflineCode | OFFLINE_CODE | — | ✅ |
| 18 | PerformerId | PERFORMER_ID | — | ✅ |
| 19 | PoVersionId | PO_VERSION_ID | — | ✅ |
| 20 | RoleCode | ROLE_CODE | — | ✅ |
| 21 | SequenceNum | SEQUENCE_NUM | 🔑 | ✅ |
| 22 | SupplierAccessibleFlag | SUPPLIER_ACCESSIBLE_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
