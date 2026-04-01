---
id: DOC-OTHER-PVO-PSCPropertyDistrictPVO
doc_type: system-doc
title: "PSCPropertyDistrictPVO — PVO Cross-Module"
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
  - PSCPropertyDistrictPVO
  - pscpropertydistrictpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyDistrictPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty District. Acessa as tabelas: PSC_COM_PARCEL_DISTRICT.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyDistrictPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 5 | 62% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_parcel_district|PSC_COM_PARCEL_DISTRICT]] — 8 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[psc_com_parcel_district|PSC_COM_PARCEL_DISTRICT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyParcelDistrictPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PropertyParcelDistrictPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PropertyParcelDistrictPEODistrictId | DISTRICT_ID | 🔑 | ✅ |
| 4 | PropertyParcelDistrictPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PropertyParcelDistrictPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | PropertyParcelDistrictPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | PropertyParcelDistrictPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | PropertyParcelDistrictPEOParcelId | PARCEL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
