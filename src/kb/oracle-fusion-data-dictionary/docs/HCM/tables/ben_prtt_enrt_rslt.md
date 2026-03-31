---
id: DOC-HCM-061
doc_type: system-doc
title: "BEN_PRTT_ENRT_RSLT — Resultados de Inscrição de Participante"
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
  - resultados-inscricao
  - enrollment-results
  - inscricao
aliases:
  - BEN_PRTT_ENRT_RSLT
  - ben_prtt_enrt_rslt
  - resultados-inscricao-beneficios
  - enrollment-results
  - ben-prtt-enrt-rslt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRTT_ENRT_RSLT

## 📌 Visão Geral

Armazena os **resultados de inscrição** em planos de benefício. Cada registro representa a inscrição efetiva de um participante em um plano/opção específica. É a **tabela transacional principal** do módulo Benefits.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inscrições ativas:** Tabela central de inscrições em benefícios.
- **Histórico de cobertura:** Registra início/fim de cada inscrição.
- **Integração com folha:** Base para deduções de benefícios.
- **Self-service:** Alimenta a visão de benefícios do colaborador.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PRTT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de resultados de inscrição de participante
```sql
SELECT * FROM BEN_PRTT_ENRT_RSLT
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Resultados de Inscrição de Participante).

---

## 🔗 PVOs Relacionados

### [[enrollmentresultsextractpvo|EnrollmentResultsExtractPVO]] (HCM · BICC: 63/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADMIN_CATEGORY_CD | AdminCategoryCd | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| BENEFIT_RELATION_ID | BenefitRelationId | ✅ |
| BNFT_AMT | BnftAmt | ✅ |
| BNFT_NNMNTRY_UOM | BnftNnmntryUom | ✅ |
| BNFT_ORDR_NUM | BnftOrdrNum | ✅ |
| BNFT_TYP_CD | BnftTypCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CIR_BENEFIT_ID | CirBenefitId | ✅ |
| COMP_LVL_CD | CompLvlCd | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ELECTION_DATE | ElectionDate | ✅ |
| ENDED_CVG_THRU_DT | EndedCvgThruDt | ✅ |
| ENDED_PER_IN_LER_ID | EndedPerInLerId | ✅ |
| ENRT_CVG_STRT_DT | EnrtCvgStrtDt | ✅ |
| ENRT_CVG_THRU_DT | EnrtCvgThruDt | ✅ |
| ENRT_MTHD_CD | EnrtMthdCd | ✅ |
| ENRT_OVRID_RSN_CD | EnrtOvridRsnCd | ✅ |
| ENRT_OVRID_THRU_DT | EnrtOvridThruDt | ✅ |
| ENRT_OVRIDN_FLAG | EnrtOvridnFlag | ✅ |
| ERLST_DEENRT_DT | ErlstDeenrtDt | ✅ |
| IMPTD_INCM_CALC_CD | ImptdIncmCalcCd | ✅ |
| INTERIM_FLAG | InterimFlag | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LER_ID | LerId | ✅ |
| MISC_PLN_FLAG | MiscPlnFlag | ✅ |
| NO_LNGR_ELIG_FLAG | NoLngrEligFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OIPL_ID | OiplId | ✅ |
| OIPL_ORDR_NUM | OiplOrdrNum | ✅ |
| OPT_ID | OptId | ✅ |
| ORGNL_ENRT_DT | OrgnlEnrtDt | ✅ |
| PER_IN_LER_ID | PerInLerId | ✅ |
| PERSON_ID | PersonId | ✅ |
| PGM_ID | PgmId | ✅ |
| PL_ID | PlId | ✅ |
| PL_ORDR_NUM | PlOrdrNum | ✅ |
| PL_TYP_ID | PlTypId | ✅ |
| PLIP_ORDR_NUM | PlipOrdrNum | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | ✅ |
| PRTT_ENRT_RSLT_STAT_CD | PrttEnrtRsltStatCd | ✅ |
| PRTT_IS_CVRD_FLAG | PrttIsCvrdFlag | ✅ |
| PRVS_CVG_STRT_DT | PrvsCvgStrtDt | ✅ |
| PRVS_CVG_THRU_DT | PrvsCvgThruDt | ✅ |
| PRVS_SSPNDD_FLAG | PrvsSspnddFlag | ✅ |
| PTIP_ID | PtipId | ✅ |
| PTIP_ORDR_NUM | PtipOrdrNum | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RPLCS_SSPNDD_RSLT_ID | RplcsSspnddRsltId | ✅ |
| SS_CATEGORY_CD | SsCategoryCd | ✅ |
| SSPNDD_FLAG | SspnddFlag | ✅ |
| SVNGS_PLN_FLAG | SvngsPlnFlag | ✅ |
| TYPE_ID | TypeId | ✅ |
| UOM | Uom | ✅ |

### [[participantenrollmentpvo|ParticipantEnrollmentPVO]] (HCM · BICC: 39/111)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADMIN_CATEGORY_CD | AdminCategoryCd | — |
| ASSIGNMENT_ID | AssignmentId | — |
| BENEFIT_RELATION_ID | BenefitRelationId | — |
| BNFT_AMT | BnftAmt | ✅ |
| BNFT_NNMNTRY_UOM | BnftNnmntryUom | ✅ |
| BNFT_ORDR_NUM | BnftOrdrNum | ✅ |
| BNFT_TYP_CD | BnftTypCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CIR_BENEFIT_ID | CirBenefitId | — |
| COMP_LVL_CD | CompLvlCd | ✅ |
| CONFIG_CHAR_1 | ConfigChar1 | ✅ |
| CONFIG_CHAR_10 | ConfigChar10 | — |
| CONFIG_CHAR_6 | ConfigChar6 | — |
| CONFIG_CHAR_7 | ConfigChar7 | — |
| CONFIG_CHAR_8 | ConfigChar8 | — |
| CONFIG_CHAR_9 | ConfigChar9 | — |
| CONFIG_ID_1 | ConfigId1 | — |
| CONFIG_ID_2 | ConfigId2 | — |
| CONFIG_ID_3 | ConfigId3 | — |
| CONFIG_ID_4 | ConfigId4 | — |
| CONFIG_ID_5 | ConfigId5 | — |
| CONFIG_NUM_1 | ConfigNum1 | — |
| CONFIG_NUM_10 | ConfigNum10 | — |
| CONFIG_NUM_6 | ConfigNum6 | — |
| CONFIG_NUM_7 | ConfigNum7 | — |
| CONFIG_NUM_8 | ConfigNum8 | — |
| CONFIG_NUM_9 | ConfigNum9 | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ELECTION_DATE | ElectionDate | ✅ |
| ENDED_CVG_THRU_DT | EndedCvgThruDt | — |
| ENDED_PER_IN_LER_ID | EndedPerInLerId | — |
| ENRT_CVG_STRT_DT | EnrtCvgStrtDt | ✅ |
| ENRT_CVG_THRU_DT | EnrtCvgThruDt | ✅ |
| ENRT_MTHD_CD | EnrtMthdCd | ✅ |
| ENRT_OVRID_RSN_CD | EnrtOvridRsnCd | ✅ |
| ENRT_OVRID_THRU_DT | EnrtOvridThruDt | ✅ |
| ENRT_OVRIDN_FLAG | EnrtOvridnFlag | ✅ |
| ERLST_DEENRT_DT | ErlstDeenrtDt | ✅ |
| IMPTD_INCM_CALC_CD | ImptdIncmCalcCd | — |
| INTERIM_FLAG | InterimFlag | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LER_ID | LerId | — |
| MISC_PLN_FLAG | MiscPlnFlag | ✅ |
| NO_LNGR_ELIG_FLAG | NoLngrEligFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OIPL_ID | OiplId | — |
| OIPL_ORDR_NUM | OiplOrdrNum | ✅ |
| OPT_ID | OptId | — |
| ORGNL_ENRT_DT | OrgnlEnrtDt | ✅ |
| PEN_ATTRIBUTE1 | PenAttribute1 | — |
| PEN_ATTRIBUTE10 | PenAttribute10 | — |
| PEN_ATTRIBUTE11 | PenAttribute11 | — |
| PEN_ATTRIBUTE12 | PenAttribute12 | — |
| PEN_ATTRIBUTE13 | PenAttribute13 | — |
| PEN_ATTRIBUTE14 | PenAttribute14 | — |
| PEN_ATTRIBUTE15 | PenAttribute15 | — |
| PEN_ATTRIBUTE16 | PenAttribute16 | — |
| PEN_ATTRIBUTE17 | PenAttribute17 | — |
| PEN_ATTRIBUTE18 | PenAttribute18 | — |
| PEN_ATTRIBUTE19 | PenAttribute19 | — |
| PEN_ATTRIBUTE2 | PenAttribute2 | — |
| PEN_ATTRIBUTE20 | PenAttribute20 | — |
| PEN_ATTRIBUTE21 | PenAttribute21 | — |
| PEN_ATTRIBUTE22 | PenAttribute22 | — |
| PEN_ATTRIBUTE23 | PenAttribute23 | — |
| PEN_ATTRIBUTE24 | PenAttribute24 | — |
| PEN_ATTRIBUTE25 | PenAttribute25 | — |
| PEN_ATTRIBUTE26 | PenAttribute26 | — |
| PEN_ATTRIBUTE27 | PenAttribute27 | — |
| PEN_ATTRIBUTE28 | PenAttribute28 | — |
| PEN_ATTRIBUTE29 | PenAttribute29 | — |
| PEN_ATTRIBUTE3 | PenAttribute3 | — |
| PEN_ATTRIBUTE30 | PenAttribute30 | — |
| PEN_ATTRIBUTE4 | PenAttribute4 | — |
| PEN_ATTRIBUTE5 | PenAttribute5 | — |
| PEN_ATTRIBUTE6 | PenAttribute6 | — |
| PEN_ATTRIBUTE7 | PenAttribute7 | — |
| PEN_ATTRIBUTE8 | PenAttribute8 | — |
| PEN_ATTRIBUTE9 | PenAttribute9 | — |
| PEN_ATTRIBUTE_CATEGORY | PenAttributeCategory | — |
| PER_IN_LER_ID | PerInLerId | — |
| PERSON_ID | PersonId | ✅ |
| PGM_ID | PgmId | — |
| PL_ID | PlId | — |
| PL_ORDR_NUM | PlOrdrNum | ✅ |
| PL_TYP_ID | PlTypId | — |
| PLIP_ORDR_NUM | PlipOrdrNum | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | ✅ |
| PRTT_ENRT_RSLT_STAT_CD | PrttEnrtRsltStatCd | ✅ |
| PRTT_IS_CVRD_FLAG | PrttIsCvrdFlag | ✅ |
| PRVS_CVG_STRT_DT | PrvsCvgStrtDt | ✅ |
| PRVS_CVG_THRU_DT | PrvsCvgThruDt | ✅ |
| PRVS_SSPNDD_FLAG | PrvsSspnddFlag | ✅ |
| PTIP_ID | PtipId | — |
| PTIP_ORDR_NUM | PtipOrdrNum | — |
| REQUEST_ID | RequestId | — |
| RPLCS_SSPNDD_RSLT_ID | RplcsSspnddRsltId | — |
| SS_CATEGORY_CD | SsCategoryCd | — |
| SSPNDD_FLAG | SspnddFlag | ✅ |
| SVNGS_PLN_FLAG | SvngsPlnFlag | ✅ |
| TYPE_ID | TypeId | ✅ |
| UOM | Uom | ✅ |

### [[personenrollmentactionpvo|PersonEnrollmentActionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| OIPL_ID | OiplId | — |
| OPT_ID | OptId | — |
| PERSON_ID | PersonId | — |
| PGM_ID | PgmId | — |
| PL_ID | PlId | — |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId1 | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PRTT_ENRT_RSLT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprttenrtrslt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
