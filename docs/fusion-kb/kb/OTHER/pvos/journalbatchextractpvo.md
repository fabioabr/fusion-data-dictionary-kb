---
id: DOC-OTHER-PVO-JournalBatchExtractPVO
doc_type: system-doc
title: "JournalBatchExtractPVO — PVO Cross-Module"
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
  - JournalBatchExtractPVO
  - journalbatchextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# JournalBatchExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Journal Batch Extract. Acessa as tabelas: GL_JE_BATCHES.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.JournalBatchExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 1 | 1 | 33 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[gl_je_batches|GL_JE_BATCHES]] — 54 atributos (1 PKs, 33 BICC)

---

## ⚙️ Atributos

### [[gl_je_batches|GL_JE_BATCHES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | JournalBatchAccountedPeriodType | ACCOUNTED_PERIOD_TYPE | — | ✅ |
| 2 | JournalBatchActualFlag | ACTUAL_FLAG | — | ✅ |
| 3 | JournalBatchApprovalStatusCode | APPROVAL_STATUS_CODE | — | ✅ |
| 4 | JournalBatchApproverEmployeeId | APPROVER_EMPLOYEE_ID | — | ✅ |
| 5 | JournalBatchAttribute1 | ATTRIBUTE1 | — | — |
| 6 | JournalBatchAttribute10 | ATTRIBUTE10 | — | — |
| 7 | JournalBatchAttribute2 | ATTRIBUTE2 | — | — |
| 8 | JournalBatchAttribute3 | ATTRIBUTE3 | — | — |
| 9 | JournalBatchAttribute4 | ATTRIBUTE4 | — | — |
| 10 | JournalBatchAttribute5 | ATTRIBUTE5 | — | — |
| 11 | JournalBatchAttribute6 | ATTRIBUTE6 | — | — |
| 12 | JournalBatchAttribute7 | ATTRIBUTE7 | — | — |
| 13 | JournalBatchAttribute8 | ATTRIBUTE8 | — | — |
| 14 | JournalBatchAttribute9 | ATTRIBUTE9 | — | — |
| 15 | JournalBatchAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 16 | JournalBatchAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 17 | JournalBatchAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 18 | JournalBatchAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 19 | JournalBatchAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 20 | JournalBatchAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 21 | JournalBatchAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 22 | JournalBatchAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 23 | JournalBatchAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 24 | JournalBatchAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 25 | JournalBatchAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 26 | JournalBatchAverageJournalFlag | AVERAGE_JOURNAL_FLAG | — | ✅ |
| 27 | JournalBatchChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 28 | JournalBatchControlTotal | CONTROL_TOTAL | — | ✅ |
| 29 | JournalBatchCreatedBy | CREATED_BY | — | ✅ |
| 30 | JournalBatchCreationDate | CREATION_DATE | — | ✅ |
| 31 | JournalBatchDateCreated | DATE_CREATED | — | ✅ |
| 32 | JournalBatchDefaultEffectiveDate | DEFAULT_EFFECTIVE_DATE | — | ✅ |
| 33 | JournalBatchDefaultPeriodName | DEFAULT_PERIOD_NAME | — | ✅ |
| 34 | JournalBatchDescription | DESCRIPTION | — | ✅ |
| 35 | JournalBatchErrorMessage | ERROR_MESSAGE | — | ✅ |
| 36 | JournalBatchFundsStatusCode | FUNDS_STATUS_CODE | — | ✅ |
| 37 | JournalBatchGroupId | GROUP_ID | — | ✅ |
| 38 | JournalBatchJeBatchId | JE_BATCH_ID | 🔑 | ✅ |
| 39 | JournalBatchJeSource | JE_SOURCE | — | ✅ |
| 40 | JournalBatchLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 41 | JournalBatchLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 42 | JournalBatchLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 43 | JournalBatchName | NAME | — | ✅ |
| 44 | JournalBatchObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 45 | JournalBatchParentJeBatchId | PARENT_JE_BATCH_ID | — | ✅ |
| 46 | JournalBatchPeriodSetName | PERIOD_SET_NAME | — | ✅ |
| 47 | JournalBatchPostedDate | POSTED_DATE | — | ✅ |
| 48 | JournalBatchPostingRunId | POSTING_RUN_ID | — | ✅ |
| 49 | JournalBatchRequestId | REQUEST_ID | — | ✅ |
| 50 | JournalBatchRunningTotalAccountedCr | RUNNING_TOTAL_ACCOUNTED_CR | — | ✅ |
| 51 | JournalBatchRunningTotalAccountedDr | RUNNING_TOTAL_ACCOUNTED_DR | — | ✅ |
| 52 | JournalBatchRunningTotalCr | RUNNING_TOTAL_CR | — | ✅ |
| 53 | JournalBatchRunningTotalDr | RUNNING_TOTAL_DR | — | ✅ |
| 54 | JournalBatchStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
