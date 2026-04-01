---
id: DOC-OTHER-PVO-TimecardLayoutCompPVO
doc_type: system-doc
title: "TimecardLayoutCompPVO — PVO Cross-Module"
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
  - TimecardLayoutCompPVO
  - timecardlayoutcomppvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimecardLayoutCompPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Timecard Layout Comp. Acessa as tabelas: HXT_TCLAYFLD_DEFNS_B, HXT_TCLAYFLD_DEFNS_TL, HXT_TCLAYST_B (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.LayoutSetAM.TimecardLayoutCompPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 154 | 6 | 1 | 58 | 38% |

---

## 🔗 Tabelas Relacionadas

- [[hxt_tclayfld_defns_b|HXT_TCLAYFLD_DEFNS_B]] — 83 atributos (1 PKs, 6 BICC)
- [[hxt_tclayfld_defns_tl|HXT_TCLAYFLD_DEFNS_TL]] — 5 atributos (3 BICC)
- [[hxt_tclayst_b|HXT_TCLAYST_B]] — 16 atributos (7 BICC)
- [[hxt_tclayst_prop|HXT_TCLAYST_PROP]] — 7 atributos (5 BICC)
- [[hxt_tclayst_tl|HXT_TCLAYST_TL]] — 4 atributos (2 BICC)
- [[hxt_tclay_region_v|HXT_TCLAY_REGION_V]] — 39 atributos (35 BICC)

---

## ⚙️ Atributos

### [[hxt_tclayfld_defns_b|HXT_TCLAYFLD_DEFNS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclayfldBPEOCreatedBy | CREATED_BY | — | — |
| 2 | TclayfldBPEOCreationDate | CREATION_DATE | — | — |
| 3 | TclayfldBPEODisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | TclayfldBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 5 | TclayfldBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TclayfldBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TclayfldBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TclayfldBPEOModuleId | MODULE_ID | — | — |
| 9 | TclayfldBPEOObjVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | TclayfldBPEOPTclayfldDefnsId | P_TCLAYFLD_DEFNS_ID | — | — |
| 11 | TclayfldBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 12 | TclayfldBPEOSguid | SGUID | — | — |
| 13 | TclayfldBPEOTclayId | TCLAY_ID | — | — |
| 14 | TclayfldBPEOTclayfldAtrbCat | TCLAYFLD_ATTRIBUTE_CATEGORY | — | — |
| 15 | TclayfldBPEOTclayfldAtrbChar1 | TCLAYFLD_ATTRIBUTE_CHAR1 | — | — |
| 16 | TclayfldBPEOTclayfldAtrbChar10 | TCLAYFLD_ATTRIBUTE_CHAR10 | — | — |
| 17 | TclayfldBPEOTclayfldAtrbChar11 | TCLAYFLD_ATTRIBUTE_CHAR11 | — | — |
| 18 | TclayfldBPEOTclayfldAtrbChar12 | TCLAYFLD_ATTRIBUTE_CHAR12 | — | — |
| 19 | TclayfldBPEOTclayfldAtrbChar13 | TCLAYFLD_ATTRIBUTE_CHAR13 | — | — |
| 20 | TclayfldBPEOTclayfldAtrbChar14 | TCLAYFLD_ATTRIBUTE_CHAR14 | — | — |
| 21 | TclayfldBPEOTclayfldAtrbChar15 | TCLAYFLD_ATTRIBUTE_CHAR15 | — | — |
| 22 | TclayfldBPEOTclayfldAtrbChar16 | TCLAYFLD_ATTRIBUTE_CHAR16 | — | — |
| 23 | TclayfldBPEOTclayfldAtrbChar17 | TCLAYFLD_ATTRIBUTE_CHAR17 | — | — |
| 24 | TclayfldBPEOTclayfldAtrbChar18 | TCLAYFLD_ATTRIBUTE_CHAR18 | — | — |
| 25 | TclayfldBPEOTclayfldAtrbChar19 | TCLAYFLD_ATTRIBUTE_CHAR19 | — | — |
| 26 | TclayfldBPEOTclayfldAtrbChar2 | TCLAYFLD_ATTRIBUTE_CHAR2 | — | — |
| 27 | TclayfldBPEOTclayfldAtrbChar20 | TCLAYFLD_ATTRIBUTE_CHAR20 | — | — |
| 28 | TclayfldBPEOTclayfldAtrbChar21 | TCLAYFLD_ATTRIBUTE_CHAR21 | — | — |
| 29 | TclayfldBPEOTclayfldAtrbChar22 | TCLAYFLD_ATTRIBUTE_CHAR22 | — | — |
| 30 | TclayfldBPEOTclayfldAtrbChar23 | TCLAYFLD_ATTRIBUTE_CHAR23 | — | — |
| 31 | TclayfldBPEOTclayfldAtrbChar24 | TCLAYFLD_ATTRIBUTE_CHAR24 | — | — |
| 32 | TclayfldBPEOTclayfldAtrbChar25 | TCLAYFLD_ATTRIBUTE_CHAR25 | — | — |
| 33 | TclayfldBPEOTclayfldAtrbChar26 | TCLAYFLD_ATTRIBUTE_CHAR26 | — | ✅ |
| 34 | TclayfldBPEOTclayfldAtrbChar27 | TCLAYFLD_ATTRIBUTE_CHAR27 | — | — |
| 35 | TclayfldBPEOTclayfldAtrbChar28 | TCLAYFLD_ATTRIBUTE_CHAR28 | — | — |
| 36 | TclayfldBPEOTclayfldAtrbChar29 | TCLAYFLD_ATTRIBUTE_CHAR29 | — | — |
| 37 | TclayfldBPEOTclayfldAtrbChar3 | TCLAYFLD_ATTRIBUTE_CHAR3 | — | — |
| 38 | TclayfldBPEOTclayfldAtrbChar30 | TCLAYFLD_ATTRIBUTE_CHAR30 | — | — |
| 39 | TclayfldBPEOTclayfldAtrbChar4 | TCLAYFLD_ATTRIBUTE_CHAR4 | — | — |
| 40 | TclayfldBPEOTclayfldAtrbChar5 | TCLAYFLD_ATTRIBUTE_CHAR5 | — | — |
| 41 | TclayfldBPEOTclayfldAtrbChar6 | TCLAYFLD_ATTRIBUTE_CHAR6 | — | — |
| 42 | TclayfldBPEOTclayfldAtrbChar7 | TCLAYFLD_ATTRIBUTE_CHAR7 | — | — |
| 43 | TclayfldBPEOTclayfldAtrbChar8 | TCLAYFLD_ATTRIBUTE_CHAR8 | — | — |
| 44 | TclayfldBPEOTclayfldAtrbChar9 | TCLAYFLD_ATTRIBUTE_CHAR9 | — | — |
| 45 | TclayfldBPEOTclayfldAtrbDate1 | TCLAYFLD_ATTRIBUTE_DATE1 | — | — |
| 46 | TclayfldBPEOTclayfldAtrbDate10 | TCLAYFLD_ATTRIBUTE_DATE10 | — | — |
| 47 | TclayfldBPEOTclayfldAtrbDate11 | TCLAYFLD_ATTRIBUTE_DATE11 | — | — |
| 48 | TclayfldBPEOTclayfldAtrbDate12 | TCLAYFLD_ATTRIBUTE_DATE12 | — | — |
| 49 | TclayfldBPEOTclayfldAtrbDate13 | TCLAYFLD_ATTRIBUTE_DATE13 | — | — |
| 50 | TclayfldBPEOTclayfldAtrbDate14 | TCLAYFLD_ATTRIBUTE_DATE14 | — | — |
| 51 | TclayfldBPEOTclayfldAtrbDate15 | TCLAYFLD_ATTRIBUTE_DATE15 | — | — |
| 52 | TclayfldBPEOTclayfldAtrbDate2 | TCLAYFLD_ATTRIBUTE_DATE2 | — | — |
| 53 | TclayfldBPEOTclayfldAtrbDate3 | TCLAYFLD_ATTRIBUTE_DATE3 | — | — |
| 54 | TclayfldBPEOTclayfldAtrbDate4 | TCLAYFLD_ATTRIBUTE_DATE4 | — | — |
| 55 | TclayfldBPEOTclayfldAtrbDate5 | TCLAYFLD_ATTRIBUTE_DATE5 | — | — |
| 56 | TclayfldBPEOTclayfldAtrbDate6 | TCLAYFLD_ATTRIBUTE_DATE6 | — | — |
| 57 | TclayfldBPEOTclayfldAtrbDate7 | TCLAYFLD_ATTRIBUTE_DATE7 | — | — |
| 58 | TclayfldBPEOTclayfldAtrbDate8 | TCLAYFLD_ATTRIBUTE_DATE8 | — | — |
| 59 | TclayfldBPEOTclayfldAtrbDate9 | TCLAYFLD_ATTRIBUTE_DATE9 | — | — |
| 60 | TclayfldBPEOTclayfldAtrbNum1 | TCLAYFLD_ATTRIBUTE_NUMBER1 | — | — |
| 61 | TclayfldBPEOTclayfldAtrbNum10 | TCLAYFLD_ATTRIBUTE_NUMBER10 | — | — |
| 62 | TclayfldBPEOTclayfldAtrbNum11 | TCLAYFLD_ATTRIBUTE_NUMBER11 | — | — |
| 63 | TclayfldBPEOTclayfldAtrbNum12 | TCLAYFLD_ATTRIBUTE_NUMBER12 | — | — |
| 64 | TclayfldBPEOTclayfldAtrbNum13 | TCLAYFLD_ATTRIBUTE_NUMBER13 | — | — |
| 65 | TclayfldBPEOTclayfldAtrbNum14 | TCLAYFLD_ATTRIBUTE_NUMBER14 | — | — |
| 66 | TclayfldBPEOTclayfldAtrbNum15 | TCLAYFLD_ATTRIBUTE_NUMBER15 | — | — |
| 67 | TclayfldBPEOTclayfldAtrbNum16 | TCLAYFLD_ATTRIBUTE_NUMBER16 | — | — |
| 68 | TclayfldBPEOTclayfldAtrbNum17 | TCLAYFLD_ATTRIBUTE_NUMBER17 | — | — |
| 69 | TclayfldBPEOTclayfldAtrbNum18 | TCLAYFLD_ATTRIBUTE_NUMBER18 | — | — |
| 70 | TclayfldBPEOTclayfldAtrbNum19 | TCLAYFLD_ATTRIBUTE_NUMBER19 | — | — |
| 71 | TclayfldBPEOTclayfldAtrbNum2 | TCLAYFLD_ATTRIBUTE_NUMBER2 | — | — |
| 72 | TclayfldBPEOTclayfldAtrbNum20 | TCLAYFLD_ATTRIBUTE_NUMBER20 | — | — |
| 73 | TclayfldBPEOTclayfldAtrbNum3 | TCLAYFLD_ATTRIBUTE_NUMBER3 | — | — |
| 74 | TclayfldBPEOTclayfldAtrbNum4 | TCLAYFLD_ATTRIBUTE_NUMBER4 | — | — |
| 75 | TclayfldBPEOTclayfldAtrbNum5 | TCLAYFLD_ATTRIBUTE_NUMBER5 | — | — |
| 76 | TclayfldBPEOTclayfldAtrbNum6 | TCLAYFLD_ATTRIBUTE_NUMBER6 | — | — |
| 77 | TclayfldBPEOTclayfldAtrbNum7 | TCLAYFLD_ATTRIBUTE_NUMBER7 | — | — |
| 78 | TclayfldBPEOTclayfldAtrbNum8 | TCLAYFLD_ATTRIBUTE_NUMBER8 | — | — |
| 79 | TclayfldBPEOTclayfldAtrbNum9 | TCLAYFLD_ATTRIBUTE_NUMBER9 | — | — |
| 80 | TclayfldBPEOTclayfldDefInsFlag | TCLAYFLD_DEFNS_INSTANCE_FLAG | — | — |
| 81 | TclayfldBPEOTclayfldDefnsCd | TCLAYFLD_DEFNS_CD | — | ✅ |
| 82 | TclayfldBPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | 🔑 | ✅ |
| 83 | TclayfldBPEOTclayfldTmplId | TCLAYFLD_TMPL_ID | — | ✅ |

### [[hxt_tclayfld_defns_tl|HXT_TCLAYFLD_DEFNS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TclayfldTLPEODescription | DESCRIPTION | — | ✅ |
| 2 | TclayfldTLPEOLabel | LABEL | — | ✅ |
| 3 | TclayfldTLPEOLanguage | LANGUAGE | — | — |
| 4 | TclayfldTLPEOName | NAME | — | ✅ |
| 5 | TclayfldTLPEOTclayfldDefnsId | TCLAYFLD_DEFNS_ID | — | — |

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
| 15 | LayoutRegionVPEOLayoutRegionCode | LAYOUT_REGION_CODE | — | ✅ |
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
| 32 | LayoutRegionVPEOTclayId | TCLAY_ID | — | ✅ |
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
