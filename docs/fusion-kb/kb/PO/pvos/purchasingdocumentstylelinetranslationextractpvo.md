---
id: DOC-PO-PVO-PurchasingDocumentStyleLineTranslationExtractPVO
doc_type: system-doc
title: "PurchasingDocumentStyleLineTranslationExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentStyleLineTranslationExtractPVO
  - purchasingdocumentstylelinetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentStyleLineTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções dos estilos de linha de documento de compra para múltiplos idiomas. Garante que rótulos e descrições dos campos de formulário sejam localizados corretamente.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentStyleLineTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_doc_style_lines_tl|PO_DOC_STYLE_LINES_TL]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[po_doc_style_lines_tl|PO_DOC_STYLE_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentSubtype | DOCUMENT_SUBTYPE | 🔑 | ✅ |
| 2 | Language | LANGUAGE | 🔑 | ✅ |
| 3 | PODocumentStyleLineTransCreatedBy | CREATED_BY | — | ✅ |
| 4 | PODocumentStyleLineTransCreationDate | CREATION_DATE | — | ✅ |
| 5 | PODocumentStyleLineTransDisplayName | DISPLAY_NAME | — | ✅ |
| 6 | PODocumentStyleLineTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PODocumentStyleLineTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PODocumentStyleLineTransLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PODocumentStyleLineTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PODocumentStyleLineTransSourceLang | SOURCE_LANG | — | ✅ |
| 11 | StyleId | STYLE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
