---
id: DOC-OTHER-PVO-BusinessUnitExtractPVO
doc_type: system-doc
title: "BusinessUnitExtractPVO — PVO Cross-Module"
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
  - BusinessUnitExtractPVO
  - businessunitextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BusinessUnitExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Business Unit Extract. Acessa as tabelas: FUN_BU_PERF_V.

**Caminho:** `FscmTopModelAM.FinExtractAM.FunBiccExtractAM.BusinessUnitExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FunBuPerfPEOBusinessUnitId | BU_ID | 🔑 | ✅ |
| 2 | FunBuPerfPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | FunBuPerfPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | FunBuPerfPEODateFrom | DATE_FROM | — | ✅ |
| 5 | FunBuPerfPEODateTo | DATE_TO | — | ✅ |
| 6 | FunBuPerfPEOEnterpriseId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | FunBuPerfPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | FunBuPerfPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | FunBuPerfPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | FunBuPerfPEOName | BU_NAME | — | ✅ |
| 11 | FunBuPerfPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
