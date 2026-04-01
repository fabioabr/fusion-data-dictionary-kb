---
id: DOC-OTHER-PVO-WOOSPActionDetailExtractPVO
doc_type: system-doc
title: "WOOSPActionDetailExtractPVO — PVO Cross-Module"
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
  - WOOSPActionDetailExtractPVO
  - woospactiondetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WOOSPActionDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WOOSPAction Detail Extract. Acessa as tabelas: WIE_WO_OSP_ACTION_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WieBiccExtractAM.WOOSPActionDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wie_wo_osp_action_details|WIE_WO_OSP_ACTION_DETAILS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[wie_wo_osp_action_details|WIE_WO_OSP_ACTION_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OSPDetailPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | OSPDetailPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | OSPDetailPEODocRef1 | DOC_REF1 | — | ✅ |
| 4 | OSPDetailPEODocRef2 | DOC_REF2 | — | ✅ |
| 5 | OSPDetailPEODocRef3 | DOC_REF3 | — | ✅ |
| 6 | OSPDetailPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 7 | OSPDetailPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | OSPDetailPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | OSPDetailPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | OSPDetailPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OSPDetailPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 12 | OSPDetailPEOQuantity | QUANTITY | — | ✅ |
| 13 | OSPDetailPEOStatus | STATUS | — | ✅ |
| 14 | OSPDetailPEOSupplierId | SUPPLIER_ID | — | ✅ |
| 15 | OSPDetailPEOSupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 16 | OSPDetailPEOWoOperationId | WO_OPERATION_ID | — | ✅ |
| 17 | OSPDetailPEOWoOspActionDetailId | WO_OSP_ACTION_DETAIL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
