---
id: DOC-PO-038
doc_type: system-doc
title: "POQ_ASSESSMENTS — Avaliações de Qualificação de Fornecedores"
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
  - supplier-qualification
  - avaliacao
  - qualificacao
aliases:
  - POQ_ASSESSMENTS
  - poq_assessments
  - avaliacoes-qualificacao-fornecedores
  - supplier-assessments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_ASSESSMENTS

## Visão Geral

Armazena as **avaliações de qualificação** de fornecedores no módulo Oracle Supplier Qualification Management (SQM). Cada registro representa uma avaliação iniciada contra um fornecedor, que pode englobar múltiplas qualificações (certificações, capacidades, compliance). A avaliação é o processo-pai que coordena o envio de questionários, coleta de respostas e determinação do resultado de qualificação.

> [!note] Módulo POQ
> O prefixo `POQ` identifica tabelas do submódulo **Oracle Supplier Qualification Management**, responsável por gerenciar o ciclo de vida de qualificação, certificação e avaliação de fornecedores.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Qualificação de fornecedores:** Gerenciamento do processo de avaliação inicial e periódica de fornecedores.
- **Onboarding de fornecedores:** Avaliação de novos fornecedores antes de habilitá-los para transações.
- **Renovação de qualificações:** Controle de avaliações periódicas (anuais, semestrais) para manter qualificações ativas.
- **Compliance regulatório:** Demonstração de due diligence na seleção e monitoramento de fornecedores.
- **Workflow de aprovação:** Coordenação do fluxo de aprovação das avaliações (pendente, aprovada, rejeitada).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSESSMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da avaliação | — | 🟡 75% |
| 2 | ASSESSMENT_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome/título da avaliação | — | 🟡 70% |
| 3 | SUPPLIER_ID | NUMBER(18) | NOT NULL | FK | Fornecedor avaliado | [[poz_suppliers]] | 🟡 75% |
| 4 | SUPPLIER_SITE_ID | NUMBER(18) | NULL | FK | Site do fornecedor avaliado | [[poz_supplier_sites_all_m]] | 🟡 65% |
| 5 | ASSESSMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da avaliação (INITIAL, PERIODIC, AD_HOC) | — | 🟡 65% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da avaliação (DRAFT, IN_PROGRESS, COMPLETED, APPROVED, REJECTED) | — | 🟡 75% |
| 7 | INITIATION_DATE | DATE | NULL | Data | Data de início da avaliação | — | 🟡 70% |
| 8 | COMPLETION_DATE | DATE | NULL | Data | Data de conclusão da avaliação | — | 🟡 70% |
| 9 | DUE_DATE | DATE | NULL | Data | Data limite para conclusão | — | 🟡 65% |
| 10 | INITIATED_BY | NUMBER(18) | NULL | FK | Usuário que iniciou a avaliação | [[per_users]] | 🟡 60% |
| 11 | OVERALL_RESULT | VARCHAR2(30) | NULL | Avaliação | Resultado consolidado (QUALIFIED, NOT_QUALIFIED, CONDITIONALLY_QUALIFIED) | — | 🟡 60% |
| 12 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários gerais sobre a avaliação | — | 🟡 65% |
| 13 | QUESTIONNAIRE_ID | NUMBER(18) | NULL | FK | Questionário associado à avaliação | [[poq_questionnaires]] | 🟡 60% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poz_suppliers]] — via `SUPPLIER_ID` (fornecedor avaliado)
- [[poz_supplier_sites_all_m]] — via `SUPPLIER_SITE_ID` (site do fornecedor)
- [[per_users]] — via `INITIATED_BY` (usuário iniciador)
- [[poq_questionnaires]] — via `QUESTIONNAIRE_ID` (questionário base da avaliação de fornecedor)

### Tabelas-filha (FK de saída)
- [[poq_assessment_quals]] — via `ASSESSMENT_ID` (qualificações da avaliação)

### Tabelas relacionadas

---

## Uso Típico

### Avaliações ativas de um fornecedor
```sql
SELECT a.ASSESSMENT_NAME, a.ASSESSMENT_TYPE, a.STATUS,
       a.INITIATION_DATE, a.DUE_DATE, a.OVERALL_RESULT
FROM   POQ_ASSESSMENTS a
WHERE  a.SUPPLIER_ID = :p_supplier_id
  AND  a.STATUS IN ('IN_PROGRESS', 'COMPLETED')
ORDER BY a.INITIATION_DATE DESC;
```

### Avaliações pendentes próximas do prazo
```sql
SELECT a.ASSESSMENT_NAME, a.SUPPLIER_ID,
       a.DUE_DATE, a.STATUS
FROM   POQ_ASSESSMENTS a
WHERE  a.STATUS = 'IN_PROGRESS'
  AND  a.DUE_DATE BETWEEN SYSDATE AND SYSDATE + 30
ORDER BY a.DUE_DATE;
```

---

## Observações

- O campo `STATUS` controla o ciclo de vida da avaliação: `DRAFT` (rascunho), `IN_PROGRESS` (em andamento), `COMPLETED` (concluída aguardando aprovação), `APPROVED` (aprovada), `REJECTED` (rejeitada).
- O `OVERALL_RESULT` é determinado após a conclusão de todas as qualificações individuais da avaliação.
- Uma avaliação pode conter múltiplas qualificações (via [[poq_assessment_quals]]), cada uma com seu próprio resultado.
- O `ASSESSMENT_TYPE` diferencia avaliações iniciais (onboarding) de periódicas (renovação) e ad hoc (sob demanda).
- A tabela [[poq_evaluation_team]] define quem são os avaliadores responsáveis por cada avaliação.

---

## Referências

- [Oracle Docs — POQ_ASSESSMENTS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/poqassessments.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[assessmentextractpvo|AssessmentExtractPVO]] (PO · BICC: 53/104)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_COMMENTS | AssessmentComments | ✅ |
| ASSESSMENT_ID | AssessmentId | ✅ |
| ASSESSMENT_NAME | AssessmentName | ✅ |
| ASSESSMENT_NUMBER | AssessmentNumber | ✅ |
| ASSESSMENT_OUTCOME | AssessmentOutcome | ✅ |
| ASSESSMENT_SCORE | AssessmentScore | ✅ |
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
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
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
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| AUTO_EVALUATED_FLAG | AutoEvaluatedFlag | ✅ |
| CANCELED_BY | CanceledBy | ✅ |
| CANCELED_DATE | CanceledDate | ✅ |
| CANCELED_REASON_CODE | CanceledReasonCode | ✅ |
| COMPLETED_DATE | CompletedDate | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_SOURCE | CreationSource | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EVAL_READY_DATE | EvalReadyDate | ✅ |
| EVALUATED_BY | EvaluatedBy | ✅ |
| EVALUATION_DATE | EvaluationDate | ✅ |
| EVALUATION_DUE_DATE | EvaluationDueDate | ✅ |
| EXPIRATION_REMINDER_PERIOD | ExpirationReminderPeriod | ✅ |
| EXPIRATION_REMINDER_TYPE | ExpirationReminderType | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LATEST_FLAG | LatestFlag | ✅ |
| MERGE_REQUEST_ID | MergeRequestId | ✅ |
| NOTE_TO_SUPPLIER | NoteToSupplier | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ORIG_ASSESSMENT_OUTCOME | OrigAssessmentOutcome | ✅ |
| ORIG_ASSESSMENT_SCORE | OrigAssessmentScore | ✅ |
| OVERRIDE_DATE | OverrideDate | ✅ |
| OVERRIDE_REASON | OverrideReason | ✅ |
| OVERRIDEN_BY | OverridenBy | ✅ |
| OWNER_ID | OwnerId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| QUAL_MODEL_ID | QualModelId | ✅ |
| REASSESS_EXECUTED_FLAG | ReassessExecutedFlag | ✅ |
| REASSESS_QUALIFICATION_FLAG | ReassessQualificationFlag | ✅ |
| REASSESS_REQUEST_ID | ReassessRequestId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| SEND_INT_QNNAIRE_FLAG | SendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | SendSuppQnnaireFlag | ✅ |
| SHOW_ASSESSMENT_QUAL_FLAG | ShowAssessmentQualFlag | ✅ |
| SHOW_ASSESSMT_TO_SUPP_FLAG | ShowAssessmtToSuppFlag | ✅ |
| SOURCING_ELIGIBILITY_CODE | SourcingEligibilityCode | ✅ |
| STATUS | Status | ✅ |
| SUPP_CONTACT_PARTY_ID | SuppContactPartyId | ✅ |
| SUPPLIER_ID | SupplierId | ✅ |
| SUPPLIER_SITE_ID | SupplierSiteId | ✅ |

### [[assessmentpvo|AssessmentPVO]] (PO · BICC: 94/97)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSESSMENT_COMMENTS | AssessmentAssessmentComments | ✅ |
| ASSESSMENT_ID | AssessmentId | ✅ |
| ASSESSMENT_NAME | AssessmentAssessmentName | ✅ |
| ASSESSMENT_NUMBER | AssessmentAssessmentNumber | ✅ |
| ASSESSMENT_OUTCOME | AssessmentAssessmentOutcome | ✅ |
| ASSESSMENT_SCORE | AssessmentAssessmentScore | ✅ |
| ATTRIBUTE1 | AssessmentAttribute1 | ✅ |
| ATTRIBUTE10 | AssessmentAttribute10 | ✅ |
| ATTRIBUTE11 | AssessmentAttribute11 | ✅ |
| ATTRIBUTE12 | AssessmentAttribute12 | ✅ |
| ATTRIBUTE13 | AssessmentAttribute13 | ✅ |
| ATTRIBUTE14 | AssessmentAttribute14 | ✅ |
| ATTRIBUTE15 | AssessmentAttribute15 | ✅ |
| ATTRIBUTE16 | AssessmentAttribute16 | ✅ |
| ATTRIBUTE17 | AssessmentAttribute17 | ✅ |
| ATTRIBUTE18 | AssessmentAttribute18 | ✅ |
| ATTRIBUTE19 | AssessmentAttribute19 | ✅ |
| ATTRIBUTE2 | AssessmentAttribute2 | ✅ |
| ATTRIBUTE20 | AssessmentAttribute20 | ✅ |
| ATTRIBUTE3 | AssessmentAttribute3 | ✅ |
| ATTRIBUTE4 | AssessmentAttribute4 | ✅ |
| ATTRIBUTE5 | AssessmentAttribute5 | ✅ |
| ATTRIBUTE6 | AssessmentAttribute6 | ✅ |
| ATTRIBUTE7 | AssessmentAttribute7 | ✅ |
| ATTRIBUTE8 | AssessmentAttribute8 | ✅ |
| ATTRIBUTE9 | AssessmentAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | AssessmentAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | AssessmentAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | AssessmentAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | AssessmentAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | AssessmentAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | AssessmentAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | AssessmentAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | AssessmentAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | AssessmentAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | AssessmentAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | AssessmentAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | AssessmentAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | AssessmentAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | AssessmentAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | AssessmentAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | AssessmentAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | AssessmentAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | AssessmentAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | AssessmentAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | AssessmentAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | AssessmentAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | AssessmentAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | AssessmentAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | AssessmentAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | AssessmentAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | AssessmentAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | AssessmentAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | AssessmentAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | AssessmentAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | AssessmentAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | AssessmentAttributeTimestamp9 | ✅ |
| AUTO_EVALUATED_FLAG | AssessmentAutoEvaluatedFlag | ✅ |
| CANCELED_BY | AssessmentCanceledBy | ✅ |
| CANCELED_DATE | AssessmentCanceledDate | ✅ |
| CANCELED_REASON_CODE | AssessmentCanceledReasonCode | ✅ |
| COMPLETED_DATE | AssessmentCompletedDate | ✅ |
| CREATED_BY | AssessmentCreatedBy | ✅ |
| CREATION_DATE | AssessmentCreationDate | ✅ |
| CREATION_SOURCE | AssessmentCreationSource | — |
| EFFECTIVE_END_DATE | AssessmentEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AssessmentEffectiveStartDate | ✅ |
| EVAL_READY_DATE | AssessmentEvalReadyDate | ✅ |
| EVALUATED_BY | AssessmentEvaluatedBy | — |
| EVALUATION_DATE | AssessmentEvaluationDate | ✅ |
| EVALUATION_DUE_DATE | AssessmentEvaluationDueDate | ✅ |
| EXPIRATION_REMINDER_PERIOD | AssessmentExpirationReminderPeriod | ✅ |
| EXPIRATION_REMINDER_TYPE | AssessmentExpirationReminderType | ✅ |
| INITIATIVE_ID | AssessmentInitiativeId | ✅ |
| LAST_UPDATE_DATE | AssessmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssessmentLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AssessmentLastUpdatedBy | ✅ |
| LATEST_FLAG | AssessmentLatestFlag | ✅ |
| NOTE_TO_SUPPLIER | AssessmentNoteToSupplier | ✅ |
| OBJECT_VERSION_NUMBER | AssessmentObjectVersionNumber | ✅ |
| ORIG_ASSESSMENT_OUTCOME | AssessmentOrigAssessmentOutcome | ✅ |
| ORIG_ASSESSMENT_SCORE | AssessmentOrigAssessmentScore | ✅ |
| OVERRIDE_DATE | AssessmentOverrideDate | ✅ |
| OVERRIDE_REASON | AssessmentOverrideReason | ✅ |
| OVERRIDEN_BY | AssessmentOverridenBy | ✅ |
| OWNER_ID | AssessmentOwnerId | ✅ |
| PRC_BU_ID | AssessmentPrcBuId | ✅ |
| QUAL_MODEL_ID | AssessmentQualModelId | ✅ |
| REASSESS_QUALIFICATION_FLAG | ReassessQualificationFlag | — |
| SEND_INT_QNNAIRE_FLAG | AssessmentSendIntQnnaireFlag | ✅ |
| SEND_SUPP_QNNAIRE_FLAG | AssessmentSendSuppQnnaireFlag | ✅ |
| SHOW_ASSESSMENT_QUAL_FLAG | AssessmentShowAssessmentQualFlag | ✅ |
| SHOW_ASSESSMT_TO_SUPP_FLAG | AssessmentShowAssessmtToSuppFlag | ✅ |
| SOURCING_ELIGIBILITY_CODE | AssessmentSourcingEligibilityCode | ✅ |
| SUPP_CONTACT_PARTY_ID | AssessmentSuppContactPartyId | ✅ |
| SUPPLIER_ID | AssessmentSupplierId | ✅ |
| SUPPLIER_SITE_ID | AssessmentSupplierSiteId | ✅ |
