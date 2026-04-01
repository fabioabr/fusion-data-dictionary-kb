---
id: DOC-OTHER-PVO-ProjectSetLineExtractPVO
doc_type: system-doc
title: "ProjectSetLineExtractPVO — PVO Cross-Module"
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
  - ProjectSetLineExtractPVO
  - projectsetlineextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectSetLineExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Set Line Extract. Acessa as tabelas: PJF_PROJECT_SET_LINES.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectSetLineExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_project_set_lines|PJF_PROJECT_SET_LINES]] — 8 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[pjf_project_set_lines|PJF_PROJECT_SET_LINES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectSetLinePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectSetLinePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectSetLinePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProjectSetLinePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | ProjectSetLinePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ProjectSetLinePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProjectSetLinePEOProjectId | PROJECT_ID | 🔑 | ✅ |
| 8 | ProjectSetLinePEOProjectSetId | PROJECT_SET_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
