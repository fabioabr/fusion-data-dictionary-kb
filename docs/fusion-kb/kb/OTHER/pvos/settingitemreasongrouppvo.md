---
id: DOC-OTHER-PVO-SettingItemReasonGroupPVO
doc_type: system-doc
title: "SettingItemReasonGroupPVO — PVO Cross-Module"
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
  - SettingItemReasonGroupPVO
  - settingitemreasongrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SettingItemReasonGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Setting Item Reason Group. Acessa as tabelas: IRC_LC_REASON_GROUPS_TL, IRC_LC_SETTING_ITEMS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.SettingItemReasonGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 2 | 1 | 3 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[irc_lc_reason_groups_tl|IRC_LC_REASON_GROUPS_TL]] — 3 atributos (2 BICC)
- [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]] — 7 atributos (1 PKs, 1 BICC)

---

## ⚙️ Atributos

### [[irc_lc_reason_groups_tl|IRC_LC_REASON_GROUPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReasonGroupTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | ReasonGroupTranslationPEOReasonGroupId | REASON_GROUP_ID | — | ✅ |
| 3 | ReasonGroupTranslationPEOReasonGroupName | REASON_GROUP_NAME | — | ✅ |

### [[irc_lc_setting_items|IRC_LC_SETTING_ITEMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemKeyName | ITEM_KEY_NAME | — | — |
| 2 | ObjectId | OBJECT_ID | — | — |
| 3 | ObjectType | OBJECT_TYPE | — | — |
| 4 | SettingId | SETTING_ID | — | — |
| 5 | SettingItemCode | SETTING_ITEM_CODE | — | — |
| 6 | SettingItemId | SETTING_ITEM_ID | 🔑 | ✅ |
| 7 | StringValue | STRING_VALUE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
