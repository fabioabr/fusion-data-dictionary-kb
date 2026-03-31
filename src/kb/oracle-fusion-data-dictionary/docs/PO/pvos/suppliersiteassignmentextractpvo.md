---
id: DOC-PO-PVO-SupplierSiteAssignmentExtractPVO
doc_type: system-doc
title: "SupplierSiteAssignmentExtractPVO — PVO Purchasing"
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
  - SupplierSiteAssignmentExtractPVO
  - suppliersiteassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSiteAssignmentExtractPVO

## 📌 Visão Geral

Extrai as atribuições de sites de fornecedores a unidades de negócio para carga BICC. Determina quais locais de fornecimento estão disponíveis para cada entidade compradora.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierSiteAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_site_assignments_all_m|POZ_SITE_ASSIGNMENTS_ALL_M]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[poz_site_assignments_all_m|POZ_SITE_ASSIGNMENTS_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcctsPayCodeCombinationId | ACCTS_PAY_CODE_COMBINATION_ID | — | ✅ |
| 2 | AllowAwtFlag | ALLOW_AWT_FLAG | — | ✅ |
| 3 | AssignmentId | ASSIGNMENT_ID | 🔑 | ✅ |
| 4 | AwtGroupId | AWT_GROUP_ID | — | ✅ |
| 5 | BillToBuId | BILL_TO_BU_ID | — | ✅ |
| 6 | BillToLocationId | BILL_TO_LOCATION_ID | — | ✅ |
| 7 | BuId | BU_ID | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | DistributionSetId | DISTRIBUTION_SET_ID | — | ✅ |
| 11 | FutureDatedPaymentCcid | FUTURE_DATED_PAYMENT_CCID | — | ✅ |
| 12 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | PrepayCodeCombinationId | PREPAY_CODE_COMBINATION_ID | — | ✅ |
| 18 | ShipToLocationId | SHIP_TO_LOCATION_ID | — | ✅ |
| 19 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
