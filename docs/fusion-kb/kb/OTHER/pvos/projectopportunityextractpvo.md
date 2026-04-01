---
id: DOC-OTHER-PVO-ProjectOpportunityExtractPVO
doc_type: system-doc
title: "ProjectOpportunityExtractPVO — PVO Cross-Module"
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
  - ProjectOpportunityExtractPVO
  - projectopportunityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectOpportunityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Opportunity Extract. Acessa as tabelas: PJT_PROJ_REF_OBJECT_B, PJT_PROJ_REF_OBJECT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectOpportunityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 31 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_proj_ref_object_b|PJT_PROJ_REF_OBJECT_B]] — 18 atributos (1 PKs, 18 BICC)
- [[pjt_proj_ref_object_tl|PJT_PROJ_REF_OBJECT_TL]] — 13 atributos (13 BICC)

---

## ⚙️ Atributos

### [[pjt_proj_ref_object_b|PJT_PROJ_REF_OBJECT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtProjectOpportunityBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtProjectOpportunityBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtProjectOpportunityBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PjtProjectOpportunityBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PjtProjectOpportunityBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PjtProjectOpportunityBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PjtProjectOpportunityBasePEOOpportunityAltNumber | OPPORTUNITY_ALT_NUMBER | — | ✅ |
| 8 | PjtProjectOpportunityBasePEOOpportunityAmount | OPPORTUNITY_AMOUNT | — | ✅ |
| 9 | PjtProjectOpportunityBasePEOOpportunityCurrencyCode | OPPORTUNITY_CURRENCY_CODE | — | ✅ |
| 10 | PjtProjectOpportunityBasePEOOpportunityCustomerId | OPPORTUNITY_CUSTOMER_ID | — | ✅ |
| 11 | PjtProjectOpportunityBasePEOOpportunityCustomerNumber | OPPORTUNITY_CUSTOMER_NUMBER | — | ✅ |
| 12 | PjtProjectOpportunityBasePEOOpportunityId | OPPORTUNITY_ID | — | ✅ |
| 13 | PjtProjectOpportunityBasePEOOpportunityNumber | OPPORTUNITY_NUMBER | — | ✅ |
| 14 | PjtProjectOpportunityBasePEOOpportunityWinConfPercent | OPPORTUNITY_WIN_CONF_PERCENT | — | ✅ |
| 15 | PjtProjectOpportunityBasePEORefObjectId | REF_OBJECT_ID | 🔑 | ✅ |
| 16 | PjtProjectOpportunityBasePEORefObjectType | REF_OBJECT_TYPE | — | ✅ |
| 17 | PjtProjectOpportunityBasePEORefProjectId | REF_PROJECT_ID | — | ✅ |
| 18 | PjtProjectOpportunityBasePEOUserLanguage | USER_LANGUAGE | — | ✅ |

### [[pjt_proj_ref_object_tl|PJT_PROJ_REF_OBJECT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtProjectOpportunityTransla1CreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtProjectOpportunityTransla1CreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtProjectOpportunityTransla1Language | LANGUAGE | — | ✅ |
| 4 | PjtProjectOpportunityTransla1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PjtProjectOpportunityTransla1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PjtProjectOpportunityTransla1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PjtProjectOpportunityTransla1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PjtProjectOpportunityTransla1OpportunityCustomerName | OPPORTUNITY_CUSTOMER_NAME | — | ✅ |
| 9 | PjtProjectOpportunityTransla1OpportunityDescription | OPPORTUNITY_DESCRIPTION | — | ✅ |
| 10 | PjtProjectOpportunityTransla1OpportunityName | OPPORTUNITY_NAME | — | ✅ |
| 11 | PjtProjectOpportunityTransla1OpportunityStatus | OPPORTUNITY_STATUS | — | ✅ |
| 12 | PjtProjectOpportunityTransla1RefObjectId | REF_OBJECT_ID | — | ✅ |
| 13 | PjtProjectOpportunityTransla1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
