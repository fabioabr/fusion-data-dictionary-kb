---
id: DOC-OTHER-PVO-CareerSiteLanguagePVO
doc_type: system-doc
title: "CareerSiteLanguagePVO — PVO Cross-Module"
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
  - CareerSiteLanguagePVO
  - careersitelanguagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CareerSiteLanguagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Career Site Language. Acessa as tabelas: IRC_CX_SITE_LANGS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidateExpSetupAM.CareerSiteLanguagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 2 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[irc_cx_site_langs|IRC_CX_SITE_LANGS]] — 8 atributos (2 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[irc_cx_site_langs|IRC_CX_SITE_LANGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | SiteId | SITE_ID | 🔑 | ✅ |
| 8 | SiteLanguage | SITE_LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
