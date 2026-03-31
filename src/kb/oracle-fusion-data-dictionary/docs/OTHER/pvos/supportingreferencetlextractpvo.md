---
id: DOC-OTHER-PVO-SupportingReferenceTLExtractPVO
doc_type: system-doc
title: "SupportingReferenceTLExtractPVO — PVO Cross-Module"
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
  - SupportingReferenceTLExtractPVO
  - supportingreferencetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupportingReferenceTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supporting Reference TLExtract. Acessa as tabelas: XLA_ANALYTICAL_HDRS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SupportingReferenceTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 4 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_analytical_hdrs_tl|XLA_ANALYTICAL_HDRS_TL]] — 13 atributos (4 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[xla_analytical_hdrs_tl|XLA_ANALYTICAL_HDRS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupportingReferenceTranslationAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | SupportingReferenceTranslationAnalyticalCriterionCode | ANALYTICAL_CRITERION_CODE | 🔑 | ✅ |
| 3 | SupportingReferenceTranslationAnalyticalCriterionTypeCode | ANALYTICAL_CRITERION_TYPE_CODE | 🔑 | ✅ |
| 4 | SupportingReferenceTranslationCreatedBy | CREATED_BY | — | ✅ |
| 5 | SupportingReferenceTranslationCreationDate | CREATION_DATE | — | ✅ |
| 6 | SupportingReferenceTranslationDescription | DESCRIPTION | — | ✅ |
| 7 | SupportingReferenceTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | SupportingReferenceTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | SupportingReferenceTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | SupportingReferenceTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | SupportingReferenceTranslationName | NAME | — | ✅ |
| 12 | SupportingReferenceTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SupportingReferenceTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
