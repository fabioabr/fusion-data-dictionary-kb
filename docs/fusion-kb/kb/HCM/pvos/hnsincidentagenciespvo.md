---
id: DOC-HCM-PVO-HNSIncidentAgenciesPVO
doc_type: system-doc
title: "HNSIncidentAgenciesPVO — PVO Human Capital Management"
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
  - HNSIncidentAgenciesPVO
  - hnsincidentagenciespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSIncidentAgenciesPVO

## 📌 Visão Geral

Extrai agências reguladoras vinculadas a incidentes de SST, com flag de presença no local. Suporta compliance com órgãos fiscalizadores.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSIncidentAgenciesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hns_incident_agencies_dtl|HNS_INCIDENT_AGENCIES_DTL]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[hns_incident_agencies_dtl|HNS_INCIDENT_AGENCIES_DTL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSIncidentAgenciesPEOAttendedSiteFlag | ATTENDED_SITE_FLAG | — | ✅ |
| 2 | HNSIncidentAgenciesPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | HNSIncidentAgenciesPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | HNSIncidentAgenciesPEODateNotified | DATE_NOTIFIED | — | ✅ |
| 5 | HNSIncidentAgenciesPEODateSiteAttended | DATE_SITE_ATTENDED | — | ✅ |
| 6 | HNSIncidentAgenciesPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 7 | HNSIncidentAgenciesPEOIncidentAgencyId | INCIDENT_AGENCY_ID | 🔑 | ✅ |
| 8 | HNSIncidentAgenciesPEOIncidentId | INCIDENT_ID | — | ✅ |
| 9 | HNSIncidentAgenciesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | HNSIncidentAgenciesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | HNSIncidentAgenciesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | HNSIncidentAgenciesPEONotifiedAgencyCode | NOTIFIED_AGENCY_CODE | — | ✅ |
| 13 | HNSIncidentAgenciesPEONotifiedBy | NOTIFIED_BY | — | ✅ |
| 14 | HNSIncidentAgenciesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
