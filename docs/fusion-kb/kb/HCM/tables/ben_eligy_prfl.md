---
id: DOC-HCM-038
doc_type: system-doc
title: "BEN_ELIGY_PRFL — Perfis de Elegibilidade de Benefícios"
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
  - elegibilidade
  - eligibility-profile
aliases:
  - BEN_ELIGY_PRFL
  - ben_eligy_prfl
  - perfil-elegibilidade-beneficios
  - eligibility-profile
  - ben-eligy-prfl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ELIGY_PRFL

## 📌 Visão Geral

Armazena os **perfis de elegibilidade** que definem critérios para participação em planos de benefícios (ex.: idade, tempo de serviço, cargo, grupo).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Regras de elegibilidade:** Define quem pode participar de cada plano.
- **Automação:** Avaliação automática de elegibilidade durante eventos de vida.
- **Configuração flexível:** Critérios combinaveis por perfil.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_ELIGY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de perfis de elegibilidade de benefícios
```sql
SELECT * FROM BEN_ELIGY_PRFL
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Perfis de Elegibilidade de Benefícios).

---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ELIGY_PRFL_ID | EligibilityProfilePEO1EligyPrflId | — |
| ELIGY_PRFL_ID | EligibilityProfilePEOEligyPrflId | — |
| NAME | EligibilityProfilePEO1Name | ✅ |
| NAME | EligibilityProfilePEOName | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ELIGY_PRFL_ID | EligibilityProfilePEOEligyPrflId | — |
| NAME | EligibilityProfilePEOName | ✅ |

### [[eligibilityprofilesextractpvo|EligibilityProfilesExtractPVO]] (HCM · BICC: 96/96)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASG_TYP_CD | AsgTypCd | ✅ |
| ASMT_TO_USE_CD | AsmtToUseCd | ✅ |
| BNFT_CAGR_PRTN_CD | BnftCagrPrtnCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CNTNG_PRTN_ELIG_PRFL_FLAG | CntngPrtnEligPrflFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| DPNT_CVG_ELIG_DET_RL | DpntCvgEligDetRl | ✅ |
| DPNT_CVRD_IN_ANTHR_PL_FLAG | DpntCvrdInAnthrPlFlag | ✅ |
| DPNT_DSGNT_CRNTLY_ENRLD_FLAG | DpntDsgntCrntlyEnrldFlag | ✅ |
| DPNT_MLTRY_FLAG | DpntMltryFlag | ✅ |
| DPNT_RLSHP_FLAG | DpntRlshpFlag | ✅ |
| DPNT_STUD_FLAG | DpntStudFlag | ✅ |
| ELIG_AGE_FLAG | EligAgeFlag | ✅ |
| ELIG_ANTHR_PL_FLAG | EligAnthrPlFlag | ✅ |
| ELIG_ASNT_SET_FLAG | EligAsntSetFlag | ✅ |
| ELIG_BENFTS_GRP_FLAG | EligBenftsGrpFlag | ✅ |
| ELIG_BRGNG_UNIT_FLAG | EligBrgngUnitFlag | ✅ |
| ELIG_BU_FLAG | EligBuFlag | ✅ |
| ELIG_CBR_QUALD_BNF_FLAG | EligCbrQualdBnfFlag | ✅ |
| ELIG_CMBN_AGE_LOS_FLAG | EligCmbnAgeLosFlag | ✅ |
| ELIG_COMP_LVL_FLAG | EligCompLvlFlag | ✅ |
| ELIG_COMPTNCY_FLAG | EligComptncyFlag | ✅ |
| ELIG_CRIT_VALUES_FLAG | EligCritValuesFlag | ✅ |
| ELIG_DPNT_CVRD_PGM_FLAG | EligDpntCvrdPgmFlag | ✅ |
| ELIG_DPNT_CVRD_PL_FLAG | EligDpntCvrdPlFlag | ✅ |
| ELIG_DPNT_CVRD_PLIP_FLAG | EligDpntCvrdPlipFlag | ✅ |
| ELIG_DPNT_CVRD_PTIP_FLAG | EligDpntCvrdPtipFlag | ✅ |
| ELIG_DPNT_OTHR_PTIP_FLAG | EligDpntOthrPtipFlag | ✅ |
| ELIG_DSBLD_FLAG | EligDsbldFlag | ✅ |
| ELIG_DSBLTY_CTG_FLAG | EligDsbltyCtgFlag | ✅ |
| ELIG_DSBLTY_DGR_FLAG | EligDsbltyDgrFlag | ✅ |
| ELIG_DSBLTY_RSN_FLAG | EligDsbltyRsnFlag | ✅ |
| ELIG_EE_STAT_FLAG | EligEeStatFlag | ✅ |
| ELIG_ENRLD_OIPL_FLAG | EligEnrldOiplFlag | ✅ |
| ELIG_ENRLD_PGM_FLAG | EligEnrldPgmFlag | ✅ |
| ELIG_ENRLD_PL_FLAG | EligEnrldPlFlag | ✅ |
| ELIG_ENRLD_PLIP_FLAG | EligEnrldPlipFlag | ✅ |
| ELIG_ENRLD_PTIP_FLAG | EligEnrldPtipFlag | ✅ |
| ELIG_FL_TM_PT_TM_FLAG | EligFlTmPtTmFlag | ✅ |
| ELIG_GEO_FLAG | EligGeoFlag | ✅ |
| ELIG_GNDR_FLAG | EligGndrFlag | ✅ |
| ELIG_GRD_FLAG | EligGrdFlag | ✅ |
| ELIG_HIREDT_FLAG | EligHiredtFlag | ✅ |
| ELIG_HLTH_CVG_FLAG | EligHlthCvgFlag | ✅ |
| ELIG_HRLY_SLRD_FLAG | EligHrlySlrdFlag | ✅ |
| ELIG_HRS_WKD_FLAG | EligHrsWkdFlag | ✅ |
| ELIG_JOB_FLAG | EligJobFlag | ✅ |
| ELIG_JOBFAM_FLAG | EligJobfamFlag | ✅ |
| ELIG_JOBFUNC_FLAG | EligJobfuncFlag | ✅ |
| ELIG_LBR_MMBR_FLAG | EligLbrMmbrFlag | ✅ |
| ELIG_LGL_ENTY_FLAG | EligLglEntyFlag | ✅ |
| ELIG_LOA_RSN_FLAG | EligLoaRsnFlag | ✅ |
| ELIG_LOS_FLAG | EligLosFlag | ✅ |
| ELIG_LVG_RSN_FLAG | EligLvgRsnFlag | ✅ |
| ELIG_MGR_FLAG | EligMgrFlag | ✅ |
| ELIG_MRTL_STS_FLAG | EligMrtlStsFlag | ✅ |
| ELIG_NO_OTHR_CVG_FLAG | EligNoOthrCvgFlag | ✅ |
| ELIG_OPTD_MDCR_FLAG | EligOptdMdcrFlag | ✅ |
| ELIG_ORG_UNIT_FLAG | EligOrgUnitFlag | ✅ |
| ELIG_PCT_FL_TM_FLAG | EligPctFlTmFlag | ✅ |
| ELIG_PER_TYP_FLAG | EligPerTypFlag | ✅ |
| ELIG_PERF_RTNG_FLAG | EligPerfRtngFlag | ✅ |
| ELIG_PPL_GRP_FLAG | EligPplGrpFlag | ✅ |
| ELIG_PRBTN_PERD_FLAG | EligPrbtnPerdFlag | ✅ |
| ELIG_PRTT_PL_FLAG | EligPrttPlFlag | ✅ |
| ELIG_PSTL_CD_FLAG | EligPstlCdFlag | ✅ |
| ELIG_PSTN_FLAG | EligPstnFlag | ✅ |
| ELIG_PTIP_PRTE_FLAG | EligPtipPrteFlag | ✅ |
| ELIG_PY_BSS_FLAG | EligPyBssFlag | ✅ |
| ELIG_PYRL_FLAG | EligPyrlFlag | ✅ |
| ELIG_QUA_IN_GR_FLAG | EligQuaInGrFlag | ✅ |
| ELIG_QUAL_TITL_FLAG | EligQualTitlFlag | ✅ |
| ELIG_RELIGION_FLAG | EligReligionFlag | ✅ |
| ELIG_SCHEDD_HRS_FLAG | EligScheddHrsFlag | ✅ |
| ELIG_SP_CLNG_PRG_PT_FLAG | EligSpClngPrgPtFlag | ✅ |
| ELIG_SUPPL_ROLE_FLAG | EligSupplRoleFlag | ✅ |
| ELIG_SVC_AREA_FLAG | EligSvcAreaFlag | ✅ |
| ELIG_TBCO_USE_FLAG | EligTbcoUseFlag | ✅ |
| ELIG_TTL_CVG_VOL_FLAG | EligTtlCvgVolFlag | ✅ |
| ELIG_TTL_PRTT_FLAG | EligTtlPrttFlag | ✅ |
| ELIG_WK_LOC_FLAG | EligWkLocFlag | ✅ |
| ELIGY_PRFL_ID | EligyPrflId | ✅ |
| ELIGY_PRFL_RL_FLAG | EligyPrflRlFlag | ✅ |
| ELP_ATTRIBUTE_CATEGORY | ElpAttributeCategory | ✅ |
| END_DATE | EndDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PROFILE_TYPE | ProfileType | ✅ |
| REGN_ID | RegnId | ✅ |
| START_DATE | StartDate | ✅ |
| STAT_CD | StatCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_ELIGY_PRFL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/beneligyprfl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
