---
id: DOC-HCM-PVO-ProfileRelationPVO
doc_type: system-doc
title: "ProfileRelationPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ProfileRelationPVO
  - profilerelationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileRelationPVO

## 📌 Visão Geral

Extrai relações entre perfis de talento, vinculando perfis a entidades organizacionais. Suporta a associação de competências a cargos e posições.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.ProfileRelationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profile_relations|HRT_PROFILE_RELATIONS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hrt_profile_relations|HRT_PROFILE_RELATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectEffEndDate | OBJECT_EFF_END_DATE | — | ✅ |
| 8 | ObjectEffStartDate | OBJECT_EFF_START_DATE | — | ✅ |
| 9 | ObjectId | OBJECT_ID | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProfileId | PROFILE_ID | — | ✅ |
| 12 | ProfileRelationId | PROFILE_RELATION_ID | 🔑 | ✅ |
| 13 | RelationId | RELATION_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
