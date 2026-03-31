---
id: DOC-HCM-039
doc_type: system-doc
title: "BEN_ELIG_CVRD_DPNT — Dependentes Cobertos Elegíveis"
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
  - dependentes-cobertos
  - covered-dependents
aliases:
  - BEN_ELIG_CVRD_DPNT
  - ben_elig_cvrd_dpnt
  - dependentes-cobertos-beneficios
  - covered-dependents
  - ben-elig-cvrd-dpnt
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_ELIG_CVRD_DPNT

## 📌 Visão Geral

Armazena os **dependentes cobertos** por benefícios, vinculando dependentes elegíveis a inscrições de planos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cobertura de dependentes:** Registra quais dependentes estão cobertos por cada inscrição.
- **Gestão familiar:** Controle de dependentes por plano.
- **Compliance:** Atende regras de cobertura obrigatória.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_ELIG_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de dependentes cobertos elegíveis
```sql
SELECT * FROM BEN_ELIG_CVRD_DPNT
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Dependentes Cobertos Elegíveis).

---

## 🔗 PVOs Relacionados

### [[covereddependentspvo|CoveredDependentsPVO]] (HCM · BICC: 15/96)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | CoveredDependentsPEOBusinessGroupId | — |
| CREATED_BY | CoveredDependentsPEOCreatedBy | ✅ |
| CREATION_DATE | CoveredDependentsPEOCreationDate | ✅ |
| CVG_PNDG_FLAG | CoveredDependentsPEOCvgPndgFlag | ✅ |
| CVG_STRT_DT | CoveredDependentsPEOCvgStrtDt | ✅ |
| CVG_THRU_DT | CoveredDependentsPEOCvgThruDt | ✅ |
| DPNT_PERSON_ID | CoveredDependentsPEODpntPersonId | — |
| ELIG_CVRD_DPNT_ID | CoveredDependentsPEOEligCvrdDpntId | ✅ |
| ELIG_PER_ELCTBL_CHC_ID | CoveredDependentsPEOEligPerElctblChcId | — |
| ENDED_CVG_THRU_DT | CoveredDependentsPEOEndedCvgThruDt | ✅ |
| ENDED_PER_IN_LER_ID | CoveredDependentsPEOEndedPerInLerId | — |
| JOB_DEFINITION_NAME | CoveredDependentsPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | CoveredDependentsPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | CoveredDependentsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | CoveredDependentsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | CoveredDependentsPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | CoveredDependentsPEOObjectVersionNumber | — |
| ORGNL_OIPL_CVG_STRT_DT | CoveredDependentsPEOOrgnlOiplCvgStrtDt | ✅ |
| ORGNL_PLAN_CVG_STRT_DT | CoveredDependentsPEOOrgnlPlanCvgStrtDt | ✅ |
| OVRDN_FLAG | CoveredDependentsPEOOvrdnFlag | ✅ |
| OVRDN_THRU_DT | CoveredDependentsPEOOvrdnThruDt | ✅ |
| PDP_ATTRIBUTE1 | CoveredDependentsPEOPdpAttribute1 | — |
| PDP_ATTRIBUTE10 | CoveredDependentsPEOPdpAttribute10 | — |
| PDP_ATTRIBUTE11 | CoveredDependentsPEOPdpAttribute11 | — |
| PDP_ATTRIBUTE12 | CoveredDependentsPEOPdpAttribute12 | — |
| PDP_ATTRIBUTE13 | CoveredDependentsPEOPdpAttribute13 | — |
| PDP_ATTRIBUTE14 | CoveredDependentsPEOPdpAttribute14 | — |
| PDP_ATTRIBUTE15 | CoveredDependentsPEOPdpAttribute15 | — |
| PDP_ATTRIBUTE16 | CoveredDependentsPEOPdpAttribute16 | — |
| PDP_ATTRIBUTE17 | CoveredDependentsPEOPdpAttribute17 | — |
| PDP_ATTRIBUTE18 | CoveredDependentsPEOPdpAttribute18 | — |
| PDP_ATTRIBUTE19 | CoveredDependentsPEOPdpAttribute19 | — |
| PDP_ATTRIBUTE2 | CoveredDependentsPEOPdpAttribute2 | — |
| PDP_ATTRIBUTE20 | CoveredDependentsPEOPdpAttribute20 | — |
| PDP_ATTRIBUTE21 | CoveredDependentsPEOPdpAttribute21 | — |
| PDP_ATTRIBUTE22 | CoveredDependentsPEOPdpAttribute22 | — |
| PDP_ATTRIBUTE23 | CoveredDependentsPEOPdpAttribute23 | — |
| PDP_ATTRIBUTE24 | CoveredDependentsPEOPdpAttribute24 | — |
| PDP_ATTRIBUTE25 | CoveredDependentsPEOPdpAttribute25 | — |
| PDP_ATTRIBUTE26 | CoveredDependentsPEOPdpAttribute26 | — |
| PDP_ATTRIBUTE27 | CoveredDependentsPEOPdpAttribute27 | — |
| PDP_ATTRIBUTE28 | CoveredDependentsPEOPdpAttribute28 | — |
| PDP_ATTRIBUTE29 | CoveredDependentsPEOPdpAttribute29 | — |
| PDP_ATTRIBUTE3 | CoveredDependentsPEOPdpAttribute3 | — |
| PDP_ATTRIBUTE30 | CoveredDependentsPEOPdpAttribute30 | — |
| PDP_ATTRIBUTE4 | CoveredDependentsPEOPdpAttribute4 | — |
| PDP_ATTRIBUTE5 | CoveredDependentsPEOPdpAttribute5 | — |
| PDP_ATTRIBUTE6 | CoveredDependentsPEOPdpAttribute6 | — |
| PDP_ATTRIBUTE7 | CoveredDependentsPEOPdpAttribute7 | — |
| PDP_ATTRIBUTE8 | CoveredDependentsPEOPdpAttribute8 | — |
| PDP_ATTRIBUTE9 | CoveredDependentsPEOPdpAttribute9 | — |
| PDP_ATTRIBUTE_CATEGORY | CoveredDependentsPEOPdpAttributeCategory | — |
| PDP_ATTRIBUTE_DATE1 | CoveredDependentsPEOPdpAttributeDate1 | — |
| PDP_ATTRIBUTE_DATE10 | CoveredDependentsPEOPdpAttributeDate10 | — |
| PDP_ATTRIBUTE_DATE11 | CoveredDependentsPEOPdpAttributeDate11 | — |
| PDP_ATTRIBUTE_DATE12 | CoveredDependentsPEOPdpAttributeDate12 | — |
| PDP_ATTRIBUTE_DATE13 | CoveredDependentsPEOPdpAttributeDate13 | — |
| PDP_ATTRIBUTE_DATE14 | CoveredDependentsPEOPdpAttributeDate14 | — |
| PDP_ATTRIBUTE_DATE15 | CoveredDependentsPEOPdpAttributeDate15 | — |
| PDP_ATTRIBUTE_DATE2 | CoveredDependentsPEOPdpAttributeDate2 | — |
| PDP_ATTRIBUTE_DATE3 | CoveredDependentsPEOPdpAttributeDate3 | — |
| PDP_ATTRIBUTE_DATE4 | CoveredDependentsPEOPdpAttributeDate4 | — |
| PDP_ATTRIBUTE_DATE5 | CoveredDependentsPEOPdpAttributeDate5 | — |
| PDP_ATTRIBUTE_DATE6 | CoveredDependentsPEOPdpAttributeDate6 | — |
| PDP_ATTRIBUTE_DATE7 | CoveredDependentsPEOPdpAttributeDate7 | — |
| PDP_ATTRIBUTE_DATE8 | CoveredDependentsPEOPdpAttributeDate8 | — |
| PDP_ATTRIBUTE_DATE9 | CoveredDependentsPEOPdpAttributeDate9 | — |
| PDP_ATTRIBUTE_NUMBER1 | CoveredDependentsPEOPdpAttributeNumber1 | — |
| PDP_ATTRIBUTE_NUMBER10 | CoveredDependentsPEOPdpAttributeNumber10 | — |
| PDP_ATTRIBUTE_NUMBER11 | CoveredDependentsPEOPdpAttributeNumber11 | — |
| PDP_ATTRIBUTE_NUMBER12 | CoveredDependentsPEOPdpAttributeNumber12 | — |
| PDP_ATTRIBUTE_NUMBER13 | CoveredDependentsPEOPdpAttributeNumber13 | — |
| PDP_ATTRIBUTE_NUMBER14 | CoveredDependentsPEOPdpAttributeNumber14 | — |
| PDP_ATTRIBUTE_NUMBER15 | CoveredDependentsPEOPdpAttributeNumber15 | — |
| PDP_ATTRIBUTE_NUMBER16 | CoveredDependentsPEOPdpAttributeNumber16 | — |
| PDP_ATTRIBUTE_NUMBER17 | CoveredDependentsPEOPdpAttributeNumber17 | — |
| PDP_ATTRIBUTE_NUMBER18 | CoveredDependentsPEOPdpAttributeNumber18 | — |
| PDP_ATTRIBUTE_NUMBER19 | CoveredDependentsPEOPdpAttributeNumber19 | — |
| PDP_ATTRIBUTE_NUMBER2 | CoveredDependentsPEOPdpAttributeNumber2 | — |
| PDP_ATTRIBUTE_NUMBER20 | CoveredDependentsPEOPdpAttributeNumber20 | — |
| PDP_ATTRIBUTE_NUMBER3 | CoveredDependentsPEOPdpAttributeNumber3 | — |
| PDP_ATTRIBUTE_NUMBER4 | CoveredDependentsPEOPdpAttributeNumber4 | — |
| PDP_ATTRIBUTE_NUMBER5 | CoveredDependentsPEOPdpAttributeNumber5 | — |
| PDP_ATTRIBUTE_NUMBER6 | CoveredDependentsPEOPdpAttributeNumber6 | — |
| PDP_ATTRIBUTE_NUMBER7 | CoveredDependentsPEOPdpAttributeNumber7 | — |
| PDP_ATTRIBUTE_NUMBER8 | CoveredDependentsPEOPdpAttributeNumber8 | — |
| PDP_ATTRIBUTE_NUMBER9 | CoveredDependentsPEOPdpAttributeNumber9 | — |
| PER_IN_LER_ID | CoveredDependentsPEOPerInLerId | — |
| PROGRAM_APP_NAME | CoveredDependentsPEOProgramAppName | — |
| PROGRAM_NAME | CoveredDependentsPEOProgramName | — |
| PROGRAM_UPDATE_DATE | CoveredDependentsPEOProgramUpdateDate | — |
| PRTT_ENRT_RSLT_ID | CoveredDependentsPEOPrttEnrtRsltId | — |
| PRVS_CVG_STRT_DT | CoveredDependentsPEOPrvsCvgStrtDt | — |
| PRVS_CVG_THRU_DT | CoveredDependentsPEOPrvsCvgThruDt | — |
| REQUEST_ID | CoveredDependentsPEORequestId | — |
| RLNSHP_CD | CoveredDependentsPEORlnshpCd | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_ELIG_CVRD_DPNT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/beneligcvrddpnt.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
