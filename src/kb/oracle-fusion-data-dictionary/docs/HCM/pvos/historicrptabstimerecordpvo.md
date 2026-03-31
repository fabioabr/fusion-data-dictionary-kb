---
id: DOC-HCM-PVO-HistoricRptAbsTimeRecordPVO
doc_type: system-doc
title: "HistoricRptAbsTimeRecordPVO — PVO Human Capital Management"
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
  - HistoricRptAbsTimeRecordPVO
  - historicrptabstimerecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HistoricRptAbsTimeRecordPVO

## 📌 Visão Geral

Extrai registros históricos de alterações em tempo reportado com timestamps de mudança. Utilizado para auditoria de modificações em timesheets.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.HistoricRptAbsTimeRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 3 | 9 | 60% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_his_rpt_entry_v|HWM_TM_HIS_RPT_ENTRY_V]] — 15 atributos (3 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_his_rpt_entry_v|HWM_TM_HIS_RPT_ENTRY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DayTmRecGrpId | DAY_TM_REC_GRP_ID | — | — |
| 2 | DayTmRecGrpVersion | DAY_TM_REC_GRP_VERSION | — | — |
| 3 | GroupTypeId | GROUP_TYPE_ID | — | — |
| 4 | HistoricChangeDateFrom | HISTORIC_CHANGE_DATE_FROM | — | ✅ |
| 5 | HistoricChangeDateTo | HISTORIC_CHANGE_DATE_TO | — | ✅ |
| 6 | HistoricChangeTime | HISTORIC_CHANGE_TIME | 🔑 | ✅ |
| 7 | TcApprovedTimestamp | TC_APPROVED_TIMESTAMP | — | ✅ |
| 8 | TcSubmittedTimestamp | TC_SUBMITTED_TIMESTAMP | — | ✅ |
| 9 | TcUiStatusValue | TC_UI_STATUS_VALUE | — | ✅ |
| 10 | TcUserStatusValue | TC_USER_STATUS_VALUE | — | ✅ |
| 11 | TimeCardTmRecGrpId | TIME_CARD_TM_REC_GRP_ID | — | — |
| 12 | TimeCardTmRecGrpVersion | TIME_CARD_TM_REC_GRP_VERSION | — | — |
| 13 | TimeRecordId | TIME_RECORD_ID | 🔑 | ✅ |
| 14 | TimeRecordLayerCode | TIME_RECORD_LAYER_CODE | — | — |
| 15 | TimeRecordVersion | TIME_RECORD_VERSION | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
