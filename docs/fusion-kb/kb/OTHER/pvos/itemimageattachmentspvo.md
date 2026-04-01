---
id: DOC-OTHER-PVO-ItemImageAttachmentsPVO
doc_type: system-doc
title: "ItemImageAttachmentsPVO — PVO Cross-Module"
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
  - ItemImageAttachmentsPVO
  - itemimageattachmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemImageAttachmentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Image Attachments. Acessa as tabelas: FND_ATTACHED_DOCUMENTS, FND_DOCUMENTS_VL.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemImageAttachmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 2 | 2 | 12 | 86% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]] — 8 atributos (1 PKs, 7 BICC)
- [[fnd_documents_vl|FND_DOCUMENTS_VL]] — 6 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttachedBy | LAST_UPDATED_BY | — | ✅ |
| 2 | AttachedDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | AttachedDocumentId | ATTACHED_DOCUMENT_ID | 🔑 | ✅ |
| 4 | CategoryName | CATEGORY_NAME | — | ✅ |
| 5 | EntityName | ENTITY_NAME | — | — |
| 6 | Pk1Value | PK1_VALUE | — | ✅ |
| 7 | Pk2Value | PK2_VALUE | — | ✅ |
| 8 | PrimaryCategoryFlag | PRIMARY_CATEGORY_FLAG | — | ✅ |

### [[fnd_documents_vl|FND_DOCUMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DatatypeCode | DATATYPE_CODE | — | — |
| 2 | Description | DESCRIPTION | — | ✅ |
| 3 | DmFolderPath | DM_FOLDER_PATH | — | ✅ |
| 4 | DocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 5 | Title | TITLE | — | ✅ |
| 6 | Type | DATATYPE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
