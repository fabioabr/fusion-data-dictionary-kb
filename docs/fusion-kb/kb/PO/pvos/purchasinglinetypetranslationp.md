---
id: DOC-PO-PVO-PurchasingLineTypeTranslationP
doc_type: system-doc
title: "PurchasingLineTypeTranslationP — PVO Purchasing"
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
  - PurchasingLineTypeTranslationP
  - purchasinglinetypetranslationp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingLineTypeTranslationP

## 📌 Visão Geral

Disponibiliza traduções de tipos de linha de compra para consulta, suportando equipes multilíngues na utilização correta dos formulários e relatórios de compras.

**Caminho:** `FscmTopModelAM.PrcPoPublicViewAM.PurchasingLineTypeTranslationP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 9 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[po_line_types_tl|PO_LINE_TYPES_TL]] — 11 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[po_line_types_tl|PO_LINE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | LineTypeId | LINE_TYPE_ID | 🔑 | ✅ |
| 3 | POLineTypeTransCreatedBy | CREATED_BY | — | ✅ |
| 4 | POLineTypeTransCreationDate | CREATION_DATE | — | ✅ |
| 5 | POLineTypeTransDescription | DESCRIPTION | — | ✅ |
| 6 | POLineTypeTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | POLineTypeTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | POLineTypeTransLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | POLineTypeTransLineType | LINE_TYPE | — | ✅ |
| 10 | POLineTypeTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | POLineTypeTransSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
