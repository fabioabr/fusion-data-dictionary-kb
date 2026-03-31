---
id: DOC-PO-PVO-SupplierSpendAuthorizationRequestsPVO
doc_type: system-doc
title: "SupplierSpendAuthorizationRequestsPVO — PVO Purchasing"
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
  - SupplierSpendAuthorizationRequestsPVO
  - supplierspendauthorizationrequestspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSpendAuthorizationRequestsPVO

## 📌 Visão Geral

Extrai solicitações de autorização de gastos com fornecedores, incluindo valores, unidade de negócio e status. Permite controle de gastos emergenciais e compliance com políticas de procurement.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierSpendAuthorizationRequestsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 10 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)
- [[poz_spend_auth_requests|POZ_SPEND_AUTH_REQUESTS]] — 23 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUBusinessUnitId | BU_ID | — | — |
| 2 | BUName | BU_NAME | — | ✅ |

### [[poz_spend_auth_requests|POZ_SPEND_AUTH_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuthorizationRequestId | AUTHORIZATION_REQUEST_ID | 🔑 | ✅ |
| 2 | SupplierSpendAuthRequestApprovalInstanceId | APPROVAL_INSTANCE_ID | — | — |
| 3 | SupplierSpendAuthRequestApprovedByPersonId | APPROVED_BY_PERSON_ID | — | — |
| 4 | SupplierSpendAuthRequestApprovedDate | APPROVED_DATE | — | ✅ |
| 5 | SupplierSpendAuthRequestAuctionHeaderId | AUCTION_HEADER_ID | — | — |
| 6 | SupplierSpendAuthRequestCreationDate | CREATION_DATE | — | — |
| 7 | SupplierSpendAuthRequestCurrentFlag | CURRENT_FLAG | — | — |
| 8 | SupplierSpendAuthRequestLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupplierSpendAuthRequestLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SupplierSpendAuthRequestLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SupplierSpendAuthRequestObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | SupplierSpendAuthRequestPrcBuId | PRC_BU_ID | — | — |
| 13 | SupplierSpendAuthRequestRejectReason | REJECT_REASON | — | ✅ |
| 14 | SupplierSpendAuthRequestRejectedByPersonId | REJECTED_BY_PERSON_ID | — | — |
| 15 | SupplierSpendAuthRequestRejectedDate | REJECTED_DATE | — | — |
| 16 | SupplierSpendAuthRequestRequestNumber | REQUEST_NUMBER | — | ✅ |
| 17 | SupplierSpendAuthRequestRequestSource | REQUEST_SOURCE | — | ✅ |
| 18 | SupplierSpendAuthRequestRequestStatus | REQUEST_STATUS | — | ✅ |
| 19 | SupplierSpendAuthRequestRequestedDate | REQUESTED_DATE | — | ✅ |
| 20 | SupplierSpendAuthRequestRequesterPersonId | REQUESTER_PERSON_ID | — | — |
| 21 | SupplierSpendAuthRequestSpendAuthJustification | SPEND_AUTH_JUSTIFICATION | — | ✅ |
| 22 | SupplierSpendAuthRequestSupplierSpendAuthRequestCreatedBy | CREATED_BY | — | — |
| 23 | SupplierSpendAuthRequestVendorId | VENDOR_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
