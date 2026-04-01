---
id: DOC-HCM-666
doc_type: system-doc
title: "PER_JOBS_F — Cargos (Jobs)"
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
  - workforce-management
  - cargos
  - jobs
aliases:
  - PER_JOBS_F
  - per_jobs_f
  - per-jobs-f
  - cargos-(jobs)
  - per-jobs-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOBS_F

## 📌 Visão Geral

Armazena a definição dos **cargos (jobs)** da organização, com vigência temporal. Um cargo define uma função genérica que pode ser atribuída a múltiplos colaboradores e posições.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de cargos** — define todos os cargos disponíveis na organização.
- **Classificação funcional** — agrupamento de funções para fins de remuneração e carreira.
- **Recrutamento** — base para descrição de vagas e requisitos.
- **Avaliação de cargo** — associação com avaliações de complexidade e valor.
- **Relatórios organizacionais** — análise da estrutura de cargos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cargo | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | JOB_CODE | VARCHAR2(30) | NULL | Identificação | Código do cargo | — | 🟢 90% |
| 5 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 6 | JOB_FAMILY_ID | NUMBER(18) | NULL | FK | Família do cargo | PER_JOB_FAMILY_F | 🟢 85% |
| 7 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativo (Y/N) | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_job_family_f]] — via `JOB_FAMILY_ID` (família do cargo)

### Tabelas-filha (FK de saída)
- [[per_jobs_f_tl]] — via `JOB_ID` (traduções do cargo)
- [[per_job_evaluations]] — via `JOB_ID` (avaliações do cargo)
- [[per_job_extra_info_f]] — via `JOB_ID` (informações extras)
- [[per_job_leg_f]] — via `JOB_ID` (dados legislativos)
- [[per_all_assignments_m]] — via `JOB_ID` (assignments com este cargo)

---

## 📎 Uso Típico

### Cargos ativos
```sql
SELECT pjf.JOB_ID, pjf.JOB_CODE, pjf.ACTIVE_STATUS
FROM   PER_JOBS_F pjf
WHERE  pjf.ACTIVE_STATUS = 'Y'
  AND  SYSDATE BETWEEN pjf.EFFECTIVE_START_DATE AND pjf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Cargos ativos
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Cargos vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Job é genérico (ex.: 'Analista de Dados') — Position é específica (ex.: 'Analista de Dados - Squad Alpha').
- Cargos são agrupados em famílias (JOB_FAMILY) para fins de classificação e carreira.
- Fundamental para relatórios de headcount por cargo e análise de estrutura organizacional.
---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 2/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobsActionOccurrenceId | — |
| ACTIVE_STATUS | JobsActiveStatus | — |
| APPROVAL_AUTHORITY | JobsApprovalAuthority | — |
| BENCHMARK_JOB_FLAG | JobsBenchmarkJobFlag | — |
| BENCHMARK_JOB_ID | JobsBenchmarkJobId | — |
| BUSINESS_GROUP_ID | JobsBusinessGroupId | — |
| CREATED_BY | JobsCreatedBy | — |
| CREATION_DATE | JobsCreationDate | — |
| EFFECTIVE_END_DATE | JobsEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobsEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobsFullPartTime | — |
| JOB_CODE | JobsJobCode | — |
| JOB_FAMILY_ID | JobsJobFamilyId | — |
| JOB_FUNCTION_CODE | JobsJobFunctionCode | — |
| JOB_ID | JobsJobId | — |
| LAST_UPDATE_DATE | JobsLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobsLastUpdateLogin | — |
| LAST_UPDATED_BY | JobsLastUpdatedBy | — |
| MANAGER_LEVEL | JobsManagerLevel | — |
| MED_CHECKUP_REQ | JobsMedCheckupReq | — |
| OBJECT_VERSION_NUMBER | JobsObjectVersionNumber | — |
| REGULAR_TEMPORARY | JobsRegularTemporary | — |
| SET_ID | JobsSetId | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 27/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | JobPEOActiveStatus | ✅ |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | ✅ |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | ✅ |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | ✅ |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | ✅ |
| CREATED_BY | JobPEOCreatedBy | ✅ |
| CREATION_DATE | JobPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | JobMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | JobPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | JobMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | ✅ |
| JOB_CODE | JobPEOJobCode | ✅ |
| JOB_FAMILY_ID | JobPEOJobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | ✅ |
| JOB_ID | JobMgrPEOJobId | ✅ |
| JOB_ID | JobPEOJobId | ✅ |
| LAST_UPDATE_DATE | JobMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | ✅ |
| MANAGER_LEVEL | JobPEOManagerLevel | ✅ |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | ✅ |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | ✅ |
| REGULAR_TEMPORARY | JobPEORegularTemporary | ✅ |
| SET_ID | JobPEOSetId | ✅ |
| STANDARD_WORKING_FREQUENCY | JobPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | JobPEOStandardWorkingHours | — |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 5/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | — |
| ACTIVE_STATUS | JobPEOActiveStatus | — |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | — |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | — |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | — |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | — |
| CREATED_BY | JobPEOCreatedBy | — |
| CREATION_DATE | JobPEOCreationDate | — |
| EFFECTIVE_END_DATE | JobMgrPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | JobPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | — |
| JOB_CODE | JobPEOJobCode | — |
| JOB_FAMILY_ID | JobPEOJobFamilyId | — |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | — |
| JOB_ID | JobMgrPEOJobId | — |
| JOB_ID | JobPEOJobId | ✅ |
| LAST_UPDATE_DATE | JobMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | — |
| MANAGER_LEVEL | JobPEOManagerLevel | — |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | — |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| REGULAR_TEMPORARY | JobPEORegularTemporary | — |
| SET_ID | JobPEOSetId | — |
| STANDARD_WORKING_FREQUENCY | JobPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | JobPEOStandardWorkingHours | — |

### [[jobextractpvo|JobExtractPVO]] (HCM · BICC: 26/94)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ACTIVE_STATUS | ActiveStatus | ✅ |
| APPROVAL_AUTHORITY | ApprovalAuthority | ✅ |
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
| BENCHMARK_JOB_FLAG | BenchmarkJobFlag | ✅ |
| BENCHMARK_JOB_ID | BenchmarkJobId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CATEGORY_CODE | CategoryCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FULL_PART_TIME | FullPartTime | ✅ |
| GRADE_LADDER_ID | GradeLadderId | ✅ |
| JOB_CODE | JobCode | ✅ |
| JOB_FAMILY_ID | JobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MANAGER_LEVEL | ManagerLevel | ✅ |
| MED_CHECKUP_REQ | MedCheckupReq | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PROGRESSION_JOB_ID | ProgressionJobId | ✅ |
| REGULAR_TEMPORARY | RegularTemporary | ✅ |
| REQUISITION_TEMPLATE_ID | RequisitionTemplateId | ✅ |
| SCHEDULING_GROUP | SchedulingGroup | — |
| SET_ID | SetId | ✅ |

### [[jobpvo|JobPVO]] (HCM · BICC: 25/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | JobPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION_UNITS | JobPEOAnnualWorkingDurationUnits | — |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | ✅ |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | ✅ |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | ✅ |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | ✅ |
| CATEGORY_CODE | JobPEOCategoryCode | — |
| CREATED_BY | JobPEOCreatedBy | ✅ |
| CREATION_DATE | JobPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | JobPEOBenchmarkJobEffectiveEndDate | — |
| EFFECTIVE_END_DATE | JobPEOProgressionJobEffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOBenchmarkJobEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOProgressionJobEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | ✅ |
| GRADE_LADDER_ID | JobPEOGradeLadderId | — |
| JOB_CODE | JobPEOBenchmarkJobJobCode | ✅ |
| JOB_CODE | JobPEOJobCode | ✅ |
| JOB_CODE | JobPEOProgressionJobJobCode | — |
| JOB_FAMILY_ID | JobPEOJobFamilyId | ✅ |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| JOB_ID | JobPEOBenchmarkJobJobId | — |
| JOB_ID | JobPEOProgressionJobJobId | — |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | ✅ |
| MANAGER_LEVEL | JobPEOManagerLevel | ✅ |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | ✅ |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| PROGRESSION_JOB_ID | JobPEOProgressionJobId | — |
| REGULAR_TEMPORARY | JobPEORegularTemporary | ✅ |
| REQUISITION_TEMPLATE_ID | JobPEORequisitionTemplateId | — |
| SCHEDULING_GROUP | JobPEOSchedulingGroup | — |
| SET_ID | JobPEOSetId | ✅ |
| STANDARD_WORKING_FREQUENCY | JobPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | JobPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | JobPEOStdAnnualWorkingDuration | — |

### [[jobpvoviewall|JobPVOViewAll]] (HCM · BICC: 7/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | — |
| ACTIVE_STATUS | JobPEOActiveStatus | — |
| ANNUAL_WORKING_DURATION_UNITS | JobPEOAnnualWorkingDurationUnits | — |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | — |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | — |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | — |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | — |
| CATEGORY_CODE | JobPEOCategoryCode | — |
| CREATED_BY | JobPEOCreatedBy | — |
| CREATION_DATE | JobPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | JobPEOBenchmarkJobEffectiveEndDate | — |
| EFFECTIVE_END_DATE | JobPEOProgressionJobEffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOBenchmarkJobEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | JobPEOProgressionJobEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | — |
| GRADE_LADDER_ID | JobPEOGradeLadderId | — |
| JOB_CODE | JobPEOBenchmarkJobJobCode | — |
| JOB_CODE | JobPEOJobCode | ✅ |
| JOB_CODE | JobPEOProgressionJobJobCode | — |
| JOB_FAMILY_ID | JobPEOJobFamilyId | — |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | — |
| JOB_ID | JobId | ✅ |
| JOB_ID | JobPEOBenchmarkJobJobId | — |
| JOB_ID | JobPEOProgressionJobJobId | — |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | — |
| MANAGER_LEVEL | JobPEOManagerLevel | — |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | — |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| PROGRESSION_JOB_ID | JobPEOProgressionJobId | — |
| REGULAR_TEMPORARY | JobPEORegularTemporary | — |
| REQUISITION_TEMPLATE_ID | JobPEORequisitionTemplateId | — |
| SCHEDULING_GROUP | JobPEOSchedulingGroup | — |
| SET_ID | JobPEOSetId | — |
| STANDARD_WORKING_FREQUENCY | JobPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | JobPEOStandardWorkingHours | — |
| STD_ANNUAL_WORKING_DURATION | JobPEOStdAnnualWorkingDuration | — |

### [[jobrefpvo|JobRefPVO]] (HCM · BICC: 8/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | JobPEOActiveStatus | ✅ |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | — |
| CREATED_BY | JobPEOCreatedBy | — |
| CREATION_DATE | JobPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_CODE | JobPEOJobCode | ✅ |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | ✅ |
| JOB_ID | JobId | ✅ |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| SET_ID | JobPEOSetId | ✅ |

### [[jobtranslationpvo|JobTranslationPVO]] (HCM · BICC: 2/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | — |
| ACTIVE_STATUS | JobPEOActiveStatus | — |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | — |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | — |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | — |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | — |
| CREATED_BY | JobPEOCreatedBy | — |
| CREATION_DATE | JobPEOCreationDate | — |
| EFFECTIVE_END_DATE | JobPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobPEOEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | — |
| JOB_CODE | JobPEOJobCode | — |
| JOB_FAMILY_ID | JobPEOJobFamilyId | — |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | — |
| JOB_ID | JobPEOJobId | — |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | — |
| MANAGER_LEVEL | JobPEOManagerLevel | — |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | — |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| REGULAR_TEMPORARY | JobPEORegularTemporary | — |
| SET_ID | JobPEOSetId | — |

### [[personmanagerhierarchyassignmentpvo|PersonManagerHierarchyAssignmentPVO]] (HCM · BICC: 3/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | JobPEOActionOccurrenceId | — |
| ACTIVE_STATUS | JobPEOActiveStatus | — |
| APPROVAL_AUTHORITY | JobPEOApprovalAuthority | — |
| BENCHMARK_JOB_FLAG | JobPEOBenchmarkJobFlag | — |
| BENCHMARK_JOB_ID | JobPEOBenchmarkJobId | — |
| BUSINESS_GROUP_ID | JobPEOBusinessGroupId | — |
| CREATED_BY | JobPEOCreatedBy | — |
| CREATION_DATE | JobPEOCreationDate | — |
| EFFECTIVE_END_DATE | JobPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobPEOEffectiveStartDate | ✅ |
| FULL_PART_TIME | JobPEOFullPartTime | — |
| JOB_CODE | JobPEOJobCode | — |
| JOB_FAMILY_ID | JobPEOJobFamilyId | — |
| JOB_FUNCTION_CODE | JobPEOJobFunctionCode | — |
| JOB_ID | JobPEOJobId | ✅ |
| LAST_UPDATE_DATE | JobPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobPEOLastUpdatedBy | — |
| MANAGER_LEVEL | JobPEOManagerLevel | — |
| MED_CHECKUP_REQ | JobPEOMedCheckupReq | — |
| OBJECT_VERSION_NUMBER | JobPEOObjectVersionNumber | — |
| REGULAR_TEMPORARY | JobPEORegularTemporary | — |
| SET_ID | JobPEOSetId | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | JobMgrPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | JobMgrPEOEffectiveStartDate | ✅ |
| JOB_ID | JobMgrPEOJobId | — |

---

## 📚 Referências

- [Oracle Docs — PER_JOBS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
