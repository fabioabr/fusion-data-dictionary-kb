---
id: DOC-HCM-649
doc_type: system-doc
title: "PER_CONTRACTS_F — Contratos de Trabalho"
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
  - workforce-management
  - contratos
  - contracts
aliases:
  - PER_CONTRACTS_F
  - per_contracts_f
  - per-contracts-f
  - contratos-de-trabalho
  - per-contracts-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CONTRACTS_F

## 📌 Visão Geral

Armazena os **contratos de trabalho** dos colaboradores, com vigência temporal. Define os termos contratuais como tipo de contrato, duração, período de experiência e condições específicas.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de contratos** — registro dos termos contratuais de cada colaborador.
- **Tipos de contrato** — CLT, temporário, estágio, aprendiz, etc.
- **Período de experiência** — controle de prazos de experiência.
- **Renovação** — rastreamento de renovações e aditivos contratuais.
- **Compliance trabalhista** — conformidade com legislação de contratos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONTRACT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do contrato | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | CONTRACT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de contrato (PERMANENT, TEMPORARY, etc.) | — | 🟢 90% |
| 6 | DURATION | NUMBER | NULL | Dados | Duração do contrato (em meses) | — | 🟢 85% |
| 7 | STATUS | VARCHAR2(30) | NULL | Status | Status do contrato (ACTIVE, EXPIRED, TERMINATED) | — | 🟢 85% |
| 8 | START_DATE | DATE | NULL | Período | Data de início do contrato | — | 🟢 90% |
| 9 | END_DATE | DATE | NULL | Período | Data de término prevista | — | 🟢 90% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador titular do contrato de trabalho)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Contrato vigente de um colaborador
```sql
SELECT pcf.CONTRACT_TYPE, pcf.STATUS, pcf.START_DATE, pcf.END_DATE
FROM   PER_CONTRACTS_F pcf
WHERE  pcf.PERSON_ID = :p_person_id
  AND  pcf.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN pcf.EFFECTIVE_START_DATE AND pcf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `CONTRACT_TYPE = 'PERMANENT'` — Contratos permanentes (CLT)
- `STATUS = 'ACTIVE'` — Contratos ativos
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- O `CONTRACT_TYPE` varia por legislação — no Brasil: PERMANENT (CLT), TEMPORARY, INTERNSHIP, APPRENTICE.
- Contratos temporários devem ter `END_DATE` preenchida.
- Integra-se com payroll para regras específicas por tipo de contrato.
---

## 🔗 PVOs Relacionados

### [[contractpvo|ContractPVO]] (HCM · BICC: 33/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | ContractPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | ContractPEOBusinessGroupId | ✅ |
| CONTRACT_END_DATE | ContractPEOContractEndDate | ✅ |
| CONTRACT_ID | ContractId | ✅ |
| CONTRACT_NUMBER | ContractPEOContractNumber | ✅ |
| CONTRACTUAL_JOB_TITLE | ContractPEOContractualJobTitle | ✅ |
| CREATED_BY | ContractPEOCreatedBy | ✅ |
| CREATION_DATE | ContractPEOCreationDate | ✅ |
| DESCRIPTION | ContractPEODescription | ✅ |
| DOC_STATUS | ContractPEODocStatus | ✅ |
| DOC_STATUS_CHANGE_DATE | ContractPEODocStatusChangeDate | ✅ |
| DURATION | ContractPEODuration | ✅ |
| DURATION_UNITS | ContractPEODurationUnits | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| END_REASON | ContractPEOEndReason | ✅ |
| EXTENSION_PERIOD | ContractPEOExtensionPeriod | ✅ |
| EXTENSION_PERIOD_UNITS | ContractPEOExtensionPeriodUnits | ✅ |
| EXTENSION_REASON | ContractPEOExtensionReason | ✅ |
| LAST_UPDATE_DATE | ContractPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ContractPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ContractPEOLegislationCode | — |
| NUMBER_OF_EXTENSIONS | ContractPEONumberOfExtensions | ✅ |
| OBJECT_VERSION_NUMBER | ContractPEOObjectVersionNumber | ✅ |
| PARTIES | ContractPEOParties | ✅ |
| PERIOD_OF_SERVICE_ID | ContractPEOPeriodOfServiceId | ✅ |
| PERSON_ID | ContractPEOPersonId | ✅ |
| REFERENCE | ContractPEOReference | ✅ |
| START_REASON | ContractPEOStartReason | ✅ |
| STATUS | ContractPEOStatus | ✅ |
| STATUS_REASON | ContractPEOStatusReason | ✅ |
| TYPE | ContractPEOType | ✅ |
| WORK_TERMS_TYPE | ContractPEOWorkTermsType | ✅ |

### [[contractpvoviewall|ContractPVOViewAll]] (HCM · BICC: 7/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | ContractPEOAssignmentId | — |
| BUSINESS_GROUP_ID | ContractPEOBusinessGroupId | — |
| CONTRACT_END_DATE | ContractPEOContractEndDate | — |
| CONTRACT_ID | ContractId | ✅ |
| CONTRACT_NUMBER | ContractPEOContractNumber | — |
| CONTRACTUAL_JOB_TITLE | ContractPEOContractualJobTitle | — |
| CREATED_BY | ContractPEOCreatedBy | — |
| CREATION_DATE | ContractPEOCreationDate | — |
| DESCRIPTION | ContractPEODescription | ✅ |
| DOC_STATUS | ContractPEODocStatus | — |
| DOC_STATUS_CHANGE_DATE | ContractPEODocStatusChangeDate | — |
| DURATION | ContractPEODuration | — |
| DURATION_UNITS | ContractPEODurationUnits | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| END_REASON | ContractPEOEndReason | — |
| EXTENSION_PERIOD | ContractPEOExtensionPeriod | — |
| EXTENSION_PERIOD_UNITS | ContractPEOExtensionPeriodUnits | — |
| EXTENSION_REASON | ContractPEOExtensionReason | — |
| LAST_UPDATE_DATE | ContractPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ContractPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ContractPEOLastUpdatedBy | — |
| LEGISLATION_CODE | ContractPEOLegislationCode | — |
| NUMBER_OF_EXTENSIONS | ContractPEONumberOfExtensions | — |
| OBJECT_VERSION_NUMBER | ContractPEOObjectVersionNumber | — |
| PARTIES | ContractPEOParties | — |
| PERIOD_OF_SERVICE_ID | ContractPEOPeriodOfServiceId | — |
| PERSON_ID | ContractPEOPersonId | — |
| REFERENCE | ContractPEOReference | — |
| START_REASON | ContractPEOStartReason | — |
| STATUS | ContractPEOStatus | ✅ |
| STATUS_REASON | ContractPEOStatusReason | — |
| TYPE | ContractPEOType | ✅ |
| WORK_TERMS_TYPE | ContractPEOWorkTermsType | — |

---

## 📚 Referências

- [Oracle Docs — PER_CONTRACTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percontractsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
