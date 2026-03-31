---
id: DOC-HCM-PVO-HNSAirQualityEventPVO
doc_type: system-doc
title: "HNSAirQualityEventPVO — PVO Human Capital Management"
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
  - HNSAirQualityEventPVO
  - hnsairqualityeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSAirQualityEventPVO

## 📌 Visão Geral

Extrai eventos de qualidade do ar registrados em saúde e segurança do trabalho. Suporta monitoramento ambiental e compliance de SST.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSAirQualityEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 1 | 1 | 10 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[hns_air_quality_evt_detail|HNS_AIR_QUALITY_EVT_DETAIL]] — 61 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[hns_air_quality_evt_detail|HNS_AIR_QUALITY_EVT_DETAIL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSAirQualityEventPEOAirQualEvtDtlId | AIR_QUALITY_EVT_DETAIL_ID | 🔑 | ✅ |
| 2 | HNSAirQualityEventPEOAirQualTypeCd | AIR_QUALITY_TYPE_CODE | — | ✅ |
| 3 | HNSAirQualityEventPEOAttrCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | HNSAirQualityEventPEOAttrNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 5 | HNSAirQualityEventPEOAttrNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 6 | HNSAirQualityEventPEOAttrNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 7 | HNSAirQualityEventPEOAttrNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 8 | HNSAirQualityEventPEOAttrNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 9 | HNSAirQualityEventPEOAttrNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 10 | HNSAirQualityEventPEOAttrNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 11 | HNSAirQualityEventPEOAttrNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 12 | HNSAirQualityEventPEOAttrNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 13 | HNSAirQualityEventPEOAttrNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 14 | HNSAirQualityEventPEOAttrTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 15 | HNSAirQualityEventPEOAttrTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 16 | HNSAirQualityEventPEOAttrTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 17 | HNSAirQualityEventPEOAttrTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 18 | HNSAirQualityEventPEOAttrTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 19 | HNSAirQualityEventPEOAttrTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 20 | HNSAirQualityEventPEOAttrTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 21 | HNSAirQualityEventPEOAttrTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 22 | HNSAirQualityEventPEOAttrTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 23 | HNSAirQualityEventPEOAttrTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 24 | HNSAirQualityEventPEOAttribute1 | ATTRIBUTE1 | — | — |
| 25 | HNSAirQualityEventPEOAttribute10 | ATTRIBUTE10 | — | — |
| 26 | HNSAirQualityEventPEOAttribute11 | ATTRIBUTE11 | — | — |
| 27 | HNSAirQualityEventPEOAttribute12 | ATTRIBUTE12 | — | — |
| 28 | HNSAirQualityEventPEOAttribute13 | ATTRIBUTE13 | — | — |
| 29 | HNSAirQualityEventPEOAttribute14 | ATTRIBUTE14 | — | — |
| 30 | HNSAirQualityEventPEOAttribute15 | ATTRIBUTE15 | — | — |
| 31 | HNSAirQualityEventPEOAttribute16 | ATTRIBUTE16 | — | — |
| 32 | HNSAirQualityEventPEOAttribute17 | ATTRIBUTE17 | — | — |
| 33 | HNSAirQualityEventPEOAttribute18 | ATTRIBUTE18 | — | — |
| 34 | HNSAirQualityEventPEOAttribute19 | ATTRIBUTE19 | — | — |
| 35 | HNSAirQualityEventPEOAttribute2 | ATTRIBUTE2 | — | — |
| 36 | HNSAirQualityEventPEOAttribute20 | ATTRIBUTE20 | — | — |
| 37 | HNSAirQualityEventPEOAttribute21 | ATTRIBUTE21 | — | — |
| 38 | HNSAirQualityEventPEOAttribute22 | ATTRIBUTE22 | — | — |
| 39 | HNSAirQualityEventPEOAttribute23 | ATTRIBUTE23 | — | — |
| 40 | HNSAirQualityEventPEOAttribute24 | ATTRIBUTE24 | — | — |
| 41 | HNSAirQualityEventPEOAttribute25 | ATTRIBUTE25 | — | — |
| 42 | HNSAirQualityEventPEOAttribute26 | ATTRIBUTE26 | — | — |
| 43 | HNSAirQualityEventPEOAttribute27 | ATTRIBUTE27 | — | — |
| 44 | HNSAirQualityEventPEOAttribute28 | ATTRIBUTE28 | — | — |
| 45 | HNSAirQualityEventPEOAttribute29 | ATTRIBUTE29 | — | — |
| 46 | HNSAirQualityEventPEOAttribute3 | ATTRIBUTE3 | — | — |
| 47 | HNSAirQualityEventPEOAttribute30 | ATTRIBUTE30 | — | — |
| 48 | HNSAirQualityEventPEOAttribute4 | ATTRIBUTE4 | — | — |
| 49 | HNSAirQualityEventPEOAttribute5 | ATTRIBUTE5 | — | — |
| 50 | HNSAirQualityEventPEOAttribute6 | ATTRIBUTE6 | — | — |
| 51 | HNSAirQualityEventPEOAttribute7 | ATTRIBUTE7 | — | — |
| 52 | HNSAirQualityEventPEOAttribute8 | ATTRIBUTE8 | — | — |
| 53 | HNSAirQualityEventPEOAttribute9 | ATTRIBUTE9 | — | — |
| 54 | HNSAirQualityEventPEOCreatedBy | CREATED_BY | — | ✅ |
| 55 | HNSAirQualityEventPEOCreationDate | CREATION_DATE | — | ✅ |
| 56 | HNSAirQualityEventPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 57 | HNSAirQualityEventPEOIncDetailId | INCIDENT_DETAIL_ID | — | ✅ |
| 58 | HNSAirQualityEventPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 59 | HNSAirQualityEventPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 60 | HNSAirQualityEventPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 61 | HNSAirQualityEventPEOObjVerNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
