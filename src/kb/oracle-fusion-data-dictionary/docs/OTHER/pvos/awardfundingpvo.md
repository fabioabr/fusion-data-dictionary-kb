---
id: DOC-OTHER-PVO-AwardFundingPVO
doc_type: system-doc
title: "AwardFundingPVO — PVO Cross-Module"
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
  - AwardFundingPVO
  - awardfundingpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardFundingPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Funding. Acessa as tabelas: GMS_AWARD_BUDGET_PERIODS, GMS_AWARD_FUNDINGS_VL, GMS_AWARD_HEADERS_B (+1).

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardFundingPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 4 | 1 | 22 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]] — 3 atributos (3 BICC)
- [[gms_award_fundings_vl|GMS_AWARD_FUNDINGS_VL]] — 17 atributos (1 PKs, 16 BICC)
- [[gms_award_headers_b|GMS_AWARD_HEADERS_B]] — 1 atributos (1 BICC)
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_award_budget_periods|GMS_AWARD_BUDGET_PERIODS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardBudgetPeriodPEOEndDate | END_DATE | — | ✅ |
| 2 | AwardBudgetPeriodPEOId | ID | — | ✅ |
| 3 | AwardBudgetPeriodPEOStartDate | START_DATE | — | ✅ |

### [[gms_award_fundings_vl|GMS_AWARD_FUNDINGS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardFundingPEOAwardFundingSourceId | AWARD_FUNDING_SOURCE_ID | — | ✅ |
| 2 | AwardFundingPEOAwardId | AWARD_ID | — | ✅ |
| 3 | AwardFundingPEOBudgetPeriodId | BUDGET_PERIOD_ID | — | ✅ |
| 4 | AwardFundingPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | AwardFundingPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | AwardFundingPEODirectFundingAmount | DIRECT_FUNDING_AMOUNT | — | ✅ |
| 7 | AwardFundingPEOFundingSourceId | FUNDING_SOURCE_ID | — | — |
| 8 | AwardFundingPEOIndirectFundingAmount | INDIRECT_FUNDING_AMOUNT | — | ✅ |
| 9 | AwardFundingPEOIssueDate | ISSUE_DATE | — | ✅ |
| 10 | AwardFundingPEOIssueDescription | ISSUE_DESCRIPTION | — | ✅ |
| 11 | AwardFundingPEOIssueNumber | ISSUE_NUMBER | — | ✅ |
| 12 | AwardFundingPEOIssueType | ISSUE_TYPE | — | ✅ |
| 13 | AwardFundingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | AwardFundingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | AwardFundingPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | AwardFundingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | Id | ID | 🔑 | ✅ |

### [[gms_award_headers_b|GMS_AWARD_HEADERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardHeaderBasePEOId | ID | — | ✅ |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitPEOBusinessUnitId | ORGANIZATION_ID | — | ✅ |
| 2 | BusinessUnitPEOPrimaryLedgerId | ORG_INFORMATION3 | — | ✅ |
| 3 | OrganizationInformationPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 4 | OrganizationInformationPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 5 | OrganizationInformationPEOOrgInformationId | ORG_INFORMATION_ID | — | — |
| 6 | OrganizationInformationPEOOrganizationId | ORGANIZATION_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
