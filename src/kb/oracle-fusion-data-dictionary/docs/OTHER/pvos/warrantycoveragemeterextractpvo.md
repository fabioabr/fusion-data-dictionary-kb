---
id: DOC-OTHER-PVO-WarrantyCoverageMeterExtractPVO
doc_type: system-doc
title: "WarrantyCoverageMeterExtractPVO — PVO Cross-Module"
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
  - WarrantyCoverageMeterExtractPVO
  - warrantycoveragemeterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WarrantyCoverageMeterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Warranty Coverage Meter Extract. Acessa as tabelas: CSE_W_COVERAGE_METERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.WarrantyCoverageMeterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_w_coverage_meters|CSE_W_COVERAGE_METERS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cse_w_coverage_meters|CSE_W_COVERAGE_METERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CoverageId | COVERAGE_ID | — | ✅ |
| 3 | CoverageMeterId | COVERAGE_METER_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 12 | MeterIntervalValue | METER_INTERVAL_VALUE | — | ✅ |
| 13 | MeterStartValue | METER_START_VALUE | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
