---
id: DOC-HCM-PVO-ConceptStructureCountPVO
doc_type: system-doc
title: "ConceptStructureCountPVO — PVO Human Capital Management"
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
  - ConceptStructureCountPVO
  - conceptstructurecountpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ConceptStructureCountPVO

## 📌 Visão Geral

Contabiliza componentes por estrutura de conceitos de inovacao. Suporta analise de complexidade e composicao de solucoes inovadoras.

**Caminho:** `FscmTopModelAM.ConceptsAnalyticsAM.ConceptStructureCountPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 10 | 91% |

---

## 🔗 Tabelas Relacionadas

- [[acd_concepts_structure_count_v|ACD_CONCEPTS_STRUCTURE_COUNT_V]] — 11 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[acd_concepts_structure_count_v|ACD_CONCEPTS_STRUCTURE_COUNT_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ComponentCount | COMPONENT_COUNT | — | ✅ |
| 2 | ConceptDescription | CONCEPT_DESCRIPTION | — | — |
| 3 | ConceptName | CONCEPT_NAME | — | ✅ |
| 4 | ConceptStructureId | CONCEPT_STRUCTURE_ID | 🔑 | ✅ |
| 5 | Distance | DISTANCE | — | ✅ |
| 6 | ElementCount | ELEMENT_COUNT | — | ✅ |
| 7 | ItemCount | ITEM_COUNT | — | ✅ |
| 8 | LifecyclePhase | LIFECYCLE_PHASE | — | ✅ |
| 9 | RelatedType | RELATED_TYPE | — | ✅ |
| 10 | RelatedTypeId | RELATED_TYPE_ID | — | ✅ |
| 11 | TopConceptId | TOP_CONCEPT_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
