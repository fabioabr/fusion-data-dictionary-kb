---
id: DOC-GL-PVO-UserRowDPVO
doc_type: system-doc
title: "UserRowDPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - UserRowDPVO
  - userrowdpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UserRowDPVO

## 📌 Visão Geral

View Object para extração BICC de dados de User Row D. Acessa as tabelas: FF_USER_ROWS_F, FF_USER_ROWS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.UserTablesAM.UserRowDPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 5 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ff_user_rows_f|FF_USER_ROWS_F]] — 17 atributos (3 PKs, 17 BICC)
- [[ff_user_rows_tl|FF_USER_ROWS_TL]] — 3 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[ff_user_rows_f|FF_USER_ROWS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserRowDPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | UserRowDPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | UserRowDPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | UserRowDPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | UserRowDPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | UserRowDPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | UserRowDPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | UserRowDPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | UserRowDPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | UserRowDPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | UserRowDPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 12 | UserRowDPEOModuleId | MODULE_ID | — | ✅ |
| 13 | UserRowDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | UserRowDPEORowHighRange | ROW_HIGH_RANGE | — | ✅ |
| 15 | UserRowDPEORowLowRangeOrName | ROW_LOW_RANGE_OR_NAME | — | ✅ |
| 16 | UserRowDPEOUserRowId | USER_ROW_ID | 🔑 | ✅ |
| 17 | UserRowDPEOUserTableId | USER_TABLE_ID | — | ✅ |

### [[ff_user_rows_tl|FF_USER_ROWS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | UserRowId | USER_ROW_ID | 🔑 | ✅ |
| 3 | UserRowTranslationDPEOUserRowName | ROW_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
