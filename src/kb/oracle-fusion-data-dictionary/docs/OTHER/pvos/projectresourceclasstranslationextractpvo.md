---
id: DOC-OTHER-PVO-ProjectResourceClassTranslationExtractPVO
doc_type: system-doc
title: "ProjectResourceClassTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectResourceClassTranslationExtractPVO
  - projectresourceclasstranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceClassTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Class Translation Extract. Acessa as tabelas: PJF_RESOURCE_CLASSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceClassTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceClassTransCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceClassTransCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceClassTransDescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceClassTransLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectResourceClassTransLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceClassTransLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceClassTransLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceClassTransName | NAME | — | ✅ |
| 9 | ProjectResourceClassTransObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceClassTransResourceClassId | RESOURCE_CLASS_ID | 🔑 | ✅ |
| 11 | ProjectResourceClassTransSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
