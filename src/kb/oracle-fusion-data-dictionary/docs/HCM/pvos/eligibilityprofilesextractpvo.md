---
id: DOC-HCM-PVO-EligibilityProfilesExtractPVO
doc_type: system-doc
title: "EligibilityProfilesExtractPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - EligibilityProfilesExtractPVO
  - eligibilityprofilesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibilityProfilesExtractPVO

## 📌 Visão Geral

Extrai perfis de elegibilidade de benefícios com critérios detalhados de qualificação. Fundamental para automação das regras de acesso a planos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.EligibilityProfilesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 96 | 1 | 1 | 96 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_eligy_prfl|BEN_ELIGY_PRFL]] — 96 atributos (1 PKs, 96 BICC)

---

## ⚙️ Atributos

### [[ben_eligy_prfl|BEN_ELIGY_PRFL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AsgTypCd | ASG_TYP_CD | — | ✅ |
| 2 | AsmtToUseCd | ASMT_TO_USE_CD | — | ✅ |
| 3 | BnftCagrPrtnCd | BNFT_CAGR_PRTN_CD | — | ✅ |
| 4 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 5 | CntngPrtnEligPrflFlag | CNTNG_PRTN_ELIG_PRFL_FLAG | — | ✅ |
| 6 | CreatedBy | CREATED_BY | — | ✅ |
| 7 | CreationDate | CREATION_DATE | — | ✅ |
| 8 | Description | DESCRIPTION | — | ✅ |
| 9 | DpntCvgEligDetRl | DPNT_CVG_ELIG_DET_RL | — | ✅ |
| 10 | DpntCvrdInAnthrPlFlag | DPNT_CVRD_IN_ANTHR_PL_FLAG | — | ✅ |
| 11 | DpntDsgntCrntlyEnrldFlag | DPNT_DSGNT_CRNTLY_ENRLD_FLAG | — | ✅ |
| 12 | DpntMltryFlag | DPNT_MLTRY_FLAG | — | ✅ |
| 13 | DpntRlshpFlag | DPNT_RLSHP_FLAG | — | ✅ |
| 14 | DpntStudFlag | DPNT_STUD_FLAG | — | ✅ |
| 15 | EligAgeFlag | ELIG_AGE_FLAG | — | ✅ |
| 16 | EligAnthrPlFlag | ELIG_ANTHR_PL_FLAG | — | ✅ |
| 17 | EligAsntSetFlag | ELIG_ASNT_SET_FLAG | — | ✅ |
| 18 | EligBenftsGrpFlag | ELIG_BENFTS_GRP_FLAG | — | ✅ |
| 19 | EligBrgngUnitFlag | ELIG_BRGNG_UNIT_FLAG | — | ✅ |
| 20 | EligBuFlag | ELIG_BU_FLAG | — | ✅ |
| 21 | EligCbrQualdBnfFlag | ELIG_CBR_QUALD_BNF_FLAG | — | ✅ |
| 22 | EligCmbnAgeLosFlag | ELIG_CMBN_AGE_LOS_FLAG | — | ✅ |
| 23 | EligCompLvlFlag | ELIG_COMP_LVL_FLAG | — | ✅ |
| 24 | EligComptncyFlag | ELIG_COMPTNCY_FLAG | — | ✅ |
| 25 | EligCritValuesFlag | ELIG_CRIT_VALUES_FLAG | — | ✅ |
| 26 | EligDpntCvrdPgmFlag | ELIG_DPNT_CVRD_PGM_FLAG | — | ✅ |
| 27 | EligDpntCvrdPlFlag | ELIG_DPNT_CVRD_PL_FLAG | — | ✅ |
| 28 | EligDpntCvrdPlipFlag | ELIG_DPNT_CVRD_PLIP_FLAG | — | ✅ |
| 29 | EligDpntCvrdPtipFlag | ELIG_DPNT_CVRD_PTIP_FLAG | — | ✅ |
| 30 | EligDpntOthrPtipFlag | ELIG_DPNT_OTHR_PTIP_FLAG | — | ✅ |
| 31 | EligDsbldFlag | ELIG_DSBLD_FLAG | — | ✅ |
| 32 | EligDsbltyCtgFlag | ELIG_DSBLTY_CTG_FLAG | — | ✅ |
| 33 | EligDsbltyDgrFlag | ELIG_DSBLTY_DGR_FLAG | — | ✅ |
| 34 | EligDsbltyRsnFlag | ELIG_DSBLTY_RSN_FLAG | — | ✅ |
| 35 | EligEeStatFlag | ELIG_EE_STAT_FLAG | — | ✅ |
| 36 | EligEnrldOiplFlag | ELIG_ENRLD_OIPL_FLAG | — | ✅ |
| 37 | EligEnrldPgmFlag | ELIG_ENRLD_PGM_FLAG | — | ✅ |
| 38 | EligEnrldPlFlag | ELIG_ENRLD_PL_FLAG | — | ✅ |
| 39 | EligEnrldPlipFlag | ELIG_ENRLD_PLIP_FLAG | — | ✅ |
| 40 | EligEnrldPtipFlag | ELIG_ENRLD_PTIP_FLAG | — | ✅ |
| 41 | EligFlTmPtTmFlag | ELIG_FL_TM_PT_TM_FLAG | — | ✅ |
| 42 | EligGeoFlag | ELIG_GEO_FLAG | — | ✅ |
| 43 | EligGndrFlag | ELIG_GNDR_FLAG | — | ✅ |
| 44 | EligGrdFlag | ELIG_GRD_FLAG | — | ✅ |
| 45 | EligHiredtFlag | ELIG_HIREDT_FLAG | — | ✅ |
| 46 | EligHlthCvgFlag | ELIG_HLTH_CVG_FLAG | — | ✅ |
| 47 | EligHrlySlrdFlag | ELIG_HRLY_SLRD_FLAG | — | ✅ |
| 48 | EligHrsWkdFlag | ELIG_HRS_WKD_FLAG | — | ✅ |
| 49 | EligJobFlag | ELIG_JOB_FLAG | — | ✅ |
| 50 | EligJobfamFlag | ELIG_JOBFAM_FLAG | — | ✅ |
| 51 | EligJobfuncFlag | ELIG_JOBFUNC_FLAG | — | ✅ |
| 52 | EligLbrMmbrFlag | ELIG_LBR_MMBR_FLAG | — | ✅ |
| 53 | EligLglEntyFlag | ELIG_LGL_ENTY_FLAG | — | ✅ |
| 54 | EligLoaRsnFlag | ELIG_LOA_RSN_FLAG | — | ✅ |
| 55 | EligLosFlag | ELIG_LOS_FLAG | — | ✅ |
| 56 | EligLvgRsnFlag | ELIG_LVG_RSN_FLAG | — | ✅ |
| 57 | EligMgrFlag | ELIG_MGR_FLAG | — | ✅ |
| 58 | EligMrtlStsFlag | ELIG_MRTL_STS_FLAG | — | ✅ |
| 59 | EligNoOthrCvgFlag | ELIG_NO_OTHR_CVG_FLAG | — | ✅ |
| 60 | EligOptdMdcrFlag | ELIG_OPTD_MDCR_FLAG | — | ✅ |
| 61 | EligOrgUnitFlag | ELIG_ORG_UNIT_FLAG | — | ✅ |
| 62 | EligPctFlTmFlag | ELIG_PCT_FL_TM_FLAG | — | ✅ |
| 63 | EligPerTypFlag | ELIG_PER_TYP_FLAG | — | ✅ |
| 64 | EligPerfRtngFlag | ELIG_PERF_RTNG_FLAG | — | ✅ |
| 65 | EligPplGrpFlag | ELIG_PPL_GRP_FLAG | — | ✅ |
| 66 | EligPrbtnPerdFlag | ELIG_PRBTN_PERD_FLAG | — | ✅ |
| 67 | EligPrttPlFlag | ELIG_PRTT_PL_FLAG | — | ✅ |
| 68 | EligPstlCdFlag | ELIG_PSTL_CD_FLAG | — | ✅ |
| 69 | EligPstnFlag | ELIG_PSTN_FLAG | — | ✅ |
| 70 | EligPtipPrteFlag | ELIG_PTIP_PRTE_FLAG | — | ✅ |
| 71 | EligPyBssFlag | ELIG_PY_BSS_FLAG | — | ✅ |
| 72 | EligPyrlFlag | ELIG_PYRL_FLAG | — | ✅ |
| 73 | EligQuaInGrFlag | ELIG_QUA_IN_GR_FLAG | — | ✅ |
| 74 | EligQualTitlFlag | ELIG_QUAL_TITL_FLAG | — | ✅ |
| 75 | EligReligionFlag | ELIG_RELIGION_FLAG | — | ✅ |
| 76 | EligScheddHrsFlag | ELIG_SCHEDD_HRS_FLAG | — | ✅ |
| 77 | EligSpClngPrgPtFlag | ELIG_SP_CLNG_PRG_PT_FLAG | — | ✅ |
| 78 | EligSupplRoleFlag | ELIG_SUPPL_ROLE_FLAG | — | ✅ |
| 79 | EligSvcAreaFlag | ELIG_SVC_AREA_FLAG | — | ✅ |
| 80 | EligTbcoUseFlag | ELIG_TBCO_USE_FLAG | — | ✅ |
| 81 | EligTtlCvgVolFlag | ELIG_TTL_CVG_VOL_FLAG | — | ✅ |
| 82 | EligTtlPrttFlag | ELIG_TTL_PRTT_FLAG | — | ✅ |
| 83 | EligWkLocFlag | ELIG_WK_LOC_FLAG | — | ✅ |
| 84 | EligyPrflId | ELIGY_PRFL_ID | 🔑 | ✅ |
| 85 | EligyPrflRlFlag | ELIGY_PRFL_RL_FLAG | — | ✅ |
| 86 | ElpAttributeCategory | ELP_ATTRIBUTE_CATEGORY | — | ✅ |
| 87 | EndDate | END_DATE | — | ✅ |
| 88 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 89 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 90 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 91 | Name | NAME | — | ✅ |
| 92 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 93 | ProfileType | PROFILE_TYPE | — | ✅ |
| 94 | RegnId | REGN_ID | — | ✅ |
| 95 | StartDate | START_DATE | — | ✅ |
| 96 | StatCd | STAT_CD | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
