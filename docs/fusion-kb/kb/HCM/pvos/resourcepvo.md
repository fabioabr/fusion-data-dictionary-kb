---
id: DOC-HCM-PVO-ResourcePVO
doc_type: system-doc
title: "ResourcePVO — PVO Human Capital Management"
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
  - ResourcePVO
  - resourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourcePVO

## 📌 Visão Geral

Disponibiliza recursos de aprendizagem (instrutores, salas, materiais) com capacidade e tipo. Suporta planejamento logístico de treinamentos no Oracle Learning.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.ResourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 88 | 2 | 1 | 7 | 8% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_resources_b|WLF_RESOURCES_B]] — 76 atributos (1 PKs, 5 BICC)
- [[wlf_resources_tl|WLF_RESOURCES_TL]] — 12 atributos (2 BICC)

---

## ⚙️ Atributos

### [[wlf_resources_b|WLF_RESOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourcePEOAddressId | ADDRESS_ID | — | — |
| 2 | ResourcePEOAttributionId | ATTRIBUTION_ID | — | — |
| 3 | ResourcePEOAttributionType | ATTRIBUTION_TYPE | — | — |
| 4 | ResourcePEOCapacity | CAPACITY | — | ✅ |
| 5 | ResourcePEOContactId | CONTACT_ID | — | — |
| 6 | ResourcePEOCreatedBy | CREATED_BY | — | — |
| 7 | ResourcePEOCreationDate | CREATION_DATE | — | — |
| 8 | ResourcePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | ResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | ResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ResourcePEOLocationId | LOCATION_ID | — | — |
| 13 | ResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ResourcePEOResourceId | RESOURCE_ID | 🔑 | ✅ |
| 15 | ResourcePEOResourceNumber | RESOURCE_NUMBER | — | ✅ |
| 16 | ResourcePEOResourceType | RESOURCE_TYPE | — | ✅ |
| 17 | ResourcePEORsAttribute1 | RS_ATTRIBUTE1 | — | — |
| 18 | ResourcePEORsAttribute10 | RS_ATTRIBUTE10 | — | — |
| 19 | ResourcePEORsAttribute11 | RS_ATTRIBUTE11 | — | — |
| 20 | ResourcePEORsAttribute12 | RS_ATTRIBUTE12 | — | — |
| 21 | ResourcePEORsAttribute13 | RS_ATTRIBUTE13 | — | — |
| 22 | ResourcePEORsAttribute14 | RS_ATTRIBUTE14 | — | — |
| 23 | ResourcePEORsAttribute15 | RS_ATTRIBUTE15 | — | — |
| 24 | ResourcePEORsAttribute16 | RS_ATTRIBUTE16 | — | — |
| 25 | ResourcePEORsAttribute17 | RS_ATTRIBUTE17 | — | — |
| 26 | ResourcePEORsAttribute18 | RS_ATTRIBUTE18 | — | — |
| 27 | ResourcePEORsAttribute19 | RS_ATTRIBUTE19 | — | — |
| 28 | ResourcePEORsAttribute2 | RS_ATTRIBUTE2 | — | — |
| 29 | ResourcePEORsAttribute20 | RS_ATTRIBUTE20 | — | — |
| 30 | ResourcePEORsAttribute3 | RS_ATTRIBUTE3 | — | — |
| 31 | ResourcePEORsAttribute4 | RS_ATTRIBUTE4 | — | — |
| 32 | ResourcePEORsAttribute5 | RS_ATTRIBUTE5 | — | — |
| 33 | ResourcePEORsAttribute6 | RS_ATTRIBUTE6 | — | — |
| 34 | ResourcePEORsAttribute7 | RS_ATTRIBUTE7 | — | — |
| 35 | ResourcePEORsAttribute8 | RS_ATTRIBUTE8 | — | — |
| 36 | ResourcePEORsAttribute9 | RS_ATTRIBUTE9 | — | — |
| 37 | ResourcePEORsAttributeCategory | RS_ATTRIBUTE_CATEGORY | — | — |
| 38 | ResourcePEORsAttributeDate1 | RS_ATTRIBUTE_DATE1 | — | — |
| 39 | ResourcePEORsAttributeDate10 | RS_ATTRIBUTE_DATE10 | — | — |
| 40 | ResourcePEORsAttributeDate11 | RS_ATTRIBUTE_DATE11 | — | — |
| 41 | ResourcePEORsAttributeDate12 | RS_ATTRIBUTE_DATE12 | — | — |
| 42 | ResourcePEORsAttributeDate13 | RS_ATTRIBUTE_DATE13 | — | — |
| 43 | ResourcePEORsAttributeDate14 | RS_ATTRIBUTE_DATE14 | — | — |
| 44 | ResourcePEORsAttributeDate15 | RS_ATTRIBUTE_DATE15 | — | — |
| 45 | ResourcePEORsAttributeDate2 | RS_ATTRIBUTE_DATE2 | — | — |
| 46 | ResourcePEORsAttributeDate3 | RS_ATTRIBUTE_DATE3 | — | — |
| 47 | ResourcePEORsAttributeDate4 | RS_ATTRIBUTE_DATE4 | — | — |
| 48 | ResourcePEORsAttributeDate5 | RS_ATTRIBUTE_DATE5 | — | — |
| 49 | ResourcePEORsAttributeDate6 | RS_ATTRIBUTE_DATE6 | — | — |
| 50 | ResourcePEORsAttributeDate7 | RS_ATTRIBUTE_DATE7 | — | — |
| 51 | ResourcePEORsAttributeDate8 | RS_ATTRIBUTE_DATE8 | — | — |
| 52 | ResourcePEORsAttributeDate9 | RS_ATTRIBUTE_DATE9 | — | — |
| 53 | ResourcePEORsAttributeNumber1 | RS_ATTRIBUTE_NUMBER1 | — | — |
| 54 | ResourcePEORsAttributeNumber10 | RS_ATTRIBUTE_NUMBER10 | — | — |
| 55 | ResourcePEORsAttributeNumber11 | RS_ATTRIBUTE_NUMBER11 | — | — |
| 56 | ResourcePEORsAttributeNumber12 | RS_ATTRIBUTE_NUMBER12 | — | — |
| 57 | ResourcePEORsAttributeNumber13 | RS_ATTRIBUTE_NUMBER13 | — | — |
| 58 | ResourcePEORsAttributeNumber14 | RS_ATTRIBUTE_NUMBER14 | — | — |
| 59 | ResourcePEORsAttributeNumber15 | RS_ATTRIBUTE_NUMBER15 | — | — |
| 60 | ResourcePEORsAttributeNumber16 | RS_ATTRIBUTE_NUMBER16 | — | — |
| 61 | ResourcePEORsAttributeNumber17 | RS_ATTRIBUTE_NUMBER17 | — | — |
| 62 | ResourcePEORsAttributeNumber18 | RS_ATTRIBUTE_NUMBER18 | — | — |
| 63 | ResourcePEORsAttributeNumber19 | RS_ATTRIBUTE_NUMBER19 | — | — |
| 64 | ResourcePEORsAttributeNumber2 | RS_ATTRIBUTE_NUMBER2 | — | — |
| 65 | ResourcePEORsAttributeNumber20 | RS_ATTRIBUTE_NUMBER20 | — | — |
| 66 | ResourcePEORsAttributeNumber3 | RS_ATTRIBUTE_NUMBER3 | — | — |
| 67 | ResourcePEORsAttributeNumber4 | RS_ATTRIBUTE_NUMBER4 | — | — |
| 68 | ResourcePEORsAttributeNumber5 | RS_ATTRIBUTE_NUMBER5 | — | — |
| 69 | ResourcePEORsAttributeNumber6 | RS_ATTRIBUTE_NUMBER6 | — | — |
| 70 | ResourcePEORsAttributeNumber7 | RS_ATTRIBUTE_NUMBER7 | — | — |
| 71 | ResourcePEORsAttributeNumber8 | RS_ATTRIBUTE_NUMBER8 | — | — |
| 72 | ResourcePEORsAttributeNumber9 | RS_ATTRIBUTE_NUMBER9 | — | — |
| 73 | ResourcePEOSourceId | SOURCE_ID | — | — |
| 74 | ResourcePEOSourceType | SOURCE_TYPE | — | — |
| 75 | ResourcePEOStatus | STATUS | — | ✅ |
| 76 | ResourcePEOTrainingVendorResId | TRAINING_VENDOR_RES_ID | — | — |

### [[wlf_resources_tl|WLF_RESOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ResourceTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ResourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ResourceTranslationPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | ResourceTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | ResourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ResourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ResourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ResourceTranslationPEOName | NAME | — | ✅ |
| 10 | ResourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ResourceTranslationPEOResourceId | RESOURCE_ID | — | — |
| 12 | ResourceTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
