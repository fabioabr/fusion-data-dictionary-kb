---
id: DOC-OTHER-PVO-ApplicationsPVO
doc_type: system-doc
title: "ApplicationsPVO — PVO Cross-Module"
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
  - ApplicationsPVO
  - applicationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplicationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Applications. Acessa as tabelas: FND_APPLICATION, FND_APPLICATION_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.ApplicationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_application|FND_APPLICATION]] — 10 atributos (10 BICC)
- [[fnd_application_tl|FND_APPLICATION_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_application|FND_APPLICATION]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId1 | APPLICATION_ID | — | ✅ |
| 2 | ApplicationShortName | APPLICATION_SHORT_NAME | — | ✅ |
| 3 | Basepath | BASEPATH | — | ✅ |
| 4 | CreatedBy1 | CREATED_BY | — | ✅ |
| 5 | CreationDate1 | CREATION_DATE | — | ✅ |
| 6 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 9 | ModuleId1 | MODULE_ID | — | ✅ |
| 10 | ProductCode | PRODUCT_CODE | — | ✅ |

### [[fnd_application_tl|FND_APPLICATION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | ApplicationName | APPLICATION_NAME | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ModuleId | MODULE_ID | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
