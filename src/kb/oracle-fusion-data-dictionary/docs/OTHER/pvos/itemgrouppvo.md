---
id: DOC-OTHER-PVO-ItemGroupPVO
doc_type: system-doc
title: "ItemGroupPVO — PVO Cross-Module"
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
  - ItemGroupPVO
  - itemgrouppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemGroupPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Group. Acessa as tabelas: VRM_ITEM_GROUPS_VL.

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.ItemGroupPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 41 | 1 | 1 | 4 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_item_groups_vl|VRM_ITEM_GROUPS_VL]] — 41 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[vrm_item_groups_vl|VRM_ITEM_GROUPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemGroupId | ITEM_GROUP_ID | 🔑 | ✅ |
| 2 | ItemGroupPEOAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ItemGroupPEOAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ItemGroupPEOAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ItemGroupPEOAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ItemGroupPEOAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ItemGroupPEOAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ItemGroupPEOAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ItemGroupPEOAttribute16 | ATTRIBUTE16 | — | — |
| 10 | ItemGroupPEOAttribute17 | ATTRIBUTE17 | — | — |
| 11 | ItemGroupPEOAttribute18 | ATTRIBUTE18 | — | — |
| 12 | ItemGroupPEOAttribute19 | ATTRIBUTE19 | — | — |
| 13 | ItemGroupPEOAttribute2 | ATTRIBUTE2 | — | — |
| 14 | ItemGroupPEOAttribute20 | ATTRIBUTE20 | — | — |
| 15 | ItemGroupPEOAttribute3 | ATTRIBUTE3 | — | — |
| 16 | ItemGroupPEOAttribute4 | ATTRIBUTE4 | — | — |
| 17 | ItemGroupPEOAttribute5 | ATTRIBUTE5 | — | — |
| 18 | ItemGroupPEOAttribute6 | ATTRIBUTE6 | — | — |
| 19 | ItemGroupPEOAttribute7 | ATTRIBUTE7 | — | — |
| 20 | ItemGroupPEOAttribute8 | ATTRIBUTE8 | — | — |
| 21 | ItemGroupPEOAttribute9 | ATTRIBUTE9 | — | — |
| 22 | ItemGroupPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 23 | ItemGroupPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 24 | ItemGroupPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | ItemGroupPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | ItemGroupPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | ItemGroupPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | ItemGroupPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 29 | ItemGroupPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 30 | ItemGroupPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 31 | ItemGroupPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 32 | ItemGroupPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 33 | ItemGroupPEOCreatedBy | CREATED_BY | — | — |
| 34 | ItemGroupPEOCreationDate | CREATION_DATE | — | — |
| 35 | ItemGroupPEODescription | DESCRIPTION | — | ✅ |
| 36 | ItemGroupPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 37 | ItemGroupPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 38 | ItemGroupPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 39 | ItemGroupPEOName | NAME | — | ✅ |
| 40 | ItemGroupPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 41 | ItemGroupPEOStatus | STATUS | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
