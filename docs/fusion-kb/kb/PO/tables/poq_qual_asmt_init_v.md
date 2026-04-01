---
id: DOC-PO-047
doc_type: system-doc
title: "POQ_QUAL_ASMT_INIT_V — Avaliações por Iniciativa de Qualificação (View)"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - qualificacao
  - supplier-qualification
  - assessments
  - view-consolidada
aliases:
  - POQ_QUAL_ASMT_INIT_V
  - poq_qual_asmt_init_v
  - avaliacoes-iniciativa-qualificacao
  - qualification-assessment-initiative-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUAL_ASMT_INIT_V

## 📌 Visão Geral

View consolidada que apresenta as **avaliações (assessments) realizadas no contexto de iniciativas de qualificação**. Combina dados de iniciativas, fornecedores, modelos e resultados em uma única consulta otimizada para relatórios e dashboards de Supplier Qualification Management.

> [!note] Sufixo _V
> O sufixo `_V` indica uma **view de consulta** (read-only) que consolida múltiplas tabelas do submódulo SQM.

---

## 🧠 Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Dashboard de qualificação:** Visão consolidada do status de todas as avaliações por iniciativa.
- **Relatórios gerenciais:** Análise de resultados de qualificação com cruzamento de dados de fornecedores, modelos e iniciativas.
- **Acompanhamento de progresso:** Monitoramento de quantos fornecedores já foram avaliados em cada iniciativa.
- **Análise de tendências:** Comparação de resultados entre iniciativas ao longo do tempo.
- **Exportação de dados:** Base para extração de dados de qualificação para BI/Analytics.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da avaliação | — | 🟢 90% |
| 2 | INITIATIVE_ID | NUMBER(18) | NOT NULL | FK | Iniciativa de qualificação | [[poq_initiatives]] | 🟢 90% |
| 3 | INITIATIVE_NAME | VARCHAR2(240) | NULL | Denormalizado | Nome da iniciativa (denormalizado na view) | — | 🟡 80% |
| 4 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor avaliado | [[poz_suppliers]] | 🟢 90% |
| 5 | SUPPLIER_NAME | VARCHAR2(360) | NULL | Denormalizado | Nome do fornecedor (denormalizado) | — | 🟡 80% |
| 6 | QUAL_MODEL_ID | NUMBER(18) | NULL | FK | Modelo de qualificação utilizado | [[poq_qual_models]] | 🟡 80% |
| 7 | QUAL_MODEL_NAME | VARCHAR2(240) | NULL | Denormalizado | Nome do modelo de qualificação | — | 🟡 75% |
| 8 | STATUS_CODE | VARCHAR2(30) | NOT NULL | Classificação | Status da avaliação: PENDING, IN_PROGRESS, COMPLETED, EXPIRED | — | 🟢 90% |
| 9 | OVERALL_SCORE | NUMBER | NULL | Pontuação | Pontuação consolidada da avaliação | — | 🟡 80% |
| 10 | OUTCOME_CODE | VARCHAR2(30) | NULL | Classificação | Resultado final: QUALIFIED, NOT_QUALIFIED, CONDITIONAL | — | 🟡 80% |
| 11 | ASSESSMENT_DATE | DATE | NULL | Data | Data de realização da avaliação | — | 🟡 80% |
| 12 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da qualificação | — | 🟡 75% |
| 13 | EVALUATOR_ID | NUMBER(18) | NULL | Referência | Usuário que realizou a avaliação | — | 🟡 70% |
| 14 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários da avaliação | — | 🟡 75% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas/Views de origem
- [[poq_initiatives]] — via `INITIATIVE_ID` (iniciativa de qualificação da avaliação)
- [[poq_initiative_suppliers]] — via `INITIATIVE_ID` + `SUPPLIER_ID` (participação do fornecedor na iniciativa)
- [[poq_qual_models]] — via `QUAL_MODEL_ID` (modelo de qualificação)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor da view de avaliação de qualificação)

### Tabelas/Views relacionadas
- [[poq_qual_model_outcomes]] — outcomes do modelo para interpretação do `OUTCOME_CODE` (resultado do modelo de qualificação do fornecedor)

---

## 📎 Uso Típico

### Resultados de uma iniciativa
```sql
SELECT v.SUPPLIER_NAME, v.OVERALL_SCORE, v.OUTCOME_CODE,
       v.STATUS_CODE, v.ASSESSMENT_DATE
FROM   POQ_QUAL_ASMT_INIT_V v
WHERE  v.INITIATIVE_ID = :p_initiative_id
  AND  v.STATUS_CODE = 'COMPLETED'
ORDER  BY v.OVERALL_SCORE DESC;
```

### Taxa de qualificação por iniciativa
```sql
SELECT v.INITIATIVE_NAME,
       COUNT(*) AS total_avaliacoes,
       SUM(CASE WHEN v.OUTCOME_CODE = 'QUALIFIED' THEN 1 ELSE 0 END) AS qualificados,
       ROUND(SUM(CASE WHEN v.OUTCOME_CODE = 'QUALIFIED' THEN 1 ELSE 0 END) * 100.0
             / COUNT(*), 1) AS pct_qualificados
FROM   POQ_QUAL_ASMT_INIT_V v
WHERE  v.STATUS_CODE = 'COMPLETED'
GROUP  BY v.INITIATIVE_NAME;
```

### Filtros comuns
- `STATUS_CODE = 'COMPLETED'` — Avaliações concluídas
- `OUTCOME_CODE = 'QUALIFIED'` — Fornecedores aprovados
- `OUTCOME_CODE = 'NOT_QUALIFIED'` — Fornecedores reprovados
- `EXPIRATION_DATE < SYSDATE` — Qualificações expiradas

---

## 🔒 Observações

- Por ser uma view (`_V`), **não suporta operações DML** (INSERT/UPDATE/DELETE).
- Campos denormalizados (nomes de fornecedor, iniciativa, modelo) evitam JOINs adicionais em relatórios.
- O `OVERALL_SCORE` é calculado a partir das pontuações das áreas individuais conforme pesos definidos no modelo.
- O `EXPIRATION_DATE` indica quando a qualificação do fornecedor precisa ser renovada.
- Avaliações com `STATUS_CODE = 'EXPIRED'` indicam que o prazo de qualificação venceu sem renovação.

---

## 🔗 PVOs Relacionados

### [[qualasmtinitpvo|QualAsmtInitPVO]] (PO · BICC: 100/102)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASMT_ASSESSMENT_SCORE | QualAsmtInitAsmtAssessmentScore | ✅ |
| ASMT_AUTO_EVALUATED_FLAG | QualAsmtInitAsmtAutoEvaluatedFlag | ✅ |
| ASMT_CANCELED_BY | QualAsmtInitAsmtCanceledBy | ✅ |
| ASMT_CANCELED_DATE | QualAsmtInitAsmtCanceledDate | ✅ |
| ASMT_CANCELED_REASON_CODE | QualAsmtInitAsmtCanceledReasonCode | ✅ |
| ASMT_COMPLETED_DATE | QualAsmtInitAsmtCompletedDate | ✅ |
| ASMT_CREATION_DATE | QualAsmtInitAsmtCreationDate | ✅ |
| ASMT_EFFECTIVE_END_DATE | QualAsmtInitAsmtEffectiveEndDate | ✅ |
| ASMT_EFFECTIVE_START_DATE | QualAsmtInitAsmtEffectiveStartDate | ✅ |
| ASMT_EVAL_READY_DATE | QualAsmtInitAsmtEvalReadyDate | ✅ |
| ASMT_EVALUATED_BY | QualAsmtInitAsmtEvaluatedBy | — |
| ASMT_EVALUATION_DATE | QualAsmtInitAsmtEvaluationDate | ✅ |
| ASMT_EVALUATION_DUE_DATE | QualAsmtInitAsmtEvaluationDueDate | ✅ |
| ASMT_EXP_REMINDER_PERIOD | QualAsmtInitAsmtExpReminderPeriod | ✅ |
| ASMT_EXP_REMINDER_TYPE | QualAsmtInitAsmtExpReminderType | ✅ |
| ASMT_LATEST_FLAG | QualAsmtInitAsmtLatestFlag | ✅ |
| ASMT_NOTE_TO_SUPPLIER | QualAsmtInitAsmtNoteToSupplier | ✅ |
| ASMT_ORIG_ASSESSMENT_OUTCOME | QualAsmtInitAsmtOrigAssessmentOutcome | ✅ |
| ASMT_ORIG_ASSESSMENT_SCORE | QualAsmtInitAsmtOrigAssessmentScore | ✅ |
| ASMT_OVERRIDE_DATE | QualAsmtInitAsmtOverrideDate | ✅ |
| ASMT_OVERRIDE_REASON | QualAsmtInitAsmtOverrideReason | ✅ |
| ASMT_OVERRIDEN_BY | QualAsmtInitAsmtOverridenBy | ✅ |
| ASMT_OWNER_ID | QualAsmtInitAsmtOwnerId | ✅ |
| ASMT_PRC_BU_ID | QualAsmtInitAsmtPrcBuId | ✅ |
| ASMT_REQUEST_ID | QualAsmtInitAsmtRequestId | ✅ |
| ASMT_SHOW_ASSESS_TO_SUPP_FLAG | QualAsmtInitAsmtShowAssessToSuppFlag | ✅ |
| ASMT_SHOW_ASSESSMENT_QUAL_FLAG | QualAsmtInitAsmtShowAssessmentQualFlag | ✅ |
| ASMT_SOURCING_ELIGIBILITY_CODE | QualAsmtInitAsmtSourcingEligibilityCode | ✅ |
| ASMT_SUPP_CONTACT_PARTY_ID | QualAsmtInitAsmtSuppContactPartyId | ✅ |
| ASMT_SUPPLIER_ID | QualAsmtInitAsmtSupplierId | ✅ |
| ASMT_SUPPLIER_SITE_ID | QualAsmtInitAsmtSupplierSiteId | ✅ |
| ASSESSMENT_COMMENTS | QualAsmtInitAssessmentComments | ✅ |
| ASSESSMENT_ID | AssessmentId | ✅ |
| ASSESSMENT_NAME | QualAsmtInitAssessmentName | ✅ |
| ASSESSMENT_NUMBER | QualAsmtInitAssessmentNumber | ✅ |
| ASSESSMENT_OUTCOME | QualAsmtInitAssessmentOutcome | ✅ |
| COMPLETED_DATE | QualAsmtInitCompletedDate | ✅ |
| DESCRIPTION | QualAsmtInitDescription | ✅ |
| INIT_AUTO_ACC_RESPONSES_FLAG | QualAsmtInitInitAutoAccResponsesFlag | ✅ |
| INIT_AUTO_POP_RESPONSES_FLAG | QualAsmtInitInitAutoPopResponsesFlag | ✅ |
| INIT_LAST_OVER_REMINDER_DATE | QualAsmtInitInitLastOverReminderDate | ✅ |
| INITIATIVE_CANCELED_BY | QualAsmtInitInitiativeCanceledBy | ✅ |
| INITIATIVE_CANCELED_DATE | QualAsmtInitInitiativeCanceledDate | ✅ |
| INITIATIVE_CANCELED_REASON | QualAsmtInitInitiativeCanceledReason | ✅ |
| INITIATIVE_CREATION_DATE | QualAsmtInitInitiativeCreationDate | ✅ |
| INITIATIVE_CREATION_SOURCE | QualAsmtInitInitiativeCreationSource | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INITIATIVE_NUMBER | QualAsmtInitInitiativeNumber | ✅ |
| INITIATIVE_OWNER_ID | QualAsmtInitInitiativeOwnerId | ✅ |
| INITIATIVE_PRC_BU_ID | QualAsmtInitInitiativePrcBuId | ✅ |
| INITIATIVE_STATUS | QualAsmtInitInitiativeStatus | ✅ |
| INTERNAL_NOTE | QualAsmtInitInternalNote | ✅ |
| LAUNCH_DATE | QualAsmtInitLaunchDate | ✅ |
| QA_ORIG_QUALIFICATION_OUTCOME | QualAsmtInitQaOrigQualificationOutcome | ✅ |
| QA_SHOW_QUAL_TO_SUPPLIER_FLAG | QualAsmtInitQaShowQualToSupplierFlag | ✅ |
| QUAL_AREA_ID | QualAsmtInitQualAreaId | ✅ |
| QUAL_AUTO_EVALUATED_FLAG | QualAsmtInitQualAutoEvaluatedFlag | ✅ |
| QUAL_CANCELED_BY | QualAsmtInitQualCanceledBy | ✅ |
| QUAL_CANCELED_DATE | QualAsmtInitQualCanceledDate | ✅ |
| QUAL_CANCELED_REASON_CODE | QualAsmtInitQualCanceledReasonCode | ✅ |
| QUAL_COMPLETED_DATE | QualAsmtInitQualCompletedDate | ✅ |
| QUAL_CREATION_DATE | QualAsmtInitQualCreationDate | ✅ |
| QUAL_CREATION_SOURCE | QualAsmtInitQualCreationSource | ✅ |
| QUAL_EFFECTIVE_END_DATE | QualAsmtInitQualEffectiveEndDate | ✅ |
| QUAL_EFFECTIVE_START_DATE | QualAsmtInitQualEffectiveStartDate | ✅ |
| QUAL_EVAL_READY_DATE | QualAsmtInitQualEvalReadyDate | ✅ |
| QUAL_EVALUATED_BY | QualAsmtInitQualEvaluatedBy | — |
| QUAL_EVALUATION_DATE | QualAsmtInitQualEvaluationDate | ✅ |
| QUAL_EVALUATION_DUE_DATE | QualAsmtInitQualEvaluationDueDate | ✅ |
| QUAL_EXP_REMINDER_PERIOD | QualAsmtInitQualExpReminderPeriod | ✅ |
| QUAL_EXP_REMINDER_TYPE | QualExpReminderType | ✅ |
| QUAL_LATEST_FLAG | QualAsmtInitQualLatestFlag | ✅ |
| QUAL_MODEL_ID | QualAsmtInitQualModelId | ✅ |
| QUAL_NOTE_TO_SUPPLIER | QualAsmtInitQualNoteToSupplier | ✅ |
| QUAL_ORIG_QUALIFICATION_SCORE | QualAsmtInitQualOrigQualificationScore | ✅ |
| QUAL_OVERRIDDEN_BY | QualAsmtInitQualOverriddenBy | ✅ |
| QUAL_OVERRIDE_DATE | QualAsmtInitQualOverrideDate | ✅ |
| QUAL_OVERRIDE_REASON | QualAsmtInitQualOverrideReason | ✅ |
| QUAL_OWNER_ID | QualAsmtInitQualOwnerId | ✅ |
| QUAL_PRC_BU_ID | QualAsmtInitQualPrcBuId | ✅ |
| QUAL_QUALIFICATION_SCORE | QualAsmtInitQualQualificationScore | ✅ |
| QUAL_REQUALIFY_EXECUTED_FLAG | QualAsmtInitQualRequalifyExecutedFlag | ✅ |
| QUAL_REQUALIFY_EXPIRATION_FLAG | QualAsmtInitQualRequalifyExpirationFlag | ✅ |
| QUAL_REQUALIFY_RESPONSE_FLAG | QualAsmtInitQualRequalifyResponseFlag | ✅ |
| QUAL_REQUEST_ID | QualAsmtInitQualRequestId | ✅ |
| QUAL_SHOW_QUAL_INTER_RESP_FLAG | QualAsmtInitQualShowQualInterRespFlag | ✅ |
| QUAL_SHOW_QUAL_SUPP_RESP_FLAG | QualAsmtInitQualShowQualSuppRespFlag | ✅ |
| QUAL_SUPP_CONTACT_PARTY_ID | QualAsmtInitQualSuppContactPartyId | ✅ |
| QUAL_SUPPLIER_ID | QualAsmtInitQualSupplierId | ✅ |
| QUAL_SUPPLIER_SITE_ID | QualAsmtInitQualSupplierSiteId | ✅ |
| QUAL_WEIGHTED_SCORE | QualAsmtInitQualWeightedScore | ✅ |
| QUALIFICATION_COMMENTS | QualAsmtInitQualificationComments | ✅ |
| QUALIFICATION_ID | QualificationId | ✅ |
| QUALIFICATION_NAME | QualAsmtInitQualificationName | ✅ |
| QUALIFICATION_NUMBER | QualAsmtInitQualificationNumber | ✅ |
| QUALIFICATION_OUTCOME | QualAsmtInitQualificationOutcome | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | QualAsmtInitReuseActiveQualFlag | ✅ |
| SEND_INT_QNNAIRE_FLAG | QualAsmtInitSendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | QualAsmtInitSendSuppQnnaireFlag | ✅ |
| TITLE | QualAsmtInitTitle | ✅ |
| TYPE | QualAsmtInitType | ✅ |
| WEIGHT | QualAsmtInitWeight | ✅ |

### [[qualificationresponsespvo|QualificationResponsesPVO]] (PO · BICC: 97/100)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASMT_ASSESSMENT_SCORE | QualificationAsmtAssessmentScore | ✅ |
| ASMT_AUTO_EVALUATED_FLAG | QualificationAsmtAutoEvaluatedFlag | ✅ |
| ASMT_CANCELED_BY | QualificationAsmtCanceledBy | ✅ |
| ASMT_CANCELED_DATE | QualificationAsmtCanceledDate | ✅ |
| ASMT_CANCELED_REASON_CODE | QualificationAsmtCanceledReasonCode | ✅ |
| ASMT_COMPLETED_DATE | QualificationAsmtCompletedDate | ✅ |
| ASMT_CREATION_DATE | QualificationAsmtCreationDate | ✅ |
| ASMT_EFFECTIVE_END_DATE | QualificationAsmtEffectiveEndDate | ✅ |
| ASMT_EFFECTIVE_START_DATE | QualificationAsmtEffectiveStartDate | ✅ |
| ASMT_EVAL_READY_DATE | QualificationAsmtEvalReadyDate | ✅ |
| ASMT_EVALUATED_BY | QualificationAsmtEvaluatedBy | — |
| ASMT_EVALUATION_DATE | QualificationAsmtEvaluationDate | ✅ |
| ASMT_EVALUATION_DUE_DATE | QualificationAsmtEvaluationDueDate | ✅ |
| ASMT_EXP_REMINDER_PERIOD | QualificationAsmtExpReminderPeriod | ✅ |
| ASMT_EXP_REMINDER_TYPE | QualificationAsmtExpReminderType | ✅ |
| ASMT_LATEST_FLAG | QualificationAsmtLatestFlag | ✅ |
| ASMT_NOTE_TO_SUPPLIER | QualificationAsmtNoteToSupplier | ✅ |
| ASMT_ORIG_ASSESSMENT_OUTCOME | QualificationAsmtOrigAssessmentOutcome | ✅ |
| ASMT_ORIG_ASSESSMENT_SCORE | QualificationAsmtOrigAssessmentScore | ✅ |
| ASMT_OVERRIDE_DATE | QualificationAsmtOverrideDate | ✅ |
| ASMT_OVERRIDE_REASON | QualificationAsmtOverrideReason | ✅ |
| ASMT_OVERRIDEN_BY | QualificationAsmtOverridenBy | ✅ |
| ASMT_OWNER_ID | QualificationAsmtOwnerId | ✅ |
| ASMT_PRC_BU_ID | QualificationAsmtPrcBuId | ✅ |
| ASMT_REQUEST_ID | QualificationAsmtRequestId | ✅ |
| ASMT_SHOW_ASSESS_TO_SUPP_FLAG | QualificationAsmtShowAssessToSuppFlag | ✅ |
| ASMT_SHOW_ASSESSMENT_QUAL_FLAG | QualificationAsmtShowAssessmentQualFlag | ✅ |
| ASMT_SOURCING_ELIGIBILITY_CODE | QualificationAsmtSourcingEligibilityCode | ✅ |
| ASMT_SUPP_CONTACT_PARTY_ID | QualificationAsmtSuppContactPartyId | ✅ |
| ASMT_SUPPLIER_ID | QualificationAsmtSupplierId | ✅ |
| ASMT_SUPPLIER_SITE_ID | QualificationAsmtSupplierSiteId | ✅ |
| ASSESSMENT_COMMENTS | QualificationAssessmentComments | ✅ |
| ASSESSMENT_ID | QualificationAssessmentId | ✅ |
| ASSESSMENT_NAME | QualificationAssessmentName | ✅ |
| ASSESSMENT_NUMBER | QualificationAssessmentNumber | ✅ |
| ASSESSMENT_OUTCOME | QualificationAssessmentOutcome | ✅ |
| COMPLETED_DATE | QualificationCompletedDate | ✅ |
| DESCRIPTION | QualificationDescription | ✅ |
| INIT_AUTO_ACC_RESPONSES_FLAG | QualificationInitAutoAccResponsesFlag | ✅ |
| INIT_AUTO_POP_RESPONSES_FLAG | QualificationInitAutoPopResponsesFlag | ✅ |
| INIT_LAST_OVER_REMINDER_DATE | QualificationInitLastOverReminderDate | ✅ |
| INITIATIVE_CANCELED_BY | QualificationInitiativeCanceledBy | ✅ |
| INITIATIVE_CANCELED_DATE | QualificationInitiativeCanceledDate | ✅ |
| INITIATIVE_CANCELED_REASON | QualificationInitiativeCanceledReason | ✅ |
| INITIATIVE_CREATION_DATE | QualificationInitiativeCreationDate | ✅ |
| INITIATIVE_CREATION_SOURCE | QualificationInitiativeCreationSource | ✅ |
| INITIATIVE_ID | QualificationInitiativeId | ✅ |
| INITIATIVE_NUMBER | QualificationInitiativeNumber | ✅ |
| INITIATIVE_OWNER_ID | QualificationInitiativeOwnerId | ✅ |
| INITIATIVE_PRC_BU_ID | QualificationInitiativePrcBuId | ✅ |
| INITIATIVE_STATUS | QualificationInitiativeStatus | ✅ |
| INTERNAL_NOTE | QualificationInternalNote | ✅ |
| LAUNCH_DATE | QualificationLaunchDate | ✅ |
| QA_ORIG_QUALIFICATION_OUTCOME | QualificationQaOrigQualificationOutcome | ✅ |
| QA_SHOW_QUAL_TO_SUPPLIER_FLAG | QualificationQaShowQualToSupplierFlag | ✅ |
| QUAL_AREA_ID | QualificationQualAreaId | ✅ |
| QUAL_AUTO_EVALUATED_FLAG | QualificationQualAutoEvaluatedFlag | ✅ |
| QUAL_CANCELED_BY | QualificationQualCanceledBy | ✅ |
| QUAL_CANCELED_DATE | QualificationQualCanceledDate | ✅ |
| QUAL_CANCELED_REASON_CODE | QualificationQualCanceledReasonCode | ✅ |
| QUAL_COMPLETED_DATE | QualificationQualCompletedDate | ✅ |
| QUAL_CREATION_DATE | QualificationQualCreationDate | ✅ |
| QUAL_CREATION_SOURCE | QualificationQualCreationSource | ✅ |
| QUAL_EFFECTIVE_END_DATE | QualificationQualEffectiveEndDate | ✅ |
| QUAL_EFFECTIVE_START_DATE | QualificationQualEffectiveStartDate | ✅ |
| QUAL_EVAL_READY_DATE | QualificationQualEvalReadyDate | ✅ |
| QUAL_EVALUATED_BY | QualificationQualEvaluatedBy | — |
| QUAL_EVALUATION_DATE | QualificationQualEvaluationDate | ✅ |
| QUAL_EVALUATION_DUE_DATE | QualificationQualEvaluationDueDate | ✅ |
| QUAL_EXP_REMINDER_PERIOD | QualificationQualExpReminderPeriod | ✅ |
| QUAL_EXP_REMINDER_TYPE | QualificationQualExpReminderType | ✅ |
| QUAL_LATEST_FLAG | QualificationQualLatestFlag | ✅ |
| QUAL_MODEL_ID | QualificationAssessmentQualModelId | — |
| QUAL_MODEL_ID | QualificationQualModelId | ✅ |
| QUAL_NOTE_TO_SUPPLIER | QualificationQualNoteToSupplier | ✅ |
| QUAL_ORIG_QUALIFICATION_SCORE | QualificationQualOrigQualificationScore | ✅ |
| QUAL_OVERRIDE_DATE | QualificationQualOverrideDate | ✅ |
| QUAL_OVERRIDE_REASON | QualificationQualOverrideReason | ✅ |
| QUAL_OWNER_ID | QualificationQualOwnerId | ✅ |
| QUAL_PRC_BU_ID | QualificationQualPrcBuId | ✅ |
| QUAL_QUALIFICATION_SCORE | QualificationQualQualificationScore | ✅ |
| QUAL_REQUALIFY_EXECUTED_FLAG | QualificationQualRequalifyExecutedFlag | ✅ |
| QUAL_REQUALIFY_EXPIRATION_FLAG | QualificationQualRequalifyExpirationFlag | ✅ |
| QUAL_REQUALIFY_RESPONSE_FLAG | QualificationQualRequalifyResponseFlag | ✅ |
| QUAL_REQUEST_ID | QualificationQualRequestId | ✅ |
| QUAL_SHOW_QUAL_INTER_RESP_FLAG | QualificationQualShowQualInterRespFlag | ✅ |
| QUAL_SHOW_QUAL_SUPP_RESP_FLAG | QualificationQualShowQualSuppRespFlag | ✅ |
| QUAL_SUPP_CONTACT_PARTY_ID | QualificationQualSuppContactPartyId | ✅ |
| QUAL_SUPPLIER_ID | QualificationQualSupplierId | ✅ |
| QUAL_SUPPLIER_SITE_ID | QualificationQualSupplierSiteId | ✅ |
| QUALIFICATION_COMMENTS | QualificationQualificationComments | ✅ |
| QUALIFICATION_ID | QualificationQualificationId | ✅ |
| QUALIFICATION_NAME | QualificationQualificationName | ✅ |
| QUALIFICATION_NUMBER | QualificationQualificationNumber | ✅ |
| QUALIFICATION_OUTCOME | QualificationQualificationOutcome | ✅ |
| REUSE_ACTIVE_QUAL_FLAG | QualificationReuseActiveQualFlag | ✅ |
| SEND_INT_QNNAIRE_FLAG | QualificationSendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | QualificationSendSuppQnnaireFlag | ✅ |
| TITLE | QualificationTitle | ✅ |
| TYPE | QualificationType | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
