---
id: DOC-OTHER-PVO-ReferenceTranslationExtractPVO
doc_type: system-doc
title: "ReferenceTranslationExtractPVO — PVO Cross-Module"
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
  - ReferenceTranslationExtractPVO
  - referencetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reference Translation Extract. Acessa as tabelas: GMS_REFERENCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.ReferenceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_references_tl|GMS_REFERENCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_references_tl|GMS_REFERENCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | ReferenceTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | ReferenceTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ReferenceTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ReferenceTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ReferenceTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ReferenceTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ReferenceTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ReferenceTranslationReferenceId | REFERENCE_ID | 🔑 | ✅ |
| 10 | ReferenceTranslationReferenceName | REFERENCE_NAME | — | ✅ |
| 11 | ReferenceTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
