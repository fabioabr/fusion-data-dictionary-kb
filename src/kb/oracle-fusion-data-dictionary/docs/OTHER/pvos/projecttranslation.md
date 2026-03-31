---
id: DOC-OTHER-PVO-ProjectTranslation
doc_type: system-doc
title: "ProjectTranslation — PVO Cross-Module"
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
  - ProjectTranslation
  - projecttranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Project Translation. Acessa as tabelas: PJF_PROJECTS_ALL_TL.

**Caminho:** `FscmTopModelAM.PjfProjectAM.ProjectTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 9 | 75% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]] — 12 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_projects_all_tl|PJF_PROJECTS_ALL_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | ExecutionCustomerName | EXECUTION_CUSTOMER_NAME | — | — |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | Name | NAME | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ProjectId | PROJECT_ID | 🔑 | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
