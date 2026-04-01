---
id: DOC-OTHER-PVO-AwardReferenceTranslationExtractPVO
doc_type: system-doc
title: "AwardReferenceTranslationExtractPVO — PVO Cross-Module"
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
  - AwardReferenceTranslationExtractPVO
  - awardreferencetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardReferenceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Reference Translation Extract. Acessa as tabelas: GMS_AWARD_REFERENCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardReferenceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_references_tl|GMS_AWARD_REFERENCES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_award_references_tl|GMS_AWARD_REFERENCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardReferenceTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | AwardReferenceTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | AwardReferenceTranslationId | ID | 🔑 | ✅ |
| 4 | AwardReferenceTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | AwardReferenceTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | AwardReferenceTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | AwardReferenceTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | AwardReferenceTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | AwardReferenceTranslationReferenceComment | REFERENCE_COMMENT | — | ✅ |
| 10 | AwardReferenceTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
