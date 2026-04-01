---
id: DOC-OTHER-PVO-PSCPropertyVlHistoryPVO
doc_type: system-doc
title: "PSCPropertyVlHistoryPVO — PVO Cross-Module"
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
  - PSCPropertyVlHistoryPVO
  - pscpropertyvlhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyVlHistoryPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty Vl History. Acessa as tabelas: PSC_COM_PARCEL_VALUE_F.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyVlHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 1 | 3 | 22 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_parcel_value_f|PSC_COM_PARCEL_VALUE_F]] — 23 atributos (3 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[psc_com_parcel_value_f|PSC_COM_PARCEL_VALUE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyValuePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PropertyValuePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PropertyValuePEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 4 | PropertyValuePEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | PropertyValuePEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | PropertyValuePEOFixtureExemption | FIXTURE_EXEMPTION | — | ✅ |
| 7 | PropertyValuePEOFixtures | FIXTURES | — | ✅ |
| 8 | PropertyValuePEOImprovementValue | IMPROVEMENT_VALUE | — | ✅ |
| 9 | PropertyValuePEOLandValue | LAND_VALUE | — | ✅ |
| 10 | PropertyValuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PropertyValuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PropertyValuePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PropertyValuePEONetAssessedValues | NET_ASSESSED_VALUES | — | ✅ |
| 14 | PropertyValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | PropertyValuePEOOtherExemption | OTHER_EXEMPTION | — | ✅ |
| 16 | PropertyValuePEOOwnerExemption | OWNER_EXEMPTION | — | ✅ |
| 17 | PropertyValuePEOParcelId | PARCEL_ID | 🔑 | ✅ |
| 18 | PropertyValuePEOParcelSize1 | PARCEL_SIZE1 | — | ✅ |
| 19 | PropertyValuePEOParcelSize1Uom | PARCEL_SIZE1_UOM | — | ✅ |
| 20 | PropertyValuePEOParcelSize2 | PARCEL_SIZE2 | — | ✅ |
| 21 | PropertyValuePEOParcelSize2Uom | PARCEL_SIZE2_UOM | — | ✅ |
| 22 | PropertyValuePEOPersonalPropertyValue | PERSONAL_PROPERTY_VALUE | — | ✅ |
| 23 | PropertyValuePEOPropertyUseCode | PROPERTY_USE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
