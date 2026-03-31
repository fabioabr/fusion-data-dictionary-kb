---
id: DOC-HCM-PVO-EstablishmentPVO
doc_type: system-doc
title: "EstablishmentPVO — PVO Human Capital Management"
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
  - EstablishmentPVO
  - establishmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EstablishmentPVO

## 📌 Visão Geral

Disponibiliza o cadastro de estabelecimentos (filiais, unidades) com localização e país. Utilizado em compliance trabalhista e relatórios por unidade operacional.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileCoreAM.EstablishmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 2 | 8 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]] — 9 atributos (2 PKs, 5 BICC)
- [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]] — 9 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_establishments_b|HRT_ESTABLISHMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EstablishmentBPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | EstablishmentBPEOCountryId | COUNTRY_ID | — | ✅ |
| 3 | EstablishmentBPEOEstablishmentId | ESTABLISHMENT_ID | 🔑 | ✅ |
| 4 | EstablishmentBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | EstablishmentBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | EstablishmentBPEOPartyId | PARTY_ID | — | — |
| 7 | EstablishmentBPEOSchoolCode | SCHOOL_CODE | — | — |
| 8 | EstablishmentBPEOStateProvinceId | STATE_PROVINCE_ID | — | ✅ |
| 9 | EstablishmentId | ESTABLISHMENT_ID | 🔑 | ✅ |

### [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EstablishmentTranslationPEOBusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 2 | EstablishmentTranslationPEODescription | DESCRIPTION | — | — |
| 3 | EstablishmentTranslationPEOEstablishmentId | ESTABLISHMENT_ID | — | — |
| 4 | EstablishmentTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | EstablishmentTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EstablishmentTranslationPEOLocation | LOCATION | — | — |
| 7 | EstablishmentTranslationPEOName | NAME | — | ✅ |
| 8 | EstablishmentTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | EstablishmentTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
