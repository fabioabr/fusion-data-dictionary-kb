---
id: DOC-HCM-743
doc_type: system-doc
title: "WLF_PLAN_PROFILES_F — Perfis de Planos de Aprendizado"
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
  - learning
  - workforce-learning
  - perfis-plano
aliases:
  - WLF_PLAN_PROFILES_F
  - wlf_plan_profiles_f
  - wlf-plan-profiles-f
  - perfis-planos-aprendizado
  - plan-profiles
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_PLAN_PROFILES_F

## Visão Geral

Armazena os **perfis de elegibilidade** associados a planos de aprendizado, definindo quais critérios (cargo, departamento, competência) determinam a elegibilidade para cada plano. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Elegibilidade automática** — define quais colaboradores são elegíveis para cada plano.
- **Segmentação** — distribui planos de aprendizado por perfil organizacional.
- **Compliance** — garante que perfis regulatórios recebam planos obrigatórios.
- **Personalização** — permite planos customizados por cargo, departamento ou competência.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PLAN_PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do perfil | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_PLAN_ID | NUMBER(18) | NOT NULL | FK | Plano de aprendizado associado | WLF_LEARNING_PLANS_F | 🟢 85% |
| 5 | PROFILE_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de perfil (JOB, DEPT, COMPETENCY) | — | 🟡 70% |
| 6 | PROFILE_VALUE_ID | NUMBER(18) | NULL | FK | ID do valor do perfil (job_id, dept_id, etc.) | — | 🟡 70% |
| 7 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Plano é obrigatório para este perfil (Y/N) | — | 🟡 70% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_plans_f]] — via `LEARNING_PLAN_ID` (plano de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Perfis de elegibilidade de um plano
```sql
SELECT pp.PROFILE_TYPE, pp.PROFILE_VALUE_ID, pp.MANDATORY_FLAG
FROM   WLF_PLAN_PROFILES_F pp
WHERE  pp.LEARNING_PLAN_ID = :p_plan_id
  AND  SYSDATE BETWEEN pp.EFFECTIVE_START_DATE AND pp.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LEARNING_PLAN_ID = :p_plan_id` — Perfis de um plano específico
- `MANDATORY_FLAG = 'Y'` — Apenas perfis obrigatórios

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- PROFILE_VALUE_ID é polimórfico — o tipo é definido por PROFILE_TYPE.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Fundamental para atribuição automática de planos de aprendizado.

---

## Referências

- [Oracle Docs — WLF_PLAN_PROFILES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfplanprofilesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[learningplanprofilespvo|LearningPlanProfilesPVO]] (HCM · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PlanProfileDEOCreatedBy | — |
| CREATION_DATE | PlanProfileDEOCreationDate | — |
| EFFECTIVE_END_DATE | PlanProfileDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PlanProfileDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | PlanProfileDEOEnterpriseId | — |
| EVENT_ASSIGNMENT_ID | PlanProfileDEOEventAssignmentId | — |
| EVENT_ID | PlanProfileDEOEventId | — |
| INITIAL_PLAN_RECORD_STATUS | PlanProfileDEOInitialPlanRecordStatus | — |
| LAST_UPDATE_DATE | PlanProfileDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PlanProfileDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PlanProfileDEOLastUpdatedBy | — |
| LEARNING_PLAN_ID | PlanProfileDEOLearningPlanId | — |
| OBJECT_VERSION_NUMBER | PlanProfileDEOObjectVersionNumber | — |
| PLAN_PROFILE_ID | PlanProfileDEOPlanProfileId | ✅ |
| PLAN_PROFILE_TYPE | PlanProfileDEOPlanProfileType | ✅ |
