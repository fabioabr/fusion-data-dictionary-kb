---
id: DOC-OTHER-PVO-PSCPropertyDistrictTypePVO
doc_type: system-doc
title: "PSCPropertyDistrictTypePVO — PVO Cross-Module"
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
  - PSCPropertyDistrictTypePVO
  - pscpropertydistricttypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCPropertyDistrictTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCProperty District Type. Acessa as tabelas: PSC_COM_DISTRICT_B, PSC_COM_DISTRICT_TYPE_B.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCPropertyDistrictTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 1 | 5 | 26% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_district_b|PSC_COM_DISTRICT_B]] — 9 atributos (1 PKs, 1 BICC)
- [[psc_com_district_type_b|PSC_COM_DISTRICT_TYPE_B]] — 10 atributos (4 BICC)

---

## ⚙️ Atributos

### [[psc_com_district_b|PSC_COM_DISTRICT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyDistrictPEOCreatedBy | CREATED_BY | — | — |
| 2 | PropertyDistrictPEOCreationDate | CREATION_DATE | — | — |
| 3 | PropertyDistrictPEODistrictId | DISTRICT_ID | 🔑 | ✅ |
| 4 | PropertyDistrictPEODistrictType | DISTRICT_TYPE | — | — |
| 5 | PropertyDistrictPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | PropertyDistrictPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | PropertyDistrictPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | PropertyDistrictPEOModuleId | MODULE_ID | — | — |
| 9 | PropertyDistrictPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[psc_com_district_type_b|PSC_COM_DISTRICT_TYPE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PropertyDistrictTypePEOCreatedBy | CREATED_BY | — | — |
| 2 | PropertyDistrictTypePEOCreationDate | CREATION_DATE | — | — |
| 3 | PropertyDistrictTypePEODistrictCategory | DISTRICT_CATEGORY | — | ✅ |
| 4 | PropertyDistrictTypePEODistrictType | DISTRICT_TYPE | — | ✅ |
| 5 | PropertyDistrictTypePEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 6 | PropertyDistrictTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PropertyDistrictTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | PropertyDistrictTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | PropertyDistrictTypePEOModuleId | MODULE_ID | — | — |
| 10 | PropertyDistrictTypePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
