---
id: DOC-PO-PVO-SupplierUpReqPVO
doc_type: system-doc
title: "SupplierUpReqPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierUpReqPVO
  - supplierupreqpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierUpReqPVO

## 📌 Visão Geral

Extrai requisições de atualização de perfil e provisionamento de roles para fornecedores no portal. Permite acompanhamento de solicitações de acesso e atualização cadastral.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierUpReqPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 4 | 2 | 5 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[per_roles_dn_vl|PER_ROLES_DN_VL]] — 5 atributos (1 PKs, 2 BICC)
- [[poz_provisionable_roles|POZ_PROVISIONABLE_ROLES]] — 1 atributos
- [[poz_up_requests|POZ_UP_REQUESTS]] — 13 atributos (1 PKs, 3 BICC)
- [[poz_up_role_requests|POZ_UP_ROLE_REQUESTS]] — 3 atributos

---

## ⚙️ Atributos

### [[per_roles_dn_vl|PER_ROLES_DN_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RoleDescription | DESCRIPTION | — | ✅ |
| 2 | RoleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 3 | RoleRoleGuid | ROLE_GUID | — | — |
| 4 | RoleRoleId | ROLE_ID | — | — |
| 5 | RoleRoleName | ROLE_NAME | 🔑 | ✅ |

### [[poz_provisionable_roles|POZ_PROVISIONABLE_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierProvRolesRoleGuid | ROLE_GUID | — | — |

### [[poz_up_requests|POZ_UP_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierUpReqContactRequestId | CONTACT_REQUEST_ID | — | — |
| 2 | SupplierUpReqCreatedBy | CREATED_BY | — | — |
| 3 | SupplierUpReqCreationDate | CREATION_DATE | — | — |
| 4 | SupplierUpReqLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SupplierUpReqLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SupplierUpReqLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SupplierUpReqObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SupplierUpReqPerLdapRequestId | PER_LDAP_REQUEST_ID | — | — |
| 9 | SupplierUpReqPersonPartyId | PERSON_PARTY_ID | — | — |
| 10 | SupplierUpReqPostInstanceId | POST_INSTANCE_ID | — | — |
| 11 | SupplierUpReqRequestStatus | REQUEST_STATUS | — | ✅ |
| 12 | SupplierUpReqSubmitInstanceId | SUBMIT_INSTANCE_ID | — | — |
| 13 | UpRequestId | UP_REQUEST_ID | 🔑 | ✅ |

### [[poz_up_role_requests|POZ_UP_ROLE_REQUESTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SupplierUpRoleReqRoleGuid | ROLE_GUID | — | — |
| 2 | SupplierUpRoleReqRoleRequestId | ROLE_REQUEST_ID | — | — |
| 3 | SupplierUpRoleReqUpRequestId | UP_REQUEST_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
