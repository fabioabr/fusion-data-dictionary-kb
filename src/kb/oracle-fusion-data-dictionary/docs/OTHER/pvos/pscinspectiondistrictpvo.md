---
id: DOC-OTHER-PVO-PSCInspectionDistrictPVO
doc_type: system-doc
title: "PSCInspectionDistrictPVO — PVO Cross-Module"
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
  - PSCInspectionDistrictPVO
  - pscinspectiondistrictpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCInspectionDistrictPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCInspection District. Acessa as tabelas: PSC_COM_DISTRICT_B, PSC_COM_DISTRICT_TL, PSC_COM_DISTRICT_TYPE_TL.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCInspectionDistrictPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 3 | 1 | 5 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_district_b|PSC_COM_DISTRICT_B]] — 9 atributos (1 PKs, 3 BICC)
- [[psc_com_district_tl|PSC_COM_DISTRICT_TL]] — 10 atributos (1 BICC)
- [[psc_com_district_type_tl|PSC_COM_DISTRICT_TYPE_TL]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_com_district_b|PSC_COM_DISTRICT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistirctPEOCreatedBy | CREATED_BY | — | — |
| 2 | DistirctPEOCreationDate | CREATION_DATE | — | — |
| 3 | DistirctPEODistrictId | DISTRICT_ID | 🔑 | ✅ |
| 4 | DistirctPEODistrictType | DISTRICT_TYPE | — | ✅ |
| 5 | DistirctPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DistirctPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | DistirctPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | DistirctPEOModuleId | MODULE_ID | — | — |
| 9 | DistirctPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[psc_com_district_tl|PSC_COM_DISTRICT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistrictTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | DistrictTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | DistrictTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | DistrictTLPEODistrictId | DISTRICT_ID | — | — |
| 5 | DistrictTLPEOLanguage | LANGUAGE | — | — |
| 6 | DistrictTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | DistrictTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DistrictTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DistrictTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DistrictTLPEOSourceLang | SOURCE_LANG | — | — |

### [[psc_com_district_type_tl|PSC_COM_DISTRICT_TYPE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DistrictTypeTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | DistrictTypeTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | DistrictTypeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | DistrictTypeTLPEODistrictType | DISTRICT_TYPE | — | — |
| 5 | DistrictTypeTLPEOLanguage | LANGUAGE | — | — |
| 6 | DistrictTypeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | DistrictTypeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DistrictTypeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DistrictTypeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DistrictTypeTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
