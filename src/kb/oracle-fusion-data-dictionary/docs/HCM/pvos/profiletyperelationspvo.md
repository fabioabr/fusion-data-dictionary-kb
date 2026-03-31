---
id: DOC-HCM-PVO-ProfileTypeRelationsPVO
doc_type: system-doc
title: "ProfileTypeRelationsPVO — PVO Human Capital Management"
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
  - ProfileTypeRelationsPVO
  - profiletyperelationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileTypeRelationsPVO

## 📌 Visão Geral

Extrai relações entre tipos de perfil, definindo vínculos configuráveis entre categorias. Suporta a arquitetura de perfis hierárquicos no Talent Management.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.ProfileTypeRelationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 3 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profile_type_rels|HRT_PROFILE_TYPE_RELS]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hrt_profile_type_rels|HRT_PROFILE_TYPE_RELS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminOnlyFlag | ADMIN_ONLY_FLAG | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ModuleId | MODULE_ID | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProfileTypeId | PROFILE_TYPE_ID | — | — |
| 11 | ProfileTypeRelationId | PROFILE_TYPE_RELATION_ID | 🔑 | ✅ |
| 12 | RelationId | RELATION_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
