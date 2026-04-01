---
id: DOC-HCM-145
doc_type: system-doc
title: "HRA_EVAL_SECTIONS — Seções de Avaliação"
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
  - eval-section
  - avaliacao
  - hra
aliases:
  - HRA_EVAL_SECTIONS
  - hra_eval_sections
  - hra-eval-sections
  - DOC-HCM-145
  - seções-de-avaliação
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRA_EVAL_SECTIONS

## 📌 Visão Geral

Armazena os **registros de seções que compõem avaliações de performance** no módulo de Performance Management. Cada registro contém dados operacionais do processo de avaliação e gestão de performance.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de seções que compõem avaliações de performance:** Registro e controle operacional.
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
| 1 | EVAL_SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
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
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da secao de avaliacao)
- [[hra_evaluations]] — via `EVALUATION_ID` (avaliacao da secao avaliada)

### Tabelas-filha (FK de saída)
- Nenhum relacionamento de saída identificado até o momento.

---

## 📎 Uso Típico

### Registros por avaliação
```sql
SELECT r.EVAL_SECTION_ID, r.PERSON_ID, r.STATUS, r.DESCRIPTION
FROM   HRA_EVAL_SECTIONS r
WHERE  r.EVALUATION_ID = :p_evaluation_id;
```

### Registros por pessoa
```sql
SELECT r.EVAL_SECTION_ID, r.EVALUATION_ID, r.STATUS
FROM   HRA_EVAL_SECTIONS r
WHERE  r.PERSON_ID = :p_person_id;
```

---

## 🔒 Observações

- Tabela operacional do processo de seções que compõem avaliações de performance.
- Integra-se com o workflow de avaliação de performance.
- O `STATUS` controla o ciclo de vida do registro.
- Dados são consumidos por relatórios e dashboards de Talent Management.

---

## 🔗 PVOs Relacionados

### [[competencyitempvo|CompetencyItemPVO]] (HCM · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[evalsectionextractpvo|EvalSectionExtractPVO]] (HCM · BICC: 51/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | AddItemsConfirmCritFlag | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CALCULATION_RULE_CODE | CalculationRuleCode | ✅ |
| COMMENT_TEXT | CommentText | ✅ |
| COMMENTS | Comments | ✅ |
| CONTENT_TYPE_ID | ContentTypeId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENABLE_ITEMS | EnableItems | ✅ |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvaluationId | ✅ |
| FAST_FORMULA_ID | FastFormulaId | ✅ |
| FREE_FORM_ALLOWED_FLAG | FreeFormAllowedFlag | ✅ |
| ITEM_CALCULATION_CODE | ItemCalculationCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERF_RATING_MODEL_ID | PerfRatingModelId | ✅ |
| PROFILE_ID | ProfileId | ✅ |
| PROFILE_TYPE_ID | ProfileTypeId | ✅ |
| RATE_ITEM_FLAG | RateItemFlag | ✅ |
| RATE_SECTION_FLAG | RateSectionFlag | ✅ |
| RATING_OVERIDE_FLAG | RatingOverideFlag | ✅ |
| RATING_TYPE_CODE | RatingTypeCode | ✅ |
| REFERENCE_SECTION_ID | ReferenceSectionId | ✅ |
| SECTION_MIN_WEIGHT | SectionMinWeight | ✅ |
| SECTION_MIN_WEIGHT_FLAG | SectionMinWeightFlag | ✅ |
| SECTION_RATING_MODEL_ID | SectionRatingModelId | ✅ |
| SECTION_TYPE_CODE | SectionTypeCode | ✅ |
| SECTION_WEIGHT | SectionWeight | ✅ |
| SECTION_WEIGHT_FLAG | SectionWeightFlag | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| SHOW_CRITICAL | ShowCritical | ✅ |
| SHOW_DESCRIPTION | ShowDescription | ✅ |
| SHOW_DUE_DATE | ShowDueDate | ✅ |
| SHOW_MANDATORY | ShowMandatory | ✅ |
| SHOW_MEASUREMENT | ShowMeasurement | ✅ |
| SHOW_OWNED_BY | ShowOwnedBy | ✅ |
| SHOW_PERCENT_COMPLETE | ShowPercentComplete | ✅ |
| SHOW_REMINDER_DATE | ShowReminderDate | ✅ |
| SHOW_STATUS | ShowStatus | ✅ |
| SHOW_TARGET_PERF_RTG | ShowTargetPerfRtg | ✅ |
| SHOW_TARGET_PROF_LEVEL | ShowTargetProfLevel | ✅ |
| TMPL_SECTION_ID | TmplSectionId | ✅ |
| USE_PROFILE_FLAG | UseProfileFlag | ✅ |
| USE_SECRTG_FOR_PERFRTG_FLAG | UseSecrtgForPerfrtgFlag | ✅ |
| USE_SPEC_CONTENT_ITEM_FLAG | UseSpecContentItemFlag | ✅ |
| USE_SPEC_PROFILE_FLAG | UseSpecProfileFlag | ✅ |
| USE_WORKER_GOALS_FLAG | UseWorkerGoalsFlag | ✅ |
| WEIGHT_SECTION_FLAG | WeightSectionFlag | ✅ |

### [[goalitempvo|GoalItemPVO]] (HCM · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId2 | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[managerperformanceoverallratingpvo|ManagerPerformanceOverallRatingPVO]] (HCM · BICC: 1/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performancedocratingdistributionpvo|PerformanceDocRatingDistributionPVO]] (HCM · BICC: 1/45)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performancedocsectionpvo|PerformanceDocSectionPVO]] (HCM · BICC: 3/50)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | ✅ |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| CREATED_BY | EvalSectionPEOCreatedBy | — |
| CREATION_DATE | EvalSectionPEOCreationDate | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionPEOEvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvalSectionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EvalSectionPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EvalSectionPEOObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performancefinalfeedbackpvoformanager|PerformanceFinalFeedbackPVOForManager]] (HCM · BICC: 3/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | ✅ |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| CREATED_BY | EvalSectionPEOCreatedBy | — |
| CREATION_DATE | EvalSectionPEOCreationDate | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionPEOEvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvalSectionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EvalSectionPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EvalSectionPEOObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performancefinalfeedbackpvoforworker|PerformanceFinalFeedbackPVOForWorker]] (HCM · BICC: 3/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | ✅ |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| CREATED_BY | EvalSectionPEOCreatedBy | — |
| CREATION_DATE | EvalSectionPEOCreationDate | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionPEOEvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EvalSectionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EvalSectionPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EvalSectionPEOObjectVersionNumber | — |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performanceitemratingpvo|PerformanceItemRatingPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| EVAL_SECTION_ID | EvalSectionId | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |

### [[performanceoverallratingpvo|PerformanceOverallRatingPVO]] (HCM · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[performancesectionratingpvo|PerformanceSectionRatingPVO]] (HCM · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADD_ITEMS_CONFIRM_CRIT_FLAG | EvalSectionPEOAddItemsConfirmCritFlag | — |
| BUSINESS_GROUP_ID | EvalSectionPEOBusinessGroupId | — |
| CALCULATION_RULE_CODE | EvalSectionPEOCalculationRuleCode | — |
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| CONTENT_TYPE_ID | EvalSectionPEOContentTypeId | — |
| ENABLE_ITEMS | EvalSectionPEOEnableItems | — |
| EVAL_SECTION_ID | EvalSectionId | ✅ |
| EVALUATION_ID | EvalSectionPEOEvaluationId | — |
| FAST_FORMULA_ID | EvalSectionPEOFastFormulaId | — |
| FREE_FORM_ALLOWED_FLAG | EvalSectionPEOFreeFormAllowedFlag | — |
| ITEM_CALCULATION_CODE | EvalSectionPEOItemCalculationCode | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| PERF_RATING_MODEL_ID | EvalSectionPEOPerfRatingModelId | — |
| PROFILE_ID | EvalSectionPEOProfileId | — |
| PROFILE_TYPE_ID | EvalSectionPEOProfileTypeId | — |
| RATE_ITEM_FLAG | EvalSectionPEORateItemFlag | — |
| RATE_SECTION_FLAG | EvalSectionPEORateSectionFlag | — |
| RATING_OVERIDE_FLAG | EvalSectionPEORatingOverideFlag | — |
| RATING_TYPE_CODE | EvalSectionPEORatingTypeCode | — |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_MIN_WEIGHT | EvalSectionPEOSectionMinWeight | — |
| SECTION_MIN_WEIGHT_FLAG | EvalSectionPEOSectionMinWeightFlag | — |
| SECTION_RATING_MODEL_ID | EvalSectionPEOSectionRatingModelId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |
| SECTION_WEIGHT | EvalSectionPEOSectionWeight | — |
| SECTION_WEIGHT_FLAG | EvalSectionPEOSectionWeightFlag | — |
| SEQUENCE_NUMBER | EvalSectionPEOSequenceNumber | — |
| SHOW_CRITICAL | EvalSectionPEOShowCritical | — |
| SHOW_DESCRIPTION | EvalSectionPEOShowDescription | — |
| SHOW_DUE_DATE | EvalSectionPEOShowDueDate | — |
| SHOW_MANDATORY | EvalSectionPEOShowMandatory | — |
| SHOW_MEASUREMENT | EvalSectionPEOShowMeasurement | — |
| SHOW_OWNED_BY | EvalSectionPEOShowOwnedBy | — |
| SHOW_PERCENT_COMPLETE | EvalSectionPEOShowPercentComplete | — |
| SHOW_REMINDER_DATE | EvalSectionPEOShowReminderDate | — |
| SHOW_STATUS | EvalSectionPEOShowStatus | — |
| SHOW_TARGET_PERF_RTG | EvalSectionPEOShowTargetPerfRtg | — |
| SHOW_TARGET_PROF_LEVEL | EvalSectionPEOShowTargetProfLevel | — |
| TMPL_SECTION_ID | EvalSectionPEOTmplSectionId | — |
| USE_PROFILE_FLAG | EvalSectionPEOUseProfileFlag | — |
| USE_SECRTG_FOR_PERFRTG_FLAG | EvalSectionPEOUseSecrtgForPerfrtgFlag | — |
| USE_SPEC_CONTENT_ITEM_FLAG | EvalSectionPEOUseSpecContentItemFlag | — |
| USE_SPEC_PROFILE_FLAG | EvalSectionPEOUseSpecProfileFlag | — |
| USE_WORKER_GOALS_FLAG | EvalSectionPEOUseWorkerGoalsFlag | — |
| WEIGHT_SECTION_FLAG | EvalSectionPEOWeightSectionFlag | — |

### [[proficiencyitemratingpvo|ProficiencyItemRatingPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENT_TEXT | EvalSectionPEOCommentText | — |
| COMMENTS | EvalSectionPEOComments | — |
| EVAL_SECTION_ID | EvalSectionId | — |
| LAST_UPDATE_DATE | EvalSectionPEOLastUpdateDate | ✅ |
| REFERENCE_SECTION_ID | ReferenceSectionId | — |
| SECTION_TYPE_CODE | EvalSectionPEOSectionTypeCode | — |

---

## 📚 Referências

- [Oracle Docs — HRA_EVAL_SECTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hraevalsections.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
