---
id: DOC-OTHER-PVO-AccessViolationsPVO
doc_type: system-doc
title: "AccessViolationsPVO — PVO Cross-Module"
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
  - AccessViolationsPVO
  - accessviolationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccessViolationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Access Violations. Acessa as tabelas: ASE_USER_ROLE_GRC_VIEW, GRC_GRI_D_AAC_INCDNT_ROLES_BG, GRC_OTBI_INTRA_ROLE.

**Caminho:** `FscmTopModelAM.GRCTOPBIAM.AccessViolationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 3 | 1 | 19 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[ase_user_role_grc_view|ASE_USER_ROLE_GRC_VIEW]] — 5 atributos
- [[grc_gri_d_aac_incdnt_roles_bg|GRC_GRI_D_AAC_INCDNT_ROLES_BG]] — 2 atributos
- [[grc_otbi_intra_role|GRC_OTBI_INTRA_ROLE]] — 19 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[ase_user_role_grc_view|ASE_USER_ROLE_GRC_VIEW]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ASEUserRolePEOCode | CODE | — | — |
| 2 | ASEUserRolePEOMembershipId | MEMBERSHIP_ID | — | — |
| 3 | ASEUserRolePEORoleId | ROLE_ID | — | — |
| 4 | ASEUserRolePEOUserGuid | USER_GUID | — | — |
| 5 | ASEUserRolePEOUserId | USER_ID | — | — |

### [[grc_gri_d_aac_incdnt_roles_bg|GRC_GRI_D_AAC_INCDNT_ROLES_BG]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | IncidentAccessRoleBridgePEOObjectId | OBJECT_ID | — | — |
| 2 | IncidentAccessRoleBridgePEORoleId | ROLE_ID | — | — |

### [[grc_otbi_intra_role|GRC_OTBI_INTRA_ROLE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessViolationsPEOAccessPathGrouping | ACCESS_PATH_GROUPING | — | ✅ |
| 2 | AccessViolationsPEOAccessPointName | ACCESS_POINT_NAME | — | ✅ |
| 3 | AccessViolationsPEOControlName | CONTROL_NAME | — | ✅ |
| 4 | AccessViolationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AccessViolationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AccessViolationsPEOEntitlement | ENTITLEMENT | — | ✅ |
| 7 | AccessViolationsPEOGlobalUserName | GLOBAL_USER_NAME | — | ✅ |
| 8 | AccessViolationsPEOIncInfoCode | INCIDENT_INFO_CODE | — | ✅ |
| 9 | AccessViolationsPEOIncidentId | INCIDENT_ID | 🔑 | ✅ |
| 10 | AccessViolationsPEOIncidentInfo | INCIDENT_INFO | — | ✅ |
| 11 | AccessViolationsPEOInvestigators | INVESTIGATORS | — | ✅ |
| 12 | AccessViolationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | AccessViolationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | AccessViolationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | AccessViolationsPEOPriority | PRIORITY | — | ✅ |
| 16 | AccessViolationsPEORoleName | ROLE_NAME | — | ✅ |
| 17 | AccessViolationsPEORowNum | ROW_NUM | — | ✅ |
| 18 | AccessViolationsPEOStatus | STATUS | — | ✅ |
| 19 | AccessViolationsPEOStatusRoleId | ROLE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
