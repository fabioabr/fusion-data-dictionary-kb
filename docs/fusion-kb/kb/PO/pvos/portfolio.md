---
id: DOC-PO-PVO-Portfolio
doc_type: system-doc
title: "Portfolio — PVO Purchasing"
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
  - Portfolio
  - portfolio
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Portfolio

## 📌 Visão Geral

Extrai dados de portfólio de projetos e produtos, incluindo nome, descrição, período de planejamento e status. Suporta gestão de portfólio, priorização de investimentos e análise estratégica.

**Caminho:** `FscmTopModelAM.PortfolioAnalyticsAM.Portfolio`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 3 | 1 | 62 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]] — 12 atributos (12 BICC)
- [[ace_portfolio_b|ACE_PORTFOLIO_B]] — 30 atributos (1 PKs, 30 BICC)
- [[ace_portfolio_tl|ACE_PORTFOLIO_TL]] — 22 atributos (20 BICC)

---

## ⚙️ Atributos

### [[ace_planning_period_b|ACE_PLANNING_PERIOD_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioPlngPrdCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioPlngPrdCreationDate | CREATION_DATE | — | ✅ |
| 3 | PortfolioPlngPrdEndPlanPeriodUnitId | END_PLAN_PERIOD_UNIT_ID | — | ✅ |
| 4 | PortfolioPlngPrdLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PortfolioPlngPrdLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PortfolioPlngPrdLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PortfolioPlngPrdObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PortfolioPlngPrdPeriodEndDate | PERIOD_END_DATE | — | ✅ |
| 9 | PortfolioPlngPrdPeriodStartDate | PERIOD_START_DATE | — | ✅ |
| 10 | PortfolioPlngPrdPeriodStatus | PERIOD_STATUS | — | ✅ |
| 11 | PortfolioPlngPrdPlanningPeriodId | PLANNING_PERIOD_ID | — | ✅ |
| 12 | PortfolioPlngPrdStartPlanPeriodUnitId | START_PLAN_PERIOD_UNIT_ID | — | ✅ |

### [[ace_portfolio_b|ACE_PORTFOLIO_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioArchiveFlag | ARCHIVE_FLAG | — | ✅ |
| 2 | PortfolioBudget | BUDGET | — | ✅ |
| 3 | PortfolioBusinessUnit | BUSINESS_UNIT | — | ✅ |
| 4 | PortfolioClassType | CLASS_TYPE | — | ✅ |
| 5 | PortfolioCompanyNodeId | COMPANY_NODE_ID | — | ✅ |
| 6 | PortfolioCreatedBy | CREATED_BY | — | ✅ |
| 7 | PortfolioCreatedFromPortfolioId | CREATED_FROM_PORTFOLIO_ID | — | ✅ |
| 8 | PortfolioCreationDate | CREATION_DATE | — | ✅ |
| 9 | PortfolioCurrencyCode | CURRENCY_CODE | — | ✅ |
| 10 | PortfolioCurrentPlanId | CURRENT_PLAN_ID | — | ✅ |
| 11 | PortfolioDeletedFlag | DELETED_FLAG | — | ✅ |
| 12 | PortfolioLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | PortfolioLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | PortfolioLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | PortfolioLatestRevisionId | LATEST_REVISION_ID | — | ✅ |
| 16 | PortfolioLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 17 | PortfolioObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | PortfolioOwner | OWNER | — | ✅ |
| 19 | PortfolioPlanningPeriodId | PLANNING_PERIOD_ID | — | ✅ |
| 20 | PortfolioPortfolioId | PORTFOLIO_ID | 🔑 | ✅ |
| 21 | PortfolioPortfolioType | PORTFOLIO_TYPE | — | ✅ |
| 22 | PortfolioPrimaryJustification | PRIMARY_JUSTIFICATION | — | ✅ |
| 23 | PortfolioProductLine | PRODUCT_LINE | — | ✅ |
| 24 | PortfolioProposedPlanId | PROPOSED_PLAN_ID | — | ✅ |
| 25 | PortfolioRevenueExpectation | REVENUE_EXPECTATION | — | ✅ |
| 26 | PortfolioSecondaryJustification | SECONDARY_JUSTIFICATION | — | ✅ |
| 27 | PortfolioTargetCost | TARGET_COST | — | ✅ |
| 28 | PortfolioTargetMargin | TARGET_MARGIN | — | ✅ |
| 29 | PortfolioTargetRevenue | TARGET_REVENUE | — | ✅ |
| 30 | PortfolioWorkflow | WORKFLOW | — | ✅ |

### [[ace_portfolio_tl|ACE_PORTFOLIO_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PortfolioTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | PortfolioTLCreatedCreatedBy | CREATED_BY | — | ✅ |
| 3 | PortfolioTLCreatedCreationDate | CREATION_DATE | — | ✅ |
| 4 | PortfolioTLCreatedDescription | DESCRIPTION | — | — |
| 5 | PortfolioTLCreatedLanguage | LANGUAGE | — | ✅ |
| 6 | PortfolioTLCreatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PortfolioTLCreatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PortfolioTLCreatedLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PortfolioTLCreatedName | NAME | — | ✅ |
| 10 | PortfolioTLCreatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PortfolioTLCreatedPortfolioId | PORTFOLIO_ID | — | ✅ |
| 12 | PortfolioTLCreatedSourceLang | SOURCE_LANG | — | ✅ |
| 13 | PortfolioTLCreationDate | CREATION_DATE | — | ✅ |
| 14 | PortfolioTLDescription | DESCRIPTION | — | — |
| 15 | PortfolioTLLanguage | LANGUAGE | — | ✅ |
| 16 | PortfolioTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | PortfolioTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 18 | PortfolioTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 19 | PortfolioTLName | NAME | — | ✅ |
| 20 | PortfolioTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 21 | PortfolioTLPortfolioId | PORTFOLIO_ID | — | ✅ |
| 22 | PortfolioTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
