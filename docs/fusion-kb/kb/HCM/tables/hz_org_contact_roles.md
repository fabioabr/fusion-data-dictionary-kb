---
id: DOC-HCM-501
doc_type: system-doc
title: "HZ_ORG_CONTACT_ROLES — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - HZ_ORG_CONTACT_ROLES
  - hz_org_contact_roles
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_ORG_CONTACT_ROLES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 2 | ORG_CONTACT_ID | — | — | — | — | — | — |
| 3 | ORG_CONTACT_ROLE_ID | — | — | — | — | — | — |
| 4 | ORIG_SYSTEM_REFERENCE | — | — | — | — | — | — |
| 5 | PRIMARY_CONTACT_PER_ROLE_TYPE | — | — | — | — | — | — |
| 6 | PRIMARY_FLAG | — | — | — | — | — | — |
| 7 | ROLE_LEVEL | — | — | — | — | — | — |
| 8 | ROLE_TYPE | — | — | — | — | — | — |
| 9 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[allsuppliercontactspvo|AllSupplierContactsPVO]] (PO · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY_MODULE | OrgContRoleCreatedByModule | — |
| ORG_CONTACT_ID | OrgContRoleOrgContactId | — |
| ORG_CONTACT_ROLE_ID | OrgContRoleOrgContactRoleId | — |
| ORIG_SYSTEM_REFERENCE | OrgContRoleOrigSystemReference | — |
| PRIMARY_CONTACT_PER_ROLE_TYPE | OrgContRolePrimaryContactPerRoleType | — |
| PRIMARY_FLAG | OrgContRolePrimaryFlag | — |
| ROLE_LEVEL | OrgContRoleRoleLevel | — |
| ROLE_TYPE | OrgContRoleRoleType | ✅ |
| STATUS | OrgContRoleStatus | — |
