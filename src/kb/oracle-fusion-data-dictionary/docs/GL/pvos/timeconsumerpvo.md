---
id: DOC-GL-PVO-TimeConsumerPVO
doc_type: system-doc
title: "TimeConsumerPVO — PVO General Ledger"
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
  - TimeConsumerPVO
  - timeconsumerpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeConsumerPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Consumer. Acessa as tabelas: HWM_TCSMRS_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeConsumerAM.TimeConsumerPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcsmrs_b|HWM_TCSMRS_B]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[hwm_tcsmrs_b|HWM_TCSMRS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 4 | FusionApplication | FUSION_APPLICATION | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ModuleId | MODULE_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | TimeAttributeStructureId | TM_ATRB_STRUCTURE_ID | — | ✅ |
| 11 | TimeConsumersCode | TCSMRS_CODE | — | ✅ |
| 12 | TimeConsumersId | TCSMRS_ID | 🔑 | ✅ |
| 13 | UpdateCalculateTimeService | UPDATE_CALC_TM_SVC | — | ✅ |
| 14 | UpdateRawTimeService | UPDATE_RAW_TM_SVC | — | ✅ |
| 15 | ValidateCalculateTimeService | VALIDATE_CALC_TM_SVC | — | ✅ |
| 16 | ValidateRawTimeService | VALIDATE_RAW_TM_SVC | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
