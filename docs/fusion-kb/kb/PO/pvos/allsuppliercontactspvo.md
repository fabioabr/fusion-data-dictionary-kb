---
id: DOC-PO-PVO-AllSupplierContactsPVO
doc_type: system-doc
title: "AllSupplierContactsPVO — PVO Purchasing"
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
  - AllSupplierContactsPVO
  - allsuppliercontactspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AllSupplierContactsPVO

## 📌 Visão Geral

Extrai todos os contatos de fornecedores com detalhes de nome, função, e-mail e telefone, vinculados a sites e organizações. Suporta comunicação eficiente com fornecedores e gestão centralizada de relacionamentos.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.AllSupplierContactsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 169 | 5 | 3 | 86 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[hz_org_contacts|HZ_ORG_CONTACTS]] — 24 atributos (2 BICC)
- [[hz_org_contact_roles|HZ_ORG_CONTACT_ROLES]] — 9 atributos (1 BICC)
- [[hz_party_sites|HZ_PARTY_SITES]] — 30 atributos (1 PKs, 3 BICC)
- [[poz_all_supplier_contacts_v|POZ_ALL_SUPPLIER_CONTACTS_V]] — 89 atributos (2 PKs, 79 BICC)
- [[poz_supplier_contacts|POZ_SUPPLIER_CONTACTS]] — 17 atributos (1 BICC)

---

## ⚙️ Atributos

### [[hz_org_contacts|HZ_ORG_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgContComments | COMMENTS | — | — |
| 2 | OrgContContactNumber | CONTACT_NUMBER | — | — |
| 3 | OrgContCreatedBy | CREATED_BY | — | — |
| 4 | OrgContCreatedByModule | CREATED_BY_MODULE | — | — |
| 5 | OrgContCreationDate | CREATION_DATE | — | — |
| 6 | OrgContDecisionMakerFlag | DECISION_MAKER_FLAG | — | — |
| 7 | OrgContDepartment | DEPARTMENT | — | — |
| 8 | OrgContDepartmentCode | DEPARTMENT_CODE | — | — |
| 9 | OrgContJobTitle | JOB_TITLE | — | ✅ |
| 10 | OrgContJobTitleCode | JOB_TITLE_CODE | — | — |
| 11 | OrgContLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | OrgContLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | OrgContLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | OrgContObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | OrgContOrgContactId | ORG_CONTACT_ID | — | — |
| 16 | OrgContOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 17 | OrgContPartyRelationshipId | PARTY_RELATIONSHIP_ID | — | — |
| 18 | OrgContPartySiteId | PARTY_SITE_ID | — | — |
| 19 | OrgContRank | RANK | — | — |
| 20 | OrgContReferenceUseFlag | REFERENCE_USE_FLAG | — | — |
| 21 | OrgContSalesAffinityCode | SALES_AFFINITY_CODE | — | — |
| 22 | OrgContSalesAffinityComments | SALES_AFFINITY_COMMENTS | — | — |
| 23 | OrgContSalesBuyingRoleCode | SALES_BUYING_ROLE_CODE | — | — |
| 24 | OrgContSalesInfluenceLevelCode | SALES_INFLUENCE_LEVEL_CODE | — | — |

### [[hz_org_contact_roles|HZ_ORG_CONTACT_ROLES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgContRoleCreatedByModule | CREATED_BY_MODULE | — | — |
| 2 | OrgContRoleOrgContactId | ORG_CONTACT_ID | — | — |
| 3 | OrgContRoleOrgContactRoleId | ORG_CONTACT_ROLE_ID | — | — |
| 4 | OrgContRoleOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 5 | OrgContRolePrimaryContactPerRoleType | PRIMARY_CONTACT_PER_ROLE_TYPE | — | — |
| 6 | OrgContRolePrimaryFlag | PRIMARY_FLAG | — | — |
| 7 | OrgContRoleRoleLevel | ROLE_LEVEL | — | — |
| 8 | OrgContRoleRoleType | ROLE_TYPE | — | ✅ |
| 9 | OrgContRoleStatus | STATUS | — | — |

### [[hz_party_sites|HZ_PARTY_SITES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartySiteActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | PartySiteAddressee | ADDRESSEE | — | — |
| 3 | PartySiteComments | COMMENTS | — | — |
| 4 | PartySiteCreatedBy | CREATED_BY | — | — |
| 5 | PartySiteCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | PartySiteCreationDate | CREATION_DATE | — | — |
| 7 | PartySiteDunsNumberC | DUNS_NUMBER_C | — | — |
| 8 | PartySiteEndDateActive | END_DATE_ACTIVE | — | — |
| 9 | PartySiteGlobalLocationNumber | GLOBAL_LOCATION_NUMBER | — | — |
| 10 | PartySiteId | PARTY_SITE_ID | 🔑 | ✅ |
| 11 | PartySiteIdentifyingAddressFlag | IDENTIFYING_ADDRESS_FLAG | — | — |
| 12 | PartySiteLanguage | PARTY_SITE_LANGUAGE | — | — |
| 13 | PartySiteLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | PartySiteLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | PartySiteLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | PartySiteLocationId | LOCATION_ID | — | — |
| 17 | PartySiteMailstop | MAILSTOP | — | — |
| 18 | PartySiteObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | PartySiteOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 20 | PartySitePartyId | PARTY_ID | — | — |
| 21 | PartySitePartyNameDba | PARTY_NAME_DBA | — | — |
| 22 | PartySitePartyNameDivision | PARTY_NAME_DIVISION | — | — |
| 23 | PartySitePartyNameLegal | PARTY_NAME_LEGAL | — | — |
| 24 | PartySitePartySiteName | PARTY_SITE_NAME | — | ✅ |
| 25 | PartySitePartySiteNumber | PARTY_SITE_NUMBER | — | — |
| 26 | PartySitePartySiteType | PARTY_SITE_TYPE | — | — |
| 27 | PartySiteRelationshipId | RELATIONSHIP_ID | — | — |
| 28 | PartySiteStartDateActive | START_DATE_ACTIVE | — | — |
| 29 | PartySiteStatus | STATUS | — | — |
| 30 | PartyUsageCode | PARTY_USAGE_CODE | — | — |

### [[poz_all_supplier_contacts_v|POZ_ALL_SUPPLIER_CONTACTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllSupplierContactsAttribute1 | ATTRIBUTE1 | — | ✅ |
| 2 | AllSupplierContactsAttribute10 | ATTRIBUTE10 | — | ✅ |
| 3 | AllSupplierContactsAttribute11 | ATTRIBUTE11 | — | ✅ |
| 4 | AllSupplierContactsAttribute12 | ATTRIBUTE12 | — | ✅ |
| 5 | AllSupplierContactsAttribute13 | ATTRIBUTE13 | — | ✅ |
| 6 | AllSupplierContactsAttribute14 | ATTRIBUTE14 | — | ✅ |
| 7 | AllSupplierContactsAttribute15 | ATTRIBUTE15 | — | ✅ |
| 8 | AllSupplierContactsAttribute16 | ATTRIBUTE16 | — | ✅ |
| 9 | AllSupplierContactsAttribute17 | ATTRIBUTE17 | — | ✅ |
| 10 | AllSupplierContactsAttribute18 | ATTRIBUTE18 | — | ✅ |
| 11 | AllSupplierContactsAttribute19 | ATTRIBUTE19 | — | ✅ |
| 12 | AllSupplierContactsAttribute2 | ATTRIBUTE2 | — | ✅ |
| 13 | AllSupplierContactsAttribute20 | ATTRIBUTE20 | — | ✅ |
| 14 | AllSupplierContactsAttribute21 | ATTRIBUTE21 | — | ✅ |
| 15 | AllSupplierContactsAttribute22 | ATTRIBUTE22 | — | ✅ |
| 16 | AllSupplierContactsAttribute23 | ATTRIBUTE23 | — | ✅ |
| 17 | AllSupplierContactsAttribute24 | ATTRIBUTE24 | — | ✅ |
| 18 | AllSupplierContactsAttribute25 | ATTRIBUTE25 | — | ✅ |
| 19 | AllSupplierContactsAttribute26 | ATTRIBUTE26 | — | ✅ |
| 20 | AllSupplierContactsAttribute27 | ATTRIBUTE27 | — | ✅ |
| 21 | AllSupplierContactsAttribute28 | ATTRIBUTE28 | — | ✅ |
| 22 | AllSupplierContactsAttribute29 | ATTRIBUTE29 | — | ✅ |
| 23 | AllSupplierContactsAttribute3 | ATTRIBUTE3 | — | ✅ |
| 24 | AllSupplierContactsAttribute30 | ATTRIBUTE30 | — | ✅ |
| 25 | AllSupplierContactsAttribute4 | ATTRIBUTE4 | — | ✅ |
| 26 | AllSupplierContactsAttribute5 | ATTRIBUTE5 | — | ✅ |
| 27 | AllSupplierContactsAttribute6 | ATTRIBUTE6 | — | ✅ |
| 28 | AllSupplierContactsAttribute7 | ATTRIBUTE7 | — | ✅ |
| 29 | AllSupplierContactsAttribute8 | ATTRIBUTE8 | — | ✅ |
| 30 | AllSupplierContactsAttribute9 | ATTRIBUTE9 | — | ✅ |
| 31 | AllSupplierContactsAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 32 | AllSupplierContactsAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 33 | AllSupplierContactsAttributeDate10 | ATTRIBUTE_DATE10 | — | ✅ |
| 34 | AllSupplierContactsAttributeDate11 | ATTRIBUTE_DATE11 | — | ✅ |
| 35 | AllSupplierContactsAttributeDate12 | ATTRIBUTE_DATE12 | — | ✅ |
| 36 | AllSupplierContactsAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 37 | AllSupplierContactsAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 38 | AllSupplierContactsAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 39 | AllSupplierContactsAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 40 | AllSupplierContactsAttributeDate6 | ATTRIBUTE_DATE6 | — | ✅ |
| 41 | AllSupplierContactsAttributeDate7 | ATTRIBUTE_DATE7 | — | ✅ |
| 42 | AllSupplierContactsAttributeDate8 | ATTRIBUTE_DATE8 | — | ✅ |
| 43 | AllSupplierContactsAttributeDate9 | ATTRIBUTE_DATE9 | — | ✅ |
| 44 | AllSupplierContactsAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 45 | AllSupplierContactsAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 46 | AllSupplierContactsAttributeNumber11 | ATTRIBUTE_NUMBER11 | — | ✅ |
| 47 | AllSupplierContactsAttributeNumber12 | ATTRIBUTE_NUMBER12 | — | ✅ |
| 48 | AllSupplierContactsAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 49 | AllSupplierContactsAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 50 | AllSupplierContactsAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 51 | AllSupplierContactsAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 52 | AllSupplierContactsAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 53 | AllSupplierContactsAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 54 | AllSupplierContactsAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 55 | AllSupplierContactsAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 56 | AllSupplierContactsCreatedBy | CREATED_BY | — | ✅ |
| 57 | AllSupplierContactsCreationDate | CREATION_DATE | — | ✅ |
| 58 | AllSupplierContactsEmailAddress | EMAIL_ADDRESS | — | ✅ |
| 59 | AllSupplierContactsEmailContactPointId | EMAIL_CONTACT_POINT_ID | — | — |
| 60 | AllSupplierContactsFaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 61 | AllSupplierContactsFaxContactPointId | FAX_CONTACT_POINT_ID | — | — |
| 62 | AllSupplierContactsFaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 63 | AllSupplierContactsFaxNumber | FAX_NUMBER | — | ✅ |
| 64 | AllSupplierContactsInactiveDate | INACTIVE_DATE | — | ✅ |
| 65 | AllSupplierContactsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 66 | AllSupplierContactsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 67 | AllSupplierContactsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 68 | AllSupplierContactsMobileAreaCode | MOBILE_AREA_CODE | — | ✅ |
| 69 | AllSupplierContactsMobileContactPointId | MOBILE_CONTACT_POINT_ID | — | — |
| 70 | AllSupplierContactsMobileCountryCode | MOBILE_COUNTRY_CODE | — | ✅ |
| 71 | AllSupplierContactsMobileNumber | MOBILE_NUMBER | — | ✅ |
| 72 | AllSupplierContactsName | NAME | — | — |
| 73 | AllSupplierContactsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 74 | AllSupplierContactsPersonFirstName | PERSON_FIRST_NAME | — | ✅ |
| 75 | AllSupplierContactsPersonLastName | PERSON_LAST_NAME | — | ✅ |
| 76 | AllSupplierContactsPersonMiddleName | PERSON_MIDDLE_NAME | — | ✅ |
| 77 | AllSupplierContactsPersonTitle | PERSON_TITLE | — | — |
| 78 | AllSupplierContactsPhoneAreaCode | PHONE_AREA_CODE | — | ✅ |
| 79 | AllSupplierContactsPhoneContactPointId | PHONE_CONTACT_POINT_ID | — | — |
| 80 | AllSupplierContactsPhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 81 | AllSupplierContactsPhoneExtension | PHONE_EXTENSION | — | ✅ |
| 82 | AllSupplierContactsPhoneNumber | PHONE_NUMBER | — | ✅ |
| 83 | AllSupplierContactsRelationshipId | RELATIONSHIP_ID | — | — |
| 84 | AllSupplierContactsSalutation | SALUTATION | — | ✅ |
| 85 | AllSupplierContactsStatus | STATUS | — | ✅ |
| 86 | AllSupplierContactsSubjectId | SUBJECT_ID | — | — |
| 87 | AllSupplierContactsSupplierName | SUPPLIER_NAME | — | ✅ |
| 88 | PerPartyId | PER_PARTY_ID | 🔑 | ✅ |
| 89 | SupPartyId | SUP_PARTY_ID | 🔑 | ✅ |

### [[poz_supplier_contacts|POZ_SUPPLIER_CONTACTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SuppAddrContactsCreatedBy | CREATED_BY | — | — |
| 2 | SuppAddrContactsCreationDate | CREATION_DATE | — | — |
| 3 | SuppAddrContactsInactiveDate | INACTIVE_DATE | — | — |
| 4 | SuppAddrContactsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | SuppAddrContactsLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SuppAddrContactsLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SuppAddrContactsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SuppAddrContactsOrgContactId | ORG_CONTACT_ID | — | — |
| 9 | SuppAddrContactsOrgPartySiteId | ORG_PARTY_SITE_ID | — | — |
| 10 | SuppAddrContactsPartySiteId | PARTY_SITE_ID | — | — |
| 11 | SuppAddrContactsPerPartyId | PER_PARTY_ID | — | — |
| 12 | SuppAddrContactsProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 13 | SuppAddrContactsProgramId | PROGRAM_ID | — | — |
| 14 | SuppAddrContactsProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 15 | SuppAddrContactsRelationshipId | RELATIONSHIP_ID | — | — |
| 16 | SuppAddrContactsRequestId | REQUEST_ID | — | — |
| 17 | SuppAddrContactsVendorContactId | VENDOR_CONTACT_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
