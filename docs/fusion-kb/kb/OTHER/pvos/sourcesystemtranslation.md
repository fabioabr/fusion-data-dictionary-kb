---
id: DOC-OTHER-PVO-SourceSystemTranslation
doc_type: system-doc
title: "SourceSystemTranslation — PVO Cross-Module"
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
  - SourceSystemTranslation
  - sourcesystemtranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SourceSystemTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Source System Translation. Acessa as tabelas: HZ_ORIG_SYSTEMS_TL.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.SourceSystemTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 3 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hz_orig_systems_tl|HZ_ORIG_SYSTEMS_TL]] — 11 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hz_orig_systems_tl|HZ_ORIG_SYSTEMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | — |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | OrigSystemId | ORIG_SYSTEM_ID | 🔑 | ✅ |
| 10 | OrigSystemName | ORIG_SYSTEM_NAME | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
