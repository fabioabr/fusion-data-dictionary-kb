---
id: DOC-PO-PVO-PurchasingDocumentTypeBExtractPVO
doc_type: system-doc
title: "PurchasingDocumentTypeBExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentTypeBExtractPVO
  - purchasingdocumenttypebextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentTypeBExtractPVO

## 📌 Visão Geral

Extrai os tipos de documentos de compra configurados (pedido padrão, contrato, pedido planejado) para carga BICC, com regras de numeração e aprovação. Fundamental para governança e classificação de transações.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentTypeBExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 3 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_document_types_all_b|PO_DOCUMENT_TYPES_ALL_B]] — 14 atributos (3 PKs, 14 BICC)
- [[po_document_types_all_tl|PO_DOCUMENT_TYPES_ALL_TL]] — 6 atributos (6 BICC)

---

## ⚙️ Atributos

### [[po_document_types_all_b|PO_DOCUMENT_TYPES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentSubtype | DOCUMENT_SUBTYPE | 🔑 | ✅ |
| 2 | DocumentTypeCode | DOCUMENT_TYPE_CODE | 🔑 | ✅ |
| 3 | PODocumentTypeCoContTermsLayoutCode | CO_CONT_TERMS_LAYOUT_CODE | — | ✅ |
| 4 | PODocumentTypeCoLayoutTemplate | CO_LAYOUT_TEMPLATE | — | ✅ |
| 5 | PODocumentTypeCoTemplateId | CO_TEMPLATE_ID | — | ✅ |
| 6 | PODocumentTypeContractTemplateCode | CONTRACT_TEMPLATE_CODE | — | ✅ |
| 7 | PODocumentTypeCreatedBy | CREATED_BY | — | ✅ |
| 8 | PODocumentTypeCreationDate | CREATION_DATE | — | ✅ |
| 9 | PODocumentTypeDocumentTemplateCode | DOCUMENT_TEMPLATE_CODE | — | ✅ |
| 10 | PODocumentTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PODocumentTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PODocumentTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PODocumentTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PrcBuId | PRC_BU_ID | 🔑 | ✅ |

### [[po_document_types_all_tl|PO_DOCUMENT_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PODocumentTypeTransDocumentSubtype | DOCUMENT_SUBTYPE | — | ✅ |
| 2 | PODocumentTypeTransDocumentTypeCode | DOCUMENT_TYPE_CODE | — | ✅ |
| 3 | PODocumentTypeTransLanguage | LANGUAGE | — | ✅ |
| 4 | PODocumentTypeTransPrcBuId | PRC_BU_ID | — | ✅ |
| 5 | PODocumentTypeTransSourceLang | SOURCE_LANG | — | ✅ |
| 6 | PODocumentTypeTransTypeName | TYPE_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
