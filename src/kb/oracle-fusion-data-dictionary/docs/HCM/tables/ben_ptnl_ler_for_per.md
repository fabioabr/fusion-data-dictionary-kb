---
id: DOC-HCM-064
doc_type: system-doc
title: "BEN_PTNL_LER_FOR_PER — Eventos de Vida Potenciais por Pessoa"
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
  - eventos-potenciais
  - potential-ler
aliases:
  - BEN_PTNL_LER_FOR_PER
  - ben_ptnl_ler_for_per
  - eventos-potenciais-beneficios
  - potential-ler-per
  - ben-ptnl-ler
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PTNL_LER_FOR_PER

## 📌 Visão Geral

Armazena os **eventos de vida potenciais** detectados para cada pessoa que ainda não foram processados ou confirmados.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Detecção automática:** Eventos detectados por mudanças de dados.
- **Fila de processamento:** Eventos pendentes de confirmação.
- **Workflow:** Alimenta o processo de reavaliação de elegibilidade.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PTNL_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de eventos de vida potenciais por pessoa
```sql
SELECT * FROM BEN_PTNL_LER_FOR_PER
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Eventos de Vida Potenciais por Pessoa).

---

## 🔗 PVOs Relacionados

### [[personpotentiallifeeventpvo|PersonPotentialLifeEventPVO]] (HCM · BICC: 18/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_RELATION_ID | BenefitRelationId | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CSD_BY_PTNL_LER_FOR_PER_ID | CsdByPtnlLerForPerId | — |
| DTCTD_DT | DtctdDt | ✅ |
| ENRT_PERD_ID | EnrtPerdId | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LER_ID | LerId | ✅ |
| LER_TYPE_CD | LerTypeCd | ✅ |
| LF_EVT_OCRD_DT | LfEvtOcrdDt | ✅ |
| MNL_DT | MnlDt | ✅ |
| MNLO_DT | MnloDt | — |
| NTFN_DT | NtfnDt | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | — |
| PROCD_DT | ProcdDt | ✅ |
| PROD_CD | ProdCd | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | — |
| PROGRAM_NAME | ProgramName | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PTNL_LER_FOR_PER_ID | PtnlLerForPerId | ✅ |
| PTNL_LER_FOR_PER_SRC_CD | PtnlLerForPerSrcCd | ✅ |
| PTNL_LER_FOR_PER_STAT_CD | PtnlLerForPerStatCd | ✅ |
| REQUEST_ID | RequestId | — |
| TRGR_TABLE_PK_ID | TrgrTablePkId | — |
| UNPROCD_DT | UnprocdDt | ✅ |
| VOIDD_DT | VoiddDt | ✅ |

### [[potentiallifeeventsextractpvo|PotentialLifeEventsExtractPVO]] (HCM · BICC: 38/38)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BENEFIT_RELATION_ID | BenefitRelationId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CLPSED_BY | ClpsedBy | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CSD_BY_PTNL_LER_FOR_PER_ID | CsdByPtnlLerForPerId | ✅ |
| DTCTD_DT | DtctdDt | ✅ |
| ENRT_PERD_ID | EnrtPerdId | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LER_ID | LerId | ✅ |
| LER_TYPE_CD | LerTypeCd | ✅ |
| LF_EVT_OCRD_DT | LfEvtOcrdDt | ✅ |
| MNL_DT | MnlDt | ✅ |
| MNLO_DT | MnloDt | ✅ |
| NTFN_DT | NtfnDt | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PersonId | ✅ |
| PROCD_DT | ProcdDt | ✅ |
| PROD_CD | ProdCd | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| PTNL_ADDNL_CHAR1 | PtnlAddnlChar1 | ✅ |
| PTNL_ADDNL_CHAR2 | PtnlAddnlChar2 | ✅ |
| PTNL_ADDNL_CHAR3 | PtnlAddnlChar3 | ✅ |
| PTNL_ADDNL_NUMBER1 | PtnlAddnlNumber1 | ✅ |
| PTNL_LER_FOR_PER_ID | PtnlLerForPerId | ✅ |
| PTNL_LER_FOR_PER_SRC_CD | PtnlLerForPerSrcCd | ✅ |
| PTNL_LER_FOR_PER_STAT_CD | PtnlLerForPerStatCd | ✅ |
| REQUEST_ID | RequestId | ✅ |
| TRGR_TABLE_PK_ID | TrgrTablePkId | ✅ |
| UNPROCD_DT | UnprocdDt | ✅ |
| VOIDD_DT | VoiddDt | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PTNL_LER_FOR_PER](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benptnllerforper.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
