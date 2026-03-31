---
id: DOC-OTHER-PVO-ActionReasonsTranslationPVO
doc_type: system-doc
title: "ActionReasonsTranslationPVO — PVO Cross-Module"
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
  - ActionReasonsTranslationPVO
  - actionreasonstranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActionReasonsTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Action Reasons Translation. Acessa as tabelas: PER_ACTION_REASONS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ActionAM.ActionReasonsTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 3 | 23% |

---

## 🔗 Tabelas Relacionadas

- [[per_action_reasons_tl|PER_ACTION_REASONS_TL]] — 13 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[per_action_reasons_tl|PER_ACTION_REASONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionReasonId | ACTION_REASON_ID | 🔑 | ✅ |
| 2 | ActionReasonsTranslationPEOActionReason | ACTION_REASON | — | — |
| 3 | ActionReasonsTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | ActionReasonsTranslationPEOCreatedBy | CREATED_BY | — | — |
| 5 | ActionReasonsTranslationPEOCreationDate | CREATION_DATE | — | — |
| 6 | ActionReasonsTranslationPEODescription | DESCRIPTION | — | — |
| 7 | ActionReasonsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ActionReasonsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | ActionReasonsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | ActionReasonsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ActionReasonsTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | ActionReasonsTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
