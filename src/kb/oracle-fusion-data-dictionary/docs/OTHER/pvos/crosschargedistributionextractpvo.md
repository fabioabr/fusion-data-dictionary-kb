---
id: DOC-OTHER-PVO-CrossChargeDistributionExtractPVO
doc_type: system-doc
title: "CrossChargeDistributionExtractPVO — PVO Cross-Module"
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
  - CrossChargeDistributionExtractPVO
  - crosschargedistributionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CrossChargeDistributionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cross Charge Distribution Extract. Acessa as tabelas: PJC_CC_DIST_LINES_ALL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.CrossChargeDistributionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 1 | 59 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_cc_dist_lines_all|PJC_CC_DIST_LINES_ALL]] — 59 atributos (1 PKs, 59 BICC)

---

## ⚙️ Atributos

### [[pjc_cc_dist_lines_all|PJC_CC_DIST_LINES_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcCCDistLinesAllAccountingStatusCode | ACCOUNTING_STATUS_CODE | — | ✅ |
| 2 | PjcCCDistLinesAllAcctCurrencyCode | ACCT_CURRENCY_CODE | — | ✅ |
| 3 | PjcCCDistLinesAllAcctEventId | ACCT_EVENT_ID | — | ✅ |
| 4 | PjcCCDistLinesAllAcctSourceCode | ACCT_SOURCE_CODE | — | ✅ |
| 5 | PjcCCDistLinesAllAcctTpExchangeRate | ACCT_TP_EXCHANGE_RATE | — | ✅ |
| 6 | PjcCCDistLinesAllAcctTpRateDate | ACCT_TP_RATE_DATE | — | ✅ |
| 7 | PjcCCDistLinesAllAcctTpRateType | ACCT_TP_RATE_TYPE | — | ✅ |
| 8 | PjcCCDistLinesAllAmount | AMOUNT | — | ✅ |
| 9 | PjcCCDistLinesAllBillMarkupPercentage | BILL_MARKUP_PERCENTAGE | — | ✅ |
| 10 | PjcCCDistLinesAllBillRate | BILL_RATE | — | ✅ |
| 11 | PjcCCDistLinesAllCcDistLineId | CC_DIST_LINE_ID | 🔑 | ✅ |
| 12 | PjcCCDistLinesAllCreatedBy | CREATED_BY | — | ✅ |
| 13 | PjcCCDistLinesAllCreationDate | CREATION_DATE | — | ✅ |
| 14 | PjcCCDistLinesAllCrossChargeCode | CROSS_CHARGE_CODE | — | ✅ |
| 15 | PjcCCDistLinesAllDenomTpCurrencyCode | DENOM_TP_CURRENCY_CODE | — | ✅ |
| 16 | PjcCCDistLinesAllDenomTransferPrice | DENOM_TRANSFER_PRICE | — | ✅ |
| 17 | PjcCCDistLinesAllDistLineIdReversed | DIST_LINE_ID_REVERSED | — | ✅ |
| 18 | PjcCCDistLinesAllExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 19 | PjcCCDistLinesAllGlDate | GL_DATE | — | ✅ |
| 20 | PjcCCDistLinesAllGlPeriodName | GL_PERIOD_NAME | — | ✅ |
| 21 | PjcCCDistLinesAllIndCompiledSetId | IND_COMPILED_SET_ID | — | ✅ |
| 22 | PjcCCDistLinesAllJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 23 | PjcCCDistLinesAllJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 24 | PjcCCDistLinesAllLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | PjcCCDistLinesAllLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | PjcCCDistLinesAllLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | PjcCCDistLinesAllLineNum | LINE_NUM | — | ✅ |
| 28 | PjcCCDistLinesAllLineNumReversed | LINE_NUM_REVERSED | — | ✅ |
| 29 | PjcCCDistLinesAllLineType | LINE_TYPE | — | ✅ |
| 30 | PjcCCDistLinesAllMarkupCalcBaseCode | MARKUP_CALC_BASE_CODE | — | ✅ |
| 31 | PjcCCDistLinesAllObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 32 | PjcCCDistLinesAllOrgId | ORG_ID | — | ✅ |
| 33 | PjcCCDistLinesAllPaDate | PA_DATE | — | ✅ |
| 34 | PjcCCDistLinesAllPaPeriodName | PA_PERIOD_NAME | — | ✅ |
| 35 | PjcCCDistLinesAllProjectId | PROJECT_ID | — | ✅ |
| 36 | PjcCCDistLinesAllProjectTpCurrencyCode | PROJECT_TP_CURRENCY_CODE | — | ✅ |
| 37 | PjcCCDistLinesAllProjectTpExchangeRate | PROJECT_TP_EXCHANGE_RATE | — | ✅ |
| 38 | PjcCCDistLinesAllProjectTpRateDate | PROJECT_TP_RATE_DATE | — | ✅ |
| 39 | PjcCCDistLinesAllProjectTpRateType | PROJECT_TP_RATE_TYPE | — | ✅ |
| 40 | PjcCCDistLinesAllProjectTransferPrice | PROJECT_TRANSFER_PRICE | — | ✅ |
| 41 | PjcCCDistLinesAllProjfuncTpCurrencyCode | PROJFUNC_TP_CURRENCY_CODE | — | ✅ |
| 42 | PjcCCDistLinesAllProjfuncTpExchangeRate | PROJFUNC_TP_EXCHANGE_RATE | — | ✅ |
| 43 | PjcCCDistLinesAllProjfuncTpRateDate | PROJFUNC_TP_RATE_DATE | — | ✅ |
| 44 | PjcCCDistLinesAllProjfuncTpRateType | PROJFUNC_TP_RATE_TYPE | — | ✅ |
| 45 | PjcCCDistLinesAllProjfuncTransferPrice | PROJFUNC_TRANSFER_PRICE | — | ✅ |
| 46 | PjcCCDistLinesAllReference1 | REFERENCE_1 | — | ✅ |
| 47 | PjcCCDistLinesAllReference2 | REFERENCE_2 | — | ✅ |
| 48 | PjcCCDistLinesAllReference3 | REFERENCE_3 | — | ✅ |
| 49 | PjcCCDistLinesAllRequestId | REQUEST_ID | — | ✅ |
| 50 | PjcCCDistLinesAllReversedFlag | REVERSED_FLAG | — | ✅ |
| 51 | PjcCCDistLinesAllRulePercentage | RULE_PERCENTAGE | — | ✅ |
| 52 | PjcCCDistLinesAllScheduleLinePercentage | SCHEDULE_LINE_PERCENTAGE | — | ✅ |
| 53 | PjcCCDistLinesAllTaskId | TASK_ID | — | ✅ |
| 54 | PjcCCDistLinesAllTpAmtTypeCode | TP_AMT_TYPE_CODE | — | ✅ |
| 55 | PjcCCDistLinesAllTpBaseAmount | TP_BASE_AMOUNT | — | ✅ |
| 56 | PjcCCDistLinesAllTpJobId | TP_JOB_ID | — | ✅ |
| 57 | PjcCCDistLinesAllTpScheduleLineId | TP_SCHEDULE_LINE_ID | — | ✅ |
| 58 | PjcCCDistLinesAllTransferRejectionCode | TRANSFER_REJECTION_CODE | — | ✅ |
| 59 | PjcCCDistLinesAllTransferredDate | TRANSFERRED_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
