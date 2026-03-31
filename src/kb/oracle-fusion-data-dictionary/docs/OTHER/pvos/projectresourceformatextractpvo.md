---
id: DOC-OTHER-PVO-ProjectResourceFormatExtractPVO
doc_type: system-doc
title: "ProjectResourceFormatExtractPVO — PVO Cross-Module"
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
  - ProjectResourceFormatExtractPVO
  - projectresourceformatextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceFormatExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Format Extract. Acessa as tabelas: PJF_RES_FORMATS_B, PJF_RES_FORMATS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceFormatExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 43 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_res_formats_b|PJF_RES_FORMATS_B]] — 31 atributos (1 PKs, 31 BICC)
- [[pjf_res_formats_tl|PJF_RES_FORMATS_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjf_res_formats_b|PJF_RES_FORMATS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceFormatBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceFormatBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceFormatBasePEOEqpLevelSeq | EQP_LEVEL_SEQ | — | ✅ |
| 4 | ProjectResourceFormatBasePEOEqpRcPrec | EQP_RC_PREC | — | ✅ |
| 5 | ProjectResourceFormatBasePEOEquipmentClassFlag | EQUIPMENT_CLASS_FLAG | — | ✅ |
| 6 | ProjectResourceFormatBasePEOFinLevelSeq | FIN_LEVEL_SEQ | — | ✅ |
| 7 | ProjectResourceFormatBasePEOFinRcPrec | FIN_RC_PREC | — | ✅ |
| 8 | ProjectResourceFormatBasePEOFinancialElemClassFlag | FINANCIAL_ELEM_CLASS_FLAG | — | ✅ |
| 9 | ProjectResourceFormatBasePEOFormatLevel | FORMAT_LEVEL | — | ✅ |
| 10 | ProjectResourceFormatBasePEOFormatToken | FORMAT_TOKEN | — | ✅ |
| 11 | ProjectResourceFormatBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ProjectResourceFormatBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ProjectResourceFormatBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ProjectResourceFormatBasePEOMatLevelSeq | MAT_LEVEL_SEQ | — | ✅ |
| 15 | ProjectResourceFormatBasePEOMatRcPrec | MAT_RC_PREC | — | ✅ |
| 16 | ProjectResourceFormatBasePEOMaterialItemClassFlag | MATERIAL_ITEM_CLASS_FLAG | — | ✅ |
| 17 | ProjectResourceFormatBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | ProjectResourceFormatBasePEOParentResFormatId | PARENT_RES_FORMAT_ID | — | ✅ |
| 19 | ProjectResourceFormatBasePEOParentResTypeId | PARENT_RES_TYPE_ID | — | ✅ |
| 20 | ProjectResourceFormatBasePEOPeopleClassFlag | PEOPLE_CLASS_FLAG | — | ✅ |
| 21 | ProjectResourceFormatBasePEOPerLevelSeq | PER_LEVEL_SEQ | — | ✅ |
| 22 | ProjectResourceFormatBasePEOPerRcPrec | PER_RC_PREC | — | ✅ |
| 23 | ProjectResourceFormatBasePEOResFormatId | RES_FORMAT_ID | 🔑 | ✅ |
| 24 | ProjectResourceFormatBasePEOResFormatSeq | RES_FORMAT_SEQ | — | ✅ |
| 25 | ProjectResourceFormatBasePEOResTypeDispChars | RES_TYPE_DISP_CHARS | — | ✅ |
| 26 | ProjectResourceFormatBasePEOResTypeId | RES_TYPE_ID | — | ✅ |
| 27 | ProjectResourceFormatBasePEOResTypeIdLevel1 | RES_TYPE_ID_LEVEL1 | — | ✅ |
| 28 | ProjectResourceFormatBasePEOResTypeIdLevel2 | RES_TYPE_ID_LEVEL2 | — | ✅ |
| 29 | ProjectResourceFormatBasePEOResTypeIdLevel3 | RES_TYPE_ID_LEVEL3 | — | ✅ |
| 30 | ProjectResourceFormatBasePEOResourceClassFlag | RESOURCE_CLASS_FLAG | — | ✅ |
| 31 | ProjectResourceFormatBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

### [[pjf_res_formats_tl|PJF_RES_FORMATS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceFormatTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceFormatTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceFormatTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceFormatTLPEOLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectResourceFormatTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceFormatTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceFormatTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceFormatTLPEOName | NAME | — | ✅ |
| 9 | ProjectResourceFormatTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceFormatTLPEOResFormatId | RES_FORMAT_ID | — | ✅ |
| 11 | ProjectResourceFormatTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | ProjectResourceFormatTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
