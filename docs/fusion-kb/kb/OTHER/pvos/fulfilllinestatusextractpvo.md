---
id: DOC-OTHER-PVO-FulfillLineStatusExtractPVO
doc_type: system-doc
title: "FulfillLineStatusExtractPVO — PVO Cross-Module"
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
  - FulfillLineStatusExtractPVO
  - fulfilllinestatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FulfillLineStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fulfill Line Status Extract. Acessa as tabelas: DOO_LINE_STATUSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.FulfillLineStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_line_statuses|DOO_LINE_STATUSES]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[doo_line_statuses|DOO_LINE_STATUSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FulfilmentLineStatusCreatedBy | CREATED_BY | — | ✅ |
| 2 | FulfilmentLineStatusCreationDate | CREATION_DATE | — | ✅ |
| 3 | FulfilmentLineStatusDefaultFlag | DEFAULT_FLAG | — | ✅ |
| 4 | FulfilmentLineStatusLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | FulfilmentLineStatusLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | FulfilmentLineStatusLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | FulfilmentLineStatusLineStatusId | LINE_STATUS_ID | 🔑 | ✅ |
| 8 | FulfilmentLineStatusObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | FulfilmentLineStatusOrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 10 | FulfilmentLineStatusStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
