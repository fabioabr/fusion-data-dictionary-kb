---
id: DOC-HCM-050
doc_type: system-doc
title: "BEN_PER_IN_LER — Pessoa em Evento de Vida"
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
  - pessoa-evento-vida
  - person-in-ler
aliases:
  - BEN_PER_IN_LER
  - ben_per_in_ler
  - pessoa-evento-vida
  - person-in-ler
  - ben-per-in-ler
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# BEN_PER_IN_LER

## 📌 Visão Geral

Armazena os **eventos de vida** ocorridos para cada pessoa, vinculando o colaborador ao motivo do evento de vida que dispara reavaliação de elegibilidade.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de eventos:** Documenta quando um evento de vida ocorreu para um colaborador.
- **Trigger de processos:** Dispara reavaliação de elegibilidade e período de inscrição.
- **Histórico:** Mantém histórico completo de eventos de vida.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BEN_PER_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 75% |
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

### Consulta de pessoa em evento de vida
```sql
SELECT * FROM BEN_PER_IN_LER
WHERE  ROWNUM <= 100;
```

### Filtros comuns
- Consultar documentação Oracle para filtros específicos

---

## 🔒 Observações

- Consultar documentação oficial Oracle para detalhes de uso.
- Tabela do módulo Benefits (Pessoa em Evento de Vida).

---

## 🔗 PVOs Relacionados

### [[coveredbeneficiariespvo|CoveredBeneficiariesPVO]] (HCM · BICC: 1/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | PersonLifeEventPEOAssignmentId | — |
| BCKT_DT | PersonLifeEventPEOBcktDt | — |
| BCKT_PER_IN_LER_ID | PersonLifeEventPEOBcktPerInLerId | — |
| BENEFIT_RELATION_ID | PersonLifeEventPEOBenefitRelationId | — |
| BUSINESS_GROUP_ID | PersonLifeEventPEOBusinessGroupId | — |
| CLSD_DT | PersonLifeEventPEOClsdDt | — |
| CREATED_BY | PersonLifeEventPEOCreatedBy | — |
| CREATION_DATE | PersonLifeEventPEOCreationDate | — |
| GROUP_PL_ID | PersonLifeEventPEOGroupPlId | — |
| JOB_DEFINITION_NAME | PersonLifeEventPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PersonLifeEventPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PersonLifeEventPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PersonLifeEventPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonLifeEventPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | PersonLifeEventPEOLegalEntityId | — |
| LER_ID | PersonLifeEventPEOLerId | — |
| LER_TYPE_CD | PersonLifeEventPEOLerTypeCd | — |
| LF_EVT_OCRD_DT | PersonLifeEventPEOLfEvtOcrdDt | — |
| NTFN_DT | PersonLifeEventPEONtfnDt | — |
| OBJECT_VERSION_NUMBER | PersonLifeEventPEOObjectVersionNumber | — |
| PER_IN_LER_ID | PersonLifeEventPEOPerInLerId | — |
| PER_IN_LER_STAT_CD | PersonLifeEventPEOPerInLerStatCd | — |
| PERSON_ID | PersonLifeEventPEOPersonId | — |
| PIL_ATTRIBUTE1 | PersonLifeEventPEOPilAttribute1 | — |
| PIL_ATTRIBUTE10 | PersonLifeEventPEOPilAttribute10 | — |
| PIL_ATTRIBUTE11 | PersonLifeEventPEOPilAttribute11 | — |
| PIL_ATTRIBUTE12 | PersonLifeEventPEOPilAttribute12 | — |
| PIL_ATTRIBUTE13 | PersonLifeEventPEOPilAttribute13 | — |
| PIL_ATTRIBUTE14 | PersonLifeEventPEOPilAttribute14 | — |
| PIL_ATTRIBUTE15 | PersonLifeEventPEOPilAttribute15 | — |
| PIL_ATTRIBUTE16 | PersonLifeEventPEOPilAttribute16 | — |
| PIL_ATTRIBUTE17 | PersonLifeEventPEOPilAttribute17 | — |
| PIL_ATTRIBUTE18 | PersonLifeEventPEOPilAttribute18 | — |
| PIL_ATTRIBUTE19 | PersonLifeEventPEOPilAttribute19 | — |
| PIL_ATTRIBUTE2 | PersonLifeEventPEOPilAttribute2 | — |
| PIL_ATTRIBUTE20 | PersonLifeEventPEOPilAttribute20 | — |
| PIL_ATTRIBUTE21 | PersonLifeEventPEOPilAttribute21 | — |
| PIL_ATTRIBUTE22 | PersonLifeEventPEOPilAttribute22 | — |
| PIL_ATTRIBUTE23 | PersonLifeEventPEOPilAttribute23 | — |
| PIL_ATTRIBUTE24 | PersonLifeEventPEOPilAttribute24 | — |
| PIL_ATTRIBUTE25 | PersonLifeEventPEOPilAttribute25 | — |
| PIL_ATTRIBUTE26 | PersonLifeEventPEOPilAttribute26 | — |
| PIL_ATTRIBUTE27 | PersonLifeEventPEOPilAttribute27 | — |
| PIL_ATTRIBUTE28 | PersonLifeEventPEOPilAttribute28 | — |
| PIL_ATTRIBUTE29 | PersonLifeEventPEOPilAttribute29 | — |
| PIL_ATTRIBUTE3 | PersonLifeEventPEOPilAttribute3 | — |
| PIL_ATTRIBUTE30 | PersonLifeEventPEOPilAttribute30 | — |
| PIL_ATTRIBUTE4 | PersonLifeEventPEOPilAttribute4 | — |
| PIL_ATTRIBUTE5 | PersonLifeEventPEOPilAttribute5 | — |
| PIL_ATTRIBUTE6 | PersonLifeEventPEOPilAttribute6 | — |
| PIL_ATTRIBUTE7 | PersonLifeEventPEOPilAttribute7 | — |
| PIL_ATTRIBUTE8 | PersonLifeEventPEOPilAttribute8 | — |
| PIL_ATTRIBUTE9 | PersonLifeEventPEOPilAttribute9 | — |
| PIL_ATTRIBUTE_CATEGORY | PersonLifeEventPEOPilAttributeCategory | — |
| PROCD_DT | PersonLifeEventPEOProcdDt | — |
| PROD_CD | PersonLifeEventPEOProdCd | — |
| PROGRAM_APP_NAME | PersonLifeEventPEOProgramAppName | — |
| PROGRAM_NAME | PersonLifeEventPEOProgramName | — |
| PROGRAM_UPDATE_DATE | PersonLifeEventPEOProgramUpdateDate | — |
| PRVS_STAT_CD | PersonLifeEventPEOPrvsStatCd | — |
| PTNL_LER_FOR_PER_ID | PersonLifeEventPEOPtnlLerForPerId | — |
| REQUEST_ID | PersonLifeEventPEORequestId | — |
| STRTD_DT | PersonLifeEventPEOStrtdDt | — |
| TRGR_TABLE_PK_ID | PersonLifeEventPEOTrgrTablePkId | — |
| VOIDD_DT | PersonLifeEventPEOVoiddDt | — |

### [[covereddependentspvo|CoveredDependentsPVO]] (HCM · BICC: 2/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | PersonLifeEventPEOAssignmentId | — |
| BCKT_DT | PersonLifeEventPEOBcktDt | — |
| BCKT_PER_IN_LER_ID | PersonLifeEventPEOBcktPerInLerId | — |
| BENEFIT_RELATION_ID | PersonLifeEventPEOBenefitRelationId | — |
| BUSINESS_GROUP_ID | PersonLifeEventPEOBusinessGroupId | — |
| CLSD_DT | PersonLifeEventPEOClsdDt | — |
| CREATED_BY | PersonLifeEventPEOCreatedBy | — |
| CREATION_DATE | PersonLifeEventPEOCreationDate1 | — |
| GROUP_PL_ID | PersonLifeEventPEOGroupPlId | — |
| JOB_DEFINITION_NAME | PersonLifeEventPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PersonLifeEventPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PersonLifeEventPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | PersonLifeEventPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PersonLifeEventPEOLastUpdatedBy1 | — |
| LEGAL_ENTITY_ID | PersonLifeEventPEOLegalEntityId | — |
| LER_ID | PersonLifeEventPEOLerId | ✅ |
| LER_TYPE_CD | PersonLifeEventPEOLerTypeCd | — |
| LF_EVT_OCRD_DT | PersonLifeEventPEOLfEvtOcrdDt | — |
| NTFN_DT | PersonLifeEventPEONtfnDt | — |
| OBJECT_VERSION_NUMBER | PersonLifeEventPEOObjectVersionNumber | — |
| PER_IN_LER_ID | PersonLifeEventPEOPerInLerId | — |
| PER_IN_LER_STAT_CD | PersonLifeEventPEOPerInLerStatCd | — |
| PERSON_ID | PersonLifeEventPEOPersonId | — |
| PIL_ATTRIBUTE1 | PersonLifeEventPEOPilAttribute1 | — |
| PIL_ATTRIBUTE10 | PersonLifeEventPEOPilAttribute10 | — |
| PIL_ATTRIBUTE11 | PersonLifeEventPEOPilAttribute11 | — |
| PIL_ATTRIBUTE12 | PersonLifeEventPEOPilAttribute12 | — |
| PIL_ATTRIBUTE13 | PersonLifeEventPEOPilAttribute13 | — |
| PIL_ATTRIBUTE14 | PersonLifeEventPEOPilAttribute14 | — |
| PIL_ATTRIBUTE15 | PersonLifeEventPEOPilAttribute15 | — |
| PIL_ATTRIBUTE16 | PersonLifeEventPEOPilAttribute16 | — |
| PIL_ATTRIBUTE17 | PersonLifeEventPEOPilAttribute17 | — |
| PIL_ATTRIBUTE18 | PersonLifeEventPEOPilAttribute18 | — |
| PIL_ATTRIBUTE19 | PersonLifeEventPEOPilAttribute19 | — |
| PIL_ATTRIBUTE2 | PersonLifeEventPEOPilAttribute2 | — |
| PIL_ATTRIBUTE20 | PersonLifeEventPEOPilAttribute20 | — |
| PIL_ATTRIBUTE21 | PersonLifeEventPEOPilAttribute21 | — |
| PIL_ATTRIBUTE22 | PersonLifeEventPEOPilAttribute22 | — |
| PIL_ATTRIBUTE23 | PersonLifeEventPEOPilAttribute23 | — |
| PIL_ATTRIBUTE24 | PersonLifeEventPEOPilAttribute24 | — |
| PIL_ATTRIBUTE25 | PersonLifeEventPEOPilAttribute25 | — |
| PIL_ATTRIBUTE26 | PersonLifeEventPEOPilAttribute26 | — |
| PIL_ATTRIBUTE27 | PersonLifeEventPEOPilAttribute27 | — |
| PIL_ATTRIBUTE28 | PersonLifeEventPEOPilAttribute28 | — |
| PIL_ATTRIBUTE29 | PersonLifeEventPEOPilAttribute29 | — |
| PIL_ATTRIBUTE3 | PersonLifeEventPEOPilAttribute3 | — |
| PIL_ATTRIBUTE30 | PersonLifeEventPEOPilAttribute30 | — |
| PIL_ATTRIBUTE4 | PersonLifeEventPEOPilAttribute4 | — |
| PIL_ATTRIBUTE5 | PersonLifeEventPEOPilAttribute5 | — |
| PIL_ATTRIBUTE6 | PersonLifeEventPEOPilAttribute6 | — |
| PIL_ATTRIBUTE7 | PersonLifeEventPEOPilAttribute7 | — |
| PIL_ATTRIBUTE8 | PersonLifeEventPEOPilAttribute8 | — |
| PIL_ATTRIBUTE9 | PersonLifeEventPEOPilAttribute9 | — |
| PIL_ATTRIBUTE_CATEGORY | PersonLifeEventPEOPilAttributeCategory | — |
| PROCD_DT | PersonLifeEventPEOProcdDt | — |
| PROD_CD | PersonLifeEventPEOProdCd | — |
| PROGRAM_APP_NAME | PersonLifeEventPEOProgramAppName | — |
| PROGRAM_NAME | PersonLifeEventPEOProgramName | — |
| PROGRAM_UPDATE_DATE | PersonLifeEventPEOProgramUpdateDate | — |
| PRVS_STAT_CD | PersonLifeEventPEOPrvsStatCd | — |
| PTNL_LER_FOR_PER_ID | PersonLifeEventPEOPtnlLerForPerId | — |
| REQUEST_ID | PersonLifeEventPEORequestId | — |
| STRTD_DT | PersonLifeEventPEOStrtdDt | — |
| TRGR_TABLE_PK_ID | PersonLifeEventPEOTrgrTablePkId | — |
| VOIDD_DT | PersonLifeEventPEOVoiddDt | — |

### [[personlifeeventpvo|PersonLifeEventPVO]] (HCM · BICC: 15/65)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| BCKT_DT | BcktDt | ✅ |
| BCKT_PER_IN_LER_ID | BcktPerInLerId | — |
| BENEFIT_RELATION_ID | BenefitRelationId | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CLSD_DT | ClsdDt | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| GROUP_PL_ID | GroupPlId | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LER_ID | LerId | ✅ |
| LER_TYPE_CD | LerTypeCd | — |
| LF_EVT_OCRD_DT | LfEvtOcrdDt | ✅ |
| NTFN_DT | NtfnDt | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_IN_LER_ID | PerInLerId | ✅ |
| PER_IN_LER_STAT_CD | PerInLerStatCd | ✅ |
| PERSON_ID | PersonId | — |
| PIL_ATTRIBUTE1 | PilAttribute1 | — |
| PIL_ATTRIBUTE10 | PilAttribute10 | — |
| PIL_ATTRIBUTE11 | PilAttribute11 | — |
| PIL_ATTRIBUTE12 | PilAttribute12 | — |
| PIL_ATTRIBUTE13 | PilAttribute13 | — |
| PIL_ATTRIBUTE14 | PilAttribute14 | — |
| PIL_ATTRIBUTE15 | PilAttribute15 | — |
| PIL_ATTRIBUTE16 | PilAttribute16 | — |
| PIL_ATTRIBUTE17 | PilAttribute17 | — |
| PIL_ATTRIBUTE18 | PilAttribute18 | — |
| PIL_ATTRIBUTE19 | PilAttribute19 | — |
| PIL_ATTRIBUTE2 | PilAttribute2 | — |
| PIL_ATTRIBUTE20 | PilAttribute20 | — |
| PIL_ATTRIBUTE21 | PilAttribute21 | — |
| PIL_ATTRIBUTE22 | PilAttribute22 | — |
| PIL_ATTRIBUTE23 | PilAttribute23 | — |
| PIL_ATTRIBUTE24 | PilAttribute24 | — |
| PIL_ATTRIBUTE25 | PilAttribute25 | — |
| PIL_ATTRIBUTE26 | PilAttribute26 | — |
| PIL_ATTRIBUTE27 | PilAttribute27 | — |
| PIL_ATTRIBUTE28 | PilAttribute28 | — |
| PIL_ATTRIBUTE29 | PilAttribute29 | — |
| PIL_ATTRIBUTE3 | PilAttribute3 | — |
| PIL_ATTRIBUTE30 | PilAttribute30 | — |
| PIL_ATTRIBUTE4 | PilAttribute4 | — |
| PIL_ATTRIBUTE5 | PilAttribute5 | — |
| PIL_ATTRIBUTE6 | PilAttribute6 | — |
| PIL_ATTRIBUTE7 | PilAttribute7 | — |
| PIL_ATTRIBUTE8 | PilAttribute8 | — |
| PIL_ATTRIBUTE9 | PilAttribute9 | — |
| PIL_ATTRIBUTE_CATEGORY | PilAttributeCategory | — |
| PROCD_DT | ProcdDt | ✅ |
| PROD_CD | ProdCd | — |
| PROGRAM_APP_NAME | ProgramAppName | — |
| PROGRAM_NAME | ProgramName | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | — |
| PRVS_STAT_CD | PrvsStatCd | — |
| PTNL_LER_FOR_PER_ID | PtnlLerForPerId | — |
| REQUEST_ID | RequestId | — |
| STRTD_DT | StrtdDt | ✅ |
| TRGR_TABLE_PK_ID | TrgrTablePkId | — |
| VOIDD_DT | VoiddDt | ✅ |

### [[personlifeeventsextractpvo|PersonLifeEventsExtractPVO]] (HCM · BICC: 34/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | ✅ |
| BCKT_DT | BcktDt | ✅ |
| BCKT_PER_IN_LER_ID | BcktPerInLerId | ✅ |
| BENEFIT_RELATION_ID | BenefitRelationId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CLSD_DT | ClsdDt | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| GROUP_PL_ID | GroupPlId | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | LegalEntityId | ✅ |
| LER_ID | LerId | ✅ |
| LER_TYPE_CD | LerTypeCd | ✅ |
| LF_EVT_OCRD_DT | LfEvtOcrdDt | ✅ |
| NTFN_DT | NtfnDt | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PER_IN_LER_ID | PerInLerId | ✅ |
| PER_IN_LER_STAT_CD | PerInLerStatCd | ✅ |
| PERSON_ID | PersonId | ✅ |
| PROCD_DT | ProcdDt | ✅ |
| PROD_CD | ProdCd | ✅ |
| PROGRAM_APP_NAME | ProgramAppName | ✅ |
| PROGRAM_NAME | ProgramName | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| PRVS_STAT_CD | PrvsStatCd | ✅ |
| PTNL_LER_FOR_PER_ID | PtnlLerForPerId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| STRTD_DT | StrtdDt | ✅ |
| TRGR_TABLE_PK_ID | TrgrTablePkId | ✅ |
| VOIDD_DT | VoiddDt | ✅ |

---

## 📚 Referências

- [Oracle Docs — BEN_PER_IN_LER](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/benperinler.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
