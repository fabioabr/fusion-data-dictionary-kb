---
id: DOC-OTHER-PVO-CfdaExtractPVO
doc_type: system-doc
title: "CfdaExtractPVO — PVO Cross-Module"
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
  - CfdaExtractPVO
  - cfdaextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CfdaExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cfda Extract. Acessa as tabelas: GMS_CFDAS_B, GMS_CFDAS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.CfdaExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_cfdas_b|GMS_CFDAS_B]] — 9 atributos (1 PKs, 9 BICC)
- [[gms_cfdas_tl|GMS_CFDAS_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[gms_cfdas_b|GMS_CFDAS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CfdaBaseCfda | CFDA | 🔑 | ✅ |
| 2 | CfdaBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | CfdaBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | CfdaBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | CfdaBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | CfdaBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | CfdaBaseModifiedDate | MODIFIED_DATE | — | ✅ |
| 8 | CfdaBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | CfdaBasePublishedDate | PUBLISHED_DATE | — | ✅ |

### [[gms_cfdas_tl|GMS_CFDAS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CfdaTransLangAgency | AGENCY | — | ✅ |
| 2 | CfdaTransLangAssistanceType | ASSISTANCE_TYPE | — | ✅ |
| 3 | CfdaTransLangCfda | CFDA | — | ✅ |
| 4 | CfdaTransLangCreatedBy | CREATED_BY | — | ✅ |
| 5 | CfdaTransLangCreationDate | CREATION_DATE | — | ✅ |
| 6 | CfdaTransLangLanguage | LANGUAGE | — | ✅ |
| 7 | CfdaTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | CfdaTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | CfdaTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | CfdaTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | CfdaTransLangProgramTitle | PROGRAM_TITLE | — | ✅ |
| 12 | CfdaTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
