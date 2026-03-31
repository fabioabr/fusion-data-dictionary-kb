---
id: DOC-PO-PVO-PurchasingASLPVO
doc_type: system-doc
title: "PurchasingASLPVO — PVO Purchasing"
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
  - PurchasingASLPVO
  - purchasingaslpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingASLPVO

## 📌 Visão Geral

Disponibiliza a lista de fornecedores aprovados para consulta operacional, suportando validações de sourcing e compliance na seleção de fornecedores para novas compras.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingASLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 4 | 4 | 25 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[fun_service_provider_bu_v|FUN_SERVICE_PROVIDER_BU_V]] — 4 atributos (2 PKs, 2 BICC)
- [[po_approved_supplier_list|PO_APPROVED_SUPPLIER_LIST]] — 12 atributos (1 PKs, 12 BICC)
- [[po_asl_attributes|PO_ASL_ATTRIBUTES]] — 9 atributos (9 BICC)
- [[po_asl_statuses|PO_ASL_STATUSES]] — 2 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[fun_service_provider_bu_v|FUN_SERVICE_PROVIDER_BU_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ClientBusinessUnitId | CLIENT_BU_ID | 🔑 | ✅ |
| 2 | DownstreamFunctionId | DOWNSTREAM_FUNCTION_ID | — | — |
| 3 | ServiceProviderBusinessUnitId | SERVICE_PROVIDER_BU_ID | 🔑 | ✅ |
| 4 | UpstreamFunctionId | UPSTREAM_FUNCTION_ID | — | — |

### [[po_approved_supplier_list|PO_APPROVED_SUPPLIER_LIST]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AslId | ASL_ID | 🔑 | ✅ |
| 2 | CategoryId | CATEGORY_ID | — | ✅ |
| 3 | DisableFlag | DISABLE_FLAG | — | ✅ |
| 4 | ItemId | ITEM_ID | — | ✅ |
| 5 | PrcBuId | PRC_BU_ID | — | ✅ |
| 6 | SupListCreatedBy | CREATED_BY | — | ✅ |
| 7 | SupListCreationDate | CREATION_DATE | — | ✅ |
| 8 | SupListLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupListLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | SupListUsingOrganizationId | USING_ORGANIZATION_ID | — | ✅ |
| 11 | VendorId | VENDOR_ID | — | ✅ |
| 12 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

### [[po_asl_attributes|PO_ASL_ATTRIBUTES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttrAslId | ASL_ID | — | ✅ |
| 2 | AttrCreatedBy | CREATED_BY | — | ✅ |
| 3 | AttrCreationDate | CREATION_DATE | — | ✅ |
| 4 | AttrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AttrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | AttrUsingOrganizationId | USING_ORGANIZATION_ID | — | ✅ |
| 7 | FixedLotMultiple | FIXED_LOT_MULTIPLE | — | ✅ |
| 8 | MinOrderQty | MIN_ORDER_QTY | — | ✅ |
| 9 | UomCode | UOM_CODE | — | ✅ |

### [[po_asl_statuses|PO_ASL_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Status | STATUS | — | ✅ |
| 2 | StatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
