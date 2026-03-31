---
id: DOC-OTHER-PVO-WDMaintenanceNameTranslationExtractPVO
doc_type: system-doc
title: "WDMaintenanceNameTranslationExtractPVO — PVO Cross-Module"
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
  - WDMaintenanceNameTranslationExtractPVO
  - wdmaintenancenametranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WDMaintenanceNameTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de WDMaintenance Name Translation Extract. Acessa as tabelas: WIS_WD_MAINTENANCE_NAMES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WDMaintenanceNameTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_wd_maintenance_names_tl|WIS_WD_MAINTENANCE_NAMES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_wd_maintenance_names_tl|WIS_WD_MAINTENANCE_NAMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MaintenanceWdDesc | MAINTENANCE_WD_DESC | — | ✅ |
| 8 | MaintenanceWdName | MAINTENANCE_WD_NAME | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |
| 11 | WdMntNameId | WD_MNT_NAME_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
