---
id: DOC-OTHER-PVO-TimezoneTranslationBIPVO
doc_type: system-doc
title: "TimezoneTranslationBIPVO — PVO Cross-Module"
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
  - TimezoneTranslationBIPVO
  - timezonetranslationbipvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimezoneTranslationBIPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Timezone Translation BI. Acessa as tabelas: FND_TIMEZONES_TL.

**Caminho:** `FscmTopModelAM.ServiceRequestAM.TimezoneTranslationBIPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 4 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_timezones_tl|FND_TIMEZONES_TL]] — 11 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_timezones_tl|FND_TIMEZONES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | EnterpriseId | ENTERPRISE_ID | — | — |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | Name | NAME | — | ✅ |
| 9 | SeedDataSource | SEED_DATA_SOURCE | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |
| 11 | TimezoneCode | TIMEZONE_CODE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
