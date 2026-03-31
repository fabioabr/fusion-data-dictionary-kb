---
id: DOC-OTHER-PVO-ProjectRoleTypeTranslationExtractPVO
doc_type: system-doc
title: "ProjectRoleTypeTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectRoleTypeTranslationExtractPVO
  - projectroletypetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectRoleTypeTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Role Type Translation Extract. Acessa as tabelas: PJF_PROJ_ROLE_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectRoleTypeTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_role_types_tl|PJF_PROJ_ROLE_TYPES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_role_types_tl|PJF_PROJ_ROLE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRoleTypeTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectRoleTypeTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectRoleTypeTranslationDescription | DESCRIPTION | — | ✅ |
| 4 | ProjectRoleTypeTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ProjectRoleTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectRoleTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectRoleTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectRoleTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectRoleTypeTranslationProjectRoleId | PROJECT_ROLE_ID | 🔑 | ✅ |
| 10 | ProjectRoleTypeTranslationProjectRoleName | PROJECT_ROLE_NAME | — | ✅ |
| 11 | ProjectRoleTypeTranslationSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectRoleTypeTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
