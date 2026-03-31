---
id: DOC-OTHER-PVO-ProjectStatusTranslation
doc_type: system-doc
title: "ProjectStatusTranslation — PVO Cross-Module"
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
  - ProjectStatusTranslation
  - projectstatustranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectStatusTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Project Status Translation. Acessa as tabelas: PJF_PROJECT_STATUSES_TL.

**Caminho:** `FscmTopModelAM.PjfSetupStatusesAnalyticsAM.ProjectStatusTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[pjf_project_statuses_tl|PJF_PROJECT_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ProjectStatusCode | PROJECT_STATUS_CODE | 🔑 | ✅ |
| 10 | ProjectStatusName | PROJECT_STATUS_NAME | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
