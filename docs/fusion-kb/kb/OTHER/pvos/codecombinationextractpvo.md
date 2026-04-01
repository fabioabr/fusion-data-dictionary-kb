---
id: DOC-OTHER-PVO-CodeCombinationExtractPVO
doc_type: system-doc
title: "CodeCombinationExtractPVO — PVO Cross-Module"
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
  - CodeCombinationExtractPVO
  - codecombinationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CodeCombinationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Code Combination Extract. Acessa as tabelas: GL_CODE_COMBINATIONS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.CodeCombinationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 60 | 1 | 1 | 49 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[gl_code_combinations|GL_CODE_COMBINATIONS]] — 60 atributos (1 PKs, 49 BICC)

---

## ⚙️ Atributos

### [[gl_code_combinations|GL_CODE_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeCombinationAccountType | ACCOUNT_TYPE | — | ✅ |
| 2 | CodeCombinationAlternateCodeCombinationId | ALTERNATE_CODE_COMBINATION_ID | — | ✅ |
| 3 | CodeCombinationAttribute1 | ATTRIBUTE1 | — | — |
| 4 | CodeCombinationAttribute10 | ATTRIBUTE10 | — | — |
| 5 | CodeCombinationAttribute2 | ATTRIBUTE2 | — | — |
| 6 | CodeCombinationAttribute3 | ATTRIBUTE3 | — | — |
| 7 | CodeCombinationAttribute4 | ATTRIBUTE4 | — | — |
| 8 | CodeCombinationAttribute5 | ATTRIBUTE5 | — | — |
| 9 | CodeCombinationAttribute6 | ATTRIBUTE6 | — | — |
| 10 | CodeCombinationAttribute7 | ATTRIBUTE7 | — | — |
| 11 | CodeCombinationAttribute8 | ATTRIBUTE8 | — | — |
| 12 | CodeCombinationAttribute9 | ATTRIBUTE9 | — | — |
| 13 | CodeCombinationAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 14 | CodeCombinationChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 15 | CodeCombinationCodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 16 | CodeCombinationCreatedBy | CREATED_BY | — | ✅ |
| 17 | CodeCombinationCreationDate | CREATION_DATE | — | ✅ |
| 18 | CodeCombinationDetailBudgetingAllowedFlag | DETAIL_BUDGETING_ALLOWED_FLAG | — | ✅ |
| 19 | CodeCombinationDetailPostingAllowedFlag | DETAIL_POSTING_ALLOWED_FLAG | — | ✅ |
| 20 | CodeCombinationEnabledFlag | ENABLED_FLAG | — | ✅ |
| 21 | CodeCombinationEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 22 | CodeCombinationFinancialCategory | FINANCIAL_CATEGORY | — | ✅ |
| 23 | CodeCombinationJgzzReconFlag | JGZZ_RECON_FLAG | — | ✅ |
| 24 | CodeCombinationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | CodeCombinationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | CodeCombinationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | CodeCombinationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | CodeCombinationPreserveFlag | PRESERVE_FLAG | — | ✅ |
| 29 | CodeCombinationSegment1 | SEGMENT1 | — | ✅ |
| 30 | CodeCombinationSegment10 | SEGMENT10 | — | ✅ |
| 31 | CodeCombinationSegment11 | SEGMENT11 | — | ✅ |
| 32 | CodeCombinationSegment12 | SEGMENT12 | — | ✅ |
| 33 | CodeCombinationSegment13 | SEGMENT13 | — | ✅ |
| 34 | CodeCombinationSegment14 | SEGMENT14 | — | ✅ |
| 35 | CodeCombinationSegment15 | SEGMENT15 | — | ✅ |
| 36 | CodeCombinationSegment16 | SEGMENT16 | — | ✅ |
| 37 | CodeCombinationSegment17 | SEGMENT17 | — | ✅ |
| 38 | CodeCombinationSegment18 | SEGMENT18 | — | ✅ |
| 39 | CodeCombinationSegment19 | SEGMENT19 | — | ✅ |
| 40 | CodeCombinationSegment2 | SEGMENT2 | — | ✅ |
| 41 | CodeCombinationSegment20 | SEGMENT20 | — | ✅ |
| 42 | CodeCombinationSegment21 | SEGMENT21 | — | ✅ |
| 43 | CodeCombinationSegment22 | SEGMENT22 | — | ✅ |
| 44 | CodeCombinationSegment23 | SEGMENT23 | — | ✅ |
| 45 | CodeCombinationSegment24 | SEGMENT24 | — | ✅ |
| 46 | CodeCombinationSegment25 | SEGMENT25 | — | ✅ |
| 47 | CodeCombinationSegment26 | SEGMENT26 | — | ✅ |
| 48 | CodeCombinationSegment27 | SEGMENT27 | — | ✅ |
| 49 | CodeCombinationSegment28 | SEGMENT28 | — | ✅ |
| 50 | CodeCombinationSegment29 | SEGMENT29 | — | ✅ |
| 51 | CodeCombinationSegment3 | SEGMENT3 | — | ✅ |
| 52 | CodeCombinationSegment30 | SEGMENT30 | — | ✅ |
| 53 | CodeCombinationSegment4 | SEGMENT4 | — | ✅ |
| 54 | CodeCombinationSegment5 | SEGMENT5 | — | ✅ |
| 55 | CodeCombinationSegment6 | SEGMENT6 | — | ✅ |
| 56 | CodeCombinationSegment7 | SEGMENT7 | — | ✅ |
| 57 | CodeCombinationSegment8 | SEGMENT8 | — | ✅ |
| 58 | CodeCombinationSegment9 | SEGMENT9 | — | ✅ |
| 59 | CodeCombinationStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 60 | CodeCombinationSummaryFlag | SUMMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
