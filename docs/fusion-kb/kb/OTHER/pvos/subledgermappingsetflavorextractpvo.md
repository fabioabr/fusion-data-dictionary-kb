---
id: DOC-OTHER-PVO-SubledgerMappingSetFlavorExtractPVO
doc_type: system-doc
title: "SubledgerMappingSetFlavorExtractPVO — PVO Cross-Module"
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
  - SubledgerMappingSetFlavorExtractPVO
  - subledgermappingsetflavorextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerMappingSetFlavorExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Mapping Set Flavor Extract. Acessa as tabelas: XLA_MAPPING_SET_FLAVORS.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerMappingSetFlavorExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 4 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_mapping_set_flavors|XLA_MAPPING_SET_FLAVORS]] — 15 atributos (4 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[xla_mapping_set_flavors|XLA_MAPPING_SET_FLAVORS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetFlavorAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | MappingSetFlavorApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 3 | MappingSetFlavorCreatedBy | CREATED_BY | — | ✅ |
| 4 | MappingSetFlavorCreationDate | CREATION_DATE | — | ✅ |
| 5 | MappingSetFlavorDefaultCcid | DEFAULT_CCID | — | ✅ |
| 6 | MappingSetFlavorDefaultConstant | DEFAULT_CONSTANT | — | ✅ |
| 7 | MappingSetFlavorEnabledFlag | ENABLED_FLAG | — | ✅ |
| 8 | MappingSetFlavorFlexfieldSegmentCode | FLEXFIELD_SEGMENT_CODE | — | ✅ |
| 9 | MappingSetFlavorLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | MappingSetFlavorLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | MappingSetFlavorLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MappingSetFlavorMappingSetCode | MAPPING_SET_CODE | 🔑 | ✅ |
| 13 | MappingSetFlavorMappingSetFlavorId | MAPPING_SET_FLAVOR_ID | — | ✅ |
| 14 | MappingSetFlavorObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | MappingSetFlavorStripeId | STRIPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
