---
id: DOC-GL-PVO-ActionReasonsPVO
doc_type: system-doc
title: "ActionReasonsPVO — PVO General Ledger"
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
  - ActionReasonsPVO
  - actionreasonspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionReasonsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Reasons. Acessa as tabelas: PER_ACTION_REASONS_B, PER_ACTION_REASONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionReasonsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 2 | 14 | 52% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_reasons_b|PER_ACTION_REASONS_B]] — 14 atributos (1 PKs, 9 BICC)
- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 13 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[per_action_reasons_b|PER_ACTION_REASONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonId | ACTION_REASON_ID | 🔑 | ✅ |
| 2 | ActionReasonsPEOActionReasonCode | ACTION_REASON_CODE | — | ✅ |
| 3 | ActionReasonsPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 4 | ActionReasonsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | ActionReasonsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | ActionReasonsPEOEndDate | END_DATE | — | ✅ |
| 7 | ActionReasonsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionReasonsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActionReasonsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ActionReasonsPEOModuleId | MODULE_ID | — | — |
| 11 | ActionReasonsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ActionReasonsPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | ActionReasonsPEOSguid | SGUID | — | — |
| 14 | ActionReasonsPEOStartDate | START_DATE | — | ✅ |

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonsTranslationPEOActionReason | ACTION_REASON | — | ✅ |
| 2 | ActionReasonsTranslationPEOActionReasonId | ACTION_REASON_ID | — | — |
| 3 | ActionReasonsTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionReasonsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 5 | ActionReasonsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 6 | ActionReasonsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 7 | ActionReasonsTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | ActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | ActionReasonsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ActionReasonsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ActionReasonsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ActionReasonsTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 13 | ActionReasonsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
