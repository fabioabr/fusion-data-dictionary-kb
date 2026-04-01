---
id: DOC-HCM-687
doc_type: system-doc
title: "PER_PERIODS_OF_SERVICE — Períodos de Serviço"
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
  - periodos-servico
  - admissao
  - demissao
  - vinculo-empregaticio
aliases:
  - PER_PERIODS_OF_SERVICE
  - per_periods_of_service
  - periodos-servico
  - vinculo-empregaticio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_PERIODS_OF_SERVICE

## Visão Geral

Armazena os **períodos de serviço** (vínculos empregatícios) de cada pessoa na organização. Cada registro representa um período contínuo de trabalho, desde a data de admissão até a data de desligamento (quando aplicável).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão do ciclo de vida do colaborador** — admissão, recontratação, desligamento
- **Cálculo de tempo de casa** — antiguidade e tempo de serviço
- **Folha de pagamento** — determinar períodos ativos para processamento
- **Relatórios trabalhistas** — CAGED, eSocial, RAIS
- **Cálculos de rescisão** — base para aviso prévio, férias proporcionais, 13º
- **Análise de turnover** — taxas de rotatividade por período

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERIOD_OF_SERVICE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do período de serviço | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Referência à pessoa | PER_PERSONS | 🟢 95% |
| 3 | DATE_START | DATE | NOT NULL | Vínculo | Data de admissão/início do serviço | — | 🟢 95% |
| 4 | ACTUAL_TERMINATION_DATE | DATE | NULL | Vínculo | Data efetiva do desligamento | — | 🟢 95% |
| 5 | FINAL_PROCESS_DATE | DATE | NULL | Vínculo | Data do processo final (última folha) | — | 🟢 90% |
| 6 | LEAVING_REASON | VARCHAR2(30) | NULL | Classificação | Motivo do desligamento | — | 🟢 85% |
| 7 | NOTIFIED_TERMINATION_DATE | DATE | NULL | Vínculo | Data de notificação do desligamento | — | 🟡 75% |
| 8 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | FK | Entidade legal do vínculo | — | 🟡 80% |
| 9 | PERIOD_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do período (empregado, contingente, etc.) | — | 🟡 75% |
| 10 | PERSON_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de pessoa durante este período | PER_PERSON_TYPES | 🟡 75% |
| 11 | ACCEPTED_TERMINATION_DATE | DATE | NULL | Vínculo | Data de aceitação do desligamento | — | 🟡 70% |
| 12 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 13 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 14 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 15 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 16 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_persons]] — via `PERSON_ID` (pessoa do período de serviço)
- [[per_person_types]] — via `PERSON_TYPE_ID` (tipo de pessoa no período de serviço)

### Tabelas-filha (FK de saída)
- [[per_all_assignments_m]] — via `PERIOD_OF_SERVICE_ID` (vínculos empregatícios do período de serviço)

---

## Uso Típico

### Colaboradores ativos (sem desligamento)
```sql
SELECT ps.PERSON_ID, ps.DATE_START, ps.PERIOD_TYPE
FROM   PER_PERIODS_OF_SERVICE ps
WHERE  ps.ACTUAL_TERMINATION_DATE IS NULL;
```

### Calcular tempo de serviço
```sql
SELECT ps.PERSON_ID,
       MONTHS_BETWEEN(SYSDATE, ps.DATE_START) AS meses_servico
FROM   PER_PERIODS_OF_SERVICE ps
WHERE  ps.ACTUAL_TERMINATION_DATE IS NULL;
```

---

## Observações

- `ACTUAL_TERMINATION_DATE IS NULL` indica colaborador ativo.
- Uma pessoa pode ter múltiplos períodos de serviço (recontratação).
- `FINAL_PROCESS_DATE` indica quando a última folha foi processada após desligamento.
- `LEAVING_REASON` deve ser preenchido obrigatoriamente em caso de desligamento.

---

## Referências

- [Oracle Docs — PER_PERIODS_OF_SERVICE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perperiodsofservice.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 8/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_TERMINATION_DATE | PeriodOfServicePEOActualTerminationDate | ✅ |
| ADJUSTED_SVC_DATE | PeriodOfServicePEOAdjustedSvcDate | — |
| DATE_START | PeriodOfServicePEODateStart | ✅ |
| LAST_UPDATE_DATE | PeriodOfServicePEOLastUpdateDate | ✅ |
| NOTIFIED_TERMINATION_DATE | PeriodOfServicePEONotifiedTerminationDate | ✅ |
| ORIGINAL_DATE_OF_HIRE | PeriodOfServicePEOOriginalDateOfHire | ✅ |
| PERIOD_OF_SERVICE_ID | PeriodOfServicePEOPeriodOfServiceId | ✅ |
| READY_TO_CONVERT | PeriodOfServicePEOReadyToConvert | ✅ |
| REVOKE_USER_ACCESS | PeriodOfServicePEORevokeUserAccess | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 7/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTUAL_TERMINATION_DATE | PeriodOfServicePEOActualTerminationDate | ✅ |
| ADJUSTED_SVC_DATE | PeriodOfServicePEOAdjustedSvcDate | — |
| DATE_START | PeriodOfServicePEODateStart | ✅ |
| LAST_UPDATE_DATE | PeriodOfServicePEOLastUpdateDate | ✅ |
| NOTIFIED_TERMINATION_DATE | PeriodOfServicePEONotifiedTerminationDate | ✅ |
| ORIGINAL_DATE_OF_HIRE | PeriodOfServicePEOOriginalDateOfHire | ✅ |
| PERIOD_OF_SERVICE_ID | PeriodOfServicePEOPeriodOfServiceId | — |
| READY_TO_CONVERT | PeriodOfServicePEOReadyToConvert | ✅ |
| REVOKE_USER_ACCESS | PeriodOfServicePEORevokeUserAccess | ✅ |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATE_START | PeriodOfServicePEODateStart | ✅ |
| PERIOD_OF_SERVICE_ID | PeriodOfServicePEOPeriodOfServiceId | — |

### [[workrelationshippvo|WorkRelationshipPVO]] (HCM · BICC: 31/34)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_TERMINATION_DATE | WorkRelationshipPEOAcceptedTerminationDate | ✅ |
| ACTION_OCCURRENCE_ID | WorkRelationshipPEOActionOccurrenceId | ✅ |
| ACTUAL_TERMINATION_DATE | WorkRelationshipPEOActualTerminationDate | ✅ |
| ADJUSTED_SVC_DATE | WorkRelationshipPEOAdjustedSvcDate | ✅ |
| BUSINESS_GROUP_ID | WorkRelationshipPEOBusinessGroupId | ✅ |
| COMMENTS | WorkRelationshipPEOComments | ✅ |
| CREATED_BY | WorkRelationshipPEOCreatedBy | ✅ |
| CREATION_DATE | WorkRelationshipPEOCreationDate | ✅ |
| DATE_EMPLOYEE_DATA_VERIFIED | WorkRelationshipPEODateEmployeeDataVerified | ✅ |
| DATE_START | WorkRelationshipPEODateStart | ✅ |
| FAST_PATH_EMPLOYEE | WorkRelationshipPEOFastPathEmployee | ✅ |
| LAST_UPDATE_DATE | WorkRelationshipPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | WorkRelationshipPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | WorkRelationshipPEOLastUpdatedBy | ✅ |
| LAST_WORKING_DATE | WorkRelationshipPEOLastWorkingDate | ✅ |
| LEGAL_ENTITY_ID | WorkRelationshipPEOLegalEntityId | ✅ |
| LEGISLATION_CODE | WorkRelationshipPEOLegislationCode | ✅ |
| NOTIFIED_TERMINATION_DATE | WorkRelationshipPEONotifiedTerminationDate | ✅ |
| OBJECT_VERSION_NUMBER | WorkRelationshipPEOObjectVersionNumber | — |
| ON_MILITARY_SERVICE | WorkRelationshipPEOOnMilitaryService | ✅ |
| ORIGINAL_DATE_OF_HIRE | WorkRelationshipPEOOriginalDateOfHire | ✅ |
| PERIOD_OF_SERVICE_ID | PeriodOfServiceId | ✅ |
| PERIOD_TYPE | WorkRelationshipPEOPeriodType | ✅ |
| PERSON_ID | WorkRelationshipPEOPersonId | ✅ |
| PRIMARY_FLAG | WorkRelationshipPEOPrimaryFlag | ✅ |
| PROJECTED_TERMINATION_DATE | WorkRelationshipPEOProjectedTerminationDate | ✅ |
| REHIRE_AUTHORIZER_PERSON_ID | WorkRelationshipPEORehireAuthorizerPersonId | — |
| REHIRE_AUTHORIZOR | WorkRelationshipPEORehireAuthorizor | ✅ |
| REHIRE_REASON | WorkRelationshipPEORehireReason | ✅ |
| REHIRE_RECOMMENDATION | WorkRelationshipPEORehireRecommendation | ✅ |
| REVOKE_USER_ACCESS | WorkRelationshipPEORevokeUserAccess | ✅ |
| TERMINATION_ACCEPTED_PERSON_ID | WorkRelationshipPEOTerminationAcceptedPersonId | — |
| WORKER_COMMENTS | WorkRelationshipPEOWorkerComments | ✅ |
| WORKER_NUMBER | WorkRelationshipPEOWorkerNumber | ✅ |
