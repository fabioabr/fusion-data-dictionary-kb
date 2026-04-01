---
id: DOC-OTHER-PVO-OptionPVO
doc_type: system-doc
title: "OptionPVO — PVO Cross-Module"
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
  - OptionPVO
  - optionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OptionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Option. Acessa as tabelas: BEN_OPT_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.OptionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 57 | 1 | 3 | 21 | 37% |

---

## 🔗 Tabelas Relacionadas

- [[ben_opt_f|BEN_OPT_F]] — 57 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[ben_opt_f|BEN_OPT_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CarrierOptName | CARRIER_OPT_NAME | — | ✅ |
| 3 | CmbnPtipOptId | CMBN_PTIP_OPT_ID | — | — |
| 4 | ComponentReason | COMPONENT_REASON | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | GlobalFlag | GLOBAL_FLAG | — | ✅ |
| 10 | GroupOptId | GROUP_OPT_ID | — | — |
| 11 | InvkWvOptFlag | INVK_WV_OPT_FLAG | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 16 | LegislationSubgroup | LEGISLATION_SUBGROUP | — | ✅ |
| 17 | MappingTableName | MAPPING_TABLE_NAME | — | ✅ |
| 18 | MappingTablePkId | MAPPING_TABLE_PK_ID | — | — |
| 19 | Name | NAME | — | ✅ |
| 20 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 21 | OptAttribute1 | OPT_ATTRIBUTE1 | — | — |
| 22 | OptAttribute10 | OPT_ATTRIBUTE10 | — | — |
| 23 | OptAttribute11 | OPT_ATTRIBUTE11 | — | — |
| 24 | OptAttribute12 | OPT_ATTRIBUTE12 | — | — |
| 25 | OptAttribute13 | OPT_ATTRIBUTE13 | — | — |
| 26 | OptAttribute14 | OPT_ATTRIBUTE14 | — | — |
| 27 | OptAttribute15 | OPT_ATTRIBUTE15 | — | — |
| 28 | OptAttribute16 | OPT_ATTRIBUTE16 | — | — |
| 29 | OptAttribute17 | OPT_ATTRIBUTE17 | — | — |
| 30 | OptAttribute18 | OPT_ATTRIBUTE18 | — | — |
| 31 | OptAttribute19 | OPT_ATTRIBUTE19 | — | — |
| 32 | OptAttribute2 | OPT_ATTRIBUTE2 | — | — |
| 33 | OptAttribute20 | OPT_ATTRIBUTE20 | — | — |
| 34 | OptAttribute21 | OPT_ATTRIBUTE21 | — | — |
| 35 | OptAttribute22 | OPT_ATTRIBUTE22 | — | — |
| 36 | OptAttribute23 | OPT_ATTRIBUTE23 | — | — |
| 37 | OptAttribute24 | OPT_ATTRIBUTE24 | — | — |
| 38 | OptAttribute25 | OPT_ATTRIBUTE25 | — | — |
| 39 | OptAttribute26 | OPT_ATTRIBUTE26 | — | — |
| 40 | OptAttribute27 | OPT_ATTRIBUTE27 | — | — |
| 41 | OptAttribute28 | OPT_ATTRIBUTE28 | — | — |
| 42 | OptAttribute29 | OPT_ATTRIBUTE29 | — | — |
| 43 | OptAttribute3 | OPT_ATTRIBUTE3 | — | — |
| 44 | OptAttribute30 | OPT_ATTRIBUTE30 | — | — |
| 45 | OptAttribute4 | OPT_ATTRIBUTE4 | — | — |
| 46 | OptAttribute5 | OPT_ATTRIBUTE5 | — | — |
| 47 | OptAttribute6 | OPT_ATTRIBUTE6 | — | — |
| 48 | OptAttribute7 | OPT_ATTRIBUTE7 | — | — |
| 49 | OptAttribute8 | OPT_ATTRIBUTE8 | — | — |
| 50 | OptAttribute9 | OPT_ATTRIBUTE9 | — | — |
| 51 | OptAttributeCategory | OPT_ATTRIBUTE_CATEGORY | — | ✅ |
| 52 | OptId | OPT_ID | 🔑 | ✅ |
| 53 | RqdPerdEnrtNenrtRl | RQD_PERD_ENRT_NENRT_RL | — | — |
| 54 | RqdPerdEnrtNenrtUom | RQD_PERD_ENRT_NENRT_UOM | — | ✅ |
| 55 | RqdPerdEnrtNenrtVal | RQD_PERD_ENRT_NENRT_VAL | — | ✅ |
| 56 | ShortCode | SHORT_CODE | — | ✅ |
| 57 | ShortName | SHORT_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
