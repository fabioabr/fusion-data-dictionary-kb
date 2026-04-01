---
id: DOC-PO-PVO-NegStyleDocTypeTranslationExtractPVO
doc_type: system-doc
title: "NegStyleDocTypeTranslationExtractPVO — PVO Purchasing"
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
  - NegStyleDocTypeTranslationExtractPVO
  - negstyledoctypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegStyleDocTypeTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções de tipos de documentos por estilo de negociação para carga BICC. Alimenta o data warehouse com terminologia multilíngue de configurações de sourcing.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegStyleDocTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 3 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_doctype_styles_tl|PON_DOCTYPE_STYLES_TL]] — 17 atributos (3 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[pon_doctype_styles_tl|PON_DOCTYPE_STYLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CoverPageText | COVER_PAGE_TEXT | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DoctypeId | DOCTYPE_ID | 🔑 | ✅ |
| 5 | IntroductionText | INTRODUCTION_TEXT | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | LinesText | LINES_TEXT | — | ✅ |
| 11 | NegotiationDisplayName | NEGOTIATION_DISPLAY_NAME | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | RequirementsText | REQUIREMENTS_TEXT | — | ✅ |
| 14 | ResponseDisplayName | RESPONSE_DISPLAY_NAME | — | ✅ |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |
| 16 | StyleId | STYLE_ID | 🔑 | ✅ |
| 17 | TermsText | TERMS_TEXT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
