---
id: DOC-OTHER-PVO-SettingItemMandatoryPVO
doc_type: system-doc
title: "SettingItemMandatoryPVO — PVO Cross-Module"
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
  - SettingItemMandatoryPVO
  - settingitemmandatorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SettingItemMandatoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Setting Item Mandatory. Acessa as tabelas: IRC_LC_SETTING_ITEMS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.SettingItemMandatoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 7 | 1 | 1 | 3 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]] — 7 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemKeyName | ITEM_KEY_NAME | — | — |
| 2 | ObjectId | OBJECT_ID | — | — |
| 3 | ObjectType | OBJECT_TYPE | — | — |
| 4 | SettingId | SETTING_ID | — | ✅ |
| 5 | SettingItemCode | SETTING_ITEM_CODE | — | — |
| 6 | SettingItemId | SETTING_ITEM_ID | 🔑 | ✅ |
| 7 | StringValue | STRING_VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
