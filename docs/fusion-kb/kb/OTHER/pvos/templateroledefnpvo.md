---
id: DOC-OTHER-PVO-TemplateRoleDefnPVO
doc_type: system-doc
title: "TemplateRoleDefnPVO — PVO Cross-Module"
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
  - TemplateRoleDefnPVO
  - templateroledefnpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TemplateRoleDefnPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Template Role Defn. Acessa as tabelas: HRA_ROLE_DEFNS_B, HRA_ROLE_DEFNS_TL, HRA_TMPL_ROLES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPerformanceSetupAM.TemplateRoleDefnPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 3 | 7 | 18 | 72% |

---

## 🔗 Tabelas Relacionadas

- [[hra_role_defns_b|HRA_ROLE_DEFNS_B]] — 8 atributos (2 PKs, 8 BICC)
- [[hra_role_defns_tl|HRA_ROLE_DEFNS_TL]] — 6 atributos (3 PKs, 6 BICC)
- [[hra_tmpl_roles|HRA_TMPL_ROLES]] — 11 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[hra_role_defns_b|HRA_ROLE_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleDefinitionBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | RoleDefinitionBPEODateFrom | DATE_FROM | — | ✅ |
| 3 | RoleDefinitionBPEODateTo | DATE_TO | — | ✅ |
| 4 | RoleDefinitionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RoleDefinitionBPEOManagerType | MANAGER_TYPE | — | ✅ |
| 6 | RoleDefinitionBPEOMatrixParticipantFlag | MATRIX_PARTICIPANT_FLAG | — | ✅ |
| 7 | RoleDefinitionBPEOStatusCode | STATUS_CODE | — | ✅ |
| 8 | RoleId | ROLE_ID | 🔑 | ✅ |

### [[hra_role_defns_tl|HRA_ROLE_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | RoleDefinitionTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | RoleDefinitionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | RoleDefinitionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RoleDefinitionTranslationPEOName | NAME | — | ✅ |
| 6 | RoleDefinitionTranslationPEORoleId | ROLE_ID | 🔑 | ✅ |

### [[hra_tmpl_roles|HRA_TMPL_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | TemplateRolePEOMinimumNumPcpns | MINIMUM_NUM_PCPNS | — | ✅ |
| 9 | TemplateRolePEORoleTypeCode | ROLE_TYPE_CODE | — | — |
| 10 | TemplateRolePEOTemplateDefnId | TEMPLATE_DEFN_ID | — | — |
| 11 | TmplRoleId | TMPL_ROLE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
