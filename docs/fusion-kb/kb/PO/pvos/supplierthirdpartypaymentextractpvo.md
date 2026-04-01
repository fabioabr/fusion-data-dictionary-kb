---
id: DOC-PO-PVO-SupplierThirdPartyPaymentExtractPVO
doc_type: system-doc
title: "SupplierThirdPartyPaymentExtractPVO — PVO Purchasing"
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
  - SupplierThirdPartyPaymentExtractPVO
  - supplierthirdpartypaymentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierThirdPartyPaymentExtractPVO

## 📌 Visão Geral

Extrai configurações de pagamento a terceiros (factoring, cessão de crédito) para carga BICC, onde pagamentos são redirecionados a entidades diferentes do fornecedor. Essencial para compliance.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierThirdPartyPaymentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_sup_thirdparty_payment_rel|POZ_SUP_THIRDPARTY_PAYMENT_REL]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[poz_sup_thirdparty_payment_rel|POZ_SUP_THIRDPARTY_PAYMENT_REL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DefaultRelationshipFlag | DEFAULT_RELATIONSHIP_FLAG | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | FromDate | FROM_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RemitToAddressId | REMIT_TO_ADDRESS_ID | — | ✅ |
| 11 | RemitToSupplierId | REMIT_TO_SUPPLIER_ID | — | ✅ |
| 12 | ToDate | TO_DATE | — | ✅ |
| 13 | TppRelationshipId | TPP_RELATIONSHIP_ID | 🔑 | ✅ |
| 14 | VendorSiteId | VENDOR_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
