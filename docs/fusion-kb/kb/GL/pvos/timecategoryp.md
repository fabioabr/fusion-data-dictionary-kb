---
id: DOC-GL-PVO-TimeCategoryP
doc_type: system-doc
title: "TimeCategoryP — PVO General Ledger"
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
  - TimeCategoryP
  - timecategoryp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeCategoryP

## 📌 Visão Geral

View Object para extração BICC de dados de Time Category P. Acessa as tabelas: HWM_TCATS_B, HWM_TCATS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeCategoryAM.TimeCategoryP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 12 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcats_b|HWM_TCATS_B]] — 14 atributos (1 PKs, 7 BICC)
- [[hwm_tcats_tl|HWM_TCATS_TL]] — 13 atributos (5 BICC)

---

## ⚙️ Atributos

### [[hwm_tcats_b|HWM_TCATS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcatId | TCAT_ID | 🔑 | ✅ |
| 2 | TimeCategoryBPEOCreatedBy | CREATED_BY | — | — |
| 3 | TimeCategoryBPEOCreationDate | CREATION_DATE | — | — |
| 4 | TimeCategoryBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | TimeCategoryBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TimeCategoryBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | TimeCategoryBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | TimeCategoryBPEOModuleId | MODULE_ID | — | — |
| 9 | TimeCategoryBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TimeCategoryBPEOPersistentFlag | PERSISTENT_FLAG | — | ✅ |
| 11 | TimeCategoryBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | TimeCategoryBPEOSguid | SGUID | — | — |
| 13 | TimeCategoryBPEOTcatCd | TCAT_CD | — | ✅ |
| 14 | TimeCategoryBPEOUom | UOM | — | ✅ |

### [[hwm_tcats_tl|HWM_TCATS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TimeCategoryTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TimeCategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | TimeCategoryTLPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | TimeCategoryTLPEOLanguage | LANGUAGE | — | — |
| 6 | TimeCategoryTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | TimeCategoryTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | TimeCategoryTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | TimeCategoryTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TimeCategoryTLPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | TimeCategoryTLPEOSourceLang | SOURCE_LANG | — | — |
| 12 | TimeCategoryTLPEOTcatId | TCAT_ID | — | — |
| 13 | TimeCategoryTLPEOTcatName | TCAT_NAME | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
