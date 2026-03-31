---
id: DOC-OTHER-PVO-TimeRepositoryAttributeUsagePVO
doc_type: system-doc
title: "TimeRepositoryAttributeUsagePVO — PVO Cross-Module"
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
  - TimeRepositoryAttributeUsagePVO
  - timerepositoryattributeusagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeRepositoryAttributeUsagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Repository Attribute Usage. Acessa as tabelas: HWM_TM_REP_ATRB_USAGES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeRepositoryAttributeUsagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rep_atrb_usages|HWM_TM_REP_ATRB_USAGES]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rep_atrb_usages|HWM_TM_REP_ATRB_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DataSetId | DATA_SET_ID | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LatestVersion | LATEST_VERSION | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TimeRepositoryAttributeId | TM_REP_ATRB_ID | — | ✅ |
| 11 | TimeRepositoryAttributeUsageId | TM_REP_ATRB_USAGE_ID | 🔑 | ✅ |
| 12 | UsagesSourceGroupLevel | USAGES_SOURCE_GRP_LEVEL | — | ✅ |
| 13 | UsagesSourceId | USAGES_SOURCE_ID | — | ✅ |
| 14 | UsagesSourceVersion | USAGES_SOURCE_VERSION | — | ✅ |
| 15 | UsagesType | USAGES_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
