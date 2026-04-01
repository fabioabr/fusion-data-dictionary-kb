---
id: DOC-OTHER-PVO-SubledgerMappingSetTLExtractPVO
doc_type: system-doc
title: "SubledgerMappingSetTLExtractPVO — PVO Cross-Module"
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
  - SubledgerMappingSetTLExtractPVO
  - subledgermappingsettlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SubledgerMappingSetTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Subledger Mapping Set TLExtract. Acessa as tabelas: XLA_MAPPING_SETS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.XlaBiccExtractAM.SubledgerMappingSetTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 4 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[xla_mapping_sets_tl|XLA_MAPPING_SETS_TL]] — 13 atributos (4 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[xla_mapping_sets_tl|XLA_MAPPING_SETS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | MappingSetTLAmbContextCode | AMB_CONTEXT_CODE | 🔑 | ✅ |
| 2 | MappingSetTLApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 3 | MappingSetTLCreatedBy | CREATED_BY | — | ✅ |
| 4 | MappingSetTLCreationDate | CREATION_DATE | — | ✅ |
| 5 | MappingSetTLDescription | DESCRIPTION | — | ✅ |
| 6 | MappingSetTLLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | MappingSetTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | MappingSetTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | MappingSetTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MappingSetTLMappingSetCode | MAPPING_SET_CODE | 🔑 | ✅ |
| 11 | MappingSetTLName | NAME | — | ✅ |
| 12 | MappingSetTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | MappingSetTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
