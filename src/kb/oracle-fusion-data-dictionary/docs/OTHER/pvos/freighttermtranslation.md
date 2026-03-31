---
id: DOC-OTHER-PVO-FreightTermTranslation
doc_type: system-doc
title: "FreightTermTranslation — PVO Cross-Module"
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
  - FreightTermTranslation
  - freighttermtranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FreightTermTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Freight Term Translation. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_TL.

**Caminho:** `FscmTopModelAM.DooTopAM.FreightTermTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 3 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]] — 12 atributos (3 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_tl|MSC_SR_LOOKUP_VALUES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 9 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 10 | Meaning | MEANING | — | ✅ |
| 11 | RefreshNumber | REFRESH_NUMBER | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
