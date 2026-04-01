---
id: DOC-HCM-PVO-TimeRecordGroupUsagePVO
doc_type: system-doc
title: "TimeRecordGroupUsagePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
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

Disponibiliza usos de grupos de registros de tempo com datasets associados. Vincula conjuntos de registros a contextos operacionais de processamento de jornada.

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
