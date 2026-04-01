---
id: DOC-HCM-PVO-ProposalsPVO
doc_type: system-doc
title: "ProposalsPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ProposalsPVO
  - proposalspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProposalsPVO

## 📌 Visão Geral

Disponibiliza dados resumidos de propostas de produto com informações de conceito. Base para visão consolidada do portfólio de inovação e pipeline de produtos.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ProposalsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 34 | 3 | 1 | 7 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 8 atributos (1 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (2 BICC)
- [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]] — 15 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptBaseConceptId | CONCEPT_ID | — | — |
| 2 | ConceptBaseCreatedBy | CREATED_BY | — | — |
| 3 | ConceptBaseCreationDate | CREATION_DATE | — | — |
| 4 | ConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ConceptBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ConceptBaseMasterId | MASTER_ID | — | — |
| 8 | ConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTranslationConceptId | CONCEPT_ID | — | — |
| 2 | ConceptTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ConceptTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ConceptTranslationDescription | DESCRIPTION | — | — |
| 5 | ConceptTranslationLanguage | LANGUAGE | — | — |
| 6 | ConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ConceptTranslationName | NAME | — | ✅ |
| 10 | ConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ConceptTranslationSourceLang | SOURCE_LANG | — | — |

### [[acd_product_proposal|ACD_PRODUCT_PROPOSAL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProposalAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | — |
| 2 | ProposalConceptMasterId | CONCEPT_MASTER_ID | — | — |
| 3 | ProposalCreatedBy | CREATED_BY | — | — |
| 4 | ProposalCreationDate | CREATION_DATE | — | ✅ |
| 5 | ProposalCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 6 | ProposalIsCloned | IS_CLONED | — | — |
| 7 | ProposalIsLatest | IS_LATEST | — | — |
| 8 | ProposalLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ProposalLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ProposalLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ProposalObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ProposalProductProposalId | PRODUCT_PROPOSAL_ID | 🔑 | ✅ |
| 13 | ProposalProposalStatus | PROPOSAL_STATUS | — | ✅ |
| 14 | ProposalPublishedFromPortfolio | PUBLISHED_FROM_PORTFOLIO | — | — |
| 15 | ProposalVersion | VERSION | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
