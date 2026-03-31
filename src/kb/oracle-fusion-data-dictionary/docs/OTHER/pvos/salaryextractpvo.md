---
id: DOC-OTHER-PVO-SalaryExtractPVO
doc_type: system-doc
title: "SalaryExtractPVO — PVO Cross-Module"
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
  - SalaryExtractPVO
  - salaryextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SalaryExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Salary Extract. Acessa as tabelas: CMP_SALARY.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmCompBiccExtractAM.SalaryExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 160 | 1 | 1 | 90 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_salary|CMP_SALARY]] — 160 atributos (1 PKs, 90 BICC)

---

## ⚙️ Atributos

### [[cmp_salary|CMP_SALARY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionId | ACTION_ID | — | ✅ |
| 2 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 3 | ActionReasonId | ACTION_REASON_ID | — | ✅ |
| 4 | AdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 5 | AdjustmentAmountScale | ADJUSTMENT_AMOUNT_SCALE | — | ✅ |
| 6 | AdjustmentPercent | ADJUSTMENT_PERCENT | — | ✅ |
| 7 | AdjustmentPercentScale | ADJUSTMENT_PERCENT_SCALE | — | ✅ |
| 8 | AmountRoundingCode | AMOUNT_ROUNDING_CODE | — | ✅ |
| 9 | AnnualFtSalary | ANNUAL_FT_SALARY | — | ✅ |
| 10 | AnnualRoundingCode | ANNUAL_ROUNDING_CODE | — | ✅ |
| 11 | AnnualSalary | ANNUAL_SALARY | — | ✅ |
| 12 | AssigGradeLadderId | ASSIG_GRADE_LADDER_ID | — | ✅ |
| 13 | AssigGradeStepId | ASSIG_GRADE_STEP_ID | — | ✅ |
| 14 | AssigLocationId | ASSIG_LOCATION_ID | — | ✅ |
| 15 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 16 | AssignmentType | ASSIGNMENT_TYPE | — | ✅ |
| 17 | Attribute1 | ATTRIBUTE1 | — | — |
| 18 | Attribute10 | ATTRIBUTE10 | — | — |
| 19 | Attribute11 | ATTRIBUTE11 | — | — |
| 20 | Attribute12 | ATTRIBUTE12 | — | — |
| 21 | Attribute13 | ATTRIBUTE13 | — | — |
| 22 | Attribute14 | ATTRIBUTE14 | — | — |
| 23 | Attribute15 | ATTRIBUTE15 | — | — |
| 24 | Attribute16 | ATTRIBUTE16 | — | — |
| 25 | Attribute17 | ATTRIBUTE17 | — | — |
| 26 | Attribute18 | ATTRIBUTE18 | — | — |
| 27 | Attribute19 | ATTRIBUTE19 | — | — |
| 28 | Attribute2 | ATTRIBUTE2 | — | — |
| 29 | Attribute20 | ATTRIBUTE20 | — | — |
| 30 | Attribute21 | ATTRIBUTE21 | — | — |
| 31 | Attribute22 | ATTRIBUTE22 | — | — |
| 32 | Attribute23 | ATTRIBUTE23 | — | — |
| 33 | Attribute24 | ATTRIBUTE24 | — | — |
| 34 | Attribute25 | ATTRIBUTE25 | — | — |
| 35 | Attribute26 | ATTRIBUTE26 | — | — |
| 36 | Attribute27 | ATTRIBUTE27 | — | — |
| 37 | Attribute28 | ATTRIBUTE28 | — | — |
| 38 | Attribute29 | ATTRIBUTE29 | — | — |
| 39 | Attribute3 | ATTRIBUTE3 | — | — |
| 40 | Attribute30 | ATTRIBUTE30 | — | — |
| 41 | Attribute4 | ATTRIBUTE4 | — | — |
| 42 | Attribute5 | ATTRIBUTE5 | — | — |
| 43 | Attribute6 | ATTRIBUTE6 | — | — |
| 44 | Attribute7 | ATTRIBUTE7 | — | — |
| 45 | Attribute8 | ATTRIBUTE8 | — | — |
| 46 | Attribute9 | ATTRIBUTE9 | — | — |
| 47 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 48 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 49 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 50 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 51 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 52 | AttributeDate13 | ATTRIBUTE_DATE13 | — | — |
| 53 | AttributeDate14 | ATTRIBUTE_DATE14 | — | — |
| 54 | AttributeDate15 | ATTRIBUTE_DATE15 | — | — |
| 55 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 56 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 57 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 58 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 59 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 60 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 61 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 62 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 63 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 64 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 65 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 66 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 67 | AttributeNumber13 | ATTRIBUTE_NUMBER13 | — | — |
| 68 | AttributeNumber14 | ATTRIBUTE_NUMBER14 | — | — |
| 69 | AttributeNumber15 | ATTRIBUTE_NUMBER15 | — | — |
| 70 | AttributeNumber16 | ATTRIBUTE_NUMBER16 | — | — |
| 71 | AttributeNumber17 | ATTRIBUTE_NUMBER17 | — | — |
| 72 | AttributeNumber18 | ATTRIBUTE_NUMBER18 | — | — |
| 73 | AttributeNumber19 | ATTRIBUTE_NUMBER19 | — | — |
| 74 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 75 | AttributeNumber20 | ATTRIBUTE_NUMBER20 | — | — |
| 76 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 77 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 78 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 79 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 80 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 81 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 82 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 83 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 84 | BusinessUnitId | BUSINESS_UNIT_ID | — | ✅ |
| 85 | CompaRatio | COMPA_RATIO | — | ✅ |
| 86 | CompaRatioScale | COMPA_RATIO_SCALE | — | ✅ |
| 87 | ComponentUsage | COMPONENT_USAGE | — | ✅ |
| 88 | CreatedBy | CREATED_BY | — | ✅ |
| 89 | CreationDate | CREATION_DATE | — | ✅ |
| 90 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 91 | DateFrom | DATE_FROM | — | ✅ |
| 92 | DateTo | DATE_TO | — | ✅ |
| 93 | DisableCompaRatio | DISABLE_COMPA_RATIO | — | ✅ |
| 94 | DisableQuartile | DISABLE_QUARTILE | — | ✅ |
| 95 | DisableQuintile | DISABLE_QUINTILE | — | ✅ |
| 96 | DisableRangePosition | DISABLE_RANGE_POSITION | — | ✅ |
| 97 | ElementEntryId | ELEMENT_ENTRY_ID | — | ✅ |
| 98 | ElementTypeId | ELEMENT_TYPE_ID | — | ✅ |
| 99 | ElementUsageLevel | ELEMENT_USAGE_LEVEL | — | ✅ |
| 100 | ForcedRanking | FORCED_RANKING | — | ✅ |
| 101 | FteImpact | FTE_IMPACT | — | ✅ |
| 102 | FteValue | FTE_VALUE | — | ✅ |
| 103 | GeographyId | GEOGRAPHY_ID | — | ✅ |
| 104 | GeographyTypeId | GEOGRAPHY_TYPE_ID | — | ✅ |
| 105 | GradeId | GRADE_ID | — | ✅ |
| 106 | GradeRateMinimumLimit | GRADE_RATE_MINIMUM_LIMIT | — | ✅ |
| 107 | InputValueId | INPUT_VALUE_ID | — | ✅ |
| 108 | JobId | JOB_ID | — | ✅ |
| 109 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 110 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 111 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 112 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 113 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 114 | MiscComment1 | MISC_COMMENT1 | — | — |
| 115 | MiscComment2 | MISC_COMMENT2 | — | — |
| 116 | MiscComment3 | MISC_COMMENT3 | — | — |
| 117 | MiscComment4 | MISC_COMMENT4 | — | — |
| 118 | MultipleComponents | MULTIPLE_COMPONENTS | — | ✅ |
| 119 | NextPerfReviewDate | NEXT_PERF_REVIEW_DATE | — | ✅ |
| 120 | NextSalReviewDate | NEXT_SAL_REVIEW_DATE | — | ✅ |
| 121 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 122 | PayrollFactor | PAYROLL_FACTOR | — | ✅ |
| 123 | PayrollFrequencyCode | PAYROLL_FREQUENCY_CODE | — | ✅ |
| 124 | PerformanceRating | PERFORMANCE_RATING | — | ✅ |
| 125 | PerformanceReviewId | PERFORMANCE_REVIEW_ID | — | ✅ |
| 126 | PersonId | PERSON_ID | — | ✅ |
| 127 | Quartile | QUARTILE | — | ✅ |
| 128 | Quintile | QUINTILE | — | ✅ |
| 129 | RangeAnalyticsForEmp | RANGE_ANALYTICS_FOR_EMP | — | ✅ |
| 130 | RangeAnalyticsForMgr | RANGE_ANALYTICS_FOR_MGR | — | ✅ |
| 131 | RangeErrorWarning | RANGE_ERROR_WARNING | — | ✅ |
| 132 | RangePosition | RANGE_POSITION | — | ✅ |
| 133 | RangePositionScale | RANGE_POSITION_SCALE | — | ✅ |
| 134 | RangeRoundingCode | RANGE_ROUNDING_CODE | — | ✅ |
| 135 | RateDefaultAmount | RATE_DEFAULT_AMOUNT | — | ✅ |
| 136 | RateFactor | RATE_FACTOR | — | ✅ |
| 137 | RateId | RATE_ID | — | ✅ |
| 138 | RateMaxAmount | RATE_MAX_AMOUNT | — | ✅ |
| 139 | RateMidAmount | RATE_MID_AMOUNT | — | ✅ |
| 140 | RateMinAmount | RATE_MIN_AMOUNT | — | ✅ |
| 141 | ReviewDate | REVIEW_DATE | — | ✅ |
| 142 | SalaryAmount | SALARY_AMOUNT | — | ✅ |
| 143 | SalaryAmountScale | SALARY_AMOUNT_SCALE | — | ✅ |
| 144 | SalaryApproved | SALARY_APPROVED | — | ✅ |
| 145 | SalaryBasisCode | SALARY_BASIS_CODE | — | ✅ |
| 146 | SalaryBasisId | SALARY_BASIS_ID | — | ✅ |
| 147 | SalaryBasisType | SALARY_BASIS_TYPE | — | ✅ |
| 148 | SalaryEffectiveEndDate | DATE_TO | — | ✅ |
| 149 | SalaryEffectiveStartDate | DATE_FROM | — | ✅ |
| 150 | SalaryFactor | SALARY_FACTOR | — | ✅ |
| 151 | SalaryId | SALARY_ID | 🔑 | ✅ |
| 152 | SalaryJustification | SALARY_JUSTIFICATION | — | ✅ |
| 153 | SalaryRangeScale | SALARY_RANGE_SCALE | — | ✅ |
| 154 | SalaryReasonCode | SALARY_REASON_CODE | — | ✅ |
| 155 | SalaryTransactionStatus | SALARY_TRANSACTION_STATUS | — | ✅ |
| 156 | TotalBasePay | TOTAL_BASE_PAY | — | ✅ |
| 157 | TotalComponentAdjAmt | TOTAL_COMPONENT_ADJ_AMT | — | ✅ |
| 158 | TotalComponentAdjPercent | TOTAL_COMPONENT_ADJ_PERCENT | — | ✅ |
| 159 | WorkAtHome | WORK_AT_HOME | — | ✅ |
| 160 | ZoneGradeRateId | ZONE_GRADE_RATE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
