---
id: DOC-HCM-PVO-HistoricTimeRecordPVO
doc_type: system-doc
title: "HistoricTimeRecordPVO — PVO Human Capital Management"
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
  - HistoricTimeRecordPVO
  - historictimerecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HistoricTimeRecordPVO

## 📌 Visão Geral

Extrai registros históricos de alterações em lançamentos de tempo. Utilizado para auditoria de trail de modificações no controle de jornada.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.HistoricTimeRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_his_entry_v|HWM_TM_HIS_ENTRY_V]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_his_entry_v|HWM_TM_HIS_ENTRY_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DayTimeRecordGroupId | DAY_TM_REC_GRP_ID | — | ✅ |
| 2 | DayTimeRecordGroupVersion | DAY_TM_REC_GRP_VERSION | — | ✅ |
| 3 | HistoricChangeDateFrom | HISTORIC_CHANGE_DATE_FROM | — | ✅ |
| 4 | HistoricChangeDateTo | HISTORIC_CHANGE_DATE_TO | — | ✅ |
| 5 | HistoricChangeTime | HISTORIC_CHANGE_TIME | 🔑 | ✅ |
| 6 | TimeCardApprovedTimestamp | TC_APPROVED_TS | — | ✅ |
| 7 | TimeCardGroupTypeId | GROUP_TYPE_ID | — | ✅ |
| 8 | TimeCardSubmittedTimestamp | TC_SUBMITTED_TS | — | ✅ |
| 9 | TimeCardTimeRecordGroupId | TIME_CARD_TM_REC_GRP_ID | — | ✅ |
| 10 | TimeCardTimeRecordGroupVersion | TIME_CARD_TM_REC_GRP_VERSION | — | ✅ |
| 11 | TimeCardUiStatusValue | TC_UI_STATUS_VALUE | — | ✅ |
| 12 | TimeCardUserStatusValue | TC_USER_STATUS_VALUE | — | ✅ |
| 13 | TimeEntryTimeRecordId | TIME_RECORD_ID | 🔑 | ✅ |
| 14 | TimeEntryTimeRecordVersion | TIME_RECORD_VERSION | 🔑 | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
