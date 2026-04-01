---
id: DOC-HCM-PVO-ConceptSolutionAltPVO
doc_type: system-doc
title: "ConceptSolutionAltPVO — PVO Human Capital Management"
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
  - ConceptSolutionAltPVO
  - conceptsolutionaltpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptSolutionAltPVO

## 📌 Visão Geral

Extrai alternativas de solucao para conceitos de inovacao com indice e acesso. Suporta comparacao de abordagens em processos de innovation management.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ConceptSolutionAltPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 31 | 2 | 1 | 30 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concept_b|ACD_CONCEPT_B]] — 17 atributos (17 BICC)
- [[acd_solution_alternative_vl|ACD_SOLUTION_ALTERNATIVE_VL]] — 14 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[acd_concept_b|ACD_CONCEPT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConceptBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | ConceptBaseConceptId | CONCEPT_ID | — | ✅ |
| 3 | ConceptBaseCreatedBy | CREATED_BY | — | ✅ |
| 4 | ConceptBaseCreationDate | CREATION_DATE | — | ✅ |
| 5 | ConceptBaseCurrencyCode | CURRENCY_CODE | — | ✅ |
| 6 | ConceptBaseDueDate | DUE_DATE | — | ✅ |
| 7 | ConceptBaseIsCurrent | IS_CURRENT | — | ✅ |
| 8 | ConceptBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ConceptBaseLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | ConceptBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ConceptBaseLifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 12 | ConceptBaseMasterId | MASTER_ID | — | ✅ |
| 13 | ConceptBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | ConceptBasePowerUnit | POWER_UNIT | — | ✅ |
| 15 | ConceptBaseType | TYPE | — | ✅ |
| 16 | ConceptBaseVersion | VERSION | — | ✅ |
| 17 | ConceptBaseVolume | VOLUME | — | ✅ |

### [[acd_solution_alternative_vl|ACD_SOLUTION_ALTERNATIVE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AlternativeIndex | ALTERNATIVE_INDEX | — | ✅ |
| 2 | ConceptId | CONCEPT_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DefaultAlternative | DEFAULT_ALTERNATIVE | — | ✅ |
| 6 | Description | DESCRIPTION | — | — |
| 7 | IsActive | IS_ACTIVE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | Name | NAME | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | Posno | POSNO | — | ✅ |
| 14 | SolutionAlternativeId | SOLUTION_ALTERNATIVE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
