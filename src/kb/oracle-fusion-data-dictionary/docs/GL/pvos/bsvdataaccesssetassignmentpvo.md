---
id: DOC-GL-PVO-BsvDataAccessSetAssignmentPVO
doc_type: system-doc
title: "BsvDataAccessSetAssignmentPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BsvDataAccessSetAssignmentPVO
  - bsvdataaccesssetassignmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BsvDataAccessSetAssignmentPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bsv Data Access Set Assignment. Acessa as tabelas: GL_ACCESS_SETS, GL_ACCESS_SET_ASSIGNMENTS.

**Caminho:** `FscmTopModelAM.FinGlSharedSetupDASAM.BsvDataAccessSetAssignmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 2 | 3 | 5 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[gl_access_sets|GL_ACCESS_SETS]] — 17 atributos (1 BICC)
- [[gl_access_set_assignments|GL_ACCESS_SET_ASSIGNMENTS]] — 13 atributos (3 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[gl_access_sets|GL_ACCESS_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DataAccessSetAccessSetId | ACCESS_SET_ID | — | — |
| 2 | DataAccessSetAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | — |
| 3 | DataAccessSetAutomaticallyCreatedFlag | AUTOMATICALLY_CREATED_FLAG | — | — |
| 4 | DataAccessSetChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 5 | DataAccessSetCreatedBy | CREATED_BY | — | — |
| 6 | DataAccessSetCreationDate | CREATION_DATE | — | — |
| 7 | DataAccessSetDefaultLedgerId | DEFAULT_LEDGER_ID | — | — |
| 8 | DataAccessSetDescription | DESCRIPTION | — | — |
| 9 | DataAccessSetEnabledFlag | ENABLED_FLAG | — | — |
| 10 | DataAccessSetLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | DataAccessSetLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | DataAccessSetLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | DataAccessSetName | NAME | — | — |
| 14 | DataAccessSetObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DataAccessSetPeriodSetName | PERIOD_SET_NAME | — | — |
| 16 | DataAccessSetSecuredSegValueSetId | SECURED_SEG_VALUE_SET_ID | — | — |
| 17 | DataAccessSetSecuritySegmentCode | SECURITY_SEGMENT_CODE | — | — |

### [[gl_access_set_assignments|GL_ACCESS_SET_ASSIGNMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AccessSetId | ACCESS_SET_ID | 🔑 | ✅ |
| 2 | DasAssignmentAccessPrivilegeCode | ACCESS_PRIVILEGE_CODE | — | — |
| 3 | DasAssignmentCreatedBy | CREATED_BY | — | — |
| 4 | DasAssignmentCreationDate | CREATION_DATE | — | — |
| 5 | DasAssignmentEndDate | END_DATE | — | — |
| 6 | DasAssignmentLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | DasAssignmentLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | DasAssignmentLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | DasAssignmentObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | DasAssignmentParentRecordId | PARENT_RECORD_ID | — | — |
| 11 | DasAssignmentStartDate | START_DATE | — | — |
| 12 | LedgerId | LEDGER_ID | 🔑 | ✅ |
| 13 | SegmentValue | SEGMENT_VALUE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
