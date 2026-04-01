---
id: DOC-HCM-053
doc_type: system-doc
title: "BEN_PIL_ELCTBL_CHC_POPL — População de Escolhas Elegíveis"
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
  - escolhas-elegiveis
  - electable-choices
aliases:
  - BEN_PIL_ELCTBL_CHC_POPL
  - ben_pil_elctbl_chc_popl
  - escolhas-elegiveis-beneficios
  - electable-choices-population
  - ben-pil-elctbl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PIL_ELCTBL_CHC_POPL

## 📌 Visão Geral

Armazena a **população de escolhas elegíveis** durante um evento de inscrição. Lista todas as opções de benefício disponíveis para cada participante elegível.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Apresentação de opções:** Lista de planos/opções disponíveis para o participante.
- **Self-service:** Alimenta a tela de inscrição com opções válidas.
- **Histórico:** Registra quais opções foram apresentadas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PIL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de população de escolhas elegíveis
```sql
SELECT * FROM BEN_PIL_ELCTBL_CHC_POPL
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (População de Escolhas Elegíveis).

---

## 🔗 PVOs Relacionados

### [[benefitspersonelectspvo|BenefitsPersonElectsPVO]] (HCM · BICC: 104/104)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTY_REF_PERD_CD | ActyRefPerdCd | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| AUTO_ASND_DT | AutoAsndDt | ✅ |
| BDGT_ACC_CD | BdgtAccCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CBR_ELIG_PERD_END_DT | CbrEligPerdEndDt | ✅ |
| CBR_ELIG_PERD_STRT_DT | CbrEligPerdStrtDt | ✅ |
| CLS_ENRT_DT_TO_USE_CD | ClsEnrtDtToUseCd | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DFLT_ASND_DT | DfltAsndDt | ✅ |
| DFLT_ENRT_DT | DfltEnrtDt | ✅ |
| ELCNS_MADE_DT | ElcnsMadeDt | ✅ |
| ENRT_PERD_END_DT | EnrtPerdEndDt | ✅ |
| ENRT_PERD_ID | EnrtPerdId | ✅ |
| ENRT_PERD_STRT_DT | EnrtPerdStrtDt | ✅ |
| ENRT_TYP_CYCL_CD | EnrtTypCyclCd | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEE_RSN_ID | LeeRsnId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PEL_ATTRIBUTE1 | PelAttribute1 | ✅ |
| PEL_ATTRIBUTE10 | PelAttribute10 | ✅ |
| PEL_ATTRIBUTE11 | PelAttribute11 | ✅ |
| PEL_ATTRIBUTE12 | PelAttribute12 | ✅ |
| PEL_ATTRIBUTE13 | PelAttribute13 | ✅ |
| PEL_ATTRIBUTE14 | PelAttribute14 | ✅ |
| PEL_ATTRIBUTE15 | PelAttribute15 | ✅ |
| PEL_ATTRIBUTE16 | PelAttribute16 | ✅ |
| PEL_ATTRIBUTE17 | PelAttribute17 | ✅ |
| PEL_ATTRIBUTE18 | PelAttribute18 | ✅ |
| PEL_ATTRIBUTE19 | PelAttribute19 | ✅ |
| PEL_ATTRIBUTE2 | PelAttribute2 | ✅ |
| PEL_ATTRIBUTE20 | PelAttribute20 | ✅ |
| PEL_ATTRIBUTE21 | PelAttribute21 | ✅ |
| PEL_ATTRIBUTE22 | PelAttribute22 | ✅ |
| PEL_ATTRIBUTE23 | PelAttribute23 | ✅ |
| PEL_ATTRIBUTE24 | PelAttribute24 | ✅ |
| PEL_ATTRIBUTE25 | PelAttribute25 | ✅ |
| PEL_ATTRIBUTE26 | PelAttribute26 | ✅ |
| PEL_ATTRIBUTE27 | PelAttribute27 | ✅ |
| PEL_ATTRIBUTE28 | PelAttribute28 | ✅ |
| PEL_ATTRIBUTE29 | PelAttribute29 | ✅ |
| PEL_ATTRIBUTE3 | PelAttribute3 | ✅ |
| PEL_ATTRIBUTE30 | PelAttribute30 | ✅ |
| PEL_ATTRIBUTE4 | PelAttribute4 | ✅ |
| PEL_ATTRIBUTE5 | PelAttribute5 | ✅ |
| PEL_ATTRIBUTE6 | PelAttribute6 | ✅ |
| PEL_ATTRIBUTE7 | PelAttribute7 | ✅ |
| PEL_ATTRIBUTE8 | PelAttribute8 | ✅ |
| PEL_ATTRIBUTE9 | PelAttribute9 | ✅ |
| PEL_ATTRIBUTE_CATEGORY | PelAttributeCategory | ✅ |
| PEL_ATTRIBUTE_DATE1 | PelAttributeDate1 | ✅ |
| PEL_ATTRIBUTE_DATE10 | PelAttributeDate10 | ✅ |
| PEL_ATTRIBUTE_DATE11 | PelAttributeDate11 | ✅ |
| PEL_ATTRIBUTE_DATE12 | PelAttributeDate12 | ✅ |
| PEL_ATTRIBUTE_DATE13 | PelAttributeDate13 | ✅ |
| PEL_ATTRIBUTE_DATE14 | PelAttributeDate14 | ✅ |
| PEL_ATTRIBUTE_DATE15 | PelAttributeDate15 | ✅ |
| PEL_ATTRIBUTE_DATE2 | PelAttributeDate2 | ✅ |
| PEL_ATTRIBUTE_DATE3 | PelAttributeDate3 | ✅ |
| PEL_ATTRIBUTE_DATE4 | PelAttributeDate4 | ✅ |
| PEL_ATTRIBUTE_DATE5 | PelAttributeDate5 | ✅ |
| PEL_ATTRIBUTE_DATE6 | PelAttributeDate6 | ✅ |
| PEL_ATTRIBUTE_DATE7 | PelAttributeDate7 | ✅ |
| PEL_ATTRIBUTE_DATE8 | PelAttributeDate8 | ✅ |
| PEL_ATTRIBUTE_DATE9 | PelAttributeDate9 | ✅ |
| PEL_ATTRIBUTE_NUMBER1 | PelAttributeNumber1 | ✅ |
| PEL_ATTRIBUTE_NUMBER10 | PelAttributeNumber10 | ✅ |
| PEL_ATTRIBUTE_NUMBER11 | PelAttributeNumber11 | ✅ |
| PEL_ATTRIBUTE_NUMBER12 | PelAttributeNumber12 | ✅ |
| PEL_ATTRIBUTE_NUMBER13 | PelAttributeNumber13 | ✅ |
| PEL_ATTRIBUTE_NUMBER14 | PelAttributeNumber14 | ✅ |
| PEL_ATTRIBUTE_NUMBER15 | PelAttributeNumber15 | ✅ |
| PEL_ATTRIBUTE_NUMBER16 | PelAttributeNumber16 | ✅ |
| PEL_ATTRIBUTE_NUMBER17 | PelAttributeNumber17 | ✅ |
| PEL_ATTRIBUTE_NUMBER18 | PelAttributeNumber18 | ✅ |
| PEL_ATTRIBUTE_NUMBER19 | PelAttributeNumber19 | ✅ |
| PEL_ATTRIBUTE_NUMBER2 | PelAttributeNumber2 | ✅ |
| PEL_ATTRIBUTE_NUMBER20 | PelAttributeNumber20 | ✅ |
| PEL_ATTRIBUTE_NUMBER3 | PelAttributeNumber3 | ✅ |
| PEL_ATTRIBUTE_NUMBER4 | PelAttributeNumber4 | ✅ |
| PEL_ATTRIBUTE_NUMBER5 | PelAttributeNumber5 | ✅ |
| PEL_ATTRIBUTE_NUMBER6 | PelAttributeNumber6 | ✅ |
| PEL_ATTRIBUTE_NUMBER7 | PelAttributeNumber7 | ✅ |
| PEL_ATTRIBUTE_NUMBER8 | PelAttributeNumber8 | ✅ |
| PEL_ATTRIBUTE_NUMBER9 | PelAttributeNumber9 | ✅ |
| PER_IN_LER_ID | PerInLerId | ✅ |
| PGM_ID | PgmId | ✅ |
| PIL_ELCTBL_CHC_POPL_ID | PilElctblChcPoplId | ✅ |
| PIL_ELCTBL_POPL_STAT_CD | PilElctblPoplStatCd | ✅ |
| PL_ID | PlId | ✅ |
| POP_CD | PopCd | ✅ |
| PROCG_END_DT | ProcgEndDt | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| REINSTATE_CD | ReinstateCd | ✅ |
| REINSTATE_OVRDN_CD | ReinstateOvrdnCd | ✅ |
| REQUEST_ID | RequestId | ✅ |
| UOM | Uom | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PIL_ELCTBL_CHC_POPL](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benpil-elctblchcpopl.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
