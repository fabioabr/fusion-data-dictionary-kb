---
id: DOC-OTHER-PVO-LegislativeDataGroupTranslationPVO
doc_type: system-doc
title: "LegislativeDataGroupTranslationPVO — PVO Cross-Module"
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
  - LegislativeDataGroupTranslationPVO
  - legislativedatagrouptranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegislativeDataGroupTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legislative Data Group Translation. Acessa as tabelas: PER_LEGISLATIVE_DATA_GROUPS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LegislativeDataGroupAM.LegislativeDataGroupTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_legislative_data_groups_tl|PER_LEGISLATIVE_DATA_GROUPS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_legislative_data_groups_tl|PER_LEGISLATIVE_DATA_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | 🔑 | ✅ |
| 3 | LegislativeDataGroupTLEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | LegislativeDataGroupTLEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | LegislativeDataGroupTLEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LegislativeDataGroupTLEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LegislativeDataGroupTLEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LegislativeDataGroupTLEOName | NAME | — | ✅ |
| 9 | LegislativeDataGroupTLEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | LegislativeDataGroupTLEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
