---
id: DOC-OTHER-PVO-ItemTranslationExtractPVO
doc_type: system-doc
title: "ItemTranslationExtractPVO — PVO Cross-Module"
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
  - ItemTranslationExtractPVO
  - itemtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Translation Extract. Acessa as tabelas: egp_system_items_tl.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_system_items_tl|egp_system_items_tl]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[egp_system_items_tl|egp_system_items_tl]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemTranslationPEOHtmlLongDescription | HTML_LONG_DESCRIPTION | — | ✅ |
| 5 | ItemTranslationPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 6 | ItemTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ItemTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ItemTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ItemTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ItemTranslationPEOLongDescription | LONG_DESCRIPTION | — | ✅ |
| 11 | ItemTranslationPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 12 | ItemTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
