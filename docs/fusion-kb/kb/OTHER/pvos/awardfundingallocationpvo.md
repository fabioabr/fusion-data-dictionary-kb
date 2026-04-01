---
id: DOC-OTHER-PVO-AwardFundingAllocationPVO
doc_type: system-doc
title: "AwardFundingAllocationPVO — PVO Cross-Module"
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
  - AwardFundingAllocationPVO
  - awardfundingallocationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundingAllocationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Funding Allocation. Acessa as tabelas: GMS_AWARD_BUDGET_PERIODS, GMS_AWARD_FUNDINGS_VL, GMS_AWARD_FUND_ALLOCATIONS (+4).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardFundingAllocationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 7 | 1 | 16 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]] — 4 atributos
- [[gms_award_fundings_vl|GMS_AWARD_FUNDINGS_VL]] — 10 atributos (5 BICC)
- [[gms_award_fund_allocations|GMS_AWARD_FUND_ALLOCATIONS]] — 14 atributos (1 PKs, 9 BICC)
- [[gms_award_headers_b|GMS_AWARD_HEADERS_B]] — 1 atributos
- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos (1 BICC)
- [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]] — 5 atributos

---

## ⚙️ Atributos

### [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardBudgetPeriodPEOAwardId | AWARD_ID | — | — |
| 2 | AwardBudgetPeriodPEOEndDate | END_DATE | — | — |
| 3 | AwardBudgetPeriodPEOStartDate | START_DATE | — | — |
| 4 | Id1 | ID | — | — |

### [[gms_award_fundings_vl|GMS_AWARD_FUNDINGS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundingPEOAwardFundingSourceId | AWARD_FUNDING_SOURCE_ID | — | — |
| 2 | AwardFundingPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | — |
| 3 | AwardFundingPEODirectFundingAmount | DIRECT_FUNDING_AMOUNT | — | — |
| 4 | AwardFundingPEOFundingSourceId | FUNDING_SOURCE_ID | — | — |
| 5 | AwardFundingPEOId | ID | — | ✅ |
| 6 | AwardFundingPEOIndirectFundingAmount | INDIRECT_FUNDING_AMOUNT | — | — |
| 7 | AwardFundingPEOIssueDate | ISSUE_DATE | — | ✅ |
| 8 | AwardFundingPEOIssueDescription | ISSUE_DESCRIPTION | — | ✅ |
| 9 | AwardFundingPEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 10 | AwardFundingPEOIssueType | ISSUE_TYPE | — | ✅ |

### [[gms_award_fund_allocations|GMS_AWARD_FUND_ALLOCATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundAllocationPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardFundAllocationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AwardFundAllocationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AwardFundAllocationPEOFundingAmount | FUNDING_AMOUNT | — | ✅ |
| 5 | AwardFundAllocationPEOFundingDate | FUNDING_DATE | — | ✅ |
| 6 | AwardFundAllocationPEOFundingId | FUNDING_ID | — | — |
| 7 | AwardFundAllocationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardFundAllocationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AwardFundAllocationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AwardFundAllocationPEOLcFundingAmount | LC_FUNDING_AMOUNT | — | — |
| 11 | AwardFundAllocationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | AwardFundAllocationPEOProjectId | PROJECT_ID | — | — |
| 13 | AwardFundAllocationPEOTaskId | TASK_ID | — | ✅ |
| 14 | Id | ID | 🔑 | ✅ |

### [[gms_award_headers_b|GMS_AWARD_HEADERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderBasePEOId | ID | — | — |

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | — |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORG_INFORMATION_ID | — | — |
| 2 | BusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | ✅ |
| 3 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[pjf_projects_all_vl|PJF_PROJECTS_ALL_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectPEOCarryingOutOrganizationId | CARRYING_OUT_ORGANIZATION_ID | — | — |
| 2 | ProjectPEOName | NAME | — | — |
| 3 | ProjectPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 4 | ProjectPEOOrgId | ORG_ID | — | — |
| 5 | ProjectPEOProjectId | PROJECT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
