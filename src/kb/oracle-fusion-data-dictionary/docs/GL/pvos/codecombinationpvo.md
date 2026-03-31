---
id: DOC-GL-PVO-CodeCombinationPVO
doc_type: system-doc
title: "CodeCombinationPVO — PVO General Ledger"
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
  - CodeCombinationPVO
  - codecombinationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CodeCombinationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Code Combination. Acessa as tabelas: AP_RECON_SUMMARY_CCID, AR_RECON_SUMMARY_CCID, FND_KF_STR_INSTANCES_VL (+2).

**Caminho:** `FscmTopModelAM.FinGlAccountsCodeComboAM.CodeCombinationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 143 | 5 | 1 | 17 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ap_recon_summary_ccid|AP_RECON_SUMMARY_CCID]] — 7 atributos
- [[ar_recon_summary_ccid|AR_RECON_SUMMARY_CCID]] — 7 atributos
- [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]] — 14 atributos (2 BICC)
- [[gl_code_combinations|GL_CODE_COMBINATIONS]] — 105 atributos (1 PKs, 14 BICC)
- [[gl_stat_account_uom|GL_STAT_ACCOUNT_UOM]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[ap_recon_summary_ccid|AP_RECON_SUMMARY_CCID]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApReconBalancingSegment | BALANCING_SEGMENT | — | — |
| 2 | ApReconChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | ApReconCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | ApReconLedgerId | LEDGER_ID | — | — |
| 5 | ApReconNaturalAccountSegment | NATURAL_ACCOUNT_SEGMENT | — | — |
| 6 | ApReconReconSummaryCcidId | RECON_SUMMARY_CCID_ID | — | — |
| 7 | ApReconRequestId | REQUEST_ID | — | — |

### [[ar_recon_summary_ccid|AR_RECON_SUMMARY_CCID]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArReconBalancingSegment | BALANCING_SEGMENT | — | — |
| 2 | ArReconChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | ArReconCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 4 | ArReconLedgerId | LEDGER_ID | — | — |
| 5 | ArReconNaturalAccountSegment | NATURAL_ACCOUNT_SEGMENT | — | — |
| 6 | ArReconReconSummaryCcidId | RECON_SUMMARY_CCID_ID | — | — |
| 7 | ArReconRequestId | REQUEST_ID | — | — |

### [[fnd_kf_str_instances_vl|FND_KF_STR_INSTANCES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeyFlexfieldStructureInstancApplicationId | APPLICATION_ID | — | — |
| 2 | KeyFlexfieldStructureInstancCreatedBy | CREATED_BY | — | — |
| 3 | KeyFlexfieldStructureInstancCreationDate | CREATION_DATE | — | — |
| 4 | KeyFlexfieldStructureInstancDescription | DESCRIPTION | — | — |
| 5 | KeyFlexfieldStructureInstancEnabledFlag | ENABLED_FLAG | — | — |
| 6 | KeyFlexfieldStructureInstancKeyFlexfieldCode | KEY_FLEXFIELD_CODE | — | — |
| 7 | KeyFlexfieldStructureInstancLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | KeyFlexfieldStructureInstancLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | KeyFlexfieldStructureInstancLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | KeyFlexfieldStructureInstancName | NAME | — | ✅ |
| 11 | KeyFlexfieldStructureInstancStructureId | STRUCTURE_ID | — | — |
| 12 | KeyFlexfieldStructureInstancStructureInstanceCode | STRUCTURE_INSTANCE_CODE | — | — |
| 13 | KeyFlexfieldStructureInstancStructureInstanceId | STRUCTURE_INSTANCE_ID | — | — |
| 14 | KeyFlexfieldStructureInstancStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | — | — |

### [[gl_code_combinations|GL_CODE_COMBINATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeCombinationAccountType | ACCOUNT_TYPE | — | ✅ |
| 2 | CodeCombinationAllocationCreateFlag | ALLOCATION_CREATE_FLAG | — | — |
| 3 | CodeCombinationAlternateCodeCombinationId | ALTERNATE_CODE_COMBINATION_ID | — | ✅ |
| 4 | CodeCombinationChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | ✅ |
| 5 | CodeCombinationCompanyCostCenterOrgId | COMPANY_COST_CENTER_ORG_ID | — | ✅ |
| 6 | CodeCombinationCreatedBy | CREATED_BY | — | ✅ |
| 7 | CodeCombinationCreationDate | CREATION_DATE | — | ✅ |
| 8 | CodeCombinationDetailBudgetingAllowedFlag | DETAIL_BUDGETING_ALLOWED_FLAG | — | — |
| 9 | CodeCombinationDetailPostingAllowedFlag | DETAIL_POSTING_ALLOWED_FLAG | — | — |
| 10 | CodeCombinationEnabledFlag | ENABLED_FLAG | — | ✅ |
| 11 | CodeCombinationEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 12 | CodeCombinationFinancialCategory | FINANCIAL_CATEGORY | — | ✅ |
| 13 | CodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 14 | CodeCombinationIgiBalancedBudgetFlag | IGI_BALANCED_BUDGET_FLAG | — | — |
| 15 | CodeCombinationJgzzReconContext | JGZZ_RECON_CONTEXT | — | — |
| 16 | CodeCombinationJgzzReconFlag | JGZZ_RECON_FLAG | — | — |
| 17 | CodeCombinationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 18 | CodeCombinationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | CodeCombinationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 20 | CodeCombinationLedgerSegment | LEDGER_SEGMENT | — | — |
| 21 | CodeCombinationLedgerTypeCode | LEDGER_TYPE_CODE | — | — |
| 22 | CodeCombinationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 23 | CodeCombinationPreserveFlag | PRESERVE_FLAG | — | — |
| 24 | CodeCombinationReference1 | REFERENCE1 | — | — |
| 25 | CodeCombinationReference2 | REFERENCE2 | — | — |
| 26 | CodeCombinationReference3 | REFERENCE3 | — | — |
| 27 | CodeCombinationReference4 | REFERENCE4 | — | — |
| 28 | CodeCombinationReference5 | REFERENCE5 | — | — |
| 29 | CodeCombinationRefreshFlag | REFRESH_FLAG | — | — |
| 30 | CodeCombinationRevaluationId | REVALUATION_ID | — | — |
| 31 | CodeCombinationSegment1 | SEGMENT1 | — | — |
| 32 | CodeCombinationSegment10 | SEGMENT10 | — | — |
| 33 | CodeCombinationSegment11 | SEGMENT11 | — | — |
| 34 | CodeCombinationSegment12 | SEGMENT12 | — | — |
| 35 | CodeCombinationSegment13 | SEGMENT13 | — | — |
| 36 | CodeCombinationSegment14 | SEGMENT14 | — | — |
| 37 | CodeCombinationSegment15 | SEGMENT15 | — | — |
| 38 | CodeCombinationSegment16 | SEGMENT16 | — | — |
| 39 | CodeCombinationSegment17 | SEGMENT17 | — | — |
| 40 | CodeCombinationSegment18 | SEGMENT18 | — | — |
| 41 | CodeCombinationSegment19 | SEGMENT19 | — | — |
| 42 | CodeCombinationSegment2 | SEGMENT2 | — | — |
| 43 | CodeCombinationSegment20 | SEGMENT20 | — | — |
| 44 | CodeCombinationSegment21 | SEGMENT21 | — | — |
| 45 | CodeCombinationSegment22 | SEGMENT22 | — | — |
| 46 | CodeCombinationSegment23 | SEGMENT23 | — | — |
| 47 | CodeCombinationSegment24 | SEGMENT24 | — | — |
| 48 | CodeCombinationSegment25 | SEGMENT25 | — | — |
| 49 | CodeCombinationSegment26 | SEGMENT26 | — | — |
| 50 | CodeCombinationSegment27 | SEGMENT27 | — | — |
| 51 | CodeCombinationSegment28 | SEGMENT28 | — | — |
| 52 | CodeCombinationSegment29 | SEGMENT29 | — | — |
| 53 | CodeCombinationSegment3 | SEGMENT3 | — | — |
| 54 | CodeCombinationSegment30 | SEGMENT30 | — | — |
| 55 | CodeCombinationSegment4 | SEGMENT4 | — | — |
| 56 | CodeCombinationSegment5 | SEGMENT5 | — | — |
| 57 | CodeCombinationSegment6 | SEGMENT6 | — | — |
| 58 | CodeCombinationSegment7 | SEGMENT7 | — | — |
| 59 | CodeCombinationSegment8 | SEGMENT8 | — | — |
| 60 | CodeCombinationSegment9 | SEGMENT9 | — | — |
| 61 | CodeCombinationSegmentAttribute1 | SEGMENT_ATTRIBUTE1 | — | — |
| 62 | CodeCombinationSegmentAttribute10 | SEGMENT_ATTRIBUTE10 | — | — |
| 63 | CodeCombinationSegmentAttribute11 | SEGMENT_ATTRIBUTE11 | — | — |
| 64 | CodeCombinationSegmentAttribute12 | SEGMENT_ATTRIBUTE12 | — | — |
| 65 | CodeCombinationSegmentAttribute13 | SEGMENT_ATTRIBUTE13 | — | — |
| 66 | CodeCombinationSegmentAttribute14 | SEGMENT_ATTRIBUTE14 | — | — |
| 67 | CodeCombinationSegmentAttribute15 | SEGMENT_ATTRIBUTE15 | — | — |
| 68 | CodeCombinationSegmentAttribute16 | SEGMENT_ATTRIBUTE16 | — | — |
| 69 | CodeCombinationSegmentAttribute17 | SEGMENT_ATTRIBUTE17 | — | — |
| 70 | CodeCombinationSegmentAttribute18 | SEGMENT_ATTRIBUTE18 | — | — |
| 71 | CodeCombinationSegmentAttribute19 | SEGMENT_ATTRIBUTE19 | — | — |
| 72 | CodeCombinationSegmentAttribute2 | SEGMENT_ATTRIBUTE2 | — | — |
| 73 | CodeCombinationSegmentAttribute20 | SEGMENT_ATTRIBUTE20 | — | — |
| 74 | CodeCombinationSegmentAttribute21 | SEGMENT_ATTRIBUTE21 | — | — |
| 75 | CodeCombinationSegmentAttribute22 | SEGMENT_ATTRIBUTE22 | — | — |
| 76 | CodeCombinationSegmentAttribute23 | SEGMENT_ATTRIBUTE23 | — | — |
| 77 | CodeCombinationSegmentAttribute24 | SEGMENT_ATTRIBUTE24 | — | — |
| 78 | CodeCombinationSegmentAttribute25 | SEGMENT_ATTRIBUTE25 | — | — |
| 79 | CodeCombinationSegmentAttribute26 | SEGMENT_ATTRIBUTE26 | — | — |
| 80 | CodeCombinationSegmentAttribute27 | SEGMENT_ATTRIBUTE27 | — | — |
| 81 | CodeCombinationSegmentAttribute28 | SEGMENT_ATTRIBUTE28 | — | — |
| 82 | CodeCombinationSegmentAttribute29 | SEGMENT_ATTRIBUTE29 | — | — |
| 83 | CodeCombinationSegmentAttribute3 | SEGMENT_ATTRIBUTE3 | — | — |
| 84 | CodeCombinationSegmentAttribute30 | SEGMENT_ATTRIBUTE30 | — | — |
| 85 | CodeCombinationSegmentAttribute31 | SEGMENT_ATTRIBUTE31 | — | — |
| 86 | CodeCombinationSegmentAttribute32 | SEGMENT_ATTRIBUTE32 | — | — |
| 87 | CodeCombinationSegmentAttribute33 | SEGMENT_ATTRIBUTE33 | — | — |
| 88 | CodeCombinationSegmentAttribute34 | SEGMENT_ATTRIBUTE34 | — | — |
| 89 | CodeCombinationSegmentAttribute35 | SEGMENT_ATTRIBUTE35 | — | — |
| 90 | CodeCombinationSegmentAttribute36 | SEGMENT_ATTRIBUTE36 | — | — |
| 91 | CodeCombinationSegmentAttribute37 | SEGMENT_ATTRIBUTE37 | — | — |
| 92 | CodeCombinationSegmentAttribute38 | SEGMENT_ATTRIBUTE38 | — | — |
| 93 | CodeCombinationSegmentAttribute39 | SEGMENT_ATTRIBUTE39 | — | — |
| 94 | CodeCombinationSegmentAttribute4 | SEGMENT_ATTRIBUTE4 | — | — |
| 95 | CodeCombinationSegmentAttribute40 | SEGMENT_ATTRIBUTE40 | — | — |
| 96 | CodeCombinationSegmentAttribute41 | SEGMENT_ATTRIBUTE41 | — | — |
| 97 | CodeCombinationSegmentAttribute42 | SEGMENT_ATTRIBUTE42 | — | — |
| 98 | CodeCombinationSegmentAttribute5 | SEGMENT_ATTRIBUTE5 | — | — |
| 99 | CodeCombinationSegmentAttribute6 | SEGMENT_ATTRIBUTE6 | — | — |
| 100 | CodeCombinationSegmentAttribute7 | SEGMENT_ATTRIBUTE7 | — | — |
| 101 | CodeCombinationSegmentAttribute8 | SEGMENT_ATTRIBUTE8 | — | — |
| 102 | CodeCombinationSegmentAttribute9 | SEGMENT_ATTRIBUTE9 | — | — |
| 103 | CodeCombinationStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 104 | CodeCombinationSummaryFlag | SUMMARY_FLAG | — | ✅ |
| 105 | CodeCombinationTemplateId | TEMPLATE_ID | — | — |

### [[gl_stat_account_uom|GL_STAT_ACCOUNT_UOM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | StatisticalUOMAccountSegmentValue | ACCOUNT_SEGMENT_VALUE | — | — |
| 2 | StatisticalUOMChartOfAccountsId | CHART_OF_ACCOUNTS_ID | — | — |
| 3 | StatisticalUOMCreatedBy | CREATED_BY | — | — |
| 4 | StatisticalUOMCreationDate | CREATION_DATE | — | — |
| 5 | StatisticalUOMDescription | DESCRIPTION | — | — |
| 6 | StatisticalUOMLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | StatisticalUOMLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | StatisticalUOMLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | StatisticalUOMObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | StatisticalUOMUnitOfMeasure | UNIT_OF_MEASURE | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
