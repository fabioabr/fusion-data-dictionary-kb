---
id: DOC-HCM-018
doc_type: system-doc
title: "ANC_PER_ABS_PLAN_ENTRIES — Entradas de Plano de Ausência por Pessoa"
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
  - entradas-plano
  - plan-entries
  - saldo-ausencia
aliases:
  - ANC_PER_ABS_PLAN_ENTRIES
  - anc_per_abs_plan_entries
  - entradas-plano-ausencia
  - absence-plan-entries
  - anc-per-abs-plan-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_PLAN_ENTRIES

## 📌 Visão Geral

Armazena as **entradas de ausência vinculadas a planos específicos** por colaborador. Associa cada ausência a um plano para controle de saldo e acumulação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de saldo:** Vincula ausências a planos para dedução de saldo.
- **Acumulação:** Rastreamento de consumo de saldo por plano.
- **Relatórios por plano:** Análise de uso de ausências por plano específico.
- **Validação de saldo:** Verificação de saldo disponível antes de aprovar ausência.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_PLAN_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de ausência | [[anc_per_abs_entries]] | 🟢 90% |
| 3 | ABSENCE_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de ausência | [[anc_absence_plans_f]] | 🟢 90% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 5 | DURATION | NUMBER | NULL | Duração | Duração consumida do plano | — | 🟡 80% |
| 6 | DURATION_UOM | VARCHAR2(30) | NULL | Classificação | Unidade de medida | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia vinculado ao plano)
- [[anc_absence_plans_f]] — via `ABSENCE_PLAN_ID` (plano de ausencia do lancamento)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do lancamento no plano de ausencia)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Consumo de saldo por plano
```sql
SELECT pe.ABSENCE_PLAN_ID, p.PLAN_NAME,
       SUM(pe.DURATION) AS total_consumido
FROM   ANC_PER_ABS_PLAN_ENTRIES pe
JOIN   ANC_ABSENCE_PLANS_F p ON pe.ABSENCE_PLAN_ID = p.ABSENCE_PLAN_ID
WHERE  pe.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN p.EFFECTIVE_START_DATE AND p.EFFECTIVE_END_DATE
GROUP BY pe.ABSENCE_PLAN_ID, p.PLAN_NAME;
```

### Filtros comuns
- `PERSON_ID = :p_person_id` — Ausências de um colaborador específico

---

## 🔒 Observações

- Associa cada ausência a um plano específico para controle de saldo.
- Um colaborador pode estar inscrito em múltiplos planos; cada ausência consome saldo de um plano específico.
- O saldo disponível é calculado pela diferença entre acumulação e consumo.

---

## 🔗 PVOs Relacionados

### [[personabsplanentryextractpvo|PersonAbsPlanEntryExtractPVO]] (HCM · BICC: 29/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_UNITS | AbsUnits | ✅ |
| ABSENCE_PAY_FACTOR | AbsencePayFactor | ✅ |
| ABSENCE_PLAN_ID | AbsencePlanId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| END_DATE | EndDate | ✅ |
| END_DATETIME | EndDatetime | ✅ |
| END_TIME | EndTime | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| ENTITLEMENT_DATE | EntitlementDate | ✅ |
| HEADER_ID | HeaderId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PER_ABS_PLAN_ENTRY_ID | PerAbsPlanEntryId | ✅ |
| PER_ABS_PLN_SUMM_ENTRY_ID | PerAbsPlnSummEntryId | ✅ |
| PER_ABS_TYPE_ENTRY_ID | PerAbsTypeEntryId | ✅ |
| PER_ABSENCE_ENTRY_ID | PerAbsenceEntryId | ✅ |
| PER_ACCRUAL_ENTRY_DTL_ID | PerAccrualEntryDtlId | — |
| PERSON_ID | PersonId | ✅ |
| QUALIFICATION_DATE | QualificationDate | ✅ |
| RATE_DEFINITION_ID | RateDefinitionId | ✅ |
| SCHEDULED_UNITS | ScheduledUnits | ✅ |
| START_DATE | StartDate | ✅ |
| START_DATETIME | StartDatetime | ✅ |
| START_TIME | StartTime | ✅ |
| TM_REC_ID | TmRecId | ✅ |
| UOM | Uom | ✅ |

### [[personabsplanentrypvo|PersonAbsPlanEntryPVO]] (GL · BICC: 13/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_UNITS | AbsUnits | ✅ |
| ABSENCE_PAY_FACTOR | AbsencePayFactor | ✅ |
| ABSENCE_PLAN_ID | AbsencePlanId | — |
| ASSIGNMENT_ID | AssignmentId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| END_DATE | EndDate | ✅ |
| END_DATETIME | EndDatetime | ✅ |
| END_TIME | EndTime | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| ENTITLEMENT_DATE | EntitlementDate | — |
| HEADER_ID | HeaderId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_ABS_PLAN_ENTRY_ID | PerAbsPlanEntryId | ✅ |
| PER_ABS_PLN_SUMM_ENTRY_ID | PerAbsPlnSummEntryId | — |
| PER_ABS_TYPE_ENTRY_ID | PerAbsTypeEntryId | — |
| PER_ABSENCE_ENTRY_ID | PerAbsenceEntryId | — |
| PERSON_ID | PersonId | — |
| QUALIFICATION_DATE | QualificationDate | — |
| RATE_DEFINITION_ID | RateDefinitionId | ✅ |
| SCHEDULED_UNITS | ScheduledUnits | ✅ |
| START_DATE | StartDate | ✅ |
| START_DATETIME | StartDatetime | ✅ |
| START_TIME | StartTime | ✅ |
| TM_REC_ID | TmRecId | — |
| UOM | Uom | — |

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_PLAN_ENTRIES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsplanentries.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
