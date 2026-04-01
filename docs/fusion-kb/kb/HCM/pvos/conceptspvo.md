---
id: DOC-HCM-PVO-ConceptsPVO
doc_type: system-doc
title: "ConceptsPVO — PVO Human Capital Management"
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
  - ConceptsPVO
  - conceptspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptsPVO

## 📌 Visão Geral

Cataloga conceitos de inovacao (Innovation Management) com numero e controle de acesso. Base para gestao do ciclo de vida de ideias e inovacoes.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ConceptsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 26 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 16 atributos (1 PKs, 16 BICC)
- [[acd_concept_tl|ACD_CONCEPT_TL]] — 11 atributos (10 BICC)

---

## ⚙️ Atributos

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptConceptId | CONCEPT_ID | 🔑 | ✅ |
| 3 | ConceptConceptNumber | CONCEPT_NUMBER | — | ✅ |
| 4 | ConceptCreatedBy | CREATED_BY | — | ✅ |
| 5 | ConceptCreationDate | CREATION_DATE | — | ✅ |
| 6 | ConceptCurrencyCode | CURRENCY_CODE | — | ✅ |
| 7 | ConceptIsCurrent | IS_CURRENT | — | ✅ |
| 8 | ConceptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ConceptLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ConceptLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ConceptLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 12 | ConceptMasterId | MASTER_ID | — | ✅ |
| 13 | ConceptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | ConceptType | TYPE | — | ✅ |
| 15 | ConceptVersion | VERSION | — | ✅ |
| 16 | DueDate | DUE_DATE | — | ✅ |

### [[acd_concept_tl|ACD_CONCEPT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptTranslationConceptId | CONCEPT_ID | — | ✅ |
| 2 | ConceptTranslationCreatedBy | CREATED_BY | — | ✅ |
| 3 | ConceptTranslationCreationDate | CREATION_DATE | — | ✅ |
| 4 | ConceptTranslationDescription | DESCRIPTION | — | — |
| 5 | ConceptTranslationLanguage | LANGUAGE | — | ✅ |
| 6 | ConceptTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ConceptTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ConceptTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ConceptTranslationName | NAME | — | ✅ |
| 10 | ConceptTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ConceptTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
