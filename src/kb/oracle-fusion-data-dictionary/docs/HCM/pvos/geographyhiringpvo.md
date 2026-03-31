---
id: DOC-HCM-PVO-GeographyHiringPVO
doc_type: system-doc
title: "GeographyHiringPVO — PVO Human Capital Management"
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
  - GeographyHiringPVO
  - geographyhiringpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GeographyHiringPVO

## 📌 Visão Geral

Extrai geografias vinculadas a hierarquias de contratação, com nós e elementos geográficos. Utilizado para definir regiões de recrutamento.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.GeographyHiringPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 116 | 2 | 2 | 22 | 19% |

---

## 🔗 Tabelas Relacionadas

- [[hz_geographies|HZ_GEOGRAPHIES]] — 106 atributos (1 PKs, 13 BICC)
- [[irc_geo_hier_nodes|IRC_GEO_HIER_NODES]] — 10 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[hz_geographies|HZ_GEOGRAPHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 34 | AttributeDate11 | ATTRIBUTE_DATE11 | — | — |
| 35 | AttributeDate12 | ATTRIBUTE_DATE12 | — | — |
| 36 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 37 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 38 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 39 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 40 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 41 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 42 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 43 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 44 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 45 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 46 | AttributeNumber11 | ATTRIBUTE_NUMBER11 | — | — |
| 47 | AttributeNumber12 | ATTRIBUTE_NUMBER12 | — | — |
| 48 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 49 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 50 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 51 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 52 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 53 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 54 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 55 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 56 | CountryCode | COUNTRY_CODE | — | ✅ |
| 57 | CreatedBy | CREATED_BY | — | — |
| 58 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 59 | CreationDate | CREATION_DATE | — | — |
| 60 | EndDate | END_DATE | — | — |
| 61 | GeocodeFlag | GEOCODE_FLAG | — | — |
| 62 | GeographyCode | GEOGRAPHY_CODE | — | ✅ |
| 63 | GeographyElement1 | GEOGRAPHY_ELEMENT1 | — | ✅ |
| 64 | GeographyElement10 | GEOGRAPHY_ELEMENT10 | — | — |
| 65 | GeographyElement10Id | GEOGRAPHY_ELEMENT10_ID | — | — |
| 66 | GeographyElement1Code | GEOGRAPHY_ELEMENT1_CODE | — | — |
| 67 | GeographyElement1Id | GEOGRAPHY_ELEMENT1_ID | — | — |
| 68 | GeographyElement2 | GEOGRAPHY_ELEMENT2 | — | ✅ |
| 69 | GeographyElement2Code | GEOGRAPHY_ELEMENT2_CODE | — | — |
| 70 | GeographyElement2Id | GEOGRAPHY_ELEMENT2_ID | — | — |
| 71 | GeographyElement3 | GEOGRAPHY_ELEMENT3 | — | ✅ |
| 72 | GeographyElement3Code | GEOGRAPHY_ELEMENT3_CODE | — | — |
| 73 | GeographyElement3Id | GEOGRAPHY_ELEMENT3_ID | — | — |
| 74 | GeographyElement4 | GEOGRAPHY_ELEMENT4 | — | — |
| 75 | GeographyElement4Code | GEOGRAPHY_ELEMENT4_CODE | — | — |
| 76 | GeographyElement4Id | GEOGRAPHY_ELEMENT4_ID | — | — |
| 77 | GeographyElement5 | GEOGRAPHY_ELEMENT5 | — | — |
| 78 | GeographyElement5Code | GEOGRAPHY_ELEMENT5_CODE | — | — |
| 79 | GeographyElement5Id | GEOGRAPHY_ELEMENT5_ID | — | — |
| 80 | GeographyElement6 | GEOGRAPHY_ELEMENT6 | — | — |
| 81 | GeographyElement6Id | GEOGRAPHY_ELEMENT6_ID | — | — |
| 82 | GeographyElement7 | GEOGRAPHY_ELEMENT7 | — | — |
| 83 | GeographyElement7Id | GEOGRAPHY_ELEMENT7_ID | — | — |
| 84 | GeographyElement8 | GEOGRAPHY_ELEMENT8 | — | — |
| 85 | GeographyElement8Id | GEOGRAPHY_ELEMENT8_ID | — | — |
| 86 | GeographyElement9 | GEOGRAPHY_ELEMENT9 | — | — |
| 87 | GeographyElement9Id | GEOGRAPHY_ELEMENT9_ID | — | — |
| 88 | GeographyId | GEOGRAPHY_ID | 🔑 | ✅ |
| 89 | GeographyName | GEOGRAPHY_NAME | — | ✅ |
| 90 | GeographyNumber | GEOGRAPHY_NUMBER | — | — |
| 91 | GeographyType | GEOGRAPHY_TYPE | — | ✅ |
| 92 | GeographyUse | GEOGRAPHY_USE | — | — |
| 93 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 94 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 95 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 96 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 97 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 98 | MultipleParentFlag | MULTIPLE_PARENT_FLAG | — | — |
| 99 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 100 | ParentGeographyHiringPEOGeographyCode | GEOGRAPHY_CODE | — | ✅ |
| 101 | ParentGeographyHiringPEOGeographyId | GEOGRAPHY_ID | — | ✅ |
| 102 | ParentGeographyHiringPEOGeographyName | GEOGRAPHY_NAME | — | ✅ |
| 103 | ParentGeographyHiringPEOGeographyType | GEOGRAPHY_TYPE | — | ✅ |
| 104 | RequestId | REQUEST_ID | — | — |
| 105 | StartDate | START_DATE | — | — |
| 106 | TimezoneCode | TIMEZONE_CODE | — | — |

### [[irc_geo_hier_nodes|IRC_GEO_HIER_NODES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GeographyNodeId | GEOGRAPHY_NODE_ID | 🔑 | ✅ |
| 2 | GeographyNodePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | GeographyNodePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | GeographyNodePEOGeographyId | GEOGRAPHY_ID | — | ✅ |
| 5 | GeographyNodePEOHierarchyId | HIERARCHY_ID | — | ✅ |
| 6 | GeographyNodePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | GeographyNodePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | GeographyNodePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | GeographyNodePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | GeographyNodePEOParentGeoNodeId | PARENT_GEO_NODE_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
