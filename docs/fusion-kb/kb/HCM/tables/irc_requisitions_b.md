---
id: DOC-HCM-522
doc_type: system-doc
title: "IRC_REQUISITIONS_B — Requisicoes de Vaga (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - requisitions
  - irc-recruiting
aliases:
  - IRC_REQUISITIONS_B
  - irc_requisitions_b
  - requisitions-b
  - requisitions-b-hcm
  - irc-requisitions-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_REQUISITIONS_B

## Visao Geral

**Requisicoes de vaga** (job requisitions). Tabela base (`_B`) central do processo de recrutamento.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Gestao de vagas:** Registro central de requisicoes.
- **Fluxo de aprovacao:** Status desde criacao ate preenchimento.
- **Headcount:** Dimensionamento de equipe.
- **Metricas:** Time-to-fill, custo por vaga.
- **Integracao:** Candidatos, ofertas, publicacoes, campanhas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 95% |
| 2 | REQUISITION_NUMBER | VARCHAR2(30) | NOT NULL | Identificacao | Numero visivel | — | 🟢 90% |
| 3 | REQUISITION_STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟢 85% |
| 4 | HIRING_MANAGER_ID | NUMBER(18) | NULL | FK | Gestor | PER_ALL_PEOPLE_F | 🟢 85% |
| 5 | RECRUITER_ID | NUMBER(18) | NULL | FK | Recrutador | PER_ALL_PEOPLE_F | 🟡 80% |
| 6 | NUMBER_OF_OPENINGS | NUMBER | NULL | Dados | Posicoes abertas | — | 🟡 80% |
| 7 | OPEN_DATE | DATE | NULL | Dados | Data de abertura | — | 🟡 80% |
| 8 | TARGET_CLOSE_DATE | DATE | NULL | Dados | Data-alvo | — | 🟡 75% |
| 9 | PROCESS_ID | NUMBER(18) | NULL | FK | Processo seletivo | IRC_PROCESSES_B | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `HIRING_MANAGER_ID` / `RECRUITER_ID` (gestor responsavel pela contratacao)
- [[irc_processes_b]] — via `PROCESS_ID` (processo seletivo da requisicao)

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Vagas abertas
```sql
SELECT r.REQUISITION_NUMBER, r.REQUISITION_STATUS,
       r.NUMBER_OF_OPENINGS, r.OPEN_DATE
FROM   IRC_REQUISITIONS_B r WHERE r.REQUISITION_STATUS = 'OPEN'
ORDER BY r.OPEN_DATE;
```

### Filtros comuns
- `REQUISITION_STATUS = 'OPEN'` — Abertas
- `HIRING_MANAGER_ID = :id` — Por gestor
---

## Observacoes

- Tabela central do Recruiting.
- REQUISITION_NUMBER e o identificador visivel.
---

## Referencias

- [Oracle Docs -- IRC_REQUISITIONS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ircrequisitionsb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[asmtpackageresultviewallpvo|AsmtPackageResultViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | — |

### [[asmtreqpackageviewallpvo|AsmtReqPackageViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQ_USAGE_CODE | RequisitionBPEOReqUsageCode | — |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | — |

### [[jobapphisteventpvo|JobAppHistEventPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OPEN_DATE | RequisitionBPEOOpenDate | — |
| REQ_USAGE_CODE | ReqUsageCode | — |
| REQUISITION_ID | RequisitionId | ✅ |

### [[jobposthistorypvo|JobPostHistoryPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobposthistoryviewallpvo|JobPostHistoryViewAllPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobpostingpvo|JobPostingPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobpostingviewallpvo|JobPostingViewAllPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobpostresultpvo|JobPostResultPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobpostresultviewallpvo|JobPostResultViewAllPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[jobreqhisteventpvo|JobReqHistEventPVO]] (PO · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| OPEN_DATE | RequisitionBPEOOpenDate | — |
| REQUISITION_ID | RequisitionId | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionBPEORequisitionTemplateId | ✅ |

### [[jobrequisitionpvo|JobRequisitionPVO]] (PO · BICC: 85/167)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_WHEN_NOT_POSTED_FLAG | RequisitionBPEOApplyWhenNotPostedIndicator | ✅ |
| APPROVED_DATE | ApprovedDate | ✅ |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR11 | AttributeChar11 | — |
| ATTRIBUTE_CHAR12 | AttributeChar12 | — |
| ATTRIBUTE_CHAR13 | AttributeChar13 | — |
| ATTRIBUTE_CHAR14 | AttributeChar14 | — |
| ATTRIBUTE_CHAR15 | AttributeChar15 | — |
| ATTRIBUTE_CHAR16 | AttributeChar16 | — |
| ATTRIBUTE_CHAR17 | AttributeChar17 | — |
| ATTRIBUTE_CHAR18 | AttributeChar18 | — |
| ATTRIBUTE_CHAR19 | AttributeChar19 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR20 | AttributeChar20 | — |
| ATTRIBUTE_CHAR21 | AttributeChar21 | — |
| ATTRIBUTE_CHAR22 | AttributeChar22 | — |
| ATTRIBUTE_CHAR23 | AttributeChar23 | — |
| ATTRIBUTE_CHAR24 | AttributeChar24 | — |
| ATTRIBUTE_CHAR25 | AttributeChar25 | — |
| ATTRIBUTE_CHAR26 | AttributeChar26 | — |
| ATTRIBUTE_CHAR27 | AttributeChar27 | — |
| ATTRIBUTE_CHAR28 | AttributeChar28 | — |
| ATTRIBUTE_CHAR29 | AttributeChar29 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR30 | AttributeChar30 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
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
| AUTO_OPEN_REQUISITION | RequisitionBPEOAutoOpenRequisition | ✅ |
| AUTO_UNPOST_REQUISITION | RequisitionBPEOAutoUnpostRequisition | ✅ |
| AUTOMATIC_FILL_FLAG | RequisitionBPEOAutomaticFillFlag | ✅ |
| BUDGET_CURRENCY_CODE | BudgetCurrencyCode | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | ✅ |
| CURRENT_STATE_ID | CurrentStateId | ✅ |
| DEPARTMENT_ID | DepartmentId | ✅ |
| DISPLAY_IN_ORG_CHART_FLAG | DisplayInOrgChartFlag | ✅ |
| EMPLOYEE_REFERRAL_BONUS | EmployeeReferralBonus | ✅ |
| EXT_CONTACT_EMAIL | ExtContactEmail | ✅ |
| EXT_CONTACT_NAME | ExtContactName | ✅ |
| EXT_EMPLOYER_DESC_ID | ExtEmployerDescId | ✅ |
| EXT_FIRST_POSTED_DATE | ExtFirstPostedDate | ✅ |
| EXT_ORGANIZATION_DESC_ID | ExtOrganizationDescId | ✅ |
| EXT_PUBLISH_JOB_END_DATE | ExtPublishJobEndDate | ✅ |
| EXT_PUBLISH_JOB_START_DATE | ExtPublishJobStartDate | ✅ |
| EXT_PUBLISH_JOB_STATUS | ExtPublishJobStatus | ✅ |
| EXTERNAL_APPLY_FLOW_ID | RequisitionBPEOExternalApplyFlowId | — |
| EXTERNAL_DESCRIPTION_ID | RequisitionBPEOExternalDescriptionId | ✅ |
| FILLED_DATE | FilledDate | ✅ |
| FULL_PART_TIME | FullPartTime | ✅ |
| GEOGRAPHY_ID | GeographyId | ✅ |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| GRADE_ID | GradeId | ✅ |
| HIRED_COUNT | HiredCount | ✅ |
| HIRING_MANAGER_ID | HiringManagerId | ✅ |
| HOT_JOB_FLAG | RequisitionBPEOHotJobFlag | — |
| INT_CONTACT_EMAIL | IntContactEmail | ✅ |
| INT_CONTACT_NAME | IntContactName | ✅ |
| INT_EMPLOYER_DESC_ID | IntEmployerDescId | ✅ |
| INT_FIRST_POSTED_DATE | IntFirstPostedDate | ✅ |
| INT_ORGANIZATION_DESC_ID | IntOrganizationDescId | ✅ |
| INT_PUBLISH_JOB_END_DATE | IntPublishJobEndDate | ✅ |
| INT_PUBLISH_JOB_START_DATE | IntPublishJobStartDate | ✅ |
| INT_PUBLISH_JOB_STATUS | IntPublishJobStatus | ✅ |
| INTERNAL_DESCRIPTION_ID | RequisitionBPEOInternalDescriptionId | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| JOB_SHIFT_CODE | JobShiftCode | ✅ |
| JOB_TYPE_CODE | JobTypeCode | ✅ |
| JUSTIFICATION_CODE | JustificationCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGAL_EMPLOYER_ID | LegalEmployerId | ✅ |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MAX_SALARY | MaxSalary | ✅ |
| MIN_SALARY | MinSalary | ✅ |
| NUMBER_TO_HIRE | NumberToHire | ✅ |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OPEN_DATE | RequisitionBPEOOpenDate | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PIPELINE_REQUISITION_FLAG | RequisitionBPEOPipelineRequisitionFlag | ✅ |
| PIPELINE_REQUISITION_ID | RequisitionBPEOPipelineRequisitionId | ✅ |
| POSITION_ID | RequisitionBPEOPositionId | ✅ |
| POSTING_EXPIRE_IN_DAYS | RequisitionBPEOPostingExpireInDays | ✅ |
| PROCESS_ID | RequisitionBPEOProcessId | — |
| PROFILE_ID | ProfileId | ✅ |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | ✅ |
| RECRUITER_ID | RecruiterId | ✅ |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | ✅ |
| REGULAR_TEMPORARY | RegularTemporary | ✅ |
| RELOCATION_BUDGET | RelocationBudget | ✅ |
| REQ_LAST_MODIFIED_DATE | ReqLastModifiedDate | ✅ |
| REQ_SOURCE_TYPE | RequisitionBPEOReqSourceType | ✅ |
| REQ_USAGE_CODE | ReqUsageCode | ✅ |
| REQ_USAGE_TYPE | RequisitionBPEOReqUsageType | — |
| REQUISITION_ID | PipelineRequisitionBPEORequisitionId | — |
| REQUISITION_ID | RequisitionId | ✅ |
| REQUISITION_NUMBER | PipelineRequisitionBPEORequisitionNumber | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionTemplateId | ✅ |
| SALARY_CURRENCY_CODE | SalaryCurrencyCode | ✅ |
| SALARY_FREQUENCY_CODE | SalaryFrequencyCode | ✅ |
| SALARY_PERIOD_CODE | RequisitionBPEOSalaryPeriodCode | — |
| SOURCING_BUDGET | SourcingBudget | ✅ |
| STUDY_LEVEL_CODE | StudyLevelCode | ✅ |
| SUBS_PROCESS_TEMPLATE_ID | RequisitionBPEOSubsProcessTemplateId | — |
| SUSPENDED_DURATION | SuspendedDuration | ✅ |
| TRAVEL_BUDGET | TravelBudget | ✅ |
| UNLIMITED_HIRE_FLAG | UnlimitedHireFlag | ✅ |
| UNPOST_FORMULA_ID | RequisitionBPEOUnpostFormulaId | ✅ |
| WORK_END_DATE | RequisitionBPEOWorkEndDate | — |
| WORK_START_DATE | RequisitionBPEOWorkStartDate | — |
| WORKER_TYPE_CODE | WorkerTypeCode | ✅ |
| WORKPLACE_TYPE_CODE | RequisitionBPEOWorkplaceTypeCode | — |

### [[jobrequisitiontemplatepvo|JobRequisitionTemplatePVO]] (PO · BICC: 34/167)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_WHEN_NOT_POSTED_FLAG | RequisitionBPEOApplyWhenNotPostedIndicator | — |
| APPROVED_DATE | ApprovedDate | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR11 | AttributeChar11 | — |
| ATTRIBUTE_CHAR12 | AttributeChar12 | — |
| ATTRIBUTE_CHAR13 | AttributeChar13 | — |
| ATTRIBUTE_CHAR14 | AttributeChar14 | — |
| ATTRIBUTE_CHAR15 | AttributeChar15 | — |
| ATTRIBUTE_CHAR16 | AttributeChar16 | — |
| ATTRIBUTE_CHAR17 | AttributeChar17 | — |
| ATTRIBUTE_CHAR18 | AttributeChar18 | — |
| ATTRIBUTE_CHAR19 | AttributeChar19 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR20 | AttributeChar20 | — |
| ATTRIBUTE_CHAR21 | AttributeChar21 | — |
| ATTRIBUTE_CHAR22 | AttributeChar22 | — |
| ATTRIBUTE_CHAR23 | AttributeChar23 | — |
| ATTRIBUTE_CHAR24 | AttributeChar24 | — |
| ATTRIBUTE_CHAR25 | AttributeChar25 | — |
| ATTRIBUTE_CHAR26 | AttributeChar26 | — |
| ATTRIBUTE_CHAR27 | AttributeChar27 | — |
| ATTRIBUTE_CHAR28 | AttributeChar28 | — |
| ATTRIBUTE_CHAR29 | AttributeChar29 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR30 | AttributeChar30 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
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
| AUTO_OPEN_REQUISITION | RequisitionBPEOAutoOpenRequisition | ✅ |
| AUTO_UNPOST_REQUISITION | RequisitionBPEOAutoUnpostRequisition | ✅ |
| AUTOMATIC_FILL_FLAG | RequisitionBPEOAutomaticFillFlag | ✅ |
| BUDGET_CURRENCY_CODE | BudgetCurrencyCode | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| COMMENTS | Comments | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | — |
| CURRENT_STATE_ID | CurrentStateId | — |
| DEPARTMENT_ID | DepartmentId | — |
| DISPLAY_IN_ORG_CHART_FLAG | DisplayInOrgChartFlag | — |
| EMPLOYEE_REFERRAL_BONUS | EmployeeReferralBonus | ✅ |
| EXT_CONTACT_EMAIL | ExtContactEmail | ✅ |
| EXT_CONTACT_NAME | ExtContactName | ✅ |
| EXT_EMPLOYER_DESC_ID | ExtEmployerDescId | — |
| EXT_FIRST_POSTED_DATE | ExtFirstPostedDate | — |
| EXT_ORGANIZATION_DESC_ID | ExtOrganizationDescId | — |
| EXT_PUBLISH_JOB_END_DATE | ExtPublishJobEndDate | — |
| EXT_PUBLISH_JOB_START_DATE | ExtPublishJobStartDate | — |
| EXT_PUBLISH_JOB_STATUS | ExtPublishJobStatus | — |
| EXTERNAL_APPLY_FLOW_ID | RequisitionBPEOExternalApplyFlowId | — |
| EXTERNAL_DESCRIPTION_ID | RequisitionBPEOExternalDescriptionId | ✅ |
| FILLED_DATE | FilledDate | — |
| FULL_PART_TIME | FullPartTime | ✅ |
| GEOGRAPHY_ID | GeographyId | — |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| GRADE_ID | GradeId | — |
| HIRED_COUNT | HiredCount | — |
| HIRING_MANAGER_ID | HiringManagerId | — |
| HOT_JOB_FLAG | RequisitionBPEOHotJobFlag | — |
| INT_CONTACT_EMAIL | IntContactEmail | ✅ |
| INT_CONTACT_NAME | IntContactName | ✅ |
| INT_EMPLOYER_DESC_ID | IntEmployerDescId | — |
| INT_FIRST_POSTED_DATE | IntFirstPostedDate | — |
| INT_ORGANIZATION_DESC_ID | IntOrganizationDescId | — |
| INT_PUBLISH_JOB_END_DATE | IntPublishJobEndDate | — |
| INT_PUBLISH_JOB_START_DATE | IntPublishJobStartDate | — |
| INT_PUBLISH_JOB_STATUS | IntPublishJobStatus | — |
| INTERNAL_DESCRIPTION_ID | RequisitionBPEOInternalDescriptionId | ✅ |
| JOB_FAMILY_ID | JobFamilyId | — |
| JOB_FUNCTION_CODE | JobFunctionCode | ✅ |
| JOB_ID | JobId | — |
| JOB_SHIFT_CODE | JobShiftCode | ✅ |
| JOB_TYPE_CODE | JobTypeCode | ✅ |
| JUSTIFICATION_CODE | JustificationCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_EMPLOYER_ID | LegalEmployerId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | — |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MAX_SALARY | MaxSalary | ✅ |
| MIN_SALARY | MinSalary | ✅ |
| NUMBER_TO_HIRE | NumberToHire | — |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPEN_DATE | RequisitionBPEOOpenDate | — |
| ORGANIZATION_ID | OrganizationId | — |
| PIPELINE_REQUISITION_FLAG | RequisitionBPEOPipelineRequisitionFlag | — |
| PIPELINE_REQUISITION_ID | RequisitionBPEOPipelineRequisitionId | — |
| POSITION_ID | RequisitionBPEOPositionId | — |
| POSTING_EXPIRE_IN_DAYS | RequisitionBPEOPostingExpireInDays | ✅ |
| PROCESS_ID | RequisitionBPEOProcessId | — |
| PROFILE_ID | ProfileId | — |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | — |
| RECRUITER_ID | RecruiterId | — |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | ✅ |
| REGULAR_TEMPORARY | RegularTemporary | ✅ |
| RELOCATION_BUDGET | RelocationBudget | — |
| REQ_LAST_MODIFIED_DATE | ReqLastModifiedDate | — |
| REQ_SOURCE_TYPE | RequisitionBPEOReqSourceType | — |
| REQ_USAGE_CODE | ReqUsageCode | ✅ |
| REQ_USAGE_TYPE | RequisitionBPEOReqUsageType | ✅ |
| REQUISITION_ID | PipelineRequisitionBPEORequisitionId | — |
| REQUISITION_ID | RequisitionId | ✅ |
| REQUISITION_NUMBER | PipelineRequisitionBPEORequisitionNumber | — |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionTemplateId | — |
| SALARY_CURRENCY_CODE | SalaryCurrencyCode | ✅ |
| SALARY_FREQUENCY_CODE | SalaryFrequencyCode | ✅ |
| SALARY_PERIOD_CODE | RequisitionBPEOSalaryPeriodCode | — |
| SOURCING_BUDGET | SourcingBudget | — |
| STUDY_LEVEL_CODE | StudyLevelCode | ✅ |
| SUBS_PROCESS_TEMPLATE_ID | RequisitionBPEOSubsProcessTemplateId | — |
| SUSPENDED_DURATION | SuspendedDuration | — |
| TRAVEL_BUDGET | TravelBudget | — |
| UNLIMITED_HIRE_FLAG | UnlimitedHireFlag | — |
| UNPOST_FORMULA_ID | RequisitionBPEOUnpostFormulaId | ✅ |
| WORK_END_DATE | RequisitionBPEOWorkEndDate | — |
| WORK_START_DATE | RequisitionBPEOWorkStartDate | — |
| WORKER_TYPE_CODE | WorkerTypeCode | ✅ |
| WORKPLACE_TYPE_CODE | RequisitionBPEOWorkplaceTypeCode | — |

### [[jobrequisitionviewallpvo|JobRequisitionViewAllPVO]] (PO · BICC: 81/167)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLY_WHEN_NOT_POSTED_FLAG | RequisitionBPEOApplyWhenNotPostedIndicator | ✅ |
| APPROVED_DATE | ApprovedDate | ✅ |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR11 | AttributeChar11 | — |
| ATTRIBUTE_CHAR12 | AttributeChar12 | — |
| ATTRIBUTE_CHAR13 | AttributeChar13 | — |
| ATTRIBUTE_CHAR14 | AttributeChar14 | — |
| ATTRIBUTE_CHAR15 | AttributeChar15 | — |
| ATTRIBUTE_CHAR16 | AttributeChar16 | — |
| ATTRIBUTE_CHAR17 | AttributeChar17 | — |
| ATTRIBUTE_CHAR18 | AttributeChar18 | — |
| ATTRIBUTE_CHAR19 | AttributeChar19 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR20 | AttributeChar20 | — |
| ATTRIBUTE_CHAR21 | AttributeChar21 | — |
| ATTRIBUTE_CHAR22 | AttributeChar22 | — |
| ATTRIBUTE_CHAR23 | AttributeChar23 | — |
| ATTRIBUTE_CHAR24 | AttributeChar24 | — |
| ATTRIBUTE_CHAR25 | AttributeChar25 | — |
| ATTRIBUTE_CHAR26 | AttributeChar26 | — |
| ATTRIBUTE_CHAR27 | AttributeChar27 | — |
| ATTRIBUTE_CHAR28 | AttributeChar28 | — |
| ATTRIBUTE_CHAR29 | AttributeChar29 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR30 | AttributeChar30 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
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
| AUTO_OPEN_REQUISITION | RequisitionBPEOAutoOpenRequisition | ✅ |
| AUTO_UNPOST_REQUISITION | RequisitionBPEOAutoUnpostRequisition | ✅ |
| AUTOMATIC_FILL_FLAG | RequisitionBPEOAutomaticFillFlag | ✅ |
| BUDGET_CURRENCY_CODE | BudgetCurrencyCode | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| COMMENTS | Comments | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | ✅ |
| CURRENT_STATE_ID | CurrentStateId | ✅ |
| DEPARTMENT_ID | DepartmentId | ✅ |
| DISPLAY_IN_ORG_CHART_FLAG | DisplayInOrgChartFlag | ✅ |
| EMPLOYEE_REFERRAL_BONUS | EmployeeReferralBonus | ✅ |
| EXT_CONTACT_EMAIL | ExtContactEmail | ✅ |
| EXT_CONTACT_NAME | ExtContactName | ✅ |
| EXT_EMPLOYER_DESC_ID | ExtEmployerDescId | ✅ |
| EXT_FIRST_POSTED_DATE | ExtFirstPostedDate | ✅ |
| EXT_ORGANIZATION_DESC_ID | ExtOrganizationDescId | ✅ |
| EXT_PUBLISH_JOB_END_DATE | ExtPublishJobEndDate | ✅ |
| EXT_PUBLISH_JOB_START_DATE | ExtPublishJobStartDate | ✅ |
| EXT_PUBLISH_JOB_STATUS | ExtPublishJobStatus | ✅ |
| EXTERNAL_APPLY_FLOW_ID | RequisitionBPEOExternalApplyFlowId | — |
| EXTERNAL_DESCRIPTION_ID | RequisitionBPEOExternalDescriptionId | ✅ |
| FILLED_DATE | FilledDate | ✅ |
| FULL_PART_TIME | FullPartTime | ✅ |
| GEOGRAPHY_ID | GeographyId | ✅ |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| GRADE_ID | GradeId | ✅ |
| HIRED_COUNT | HiredCount | ✅ |
| HIRING_MANAGER_ID | HiringManagerId | ✅ |
| HOT_JOB_FLAG | RequisitionBPEOHotJobFlag | — |
| INT_CONTACT_EMAIL | IntContactEmail | ✅ |
| INT_CONTACT_NAME | IntContactName | ✅ |
| INT_EMPLOYER_DESC_ID | IntEmployerDescId | ✅ |
| INT_FIRST_POSTED_DATE | IntFirstPostedDate | ✅ |
| INT_ORGANIZATION_DESC_ID | IntOrganizationDescId | ✅ |
| INT_PUBLISH_JOB_END_DATE | IntPublishJobEndDate | ✅ |
| INT_PUBLISH_JOB_START_DATE | IntPublishJobStartDate | ✅ |
| INT_PUBLISH_JOB_STATUS | IntPublishJobStatus | ✅ |
| INTERNAL_DESCRIPTION_ID | RequisitionBPEOInternalDescriptionId | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| JOB_SHIFT_CODE | JobShiftCode | ✅ |
| JOB_TYPE_CODE | JobTypeCode | ✅ |
| JUSTIFICATION_CODE | JustificationCode | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_EMPLOYER_ID | LegalEmployerId | ✅ |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MAX_SALARY | MaxSalary | ✅ |
| MIN_SALARY | MinSalary | ✅ |
| NUMBER_TO_HIRE | NumberToHire | ✅ |
| OBJECT_STATUS | ObjectStatus | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| OPEN_DATE | RequisitionBPEOOpenDate | ✅ |
| ORGANIZATION_ID | OrganizationId | ✅ |
| PIPELINE_REQUISITION_FLAG | RequisitionBPEOPipelineRequisitionFlag | ✅ |
| PIPELINE_REQUISITION_ID | RequisitionBPEOPipelineRequisitionId | ✅ |
| POSITION_ID | RequisitionBPEOPositionId | ✅ |
| POSTING_EXPIRE_IN_DAYS | RequisitionBPEOPostingExpireInDays | ✅ |
| PROCESS_ID | RequisitionBPEOProcessId | — |
| PROFILE_ID | ProfileId | ✅ |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | ✅ |
| RECRUITER_ID | RecruiterId | ✅ |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | ✅ |
| REGULAR_TEMPORARY | RegularTemporary | ✅ |
| RELOCATION_BUDGET | RelocationBudget | ✅ |
| REQ_LAST_MODIFIED_DATE | ReqLastModifiedDate | ✅ |
| REQ_SOURCE_TYPE | RequisitionBPEOReqSourceType | ✅ |
| REQ_USAGE_CODE | ReqUsageCode | ✅ |
| REQ_USAGE_TYPE | RequisitionBPEOReqUsageType | — |
| REQUISITION_ID | PipelineRequisitionBPEORequisitionId | — |
| REQUISITION_ID | RequisitionId | ✅ |
| REQUISITION_NUMBER | PipelineRequisitionBPEORequisitionNumber | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionTemplateId | ✅ |
| SALARY_CURRENCY_CODE | SalaryCurrencyCode | ✅ |
| SALARY_FREQUENCY_CODE | SalaryFrequencyCode | ✅ |
| SALARY_PERIOD_CODE | RequisitionBPEOSalaryPeriodCode | — |
| SOURCING_BUDGET | SourcingBudget | ✅ |
| STUDY_LEVEL_CODE | StudyLevelCode | ✅ |
| SUBS_PROCESS_TEMPLATE_ID | RequisitionBPEOSubsProcessTemplateId | — |
| SUSPENDED_DURATION | SuspendedDuration | ✅ |
| TRAVEL_BUDGET | TravelBudget | ✅ |
| UNLIMITED_HIRE_FLAG | UnlimitedHireFlag | ✅ |
| UNPOST_FORMULA_ID | RequisitionBPEOUnpostFormulaId | ✅ |
| WORK_END_DATE | RequisitionBPEOWorkEndDate | — |
| WORK_START_DATE | RequisitionBPEOWorkStartDate | — |
| WORKER_TYPE_CODE | WorkerTypeCode | ✅ |
| WORKPLACE_TYPE_CODE | RequisitionBPEOWorkplaceTypeCode | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RequisitionBPEOLastUpdateDate | ✅ |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | RequisitionBPEOLastUpdateDate | ✅ |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[prospectspvo|ProspectsPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | ReqBPEORequisitionId | ✅ |
| REQUISITION_TEMPLATE_ID | ReqBPEORequisitionTemplateId | ✅ |

### [[prospectsviewallpvo|ProspectsViewAllPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | ReqBPEORequisitionId | — |
| REQUISITION_TEMPLATE_ID | ReqBPEORequisitionTemplateId | — |

### [[requisitionqstnrexternalviewallpvo|RequisitionQstnrExternalViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQ_USAGE_CODE | RequisitionBPEOReqUsageCode | — |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |

### [[requisitionqstnrinternalviewallpvo|RequisitionQstnrInternalViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQ_USAGE_CODE | RequisitionBPEOReqUsageCode | — |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |

### [[requisitionqstnrinterviewviewallpvo|RequisitionQstnrInterviewViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQ_USAGE_CODE | RequisitionBPEOReqUsageCode | — |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |

### [[requisitiontemplatepvo|RequisitionTemplatePVO]] (PO · BICC: 14/152)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_CHAR1 | AttributeChar1 | — |
| ATTRIBUTE_CHAR10 | AttributeChar10 | — |
| ATTRIBUTE_CHAR11 | AttributeChar11 | — |
| ATTRIBUTE_CHAR12 | AttributeChar12 | — |
| ATTRIBUTE_CHAR13 | AttributeChar13 | — |
| ATTRIBUTE_CHAR14 | AttributeChar14 | — |
| ATTRIBUTE_CHAR15 | AttributeChar15 | — |
| ATTRIBUTE_CHAR16 | AttributeChar16 | — |
| ATTRIBUTE_CHAR17 | AttributeChar17 | — |
| ATTRIBUTE_CHAR18 | AttributeChar18 | — |
| ATTRIBUTE_CHAR19 | AttributeChar19 | — |
| ATTRIBUTE_CHAR2 | AttributeChar2 | — |
| ATTRIBUTE_CHAR20 | AttributeChar20 | — |
| ATTRIBUTE_CHAR21 | AttributeChar21 | — |
| ATTRIBUTE_CHAR22 | AttributeChar22 | — |
| ATTRIBUTE_CHAR23 | AttributeChar23 | — |
| ATTRIBUTE_CHAR24 | AttributeChar24 | — |
| ATTRIBUTE_CHAR25 | AttributeChar25 | — |
| ATTRIBUTE_CHAR26 | AttributeChar26 | — |
| ATTRIBUTE_CHAR27 | AttributeChar27 | — |
| ATTRIBUTE_CHAR28 | AttributeChar28 | — |
| ATTRIBUTE_CHAR29 | AttributeChar29 | — |
| ATTRIBUTE_CHAR3 | AttributeChar3 | — |
| ATTRIBUTE_CHAR30 | AttributeChar30 | — |
| ATTRIBUTE_CHAR4 | AttributeChar4 | — |
| ATTRIBUTE_CHAR5 | AttributeChar5 | — |
| ATTRIBUTE_CHAR6 | AttributeChar6 | — |
| ATTRIBUTE_CHAR7 | AttributeChar7 | — |
| ATTRIBUTE_CHAR8 | AttributeChar8 | — |
| ATTRIBUTE_CHAR9 | AttributeChar9 | — |
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
| AUTO_OPEN_REQUISITION | RequisitionBPEOAutoOpenRequisition | ✅ |
| AUTO_UNPOST_REQUISITION | RequisitionBPEOAutoUnpostRequisition | ✅ |
| AUTOMATIC_FILL_FLAG | RequisitionBPEOAutomaticFillFlag | — |
| BUDGET_CURRENCY_CODE | BudgetCurrencyCode | — |
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| COMMENTS | Comments | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CURRENT_PHASE_ID | CurrentPhaseId | — |
| CURRENT_STATE_ID | CurrentStateId | — |
| DEPARTMENT_ID | DepartmentId | — |
| DISPLAY_IN_ORG_CHART_FLAG | DisplayInOrgChartFlag | — |
| EMPLOYEE_REFERRAL_BONUS | EmployeeReferralBonus | — |
| EXT_CONTACT_EMAIL | ExtContactEmail | — |
| EXT_CONTACT_NAME | ExtContactName | — |
| EXT_EMPLOYER_DESC_ID | ExtEmployerDescId | — |
| EXT_ORGANIZATION_DESC_ID | ExtOrganizationDescId | — |
| EXT_PUBLISH_JOB_END_DATE | ExtPublishJobEndDate | — |
| EXT_PUBLISH_JOB_START_DATE | ExtPublishJobStartDate | — |
| EXT_PUBLISH_JOB_STATUS | ExtPublishJobStatus | — |
| EXTERNAL_APPLY_FLOW_ID | ExternalApplyFlowId | — |
| EXTERNAL_DESCRIPTION_ID | RequisitionBPEOExternalDescriptionId | ✅ |
| FULL_PART_TIME | FullPartTime | — |
| GEOGRAPHY_ID | GeographyId | — |
| GEOGRAPHY_NODE_ID | GeographyNodeId | — |
| GRADE_ID | GradeId | — |
| HIRED_COUNT | HiredCount | — |
| HIRING_MANAGER_ID | HiringManagerId | — |
| INT_CONTACT_EMAIL | IntContactEmail | — |
| INT_CONTACT_NAME | IntContactName | — |
| INT_EMPLOYER_DESC_ID | IntEmployerDescId | — |
| INT_ORGANIZATION_DESC_ID | IntOrganizationDescId | — |
| INT_PUBLISH_JOB_END_DATE | IntPublishJobEndDate | — |
| INT_PUBLISH_JOB_START_DATE | IntPublishJobStartDate | — |
| INT_PUBLISH_JOB_STATUS | IntPublishJobStatus | — |
| INTERNAL_DESCRIPTION_ID | RequisitionBPEOInternalDescriptionId | ✅ |
| JOB_FAMILY_ID | JobFamilyId | — |
| JOB_FUNCTION_CODE | JobFunctionCode | — |
| JOB_ID | JobId | — |
| JOB_SHIFT_CODE | JobShiftCode | — |
| JOB_TYPE_CODE | JobTypeCode | — |
| JUSTIFICATION_CODE | JustificationCode | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_EMPLOYER_ID | LegalEmployerId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | — |
| MANAGER_LEVEL | ManagerLevel | — |
| MAX_SALARY | MaxSalary | — |
| MIN_SALARY | MinSalary | — |
| NUMBER_TO_HIRE | NumberToHire | — |
| OBJECT_STATUS | ObjectStatus | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| ORGANIZATION_ID | OrganizationId | — |
| POSTING_EXPIRE_IN_DAYS | RequisitionBPEOPostingExpireInDays | ✅ |
| PROCESS_ID | ProcessId | — |
| PROFILE_ID | ProfileId | — |
| RECRUITER_ASSIGNMENT_ID | RecruiterAssignmentId | — |
| RECRUITER_ID | RecruiterId | — |
| RECRUITING_TYPE_CODE | RecruitingTypeCode | ✅ |
| REGULAR_TEMPORARY | RegularTemporary | — |
| RELOCATION_BUDGET | RelocationBudget | — |
| REQ_LAST_MODIFIED_DATE | ReqLastModifiedDate | — |
| REQ_USAGE_CODE | ReqUsageCode | ✅ |
| REQ_USAGE_TYPE | RequisitionBPEOReqUsageType | ✅ |
| REQUISITION_ID | RequisitionId | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionTemplateId | — |
| SALARY_CURRENCY_CODE | SalaryCurrencyCode | — |
| SALARY_FREQUENCY_CODE | SalaryFrequencyCode | — |
| SALARY_PERIOD_CODE | RequisitionBPEOSalaryPeriodCode | — |
| SOURCING_BUDGET | SourcingBudget | — |
| STUDY_LEVEL_CODE | StudyLevelCode | — |
| SUBS_PROCESS_TEMPLATE_ID | SubsProcessTemplateId | — |
| TRAVEL_BUDGET | TravelBudget | — |
| UNLIMITED_HIRE_FLAG | UnlimitedHireFlag | — |
| UNPOST_FORMULA_ID | RequisitionBPEOUnpostFormulaId | ✅ |
| WORK_END_DATE | RequisitionBPEOWorkEndDate | — |
| WORK_START_DATE | RequisitionBPEOWorkStartDate | — |
| WORKER_TYPE_CODE | WorkerTypeCode | — |

### [[screeningpackagepvo|ScreeningPackagePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[screeningresultviewallpvo|ScreeningResultViewAllPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[screeningviewallpvo|ScreeningViewAllPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[searchactiondetailpvo|SearchActionDetailPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[sourcetrackingviewallpvo|SourceTrackingViewAllPVO]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | FromRequisitionBPEORequisitionId | — |
| REQUISITION_ID | RequisitionBPEORequisitionId | — |
| REQUISITION_NUMBER | FromRequisitionBPEORequisitionNumber | ✅ |
| REQUISITION_NUMBER | RequisitionBPEORequisitionNumber | ✅ |

### [[submissionqstnrsviewallpvo|SubmissionQstnrsViewAllPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_ID | RequisitionBPEORequisitionId | — |

### [[submissionrestrictedpvo|SubmissionRestrictedPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RequisitionPEOCreatedBy | — |
| CREATION_DATE | RequisitionPEOCreationDate | — |
| HIRING_MANAGER_ID | RequisitionPEOHiringManagerId | ✅ |
| LAST_UPDATE_DATE | RequisitionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionPEOLastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | RequisitionPEOManagerAssignmentId | ✅ |
| OPEN_DATE | RequisitionBPEOOpenDate | — |
| RECRUITER_ASSIGNMENT_ID | RequisitionPEORecruiterAssignmentId | ✅ |
| RECRUITER_ID | RequisitionPEORecruiterId | — |
| REQ_USAGE_CODE | ReqUsageCode | — |
| REQUISITION_ID | RequisitionPEORequisitionId | — |

### [[submissionviewallpvo|SubmissionViewAllPVO]] (HCM · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | RequisitionPEOCreatedBy | — |
| CREATION_DATE | RequisitionPEOCreationDate | — |
| HIRING_MANAGER_ID | RequisitionPEOHiringManagerId | ✅ |
| LAST_UPDATE_DATE | RequisitionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionPEOLastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | RequisitionPEOManagerAssignmentId | ✅ |
| OPEN_DATE | RequisitionBPEOOpenDate | — |
| RECRUITER_ASSIGNMENT_ID | RequisitionPEORecruiterAssignmentId | ✅ |
| RECRUITER_ID | RequisitionPEORecruiterId | — |
| REQ_USAGE_CODE | ReqUsageCode | — |
| REQUISITION_ID | RequisitionPEORequisitionId | — |
