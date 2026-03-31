---
id: DOC-OTHER-PVO-FosQualifierDefinitionExtractPVO
doc_type: system-doc
title: "FosQualifierDefinitionExtractPVO — PVO Cross-Module"
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
  - FosQualifierDefinitionExtractPVO
  - fosqualifierdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosQualifierDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Qualifier Definition Extract. Acessa as tabelas: FOS_QUALIFIER_DEFINITIONS_B, FOS_QUALIFIER_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosQualifierDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 2 | 1 | 24 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[fos_qualifier_definitions_b|FOS_QUALIFIER_DEFINITIONS_B]] — 15 atributos (1 PKs, 15 BICC)
- [[fos_qualifier_definitions_tl|FOS_QUALIFIER_DEFINITIONS_TL]] — 11 atributos (9 BICC)

---

## ⚙️ Atributos

### [[fos_qualifier_definitions_b|FOS_QUALIFIER_DEFINITIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierDefinitionBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualifierDefinitionBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualifierDefinitionBPEODropShipQualifierFlag | DROP_SHIP_QUALIFIER_FLAG | — | ✅ |
| 4 | QualifierDefinitionBPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | QualifierDefinitionBPEOGpQualifierFlag | GP_QUALIFIER_FLAG | — | ✅ |
| 6 | QualifierDefinitionBPEOImtQualifierFlag | IMT_QUALIFIER_FLAG | — | ✅ |
| 7 | QualifierDefinitionBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | QualifierDefinitionBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | QualifierDefinitionBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | QualifierDefinitionBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | QualifierDefinitionBPEOQualifierCode | QUALIFIER_CODE | — | ✅ |
| 12 | QualifierDefinitionBPEOQualifierId | QUALIFIER_ID | 🔑 | ✅ |
| 13 | QualifierDefinitionBPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 14 | QualifierDefinitionBPEOServiceSalesQualifierFlag | SERVICE_SALES_QUALIFIER_FLAG | — | ✅ |
| 15 | QualifierDefinitionBPEOShipmentQualifierFlag | SHIPMENT_QUALIFIER_FLAG | — | ✅ |

### [[fos_qualifier_definitions_tl|FOS_QUALIFIER_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierDefinitionTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualifierDefinitionTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualifierDefinitionTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | QualifierDefinitionTLPEOLanguage | LANGUAGE | — | — |
| 5 | QualifierDefinitionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QualifierDefinitionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | QualifierDefinitionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | QualifierDefinitionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QualifierDefinitionTLPEOQualifierId | QUALIFIER_ID | — | ✅ |
| 10 | QualifierDefinitionTLPEOQualifierMeaning | QUALIFIER_MEANING | — | ✅ |
| 11 | QualifierDefinitionTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
