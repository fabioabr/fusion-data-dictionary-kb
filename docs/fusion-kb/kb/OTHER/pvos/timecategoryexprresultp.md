---
id: DOC-OTHER-PVO-TimeCategoryExprResultP
doc_type: system-doc
title: "TimeCategoryExprResultP — PVO Cross-Module"
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
  - TimeCategoryExprResultP
  - timecategoryexprresultp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeCategoryExprResultP

## 📌 Visão Geral

View Object para extração BICC de dados de Time Category Expr Result P. Acessa as tabelas: HWM_TCATS_B, HWM_TCATS_TL, HWM_TCAT_EXPR_RESULTS_B (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.TimeCategoryAM.TimeCategoryExprResultP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 50 | 5 | 1 | 29 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tcats_b|HWM_TCATS_B]] — 14 atributos (9 BICC)
- [[hwm_tcats_tl|HWM_TCATS_TL]] — 4 atributos (2 BICC)
- [[hwm_tcat_expr_results_b|HWM_TCAT_EXPR_RESULTS_B]] — 26 atributos (1 PKs, 16 BICC)
- [[hwm_tcat_expr_results_tl|HWM_TCAT_EXPR_RESULTS_TL]] — 3 atributos
- [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]] — 3 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hwm_tcats_b|HWM_TCATS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeCategoryBPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | TimeCategoryBPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | TimeCategoryBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 4 | TimeCategoryBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TimeCategoryBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TimeCategoryBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TimeCategoryBPEOModuleId | MODULE_ID | — | — |
| 8 | TimeCategoryBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | TimeCategoryBPEOPersistentFlag | PERSISTENT_FLAG | — | ✅ |
| 10 | TimeCategoryBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 11 | TimeCategoryBPEOSguid | SGUID | — | — |
| 12 | TimeCategoryBPEOTcatCd | TCAT_CD | — | ✅ |
| 13 | TimeCategoryBPEOTcatId | TCAT_ID | — | ✅ |
| 14 | TimeCategoryBPEOUom | UOM | — | ✅ |

### [[hwm_tcats_tl|HWM_TCATS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TcatId | TCAT_ID | — | — |
| 2 | TimeCategoryTLPEODescription | DESCRIPTION | — | ✅ |
| 3 | TimeCategoryTLPEOLanguage | LANGUAGE | — | — |
| 4 | TimeCategoryTLPEOTcatName | TCAT_NAME | — | ✅ |

### [[hwm_tcat_expr_results_b|HWM_TCAT_EXPR_RESULTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TCatExprResultBPEOCreatedBy | CREATED_BY | — | — |
| 2 | TCatExprResultBPEOCreationDate | CREATION_DATE | — | — |
| 3 | TCatExprResultBPEODataSourceUsageId | DATA_SOURCE_USAGE_ID | — | — |
| 4 | TCatExprResultBPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | TCatExprResultBPEODisplayValue | DISPLAY_VALUE | — | ✅ |
| 6 | TCatExprResultBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | TCatExprResultBPEOExprRowIdentifier | EXPR_ROW_IDENTIFIER | — | — |
| 8 | TCatExprResultBPEOExpressionGroupId | EXPRESSION_GROUP_ID | — | — |
| 9 | TCatExprResultBPEOImpTcatId | IMP_TCAT_ID | — | — |
| 10 | TCatExprResultBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | TCatExprResultBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | TCatExprResultBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | TCatExprResultBPEOLeftParenthesisNum | LEFT_PARENTHESIS_NUM | — | ✅ |
| 14 | TCatExprResultBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | TCatExprResultBPEOOperator11 | OPERATOR | — | ✅ |
| 16 | TCatExprResultBPEORightParenthesisNum | RIGHT_PARENTHESIS_NUM | — | ✅ |
| 17 | TCatExprResultBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 18 | TCatExprResultBPEOSguid | SGUID | — | — |
| 19 | TCatExprResultBPEOTcatExprResultId | TCAT_EXPR_RESULT_ID | 🔑 | ✅ |
| 20 | TCatExprResultBPEOTcatId | TCAT_ID | — | ✅ |
| 21 | TCatExprResultBPEOTimeAtrbFldId | TIME_ATRB_FLD_ID | — | ✅ |
| 22 | TCatExprResultBPEOValueChar | VALUE_CHAR | — | ✅ |
| 23 | TCatExprResultBPEOValueDate | VALUE_DATE | — | ✅ |
| 24 | TCatExprResultBPEOValueId | VALUE_ID | — | ✅ |
| 25 | TCatExprResultBPEOValueTimestamp | VALUE_TIMESTAMP | — | ✅ |
| 26 | TCatExprResultBPEOValueType | VALUE_TYPE | — | ✅ |

### [[hwm_tcat_expr_results_tl|HWM_TCAT_EXPR_RESULTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TCatExprResultTLPEOLanguage | LANGUAGE | — | — |
| 2 | TCatExprResultTLPEOTcatExprResultId | TCAT_EXPR_RESULT_ID | — | — |
| 3 | TCatExprResultTLPEOUserDescription | USER_DESCRIPTION | — | — |

### [[hwm_tm_atrb_flds_vl|HWM_TM_ATRB_FLDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TimeAttributeFieldVLPEODisplayName | DISPLAY_NAME | — | ✅ |
| 2 | TimeAttributeFieldVLPEOName | NAME | — | ✅ |
| 3 | TimeAttributeFieldVLPEOTimeAttributeFieldId | TM_ATRB_FLD_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
