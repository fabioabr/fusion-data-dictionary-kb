---
id: DOC-OTHER-PVO-StandardTextTranslationExtractPVO
doc_type: system-doc
title: "StandardTextTranslationExtractPVO — PVO Cross-Module"
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
  - StandardTextTranslationExtractPVO
  - standardtexttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StandardTextTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Standard Text Translation Extract. Acessa as tabelas: AR_STANDARD_TEXT_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.StandardTextTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ar_standard_text_tl|AR_STANDARD_TEXT_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[ar_standard_text_tl|AR_STANDARD_TEXT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArStandardTextTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | ArStandardTextTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | ArStandardTextTLLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ArStandardTextTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ArStandardTextTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ArStandardTextTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ArStandardTextTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ArStandardTextTLSourceLang | SOURCE_LANG | — | ✅ |
| 9 | ArStandardTextTLStandardTextId | STANDARD_TEXT_ID | 🔑 | ✅ |
| 10 | ArStandardTextTLText | TEXT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
