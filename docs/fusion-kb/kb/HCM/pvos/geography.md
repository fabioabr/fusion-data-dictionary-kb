---
id: DOC-HCM-PVO-Geography
doc_type: system-doc
title: "Geography — PVO Human Capital Management"
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
  - Geography
  - geography
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Geography

## 📌 Visão Geral

Disponibiliza o cadastro de geografias (países, estados, cidades) com hierarquia. Tabela de referência para endereçamento e localização no HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GeographiesAnalyticsAM.Geography`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 1 | 3 | 7% |

---

## 🔗 Tabelas Relacionadas

- [[hz_geographies|HZ_GEOGRAPHIES]] — 45 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_geographies|HZ_GEOGRAPHIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CountryCode | COUNTRY_CODE | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreatedByModule | CREATED_BY_MODULE | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | EndDate | END_DATE | — | — |
| 6 | GeographyCode | GEOGRAPHY_CODE | — | — |
| 7 | GeographyElement1 | GEOGRAPHY_ELEMENT1 | — | — |
| 8 | GeographyElement10 | GEOGRAPHY_ELEMENT10 | — | — |
| 9 | GeographyElement10Id | GEOGRAPHY_ELEMENT10_ID | — | — |
| 10 | GeographyElement1Code | GEOGRAPHY_ELEMENT1_CODE | — | — |
| 11 | GeographyElement1Id | GEOGRAPHY_ELEMENT1_ID | — | — |
| 12 | GeographyElement2 | GEOGRAPHY_ELEMENT2 | — | — |
| 13 | GeographyElement2Code | GEOGRAPHY_ELEMENT2_CODE | — | — |
| 14 | GeographyElement2Id | GEOGRAPHY_ELEMENT2_ID | — | — |
| 15 | GeographyElement3 | GEOGRAPHY_ELEMENT3 | — | — |
| 16 | GeographyElement3Code | GEOGRAPHY_ELEMENT3_CODE | — | — |
| 17 | GeographyElement3Id | GEOGRAPHY_ELEMENT3_ID | — | — |
| 18 | GeographyElement4 | GEOGRAPHY_ELEMENT4 | — | — |
| 19 | GeographyElement4Code | GEOGRAPHY_ELEMENT4_CODE | — | — |
| 20 | GeographyElement4Id | GEOGRAPHY_ELEMENT4_ID | — | — |
| 21 | GeographyElement5 | GEOGRAPHY_ELEMENT5 | — | — |
| 22 | GeographyElement5Code | GEOGRAPHY_ELEMENT5_CODE | — | — |
| 23 | GeographyElement5Id | GEOGRAPHY_ELEMENT5_ID | — | — |
| 24 | GeographyElement6 | GEOGRAPHY_ELEMENT6 | — | — |
| 25 | GeographyElement6Id | GEOGRAPHY_ELEMENT6_ID | — | — |
| 26 | GeographyElement7 | GEOGRAPHY_ELEMENT7 | — | — |
| 27 | GeographyElement7Id | GEOGRAPHY_ELEMENT7_ID | — | — |
| 28 | GeographyElement8 | GEOGRAPHY_ELEMENT8 | — | — |
| 29 | GeographyElement8Id | GEOGRAPHY_ELEMENT8_ID | — | — |
| 30 | GeographyElement9 | GEOGRAPHY_ELEMENT9 | — | — |
| 31 | GeographyElement9Id | GEOGRAPHY_ELEMENT9_ID | — | — |
| 32 | GeographyId | GEOGRAPHY_ID | 🔑 | ✅ |
| 33 | GeographyName | GEOGRAPHY_NAME | — | ✅ |
| 34 | GeographyType | GEOGRAPHY_TYPE | — | — |
| 35 | GeographyUse | GEOGRAPHY_USE | — | — |
| 36 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 37 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 38 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 39 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 40 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 41 | MultipleParentFlag | MULTIPLE_PARENT_FLAG | — | — |
| 42 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | RequestId | REQUEST_ID | — | — |
| 44 | StartDate | START_DATE | — | — |
| 45 | TimezoneCode | TIMEZONE_CODE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
