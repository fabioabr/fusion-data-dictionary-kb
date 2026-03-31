---
id: DOC-HCM-139
doc_type: system-doc
title: "HRA_EVALUATIONS — Avaliações de Performance"
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
  - evaluation
  - avaliacao
  - hra
aliases:
  - HRA_EVALUATIONS
  - hra_evaluations
  - hra-evaluations
  - DOC-HCM-139
  - avaliações-de-performance
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVALUATIONS

## 📌 Visão Geral

Armazena os **registros de avaliações de performance** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de avaliações de performance:** Registro e controle operacional.
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
| 1 | EVALUATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
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
- [[per_all_people_f]] — via `PERSON_ID` (colaborador avaliado)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao anterior vinculada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVALUATION_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVALUATIONS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVALUATION_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVALUATIONS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de avaliações de performance.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[evaluationextractpvo|EvaluationExtractPVO]] (HCM · BICC: 103/103)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | ✅ |
| ACTION_PERFORMED_BY | ActionPerformedBy | ✅ |
| ACTION_PERFORMED_DATE | ActionPerformedDate | ✅ |
| ACTION_REASON | ActionReason | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
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
| CALCULATION_RATINGS_FLAG | CalculationRatingsFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DECIMAL_PLACES | DecimalPlaces | ✅ |
| END_DATE | EndDate | ✅ |
| EVALUATION_DATE | EvaluationDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | LanguageCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOCKED_BY_USER_ID | LockedByUserId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_COMMENTS | ManagerComments | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MAPPING_METHOD_CODE | MappingMethodCode | ✅ |
| MEETING_HELD_DATE | MeetingHeldDate | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PREV_STATUS_CODE | PrevStatusCode | ✅ |
| REVIEW_PERIOD_ID | ReviewPeriodId | ✅ |
| ROUNDING_RULE_CODE | RoundingRuleCode | ✅ |
| SELECT_MANAGER_ALLOWED_FLAG | SelectManagerAllowedFlag | ✅ |
| STAR_RATING_ENABLED_FLAG | StarRatingEnabledFlag | ✅ |
| START_DATE | StartDate | ✅ |
| STATUS_CODE | StatusCode | ✅ |
| TEMPLATE_DEFN_ID | TemplateDefnId | ✅ |
| TEMPLATE_TYPE_CODE | TemplateTypeCode | ✅ |
| TMPL_PERIOD_ID | TmplPeriodId | ✅ |
| WORKER_COMMENTS | WorkerComments | ✅ |
| WORKER_ID | WorkerId | ✅ |

### [[evaluationparticipantratingpvo|EvaluationParticipantRatingPVO]] (HCM · BICC: 14/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | EvaluationPEOAssignmentId | — |
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | ✅ |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | ✅ |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | ✅ |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | ✅ |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | ✅ |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | ✅ |
| START_DATE | EvaluationPEOStartDate | ✅ |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[evaluationpvo|EvaluationPVO]] (HCM · BICC: 17/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | EvaluationPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| END_DATE | EvaluationPEOEndDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| START_DATE | EvaluationPEOStartDate | ✅ |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | ✅ |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | ✅ |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | ✅ |
| WORKER_ID | EvaluationPEOWorkerId | ✅ |

### [[managerperformanceoverallratingpvo|ManagerPerformanceOverallRatingPVO]] (HCM · BICC: 11/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | EvaluationPEOAssignmentId | ✅ |
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | ✅ |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | ✅ |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | ✅ |

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM · BICC: 4/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | ✅ |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[performancedocumentdetailspvo|PerformanceDocumentDetailsPVO]] (HCM · BICC: 9/101)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | ActionCode | — |
| ACTION_PERFORMED_BY | ActionPerformedBy | — |
| ACTION_PERFORMED_DATE | ActionPerformedDate | — |
| ACTION_REASON | ActionReason | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | CalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | DecimalPlaces | — |
| END_DATE | EndDate | ✅ |
| EVALUATION_DATE | EvaluationDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | LanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | LockedByUserId | — |
| MANAGER_COMMENTS | ManagerComments | — |
| MANAGER_ID | ManagerId | ✅ |
| MAPPING_METHOD_CODE | MappingMethodCode | — |
| MEETING_HELD_DATE | MeetingHeldDate | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | PrevStatusCode | — |
| ROUNDING_RULE_CODE | RoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | SelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | StarRatingEnabledFlag | — |
| START_DATE | StartDate | ✅ |
| STATUS_CODE | StatusCode | ✅ |
| TEMPLATE_DEFN_ID | TemplateDefnId | — |
| TEMPLATE_TYPE_CODE | TemplateTypeCode | — |
| TMPL_PERIOD_ID | TmplPeriodId | — |
| WORKER_COMMENTS | WorkerComments | — |
| WORKER_ID | WorkerId | — |

### [[performancedocumentspvo|PerformanceDocumentsPVO]] (HCM · BICC: 19/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | ✅ |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | ✅ |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | ✅ |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | ✅ |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | ✅ |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | ✅ |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | ✅ |
| START_DATE | EvaluationPEOStartDate | ✅ |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | ✅ |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[performancedocumentstatuspvo|PerformanceDocumentStatusPVO]] (HCM · BICC: 19/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | ✅ |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | ✅ |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | ✅ |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | ✅ |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | ✅ |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | ✅ |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | ✅ |
| START_DATE | EvaluationPEOStartDate | ✅ |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | ✅ |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 3/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 5/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | ✅ |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 5/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | ✅ |

### [[performancesubtaskstatuspvo|PerformanceSubTaskStatusPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationPEOEvaluationId | — |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | — |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[performancetaskstatuspvo|PerformanceTaskStatusPVO]] (HCM · BICC: 2/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationPEOEvaluationId | — |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | ✅ |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 3/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | ✅ |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

### [[templateperiodevaluationpvo|TemplatePeriodEvaluationPVO]] (HCM · BICC: 2/95)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | EvaluationPEOAssignmentId | — |
| ATTRIBUTE1 | EvaluationPEOAttribute1 | — |
| ATTRIBUTE10 | EvaluationPEOAttribute10 | — |
| ATTRIBUTE11 | EvaluationPEOAttribute11 | — |
| ATTRIBUTE12 | EvaluationPEOAttribute12 | — |
| ATTRIBUTE13 | EvaluationPEOAttribute13 | — |
| ATTRIBUTE14 | EvaluationPEOAttribute14 | — |
| ATTRIBUTE15 | EvaluationPEOAttribute15 | — |
| ATTRIBUTE16 | EvaluationPEOAttribute16 | — |
| ATTRIBUTE17 | EvaluationPEOAttribute17 | — |
| ATTRIBUTE18 | EvaluationPEOAttribute18 | — |
| ATTRIBUTE19 | EvaluationPEOAttribute19 | — |
| ATTRIBUTE2 | EvaluationPEOAttribute2 | — |
| ATTRIBUTE20 | EvaluationPEOAttribute20 | — |
| ATTRIBUTE21 | EvaluationPEOAttribute21 | — |
| ATTRIBUTE22 | EvaluationPEOAttribute22 | — |
| ATTRIBUTE23 | EvaluationPEOAttribute23 | — |
| ATTRIBUTE24 | EvaluationPEOAttribute24 | — |
| ATTRIBUTE25 | EvaluationPEOAttribute25 | — |
| ATTRIBUTE26 | EvaluationPEOAttribute26 | — |
| ATTRIBUTE27 | EvaluationPEOAttribute27 | — |
| ATTRIBUTE28 | EvaluationPEOAttribute28 | — |
| ATTRIBUTE29 | EvaluationPEOAttribute29 | — |
| ATTRIBUTE3 | EvaluationPEOAttribute3 | — |
| ATTRIBUTE30 | EvaluationPEOAttribute30 | — |
| ATTRIBUTE4 | EvaluationPEOAttribute4 | — |
| ATTRIBUTE5 | EvaluationPEOAttribute5 | — |
| ATTRIBUTE6 | EvaluationPEOAttribute6 | — |
| ATTRIBUTE7 | EvaluationPEOAttribute7 | — |
| ATTRIBUTE8 | EvaluationPEOAttribute8 | — |
| ATTRIBUTE9 | EvaluationPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | EvaluationPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | EvaluationPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | EvaluationPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | EvaluationPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | EvaluationPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | EvaluationPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | EvaluationPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | EvaluationPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | EvaluationPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | EvaluationPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | EvaluationPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | EvaluationPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | EvaluationPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | EvaluationPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | EvaluationPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | EvaluationPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | EvaluationPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | EvaluationPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | EvaluationPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | EvaluationPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | EvaluationPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | EvaluationPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | EvaluationPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | EvaluationPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | EvaluationPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | EvaluationPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | EvaluationPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | EvaluationPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | EvaluationPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | EvaluationPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | EvaluationPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | EvaluationPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | EvaluationPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | EvaluationPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | EvaluationPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | EvaluationPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | EvaluationPEOBusinessGroupId1 | — |
| CALCULATION_RATINGS_FLAG | EvaluationPEOCalculationRatingsFlag | — |
| CREATED_BY | EvaluationPEOCreatedBy1 | — |
| CREATION_DATE | EvaluationPEOCreationDate1 | — |
| DECIMAL_PLACES | EvaluationPEODecimalPlaces | — |
| END_DATE | EvaluationPEOEndDate | — |
| EVALUATION_DATE | EvaluationPEOEvaluationDate | — |
| EVALUATION_ID | EvaluationPEOEvaluationId | ✅ |
| LANGUAGE_CODE | EvaluationPEOLanguageCode | — |
| LAST_UPDATE_DATE | EvaluationPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | EvaluationPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | EvaluationPEOLastUpdatedBy1 | — |
| LOCKED_BY_USER_ID | EvaluationPEOLockedByUserId | — |
| MANAGER_COMMENTS | EvaluationPEOManagerComments | — |
| MANAGER_ID | EvaluationPEOManagerId | — |
| MAPPING_METHOD_CODE | EvaluationPEOMappingMethodCode | — |
| MEETING_HELD_DATE | EvaluationPEOMeetingHeldDate | — |
| OBJECT_VERSION_NUMBER | EvaluationPEOObjectVersionNumber1 | — |
| PREV_STATUS_CODE | EvaluationPEOPrevStatusCode | — |
| ROUNDING_RULE_CODE | EvaluationPEORoundingRuleCode | — |
| SELECT_MANAGER_ALLOWED_FLAG | EvaluationPEOSelectManagerAllowedFlag | — |
| STAR_RATING_ENABLED_FLAG | EvaluationPEOStarRatingEnabledFlag | — |
| START_DATE | EvaluationPEOStartDate | — |
| STATUS_CODE | EvaluationPEOStatusCode | — |
| TEMPLATE_DEFN_ID | EvaluationPEOTemplateDefnId1 | — |
| TMPL_PERIOD_ID | EvaluationPEOTmplPeriodId1 | — |
| WORKER_COMMENTS | EvaluationPEOWorkerComments | — |
| WORKER_ID | EvaluationPEOWorkerId | — |

---

## 📚 Referências

- [Oracle Docs — HRA_EVALUATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevaluations.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
