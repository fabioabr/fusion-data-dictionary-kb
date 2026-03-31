---
id: DOC-OTHER-PVO-OfferSalaryPVO
doc_type: system-doc
title: "OfferSalaryPVO — PVO Cross-Module"
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
  - OfferSalaryPVO
  - offersalarypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OfferSalaryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Offer Salary. Acessa as tabelas: CMP_PRE_SALARY_V, CMP_SALARY, CMP_SALARY_BASES (+4).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.OfferSalaryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 108 | 7 | 1 | 19 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_pre_salary_v|CMP_PRE_SALARY_V]] — 26 atributos (7 BICC)
- [[cmp_salary|CMP_SALARY]] — 22 atributos (1 PKs, 4 BICC)
- [[cmp_salary_bases|CMP_SALARY_BASES]] — 20 atributos (3 BICC)
- [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]] — 11 atributos (2 BICC)
- [[irc_offers|IRC_OFFERS]] — 7 atributos
- [[pay_input_values_tl|PAY_INPUT_VALUES_TL]] — 12 atributos (1 BICC)
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 10 atributos (2 BICC)

---

## ⚙️ Atributos

### [[cmp_pre_salary_v|CMP_PRE_SALARY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnnualizationFactor | ANNUALIZATION_FACTOR | — | — |
| 2 | AssignmentId | ASSIGNMENT_ID | — | — |
| 3 | Comparatio | COMPARATIO | — | — |
| 4 | DateFrom | DATE_FROM | — | ✅ |
| 5 | DateTo | DATE_TO | — | ✅ |
| 6 | ElementTypeId | ELEMENT_TYPE_ID | — | — |
| 7 | Maximum | MAXIMUM | — | ✅ |
| 8 | MidValue | MID_VALUE | — | ✅ |
| 9 | Minimum | MINIMUM | — | ✅ |
| 10 | PayrollAnnualFactor | PAYROLL_ANNUAL_FACTOR | — | ✅ |
| 11 | PayrollFrequencyCode | PAYROLL_FREQUENCY_CODE | — | ✅ |
| 12 | Percentile | PERCENTILE | — | — |
| 13 | PrevAmt | PREV_AMT | — | — |
| 14 | PrevCurrCode | PREV_CURR_CODE | — | — |
| 15 | PrevSalaryBasis | PREV_SALARY_BASIS | — | — |
| 16 | Quartile | QUARTILE | — | — |
| 17 | Quintile | QUINTILE | — | — |
| 18 | RateFrequency | RATE_FREQUENCY | — | — |
| 19 | RateId | RATE_ID | — | — |
| 20 | RateName | RATE_NAME | — | — |
| 21 | RateObjectType | RATE_OBJECT_TYPE | — | — |
| 22 | RateType | RATE_TYPE | — | — |
| 23 | SalaryAmount | SALARY_AMOUNT | — | — |
| 24 | SalaryChangeAmt | SALARY_CHANGE_AMT | — | — |
| 25 | SalaryChangePer | SALARY_CHANGE_PER | — | — |
| 26 | SalaryId1 | SALARY_ID | — | — |

### [[cmp_salary|CMP_SALARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryEffectiveEndDate | DATE_TO | — | — |
| 2 | SalaryEffectiveStartDate | DATE_FROM | — | — |
| 3 | SalaryId | SALARY_ID | 🔑 | ✅ |
| 4 | SalaryPEOActionId | ACTION_ID | — | — |
| 5 | SalaryPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 6 | SalaryPEOActionReasonId | ACTION_REASON_ID | — | — |
| 7 | SalaryPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 8 | SalaryPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | SalaryPEOCreatedBy | CREATED_BY | — | — |
| 10 | SalaryPEOCreationDate | CREATION_DATE | — | — |
| 11 | SalaryPEODateFrom | DATE_FROM | — | — |
| 12 | SalaryPEODateTo | DATE_TO | — | — |
| 13 | SalaryPEOElementEntryId | ELEMENT_ENTRY_ID | — | — |
| 14 | SalaryPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | SalaryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | SalaryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | SalaryPEOMultipleComponents | MULTIPLE_COMPONENTS | — | ✅ |
| 18 | SalaryPEONextSalReviewDate | NEXT_SAL_REVIEW_DATE | — | — |
| 19 | SalaryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | SalaryPEOSalaryAmount | SALARY_AMOUNT | — | ✅ |
| 21 | SalaryPEOSalaryApproved | SALARY_APPROVED | — | — |
| 22 | SalaryPEOSalaryBasisId | SALARY_BASIS_ID | — | — |

### [[cmp_salary_bases|CMP_SALARY_BASES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasesPEOAnnualizedHours | ANNUALIZED_HOURS | — | — |
| 2 | SalaryBasesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | SalaryBasesPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 4 | SalaryBasesPEOComponentUsage | COMPONENT_USAGE | — | — |
| 5 | SalaryBasesPEOCreatedBy1 | CREATED_BY | — | — |
| 6 | SalaryBasesPEOCreationDate1 | CREATION_DATE | — | — |
| 7 | SalaryBasesPEOElementTypeId | ELEMENT_TYPE_ID | — | — |
| 8 | SalaryBasesPEOGradeAnnualizationFactor | GRADE_ANNUALIZATION_FACTOR | — | — |
| 9 | SalaryBasesPEOGradeRateBasisCode | GRADE_RATE_BASIS_CODE | — | — |
| 10 | SalaryBasesPEOGradeRateId | GRADE_RATE_ID | — | — |
| 11 | SalaryBasesPEOInputValueId | INPUT_VALUE_ID | — | — |
| 12 | SalaryBasesPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 13 | SalaryBasesPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 14 | SalaryBasesPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 15 | SalaryBasesPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 16 | SalaryBasesPEOName | NAME | — | — |
| 17 | SalaryBasesPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 18 | SalaryBasesPEOSalaryAnnualizationFactor | SALARY_ANNUALIZATION_FACTOR | — | ✅ |
| 19 | SalaryBasesPEOSalaryBasisCode | SALARY_BASIS_CODE | — | ✅ |
| 20 | SalaryBasesPEOSalaryBasisId1 | SALARY_BASIS_ID | — | — |

### [[cmp_salary_bases_tl|CMP_SALARY_BASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SalaryBasesTLPEOCreatedBy2 | CREATED_BY | — | — |
| 2 | SalaryBasesTLPEOCreationDate2 | CREATION_DATE | — | — |
| 3 | SalaryBasesTLPEODescription | DESCRIPTION | — | — |
| 4 | SalaryBasesTLPEOLanguage | LANGUAGE | — | — |
| 5 | SalaryBasesTLPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 6 | SalaryBasesTLPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 7 | SalaryBasesTLPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 8 | SalaryBasesTLPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 9 | SalaryBasesTLPEOSalaryBasisId2 | SALARY_BASIS_ID | — | — |
| 10 | SalaryBasesTLPEOSalaryBasisName | SALARY_BASIS_NAME | — | ✅ |
| 11 | SalaryBasesTLPEOSourceLang | SOURCE_LANG | — | — |

### [[irc_offers|IRC_OFFERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OffersPEOAssignmentOfferId | ASSIGNMENT_OFFER_ID | — | — |
| 2 | OffersPEOHiringManagerId | HIRING_MANAGER_ID | — | — |
| 3 | OffersPEOManagerAssignmentId | MANAGER_ASSIGNMENT_ID | — | — |
| 4 | OffersPEOOfferId | OFFER_ID | — | — |
| 5 | OffersPEOPersonId1 | PERSON_ID | — | — |
| 6 | OffersPEORecruiterAssignmentId | RECRUITER_ASSIGNMENT_ID | — | — |
| 7 | OffersPEORecruiterId | RECRUITER_ID | — | — |

### [[pay_input_values_tl|PAY_INPUT_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InputValueTranslationPEOCreatedBy3 | CREATED_BY | — | — |
| 2 | InputValueTranslationPEOCreationDate3 | CREATION_DATE | — | — |
| 3 | InputValueTranslationPEOInputValueId1 | INPUT_VALUE_ID | — | — |
| 4 | InputValueTranslationPEOInputValueId2 | INPUT_VALUE_ID | — | — |
| 5 | InputValueTranslationPEOLanguage2 | LANGUAGE | — | — |
| 6 | InputValueTranslationPEOLanguage3 | LANGUAGE | — | — |
| 7 | InputValueTranslationPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | InputValueTranslationPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 9 | InputValueTranslationPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 10 | InputValueTranslationPEOName1 | NAME | — | — |
| 11 | InputValueTranslationPEOObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 12 | InputValueTranslationPEOSourceLang1 | SOURCE_LANG | — | — |

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentPEOAssignmentId1 | ASSIGNMENT_ID | — | — |
| 2 | AssignmentPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentPEOEffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 4 | AssignmentPEOEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 5 | AssignmentPEOEffectiveLatestChange1 | EFFECTIVE_LATEST_CHANGE | — | — |
| 6 | AssignmentPEOEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 7 | AssignmentPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | AssignmentPEOEffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 9 | AssignmentPEOPersonId | PERSON_ID | — | — |
| 10 | EffectiveSequence1 | EFFECTIVE_SEQUENCE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
