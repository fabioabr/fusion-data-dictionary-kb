---
id: DOC-HCM-054
doc_type: system-doc
title: "BEN_PL_BNF — Beneficiários por Plano"
system: Oracle Fusion Cloud HCM
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
  - benefits
  - beneficiarios-plano
  - plan-beneficiary
aliases:
  - BEN_PL_BNF
  - ben_pl_bnf
  - beneficiarios-plano-beneficios
  - plan-beneficiary
  - ben-pl-bnf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PL_BNF

## 📌 Visão Geral

Armazena os **beneficiários designados** a nível de plano de benefício, com percentuais de distribuição.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Designação por plano:** Beneficiários específicos para cada plano.
- **Distribuição:** Percentuais e prioridades entre beneficiários.
- **Seguro de vida:** Primário vs. contingente.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Colaborador | [[per_all_people_f]] | 🟡 80% |
| 3 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 4 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 5 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 6 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (quando aplicável)

### Tabelas-filha (FK de saída)
- Consultar documentação Oracle para tabelas-filha específicas.

---

## 📎 Uso Típico

### Consulta de beneficiários por plano
```sql
SELECT * FROM BEN_PL_BNF
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Beneficiários por Plano).

---

## 🔗 PVOs Relacionados

### [[coveredbeneficiariesextractpvo|CoveredBeneficiariesExtractPVO]] (HCM · BICC: 46/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_INSTRN_TXT | AddlInstrnTxt | ✅ |
| AMT_DSGD_UOM | AmtDsgdUom | ✅ |
| AMT_DSGD_VAL | AmtDsgdVal | ✅ |
| BNF_OVRD | BnfOvrd | ✅ |
| BNF_PERSON_ID | BnfPersonId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CNTNGT_BNFS_ALWD_FLAG | CntngtBnfsAlwdFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CTFN_REQD_FLAG | CtfnReqdFlag | ✅ |
| CVRD_AMT | CvrdAmt | ✅ |
| CVRD_CNTNGT_AMT | CvrdCntngtAmt | ✅ |
| CVRD_CNTNGT_PERCENTAGE | CvrdCntngtPercentage | ✅ |
| CVRD_FLAG | CvrdFlag | ✅ |
| CVRD_PERCENTAGE | CvrdPercentage | ✅ |
| CVRD_PRMRY_CNTNGNT_CD | CvrdPrmryCntngntCd | ✅ |
| DSGN_STRT_DT | DsgnStrtDt | ✅ |
| DSGN_THRU_DT | DsgnThruDt | ✅ |
| ELIG_PER_ELCTBL_CHC_ID | EligPerElctblChcId | ✅ |
| ENDED_CVG_THRU_DT | EndedCvgThruDt | ✅ |
| ENDED_PER_IN_LER_ID | EndedPerInLerId | ✅ |
| ENRT_BNFT_ID | EnrtBnftId | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| ORGNL_OIPL_DSGN_STRT_DT | OrgnlOiplDsgnStrtDt | ✅ |
| ORGNL_PLAN_DSGN_STRT_DT | OrgnlPlanDsgnStrtDt | ✅ |
| PBN_ATTRIBUTE_CATEGORY | PbnAttributeCategory | ✅ |
| PCT_DSGD_NUM | PctDsgdNum | ✅ |
| PER_IN_LER_ID | PerInLerId | ✅ |
| PL_BNF_ID | PlBnfId | ✅ |
| PRMRY_CNTNGNT_CD | PrmryCntngntCd | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | ✅ |
| PRVS_CVG_STRT_DT | PrvsCvgStrtDt | ✅ |
| PRVS_CVG_THRU_DT | PrvsCvgThruDt | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RLNSHP_CD | RlnshpCd | ✅ |
| SUSPEND_FLAG | SuspendFlag | ✅ |
| TTEE_PERSON_ID | TteePersonId | ✅ |

### [[coveredbeneficiariespvo|CoveredBeneficiariesPVO]] (HCM · BICC: 29/141)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDL_INSTRN_TXT | CoveredBeneficiariesPEOAddlInstrnTxt | ✅ |
| AMT_DSGD_UOM | CoveredBeneficiariesPEOAmtDsgdUom | ✅ |
| AMT_DSGD_VAL | CoveredBeneficiariesPEOAmtDsgdVal | ✅ |
| BNF_OVRD | BnfOvrd | — |
| BNF_PERSON_ID | CoveredBeneficiariesPEOBnfPersonId | ✅ |
| BUSINESS_GROUP_ID | CoveredBeneficiariesPEOBusinessGroupId | — |
| CNTNGT_BNFS_ALWD_FLAG | CoveredBeneficiariesPEOCntngtBnfsAlwdFlag | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | — |
| CONFIG_CHAR_10 | ConfigChar10 | — |
| CONFIG_CHAR_2 | ConfigChar2 | — |
| CONFIG_CHAR_3 | ConfigChar3 | — |
| CONFIG_CHAR_4 | ConfigChar4 | — |
| CONFIG_CHAR_5 | ConfigChar5 | — |
| CONFIG_CHAR_6 | ConfigChar6 | — |
| CONFIG_CHAR_7 | ConfigChar7 | — |
| CONFIG_CHAR_8 | ConfigChar8 | — |
| CONFIG_CHAR_9 | ConfigChar9 | — |
| CONFIG_DATE_1 | ConfigDate1 | — |
| CONFIG_DATE_10 | ConfigDate10 | — |
| CONFIG_DATE_2 | ConfigDate2 | — |
| CONFIG_DATE_3 | ConfigDate3 | — |
| CONFIG_DATE_4 | ConfigDate4 | — |
| CONFIG_DATE_5 | ConfigDate5 | — |
| CONFIG_DATE_6 | ConfigDate6 | — |
| CONFIG_DATE_7 | ConfigDate7 | — |
| CONFIG_DATE_8 | ConfigDate8 | — |
| CONFIG_DATE_9 | ConfigDate9 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_10 | ConfigNum10 | — |
| CONFIG_NUM_2 | ConfigNum2 | — |
| CONFIG_NUM_3 | ConfigNum3 | — |
| CONFIG_NUM_4 | ConfigNum4 | — |
| CONFIG_NUM_5 | ConfigNum5 | — |
| CONFIG_NUM_6 | ConfigNum6 | — |
| CONFIG_NUM_7 | ConfigNum7 | — |
| CONFIG_NUM_8 | ConfigNum8 | — |
| CONFIG_NUM_9 | ConfigNum9 | — |
| CREATED_BY | CoveredBeneficiariesPEOCreatedBy | ✅ |
| CREATION_DATE | CoveredBeneficiariesPEOCreationDate | ✅ |
| CTFN_REQD_FLAG | CoveredBeneficiariesPEOCtfnReqdFlag | — |
| CVRD_AMT | CoveredBeneficiariesPEOCvrdAmt | ✅ |
| CVRD_CNTNGT_AMT | CoveredBeneficiariesPEOCvrdCntngtAmt | ✅ |
| CVRD_CNTNGT_PERCENTAGE | CoveredBeneficiariesPEOCvrdCntngtPercentage | ✅ |
| CVRD_FLAG | CoveredBeneficiariesPEOCvrdFlag | ✅ |
| CVRD_PERCENTAGE | CoveredBeneficiariesPEOCvrdPercentage | ✅ |
| CVRD_PRMRY_CNTNGNT_CD | CoveredBeneficiariesPEOCvrdPrmryCntngntCd | ✅ |
| DSGN_STRT_DT | CoveredBeneficiariesPEODsgnStrtDt | ✅ |
| DSGN_THRU_DT | CoveredBeneficiariesPEODsgnThruDt | ✅ |
| ELIG_PER_ELCTBL_CHC_ID | CoveredBeneficiariesPEOEligPerElctblChcId | — |
| ENDED_CVG_THRU_DT | CoveredBeneficiariesPEOEndedCvgThruDt | ✅ |
| ENDED_PER_IN_LER_ID | CoveredBeneficiariesPEOEndedPerInLerId | — |
| ENRT_BNFT_ID | CoveredBeneficiariesPEOEnrtBnftId | — |
| JOB_DEFINITION_NAME | CoveredBeneficiariesPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | CoveredBeneficiariesPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | CoveredBeneficiariesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CoveredBeneficiariesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CoveredBeneficiariesPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | CoveredBeneficiariesPEOObjectVersionNumber | — |
| ORGANIZATION_ID | CoveredBeneficiariesPEOOrganizationId | ✅ |
| ORGNL_OIPL_DSGN_STRT_DT | CoveredBeneficiariesPEOOrgnlOiplDsgnStrtDt | — |
| ORGNL_PLAN_DSGN_STRT_DT | CoveredBeneficiariesPEOOrgnlPlanDsgnStrtDt | — |
| PBN_ATTRIBUTE1 | CoveredBeneficiariesPEOPbnAttribute1 | — |
| PBN_ATTRIBUTE10 | CoveredBeneficiariesPEOPbnAttribute10 | — |
| PBN_ATTRIBUTE11 | CoveredBeneficiariesPEOPbnAttribute11 | — |
| PBN_ATTRIBUTE12 | CoveredBeneficiariesPEOPbnAttribute12 | — |
| PBN_ATTRIBUTE13 | CoveredBeneficiariesPEOPbnAttribute13 | — |
| PBN_ATTRIBUTE14 | CoveredBeneficiariesPEOPbnAttribute14 | — |
| PBN_ATTRIBUTE15 | CoveredBeneficiariesPEOPbnAttribute15 | — |
| PBN_ATTRIBUTE16 | CoveredBeneficiariesPEOPbnAttribute16 | — |
| PBN_ATTRIBUTE17 | CoveredBeneficiariesPEOPbnAttribute17 | — |
| PBN_ATTRIBUTE18 | CoveredBeneficiariesPEOPbnAttribute18 | — |
| PBN_ATTRIBUTE19 | CoveredBeneficiariesPEOPbnAttribute19 | — |
| PBN_ATTRIBUTE2 | CoveredBeneficiariesPEOPbnAttribute2 | — |
| PBN_ATTRIBUTE20 | CoveredBeneficiariesPEOPbnAttribute20 | — |
| PBN_ATTRIBUTE21 | CoveredBeneficiariesPEOPbnAttribute21 | — |
| PBN_ATTRIBUTE22 | CoveredBeneficiariesPEOPbnAttribute22 | — |
| PBN_ATTRIBUTE23 | CoveredBeneficiariesPEOPbnAttribute23 | — |
| PBN_ATTRIBUTE24 | CoveredBeneficiariesPEOPbnAttribute24 | — |
| PBN_ATTRIBUTE25 | CoveredBeneficiariesPEOPbnAttribute25 | — |
| PBN_ATTRIBUTE26 | CoveredBeneficiariesPEOPbnAttribute26 | — |
| PBN_ATTRIBUTE27 | CoveredBeneficiariesPEOPbnAttribute27 | — |
| PBN_ATTRIBUTE28 | CoveredBeneficiariesPEOPbnAttribute28 | — |
| PBN_ATTRIBUTE29 | CoveredBeneficiariesPEOPbnAttribute29 | — |
| PBN_ATTRIBUTE3 | CoveredBeneficiariesPEOPbnAttribute3 | — |
| PBN_ATTRIBUTE30 | CoveredBeneficiariesPEOPbnAttribute30 | — |
| PBN_ATTRIBUTE4 | CoveredBeneficiariesPEOPbnAttribute4 | — |
| PBN_ATTRIBUTE5 | CoveredBeneficiariesPEOPbnAttribute5 | — |
| PBN_ATTRIBUTE6 | CoveredBeneficiariesPEOPbnAttribute6 | — |
| PBN_ATTRIBUTE7 | CoveredBeneficiariesPEOPbnAttribute7 | — |
| PBN_ATTRIBUTE8 | CoveredBeneficiariesPEOPbnAttribute8 | — |
| PBN_ATTRIBUTE9 | CoveredBeneficiariesPEOPbnAttribute9 | — |
| PBN_ATTRIBUTE_CATEGORY | CoveredBeneficiariesPEOPbnAttributeCategory | — |
| PBN_ATTRIBUTE_DATE1 | CoveredBeneficiariesPEOPbnAttributeDate1 | — |
| PBN_ATTRIBUTE_DATE10 | CoveredBeneficiariesPEOPbnAttributeDate10 | — |
| PBN_ATTRIBUTE_DATE11 | CoveredBeneficiariesPEOPbnAttributeDate11 | — |
| PBN_ATTRIBUTE_DATE12 | CoveredBeneficiariesPEOPbnAttributeDate12 | — |
| PBN_ATTRIBUTE_DATE13 | CoveredBeneficiariesPEOPbnAttributeDate13 | — |
| PBN_ATTRIBUTE_DATE14 | CoveredBeneficiariesPEOPbnAttributeDate14 | — |
| PBN_ATTRIBUTE_DATE15 | CoveredBeneficiariesPEOPbnAttributeDate15 | — |
| PBN_ATTRIBUTE_DATE2 | CoveredBeneficiariesPEOPbnAttributeDate2 | — |
| PBN_ATTRIBUTE_DATE3 | CoveredBeneficiariesPEOPbnAttributeDate3 | — |
| PBN_ATTRIBUTE_DATE4 | CoveredBeneficiariesPEOPbnAttributeDate4 | — |
| PBN_ATTRIBUTE_DATE5 | CoveredBeneficiariesPEOPbnAttributeDate5 | — |
| PBN_ATTRIBUTE_DATE6 | CoveredBeneficiariesPEOPbnAttributeDate6 | — |
| PBN_ATTRIBUTE_DATE7 | CoveredBeneficiariesPEOPbnAttributeDate7 | — |
| PBN_ATTRIBUTE_DATE8 | CoveredBeneficiariesPEOPbnAttributeDate8 | — |
| PBN_ATTRIBUTE_DATE9 | CoveredBeneficiariesPEOPbnAttributeDate9 | — |
| PBN_ATTRIBUTE_NUMBER1 | CoveredBeneficiariesPEOPbnAttributeNumber1 | — |
| PBN_ATTRIBUTE_NUMBER10 | CoveredBeneficiariesPEOPbnAttributeNumber10 | — |
| PBN_ATTRIBUTE_NUMBER11 | CoveredBeneficiariesPEOPbnAttributeNumber11 | — |
| PBN_ATTRIBUTE_NUMBER12 | CoveredBeneficiariesPEOPbnAttributeNumber12 | — |
| PBN_ATTRIBUTE_NUMBER13 | CoveredBeneficiariesPEOPbnAttributeNumber13 | — |
| PBN_ATTRIBUTE_NUMBER14 | CoveredBeneficiariesPEOPbnAttributeNumber14 | — |
| PBN_ATTRIBUTE_NUMBER15 | CoveredBeneficiariesPEOPbnAttributeNumber15 | — |
| PBN_ATTRIBUTE_NUMBER16 | CoveredBeneficiariesPEOPbnAttributeNumber16 | — |
| PBN_ATTRIBUTE_NUMBER17 | CoveredBeneficiariesPEOPbnAttributeNumber17 | — |
| PBN_ATTRIBUTE_NUMBER18 | CoveredBeneficiariesPEOPbnAttributeNumber18 | — |
| PBN_ATTRIBUTE_NUMBER19 | CoveredBeneficiariesPEOPbnAttributeNumber19 | — |
| PBN_ATTRIBUTE_NUMBER2 | CoveredBeneficiariesPEOPbnAttributeNumber2 | — |
| PBN_ATTRIBUTE_NUMBER20 | CoveredBeneficiariesPEOPbnAttributeNumber20 | — |
| PBN_ATTRIBUTE_NUMBER3 | CoveredBeneficiariesPEOPbnAttributeNumber3 | — |
| PBN_ATTRIBUTE_NUMBER4 | CoveredBeneficiariesPEOPbnAttributeNumber4 | — |
| PBN_ATTRIBUTE_NUMBER5 | CoveredBeneficiariesPEOPbnAttributeNumber5 | — |
| PBN_ATTRIBUTE_NUMBER6 | CoveredBeneficiariesPEOPbnAttributeNumber6 | — |
| PBN_ATTRIBUTE_NUMBER7 | CoveredBeneficiariesPEOPbnAttributeNumber7 | — |
| PBN_ATTRIBUTE_NUMBER8 | CoveredBeneficiariesPEOPbnAttributeNumber8 | — |
| PBN_ATTRIBUTE_NUMBER9 | CoveredBeneficiariesPEOPbnAttributeNumber9 | — |
| PCT_DSGD_NUM | CoveredBeneficiariesPEOPctDsgdNum | ✅ |
| PER_IN_LER_ID | CoveredBeneficiariesPEOPerInLerId | — |
| PL_BNF_ID | CoveredBeneficiariesPEOPlBnfId | ✅ |
| PRMRY_CNTNGNT_CD | CoveredBeneficiariesPEOPrmryCntngntCd | ✅ |
| PROGRAM_APP_NAME | CoveredBeneficiariesPEOProgramAppName | — |
| PROGRAM_NAME | CoveredBeneficiariesPEOProgramName | — |
| PROGRAM_UPDATE_DATE | CoveredBeneficiariesPEOProgramUpdateDate | — |
| PRTT_ENRT_RSLT_ID | CoveredBeneficiariesPEOPrttEnrtRsltId | ✅ |
| PRVS_CVG_STRT_DT | CoveredBeneficiariesPEOPrvsCvgStrtDt | ✅ |
| PRVS_CVG_THRU_DT | CoveredBeneficiariesPEOPrvsCvgThruDt | ✅ |
| REQUEST_ID | CoveredBeneficiariesPEORequestId | — |
| RLNSHP_CD | CoveredBeneficiariesPEORlnshpCd | ✅ |
| SUSPEND_FLAG | CoveredBeneficiariesPEOSuspendFlag | ✅ |
| TTEE_PERSON_ID | CoveredBeneficiariesPEOTteePersonId | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PL_BNF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benplbnf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
