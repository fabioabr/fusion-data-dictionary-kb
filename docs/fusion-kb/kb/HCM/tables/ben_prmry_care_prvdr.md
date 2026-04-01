---
id: DOC-HCM-057
doc_type: system-doc
title: "BEN_PRMRY_CARE_PRVDR — Provedores de Cuidado Primário"
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
  - provedor-cuidado
  - primary-care-provider
  - pcp
aliases:
  - BEN_PRMRY_CARE_PRVDR
  - ben_prmry_care_prvdr
  - provedor-cuidado-beneficios
  - primary-care-provider
  - ben-prmry-care-prvdr
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRMRY_CARE_PRVDR

## 📌 Visão Geral

Armazena os **provedores de cuidado primário** (PCP) selecionados pelos participantes de planos de saúde.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Seleção de PCP:** Registro do médico/clínica de cuidado primário.
- **Self-service:** Permite ao colaborador selecionar/alterar seu PCP.
- **Rede credenciada:** Vinculação com provedores da rede.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PRMRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de provedores de cuidado primário
```sql
SELECT * FROM BEN_PRMRY_CARE_PRVDR
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Provedores de Cuidado Primário).

---

## 🔗 PVOs Relacionados

### [[primarycareproviderpvo|PrimaryCareProviderPVO]] (HCM · BICC: 19/92)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CVG_STRT_DT | CvgStrtDt | ✅ |
| CVG_THRU_DT | CvgThruDt | ✅ |
| CVRD_FLAG | CvrdFlag | ✅ |
| ELIG_CVRD_DPNT_ID | EligCvrdDpntId | ✅ |
| ELIG_DPNT_ID | EligDpntId | ✅ |
| ELIG_PER_ELCTBL_CHC_ID | EligPerElctblChcId | ✅ |
| ENDED_CVG_THRU_DT | EndedCvgThruDt | ✅ |
| ENDED_PER_IN_LER_ID | EndedPerInLerId | ✅ |
| EXT_IDENT | ExtIdent | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PPR_ATTRIBUTE1 | PprAttribute1 | — |
| PPR_ATTRIBUTE10 | PprAttribute10 | — |
| PPR_ATTRIBUTE11 | PprAttribute11 | — |
| PPR_ATTRIBUTE12 | PprAttribute12 | — |
| PPR_ATTRIBUTE13 | PprAttribute13 | — |
| PPR_ATTRIBUTE14 | PprAttribute14 | — |
| PPR_ATTRIBUTE15 | PprAttribute15 | — |
| PPR_ATTRIBUTE16 | PprAttribute16 | — |
| PPR_ATTRIBUTE17 | PprAttribute17 | — |
| PPR_ATTRIBUTE18 | PprAttribute18 | — |
| PPR_ATTRIBUTE19 | PprAttribute19 | — |
| PPR_ATTRIBUTE2 | PprAttribute2 | — |
| PPR_ATTRIBUTE20 | PprAttribute20 | — |
| PPR_ATTRIBUTE21 | PprAttribute21 | — |
| PPR_ATTRIBUTE22 | PprAttribute22 | — |
| PPR_ATTRIBUTE23 | PprAttribute23 | — |
| PPR_ATTRIBUTE24 | PprAttribute24 | — |
| PPR_ATTRIBUTE25 | PprAttribute25 | — |
| PPR_ATTRIBUTE26 | PprAttribute26 | — |
| PPR_ATTRIBUTE27 | PprAttribute27 | — |
| PPR_ATTRIBUTE28 | PprAttribute28 | — |
| PPR_ATTRIBUTE29 | PprAttribute29 | — |
| PPR_ATTRIBUTE3 | PprAttribute3 | — |
| PPR_ATTRIBUTE30 | PprAttribute30 | — |
| PPR_ATTRIBUTE4 | PprAttribute4 | — |
| PPR_ATTRIBUTE5 | PprAttribute5 | — |
| PPR_ATTRIBUTE6 | PprAttribute6 | — |
| PPR_ATTRIBUTE7 | PprAttribute7 | — |
| PPR_ATTRIBUTE8 | PprAttribute8 | — |
| PPR_ATTRIBUTE9 | PprAttribute9 | — |
| PPR_ATTRIBUTE_CATEGORY | PprAttributeCategory | — |
| PPR_ATTRIBUTE_DATE1 | PprAttributeDate1 | — |
| PPR_ATTRIBUTE_DATE10 | PprAttributeDate10 | — |
| PPR_ATTRIBUTE_DATE11 | PprAttributeDate11 | — |
| PPR_ATTRIBUTE_DATE12 | PprAttributeDate12 | — |
| PPR_ATTRIBUTE_DATE13 | PprAttributeDate13 | — |
| PPR_ATTRIBUTE_DATE14 | PprAttributeDate14 | — |
| PPR_ATTRIBUTE_DATE15 | PprAttributeDate15 | — |
| PPR_ATTRIBUTE_DATE2 | PprAttributeDate2 | — |
| PPR_ATTRIBUTE_DATE3 | PprAttributeDate3 | — |
| PPR_ATTRIBUTE_DATE4 | PprAttributeDate4 | — |
| PPR_ATTRIBUTE_DATE5 | PprAttributeDate5 | — |
| PPR_ATTRIBUTE_DATE6 | PprAttributeDate6 | — |
| PPR_ATTRIBUTE_DATE7 | PprAttributeDate7 | — |
| PPR_ATTRIBUTE_DATE8 | PprAttributeDate8 | — |
| PPR_ATTRIBUTE_DATE9 | PprAttributeDate9 | — |
| PPR_ATTRIBUTE_NUMBER1 | PprAttributeNumber1 | — |
| PPR_ATTRIBUTE_NUMBER10 | PprAttributeNumber10 | — |
| PPR_ATTRIBUTE_NUMBER11 | PprAttributeNumber11 | — |
| PPR_ATTRIBUTE_NUMBER12 | PprAttributeNumber12 | — |
| PPR_ATTRIBUTE_NUMBER13 | PprAttributeNumber13 | — |
| PPR_ATTRIBUTE_NUMBER14 | PprAttributeNumber14 | — |
| PPR_ATTRIBUTE_NUMBER15 | PprAttributeNumber15 | — |
| PPR_ATTRIBUTE_NUMBER16 | PprAttributeNumber16 | — |
| PPR_ATTRIBUTE_NUMBER17 | PprAttributeNumber17 | — |
| PPR_ATTRIBUTE_NUMBER18 | PprAttributeNumber18 | — |
| PPR_ATTRIBUTE_NUMBER19 | PprAttributeNumber19 | — |
| PPR_ATTRIBUTE_NUMBER2 | PprAttributeNumber2 | — |
| PPR_ATTRIBUTE_NUMBER20 | PprAttributeNumber20 | — |
| PPR_ATTRIBUTE_NUMBER3 | PprAttributeNumber3 | — |
| PPR_ATTRIBUTE_NUMBER4 | PprAttributeNumber4 | — |
| PPR_ATTRIBUTE_NUMBER5 | PprAttributeNumber5 | — |
| PPR_ATTRIBUTE_NUMBER6 | PprAttributeNumber6 | — |
| PPR_ATTRIBUTE_NUMBER7 | PprAttributeNumber7 | — |
| PPR_ATTRIBUTE_NUMBER8 | PprAttributeNumber8 | — |
| PPR_ATTRIBUTE_NUMBER9 | PprAttributeNumber9 | — |
| PRMRY_CARE_PRVDR_ID | PrmryCarePrvdrId | ✅ |
| PRMRY_CARE_PRVDR_TYP_CD | PrmryCarePrvdrTypCd | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | ✅ |
| PRVS_CVG_STRT_DT | PrvsCvgStrtDt | — |
| PRVS_CVG_THRU_DT | PrvsCvgThruDt | — |
| REQUEST_ID | RequestId | — |

---

## 📚 Referências

- [Oracle Docs — BEN_PRMRY_CARE_PRVDR](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprmrycareprvdr.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
