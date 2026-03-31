---
id: DOC-OTHER-PVO-WorkMethodTranslationExtractPVO
doc_type: system-doc
title: "WorkMethodTranslationExtractPVO — PVO Cross-Module"
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
  - WorkMethodTranslationExtractPVO
  - workmethodtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkMethodTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Method Translation Extract. Acessa as tabelas: WIS_WORK_METHODS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WorkMethodTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_work_methods_tl|WIS_WORK_METHODS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[wis_work_methods_tl|WIS_WORK_METHODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | WorkMethodDescription | WORK_METHOD_DESCRIPTION | — | ✅ |
| 11 | WorkMethodId | WORK_METHOD_ID | 🔑 | ✅ |
| 12 | WorkMethodName | WORK_METHOD_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
