---
id: DOC-OTHER-PVO-PjtProjectTaskCodeValuesPVO
doc_type: system-doc
title: "PjtProjectTaskCodeValuesPVO — PVO Cross-Module"
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
  - PjtProjectTaskCodeValuesPVO
  - pjtprojecttaskcodevaluespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjtProjectTaskCodeValuesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pjt Project Task Code Values. Acessa as tabelas: PJT_COLUMN_LKP_VALUES_VL, PJT_COLUMN_MAP_B.

**Caminho:** `FscmTopModelAM.PjtSetupAM.PjtProjectTaskCodeValuesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 4 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_column_lkp_values_vl|PJT_COLUMN_LKP_VALUES_VL]] — 11 atributos (1 PKs, 3 BICC)
- [[pjt_column_map_b|PJT_COLUMN_MAP_B]] — 14 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjt_column_lkp_values_vl|PJT_COLUMN_LKP_VALUES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeValueId | CODE_VALUE_ID | 🔑 | ✅ |
| 2 | ColumnLkpValuesPEOColumnMapId | COLUMN_MAP_ID | — | — |
| 3 | ColumnLkpValuesPEOCreatedBy | CREATED_BY | — | — |
| 4 | ColumnLkpValuesPEOCreationDate | CREATION_DATE | — | — |
| 5 | ColumnLkpValuesPEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 6 | ColumnLkpValuesPEOEnabledFlag | ENABLED_FLAG | — | — |
| 7 | ColumnLkpValuesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ColumnLkpValuesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ColumnLkpValuesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ColumnLkpValuesPEOMeaning | MEANING | — | ✅ |
| 11 | ColumnLkpValuesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pjt_column_map_b|PJT_COLUMN_MAP_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ColumnMapBasePEOAttrDataType | ATTR_DATA_TYPE | — | — |
| 2 | ColumnMapBasePEOColumnMapId | COLUMN_MAP_ID | — | — |
| 3 | ColumnMapBasePEOColumnName | COLUMN_NAME | — | — |
| 4 | ColumnMapBasePEOCreatedBy | CREATED_BY | — | — |
| 5 | ColumnMapBasePEOCreationDate | CREATION_DATE | — | — |
| 6 | ColumnMapBasePEOEnabledFlag | ENABLED_FLAG | — | — |
| 7 | ColumnMapBasePEOGlobalFlag | GLOBAL_FLAG | — | — |
| 8 | ColumnMapBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ColumnMapBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ColumnMapBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ColumnMapBasePEOObjectType | OBJECT_TYPE | — | — |
| 12 | ColumnMapBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | ColumnMapBasePEOProjectId | PROJECT_ID | — | — |
| 14 | ColumnMapBasePEOTableName | TABLE_NAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
