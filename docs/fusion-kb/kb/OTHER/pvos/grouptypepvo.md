---
id: DOC-OTHER-PVO-GroupTypePVO
doc_type: system-doc
title: "GroupTypePVO — PVO Cross-Module"
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
  - GroupTypePVO
  - grouptypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Type. Acessa as tabelas: HWM_GRP_TYPE.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_grp_type|HWM_GRP_TYPE]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[hwm_grp_type|HWM_GRP_TYPE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | GroupLevel | GRP_LEVEL | — | ✅ |
| 6 | GroupRowId | GROUP_ROW_ID | 🔑 | ✅ |
| 7 | GroupType | GRP_TYPE | — | ✅ |
| 8 | GroupTypeId | GRP_TYPE_ID | — | ✅ |
| 9 | IsTimeRecord | IS_TM_REC | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | LayerId | LAYER_ID | — | ✅ |
| 14 | ModuleId | MODULE_ID | — | ✅ |
| 15 | Name | NAME | — | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ParentGroupId | PARENT_GRP_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
