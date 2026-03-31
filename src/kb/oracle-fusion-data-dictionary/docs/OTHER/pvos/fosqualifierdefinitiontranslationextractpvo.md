---
id: DOC-OTHER-PVO-FosQualifierDefinitionTranslationExtractPVO
doc_type: system-doc
title: "FosQualifierDefinitionTranslationExtractPVO — PVO Cross-Module"
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
  - FosQualifierDefinitionTranslationExtractPVO
  - fosqualifierdefinitiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosQualifierDefinitionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Qualifier Definition Translation Extract. Acessa as tabelas: FOS_QUALIFIER_DEFINITIONS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosQualifierDefinitionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 10 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[fos_qualifier_definitions_tl|FOS_QUALIFIER_DEFINITIONS_TL]] — 12 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[fos_qualifier_definitions_tl|FOS_QUALIFIER_DEFINITIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifierDefinitionTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | QualifierDefinitionTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | QualifierDefinitionTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | QualifierDefinitionTLPEOLanguage | LANGUAGE | 🔑 | — |
| 5 | QualifierDefinitionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | QualifierDefinitionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | QualifierDefinitionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | QualifierDefinitionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QualifierDefinitionTLPEOQualifierId | QUALIFIER_ID | 🔑 | ✅ |
| 10 | QualifierDefinitionTLPEOQualifierMeaning | QUALIFIER_MEANING | — | ✅ |
| 11 | QualifierDefinitionTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | QualifierDefinitionTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
