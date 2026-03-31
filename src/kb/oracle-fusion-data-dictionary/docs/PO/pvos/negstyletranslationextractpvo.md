---
id: DOC-PO-PVO-NegStyleTranslationExtractPVO
doc_type: system-doc
title: "NegStyleTranslationExtractPVO — PVO Purchasing"
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
  - NegStyleTranslationExtractPVO
  - negstyletranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegStyleTranslationExtractPVO

## 📌 Visão Geral

Extrai traduções de estilos de negociação para múltiplos idiomas. Garante que nomes e descrições dos tipos de evento de sourcing sejam exibidos corretamente em cada localidade.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegStyleTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_negotiation_styles_tl|PON_NEGOTIATION_STYLES_TL]] — 11 atributos (2 PKs, 11 BICC)

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
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | StyleId | STYLE_ID | 🔑 | ✅ |
| 11 | StyleName | STYLE_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
