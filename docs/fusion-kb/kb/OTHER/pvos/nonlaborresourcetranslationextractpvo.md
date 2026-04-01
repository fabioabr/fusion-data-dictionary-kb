---
id: DOC-OTHER-PVO-NonLaborResourceTranslationExtractPVO
doc_type: system-doc
title: "NonLaborResourceTranslationExtractPVO — PVO Cross-Module"
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
  - NonLaborResourceTranslationExtractPVO
  - nonlaborresourcetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NonLaborResourceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Non Labor Resource Translation Extract. Acessa as tabelas: PJF_NON_LABOR_RES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.NonLaborResourceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_non_labor_res_tl|PJF_NON_LABOR_RES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NonLaborResourceTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | NonLaborResourceTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | NonLaborResourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | NonLaborResourceTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | NonLaborResourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | NonLaborResourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | NonLaborResourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | NonLaborResourceTranslationPEONlrName | NLR_NAME | — | ✅ |
| 9 | NonLaborResourceTranslationPEONonLaborResourceId | NON_LABOR_RESOURCE_ID | 🔑 | ✅ |
| 10 | NonLaborResourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | NonLaborResourceTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
