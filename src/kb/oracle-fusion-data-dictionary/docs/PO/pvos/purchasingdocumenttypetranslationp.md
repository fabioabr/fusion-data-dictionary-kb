---
id: DOC-PO-PVO-PurchasingDocumentTypeTranslationP
doc_type: system-doc
title: "PurchasingDocumentTypeTranslationP — PVO Purchasing"
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
  - PurchasingDocumentTypeTranslationP
  - purchasingdocumenttypetranslationp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentTypeTranslationP

## 📌 Visão Geral

Disponibiliza traduções de tipos de documentos de compra para operações multinacionais, assegurando exibição correta em cada localidade e idioma configurado.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingDocumentTypeTranslationP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 5 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[po_document_types_all_tl|PO_DOCUMENT_TYPES_ALL_TL]] — 12 atributos (4 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[po_document_types_all_tl|PO_DOCUMENT_TYPES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentSubtype | DOCUMENT_SUBTYPE | 🔑 | ✅ |
| 2 | DocumentTypeCode | DOCUMENT_TYPE_CODE | 🔑 | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | PODocumentTypeTransCreatedBy | CREATED_BY | — | — |
| 5 | PODocumentTypeTransCreationDate | CREATION_DATE | — | — |
| 6 | PODocumentTypeTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PODocumentTypeTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PODocumentTypeTransLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PODocumentTypeTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PODocumentTypeTransSourceLang | SOURCE_LANG | — | — |
| 11 | PODocumentTypeTransTypeName | TYPE_NAME | — | — |
| 12 | PrcBuId | PRC_BU_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
