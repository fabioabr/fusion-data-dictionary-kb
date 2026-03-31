---
id: DOC-HCM-500
doc_type: system-doc
title: "HZ_ORG_CONTACTS — (título a preencher)"
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
  - HZ_ORG_CONTACTS
  - hz_org_contacts
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_ORG_CONTACTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMMENTS | — | — | — | — | — | — |
| 2 | CONTACT_NUMBER | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | CURRENCY_CODE | — | — | — | — | — | — |
| 7 | DECISION_MAKER_FLAG | — | — | — | — | — | — |
| 8 | DEPARTMENT | — | — | — | — | — | — |
| 9 | DEPARTMENT_CODE | — | — | — | — | — | — |
| 10 | JOB_TITLE | — | — | — | — | — | — |
| 11 | JOB_TITLE_CODE | — | — | — | — | — | — |
| 12 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 15 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 16 | ORG_CONTACT_ID | — | — | — | — | — | — |
| 17 | ORIG_SYSTEM_REFERENCE | — | — | — | — | — | — |
| 18 | PARTY_RELATIONSHIP_ID | — | — | — | — | — | — |
| 19 | PARTY_SITE_ID | — | — | — | — | — | — |
| 20 | RANK | — | — | — | — | — | — |
| 21 | REFERENCE_USE_FLAG | — | — | — | — | — | — |
| 22 | SALES_AFFINITY_CODE | — | — | — | — | — | — |
| 23 | SALES_AFFINITY_COMMENTS | — | — | — | — | — | — |
| 24 | SALES_BUYING_ROLE_CODE | — | — | — | — | — | — |
| 25 | SALES_INFLUENCE_LEVEL_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountcontactrelationship|AccountContactRelationShip]] (AR · BICC: 5/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | OrganizationContactComments | — |
| CONTACT_NUMBER | OrganizationContactContactNumber | ✅ |
| CREATED_BY | OrganizationContactCreatedBy | — |
| CREATED_BY_MODULE | OrganizationContactCreatedByModule | — |
| CREATION_DATE | OrganizationContactCreationDate | — |
| CURRENCY_CODE | OrganizationContactCurrencyCode | — |
| DECISION_MAKER_FLAG | OrganizationContactDecisionMakerFlag | — |
| DEPARTMENT | OrganizationContactDepartment | — |
| DEPARTMENT_CODE | OrganizationContactDepartmentCode | ✅ |
| JOB_TITLE | OrganizationContactJobTitle | ✅ |
| JOB_TITLE_CODE | OrganizationContactJobTitleCode | ✅ |
| LAST_UPDATE_DATE | OrganizationContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationContactLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationContactLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | OrganizationContactObjectVersionNumber | — |
| ORG_CONTACT_ID | OrganizationContactOrgContactId | — |
| ORIG_SYSTEM_REFERENCE | OrganizationContactOrigSystemReference | — |
| PARTY_RELATIONSHIP_ID | OrganizationContactPartyRelationshipId | — |
| PARTY_SITE_ID | OrganizationContactPartySiteId | — |
| RANK | OrganizationContactRank | — |
| REFERENCE_USE_FLAG | OrganizationContactReferenceUseFlag | — |
| SALES_AFFINITY_CODE | OrganizationContactSalesAffinityCode | — |
| SALES_AFFINITY_COMMENTS | OrganizationContactSalesAffinityComments | — |
| SALES_BUYING_ROLE_CODE | OrganizationContactSalesBuyingRoleCode | — |
| SALES_INFLUENCE_LEVEL_CODE | OrganizationContactSalesInfluenceLevelCode | — |

### [[allsuppliercontactspvo|AllSupplierContactsPVO]] (PO · BICC: 2/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | OrgContComments | — |
| CONTACT_NUMBER | OrgContContactNumber | — |
| CREATED_BY | OrgContCreatedBy | — |
| CREATED_BY_MODULE | OrgContCreatedByModule | — |
| CREATION_DATE | OrgContCreationDate | — |
| DECISION_MAKER_FLAG | OrgContDecisionMakerFlag | — |
| DEPARTMENT | OrgContDepartment | — |
| DEPARTMENT_CODE | OrgContDepartmentCode | — |
| JOB_TITLE | OrgContJobTitle | ✅ |
| JOB_TITLE_CODE | OrgContJobTitleCode | — |
| LAST_UPDATE_DATE | OrgContLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrgContLastUpdateLogin | — |
| LAST_UPDATED_BY | OrgContLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | OrgContObjectVersionNumber | — |
| ORG_CONTACT_ID | OrgContOrgContactId | — |
| ORIG_SYSTEM_REFERENCE | OrgContOrigSystemReference | — |
| PARTY_RELATIONSHIP_ID | OrgContPartyRelationshipId | — |
| PARTY_SITE_ID | OrgContPartySiteId | — |
| RANK | OrgContRank | — |
| REFERENCE_USE_FLAG | OrgContReferenceUseFlag | — |
| SALES_AFFINITY_CODE | OrgContSalesAffinityCode | — |
| SALES_AFFINITY_COMMENTS | OrgContSalesAffinityComments | — |
| SALES_BUYING_ROLE_CODE | OrgContSalesBuyingRoleCode | — |
| SALES_INFLUENCE_LEVEL_CODE | OrgContSalesInfluenceLevelCode | — |

### [[sitecontactrelationship|SiteContactRelationShip]] (AR · BICC: 5/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | OrganizationContactComments | — |
| CONTACT_NUMBER | OrganizationContactContactNumber | ✅ |
| CREATED_BY | OrganizationContactCreatedBy | — |
| CREATED_BY_MODULE | OrganizationContactCreatedByModule | — |
| CREATION_DATE | OrganizationContactCreationDate | — |
| CURRENCY_CODE | OrganizationContactCurrencyCode | — |
| DECISION_MAKER_FLAG | OrganizationContactDecisionMakerFlag | — |
| DEPARTMENT | OrganizationContactDepartment | — |
| DEPARTMENT_CODE | OrganizationContactDepartmentCode | ✅ |
| JOB_TITLE | OrganizationContactJobTitle | ✅ |
| JOB_TITLE_CODE | OrganizationContactJobTitleCode | ✅ |
| LAST_UPDATE_DATE | OrganizationContactLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | OrganizationContactLastUpdateLogin | — |
| LAST_UPDATED_BY | OrganizationContactLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | OrganizationContactObjectVersionNumber | — |
| ORG_CONTACT_ID | OrganizationContactOrgContactId | — |
| ORIG_SYSTEM_REFERENCE | OrganizationContactOrigSystemReference | — |
| PARTY_RELATIONSHIP_ID | OrganizationContactPartyRelationshipId | — |
| PARTY_SITE_ID | OrganizationContactPartySiteId | — |
| RANK | OrganizationContactRank | — |
| REFERENCE_USE_FLAG | OrganizationContactReferenceUseFlag | — |
| SALES_AFFINITY_CODE | OrganizationContactSalesAffinityCode | — |
| SALES_AFFINITY_COMMENTS | OrganizationContactSalesAffinityComments | — |
| SALES_BUYING_ROLE_CODE | OrganizationContactSalesBuyingRoleCode | — |
| SALES_INFLUENCE_LEVEL_CODE | OrganizationContactSalesInfluenceLevelCode | — |

### [[suppliercontactspvo|SupplierContactsPVO]] (PO · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | OrgComments | — |
| CONTACT_NUMBER | OrgContactNumber | — |
| CREATED_BY_MODULE | OrgCreatedByModule | — |
| DECISION_MAKER_FLAG | OrgDecisionMakerFlag | — |
| DEPARTMENT | OrgDepartment | — |
| DEPARTMENT_CODE | OrgDepartmentCode | — |
| JOB_TITLE | OrgJobTitle | ✅ |
| JOB_TITLE_CODE | OrgJobTitleCode | — |
| ORG_CONTACT_ID | OrgOrgContactId | ✅ |
| ORIG_SYSTEM_REFERENCE | OrgOrigSystemReference | — |
| PARTY_RELATIONSHIP_ID | OrgPartyRelationshipId | — |
| PARTY_SITE_ID | OrgPartySiteId | — |
| RANK | OrgRank | — |
| REFERENCE_USE_FLAG | OrgReferenceUseFlag | — |
| SALES_AFFINITY_CODE | OrgSalesAffinityCode | — |
| SALES_AFFINITY_COMMENTS | OrgSalesAffinityComments | — |
| SALES_BUYING_ROLE_CODE | OrgSalesBuyingRoleCode | — |
| SALES_INFLUENCE_LEVEL_CODE | OrgSalesInfluenceLevelCode | — |
