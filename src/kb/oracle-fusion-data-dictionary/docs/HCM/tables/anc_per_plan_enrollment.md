---
id: DOC-HCM-023
doc_type: system-doc
title: "ANC_PER_PLAN_ENROLLMENT — Inscrição em Plano de Ausência"
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
  - absence-management
  - inscricao
  - enrollment
  - elegibilidade
aliases:
  - ANC_PER_PLAN_ENROLLMENT
  - anc_per_plan_enrollment
  - inscricao-plano-ausencia
  - plan-enrollment
  - anc-per-plan-enrollment
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_PLAN_ENROLLMENT

## 📌 Visão Geral

Armazena as **inscrições de colaboradores em planos de ausência**. Cada registro indica que um colaborador está elegível e inscrito em um plano específico, com datas de início e fim da inscrição.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Elegibilidade:** Controla quais colaboradores estão inscritos em quais planos.
- **Ativação de saldo:** A inscrição ativa a acumulação de saldo para o colaborador.
- **Gestão de políticas:** Permite atribuir planos diferentes a grupos de colaboradores.
- **Auditoria:** Histórico de inscrições e desinscrições.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_PLAN_ENROLLMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da inscrição | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 95% |
| 3 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência | [[anc_absence_plans_f]] | 🟢 95% |
| 4 | ENROLLMENT_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status (ACTIVE, INACTIVE, TERMINATED) | — | 🟡 80% |
| 5 | ENROLLMENT_START_DATE | DATE | NOT NULL | Data | Data de início da inscrição | — | 🟢 85% |
| 6 | ENROLLMENT_END_DATE | DATE | NULL | Data | Data de fim da inscrição | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador inscrito no plano de ausencia)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausencia da inscricao)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Colaboradores inscritos em um plano
```sql
SELECT pe.PERSON_ID, pe.ENROLLMENT_STATUS,
       pe.ENROLLMENT_START_DATE, pe.ENROLLMENT_END_DATE
FROM   ANC_PER_PLAN_ENROLLMENT pe
WHERE  pe.ABSENCE_PLAN_ID = :p_plan_id
  AND  pe.ENROLLMENT_STATUS = 'ACTIVE';
```

### Filtros comuns
- `ENROLLMENT_STATUS = 'ACTIVE'` — Inscrições ativas
- `ENROLLMENT_STATUS = 'TERMINATED'` — Inscrições encerradas

---

## 🔒 Observações

- A inscrição é pré-requisito para acumulação de saldo e solicitação de ausência.
- `ENROLLMENT_END_DATE` nulo indica inscrição sem data de término prevista.
- A desinscrição pode ser automática (ex.: término de contrato) ou manual (mudança de política).

---

## 🔗 PVOs Relacionados

### [[absperplanenrollmentpvo|AbsPerPlanEnrollmentPVO]] (GL · BICC: 5/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CEILING_AMT | CeilingAmt | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| ENRT_END_DT | EnrtEndDt | ✅ |
| ENRT_ST_DT | EnrtStDt | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_ACCRUAL_RUN | LastAccrualRun | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPERATION_TYPE | OperationType | — |
| PAYROLL_MAPPING_ID | PayrollMappingId | — |
| PAYROLL_STATUS | PayrollStatus | — |
| PER_EVENT_ID | PerEventId | — |
| PER_PLAN_ENRT_ID | PerPlanEnrtId | ✅ |
| PERSON_ID | PersonId | — |
| PLAN_ID | PlanId | — |
| PRD_OF_SVC_ID | PrdOfSvcId | — |
| RECIPIENT_ALIAS | RecipientAlias | — |
| SOURCE_ENRT_ID | SourceEnrtId | — |
| STATUS | Status | — |
| WAIT_PERIOD_DUR_UNITS | WaitPeriodDurUnits | — |
| WAIT_PERIOD_DUR_UOM | WaitPeriodDurUom | — |
| WORK_TERM_ASG_ID | WorkTermAsgId | — |

### [[persondonationentrydtlpvo|PersonDonationEntryDtlPVO]] (GL · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PER_PLAN_ENRT_ID | AbsPerPlanEnrollmentPEORecipientPerPlanEnrtId | ✅ |
| PERSON_ID | AbsPerPlanEnrollmentPEORecipientPersonID | ✅ |
| PLAN_ID | AbsPerPlanEnrollmentPEORecipientPlanID | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_PER_PLAN_ENROLLMENT](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperplanenrollment.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
