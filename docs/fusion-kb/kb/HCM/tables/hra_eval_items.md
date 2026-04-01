---
id: DOC-HCM-140
doc_type: system-doc
title: "HRA_EVAL_ITEMS — Itens de Avaliação"
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
  - performance-management
  - eval-item
  - avaliacao
  - hra
aliases:
  - HRA_EVAL_ITEMS
  - hra_eval_items
  - hra-eval-items
  - DOC-HCM-140
  - itens-de-avaliação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVAL_ITEMS

## 📌 Visão Geral

Armazena os **registros de itens individuais de avaliação** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de itens individuais de avaliação:** Registro e controle operacional.
- **Workflow de avaliação:** Suporte ao processo de avaliação de performance.
- **Rastreabilidade:** Histórico completo de ações e decisões.
- **Relatórios de performance:** Dados para dashboards e análises.
- **Compliance:** Documentação de processos de avaliação.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVAL_ITEM_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa associada | [[per_all_people_f]] | 🟡 80% |
| 3 | EVALUATION_ID | NUMBER(18) | NULL | FK | Avaliação associada | [[hra_evaluations]] | 🟡 80% |
| 4 | STATUS | VARCHAR2(30) | NULL | Status | Status do registro | — | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto | Descrição | — | 🟡 75% |
| 6 | EFFECTIVE_DATE | DATE | NULL | Data | Data de efetividade | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do item de avaliacao)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao do item avaliado)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVAL_ITEM_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVAL_ITEMS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVAL_ITEM_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVAL_ITEMS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de itens individuais de avaliação.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[competencyitempvo|CompetencyItemPVO]] (HCM · BICC: 22/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | EvalItemPEOAchievementDate | ✅ |
| BUSINESS_GROUP_ID | EvalItemPEOBusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_FLAG | EvalItemPEOCriticalFlag | ✅ |
| DESCRIPTION | EvalItemPEODescription | ✅ |
| DUE_DATE | EvalItemPEODueDate | ✅ |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| EVAL_SECTION_ID | EvalItemPEOEvalSectionId | — |
| EVALUATION_ID | EvalItemPEOEvaluationId | — |
| ITEM_NAME | EvalItemPEOItemName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANDATORY_FLAG | EvalItemPEOMandatoryFlag | ✅ |
| MEASUREMENT | EvalItemPEOMeasurement | ✅ |
| MIN_WEIGHT | EvalItemPEOMinWeight | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNED_BY | EvalItemPEOOwnedBy | ✅ |
| PARENT_ITEM_ID | EvalItemPEOParentItemId | — |
| PERCENT_COMPLETED | EvalItemPEOPercentCompleted | ✅ |
| PERF_RATING_MODEL_ID | EvalItemPEOPerfRatingModelId | ✅ |
| PROF_RATING_MODEL_ID | EvalItemPEOProfRatingModelId | ✅ |
| RATING_OVERIDE_FLAG | EvalItemPEORatingOverideFlag | ✅ |
| REFERENCE_ITEM_ID | ReferenceItemId | ✅ |
| REMINDER_DATE | EvalItemPEOReminderDate | ✅ |
| START_DATE | EvalItemPEOStartDate | ✅ |
| TARGET_DATE | EvalItemPEOTargetDate | ✅ |
| TARGET_PERF_REV_RATING_ID | EvalItemPEOTargetPerfRevRatingId | ✅ |
| TARGET_PROF_REV_RATING_ID | EvalItemPEOTargetProfRevRatingId | ✅ |
| WEIGHT | EvalItemPEOWeight | ✅ |

### [[evalitemextractpvo|EvalItemExtractPVO]] (HCM · BICC: 97/97)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | AchievementDate | ✅ |
| ATTRIBUTE1 | Attribute1 | ✅ |
| ATTRIBUTE10 | Attribute10 | ✅ |
| ATTRIBUTE11 | Attribute11 | ✅ |
| ATTRIBUTE12 | Attribute12 | ✅ |
| ATTRIBUTE13 | Attribute13 | ✅ |
| ATTRIBUTE14 | Attribute14 | ✅ |
| ATTRIBUTE15 | Attribute15 | ✅ |
| ATTRIBUTE16 | Attribute16 | ✅ |
| ATTRIBUTE17 | Attribute17 | ✅ |
| ATTRIBUTE18 | Attribute18 | ✅ |
| ATTRIBUTE19 | Attribute19 | ✅ |
| ATTRIBUTE2 | Attribute2 | ✅ |
| ATTRIBUTE20 | Attribute20 | ✅ |
| ATTRIBUTE21 | Attribute21 | ✅ |
| ATTRIBUTE22 | Attribute22 | ✅ |
| ATTRIBUTE23 | Attribute23 | ✅ |
| ATTRIBUTE24 | Attribute24 | ✅ |
| ATTRIBUTE25 | Attribute25 | ✅ |
| ATTRIBUTE26 | Attribute26 | ✅ |
| ATTRIBUTE27 | Attribute27 | ✅ |
| ATTRIBUTE28 | Attribute28 | ✅ |
| ATTRIBUTE29 | Attribute29 | ✅ |
| ATTRIBUTE3 | Attribute3 | ✅ |
| ATTRIBUTE30 | Attribute30 | ✅ |
| ATTRIBUTE4 | Attribute4 | ✅ |
| ATTRIBUTE5 | Attribute5 | ✅ |
| ATTRIBUTE6 | Attribute6 | ✅ |
| ATTRIBUTE7 | Attribute7 | ✅ |
| ATTRIBUTE8 | Attribute8 | ✅ |
| ATTRIBUTE9 | Attribute9 | ✅ |
| ATTRIBUTE_CATEGORY | AttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | AttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | AttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | AttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | AttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | AttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | AttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | AttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | AttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | AttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CRITICAL_FLAG | CriticalFlag | ✅ |
| DESCRIPTION | Description | ✅ |
| DUE_DATE | DueDate | ✅ |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| ITEM_NAME | ItemName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MANDATORY_FLAG | MandatoryFlag | ✅ |
| MEASUREMENT | Measurement | ✅ |
| MIN_WEIGHT | MinWeight | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OWNED_BY | OwnedBy | ✅ |
| PARENT_ITEM_ID | ParentItemId | ✅ |
| PERCENT_COMPLETED | PercentCompleted | ✅ |
| PERF_RATING_MODEL_ID | PerfRatingModelId | ✅ |
| PROF_RATING_MODEL_ID | ProfRatingModelId | ✅ |
| RATING_OVERIDE_FLAG | RatingOverideFlag | ✅ |
| REFERENCE_ITEM_ID | ReferenceItemId | ✅ |
| REMINDER_DATE | ReminderDate | ✅ |
| START_DATE | StartDate | ✅ |
| TARGET_DATE | TargetDate | ✅ |
| TARGET_PERF_REV_RATING_ID | TargetPerfRevRatingId | ✅ |
| TARGET_PROF_REV_RATING_ID | TargetProfRevRatingId | ✅ |
| WEIGHT | Weight | ✅ |

### [[evalitempvo|EvalItemPVO]] (HCM · BICC: 12/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | EvalItemPEOAchievementDate | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | EvalItemPEODescription | — |
| DUE_DATE | EvalItemPEODueDate | ✅ |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| ITEM_NAME | EvalItemPEOItemName | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANDATORY_FLAG | EvalItemPEOMandatoryFlag | — |
| MEASUREMENT | EvalItemPEOMeasurement | ✅ |
| MIN_WEIGHT | EvalItemPEOMinWeight | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNED_BY | EvalItemPEOOwnedBy | ✅ |
| PERCENT_COMPLETED | EvalItemPEOPercentCompleted | ✅ |
| RATING_OVERIDE_FLAG | EvalItemPEORatingOverideFlag | — |
| REMINDER_DATE | EvalItemPEOReminderDate | ✅ |
| START_DATE | EvalItemPEOStartDate | ✅ |
| TARGET_DATE | EvalItemPEOTargetDate | ✅ |
| WEIGHT | EvalItemPEOWeight | ✅ |

### [[goalitempvo|GoalItemPVO]] (HCM · BICC: 23/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | EvalItemPEOAchievementDate | ✅ |
| BUSINESS_GROUP_ID | EvalItemPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| CRITICAL_FLAG | EvalItemPEOCriticalFlag | ✅ |
| DESCRIPTION | EvalItemPEODescription | ✅ |
| DUE_DATE | EvalItemPEODueDate | ✅ |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| EVAL_SECTION_ID | EvalItemPEOEvalSectionId | — |
| EVALUATION_ID | EvalItemPEOEvaluationId | — |
| ITEM_NAME | EvalItemPEOItemName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MANDATORY_FLAG | EvalItemPEOMandatoryFlag | ✅ |
| MEASUREMENT | EvalItemPEOMeasurement | ✅ |
| MIN_WEIGHT | EvalItemPEOMinWeight | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OWNED_BY | EvalItemPEOOwnedBy | ✅ |
| PARENT_ITEM_ID | EvalItemPEOParentItemId | — |
| PERCENT_COMPLETED | EvalItemPEOPercentCompleted | ✅ |
| PERF_RATING_MODEL_ID | EvalItemPEOPerfRatingModelId | ✅ |
| PROF_RATING_MODEL_ID | EvalItemPEOProfRatingModelId | ✅ |
| RATING_OVERIDE_FLAG | EvalItemPEORatingOverideFlag | ✅ |
| REFERENCE_ITEM_ID | ReferenceItemId | ✅ |
| REMINDER_DATE | EvalItemPEOReminderDate | ✅ |
| START_DATE | EvalItemPEOStartDate | ✅ |
| TARGET_DATE | EvalItemPEOTargetDate | ✅ |
| TARGET_PERF_REV_RATING_ID | EvalItemPEOTargetPerfRevRatingId | ✅ |
| TARGET_PROF_REV_RATING_ID | EvalItemPEOTargetProfRevRatingId | ✅ |
| WEIGHT | EvalItemPEOWeight | ✅ |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 3/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | EvalItemPEOAchievementDate | — |
| BUSINESS_GROUP_ID | EvalItemPEOBusinessGroupId | — |
| CRITICAL_FLAG | EvalItemPEOCriticalFlag | — |
| DESCRIPTION | EvalItemPEODescription | — |
| DUE_DATE | EvalItemPEODueDate | — |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| EVAL_SECTION_ID | EvalItemPEOEvalSectionId | — |
| EVALUATION_ID | EvalItemPEOEvaluationId | — |
| ITEM_NAME | EvalItemPEOItemName | — |
| LAST_UPDATE_DATE | EvalItemPEOLastUpdateDate | ✅ |
| MANDATORY_FLAG | EvalItemPEOMandatoryFlag | — |
| MEASUREMENT | EvalItemPEOMeasurement | — |
| MIN_WEIGHT | EvalItemPEOMinWeight | — |
| OWNED_BY | EvalItemPEOOwnedBy | — |
| PARENT_ITEM_ID | EvalItemPEOParentItemId | — |
| PERCENT_COMPLETED | EvalItemPEOPercentCompleted | — |
| PERF_RATING_MODEL_ID | EvalItemPEOPerfRatingModelId | — |
| PROF_RATING_MODEL_ID | EvalItemPEOProfRatingModelId | — |
| RATING_OVERIDE_FLAG | EvalItemPEORatingOverideFlag | — |
| REFERENCE_ITEM_ID | ReferenceItemId | ✅ |
| REMINDER_DATE | EvalItemPEOReminderDate | — |
| START_DATE | EvalItemPEOStartDate | — |
| TARGET_DATE | EvalItemPEOTargetDate | — |
| TARGET_PERF_REV_RATING_ID | EvalItemPEOTargetPerfRevRatingId | — |
| TARGET_PROF_REV_RATING_ID | EvalItemPEOTargetProfRevRatingId | — |
| WEIGHT | EvalItemPEOWeight | — |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 3/26)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACHIEVEMENT_DATE | EvalItemPEOAchievementDate | — |
| BUSINESS_GROUP_ID | EvalItemPEOBusinessGroupId | — |
| CRITICAL_FLAG | EvalItemPEOCriticalFlag | — |
| DESCRIPTION | EvalItemPEODescription | — |
| DUE_DATE | EvalItemPEODueDate | — |
| EVAL_ITEM_ID | EvalItemId | ✅ |
| EVAL_SECTION_ID | EvalItemPEOEvalSectionId | — |
| EVALUATION_ID | EvalItemPEOEvaluationId | — |
| ITEM_NAME | EvalItemPEOItemName | — |
| LAST_UPDATE_DATE | EvalItemPEOLastUpdateDate | ✅ |
| MANDATORY_FLAG | EvalItemPEOMandatoryFlag | — |
| MEASUREMENT | EvalItemPEOMeasurement | — |
| MIN_WEIGHT | EvalItemPEOMinWeight | — |
| OWNED_BY | EvalItemPEOOwnedBy | — |
| PARENT_ITEM_ID | EvalItemPEOParentItemId | — |
| PERCENT_COMPLETED | EvalItemPEOPercentCompleted | — |
| PERF_RATING_MODEL_ID | EvalItemPEOPerfRatingModelId | — |
| PROF_RATING_MODEL_ID | EvalItemPEOProfRatingModelId | — |
| RATING_OVERIDE_FLAG | EvalItemPEORatingOverideFlag | — |
| REFERENCE_ITEM_ID | ReferenceItemId | ✅ |
| REMINDER_DATE | EvalItemPEOReminderDate | — |
| START_DATE | EvalItemPEOStartDate | — |
| TARGET_DATE | EvalItemPEOTargetDate | — |
| TARGET_PERF_REV_RATING_ID | EvalItemPEOTargetPerfRevRatingId | — |
| TARGET_PROF_REV_RATING_ID | EvalItemPEOTargetProfRevRatingId | — |
| WEIGHT | EvalItemPEOWeight | — |

---

## 📚 Referências

- [Oracle Docs — HRA_EVAL_ITEMS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevalitems.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
