---
id: DOC-OTHER-PVO-ActionReasonsUsagesPVO
doc_type: system-doc
title: "ActionReasonsUsagesPVO — PVO Cross-Module"
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
  - ActionReasonsUsagesPVO
  - actionreasonsusagespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionReasonsUsagesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Reasons Usages. Acessa as tabelas: PER_ACTION_REASON_USAGES.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionReasonsUsagesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 4 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_reason_usages|PER_ACTION_REASON_USAGES]] — 15 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_action_reason_usages|PER_ACTION_REASON_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonUsageId | ACTION_REASON_USAGE_ID | 🔑 | ✅ |
| 2 | ActionReasonUsagesPEOActionCode | ACTION_CODE | — | — |
| 3 | ActionReasonUsagesPEOActionId | ACTION_ID | — | ✅ |
| 4 | ActionReasonUsagesPEOActionReasonCode | ACTION_REASON_CODE | — | — |
| 5 | ActionReasonUsagesPEOActionReasonId | ACTION_REASON_ID | — | ✅ |
| 6 | ActionReasonUsagesPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 7 | ActionReasonUsagesPEOCreatedBy | CREATED_BY | — | — |
| 8 | ActionReasonUsagesPEOCreationDate | CREATION_DATE | — | — |
| 9 | ActionReasonUsagesPEOEndDate | END_DATE | — | — |
| 10 | ActionReasonUsagesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | ActionReasonUsagesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ActionReasonUsagesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ActionReasonUsagesPEOModuleId | MODULE_ID | — | — |
| 14 | ActionReasonUsagesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | ActionReasonUsagesPEOStartDate | START_DATE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
