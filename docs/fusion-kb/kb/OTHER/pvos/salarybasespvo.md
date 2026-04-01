---
id: DOC-OTHER-PVO-SalaryBasesPVO
doc_type: system-doc
title: "SalaryBasesPVO — PVO Cross-Module"
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
  - SalaryBasesPVO
  - salarybasespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryBasesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Salary Bases. Acessa as tabelas: CMP_SALARY_BASES, CMP_SALARY_BASES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.SalaryBasesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 2 | 1 | 4 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary_bases|CMP_SALARY_BASES]] — 29 atributos (1 PKs, 2 BICC)
- [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]] — 11 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cmp_salary_bases|CMP_SALARY_BASES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CalculationMode | CALCULATION_MODE | — | — |
| 2 | SalaryBasesPEOAmountDecimalPrecision | AMOUNT_DECIMAL_PRECISION | — | — |
| 3 | SalaryBasesPEOAmountRoundingCode | AMOUNT_ROUNDING_CODE | — | — |
| 4 | SalaryBasesPEOAnnualRoundingCode | ANNUAL_ROUNDING_CODE | — | — |
| 5 | SalaryBasesPEOAnnualizedHours | ANNUALIZED_HOURS | — | — |
| 6 | SalaryBasesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 7 | SalaryBasesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 8 | SalaryBasesPEOCode | CODE | — | — |
| 9 | SalaryBasesPEOComponentUsage | COMPONENT_USAGE | — | — |
| 10 | SalaryBasesPEOCreatedBy | CREATED_BY | — | — |
| 11 | SalaryBasesPEOCreationDate | CREATION_DATE | — | — |
| 12 | SalaryBasesPEOElementTypeId | ELEMENT_TYPE_ID | — | — |
| 13 | SalaryBasesPEOGradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | — |
| 14 | SalaryBasesPEOGradeRateBasisCode | GRADE_RATE_BASIS_CODE | — | — |
| 15 | SalaryBasesPEOGradeRateId | GRADE_RATE_ID | — | — |
| 16 | SalaryBasesPEOInputValueId | INPUT_VALUE_ID | — | — |
| 17 | SalaryBasesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | SalaryBasesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | SalaryBasesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | SalaryBasesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 21 | SalaryBasesPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 22 | SalaryBasesPEOName | NAME | — | — |
| 23 | SalaryBasesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | SalaryBasesPEORangeRoundingCode | RANGE_ROUNDING_CODE | — | — |
| 25 | SalaryBasesPEOSalaryAnnualizationFactor | SALARY_ANNUALIZATION_FACTOR | — | — |
| 26 | SalaryBasesPEOSalaryBasisCode | SALARY_BASIS_CODE | — | — |
| 27 | SalaryBasesPEOSalaryBasisType | SALARY_BASIS_TYPE | — | — |
| 28 | SalaryBasesPEOStatus | STATUS | — | — |
| 29 | SalaryBasisId | SALARY_BASIS_ID | 🔑 | ✅ |

### [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasesTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | SalaryBasesTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | SalaryBasesTLPEODescription | DESCRIPTION | — | — |
| 4 | SalaryBasesTLPEOLanguage | LANGUAGE | — | — |
| 5 | SalaryBasesTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SalaryBasesTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SalaryBasesTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SalaryBasesTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SalaryBasesTLPEOSalaryBasisId | SALARY_BASIS_ID | — | — |
| 10 | SalaryBasesTLPEOSalaryBasisName | SALARY_BASIS_NAME | — | ✅ |
| 11 | SalaryBasesTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
