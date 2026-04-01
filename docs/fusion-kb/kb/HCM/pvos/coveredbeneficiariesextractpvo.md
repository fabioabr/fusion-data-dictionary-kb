---
id: DOC-HCM-PVO-CoveredBeneficiariesExtractPVO
doc_type: system-doc
title: "CoveredBeneficiariesExtractPVO — PVO Human Capital Management"
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
  - CoveredBeneficiariesExtractPVO
  - coveredbeneficiariesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CoveredBeneficiariesExtractPVO

## 📌 Visão Geral

Extrai beneficiarios cobertos em planos de beneficios via BICC com instrucoes e valores. Suporta cargas analiticas de cobertura de beneficiarios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.CoveredBeneficiariesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 46 | 1 | 1 | 46 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_pl_bnf|BEN_PL_BNF]] — 46 atributos (1 PKs, 46 BICC)

---

## ⚙️ Atributos

### [[ben_pl_bnf|BEN_PL_BNF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddlInstrnTxt | ADDL_INSTRN_TXT | — | ✅ |
| 2 | AmtDsgdUom | AMT_DSGD_UOM | — | ✅ |
| 3 | AmtDsgdVal | AMT_DSGD_VAL | — | ✅ |
| 4 | BnfOvrd | BNF_OVRD | — | ✅ |
| 5 | BnfPersonId | BNF_PERSON_ID | — | ✅ |
| 6 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 7 | CntngtBnfsAlwdFlag | CNTNGT_BNFS_ALWD_FLAG | — | ✅ |
| 8 | CreatedBy | CREATED_BY | — | ✅ |
| 9 | CreationDate | CREATION_DATE | — | ✅ |
| 10 | CtfnReqdFlag | CTFN_REQD_FLAG | — | ✅ |
| 11 | CvrdAmt | CVRD_AMT | — | ✅ |
| 12 | CvrdCntngtAmt | CVRD_CNTNGT_AMT | — | ✅ |
| 13 | CvrdCntngtPercentage | CVRD_CNTNGT_PERCENTAGE | — | ✅ |
| 14 | CvrdFlag | CVRD_FLAG | — | ✅ |
| 15 | CvrdPercentage | CVRD_PERCENTAGE | — | ✅ |
| 16 | CvrdPrmryCntngntCd | CVRD_PRMRY_CNTNGNT_CD | — | ✅ |
| 17 | DsgnStrtDt | DSGN_STRT_DT | — | ✅ |
| 18 | DsgnThruDt | DSGN_THRU_DT | — | ✅ |
| 19 | EligPerElctblChcId | ELIG_PER_ELCTBL_CHC_ID | — | ✅ |
| 20 | EndedCvgThruDt | ENDED_CVG_THRU_DT | — | ✅ |
| 21 | EndedPerInLerId | ENDED_PER_IN_LER_ID | — | ✅ |
| 22 | EnrtBnftId | ENRT_BNFT_ID | — | ✅ |
| 23 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 24 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 25 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 30 | OrgnlOiplDsgnStrtDt | ORGNL_OIPL_DSGN_STRT_DT | — | ✅ |
| 31 | OrgnlPlanDsgnStrtDt | ORGNL_PLAN_DSGN_STRT_DT | — | ✅ |
| 32 | PbnAttributeCategory | PBN_ATTRIBUTE_CATEGORY | — | ✅ |
| 33 | PctDsgdNum | PCT_DSGD_NUM | — | ✅ |
| 34 | PerInLerId | PER_IN_LER_ID | — | ✅ |
| 35 | PlBnfId | PL_BNF_ID | 🔑 | ✅ |
| 36 | PrmryCntngntCd | PRMRY_CNTNGNT_CD | — | ✅ |
| 37 | ProgramAppName | PROGRAM_APP_NAME | — | ✅ |
| 38 | ProgramName | PROGRAM_NAME | — | ✅ |
| 39 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 40 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | ✅ |
| 41 | PrvsCvgStrtDt | PRVS_CVG_STRT_DT | — | ✅ |
| 42 | PrvsCvgThruDt | PRVS_CVG_THRU_DT | — | ✅ |
| 43 | RequestId | REQUEST_ID | — | ✅ |
| 44 | RlnshpCd | RLNSHP_CD | — | ✅ |
| 45 | SuspendFlag | SUSPEND_FLAG | — | ✅ |
| 46 | TteePersonId | TTEE_PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
