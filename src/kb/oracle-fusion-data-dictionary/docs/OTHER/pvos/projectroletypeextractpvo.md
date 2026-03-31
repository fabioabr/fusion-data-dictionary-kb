---
id: DOC-OTHER-PVO-ProjectRoleTypeExtractPVO
doc_type: system-doc
title: "ProjectRoleTypeExtractPVO — PVO Cross-Module"
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
  - ProjectRoleTypeExtractPVO
  - projectroletypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectRoleTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Role Type Extract. Acessa as tabelas: PJF_PROJ_ROLE_TYPES_B, PJF_PROJ_ROLE_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectRoleTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 2 | 1 | 29 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_proj_role_types_b|PJF_PROJ_ROLE_TYPES_B]] — 33 atributos (1 PKs, 17 BICC)
- [[pjf_proj_role_types_tl|PJF_PROJ_ROLE_TYPES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjf_proj_role_types_b|PJF_PROJ_ROLE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRoleTypeBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ProjectRoleTypeBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ProjectRoleTypeBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ProjectRoleTypeBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ProjectRoleTypeBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ProjectRoleTypeBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ProjectRoleTypeBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ProjectRoleTypeBaseAttribute2 | ATTRIBUTE2 | — | — |
| 9 | ProjectRoleTypeBaseAttribute3 | ATTRIBUTE3 | — | — |
| 10 | ProjectRoleTypeBaseAttribute4 | ATTRIBUTE4 | — | — |
| 11 | ProjectRoleTypeBaseAttribute5 | ATTRIBUTE5 | — | — |
| 12 | ProjectRoleTypeBaseAttribute6 | ATTRIBUTE6 | — | — |
| 13 | ProjectRoleTypeBaseAttribute7 | ATTRIBUTE7 | — | — |
| 14 | ProjectRoleTypeBaseAttribute8 | ATTRIBUTE8 | — | — |
| 15 | ProjectRoleTypeBaseAttribute9 | ATTRIBUTE9 | — | — |
| 16 | ProjectRoleTypeBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | ProjectRoleTypeBaseCreatedBy | CREATED_BY | — | ✅ |
| 18 | ProjectRoleTypeBaseCreationDate | CREATION_DATE | — | ✅ |
| 19 | ProjectRoleTypeBaseDefaultHrJobId | DEFAULT_HR_JOB_ID | — | ✅ |
| 20 | ProjectRoleTypeBaseDefaultMaxHrJobLevel | DEFAULT_MAX_HR_JOB_LEVEL | — | ✅ |
| 21 | ProjectRoleTypeBaseDefaultMinHrJobLevel | DEFAULT_MIN_HR_JOB_LEVEL | — | ✅ |
| 22 | ProjectRoleTypeBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 23 | ProjectRoleTypeBaseIsSeeded | IS_SEEDED | — | ✅ |
| 24 | ProjectRoleTypeBaseJobRoleId | JOB_ROLE_ID | — | ✅ |
| 25 | ProjectRoleTypeBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | ProjectRoleTypeBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | ProjectRoleTypeBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ProjectRoleTypeBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | ProjectRoleTypeBaseProjectRoleId | PROJECT_ROLE_ID | 🔑 | ✅ |
| 30 | ProjectRoleTypeBaseRoleId | ROLE_ID | — | ✅ |
| 31 | ProjectRoleTypeBaseSecurityRoleGuid | SECURITY_ROLE_GUID | — | ✅ |
| 32 | ProjectRoleTypeBaseSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 33 | ProjectRoleTypeBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[pjf_proj_role_types_tl|PJF_PROJ_ROLE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectRoleTypeTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectRoleTypeTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectRoleTypeTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | ProjectRoleTypeTransLangLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectRoleTypeTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectRoleTypeTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectRoleTypeTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectRoleTypeTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectRoleTypeTransLangProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 10 | ProjectRoleTypeTransLangProjectRoleName | PROJECT_ROLE_NAME | — | ✅ |
| 11 | ProjectRoleTypeTransLangSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectRoleTypeTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
