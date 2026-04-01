---
id: DOC-OTHER-PVO-TierTranslation
doc_type: system-doc
title: "TierTranslation — PVO Cross-Module"
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
  - TierTranslation
  - tiertranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TierTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Tier Translation. Acessa as tabelas: ZPM_TIER_TL.

**Caminho:** `FscmTopModelAM.PartnerProgramAnalyticsAM.TierTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 7 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[zpm_tier_tl|ZPM_TIER_TL]] — 11 atributos (2 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[zpm_tier_tl|ZPM_TIER_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | Name | NAME | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | 🔑 | ✅ |
| 11 | TierId | TIER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
