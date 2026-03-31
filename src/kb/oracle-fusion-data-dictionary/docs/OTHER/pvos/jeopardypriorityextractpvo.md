---
id: DOC-OTHER-PVO-JeopardyPriorityExtractPVO
doc_type: system-doc
title: "JeopardyPriorityExtractPVO — PVO Cross-Module"
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
  - JeopardyPriorityExtractPVO
  - jeopardypriorityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JeopardyPriorityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Jeopardy Priority Extract. Acessa as tabelas: DOO_JEOPARDY_PRIORITIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.JeopardyPriorityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_jeopardy_priorities|DOO_JEOPARDY_PRIORITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | JeopardyPriorityCode | JEOPARDY_PRIORITY_CODE | — | ✅ |
| 4 | JeopardyPriorityId | JEOPARDY_PRIORITY_ID | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | MaximumScore | MAXIMUM_SCORE | — | ✅ |
| 9 | MinimumScore | MINIMUM_SCORE | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
