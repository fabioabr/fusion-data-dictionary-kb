---
id: DOC-OTHER-PVO-ProjectOpportunityTranslationExtractPVO
doc_type: system-doc
title: "ProjectOpportunityTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectOpportunityTranslationExtractPVO
  - projectopportunitytranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectOpportunityTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Opportunity Translation Extract. Acessa as tabelas: PJT_PROJ_REF_OBJECT_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectOpportunityTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_proj_ref_object_tl|PJT_PROJ_REF_OBJECT_TL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pjt_proj_ref_object_tl|PJT_PROJ_REF_OBJECT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtProjectOpportunityTransla1CreatedBy | CREATED_BY | — | ✅ |
| 2 | PjtProjectOpportunityTransla1CreationDate | CREATION_DATE | — | ✅ |
| 3 | PjtProjectOpportunityTransla1Language | LANGUAGE | 🔑 | ✅ |
| 4 | PjtProjectOpportunityTransla1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PjtProjectOpportunityTransla1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PjtProjectOpportunityTransla1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PjtProjectOpportunityTransla1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | PjtProjectOpportunityTransla1OpportunityCustomerName | OPPORTUNITY_CUSTOMER_NAME | — | ✅ |
| 9 | PjtProjectOpportunityTransla1OpportunityDescription | OPPORTUNITY_DESCRIPTION | — | ✅ |
| 10 | PjtProjectOpportunityTransla1OpportunityName | OPPORTUNITY_NAME | — | ✅ |
| 11 | PjtProjectOpportunityTransla1OpportunityStatus | OPPORTUNITY_STATUS | — | ✅ |
| 12 | PjtProjectOpportunityTransla1RefObjectId | REF_OBJECT_ID | 🔑 | ✅ |
| 13 | PjtProjectOpportunityTransla1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
