---
id: DOC-PO-PVO-NegotiationStyleDocumentTypeVLPVO
doc_type: system-doc
title: "NegotiationStyleDocumentTypeVLPVO — PVO Purchasing"
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
  - NegotiationStyleDocumentTypeVLPVO
  - negotiationstyledocumenttypevlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationStyleDocumentTypeVLPVO

## 📌 Visão Geral

Extrai a lista de valores (Value List) dos tipos de documentos por estilo de negociação. Suporta validação de configurações e consistência do setup de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationStyleDocumentTypeVLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 2 | 3 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[pon_doctype_styles_vl|PON_DOCTYPE_STYLES_VL]] — 16 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pon_doctype_styles_vl|PON_DOCTYPE_STYLES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegStyleDocTypeVLPEOCoverPageText | COVER_PAGE_TEXT | — | — |
| 2 | NegStyleDocTypeVLPEOCreatedBy | CREATED_BY | — | — |
| 3 | NegStyleDocTypeVLPEOCreationDate | CREATION_DATE | — | — |
| 4 | NegStyleDocTypeVLPEODoctypeId | DOCTYPE_ID | 🔑 | — |
| 5 | NegStyleDocTypeVLPEOEnabledFlag | ENABLED_FLAG | — | — |
| 6 | NegStyleDocTypeVLPEOIntroductionText | INTRODUCTION_TEXT | — | — |
| 7 | NegStyleDocTypeVLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 8 | NegStyleDocTypeVLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | NegStyleDocTypeVLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | NegStyleDocTypeVLPEOLinesText | LINES_TEXT | — | — |
| 11 | NegStyleDocTypeVLPEONegotiationDisplayName | NEGOTIATION_DISPLAY_NAME | — | ✅ |
| 12 | NegStyleDocTypeVLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | NegStyleDocTypeVLPEORequirementsText | REQUIREMENTS_TEXT | — | — |
| 14 | NegStyleDocTypeVLPEOResponseDisplayName | RESPONSE_DISPLAY_NAME | — | — |
| 15 | NegStyleDocTypeVLPEOStyleId | STYLE_ID | 🔑 | ✅ |
| 16 | NegStyleDocTypeVLPEOTermsText | TERMS_TEXT | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
