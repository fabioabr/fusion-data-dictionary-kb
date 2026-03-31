---
id: DOC-PO-PVO-SourcingNegotiationStyleTranslationPVO
doc_type: system-doc
title: "SourcingNegotiationStyleTranslationPVO — PVO Purchasing"
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
  - SourcingNegotiationStyleTranslationPVO
  - sourcingnegotiationstyletranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourcingNegotiationStyleTranslationPVO

## 📌 Visão Geral

Disponibiliza traduções de estilos de negociação de sourcing, garantindo que nomes de tipos de evento (RFQ, Auction, RFP) sejam corretamente exibidos em cada idioma.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.SourcingNegotiationStyleTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 10 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[pon_negotiation_styles_tl|PON_NEGOTIATION_STYLES_TL]] — 11 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[pon_negotiation_styles_tl|PON_NEGOTIATION_STYLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | StyleId | STYLE_ID | 🔑 | ✅ |
| 11 | StyleName | STYLE_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
