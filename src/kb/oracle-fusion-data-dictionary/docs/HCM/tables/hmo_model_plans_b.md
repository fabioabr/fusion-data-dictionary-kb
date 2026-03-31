---
id: DOC-HCM-130
doc_type: system-doc
title: "HMO_MODEL_PLANS_B — Planos de Modelo Organizacional (Base)"
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
  - workforce-modeling
  - modelo-organizacional
  - planejamento
  - hmo
aliases:
  - HMO_MODEL_PLANS_B
  - hmo_model_plans_b
  - hmo-model-plans-b
  - DOC-HCM-130
  - planos-de-modelo-organizacional-(base)
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HMO_MODEL_PLANS_B

## 📌 Visão Geral

Armazena as **definições base dos planos de modelo organizacional** — modelos de estrutura hierárquica usados para planejamento de mudanças organizacionais (fusões, reestruturações, novos departamentos).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Planejamento organizacional:** Modelos de estrutura para reorganizações.
- **Simulação de cenários:** Planos hipotéticos antes da efetivação.
- **Gestão de mudanças:** Controle de propostas de mudança organizacional.
- **Aprovação hierárquica:** Workflow de aprovação de modelos.
- **Base para tradução:** Complementada por `HMO_MODEL_PLANS_TL`.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MODEL_PLAN_ID | NUMBER(18) | NOT NULL | PK | Identificador único do plano de modelo | — | 🟢 90% |
| 2 | MODEL_PLAN_CODE | VARCHAR2(30) | NOT NULL | Identificação | Código do plano | — | 🟡 80% |
| 3 | STATUS_CODE | VARCHAR2(30) | NULL | Status | Status (DRAFT, PROPOSED, APPROVED, REJECTED) | — | 🟡 80% |
| 4 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade planejada | — | 🟡 80% |
| 5 | MODEL_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de modelo (RESTRUCTURE, MERGER, EXPANSION) | — | 🟡 70% |
| 6 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócios | [[per_business_groups]] | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Número de versão do objeto | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_business_groups]] — via `BUSINESS_GROUP_ID` (grupo empresarial do modelo de headcount)

### Tabelas-filha (FK de saída)
- [[hmo_model_plans_tl]] — via `MODEL_PLAN_ID` (traducoes multilingue do registro)
- [[hmo_model_plan_details]] — via `MODEL_PLAN_ID` (detalhes do modelo de headcount)

---

## 📎 Uso Típico

### Planos de modelo ativos
```sql
SELECT mp.MODEL_PLAN_ID, mp.MODEL_PLAN_CODE, mp.STATUS_CODE,
       mp.EFFECTIVE_DATE, mp.MODEL_TYPE
FROM   HMO_MODEL_PLANS_B mp
WHERE  mp.STATUS_CODE IN ('DRAFT', 'PROPOSED');
```

### Planos aprovados por tipo
```sql
SELECT mp.MODEL_TYPE, COUNT(*) AS qtd
FROM   HMO_MODEL_PLANS_B mp
WHERE  mp.STATUS_CODE = 'APPROVED'
GROUP BY mp.MODEL_TYPE;
```

---

## 🔒 Observações

- Tabela _B (base) contém dados independentes de idioma.
- Cada plano pode ter múltiplos detalhes em `HMO_MODEL_PLAN_DETAILS`.
- O `STATUS_CODE` controla o ciclo: DRAFT -> PROPOSED -> APPROVED/REJECTED.
- Planos aprovados podem ser efetivados na estrutura organizacional real.

---

## 🔗 PVOs Relacionados

### [[modelplandetailsfactpvo|ModelPlanDetailsFactPVO]] (HCM · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_TOP_MANAGER | ModelPlanPEOAccessToTopManager | — |
| ACTION_ID | ModelPlanPEOActionId | — |
| ACTION_REASON_ID | ModelPlanPEOActionReasonId | — |
| AUTHOR_PERSON_ID | ModelPlanPEOAuthorPersonId | — |
| CREATED_BY | ModelPlanPEOCreatedBy | — |
| CREATION_DATE | ModelPlanPEOCreationDate | — |
| EFFECTIVE_DATE | ModelPlanPEOEffectiveDate | — |
| ENTERPRISE_ID | ModelPlanPEOEnterpriseId | — |
| LAST_SYNC_DATE | ModelPlanPEOLastSyncDate | — |
| LAST_UPDATE_DATE | ModelPlanPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ModelPlanPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ModelPlanPEOLastUpdatedBy | — |
| MODEL_LOADER_BATCH_ID | ModelPlanPEOModelLoaderBatchId | — |
| MODEL_PLAN_ID | ModelPlanPEOModelPlanId | — |
| MODEL_PLAN_STATUS | ModelPlanPEOModelPlanStatus | — |
| MODEL_PLAN_TYPE | ModelPlanPEOModelPlanType | ✅ |
| OBJECT_VERSION_NUMBER | ModelPlanPEOObjectVersionNumber | — |
| TOP_MANAGER_ASSIGNMENT_ID | ModelPlanPEOTopManagerAssignmentId | — |
| TOP_MANAGER_ID | ModelPlanPEOTopManagerId | — |
| TOP_MANAGER_TYPE | ModelPlanPEOTopManagerType | — |

### [[modelplandetailspvomodel|ModelPlanDetailsPVOModel]] (HCM · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_TOP_MANAGER | ModelPlanPEOAccessToTopManager | — |
| ACTION_ID | ModelPlanPEOActionId | — |
| ACTION_REASON_ID | ModelPlanPEOActionReasonId | — |
| AUTHOR_PERSON_ID | ModelPlanPEOAuthorPersonId | — |
| CREATED_BY | ModelPlanPEOCreatedBy | — |
| CREATION_DATE | ModelPlanPEOCreationDate | — |
| EFFECTIVE_DATE | ModelPlanPEOEffectiveDate | — |
| ENTERPRISE_ID | ModelPlanPEOEnterpriseId | — |
| LAST_SYNC_DATE | ModelPlanPEOLastSyncDate | — |
| LAST_UPDATE_DATE | ModelPlanPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ModelPlanPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ModelPlanPEOLastUpdatedBy | — |
| MODEL_LOADER_BATCH_ID | ModelPlanPEOModelLoaderBatchId | — |
| MODEL_PLAN_ID | ModelPlanPEOModelPlanId | — |
| MODEL_PLAN_STATUS | ModelPlanPEOModelPlanStatus | — |
| MODEL_PLAN_TYPE | ModelPlanPEOModelPlanType | ✅ |
| OBJECT_VERSION_NUMBER | ModelPlanPEOObjectVersionNumber | — |
| TOP_MANAGER_ASSIGNMENT_ID | ModelPlanPEOTopManagerAssignmentId | — |
| TOP_MANAGER_ID | ModelPlanPEOTopManagerId | — |
| TOP_MANAGER_TYPE | ModelPlanPEOTopManagerType | — |

### [[modelplanpvo|ModelPlanPVO]] (HCM · BICC: 10/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_TOP_MANAGER | AccessToTopManager | ✅ |
| ACTION_ID | ActionId | — |
| ACTION_REASON_ID | ActionReasonId | — |
| AUTHOR_PERSON_ID | AuthorPersonId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_DATE | EffectiveDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_SYNC_DATE | LastSyncDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODEL_LOADER_BATCH_ID | ModelLoaderBatchId | — |
| MODEL_PLAN_ID | ModelPlanId | ✅ |
| MODEL_PLAN_STATUS | ModelPlanStatus | ✅ |
| MODEL_PLAN_TYPE | ModelPlanType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| TOP_MANAGER_ASSIGNMENT_ID | TopManagerAssignmentId | — |
| TOP_MANAGER_ID | TopManagerId | — |
| TOP_MANAGER_TYPE | TopManagerType | — |

### [[modelplanpvoviewall|ModelPlanPVOViewAll]] (HCM · BICC: 10/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCESS_TO_TOP_MANAGER | AccessToTopManager | ✅ |
| ACTION_ID | ActionId | — |
| ACTION_REASON_ID | ActionReasonId | — |
| AUTHOR_PERSON_ID | AuthorPersonId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_DATE | EffectiveDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_SYNC_DATE | LastSyncDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MODEL_LOADER_BATCH_ID | ModelLoaderBatchId | — |
| MODEL_PLAN_ID | ModelPlanId | ✅ |
| MODEL_PLAN_STATUS | ModelPlanStatus | ✅ |
| MODEL_PLAN_TYPE | ModelPlanType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| TOP_MANAGER_ASSIGNMENT_ID | TopManagerAssignmentId | — |
| TOP_MANAGER_ID | TopManagerId | — |
| TOP_MANAGER_TYPE | TopManagerType | — |

---

## 📚 Referências

- [Oracle Docs — HMO_MODEL_PLANS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hmomodelplansb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
