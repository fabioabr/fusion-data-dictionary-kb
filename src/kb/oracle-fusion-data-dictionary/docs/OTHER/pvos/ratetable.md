---
id: DOC-OTHER-PVO-RateTable
doc_type: system-doc
title: "RateTable — PVO Cross-Module"
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
  - RateTable
  - ratetable
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateTable

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Table. Acessa as tabelas: CN_RATE_TABLES_ALL_B, CN_RATE_TABLES_ALL_TL, FUN_ALL_BUSINESS_UNITS_V.

**Caminho:** `FscmTopModelAM.RateTableAM.RateTable`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 3 | 1 | 14 | 78% |

---

## 🔗 Tabelas Relacionadas

- [[cn_rate_tables_all_b|CN_RATE_TABLES_ALL_B]] — 10 atributos (1 PKs, 9 BICC)
- [[cn_rate_tables_all_tl|CN_RATE_TABLES_ALL_TL]] — 6 atributos (4 BICC)
- [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[cn_rate_tables_all_b|CN_RATE_TABLES_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CommissionUnitCode | COMMISSION_UNIT_CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | NumberDim | NUMBER_DIM | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrgId | ORG_ID | — | ✅ |
| 10 | RateTableId | RATE_TABLE_ID | 🔑 | ✅ |

### [[cn_rate_tables_all_tl|CN_RATE_TABLES_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | DisplayName | DISPLAY_NAME | — | ✅ |
| 3 | Language | LANGUAGE | — | ✅ |
| 4 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 5 | RateTableId1 | RATE_TABLE_ID | — | — |
| 6 | RateTableName | RATE_TABLE_NAME | — | ✅ |

### [[fun_all_business_units_v|FUN_ALL_BUSINESS_UNITS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitId | BU_ID | — | — |
| 2 | Name | BU_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
