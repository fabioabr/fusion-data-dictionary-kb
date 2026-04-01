---
id: DOC-OTHER-PVO-ConceptsViewPVO
doc_type: system-doc
title: "ConceptsViewPVO — PVO Cross-Module"
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
  - ConceptsViewPVO
  - conceptsviewpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptsViewPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Concepts View. Acessa as tabelas: ACD_CONCEPT_VL.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ConceptsViewPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 2 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_vl|ACD_CONCEPT_VL]] — 17 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[acd_concept_vl|ACD_CONCEPT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | — |
| 2 | ConceptConceptId | CONCEPT_ID | 🔑 | ✅ |
| 3 | ConceptCreatedBy | CREATED_BY | — | — |
| 4 | ConceptCreationDate | CREATION_DATE | — | — |
| 5 | ConceptDescription | DESCRIPTION | — | — |
| 6 | ConceptDueDate | DUE_DATE | — | — |
| 7 | ConceptIsCurrent | IS_CURRENT | — | — |
| 8 | ConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ConceptLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ConceptLifecyclePhase | LIFECYCLE_PHASE | — | — |
| 12 | ConceptMasterId | MASTER_ID | — | — |
| 13 | ConceptName | NAME | — | — |
| 14 | ConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ConceptType | TYPE | — | — |
| 16 | ConceptVersion | VERSION | — | — |
| 17 | CurrencyCode | CURRENCY_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
