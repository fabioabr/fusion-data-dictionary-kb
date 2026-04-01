---
id: DOC-OTHER-PVO-ProjectSprintExtractPVO
doc_type: system-doc
title: "ProjectSprintExtractPVO — PVO Cross-Module"
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
  - ProjectSprintExtractPVO
  - projectsprintextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectSprintExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Sprint Extract. Acessa as tabelas: PJT_SPRINT_B, PJT_SPRINT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectSprintExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_sprint_b|PJT_SPRINT_B]] — 10 atributos (1 PKs, 10 BICC)
- [[pjt_sprint_tl|PJT_SPRINT_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjt_sprint_b|PJT_SPRINT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtSprintBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtSprintBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtSprintBasePEOEndDate | END_DATE | — | ✅ |
| 4 | PjtSprintBasePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | PjtSprintBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PjtSprintBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PjtSprintBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PjtSprintBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PjtSprintBasePEOSprintId | SPRINT_ID | 🔑 | ✅ |
| 10 | PjtSprintBasePEOStartDate | START_DATE | — | ✅ |

### [[pjt_sprint_tl|PJT_SPRINT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtSprintTranslationEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtSprintTranslationEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtSprintTranslationEOLanguage | LANGUAGE | — | ✅ |
| 4 | PjtSprintTranslationEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PjtSprintTranslationEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PjtSprintTranslationEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PjtSprintTranslationEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PjtSprintTranslationEOSourceLang | SOURCE_LANG | — | ✅ |
| 9 | PjtSprintTranslationEOSprintDesc | SPRINT_DESC | — | ✅ |
| 10 | PjtSprintTranslationEOSprintId | SPRINT_ID | — | ✅ |
| 11 | PjtSprintTranslationEOSprintName | SPRINT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
