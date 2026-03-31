---
id: DOC-OTHER-PVO-TimeRecordGroupUsagePVO
doc_type: system-doc
title: "TimeRecordGroupUsagePVO — PVO Cross-Module"
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
  - TimeRecordGroupUsagePVO
  - timerecordgroupusagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeRecordGroupUsagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Record Group Usage. Acessa as tabelas: HWM_TM_REC_GRP_USAGES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeRecordGroupUsagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_rec_grp_usages|HWM_TM_REC_GRP_USAGES]] — 15 atributos (2 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_rec_grp_usages|HWM_TM_REC_GRP_USAGES]]

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
| 9 | LayerCode | LAYER_CODE | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | 🔑 | ✅ |
| 11 | TimeRecordGroupId | TM_REC_GRP_ID | — | ✅ |
| 12 | TimeRecordGroupUsagesId | TM_REC_GRP_USAGES_ID | 🔑 | ✅ |
| 13 | TimeRecordGroupVersion | TM_REC_GRP_VERSION | — | ✅ |
| 14 | TimeRecordId | TM_REC_ID | — | ✅ |
| 15 | TimeRecordVersion | TM_REC_VERSION | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
