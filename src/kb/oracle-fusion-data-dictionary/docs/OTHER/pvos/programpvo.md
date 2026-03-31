---
id: DOC-OTHER-PVO-ProgramPVO
doc_type: system-doc
title: "ProgramPVO — PVO Cross-Module"
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
  - ProgramPVO
  - programpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProgramPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Program. Acessa as tabelas: BEN_PGM_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.ProgramPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 110 | 1 | 3 | 56 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[ben_pgm_f|BEN_PGM_F]] — 110 atributos (3 PKs, 56 BICC)

---

## ⚙️ Atributos

### [[ben_pgm_f|BEN_PGM_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActyRefPerdCd | ACTY_REF_PERD_CD | — | ✅ |
| 2 | AlwsUnrstrctdEnrtFlag | ALWS_UNRSTRCTD_ENRT_FLAG | — | ✅ |
| 3 | AutoEnrtMthdRl | AUTO_ENRT_MTHD_RL | — | — |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 5 | ConfigChar1 | CONFIG_CHAR_1 | — | ✅ |
| 6 | CoordCvgForAllPlsFlg | COORD_CVG_FOR_ALL_PLS_FLG | — | ✅ |
| 7 | CreatedBy | CREATED_BY | — | ✅ |
| 8 | CreationDate | CREATION_DATE | — | ✅ |
| 9 | DfltElementTypeId | DFLT_ELEMENT_TYPE_ID | — | — |
| 10 | DfltInputValueId | DFLT_INPUT_VALUE_ID | — | — |
| 11 | DfltPgmFlag | DFLT_PGM_FLAG | — | — |
| 12 | DfltStepCd | DFLT_STEP_CD | — | ✅ |
| 13 | DfltStepRl | DFLT_STEP_RL | — | — |
| 14 | DpntCvgEndDtCd | DPNT_CVG_END_DT_CD | — | ✅ |
| 15 | DpntCvgEndDtRl | DPNT_CVG_END_DT_RL | — | — |
| 16 | DpntCvgStrtDtCd | DPNT_CVG_STRT_DT_CD | — | ✅ |
| 17 | DpntCvgStrtDtRl | DPNT_CVG_STRT_DT_RL | — | — |
| 18 | DpntDsgnLvlCd | DPNT_DSGN_LVL_CD | — | ✅ |
| 19 | DpntDsgnNoCtfnRqdFlag | DPNT_DSGN_NO_CTFN_RQD_FLAG | — | ✅ |
| 20 | DrvblFctrAplsRtsFlag | DRVBL_FCTR_APLS_RTS_FLAG | — | ✅ |
| 21 | DrvblFctrDpntEligFlag | DRVBL_FCTR_DPNT_ELIG_FLAG | — | ✅ |
| 22 | DrvblFctrPrtnEligFlag | DRVBL_FCTR_PRTN_ELIG_FLAG | — | ✅ |
| 23 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 24 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 25 | EligAplsFlag | ELIG_APLS_FLAG | — | ✅ |
| 26 | EnrtCd | ENRT_CD | — | ✅ |
| 27 | EnrtCvgEndDtCd | ENRT_CVG_END_DT_CD | — | ✅ |
| 28 | EnrtCvgEndDtRl | ENRT_CVG_END_DT_RL | — | — |
| 29 | EnrtCvgStrtDtCd | ENRT_CVG_STRT_DT_CD | — | ✅ |
| 30 | EnrtCvgStrtDtRl | ENRT_CVG_STRT_DT_RL | — | — |
| 31 | EnrtInfoRtFreqCd | ENRT_INFO_RT_FREQ_CD | — | ✅ |
| 32 | EnrtMthdCd | ENRT_MTHD_CD | — | ✅ |
| 33 | EnrtRl | ENRT_RL | — | — |
| 34 | GlobalFlag | GLOBAL_FLAG | — | ✅ |
| 35 | GspAllowOverrideFlag | GSP_ALLOW_OVERRIDE_FLAG | — | — |
| 36 | IvrIdent | IVR_IDENT | — | ✅ |
| 37 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 38 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 39 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 40 | LegislationCode | LEGISLATION_CODE | — | — |
| 41 | LegislationSubgroup | LEGISLATION_SUBGROUP | — | ✅ |
| 42 | MxDpntPctPrttLfAmt | MX_DPNT_PCT_PRTT_LF_AMT | — | ✅ |
| 43 | MxSpsPctPrttLfAmt | MX_SPS_PCT_PRTT_LF_AMT | — | ✅ |
| 44 | Name | NAME | — | ✅ |
| 45 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 46 | PerCvrdCd | PER_CVRD_CD | — | ✅ |
| 47 | PgmAttribute1 | PGM_ATTRIBUTE1 | — | — |
| 48 | PgmAttribute10 | PGM_ATTRIBUTE10 | — | — |
| 49 | PgmAttribute11 | PGM_ATTRIBUTE11 | — | — |
| 50 | PgmAttribute12 | PGM_ATTRIBUTE12 | — | — |
| 51 | PgmAttribute13 | PGM_ATTRIBUTE13 | — | — |
| 52 | PgmAttribute14 | PGM_ATTRIBUTE14 | — | — |
| 53 | PgmAttribute15 | PGM_ATTRIBUTE15 | — | — |
| 54 | PgmAttribute16 | PGM_ATTRIBUTE16 | — | — |
| 55 | PgmAttribute17 | PGM_ATTRIBUTE17 | — | — |
| 56 | PgmAttribute18 | PGM_ATTRIBUTE18 | — | — |
| 57 | PgmAttribute19 | PGM_ATTRIBUTE19 | — | — |
| 58 | PgmAttribute2 | PGM_ATTRIBUTE2 | — | — |
| 59 | PgmAttribute20 | PGM_ATTRIBUTE20 | — | — |
| 60 | PgmAttribute21 | PGM_ATTRIBUTE21 | — | — |
| 61 | PgmAttribute22 | PGM_ATTRIBUTE22 | — | — |
| 62 | PgmAttribute23 | PGM_ATTRIBUTE23 | — | — |
| 63 | PgmAttribute24 | PGM_ATTRIBUTE24 | — | — |
| 64 | PgmAttribute25 | PGM_ATTRIBUTE25 | — | — |
| 65 | PgmAttribute26 | PGM_ATTRIBUTE26 | — | — |
| 66 | PgmAttribute27 | PGM_ATTRIBUTE27 | — | — |
| 67 | PgmAttribute28 | PGM_ATTRIBUTE28 | — | — |
| 68 | PgmAttribute29 | PGM_ATTRIBUTE29 | — | — |
| 69 | PgmAttribute3 | PGM_ATTRIBUTE3 | — | — |
| 70 | PgmAttribute30 | PGM_ATTRIBUTE30 | — | — |
| 71 | PgmAttribute4 | PGM_ATTRIBUTE4 | — | — |
| 72 | PgmAttribute5 | PGM_ATTRIBUTE5 | — | — |
| 73 | PgmAttribute6 | PGM_ATTRIBUTE6 | — | — |
| 74 | PgmAttribute7 | PGM_ATTRIBUTE7 | — | — |
| 75 | PgmAttribute8 | PGM_ATTRIBUTE8 | — | — |
| 76 | PgmAttribute9 | PGM_ATTRIBUTE9 | — | — |
| 77 | PgmAttributeCategory | PGM_ATTRIBUTE_CATEGORY | — | — |
| 78 | PgmDesc | PGM_DESC | — | ✅ |
| 79 | PgmGrpCd | PGM_GRP_CD | — | ✅ |
| 80 | PgmId | PGM_ID | 🔑 | ✅ |
| 81 | PgmPrvdsCrFlag | PGM_PRVDS_CR_FLAG | — | — |
| 82 | PgmPrvdsNoAutoEnrtFlag | PGM_PRVDS_NO_AUTO_ENRT_FLAG | — | ✅ |
| 83 | PgmPrvdsNoDfltEnrtFlag | PGM_PRVDS_NO_DFLT_ENRT_FLAG | — | ✅ |
| 84 | PgmStatCd | PGM_STAT_CD | — | ✅ |
| 85 | PgmTypCd | PGM_TYP_CD | — | ✅ |
| 86 | PgmUom | PGM_UOM | — | ✅ |
| 87 | PgmUseAllAsntsEligFlag | PGM_USE_ALL_ASNTS_ELIG_FLAG | — | ✅ |
| 88 | PoeLvlCd | POE_LVL_CD | — | ✅ |
| 89 | PrtnEligOvridAlwdFlag | PRTN_ELIG_OVRID_ALWD_FLAG | — | ✅ |
| 90 | PrttChcUncrsTrtmtFlag | PRTT_CHC_UNCRS_TRTMT_FLAG | — | — |
| 91 | RtEndDtCd | RT_END_DT_CD | — | ✅ |
| 92 | RtEndDtRl | RT_END_DT_RL | — | — |
| 93 | RtStrtDtCd | RT_STRT_DT_CD | — | ✅ |
| 94 | RtStrtDtRl | RT_STRT_DT_RL | — | — |
| 95 | SalaryCalcMthdCd | SALARY_CALC_MTHD_CD | — | ✅ |
| 96 | SalaryCalcMthdRl | SALARY_CALC_MTHD_RL | — | ✅ |
| 97 | ScoresCalcMthdCd | SCORES_CALC_MTHD_CD | — | ✅ |
| 98 | ScoresCalcRl | SCORES_CALC_RL | — | ✅ |
| 99 | ShortCode | SHORT_CODE | — | ✅ |
| 100 | ShortName | SHORT_NAME | — | ✅ |
| 101 | TrkIneligPerFlag | TRK_INELIG_PER_FLAG | — | ✅ |
| 102 | UpdateSalaryCd | UPDATE_SALARY_CD | — | ✅ |
| 103 | UrlRefName | URL_REF_NAME | — | ✅ |
| 104 | UseMultiPayRatesFlag | USE_MULTI_PAY_RATES_FLAG | — | — |
| 105 | UseProgPointsFlag | USE_PROG_POINTS_FLAG | — | — |
| 106 | UseScoresCd | USE_SCORES_CD | — | — |
| 107 | UseVariableRatesFlag | USE_VARIABLE_RATES_FLAG | — | — |
| 108 | UsesAllAsmtsForRtsFlag | USES_ALL_ASMTS_FOR_RTS_FLAG | — | ✅ |
| 109 | VrfyFmlyMmbrCd | VRFY_FMLY_MMBR_CD | — | ✅ |
| 110 | VrfyFmlyMmbrRl | VRFY_FMLY_MMBR_RL | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
