---
id: DOC-OTHER-PVO-CompRolePVO
doc_type: system-doc
title: "CompRolePVO — PVO Cross-Module"
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
  - CompRolePVO
  - comprolepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CompRolePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Comp Role. Acessa as tabelas: CN_ROLES_B, CN_ROLES_TL.

**Caminho:** `FscmTopModelAM.ParticipantSetupAM.CompRolePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 14 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[cn_roles_b|CN_ROLES_B]] — 15 atributos (1 PKs, 11 BICC)
- [[cn_roles_tl|CN_ROLES_TL]] — 6 atributos (3 BICC)

---

## ⚙️ Atributos

### [[cn_roles_b|CN_ROLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessType | ACCESS_TYPE | — | ✅ |
| 2 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RevenueType | REVENUE_TYPE | — | ✅ |
| 11 | RoleCode | ROLE_CODE | — | ✅ |
| 12 | RoleId | ROLE_ID | 🔑 | ✅ |
| 13 | RoleTypeCode | ROLE_TYPE_CODE | — | ✅ |
| 14 | SeededFlag | SEEDED_FLAG | — | — |
| 15 | SplitPct | SPLIT_PCT | — | ✅ |

### [[cn_roles_tl|CN_ROLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | — | ✅ |
| 2 | ObjectVersionNumberTLEO | OBJECT_VERSION_NUMBER | — | — |
| 3 | RoleDesc | ROLE_DESC | — | ✅ |
| 4 | RoleIdTLEO | ROLE_ID | — | — |
| 5 | RoleName | ROLE_NAME | — | ✅ |
| 6 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
