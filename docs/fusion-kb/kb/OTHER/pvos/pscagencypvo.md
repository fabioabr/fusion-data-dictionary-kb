---
id: DOC-OTHER-PVO-PSCAgencyPVO
doc_type: system-doc
title: "PSCAgencyPVO — PVO Cross-Module"
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
  - PSCAgencyPVO
  - pscagencypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PSCAgencyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de PSCAgency. Acessa as tabelas: PSC_COM_AGENCY_B, PSC_COM_AGENCY_TL.

**Caminho:** `FscmTopModelAM.PscPermitsReportingAM.PSCAgencyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 23 | 2 | 1 | 7 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[psc_com_agency_b|PSC_COM_AGENCY_B]] — 13 atributos (1 PKs, 6 BICC)
- [[psc_com_agency_tl|PSC_COM_AGENCY_TL]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[psc_com_agency_b|PSC_COM_AGENCY_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgencyPEOAgencyId | AGENCY_ID | 🔑 | ✅ |
| 2 | AgencyPEOAgencyName | AGENCY_NAME | — | ✅ |
| 3 | AgencyPEOAssignmentOption | ASSIGNMENT_OPTION | — | — |
| 4 | AgencyPEOCountryCode | COUNTRY_CODE | — | ✅ |
| 5 | AgencyPEOCreatedBy | CREATED_BY | — | — |
| 6 | AgencyPEOCreationDate | CREATION_DATE | — | — |
| 7 | AgencyPEOCurrencyCode | CURRENCY_CODE | — | ✅ |
| 8 | AgencyPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | AgencyPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | AgencyPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | AgencyPEOModuleId | MODULE_ID | — | — |
| 12 | AgencyPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | AgencyPEOTzname | TZNAME | — | ✅ |

### [[psc_com_agency_tl|PSC_COM_AGENCY_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgencyTLPEOAgencyId | AGENCY_ID | — | — |
| 2 | AgencyTLPEOCreatedBy | CREATED_BY | — | — |
| 3 | AgencyTLPEOCreationDate | CREATION_DATE | — | — |
| 4 | AgencyTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | AgencyTLPEOLanguage | LANGUAGE | — | — |
| 6 | AgencyTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | AgencyTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | AgencyTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | AgencyTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | AgencyTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
