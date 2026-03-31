---
id: DOC-OTHER-PVO-EnrollmentResultsExtractPVO
doc_type: system-doc
title: "EnrollmentResultsExtractPVO — PVO Cross-Module"
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
  - EnrollmentResultsExtractPVO
  - enrollmentresultsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EnrollmentResultsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Enrollment Results Extract. Acessa as tabelas: BEN_PRTT_ENRT_RSLT.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.EnrollmentResultsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 63 | 1 | 1 | 63 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]] — 63 atributos (1 PKs, 63 BICC)

---

## ⚙️ Atributos

### [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminCategoryCd | ADMIN_CATEGORY_CD | — | ✅ |
| 2 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | BenefitRelationId | BENEFIT_RELATION_ID | — | ✅ |
| 4 | BnftAmt | BNFT_AMT | — | ✅ |
| 5 | BnftNnmntryUom | BNFT_NNMNTRY_UOM | — | ✅ |
| 6 | BnftOrdrNum | BNFT_ORDR_NUM | — | ✅ |
| 7 | BnftTypCd | BNFT_TYP_CD | — | ✅ |
| 8 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 9 | CirBenefitId | CIR_BENEFIT_ID | — | ✅ |
| 10 | CompLvlCd | COMP_LVL_CD | — | ✅ |
| 11 | CreatedBy | CREATED_BY | — | ✅ |
| 12 | CreationDate | CREATION_DATE | — | ✅ |
| 13 | ElectionDate | ELECTION_DATE | — | ✅ |
| 14 | EndedCvgThruDt | ENDED_CVG_THRU_DT | — | ✅ |
| 15 | EndedPerInLerId | ENDED_PER_IN_LER_ID | — | ✅ |
| 16 | EnrtCvgStrtDt | ENRT_CVG_STRT_DT | — | ✅ |
| 17 | EnrtCvgThruDt | ENRT_CVG_THRU_DT | — | ✅ |
| 18 | EnrtMthdCd | ENRT_MTHD_CD | — | ✅ |
| 19 | EnrtOvridRsnCd | ENRT_OVRID_RSN_CD | — | ✅ |
| 20 | EnrtOvridThruDt | ENRT_OVRID_THRU_DT | — | ✅ |
| 21 | EnrtOvridnFlag | ENRT_OVRIDN_FLAG | — | ✅ |
| 22 | ErlstDeenrtDt | ERLST_DEENRT_DT | — | ✅ |
| 23 | ImptdIncmCalcCd | IMPTD_INCM_CALC_CD | — | ✅ |
| 24 | InterimFlag | INTERIM_FLAG | — | ✅ |
| 25 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 26 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 27 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 28 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 29 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 30 | LegalEntityId | LEGAL_ENTITY_ID | — | ✅ |
| 31 | LerId | LER_ID | — | ✅ |
| 32 | MiscPlnFlag | MISC_PLN_FLAG | — | ✅ |
| 33 | NoLngrEligFlag | NO_LNGR_ELIG_FLAG | — | ✅ |
| 34 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | OiplId | OIPL_ID | — | ✅ |
| 36 | OiplOrdrNum | OIPL_ORDR_NUM | — | ✅ |
| 37 | OptId | OPT_ID | — | ✅ |
| 38 | OrgnlEnrtDt | ORGNL_ENRT_DT | — | ✅ |
| 39 | PerInLerId | PER_IN_LER_ID | — | ✅ |
| 40 | PersonId | PERSON_ID | — | ✅ |
| 41 | PgmId | PGM_ID | — | ✅ |
| 42 | PlId | PL_ID | — | ✅ |
| 43 | PlOrdrNum | PL_ORDR_NUM | — | ✅ |
| 44 | PlTypId | PL_TYP_ID | — | ✅ |
| 45 | PlipOrdrNum | PLIP_ORDR_NUM | — | ✅ |
| 46 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 47 | ProgramName | PROGRAM_NAME | — | ✅ |
| 48 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 49 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | 🔑 | ✅ |
| 50 | PrttEnrtRsltStatCd | PRTT_ENRT_RSLT_STAT_CD | — | ✅ |
| 51 | PrttIsCvrdFlag | PRTT_IS_CVRD_FLAG | — | ✅ |
| 52 | PrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | ✅ |
| 53 | PrvsCvgThruDt | PRVS_CVG_THRU_DT | — | ✅ |
| 54 | PrvsSspnddFlag | PRVS_SSPNDD_FLAG | — | ✅ |
| 55 | PtipId | PTIP_ID | — | ✅ |
| 56 | PtipOrdrNum | PTIP_ORDR_NUM | — | ✅ |
| 57 | RequestId | REQUEST_ID | — | ✅ |
| 58 | RplcsSspnddRsltId | RPLCS_SSPNDD_RSLT_ID | — | ✅ |
| 59 | SsCategoryCd | SS_CATEGORY_CD | — | ✅ |
| 60 | SspnddFlag | SSPNDD_FLAG | — | ✅ |
| 61 | SvngsPlnFlag | SVNGS_PLN_FLAG | — | ✅ |
| 62 | TypeId | TYPE_ID | — | ✅ |
| 63 | Uom | UOM | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
