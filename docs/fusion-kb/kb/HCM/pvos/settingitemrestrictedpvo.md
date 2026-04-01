---
id: DOC-HCM-PVO-SettingItemRestrictedPVO
doc_type: system-doc
title: "SettingItemRestrictedPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SettingItemRestrictedPVO
  - settingitemrestrictedpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SettingItemRestrictedPVO

## 📌 Visão Geral

Disponibiliza itens de configuração restritos em processos de recrutamento. Define parâmetros com acesso controlado no ciclo de vida de contratação.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecProcessLifecycleAM.SettingItemRestrictedPVO`

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
