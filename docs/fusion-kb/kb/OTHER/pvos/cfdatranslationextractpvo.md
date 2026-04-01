---
id: DOC-OTHER-PVO-CfdaTranslationExtractPVO
doc_type: system-doc
title: "CfdaTranslationExtractPVO — PVO Cross-Module"
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
  - CfdaTranslationExtractPVO
  - cfdatranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CfdaTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cfda Translation Extract. Acessa as tabelas: GMS_CFDAS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.CfdaTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_cfdas_tl|GMS_CFDAS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[gms_cfdas_tl|GMS_CFDAS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CfdaTranslationAgency | AGENCY | — | ✅ |
| 2 | CfdaTranslationAssistanceType | ASSISTANCE_TYPE | — | ✅ |
| 3 | CfdaTranslationCfda | CFDA | 🔑 | ✅ |
| 4 | CfdaTranslationCreatedBy | CREATED_BY | — | ✅ |
| 5 | CfdaTranslationCreationDate | CREATION_DATE | — | ✅ |
| 6 | CfdaTranslationLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | CfdaTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CfdaTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CfdaTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CfdaTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CfdaTranslationProgramTitle | PROGRAM_TITLE | — | ✅ |
| 12 | CfdaTranslationSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
