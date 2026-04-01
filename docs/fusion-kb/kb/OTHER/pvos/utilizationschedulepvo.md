---
id: DOC-OTHER-PVO-UtilizationSchedulePVO
doc_type: system-doc
title: "UtilizationSchedulePVO — PVO Cross-Module"
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
  - UtilizationSchedulePVO
  - utilizationschedulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# UtilizationSchedulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Utilization Schedule. Acessa as tabelas: PJR_SUM_OTBI_SCH.

**Caminho:** `FscmTopModelAM.PjrReportingAM.UtilizationSchedulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 4 | 7 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[pjr_sum_otbi_sch|PJR_SUM_OTBI_SCH]] — 12 atributos (4 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[pjr_sum_otbi_sch|PJR_SUM_OTBI_SCH]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 2 | ResourcePoolId | RESOURCE_POOL_ID | 🔑 | ✅ |
| 3 | RollupId | ROLLUP_ID | 🔑 | ✅ |
| 4 | TxnDate | TXN_DATE | 🔑 | ✅ |
| 5 | UtilizationSchedulePEOAvailableHours | AVAILABLE_HOURS | — | ✅ |
| 6 | UtilizationSchedulePEOCreatedBy | CREATED_BY | — | — |
| 7 | UtilizationSchedulePEOCreationDate | CREATION_DATE | — | — |
| 8 | UtilizationSchedulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | UtilizationSchedulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | UtilizationSchedulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | UtilizationSchedulePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | UtilizationSchedulePEOTargetHours | TARGET_HOURS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
