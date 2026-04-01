---
id: DOC-HCM-PVO-TrainingSupplierResourcePVO
doc_type: system-doc
title: "TrainingSupplierResourcePVO — PVO Human Capital Management"
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
  - TrainingSupplierResourcePVO
  - trainingsupplierresourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TrainingSupplierResourcePVO

## 📌 Visão Geral

Disponibiliza recursos de fornecedores de treinamento (instrutores externos, salas) com capacidade. Suporta gestão de fornecedores no Oracle Learning.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.TrainingSupplierResourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 88 | 2 | 1 | 6 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_resources_b|WLF_RESOURCES_B]] — 76 atributos (1 PKs, 4 BICC)
- [[wlf_resources_tl|WLF_RESOURCES_TL]] — 12 atributos (2 BICC)

---

## ⚙️ Atributos

### [[wlf_resources_b|WLF_RESOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrainingSupplierResourcePEOAddressId | ADDRESS_ID | — | — |
| 2 | TrainingSupplierResourcePEOAttributionId | ATTRIBUTION_ID | — | — |
| 3 | TrainingSupplierResourcePEOAttributionType | ATTRIBUTION_TYPE | — | — |
| 4 | TrainingSupplierResourcePEOCapacity | CAPACITY | — | — |
| 5 | TrainingSupplierResourcePEOContactId | CONTACT_ID | — | — |
| 6 | TrainingSupplierResourcePEOCreatedBy | CREATED_BY | — | — |
| 7 | TrainingSupplierResourcePEOCreationDate | CREATION_DATE | — | — |
| 8 | TrainingSupplierResourcePEOEnterpriseId | ENTERPRISE_ID | — | — |
| 9 | TrainingSupplierResourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 10 | TrainingSupplierResourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | TrainingSupplierResourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | TrainingSupplierResourcePEOLocationId | LOCATION_ID | — | — |
| 13 | TrainingSupplierResourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | TrainingSupplierResourcePEOResourceId | RESOURCE_ID | 🔑 | ✅ |
| 15 | TrainingSupplierResourcePEOResourceNumber | RESOURCE_NUMBER | — | ✅ |
| 16 | TrainingSupplierResourcePEOResourceType | RESOURCE_TYPE | — | ✅ |
| 17 | TrainingSupplierResourcePEORsAttribute1 | RS_ATTRIBUTE1 | — | — |
| 18 | TrainingSupplierResourcePEORsAttribute10 | RS_ATTRIBUTE10 | — | — |
| 19 | TrainingSupplierResourcePEORsAttribute11 | RS_ATTRIBUTE11 | — | — |
| 20 | TrainingSupplierResourcePEORsAttribute12 | RS_ATTRIBUTE12 | — | — |
| 21 | TrainingSupplierResourcePEORsAttribute13 | RS_ATTRIBUTE13 | — | — |
| 22 | TrainingSupplierResourcePEORsAttribute14 | RS_ATTRIBUTE14 | — | — |
| 23 | TrainingSupplierResourcePEORsAttribute15 | RS_ATTRIBUTE15 | — | — |
| 24 | TrainingSupplierResourcePEORsAttribute16 | RS_ATTRIBUTE16 | — | — |
| 25 | TrainingSupplierResourcePEORsAttribute17 | RS_ATTRIBUTE17 | — | — |
| 26 | TrainingSupplierResourcePEORsAttribute18 | RS_ATTRIBUTE18 | — | — |
| 27 | TrainingSupplierResourcePEORsAttribute19 | RS_ATTRIBUTE19 | — | — |
| 28 | TrainingSupplierResourcePEORsAttribute2 | RS_ATTRIBUTE2 | — | — |
| 29 | TrainingSupplierResourcePEORsAttribute20 | RS_ATTRIBUTE20 | — | — |
| 30 | TrainingSupplierResourcePEORsAttribute3 | RS_ATTRIBUTE3 | — | — |
| 31 | TrainingSupplierResourcePEORsAttribute4 | RS_ATTRIBUTE4 | — | — |
| 32 | TrainingSupplierResourcePEORsAttribute5 | RS_ATTRIBUTE5 | — | — |
| 33 | TrainingSupplierResourcePEORsAttribute6 | RS_ATTRIBUTE6 | — | — |
| 34 | TrainingSupplierResourcePEORsAttribute7 | RS_ATTRIBUTE7 | — | — |
| 35 | TrainingSupplierResourcePEORsAttribute8 | RS_ATTRIBUTE8 | — | — |
| 36 | TrainingSupplierResourcePEORsAttribute9 | RS_ATTRIBUTE9 | — | — |
| 37 | TrainingSupplierResourcePEORsAttributeCategory | RS_ATTRIBUTE_CATEGORY | — | — |
| 38 | TrainingSupplierResourcePEORsAttributeDate1 | RS_ATTRIBUTE_DATE1 | — | — |
| 39 | TrainingSupplierResourcePEORsAttributeDate10 | RS_ATTRIBUTE_DATE10 | — | — |
| 40 | TrainingSupplierResourcePEORsAttributeDate11 | RS_ATTRIBUTE_DATE11 | — | — |
| 41 | TrainingSupplierResourcePEORsAttributeDate12 | RS_ATTRIBUTE_DATE12 | — | — |
| 42 | TrainingSupplierResourcePEORsAttributeDate13 | RS_ATTRIBUTE_DATE13 | — | — |
| 43 | TrainingSupplierResourcePEORsAttributeDate14 | RS_ATTRIBUTE_DATE14 | — | — |
| 44 | TrainingSupplierResourcePEORsAttributeDate15 | RS_ATTRIBUTE_DATE15 | — | — |
| 45 | TrainingSupplierResourcePEORsAttributeDate2 | RS_ATTRIBUTE_DATE2 | — | — |
| 46 | TrainingSupplierResourcePEORsAttributeDate3 | RS_ATTRIBUTE_DATE3 | — | — |
| 47 | TrainingSupplierResourcePEORsAttributeDate4 | RS_ATTRIBUTE_DATE4 | — | — |
| 48 | TrainingSupplierResourcePEORsAttributeDate5 | RS_ATTRIBUTE_DATE5 | — | — |
| 49 | TrainingSupplierResourcePEORsAttributeDate6 | RS_ATTRIBUTE_DATE6 | — | — |
| 50 | TrainingSupplierResourcePEORsAttributeDate7 | RS_ATTRIBUTE_DATE7 | — | — |
| 51 | TrainingSupplierResourcePEORsAttributeDate8 | RS_ATTRIBUTE_DATE8 | — | — |
| 52 | TrainingSupplierResourcePEORsAttributeDate9 | RS_ATTRIBUTE_DATE9 | — | — |
| 53 | TrainingSupplierResourcePEORsAttributeNumber1 | RS_ATTRIBUTE_NUMBER1 | — | — |
| 54 | TrainingSupplierResourcePEORsAttributeNumber10 | RS_ATTRIBUTE_NUMBER10 | — | — |
| 55 | TrainingSupplierResourcePEORsAttributeNumber11 | RS_ATTRIBUTE_NUMBER11 | — | — |
| 56 | TrainingSupplierResourcePEORsAttributeNumber12 | RS_ATTRIBUTE_NUMBER12 | — | — |
| 57 | TrainingSupplierResourcePEORsAttributeNumber13 | RS_ATTRIBUTE_NUMBER13 | — | — |
| 58 | TrainingSupplierResourcePEORsAttributeNumber14 | RS_ATTRIBUTE_NUMBER14 | — | — |
| 59 | TrainingSupplierResourcePEORsAttributeNumber15 | RS_ATTRIBUTE_NUMBER15 | — | — |
| 60 | TrainingSupplierResourcePEORsAttributeNumber16 | RS_ATTRIBUTE_NUMBER16 | — | — |
| 61 | TrainingSupplierResourcePEORsAttributeNumber17 | RS_ATTRIBUTE_NUMBER17 | — | — |
| 62 | TrainingSupplierResourcePEORsAttributeNumber18 | RS_ATTRIBUTE_NUMBER18 | — | — |
| 63 | TrainingSupplierResourcePEORsAttributeNumber19 | RS_ATTRIBUTE_NUMBER19 | — | — |
| 64 | TrainingSupplierResourcePEORsAttributeNumber2 | RS_ATTRIBUTE_NUMBER2 | — | — |
| 65 | TrainingSupplierResourcePEORsAttributeNumber20 | RS_ATTRIBUTE_NUMBER20 | — | — |
| 66 | TrainingSupplierResourcePEORsAttributeNumber3 | RS_ATTRIBUTE_NUMBER3 | — | — |
| 67 | TrainingSupplierResourcePEORsAttributeNumber4 | RS_ATTRIBUTE_NUMBER4 | — | — |
| 68 | TrainingSupplierResourcePEORsAttributeNumber5 | RS_ATTRIBUTE_NUMBER5 | — | — |
| 69 | TrainingSupplierResourcePEORsAttributeNumber6 | RS_ATTRIBUTE_NUMBER6 | — | — |
| 70 | TrainingSupplierResourcePEORsAttributeNumber7 | RS_ATTRIBUTE_NUMBER7 | — | — |
| 71 | TrainingSupplierResourcePEORsAttributeNumber8 | RS_ATTRIBUTE_NUMBER8 | — | — |
| 72 | TrainingSupplierResourcePEORsAttributeNumber9 | RS_ATTRIBUTE_NUMBER9 | — | — |
| 73 | TrainingSupplierResourcePEOSourceId | SOURCE_ID | — | — |
| 74 | TrainingSupplierResourcePEOSourceType | SOURCE_TYPE | — | — |
| 75 | TrainingSupplierResourcePEOStatus | STATUS | — | ✅ |
| 76 | TrainingSupplierResourcePEOTrainingVendorResId | TRAINING_VENDOR_RES_ID | — | — |

### [[wlf_resources_tl|WLF_RESOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TrainingSupplierResourceTranslationPEOCreatedBy1 | CREATED_BY | — | — |
| 2 | TrainingSupplierResourceTranslationPEOCreationDate1 | CREATION_DATE | — | — |
| 3 | TrainingSupplierResourceTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | TrainingSupplierResourceTranslationPEOEnterpriseId1 | ENTERPRISE_ID | — | — |
| 5 | TrainingSupplierResourceTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | TrainingSupplierResourceTranslationPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 7 | TrainingSupplierResourceTranslationPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 8 | TrainingSupplierResourceTranslationPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 9 | TrainingSupplierResourceTranslationPEOName | NAME | — | ✅ |
| 10 | TrainingSupplierResourceTranslationPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 11 | TrainingSupplierResourceTranslationPEOResourceId1 | RESOURCE_ID | — | — |
| 12 | TrainingSupplierResourceTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
