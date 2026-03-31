---
id: DOC-HCM-052
doc_type: system-doc
title: "BEN_PGM_F — Programas de Benefícios"
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
  - programas-beneficios
  - benefit-programs
aliases:
  - BEN_PGM_F
  - ben_pgm_f
  - programas-beneficios-hcm
  - benefit-programs
  - ben-pgm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PGM_F

## 📌 Visão Geral

Armazena os **programas de benefícios** que agrupam múltiplos planos em um programa coeso (ex.: Programa de Benefícios Executivos, Programa Flexível).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agrupamento de planos:** Organiza planos relacionados em programas.
- **Gestão integrada:** Permite gerenciar conjuntos de benefícios.
- **Elegibilidade programática:** Regras de elegibilidade a nível de programa.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PGM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de programas de benefícios
```sql
SELECT * FROM BEN_PGM_F
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Programas de Benefícios).

---

## 🔗 PVOs Relacionados

### [[programpvo|ProgramPVO]] (HCM · BICC: 56/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTY_REF_PERD_CD | ActyRefPerdCd | ✅ |
| ALWS_UNRSTRCTD_ENRT_FLAG | AlwsUnrstrctdEnrtFlag | ✅ |
| AUTO_ENRT_MTHD_RL | AutoEnrtMthdRl | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CONFIG_CHAR_1 | ConfigChar1 | ✅ |
| COORD_CVG_FOR_ALL_PLS_FLG | CoordCvgForAllPlsFlg | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DFLT_ELEMENT_TYPE_ID | DfltElementTypeId | — |
| DFLT_INPUT_VALUE_ID | DfltInputValueId | — |
| DFLT_PGM_FLAG | DfltPgmFlag | — |
| DFLT_STEP_CD | DfltStepCd | ✅ |
| DFLT_STEP_RL | DfltStepRl | — |
| DPNT_CVG_END_DT_CD | DpntCvgEndDtCd | ✅ |
| DPNT_CVG_END_DT_RL | DpntCvgEndDtRl | — |
| DPNT_CVG_STRT_DT_CD | DpntCvgStrtDtCd | ✅ |
| DPNT_CVG_STRT_DT_RL | DpntCvgStrtDtRl | — |
| DPNT_DSGN_LVL_CD | DpntDsgnLvlCd | ✅ |
| DPNT_DSGN_NO_CTFN_RQD_FLAG | DpntDsgnNoCtfnRqdFlag | ✅ |
| DRVBL_FCTR_APLS_RTS_FLAG | DrvblFctrAplsRtsFlag | ✅ |
| DRVBL_FCTR_DPNT_ELIG_FLAG | DrvblFctrDpntEligFlag | ✅ |
| DRVBL_FCTR_PRTN_ELIG_FLAG | DrvblFctrPrtnEligFlag | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| ELIG_APLS_FLAG | EligAplsFlag | ✅ |
| ENRT_CD | EnrtCd | ✅ |
| ENRT_CVG_END_DT_CD | EnrtCvgEndDtCd | ✅ |
| ENRT_CVG_END_DT_RL | EnrtCvgEndDtRl | — |
| ENRT_CVG_STRT_DT_CD | EnrtCvgStrtDtCd | ✅ |
| ENRT_CVG_STRT_DT_RL | EnrtCvgStrtDtRl | — |
| ENRT_INFO_RT_FREQ_CD | EnrtInfoRtFreqCd | ✅ |
| ENRT_MTHD_CD | EnrtMthdCd | ✅ |
| ENRT_RL | EnrtRl | — |
| GLOBAL_FLAG | GlobalFlag | ✅ |
| GSP_ALLOW_OVERRIDE_FLAG | GspAllowOverrideFlag | — |
| IVR_IDENT | IvrIdent | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATION_CODE | LegislationCode | — |
| LEGISLATION_SUBGROUP | LegislationSubgroup | ✅ |
| MX_DPNT_PCT_PRTT_LF_AMT | MxDpntPctPrttLfAmt | ✅ |
| MX_SPS_PCT_PRTT_LF_AMT | MxSpsPctPrttLfAmt | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_CVRD_CD | PerCvrdCd | ✅ |
| PGM_ATTRIBUTE1 | PgmAttribute1 | — |
| PGM_ATTRIBUTE10 | PgmAttribute10 | — |
| PGM_ATTRIBUTE11 | PgmAttribute11 | — |
| PGM_ATTRIBUTE12 | PgmAttribute12 | — |
| PGM_ATTRIBUTE13 | PgmAttribute13 | — |
| PGM_ATTRIBUTE14 | PgmAttribute14 | — |
| PGM_ATTRIBUTE15 | PgmAttribute15 | — |
| PGM_ATTRIBUTE16 | PgmAttribute16 | — |
| PGM_ATTRIBUTE17 | PgmAttribute17 | — |
| PGM_ATTRIBUTE18 | PgmAttribute18 | — |
| PGM_ATTRIBUTE19 | PgmAttribute19 | — |
| PGM_ATTRIBUTE2 | PgmAttribute2 | — |
| PGM_ATTRIBUTE20 | PgmAttribute20 | — |
| PGM_ATTRIBUTE21 | PgmAttribute21 | — |
| PGM_ATTRIBUTE22 | PgmAttribute22 | — |
| PGM_ATTRIBUTE23 | PgmAttribute23 | — |
| PGM_ATTRIBUTE24 | PgmAttribute24 | — |
| PGM_ATTRIBUTE25 | PgmAttribute25 | — |
| PGM_ATTRIBUTE26 | PgmAttribute26 | — |
| PGM_ATTRIBUTE27 | PgmAttribute27 | — |
| PGM_ATTRIBUTE28 | PgmAttribute28 | — |
| PGM_ATTRIBUTE29 | PgmAttribute29 | — |
| PGM_ATTRIBUTE3 | PgmAttribute3 | — |
| PGM_ATTRIBUTE30 | PgmAttribute30 | — |
| PGM_ATTRIBUTE4 | PgmAttribute4 | — |
| PGM_ATTRIBUTE5 | PgmAttribute5 | — |
| PGM_ATTRIBUTE6 | PgmAttribute6 | — |
| PGM_ATTRIBUTE7 | PgmAttribute7 | — |
| PGM_ATTRIBUTE8 | PgmAttribute8 | — |
| PGM_ATTRIBUTE9 | PgmAttribute9 | — |
| PGM_ATTRIBUTE_CATEGORY | PgmAttributeCategory | — |
| PGM_DESC | PgmDesc | ✅ |
| PGM_GRP_CD | PgmGrpCd | ✅ |
| PGM_ID | PgmId | ✅ |
| PGM_PRVDS_CR_FLAG | PgmPrvdsCrFlag | — |
| PGM_PRVDS_NO_AUTO_ENRT_FLAG | PgmPrvdsNoAutoEnrtFlag | ✅ |
| PGM_PRVDS_NO_DFLT_ENRT_FLAG | PgmPrvdsNoDfltEnrtFlag | ✅ |
| PGM_STAT_CD | PgmStatCd | ✅ |
| PGM_TYP_CD | PgmTypCd | ✅ |
| PGM_UOM | PgmUom | ✅ |
| PGM_USE_ALL_ASNTS_ELIG_FLAG | PgmUseAllAsntsEligFlag | ✅ |
| POE_LVL_CD | PoeLvlCd | ✅ |
| PRTN_ELIG_OVRID_ALWD_FLAG | PrtnEligOvridAlwdFlag | ✅ |
| PRTT_CHC_UNCRS_TRTMT_FLAG | PrttChcUncrsTrtmtFlag | — |
| RT_END_DT_CD | RtEndDtCd | ✅ |
| RT_END_DT_RL | RtEndDtRl | — |
| RT_STRT_DT_CD | RtStrtDtCd | ✅ |
| RT_STRT_DT_RL | RtStrtDtRl | — |
| SALARY_CALC_MTHD_CD | SalaryCalcMthdCd | ✅ |
| SALARY_CALC_MTHD_RL | SalaryCalcMthdRl | ✅ |
| SCORES_CALC_MTHD_CD | ScoresCalcMthdCd | ✅ |
| SCORES_CALC_RL | ScoresCalcRl | ✅ |
| SHORT_CODE | ShortCode | ✅ |
| SHORT_NAME | ShortName | ✅ |
| TRK_INELIG_PER_FLAG | TrkIneligPerFlag | ✅ |
| UPDATE_SALARY_CD | UpdateSalaryCd | ✅ |
| URL_REF_NAME | UrlRefName | ✅ |
| USE_MULTI_PAY_RATES_FLAG | UseMultiPayRatesFlag | — |
| USE_PROG_POINTS_FLAG | UseProgPointsFlag | — |
| USE_SCORES_CD | UseScoresCd | — |
| USE_VARIABLE_RATES_FLAG | UseVariableRatesFlag | — |
| USES_ALL_ASMTS_FOR_RTS_FLAG | UsesAllAsmtsForRtsFlag | ✅ |
| VRFY_FMLY_MMBR_CD | VrfyFmlyMmbrCd | ✅ |
| VRFY_FMLY_MMBR_RL | VrfyFmlyMmbrRl | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PGM_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benpgmf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
