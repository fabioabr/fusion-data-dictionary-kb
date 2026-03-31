---
id: DOC-PO-PVO-FundingPositionPVO
doc_type: system-doc
title: "FundingPositionPVO — PVO Purchasing"
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
  - FundingPositionPVO
  - fundingpositionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FundingPositionPVO

## 📌 Visão Geral

Extrai posições de funding (dotação orçamentária) vinculadas a cargos, incluindo organização, incumbente e hierarquia. Essencial para controle orçamentário de posições e planejamento de headcount.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.FundingPositionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 109 | 5 | 3 | 16 | 15% |

---

## 🔗 Tabelas Relacionadas

- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 18 atributos (2 BICC)
- [[hr_all_positions_f|HR_ALL_POSITIONS_F]] — 54 atributos (3 BICC)
- [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]] — 12 atributos (3 BICC)
- [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]] — 12 atributos (3 BICC)
- [[per_pos_funding_positions_f|PER_POS_FUNDING_POSITIONS_F]] — 13 atributos (3 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | BusinessUnitPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | BusinessUnitPEOCostAllocationKeyflexId | COST_ALLOCATION_KEYFLEX_ID | — | — |
| 4 | BusinessUnitPEOCreatedBy | CREATED_BY | — | — |
| 5 | BusinessUnitPEOCreationDate | CREATION_DATE | — | — |
| 6 | BusinessUnitPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 7 | BusinessUnitPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 8 | BusinessUnitPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 9 | BusinessUnitPEOInternalAddressLine | INTERNAL_ADDRESS_LINE | — | — |
| 10 | BusinessUnitPEOInternalExternalFlag | INTERNAL_EXTERNAL_FLAG | — | — |
| 11 | BusinessUnitPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | BusinessUnitPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | BusinessUnitPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | BusinessUnitPEOLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 15 | BusinessUnitPEOLocationId | LOCATION_ID | — | — |
| 16 | BusinessUnitPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | BusinessUnitPEOOrganizationId | ORGANIZATION_ID | — | — |
| 18 | BusinessUnitPEOType | TYPE | — | — |

### [[hr_all_positions_f|HR_ALL_POSITIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | PositionPEOActiveStatus | ACTIVE_STATUS | — | — |
| 3 | PositionPEOAssignmentCategory | ASSIGNMENT_CATEGORY | — | — |
| 4 | PositionPEOBargainingUnitCd | BARGAINING_UNIT_CD | — | — |
| 5 | PositionPEOBudgetAmount | BUDGET_AMOUNT | — | — |
| 6 | PositionPEOBudgetAmountCurrency | BUDGET_AMOUNT_CURRENCY | — | — |
| 7 | PositionPEOBudgetedPositionFlag | BUDGETED_POSITION_FLAG | — | — |
| 8 | PositionPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 9 | PositionPEOBusinessUnitId | BUSINESS_UNIT_ID | — | — |
| 10 | PositionPEOCategoryCode | CATEGORY_CODE | — | — |
| 11 | PositionPEOCollectiveAgreementId | COLLECTIVE_AGREEMENT_ID | — | — |
| 12 | PositionPEOCostCenter | COST_CENTER | — | — |
| 13 | PositionPEOCreatedBy | CREATED_BY | — | — |
| 14 | PositionPEOCreationDate | CREATION_DATE | — | — |
| 15 | PositionPEODelegatePositionId | DELEGATE_POSITION_ID | — | — |
| 16 | PositionPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 17 | PositionPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 18 | PositionPEOEntryGradeId | ENTRY_GRADE_ID | — | — |
| 19 | PositionPEOEntryStepId | ENTRY_STEP_ID | — | — |
| 20 | PositionPEOFrequency | FREQUENCY | — | — |
| 21 | PositionPEOFte | FTE | — | — |
| 22 | PositionPEOFullPartTime | FULL_PART_TIME | — | — |
| 23 | PositionPEOFundedByExistingPosition | FUNDED_BY_EXISTING_POSITION | — | — |
| 24 | PositionPEOGradeLadderId | GRADE_LADDER_ID | — | — |
| 25 | PositionPEOHiringStatus | HIRING_STATUS | — | — |
| 26 | PositionPEOJobId | JOB_ID | — | — |
| 27 | PositionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | PositionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 29 | PositionPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 30 | PositionPEOLocationId | LOCATION_ID | — | — |
| 31 | PositionPEOMaxPersons | MAX_PERSONS | — | — |
| 32 | PositionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 33 | PositionPEOOrganizationId | ORGANIZATION_ID | — | — |
| 34 | PositionPEOOverlapAllowed | OVERLAP_ALLOWED | — | — |
| 35 | PositionPEOPermanentTemporaryFlag | PERMANENT_TEMPORARY_FLAG | — | — |
| 36 | PositionPEOPositionCode | POSITION_CODE | — | ✅ |
| 37 | PositionPEOPositionId | POSITION_ID | — | — |
| 38 | PositionPEOPositionSynchronizationFlag | POSITION_SYNCHRONIZATION_FLAG | — | — |
| 39 | PositionPEOPositionType | POSITION_TYPE | — | — |
| 40 | PositionPEOProbationPeriod | PROBATION_PERIOD | — | — |
| 41 | PositionPEOProbationPeriodUnitCd | PROBATION_PERIOD_UNIT_CD | — | — |
| 42 | PositionPEORequisitionTemplateId | REQUISITION_TEMPLATE_ID | — | — |
| 43 | PositionPEOSeasonalEndDate | SEASONAL_END_DATE | — | — |
| 44 | PositionPEOSeasonalFlag | SEASONAL_FLAG | — | — |
| 45 | PositionPEOSeasonalStartDate | SEASONAL_START_DATE | — | — |
| 46 | PositionPEOSecurityClearance | SECURITY_CLEARANCE | — | — |
| 47 | PositionPEOStandardWorkingFrequency | STANDARD_WORKING_FREQUENCY | — | — |
| 48 | PositionPEOStandardWorkingHours | STANDARD_WORKING_HOURS | — | — |
| 49 | PositionPEOSupervisorAssignmentId | SUPERVISOR_ASSIGNMENT_ID | — | — |
| 50 | PositionPEOSupervisorId | SUPERVISOR_ID | — | — |
| 51 | PositionPEOTimeNormalFinish | TIME_NORMAL_FINISH | — | — |
| 52 | PositionPEOTimeNormalStart | TIME_NORMAL_START | — | — |
| 53 | PositionPEOUnionId | UNION_ID | — | — |
| 54 | PositionPEOWorkingHours | WORKING_HOURS | — | — |

### [[hr_all_positions_f_tl|HR_ALL_POSITIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PositionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | PositionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | PositionTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | PositionTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | PositionTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | PositionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PositionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PositionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PositionTranslationPEOName | NAME | — | ✅ |
| 10 | PositionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | PositionTranslationPEOPositionId | POSITION_ID | — | — |
| 12 | PositionTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[hr_organization_units_f_tl|HR_ORGANIZATION_UNITS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | BusinessUnitTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | BusinessUnitTranslationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | BusinessUnitTranslationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 5 | BusinessUnitTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | BusinessUnitTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | BusinessUnitTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | BusinessUnitTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | BusinessUnitTranslationPEOName | NAME | — | ✅ |
| 10 | BusinessUnitTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | BusinessUnitTranslationPEOOrganizationId | ORGANIZATION_ID | — | — |
| 12 | BusinessUnitTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[per_pos_funding_positions_f|PER_POS_FUNDING_POSITIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | FundingPositionId | FUNDING_POSITION_ID | — | ✅ |
| 8 | FundingRelationshipId | FUNDING_RELATIONSHIP_ID | 🔑 | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | PositionId | POSITION_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
