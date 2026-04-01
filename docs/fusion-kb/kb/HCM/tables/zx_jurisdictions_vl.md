---
id: DOC-HCM-892
doc_type: system-doc
title: "ZX_JURISDICTIONS_VL — (título a preencher)"
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
  - ZX_JURISDICTIONS_VL
  - zx_jurisdictions_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_JURISDICTIONS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOW_TAX_REGISTRATIONS_FLAG | — | — | — | — | — | — |
| 2 | COLL_TAX_AUTHORITY_ID | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DEFAULT_FLG_EFFECTIVE_FROM | — | — | — | — | — | — |
| 6 | DEFAULT_FLG_EFFECTIVE_TO | — | — | — | — | — | — |
| 7 | DEFAULT_JURISDICTION_FLAG | — | — | — | — | — | — |
| 8 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 9 | EFFECTIVE_TO | — | — | — | — | — | — |
| 10 | INNER_CITY_JURISDICTION_FLAG | — | — | — | — | — | — |
| 11 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 12 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 13 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 14 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 15 | PRECEDENCE_LEVEL | — | — | — | — | — | — |
| 16 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 17 | PROGRAM_LOGIN_ID | — | — | — | — | — | — |
| 18 | PROGRAM_NAME | — | — | — | — | — | — |
| 19 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 20 | REP_TAX_AUTHORITY_ID | — | — | — | — | — | — |
| 21 | REQUEST_ID | — | — | — | — | — | — |
| 22 | TAX | — | — | — | — | — | — |
| 23 | TAX_ACCT_SRC_JURISDICT_ID | — | — | — | — | — | — |
| 24 | TAX_EXMPT_SRC_JURISDICT_ID | — | — | — | — | — | — |
| 25 | TAX_JURISDICTION_CODE | — | — | — | — | — | — |
| 26 | TAX_JURISDICTION_ID | — | — | — | — | — | — |
| 27 | TAX_JURISDICTION_NAME | — | — | — | — | — | — |
| 28 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 29 | THRSHLD_SCHEDULE_GRP_LVL_FLAG | — | — | — | — | — | — |
| 30 | WHT_BUCKET_LEVEL_FLAG | — | — | — | — | — | — |
| 31 | ZONE_GEOGRAPHY_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxexemption|SiteTaxExemption]] (AR · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_FROM | TaxJurisdictionEffectiveFrom | — |
| EFFECTIVE_TO | TaxJurisdictionEffectiveTo | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber | — |
| TAX | TaxJurisdictionTax | — |
| TAX_ACCT_SRC_JURISDICT_ID | TaxJurisdictionTaxAcctSrcJurisdictId | — |
| TAX_EXMPT_SRC_JURISDICT_ID | TaxJurisdictionTaxExmptSrcJurisdictId | — |
| TAX_JURISDICTION_CODE | TaxJurisdictionTaxJurisdictionCode | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTaxJurisdictionId | — |
| TAX_JURISDICTION_NAME | TaxJurisdictionTaxJurisdictionName | ✅ |
| TAX_REGIME_CODE | TaxJurisdictionTaxRegimeCode | — |

### [[sitetaxregistration|SiteTaxRegistration]] (AR · BICC: 2/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_TAX_REGISTRATIONS_FLAG | TaxJurisdictionAllowTaxRegistrationsFlag | — |
| COLL_TAX_AUTHORITY_ID | TaxJurisdictionCollTaxAuthorityId | — |
| CREATED_BY | TaxJurisdictionCreatedBy | — |
| CREATION_DATE | TaxJurisdictionCreationDate | — |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxJurisdictionDefaultFlgEffectiveFrom | — |
| DEFAULT_FLG_EFFECTIVE_TO | TaxJurisdictionDefaultFlgEffectiveTo | — |
| DEFAULT_JURISDICTION_FLAG | TaxJurisdictionDefaultJurisdictionFlag | — |
| EFFECTIVE_FROM | TaxJurisdictionEffectiveFrom | — |
| EFFECTIVE_TO | TaxJurisdictionEffectiveTo | — |
| INNER_CITY_JURISDICTION_FLAG | TaxJurisdictionInnerCityJurisdictionFlag | — |
| LAST_UPDATE_DATE | TaxJurisdictionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxJurisdictionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber3 | — |
| PRECEDENCE_LEVEL | TaxJurisdictionPrecedenceLevel | — |
| PROGRAM_APP_NAME | TaxJurisdictionProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxJurisdictionProgramLoginId | — |
| PROGRAM_NAME | TaxJurisdictionProgramName | — |
| RECORD_TYPE_CODE | TaxJurisdictionRecordTypeCode | — |
| REP_TAX_AUTHORITY_ID | TaxJurisdictionRepTaxAuthorityId | — |
| REQUEST_ID | TaxJurisdictionRequestId | — |
| TAX | TaxJurisdictionTax | — |
| TAX_ACCT_SRC_JURISDICT_ID | TaxJurisdictionTaxAcctSrcJurisdictId | — |
| TAX_EXMPT_SRC_JURISDICT_ID | TaxJurisdictionTaxExmptSrcJurisdictId | — |
| TAX_JURISDICTION_CODE | TaxJurisdictionTaxJurisdictionCode | — |
| TAX_JURISDICTION_ID | TaxJurisdictionTaxJurisdictionId | — |
| TAX_JURISDICTION_NAME | TaxJurisdictionTaxJurisdictionName | ✅ |
| TAX_REGIME_CODE | TaxJurisdictionTaxRegimeCode | — |
| THRSHLD_SCHEDULE_GRP_LVL_FLAG | TaxJurisdictionThrshldScheduleGrpLvlFlag | — |
| WHT_BUCKET_LEVEL_FLAG | TaxJurisdictionWhtBucketLevelFlag | — |
| ZONE_GEOGRAPHY_ID | TaxJurisdictionZoneGeographyId | — |

### [[taxexemption|TaxExemption]] (AR · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_FROM | TaxJurisdictionEffectiveFrom | — |
| EFFECTIVE_TO | TaxJurisdictionEffectiveTo | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber | — |
| TAX | TaxJurisdictionTax | — |
| TAX_ACCT_SRC_JURISDICT_ID | TaxJurisdictionTaxAcctSrcJurisdictId | — |
| TAX_EXMPT_SRC_JURISDICT_ID | TaxJurisdictionTaxExmptSrcJurisdictId | — |
| TAX_JURISDICTION_CODE | TaxJurisdictionTaxJurisdictionCode | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTaxJurisdictionId | — |
| TAX_JURISDICTION_NAME | TaxJurisdictionTaxJurisdictionName | ✅ |
| TAX_REGIME_CODE | TaxJurisdictionTaxRegimeCode | — |

### [[taxregistration|TaxRegistration]] (AR · BICC: 3/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_TAX_REGISTRATIONS_FLAG | TaxJurisdictionAllowTaxRegistrationsFlag | — |
| COLL_TAX_AUTHORITY_ID | TaxJurisdictionCollTaxAuthorityId | — |
| CREATED_BY | TaxJurisdictionCreatedBy | — |
| CREATION_DATE | TaxJurisdictionCreationDate | — |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxJurisdictionDefaultFlgEffectiveFrom | — |
| DEFAULT_FLG_EFFECTIVE_TO | TaxJurisdictionDefaultFlgEffectiveTo | — |
| DEFAULT_JURISDICTION_FLAG | TaxJurisdictionDefaultJurisdictionFlag | — |
| EFFECTIVE_FROM | TaxJurisdictionEffectiveFrom | — |
| EFFECTIVE_TO | TaxJurisdictionEffectiveTo | — |
| INNER_CITY_JURISDICTION_FLAG | TaxJurisdictionInnerCityJurisdictionFlag | — |
| LAST_UPDATE_DATE | TaxJurisdictionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxJurisdictionLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber2 | — |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber3 | — |
| PRECEDENCE_LEVEL | TaxJurisdictionPrecedenceLevel | — |
| PROGRAM_APP_NAME | TaxJurisdictionProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxJurisdictionProgramLoginId | — |
| PROGRAM_NAME | TaxJurisdictionProgramName | — |
| RECORD_TYPE_CODE | TaxJurisdictionRecordTypeCode | — |
| REP_TAX_AUTHORITY_ID | TaxJurisdictionRepTaxAuthorityId | — |
| REQUEST_ID | TaxJurisdictionRequestId | — |
| TAX | TaxJurisdictionTax | — |
| TAX_ACCT_SRC_JURISDICT_ID | TaxJurisdictionTaxAcctSrcJurisdictId | — |
| TAX_EXMPT_SRC_JURISDICT_ID | TaxJurisdictionTaxExmptSrcJurisdictId | — |
| TAX_JURISDICTION_CODE | TaxJurisdictionTaxJurisdictionCode | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTaxJurisdictionId | — |
| TAX_JURISDICTION_NAME | TaxJurisdictionTaxJurisdictionName | ✅ |
| TAX_REGIME_CODE | TaxJurisdictionTaxRegimeCode | — |
| THRSHLD_SCHEDULE_GRP_LVL_FLAG | TaxJurisdictionThrshldScheduleGrpLvlFlag | — |
| WHT_BUCKET_LEVEL_FLAG | TaxJurisdictionWhtBucketLevelFlag | — |
| ZONE_GEOGRAPHY_ID | TaxJurisdictionZoneGeographyId | — |
