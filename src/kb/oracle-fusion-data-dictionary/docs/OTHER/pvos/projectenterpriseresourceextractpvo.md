---
id: DOC-OTHER-PVO-ProjectEnterpriseResourceExtractPVO
doc_type: system-doc
title: "ProjectEnterpriseResourceExtractPVO — PVO Cross-Module"
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
  - ProjectEnterpriseResourceExtractPVO
  - projectenterpriseresourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectEnterpriseResourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Enterprise Resource Extract. Acessa as tabelas: PJT_PRJ_ENTERPRISE_RESOURCE_B, PJT_PRJ_ENTERPRISE_RESOURCE_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectEnterpriseResourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 48 | 2 | 1 | 48 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 36 atributos (1 PKs, 36 BICC)
- [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceBasePEOBillRate | BILL_RATE | — | ✅ |
| 2 | PrjEnterpriseResourceBasePEOBillRateCurrencyCode | BILL_RATE_CURRENCY_CODE | — | ✅ |
| 3 | PrjEnterpriseResourceBasePEOCostRate | COST_RATE | — | ✅ |
| 4 | PrjEnterpriseResourceBasePEOCostRateCurrencyCode | COST_RATE_CURRENCY_CODE | — | ✅ |
| 5 | PrjEnterpriseResourceBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | PrjEnterpriseResourceBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | PrjEnterpriseResourceBasePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | PrjEnterpriseResourceBasePEOEmail | EMAIL | — | ✅ |
| 9 | PrjEnterpriseResourceBasePEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 10 | PrjEnterpriseResourceBasePEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 11 | PrjEnterpriseResourceBasePEOExpenditureAmount | EXPENDITURE_AMOUNT | — | ✅ |
| 12 | PrjEnterpriseResourceBasePEOExpenditureTypeId | EXPENDITURE_TYPE_ID | — | ✅ |
| 13 | PrjEnterpriseResourceBasePEOExternalId | EXTERNAL_ID | — | ✅ |
| 14 | PrjEnterpriseResourceBasePEOFirstName | FIRST_NAME | — | ✅ |
| 15 | PrjEnterpriseResourceBasePEOIsSeeded | IS_SEEDED | — | ✅ |
| 16 | PrjEnterpriseResourceBasePEOLastName | LAST_NAME | — | ✅ |
| 17 | PrjEnterpriseResourceBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | PrjEnterpriseResourceBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 19 | PrjEnterpriseResourceBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | PrjEnterpriseResourceBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PrjEnterpriseResourceBasePEOPartyId | PARTY_ID | — | ✅ |
| 22 | PrjEnterpriseResourceBasePEOPersonId | PERSON_ID | — | ✅ |
| 23 | PrjEnterpriseResourceBasePEOPhone | PHONE | — | ✅ |
| 24 | PrjEnterpriseResourceBasePEOProjectId | PROJECT_ID | — | ✅ |
| 25 | PrjEnterpriseResourceBasePEOProjectRoleId | PROJECT_ROLE_ID | — | ✅ |
| 26 | PrjEnterpriseResourceBasePEORate | RATE | — | ✅ |
| 27 | PrjEnterpriseResourceBasePEOResMgmtFlag | RES_MGMT_FLAG | — | ✅ |
| 28 | PrjEnterpriseResourceBasePEOResourceClass | RESOURCE_CLASS | — | ✅ |
| 29 | PrjEnterpriseResourceBasePEOResourceId | RESOURCE_ID | 🔑 | ✅ |
| 30 | PrjEnterpriseResourceBasePEOResourceManagerId | RESOURCE_MANAGER_ID | — | ✅ |
| 31 | PrjEnterpriseResourceBasePEOResourceScope | RESOURCE_SCOPE | — | ✅ |
| 32 | PrjEnterpriseResourceBasePEOResourceType | RESOURCE_TYPE | — | ✅ |
| 33 | PrjEnterpriseResourceBasePEOScheduleId | SCHEDULE_ID | — | ✅ |
| 34 | PrjEnterpriseResourceBasePEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 35 | PrjEnterpriseResourceBasePEOUnitOfMeasure | UNIT_OF_MEASURE | — | ✅ |
| 36 | PrjEnterpriseResourceBasePEOUserDefinedFlag | USER_DEFINED_FLAG | — | ✅ |

### [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceTransla1CreatedBy | CREATED_BY | — | ✅ |
| 2 | PrjEnterpriseResourceTransla1CreationDate | CREATION_DATE | — | ✅ |
| 3 | PrjEnterpriseResourceTransla1Description | DESCRIPTION | — | ✅ |
| 4 | PrjEnterpriseResourceTransla1DisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PrjEnterpriseResourceTransla1EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | PrjEnterpriseResourceTransla1Language | LANGUAGE | — | ✅ |
| 7 | PrjEnterpriseResourceTransla1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PrjEnterpriseResourceTransla1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PrjEnterpriseResourceTransla1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PrjEnterpriseResourceTransla1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PrjEnterpriseResourceTransla1ResourceId | RESOURCE_ID | — | ✅ |
| 12 | PrjEnterpriseResourceTransla1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
