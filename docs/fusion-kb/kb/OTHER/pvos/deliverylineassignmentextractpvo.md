---
id: DOC-OTHER-PVO-DeliveryLineAssignmentExtractPVO
doc_type: system-doc
title: "DeliveryLineAssignmentExtractPVO — PVO Cross-Module"
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
  - DeliveryLineAssignmentExtractPVO
  - deliverylineassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeliveryLineAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Delivery Line Assignment Extract. Acessa as tabelas: WSH_DELIVERY_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WshBiccExtractAM.DeliveryLineAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wsh_delivery_assignments|WSH_DELIVERY_ASSIGNMENTS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[wsh_delivery_assignments|WSH_DELIVERY_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeliveryLineAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DeliveryLineAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DeliveryLineAssignmentPEODeliveryAssignmentId | DELIVERY_ASSIGNMENT_ID | 🔑 | ✅ |
| 4 | DeliveryLineAssignmentPEODeliveryDetailId | DELIVERY_DETAIL_ID | — | ✅ |
| 5 | DeliveryLineAssignmentPEODeliveryId | DELIVERY_ID | — | ✅ |
| 6 | DeliveryLineAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DeliveryLineAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | DeliveryLineAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | DeliveryLineAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | DeliveryLineAssignmentPEORequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
