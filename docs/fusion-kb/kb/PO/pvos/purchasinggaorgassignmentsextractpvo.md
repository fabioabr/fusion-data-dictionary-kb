---
id: DOC-PO-PVO-PurchasingGaOrgAssignmentsExtractPVO
doc_type: system-doc
title: "PurchasingGaOrgAssignmentsExtractPVO — PVO Purchasing"
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
  - PurchasingGaOrgAssignmentsExtractPVO
  - purchasinggaorgassignmentsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingGaOrgAssignmentsExtractPVO

## 📌 Visão Geral

Extrai as atribuições organizacionais de Global Agreements para carga BICC, mapeando quais unidades de negócio podem utilizar cada acordo global de compra.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingGaOrgAssignmentsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_ga_org_assignments|PO_GA_ORG_ASSIGNMENTS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[po_ga_org_assignments|PO_GA_ORG_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 2 | BilltoBuId | BILLTO_BU_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | OrderedLocallyFlag | ORDERED_LOCALLY_FLAG | — | ✅ |
| 11 | OrgAssignmentId | ORG_ASSIGNMENT_ID | 🔑 | ✅ |
| 12 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 13 | PrcBuId | PRC_BU_ID | — | ✅ |
| 14 | ReqBuId | REQ_BU_ID | — | ✅ |
| 15 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 16 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
