---
id: DOC-HCM-PVO-RoleDNExtractPVO
doc_type: system-doc
title: "RoleDNExtractPVO — PVO Human Capital Management"
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
  - RoleDNExtractPVO
  - rolednextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RoleDNExtractPVO

## 📌 Visão Geral

Extrai papéis (roles) com Distinguished Names para carga BICC de usuários. Suporta mapeamento de atribuições de segurança e acesso no HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.UserBiccExtractAM.RoleDNExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 1 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_roles_dn_vl|PER_ROLES_DN_VL]] — 22 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[per_roles_dn_vl|PER_ROLES_DN_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbstractRole | ABSTRACT_ROLE | — | ✅ |
| 2 | ActiveFlag | ACTIVE_FLAG | — | ✅ |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DataRole | DATA_ROLE | — | ✅ |
| 7 | DelegationAllowed | DELEGATION_ALLOWED | — | ✅ |
| 8 | Description | DESCRIPTION | — | ✅ |
| 9 | DutyRole | DUTY_ROLE | — | ✅ |
| 10 | ExternalId | EXTERNAL_ID | — | ✅ |
| 11 | ExternalRole | EXTERNAL_ROLE | — | ✅ |
| 12 | JobRole | JOB_ROLE | — | ✅ |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | MultitenancyCommonName | MULTITENANCY_COMMON_NAME | — | ✅ |
| 17 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | RoleCommonName | ROLE_COMMON_NAME | — | ✅ |
| 19 | RoleDistinguishedName | ROLE_DISTINGUISHED_NAME | — | ✅ |
| 20 | RoleGuid | ROLE_GUID | — | ✅ |
| 21 | RoleId | ROLE_ID | 🔑 | ✅ |
| 22 | RoleName | ROLE_NAME | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
