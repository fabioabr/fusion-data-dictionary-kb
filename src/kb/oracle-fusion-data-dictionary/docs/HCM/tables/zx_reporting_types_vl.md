---
id: DOC-HCM-906
doc_type: system-doc
title: "ZX_REPORTING_TYPES_VL — (título a preencher)"
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
  - ZX_REPORTING_TYPES_VL
  - zx_reporting_types_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_REPORTING_TYPES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COUNTRY_CODE | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 5 | EFFECTIVE_TO | — | — | — | — | — | — |
| 6 | FORMAT_MASK | — | — | — | — | — | — |
| 7 | HAS_REPORTING_CODES_FLAG | — | — | — | — | — | — |
| 8 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 9 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 10 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 11 | LEGAL_MESSAGE_FLAG | — | — | — | — | — | — |
| 12 | MAX_LENGTH | — | — | — | — | — | — |
| 13 | MIN_LENGTH | — | — | — | — | — | — |
| 14 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 15 | PROGRAM_APP_NAME | — | — | — | — | — | — |
| 16 | PROGRAM_LOGIN_ID | — | — | — | — | — | — |
| 17 | PROGRAM_NAME | — | — | — | — | — | — |
| 18 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 19 | REGISTRATION_TYPE | — | — | — | — | — | — |
| 20 | REPORTING_TYPE_CODE | — | — | — | — | — | — |
| 21 | REPORTING_TYPE_DATATYPE_CODE | — | — | — | — | — | — |
| 22 | REPORTING_TYPE_ID | — | — | — | — | — | — |
| 23 | REPORTING_TYPE_NAME | — | — | — | — | — | — |
| 24 | REQUEST_ID | — | — | — | — | — | — |
| 25 | TAX | — | — | — | — | — | — |
| 26 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 27 | UNIQUENESS_VALIDATION_LEVEL | — | — | — | — | — | — |
| 28 | VALIDATION_LEVEL | — | — | — | — | — | — |
| 29 | VALIDATION_ROUTINE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxreportingcode|SiteTaxReportingCode]] (AR · BICC: 3/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | TaxReportingTypeCountryCode | — |
| CREATED_BY | TaxReportingTypeCreatedBy | — |
| CREATION_DATE | TaxReportingTypeCreationDate | — |
| EFFECTIVE_FROM | TaxReportingTypeEffectiveFrom | — |
| EFFECTIVE_TO | TaxReportingTypeEffectiveTo | — |
| FORMAT_MASK | TaxReportingTypeFormatMask | — |
| HAS_REPORTING_CODES_FLAG | TaxReportingTypeHasReportingCodesFlag | — |
| LAST_UPDATE_DATE | TaxReportingTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxReportingTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxReportingTypeLastUpdatedBy | — |
| LEGAL_MESSAGE_FLAG | TaxReportingTypeLegalMessageFlag | — |
| MAX_LENGTH | TaxReportingTypeMaxLength | — |
| MIN_LENGTH | TaxReportingTypeMinLength | — |
| OBJECT_VERSION_NUMBER | TaxReportingTypeObjectVersionNumber | — |
| PROGRAM_APP_NAME | TaxReportingTypeProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxReportingTypeProgramLoginId | — |
| PROGRAM_NAME | TaxReportingTypeProgramName | — |
| RECORD_TYPE_CODE | TaxReportingTypeRecordTypeCode | — |
| REGISTRATION_TYPE | TaxReportingTypeRegistrationType | — |
| REPORTING_TYPE_CODE | TaxReportingTypeReportingTypeCode | ✅ |
| REPORTING_TYPE_DATATYPE_CODE | TaxReportingTypeReportingTypeDatatypeCode | ✅ |
| REPORTING_TYPE_ID | TaxReportingTypeReportingTypeId | — |
| REPORTING_TYPE_NAME | TaxReportingTypeReportingTypeName | — |
| REQUEST_ID | TaxReportingTypeRequestId | — |
| TAX | TaxReportingTypeTax | — |
| TAX_REGIME_CODE | TaxReportingTypeTaxRegimeCode | — |
| UNIQUENESS_VALIDATION_LEVEL | TaxReportingTypeUniquenessValidationLevel | — |
| VALIDATION_LEVEL | TaxReportingTypeValidationLevel | — |
| VALIDATION_ROUTINE | TaxReportingTypeValidationRoutine | — |

### [[taxreportingcode|TaxReportingCode]] (AR · BICC: 3/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | TaxReportingTypeCountryCode | — |
| CREATED_BY | TaxReportingTypeCreatedBy | — |
| CREATION_DATE | TaxReportingTypeCreationDate | — |
| EFFECTIVE_FROM | TaxReportingTypeEffectiveFrom | — |
| EFFECTIVE_TO | TaxReportingTypeEffectiveTo | — |
| FORMAT_MASK | TaxReportingTypeFormatMask | — |
| HAS_REPORTING_CODES_FLAG | TaxReportingTypeHasReportingCodesFlag | — |
| LAST_UPDATE_DATE | TaxReportingTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxReportingTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxReportingTypeLastUpdatedBy | — |
| LEGAL_MESSAGE_FLAG | TaxReportingTypeLegalMessageFlag | — |
| MAX_LENGTH | TaxReportingTypeMaxLength | — |
| MIN_LENGTH | TaxReportingTypeMinLength | — |
| OBJECT_VERSION_NUMBER | TaxReportingTypeObjectVersionNumber | — |
| PROGRAM_APP_NAME | TaxReportingTypeProgramAppName | — |
| PROGRAM_LOGIN_ID | TaxReportingTypeProgramLoginId | — |
| PROGRAM_NAME | TaxReportingTypeProgramName | — |
| RECORD_TYPE_CODE | TaxReportingTypeRecordTypeCode | — |
| REGISTRATION_TYPE | TaxReportingTypeRegistrationType | — |
| REPORTING_TYPE_CODE | TaxReportingTypeReportingTypeCode | ✅ |
| REPORTING_TYPE_DATATYPE_CODE | TaxReportingTypeReportingTypeDatatypeCode | ✅ |
| REPORTING_TYPE_ID | TaxReportingTypeReportingTypeId | — |
| REPORTING_TYPE_NAME | TaxReportingTypeReportingTypeName | — |
| REQUEST_ID | TaxReportingTypeRequestId | — |
| TAX | TaxReportingTypeTax | — |
| TAX_REGIME_CODE | TaxReportingTypeTaxRegimeCode | — |
| UNIQUENESS_VALIDATION_LEVEL | TaxReportingTypeUniquenessValidationLevel | — |
| VALIDATION_LEVEL | TaxReportingTypeValidationLevel | — |
| VALIDATION_ROUTINE | TaxReportingTypeValidationRoutine | — |
