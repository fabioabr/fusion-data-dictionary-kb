---
id: DOC-HCM-059
doc_type: system-doc
title: "BEN_PRTT_ENRT_ACTN — Ações de Inscrição de Participante"
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
  - acoes-inscricao
  - enrollment-actions
aliases:
  - BEN_PRTT_ENRT_ACTN
  - ben_prtt_enrt_actn
  - acoes-inscricao-beneficios
  - enrollment-actions
  - ben-prtt-enrt-actn
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PRTT_ENRT_ACTN

## 📌 Visão Geral

Armazena as **ações executadas** durante o processo de inscrição de benefícios (ex.: inscrição, alteração de opção, cancelamento, waive).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Histórico de ações:** Registra cada ação do processo de inscrição.
- **Auditoria:** Rastreabilidade de decisões do participante.
- **Workflow:** Controle do fluxo de inscrição.

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

### Consulta de ações de inscrição de participante
```sql
SELECT * FROM BEN_PRTT_ENRT_ACTN
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Ações de Inscrição de Participante).

---

## 🔗 PVOs Relacionados

### [[personenrollmentactionpvo|PersonEnrollmentActionPVO]] (HCM · BICC: 12/91)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTN_TYP_ID | ActnTypId | ✅ |
| ACTN_TYP_LVL_CD | ActnTypLvlCd | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CMPLTD_DT | CmpltdDt | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DUE_DT | DueDt | ✅ |
| ELIG_CVRD_DPNT_ID | EligCvrdDpntId | — |
| ENDED_PER_IN_LER_ID | EndedPerInLerId | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PEA_ATTRIBUTE1 | PeaAttribute1 | — |
| PEA_ATTRIBUTE10 | PeaAttribute10 | — |
| PEA_ATTRIBUTE11 | PeaAttribute11 | — |
| PEA_ATTRIBUTE12 | PeaAttribute12 | — |
| PEA_ATTRIBUTE13 | PeaAttribute13 | — |
| PEA_ATTRIBUTE14 | PeaAttribute14 | — |
| PEA_ATTRIBUTE15 | PeaAttribute15 | — |
| PEA_ATTRIBUTE16 | PeaAttribute16 | — |
| PEA_ATTRIBUTE17 | PeaAttribute17 | — |
| PEA_ATTRIBUTE18 | PeaAttribute18 | — |
| PEA_ATTRIBUTE19 | PeaAttribute19 | — |
| PEA_ATTRIBUTE2 | PeaAttribute2 | — |
| PEA_ATTRIBUTE20 | PeaAttribute20 | — |
| PEA_ATTRIBUTE21 | PeaAttribute21 | — |
| PEA_ATTRIBUTE22 | PeaAttribute22 | — |
| PEA_ATTRIBUTE23 | PeaAttribute23 | — |
| PEA_ATTRIBUTE24 | PeaAttribute24 | — |
| PEA_ATTRIBUTE25 | PeaAttribute25 | — |
| PEA_ATTRIBUTE26 | PeaAttribute26 | — |
| PEA_ATTRIBUTE27 | PeaAttribute27 | — |
| PEA_ATTRIBUTE28 | PeaAttribute28 | — |
| PEA_ATTRIBUTE29 | PeaAttribute29 | — |
| PEA_ATTRIBUTE3 | PeaAttribute3 | — |
| PEA_ATTRIBUTE30 | PeaAttribute30 | — |
| PEA_ATTRIBUTE4 | PeaAttribute4 | — |
| PEA_ATTRIBUTE5 | PeaAttribute5 | — |
| PEA_ATTRIBUTE6 | PeaAttribute6 | — |
| PEA_ATTRIBUTE7 | PeaAttribute7 | — |
| PEA_ATTRIBUTE8 | PeaAttribute8 | — |
| PEA_ATTRIBUTE9 | PeaAttribute9 | — |
| PEA_ATTRIBUTE_CATEGORY | PeaAttributeCategory | — |
| PEA_ATTRIBUTE_DATE1 | PeaAttributeDate1 | — |
| PEA_ATTRIBUTE_DATE10 | PeaAttributeDate10 | — |
| PEA_ATTRIBUTE_DATE11 | PeaAttributeDate11 | — |
| PEA_ATTRIBUTE_DATE12 | PeaAttributeDate12 | — |
| PEA_ATTRIBUTE_DATE13 | PeaAttributeDate13 | — |
| PEA_ATTRIBUTE_DATE14 | PeaAttributeDate14 | — |
| PEA_ATTRIBUTE_DATE15 | PeaAttributeDate15 | — |
| PEA_ATTRIBUTE_DATE2 | PeaAttributeDate2 | — |
| PEA_ATTRIBUTE_DATE3 | PeaAttributeDate3 | — |
| PEA_ATTRIBUTE_DATE4 | PeaAttributeDate4 | — |
| PEA_ATTRIBUTE_DATE5 | PeaAttributeDate5 | — |
| PEA_ATTRIBUTE_DATE6 | PeaAttributeDate6 | — |
| PEA_ATTRIBUTE_DATE7 | PeaAttributeDate7 | — |
| PEA_ATTRIBUTE_DATE8 | PeaAttributeDate8 | — |
| PEA_ATTRIBUTE_DATE9 | PeaAttributeDate9 | — |
| PEA_ATTRIBUTE_NUMBER1 | PeaAttributeNumber1 | — |
| PEA_ATTRIBUTE_NUMBER10 | PeaAttributeNumber10 | — |
| PEA_ATTRIBUTE_NUMBER11 | PeaAttributeNumber11 | — |
| PEA_ATTRIBUTE_NUMBER12 | PeaAttributeNumber12 | — |
| PEA_ATTRIBUTE_NUMBER13 | PeaAttributeNumber13 | — |
| PEA_ATTRIBUTE_NUMBER14 | PeaAttributeNumber14 | — |
| PEA_ATTRIBUTE_NUMBER15 | PeaAttributeNumber15 | — |
| PEA_ATTRIBUTE_NUMBER16 | PeaAttributeNumber16 | — |
| PEA_ATTRIBUTE_NUMBER17 | PeaAttributeNumber17 | — |
| PEA_ATTRIBUTE_NUMBER18 | PeaAttributeNumber18 | — |
| PEA_ATTRIBUTE_NUMBER19 | PeaAttributeNumber19 | — |
| PEA_ATTRIBUTE_NUMBER2 | PeaAttributeNumber2 | — |
| PEA_ATTRIBUTE_NUMBER20 | PeaAttributeNumber20 | — |
| PEA_ATTRIBUTE_NUMBER3 | PeaAttributeNumber3 | — |
| PEA_ATTRIBUTE_NUMBER4 | PeaAttributeNumber4 | — |
| PEA_ATTRIBUTE_NUMBER5 | PeaAttributeNumber5 | — |
| PEA_ATTRIBUTE_NUMBER6 | PeaAttributeNumber6 | — |
| PEA_ATTRIBUTE_NUMBER7 | PeaAttributeNumber7 | — |
| PEA_ATTRIBUTE_NUMBER8 | PeaAttributeNumber8 | — |
| PEA_ATTRIBUTE_NUMBER9 | PeaAttributeNumber9 | — |
| PER_IN_LER_ID | PerInLerId | — |
| PL_BNF_ID | PlBnfId | — |
| PROGRAM_APP_NAME | ProgramAppName | — |
| PROGRAM_NAME | ProgramName | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PRTT_ENRT_ACTN_ID | PrttEnrtActnId | ✅ |
| PRTT_ENRT_RSLT_ID | PrttEnrtRsltId | — |
| REQUEST_ID | RequestId | — |
| RQD_FLAG | RqdFlag | ✅ |
| SSPND_FLAG | SspndFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PRTT_ENRT_ACTN](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benprttenrtactn.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
