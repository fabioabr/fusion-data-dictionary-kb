---
id: DOC-OTHER-PVO-ProjectResourceTypeExtractPVO
doc_type: system-doc
title: "ProjectResourceTypeExtractPVO — PVO Cross-Module"
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
  - ProjectResourceTypeExtractPVO
  - projectresourcetypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Type Extract. Acessa as tabelas: PJF_RES_TYPES_B, PJF_RES_TYPES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_res_types_b|PJF_RES_TYPES_B]] — 15 atributos (1 PKs, 15 BICC)
- [[pjf_res_types_tl|PJF_RES_TYPES_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjf_res_types_b|PJF_RES_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceTypeBasePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | ProjectResourceTypeBasePEOEqpRcPrec | EQP_RC_PREC | — | ✅ |
| 5 | ProjectResourceTypeBasePEOFinRcPrec | FIN_RC_PREC | — | ✅ |
| 6 | ProjectResourceTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ProjectResourceTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ProjectResourceTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ProjectResourceTypeBasePEOMatRcPrec | MAT_RC_PREC | — | ✅ |
| 10 | ProjectResourceTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ProjectResourceTypeBasePEOPerRcPrec | PER_RC_PREC | — | ✅ |
| 12 | ProjectResourceTypeBasePEOResTypeCode | RES_TYPE_CODE | — | ✅ |
| 13 | ProjectResourceTypeBasePEOResTypeId | RES_TYPE_ID | 🔑 | ✅ |
| 14 | ProjectResourceTypeBasePEOResTypeScode | RES_TYPE_SCODE | — | ✅ |
| 15 | ProjectResourceTypeBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

### [[pjf_res_types_tl|PJF_RES_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceTypeTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceTypeTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceTypeTLPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectResourceTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceTypeTLPEOName | NAME | — | ✅ |
| 9 | ProjectResourceTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceTypeTLPEOResTypeId | RES_TYPE_ID | — | ✅ |
| 11 | ProjectResourceTypeTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectResourceTypeTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
