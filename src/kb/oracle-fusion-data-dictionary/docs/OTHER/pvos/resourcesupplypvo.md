---
id: DOC-OTHER-PVO-ResourceSupplyPVO
doc_type: system-doc
title: "ResourceSupplyPVO — PVO Cross-Module"
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
  - ResourceSupplyPVO
  - resourcesupplypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceSupplyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Supply. Acessa as tabelas: PJT_PRJ_ENTERPRISE_RESOURCE_VL, ZMM_SR_SCHEDULE_DTLS, ZMM_SR_SHIFTS_VL.

**Caminho:** `FscmTopModelAM.PjrResourceAM.ResourceSupplyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 3 | 1 | 2 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]] — 1 atributos (1 PKs, 1 BICC)
- [[zmm_sr_schedule_dtls|ZMM_SR_SCHEDULE_DTLS]] — 3 atributos
- [[zmm_sr_shifts_vl|ZMM_SR_SHIFTS_VL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjt_prj_enterprise_resource_vl|PJT_PRJ_ENTERPRISE_RESOURCE_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceId | RESOURCE_ID | 🔑 | ✅ |

### [[zmm_sr_schedule_dtls|ZMM_SR_SCHEDULE_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ScheduleDetailEOShiftId | SHIFT_ID | — | — |
| 2 | ScheduleDetailEOStartDateTime | START_DATE_TIME | — | — |
| 3 | ScheduleDetailId | SCHEDULE_DETAIL_ID | — | — |

### [[zmm_sr_shifts_vl|ZMM_SR_SHIFTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ShiftEODurationMsNum | DURATION_MS_NUM | — | ✅ |
| 2 | ShiftEOShiftName | SHIFT_NAME | — | — |
| 3 | ShiftId | SHIFT_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
