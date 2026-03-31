---
id: DOC-HCM-PVO-EstablishmentTranslationPVO
doc_type: system-doc
title: "EstablishmentTranslationPVO — PVO Human Capital Management"
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
  - EstablishmentTranslationPVO
  - establishmenttranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EstablishmentTranslationPVO

## 📌 Visão Geral

Extrai traduções dos nomes de estabelecimentos por idioma. Suporta relatórios multilíngues e exibição localizada de filiais e unidades.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmProfileCoreAM.EstablishmentTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[hrt_establishments_tl|HRT_ESTABLISHMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EstablishmentId | ESTABLISHMENT_ID | 🔑 | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | Location | LOCATION | — | ✅ |
| 11 | Name | NAME | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
