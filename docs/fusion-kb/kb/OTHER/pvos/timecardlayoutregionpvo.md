---
id: DOC-OTHER-PVO-TimecardLayoutRegionPVO
doc_type: system-doc
title: "TimecardLayoutRegionPVO — PVO Cross-Module"
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
  - TimecardLayoutRegionPVO
  - timecardlayoutregionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimecardLayoutRegionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Timecard Layout Region. Acessa as tabelas: HXT_TCLAYST_B, HXT_TCLAYST_PROP, HXT_TCLAYST_TL (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TimecardLayoutRegionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 4 | 2 | 49 | 74% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_tclayst_b|HXT_TCLAYST_B]] — 16 atributos (7 BICC)
- [[hxt_tclayst_prop|HXT_TCLAYST_PROP]] — 7 atributos (5 BICC)
- [[hxt_tclayst_tl|HXT_TCLAYST_TL]] — 4 atributos (2 BICC)
- [[hxt_tclay_region_v|HXT_TCLAY_REGION_V]] — 39 atributos (2 PKs, 35 BICC)

---

## ⚙️ Atributos

### [[hxt_tclayst_b|HXT_TCLAYST_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPEOAnswerSetId | ANS_SET_ID | — | — |
| 2 | TclaystPEOAuditUsageFlag | AUDIT_USAGE_FLAG | — | — |
| 3 | TclaystPEOCompletionStatus | COMPLETION_STATUS | — | — |
| 4 | TclaystPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | TclaystPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | TclaystPEODefaultAuditConfigFlag | DEFAULT_AUDIT_CONFIG_FLAG | — | — |
| 7 | TclaystPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 8 | TclaystPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | TclaystPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | TclaystPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | TclaystPEOModuleId | MODULE_ID | — | — |
| 12 | TclaystPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | TclaystPEOOwner | OWNER | — | — |
| 14 | TclaystPEOShortCode | SHORT_CODE | — | ✅ |
| 15 | TclaystPEOTimeConsumerSetId | TCSMR_SET_ID | — | ✅ |
| 16 | TclaystPEOTimecardLayoutSetId | TCLAYST_ID | — | — |

### [[hxt_tclayst_prop|HXT_TCLAYST_PROP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystPropPEOAnsSetId | ANS_SET_ID | — | — |
| 2 | TclaystPropPEOIndMgrFlag | IND_MGR_FLAG | — | ✅ |
| 3 | TclaystPropPEOIndTcsmrsCode | IND_TCSMRS_CODE | — | ✅ |
| 4 | TclaystPropPEOMembershipFlag | MEMBERSHIP_FLAG | — | ✅ |
| 5 | TclaystPropPEOTclaystPropCd | TCLAYST_PROP_CD | — | ✅ |
| 6 | TclaystPropPEOTclaystPropId | TCLAYST_PROP_ID | — | ✅ |
| 7 | TclaystPropPEOTclaystTeType | TCLAYST_TE_TYPE | — | — |

### [[hxt_tclayst_tl|HXT_TCLAYST_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclaystTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TclaystTLPEOLanguage | LANGUAGE | — | — |
| 3 | TclaystTLPEOName | NAME | — | ✅ |
| 4 | TclaystTLPEOTimecardLayoutSetId | TCLAYST_ID | — | — |

### [[hxt_tclay_region_v|HXT_TCLAY_REGION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LayoutRegionVPEOAddtlLabel | ADDTL_LABEL | — | ✅ |
| 2 | LayoutRegionVPEOCommentDateFormat | COMMENT_DATE_FORMAT | — | ✅ |
| 3 | LayoutRegionVPEOCommentDisplayOption | COMMENT_DISPLAY_OPTION | — | ✅ |
| 4 | LayoutRegionVPEOCommentLabel | COMMENT_LABEL | — | ✅ |
| 5 | LayoutRegionVPEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | LayoutRegionVPEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | LayoutRegionVPEODailyDateFormat | DAILY_DATE_FORMAT | — | ✅ |
| 8 | LayoutRegionVPEODailyLabel | DAILY_LABEL | — | ✅ |
| 9 | LayoutRegionVPEOHoursDateFormat | HOURS_DATE_FORMAT | — | ✅ |
| 10 | LayoutRegionVPEOHoursDecimalPlace | HOURS_DECIMAL_PLACE | — | ✅ |
| 11 | LayoutRegionVPEOInstanceFlag | INSTANCE_FLAG | — | — |
| 12 | LayoutRegionVPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LayoutRegionVPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LayoutRegionVPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LayoutRegionVPEOLayoutRegionCode | LAYOUT_REGION_CODE | 🔑 | ✅ |
| 16 | LayoutRegionVPEOMatrixBlankRowsDefault | MATRIX_BLANK_ROWS_DEFAULT | — | ✅ |
| 17 | LayoutRegionVPEOMatrixDateFormat | MATRIX_DATE_FORMAT | — | ✅ |
| 18 | LayoutRegionVPEOMatrixDecimalPlace | MATRIX_DECIMAL_PLACE | — | ✅ |
| 19 | LayoutRegionVPEOMatrixDisplayHourSlider | MATRIX_DISPLAY_HOUR_SLIDER | — | ✅ |
| 20 | LayoutRegionVPEOMatrixDisplayTimeSlider | MATRIX_DISPLAY_TIME_SLIDER | — | ✅ |
| 21 | LayoutRegionVPEOMatrixDisplayUom | MATRIX_DISPLAY_UOM | — | ✅ |
| 22 | LayoutRegionVPEOMatrixEnableButtonRule | MATRIX_ENABLE_BUTTON_RULE | — | ✅ |
| 23 | LayoutRegionVPEOMatrixEnableMidnight | MATRIX_ENABLE_MIDNIGHT | — | ✅ |
| 24 | LayoutRegionVPEOMatrixEnableNegative | MATRIX_ENABLE_NEGATIVE | — | ✅ |
| 25 | LayoutRegionVPEOMatrixHideSeconds | MATRIX_HIDE_SECONDS | — | ✅ |
| 26 | LayoutRegionVPEOMatrixHighlightOt | MATRIX_HIGHLIGHT_OT | — | ✅ |
| 27 | LayoutRegionVPEOMatrixTeFormat | MATRIX_TE_FORMAT | — | ✅ |
| 28 | LayoutRegionVPEOMatrixViewDailyTevt | MATRIX_VIEW_DAILY_TEVT | — | ✅ |
| 29 | LayoutRegionVPEOTaskName | TASK_NAME | — | ✅ |
| 30 | LayoutRegionVPEOTaskShortName | TASK_SHORT_NAME | — | — |
| 31 | LayoutRegionVPEOTclayCd | TCLAY_CD | — | ✅ |
| 32 | LayoutRegionVPEOTclayId | TCLAY_ID | 🔑 | ✅ |
| 33 | LayoutRegionVPEOTclayTaskShortName | TCLAY_TASK_SHORT_NAME | — | ✅ |
| 34 | LayoutRegionVPEOTclayType | TCLAY_TYPE | — | ✅ |
| 35 | LayoutRegionVPEOTclaystId | TCLAYST_ID | — | ✅ |
| 36 | LayoutRegionVPEOTimetotalsDecimalPlace | TIMETOTALS_DECIMAL_PLACE | — | ✅ |
| 37 | LayoutRegionVPEOTlTaskFeaturesId | TL_TASK_FEATURES_ID | — | — |
| 38 | LayoutRegionVPEOTlTaskResultsId | TL_TASK_RESULTS_ID | — | — |
| 39 | LayoutRegionVPEOUnitsDateFormat | UNITS_DATE_FORMAT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
