---
id: DOC-OTHER-PVO-WorkCenterProductionCalendarExtractPVO
doc_type: system-doc
title: "WorkCenterProductionCalendarExtractPVO — PVO Cross-Module"
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
  - WorkCenterProductionCalendarExtractPVO
  - workcenterproductioncalendarextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterProductionCalendarExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center Production Calendar Extract. Acessa as tabelas: WIS_WC_PROD_CALENDARS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WorkCenterProductionCalendarExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_wc_prod_calendars|WIS_WC_PROD_CALENDARS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_wc_prod_calendars|WIS_WC_PROD_CALENDARS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EffectiveFromDate | EFFECTIVE_FROM_DATE | — | ✅ |
| 4 | EffectiveToDate | EFFECTIVE_TO_DATE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | MfgCalendarId | MFG_CALENDAR_ID | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | WcProdCalendarId | WC_PROD_CALENDAR_ID | 🔑 | ✅ |
| 11 | WorkCenterId | WORK_CENTER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
