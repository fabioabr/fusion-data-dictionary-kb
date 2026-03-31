---
id: DOC-OTHER-PVO-ItemPhaseTranslationPVO
doc_type: system-doc
title: "ItemPhaseTranslationPVO — PVO Cross-Module"
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
  - ItemPhaseTranslationPVO
  - itemphasetranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemPhaseTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Phase Translation. Acessa as tabelas: EGP_PHASES_TL.

**Caminho:** `FscmTopModelAM.CommonAnalyticsAM.ItemPhaseTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 4 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[egp_phases_tl|EGP_PHASES_TL]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[egp_phases_tl|EGP_PHASES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemPhaseTranslationCreatedBy | CREATED_BY | — | — |
| 2 | ItemPhaseTranslationCreationDate | CREATION_DATE | — | — |
| 3 | ItemPhaseTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ItemPhaseTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ItemPhaseTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | ItemPhaseTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ItemPhaseTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | ItemPhaseTranslationPhaseCode | PHASE_CODE | 🔑 | ✅ |
| 9 | ItemPhaseTranslationPhaseName | PHASE_NAME | — | ✅ |
| 10 | ItemPhaseTranslationSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
