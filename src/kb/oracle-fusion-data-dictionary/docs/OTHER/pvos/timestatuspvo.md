---
id: DOC-OTHER-PVO-TimeStatusPVO
doc_type: system-doc
title: "TimeStatusPVO — PVO Cross-Module"
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
  - TimeStatusPVO
  - timestatuspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeStatusPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Status. Acessa as tabelas: HWM_TM_STATUSES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeRepositoryAM.TimeStatusPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_statuses|HWM_TM_STATUSES]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_statuses|HWM_TM_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DateFrom | DATE_FROM | — | ✅ |
| 4 | DateTo | DATE_TO | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ModuleId | MODULE_ID | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ResourceId | RESOURCE_ID | — | ✅ |
| 12 | StatusId | STATUS_ID | 🔑 | ✅ |
| 13 | StatusValue | STATUS_VALUE | — | ✅ |
| 14 | TimeBuildingBlockId | TM_BLDG_BLK_ID | — | ✅ |
| 15 | TimeBuildingBlockVersion | TM_BLDG_BLK_VERSION | — | ✅ |
| 16 | TimeStatusDefId | TM_STATUS_DEF_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
