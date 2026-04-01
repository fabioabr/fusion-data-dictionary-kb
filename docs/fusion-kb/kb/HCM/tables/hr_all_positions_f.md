---
id: DOC-HCM-274
doc_type: system-doc
title: "HR_ALL_POSITIONS_F — Posicoes"
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
  - positions
  - workforce
  - core-hr
aliases:
  - HR_ALL_POSITIONS_F
  - hr_all_positions_f
  - hr-all-positions-f
  - all-positions
  - posicoes
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HR_ALL_POSITIONS_F

## 📌 Visao Geral

Tabela principal que armazena todas as **posicoes** (positions) da organizacao com versionamento date-effective. Uma posicao representa um lugar especifico dentro de uma organizacao.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Workforce Planning:** Gerenciar posicoes e headcount.
- **Recrutamento:** Posicoes abertas geram requisicoes.
- **Orcamento:** Controlar custos por posicao.
- **Hierarquia:** Posicoes formam a hierarquia de reporte.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POSITION_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da posicao | — | 🟢 100% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | PK | Data de inicio da versao | — | 🟢 100% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Data | Data de fim da versao | — | 🟢 100% |
| 4 | BUSINESS_UNIT_ID | NUMBER(18) | NOT NULL | FK | Business unit | [[hr_all_organization_units_f]] | 🟢 95% |
| 5 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento | [[hr_all_organization_units_f]] | 🟢 95% |
| 6 | JOB_ID | NUMBER(18) | NULL | FK | Job (cargo generico) associado | — | 🟢 90% |
| 7 | LOCATION_ID | NUMBER(18) | NULL | FK | Localizacao | — | 🟢 90% |
| 8 | MAX_HEAD_COUNT | NUMBER | NULL | Dados | Headcount maximo (FTE) | — | 🟢 90% |
| 9 | STATUS | VARCHAR2(30) | NOT NULL | Classificacao | Status da posicao | — | 🟢 95% |
| 10 | POSITION_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de posicao (SINGLE, SHARED, POOLED) | — | 🟢 90% |
| 11 | MANAGER_POSITION_ID | NUMBER(18) | NULL | FK | Posicao do gestor (hierarquia) | [[hr_all_positions_f]] | 🟢 90% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `MANAGER_POSITION_ID` (auto-referencia)

### Tabelas-filha (FK de saida)
- [[hr_all_positions_f_tl]] — via `POSITION_ID` (traducoes multilingue do registro)
- [[hrt_profiles_b]] — via `POSITION_ID` (perfil de talento da posicao)

---

## 📎 Uso Tipico

### Posicoes ativas
```sql
SELECT p.POSITION_ID, p.DEPARTMENT_ID, p.JOB_ID,
       p.MAX_HEAD_COUNT, p.STATUS
FROM   HR_ALL_POSITIONS_F p
WHERE  p.STATUS = 'ACTIVE'
  AND  SYSDATE BETWEEN p.EFFECTIVE_START_DATE AND p.EFFECTIVE_END_DATE;
```

---

## 🔒 Observacoes

- Sufixo `_F` indica date-effective — PK (POSITION_ID, EFFECTIVE_START_DATE).
- MANAGER_POSITION_ID cria hierarquia de reporte posicional.
- MAX_HEAD_COUNT controla quantos colaboradores podem ocupar a posicao.

---

## 📚 Referencias

- [Oracle Docs — HR_ALL_POSITIONS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hrallpositionsf.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[fundingpositionpvo|FundingPositionPVO]] (PO · BICC: 3/54)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | — |
| ACTIVE_STATUS | PositionPEOActiveStatus | — |
| ASSIGNMENT_CATEGORY | PositionPEOAssignmentCategory | — |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | — |
| BUDGET_AMOUNT | PositionPEOBudgetAmount | — |
| BUDGET_AMOUNT_CURRENCY | PositionPEOBudgetAmountCurrency | — |
| BUDGETED_POSITION_FLAG | PositionPEOBudgetedPositionFlag | — |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | — |
| CATEGORY_CODE | PositionPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | PositionPEOCollectiveAgreementId | — |
| COST_CENTER | PositionPEOCostCenter | — |
| CREATED_BY | PositionPEOCreatedBy | — |
| CREATION_DATE | PositionPEOCreationDate | — |
| DELEGATE_POSITION_ID | PositionPEODelegatePositionId | — |
| EFFECTIVE_END_DATE | PositionPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PositionPEOEffectiveStartDate | ✅ |
| ENTRY_GRADE_ID | PositionPEOEntryGradeId | — |
| ENTRY_STEP_ID | PositionPEOEntryStepId | — |
| FREQUENCY | PositionPEOFrequency | — |
| FTE | PositionPEOFte | — |
| FULL_PART_TIME | PositionPEOFullPartTime | — |
| FUNDED_BY_EXISTING_POSITION | PositionPEOFundedByExistingPosition | — |
| GRADE_LADDER_ID | PositionPEOGradeLadderId | — |
| HIRING_STATUS | PositionPEOHiringStatus | — |
| JOB_ID | PositionPEOJobId | — |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | — |
| LOCATION_ID | PositionPEOLocationId | — |
| MAX_PERSONS | PositionPEOMaxPersons | — |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PositionPEOOrganizationId | — |
| OVERLAP_ALLOWED | PositionPEOOverlapAllowed | — |
| PERMANENT_TEMPORARY_FLAG | PositionPEOPermanentTemporaryFlag | — |
| POSITION_CODE | PositionPEOPositionCode | ✅ |
| POSITION_ID | PositionPEOPositionId | — |
| POSITION_SYNCHRONIZATION_FLAG | PositionPEOPositionSynchronizationFlag | — |
| POSITION_TYPE | PositionPEOPositionType | — |
| PROBATION_PERIOD | PositionPEOProbationPeriod | — |
| PROBATION_PERIOD_UNIT_CD | PositionPEOProbationPeriodUnitCd | — |
| REQUISITION_TEMPLATE_ID | PositionPEORequisitionTemplateId | — |
| SEASONAL_END_DATE | PositionPEOSeasonalEndDate | — |
| SEASONAL_FLAG | PositionPEOSeasonalFlag | — |
| SEASONAL_START_DATE | PositionPEOSeasonalStartDate | — |
| SECURITY_CLEARANCE | PositionPEOSecurityClearance | — |
| STANDARD_WORKING_FREQUENCY | PositionPEOStandardWorkingFrequency | — |
| STANDARD_WORKING_HOURS | PositionPEOStandardWorkingHours | — |
| SUPERVISOR_ASSIGNMENT_ID | PositionPEOSupervisorAssignmentId | — |
| SUPERVISOR_ID | PositionPEOSupervisorId | — |
| TIME_NORMAL_FINISH | PositionPEOTimeNormalFinish | — |
| TIME_NORMAL_START | PositionPEOTimeNormalStart | — |
| UNION_ID | PositionPEOUnionId | — |
| WORKING_HOURS | PositionPEOWorkingHours | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 149/149)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionMgrPEOActionOccurrenceId | ✅ |
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | PositionMgrPEOActiveStatus | ✅ |
| ACTIVE_STATUS | PositionPEOActiveStatus | ✅ |
| ATTRIBUTE1 | PositionMgrPEOAttribute1 | ✅ |
| ATTRIBUTE10 | PositionMgrPEOAttribute10 | ✅ |
| ATTRIBUTE11 | PositionMgrPEOAttribute11 | ✅ |
| ATTRIBUTE12 | PositionMgrPEOAttribute12 | ✅ |
| ATTRIBUTE13 | PositionMgrPEOAttribute13 | ✅ |
| ATTRIBUTE14 | PositionMgrPEOAttribute14 | ✅ |
| ATTRIBUTE15 | PositionMgrPEOAttribute15 | ✅ |
| ATTRIBUTE16 | PositionMgrPEOAttribute16 | ✅ |
| ATTRIBUTE17 | PositionMgrPEOAttribute17 | ✅ |
| ATTRIBUTE18 | PositionMgrPEOAttribute18 | ✅ |
| ATTRIBUTE19 | PositionMgrPEOAttribute19 | ✅ |
| ATTRIBUTE2 | PositionMgrPEOAttribute2 | ✅ |
| ATTRIBUTE20 | PositionMgrPEOAttribute20 | ✅ |
| ATTRIBUTE21 | PositionMgrPEOAttribute21 | ✅ |
| ATTRIBUTE22 | PositionMgrPEOAttribute22 | ✅ |
| ATTRIBUTE23 | PositionMgrPEOAttribute23 | ✅ |
| ATTRIBUTE24 | PositionMgrPEOAttribute24 | ✅ |
| ATTRIBUTE25 | PositionMgrPEOAttribute25 | ✅ |
| ATTRIBUTE26 | PositionMgrPEOAttribute26 | ✅ |
| ATTRIBUTE27 | PositionMgrPEOAttribute27 | ✅ |
| ATTRIBUTE28 | PositionMgrPEOAttribute28 | ✅ |
| ATTRIBUTE29 | PositionMgrPEOAttribute29 | ✅ |
| ATTRIBUTE3 | PositionMgrPEOAttribute3 | ✅ |
| ATTRIBUTE30 | PositionMgrPEOAttribute30 | ✅ |
| ATTRIBUTE4 | PositionMgrPEOAttribute4 | ✅ |
| ATTRIBUTE5 | PositionMgrPEOAttribute5 | ✅ |
| ATTRIBUTE6 | PositionMgrPEOAttribute6 | ✅ |
| ATTRIBUTE7 | PositionMgrPEOAttribute7 | ✅ |
| ATTRIBUTE8 | PositionMgrPEOAttribute8 | ✅ |
| ATTRIBUTE9 | PositionMgrPEOAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | PositionMgrPEOAttributeCategory | ✅ |
| ATTRIBUTE_CATEGORY | PositionPEOAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | PositionMgrPEOAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | PositionMgrPEOAttributeDate10 | ✅ |
| ATTRIBUTE_DATE11 | PositionMgrPEOAttributeDate11 | ✅ |
| ATTRIBUTE_DATE12 | PositionMgrPEOAttributeDate12 | ✅ |
| ATTRIBUTE_DATE13 | PositionMgrPEOAttributeDate13 | ✅ |
| ATTRIBUTE_DATE14 | PositionMgrPEOAttributeDate14 | ✅ |
| ATTRIBUTE_DATE15 | PositionMgrPEOAttributeDate15 | ✅ |
| ATTRIBUTE_DATE2 | PositionMgrPEOAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | PositionMgrPEOAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | PositionMgrPEOAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | PositionMgrPEOAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | PositionMgrPEOAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | PositionMgrPEOAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | PositionMgrPEOAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | PositionMgrPEOAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | PositionMgrPEOAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | PositionMgrPEOAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER11 | PositionMgrPEOAttributeNumber11 | ✅ |
| ATTRIBUTE_NUMBER12 | PositionMgrPEOAttributeNumber12 | ✅ |
| ATTRIBUTE_NUMBER13 | PositionMgrPEOAttributeNumber13 | ✅ |
| ATTRIBUTE_NUMBER14 | PositionMgrPEOAttributeNumber14 | ✅ |
| ATTRIBUTE_NUMBER15 | PositionMgrPEOAttributeNumber15 | ✅ |
| ATTRIBUTE_NUMBER16 | PositionMgrPEOAttributeNumber16 | ✅ |
| ATTRIBUTE_NUMBER17 | PositionMgrPEOAttributeNumber17 | ✅ |
| ATTRIBUTE_NUMBER18 | PositionMgrPEOAttributeNumber18 | ✅ |
| ATTRIBUTE_NUMBER19 | PositionMgrPEOAttributeNumber19 | ✅ |
| ATTRIBUTE_NUMBER2 | PositionMgrPEOAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER20 | PositionMgrPEOAttributeNumber20 | ✅ |
| ATTRIBUTE_NUMBER3 | PositionMgrPEOAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | PositionMgrPEOAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | PositionMgrPEOAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | PositionMgrPEOAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | PositionMgrPEOAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | PositionMgrPEOAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | PositionMgrPEOAttributeNumber9 | ✅ |
| BARGAINING_UNIT_CD | PositionMgrPEOBargainingUnitCd | ✅ |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | ✅ |
| BUSINESS_GROUP_ID | PositionMgrPEOBusinessGroupId | ✅ |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | PositionMgrPEOBusinessUnitId | ✅ |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | ✅ |
| CREATED_BY | PositionMgrPEOCreatedBy | ✅ |
| CREATED_BY | PositionPEOCreatedBy | ✅ |
| CREATION_DATE | PositionMgrPEOCreationDate | ✅ |
| CREATION_DATE | PositionPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | PositionMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | PositionPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | PositionMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PositionPEOEffectiveStartDate | ✅ |
| ENTRY_GRADE_ID | PositionMgrPEOEntryGradeId | ✅ |
| ENTRY_GRADE_ID | PositionPEOEntryGradeId | ✅ |
| ENTRY_STEP_ID | PositionMgrPEOEntryStepId | ✅ |
| ENTRY_STEP_ID | PositionPEOEntryStepId | ✅ |
| FREQUENCY | PositionMgrPEOFrequency | ✅ |
| FREQUENCY | PositionPEOFrequency | ✅ |
| FTE | PositionMgrPEOFte | ✅ |
| FTE | PositionPEOFte | ✅ |
| FULL_PART_TIME | PositionMgrPEOFullPartTime | ✅ |
| FULL_PART_TIME | PositionPEOFullPartTime | ✅ |
| HIRING_STATUS | PositionMgrPEOHiringStatus | ✅ |
| HIRING_STATUS | PositionPEOHiringStatus | ✅ |
| JOB_ID | PositionMgrPEOJobId | ✅ |
| JOB_ID | PositionPEOJobId | ✅ |
| LAST_UPDATE_DATE | PositionMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionMgrPEOLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PositionMgrPEOLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | ✅ |
| LOCATION_ID | PositionMgrPEOLocationId | ✅ |
| LOCATION_ID | PositionPEOLocationId | ✅ |
| MAX_PERSONS | PositionMgrPEOMaxPersons | ✅ |
| MAX_PERSONS | PositionPEOMaxPersons | ✅ |
| OBJECT_VERSION_NUMBER | PositionMgrPEOObjectVersionNumber | ✅ |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | PositionMgrPEOOrganizationId | ✅ |
| ORGANIZATION_ID | PositionPEOOrganizationId | ✅ |
| OVERLAP_ALLOWED | PositionMgrPEOOverlapAllowed | ✅ |
| OVERLAP_ALLOWED | PositionPEOOverlapAllowed | ✅ |
| PERMANENT_TEMPORARY_FLAG | PositionMgrPEOPermanentTemporaryFlag | ✅ |
| PERMANENT_TEMPORARY_FLAG | PositionPEOPermanentTemporaryFlag | ✅ |
| POSITION_CODE | PositionMgrPEOPositionCode | ✅ |
| POSITION_CODE | PositionPEOPositionCode | ✅ |
| POSITION_ID | PositionMgrPEOPositionId | ✅ |
| POSITION_ID | PositionPEOPositionId | ✅ |
| POSITION_SYNCHRONIZATION_FLAG | PositionMgrPEOPositionSynchronizationFlag | ✅ |
| POSITION_SYNCHRONIZATION_FLAG | PositionPEOPositionSynchronizationFlag | ✅ |
| POSITION_TYPE | PositionMgrPEOPositionType | ✅ |
| POSITION_TYPE | PositionPEOPositionType | ✅ |
| PROBATION_PERIOD | PositionMgrPEOProbationPeriod | ✅ |
| PROBATION_PERIOD | PositionPEOProbationPeriod | ✅ |
| PROBATION_PERIOD_UNIT_CD | PositionMgrPEOProbationPeriodUnitCd | ✅ |
| PROBATION_PERIOD_UNIT_CD | PositionPEOProbationPeriodUnitCd | ✅ |
| SEASONAL_END_DATE | PositionMgrPEOSeasonalEndDate | ✅ |
| SEASONAL_END_DATE | PositionPEOSeasonalEndDate | ✅ |
| SEASONAL_FLAG | PositionMgrPEOSeasonalFlag | ✅ |
| SEASONAL_FLAG | PositionPEOSeasonalFlag | ✅ |
| SEASONAL_START_DATE | PositionMgrPEOSeasonalStartDate | ✅ |
| SEASONAL_START_DATE | PositionPEOSeasonalStartDate | ✅ |
| SECURITY_CLEARANCE | PositionMgrPEOSecurityClearance | ✅ |
| SECURITY_CLEARANCE | PositionPEOSecurityClearance | ✅ |
| STANDARD_WORKING_FREQUENCY | PositionPEOStandardWorkingFrequency | ✅ |
| STANDARD_WORKING_HOURS | PositionPEOStandardWorkingHours | ✅ |
| SUPERVISOR_ASSIGNMENT_ID | PositionMgrPEOSupervisorAssignmentId | ✅ |
| SUPERVISOR_ASSIGNMENT_ID | PositionPEOSupervisorAssignmentId | ✅ |
| SUPERVISOR_ID | PositionMgrPEOSupervisorId | ✅ |
| SUPERVISOR_ID | PositionPEOSupervisorId | ✅ |
| TIME_NORMAL_FINISH | PositionMgrPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_FINISH | PositionPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | PositionMgrPEOTimeNormalStart | ✅ |
| TIME_NORMAL_START | PositionPEOTimeNormalStart | ✅ |
| WORKING_HOURS | PositionMgrPEOWorkingHours | ✅ |
| WORKING_HOURS | PositionPEOWorkingHours | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 9/149)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionMgrPEOActionOccurrenceId | — |
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | — |
| ACTIVE_STATUS | PositionMgrPEOActiveStatus | — |
| ACTIVE_STATUS | PositionPEOActiveStatus | — |
| ATTRIBUTE1 | PositionMgrPEOAttribute1 | — |
| ATTRIBUTE10 | PositionMgrPEOAttribute10 | — |
| ATTRIBUTE11 | PositionMgrPEOAttribute11 | — |
| ATTRIBUTE12 | PositionMgrPEOAttribute12 | — |
| ATTRIBUTE13 | PositionMgrPEOAttribute13 | — |
| ATTRIBUTE14 | PositionMgrPEOAttribute14 | — |
| ATTRIBUTE15 | PositionMgrPEOAttribute15 | — |
| ATTRIBUTE16 | PositionMgrPEOAttribute16 | — |
| ATTRIBUTE17 | PositionMgrPEOAttribute17 | — |
| ATTRIBUTE18 | PositionMgrPEOAttribute18 | — |
| ATTRIBUTE19 | PositionMgrPEOAttribute19 | — |
| ATTRIBUTE2 | PositionMgrPEOAttribute2 | — |
| ATTRIBUTE20 | PositionMgrPEOAttribute20 | — |
| ATTRIBUTE21 | PositionMgrPEOAttribute21 | — |
| ATTRIBUTE22 | PositionMgrPEOAttribute22 | — |
| ATTRIBUTE23 | PositionMgrPEOAttribute23 | — |
| ATTRIBUTE24 | PositionMgrPEOAttribute24 | — |
| ATTRIBUTE25 | PositionMgrPEOAttribute25 | — |
| ATTRIBUTE26 | PositionMgrPEOAttribute26 | — |
| ATTRIBUTE27 | PositionMgrPEOAttribute27 | — |
| ATTRIBUTE28 | PositionMgrPEOAttribute28 | — |
| ATTRIBUTE29 | PositionMgrPEOAttribute29 | — |
| ATTRIBUTE3 | PositionMgrPEOAttribute3 | — |
| ATTRIBUTE30 | PositionMgrPEOAttribute30 | — |
| ATTRIBUTE4 | PositionMgrPEOAttribute4 | — |
| ATTRIBUTE5 | PositionMgrPEOAttribute5 | — |
| ATTRIBUTE6 | PositionMgrPEOAttribute6 | — |
| ATTRIBUTE7 | PositionMgrPEOAttribute7 | — |
| ATTRIBUTE8 | PositionMgrPEOAttribute8 | — |
| ATTRIBUTE9 | PositionMgrPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PositionMgrPEOAttributeCategory | — |
| ATTRIBUTE_CATEGORY | PositionPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | PositionMgrPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | PositionMgrPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | PositionMgrPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | PositionMgrPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | PositionMgrPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | PositionMgrPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | PositionMgrPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | PositionMgrPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | PositionMgrPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | PositionMgrPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | PositionMgrPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | PositionMgrPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | PositionMgrPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | PositionMgrPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | PositionMgrPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | PositionMgrPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | PositionMgrPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | PositionMgrPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | PositionMgrPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | PositionMgrPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | PositionMgrPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | PositionMgrPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | PositionMgrPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | PositionMgrPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | PositionMgrPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | PositionMgrPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | PositionMgrPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | PositionMgrPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | PositionMgrPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | PositionMgrPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | PositionMgrPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | PositionMgrPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | PositionMgrPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | PositionMgrPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | PositionMgrPEOAttributeNumber9 | — |
| BARGAINING_UNIT_CD | PositionMgrPEOBargainingUnitCd | — |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | — |
| BUSINESS_GROUP_ID | PositionMgrPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | PositionMgrPEOBusinessUnitId | — |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | — |
| CREATED_BY | PositionMgrPEOCreatedBy | — |
| CREATED_BY | PositionPEOCreatedBy | — |
| CREATION_DATE | PositionMgrPEOCreationDate | — |
| CREATION_DATE | PositionPEOCreationDate | — |
| EFFECTIVE_END_DATE | PositionMgrPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | PositionPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | PositionMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | PositionPEOEffectiveStartDate | ✅ |
| ENTRY_GRADE_ID | PositionMgrPEOEntryGradeId | — |
| ENTRY_GRADE_ID | PositionPEOEntryGradeId | — |
| ENTRY_STEP_ID | PositionMgrPEOEntryStepId | — |
| ENTRY_STEP_ID | PositionPEOEntryStepId | — |
| FREQUENCY | PositionMgrPEOFrequency | — |
| FREQUENCY | PositionPEOFrequency | ✅ |
| FTE | PositionMgrPEOFte | — |
| FTE | PositionPEOFte | — |
| FULL_PART_TIME | PositionMgrPEOFullPartTime | — |
| FULL_PART_TIME | PositionPEOFullPartTime | — |
| HIRING_STATUS | PositionMgrPEOHiringStatus | — |
| HIRING_STATUS | PositionPEOHiringStatus | — |
| JOB_ID | PositionMgrPEOJobId | — |
| JOB_ID | PositionPEOJobId | — |
| LAST_UPDATE_DATE | PositionMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionMgrPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PositionMgrPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | — |
| LOCATION_ID | PositionMgrPEOLocationId | — |
| LOCATION_ID | PositionPEOLocationId | — |
| MAX_PERSONS | PositionMgrPEOMaxPersons | — |
| MAX_PERSONS | PositionPEOMaxPersons | — |
| OBJECT_VERSION_NUMBER | PositionMgrPEOObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PositionMgrPEOOrganizationId | — |
| ORGANIZATION_ID | PositionPEOOrganizationId | — |
| OVERLAP_ALLOWED | PositionMgrPEOOverlapAllowed | — |
| OVERLAP_ALLOWED | PositionPEOOverlapAllowed | — |
| PERMANENT_TEMPORARY_FLAG | PositionMgrPEOPermanentTemporaryFlag | — |
| PERMANENT_TEMPORARY_FLAG | PositionPEOPermanentTemporaryFlag | — |
| POSITION_CODE | PositionMgrPEOPositionCode | ✅ |
| POSITION_CODE | PositionPEOPositionCode | — |
| POSITION_ID | PositionMgrPEOPositionId | — |
| POSITION_ID | PositionPEOPositionId | — |
| POSITION_SYNCHRONIZATION_FLAG | PositionMgrPEOPositionSynchronizationFlag | — |
| POSITION_SYNCHRONIZATION_FLAG | PositionPEOPositionSynchronizationFlag | — |
| POSITION_TYPE | PositionMgrPEOPositionType | — |
| POSITION_TYPE | PositionPEOPositionType | — |
| PROBATION_PERIOD | PositionMgrPEOProbationPeriod | — |
| PROBATION_PERIOD | PositionPEOProbationPeriod | — |
| PROBATION_PERIOD_UNIT_CD | PositionMgrPEOProbationPeriodUnitCd | — |
| PROBATION_PERIOD_UNIT_CD | PositionPEOProbationPeriodUnitCd | — |
| SEASONAL_END_DATE | PositionMgrPEOSeasonalEndDate | — |
| SEASONAL_END_DATE | PositionPEOSeasonalEndDate | — |
| SEASONAL_FLAG | PositionMgrPEOSeasonalFlag | — |
| SEASONAL_FLAG | PositionPEOSeasonalFlag | — |
| SEASONAL_START_DATE | PositionMgrPEOSeasonalStartDate | — |
| SEASONAL_START_DATE | PositionPEOSeasonalStartDate | — |
| SECURITY_CLEARANCE | PositionMgrPEOSecurityClearance | — |
| SECURITY_CLEARANCE | PositionPEOSecurityClearance | — |
| STANDARD_WORKING_FREQUENCY | PositionPEOStandardWorkingFrequency | ✅ |
| STANDARD_WORKING_HOURS | PositionPEOStandardWorkingHours | ✅ |
| SUPERVISOR_ASSIGNMENT_ID | PositionMgrPEOSupervisorAssignmentId | — |
| SUPERVISOR_ASSIGNMENT_ID | PositionPEOSupervisorAssignmentId | — |
| SUPERVISOR_ID | PositionMgrPEOSupervisorId | — |
| SUPERVISOR_ID | PositionPEOSupervisorId | — |
| TIME_NORMAL_FINISH | PositionMgrPEOTimeNormalFinish | — |
| TIME_NORMAL_FINISH | PositionPEOTimeNormalFinish | — |
| TIME_NORMAL_START | PositionMgrPEOTimeNormalStart | — |
| TIME_NORMAL_START | PositionPEOTimeNormalStart | — |
| WORKING_HOURS | PositionMgrPEOWorkingHours | — |
| WORKING_HOURS | PositionPEOWorkingHours | ✅ |

### [[positionpvo|PositionPVO]] (PO · BICC: 56/70)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | PositionPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION | PositionPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | PositionPEOAnnualWorkingDurationUnits | — |
| ASSIGNMENT_CATEGORY | PositionPEOAssignmentCategory | ✅ |
| ATTRIBUTE_CATEGORY | PositionPEOAttributeCategory | ✅ |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | ✅ |
| BUDGET_AMOUNT | PositionPEOBudgetAmount | ✅ |
| BUDGET_AMOUNT_CURRENCY | PositionPEOBudgetAmountCurrency | ✅ |
| BUDGETED_POSITION_FLAG | PositionPEOBudgetedPositionFlag | ✅ |
| BUSINESS_GROUP_ID | ParentPositionPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | ✅ |
| CALCULATE_FTE | PositionPEOCalculateFte | — |
| CATEGORY_CODE | PositionPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | PositionPEOCollectiveAgreementId | — |
| COST_CENTER | PositionPEOCostCenter | — |
| CREATED_BY | PositionPEOCreatedBy | ✅ |
| CREATION_DATE | PositionPEOCreationDate | ✅ |
| DELEGATE_POSITION_ID | PositionPEODelegatePositionId | ✅ |
| EFFECTIVE_END_DATE | DelegatePositionPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | ParentPositionPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionPEOEffectiveStartDate | ✅ |
| ENTRY_GRADE_ID | PositionPEOEntryGradeId | ✅ |
| ENTRY_STEP_ID | PositionPEOEntryStepId | ✅ |
| FREQUENCY | PositionPEOFrequency | ✅ |
| FTE | PositionPEOFte | ✅ |
| FULL_PART_TIME | PositionPEOFullPartTime | ✅ |
| FUNDED_BY_EXISTING_POSITION | PositionPEOFundedByExistingPosition | ✅ |
| GRADE_LADDER_ID | PositionPEOGradeLadderId | — |
| HIRING_STATUS | PositionPEOHiringStatus | ✅ |
| JOB_ID | PositionPEOJobId | ✅ |
| LAST_UPDATE_DATE | DelegatePositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | ✅ |
| LOCATION_ID | PositionPEOLocationId | ✅ |
| MAX_PERSONS | PositionPEOMaxPersons | ✅ |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PositionPEOOrganizationId | ✅ |
| OVERLAP_ALLOWED | PositionPEOOverlapAllowed | ✅ |
| PERMANENT_TEMPORARY_FLAG | PositionPEOPermanentTemporaryFlag | ✅ |
| POSITION_CODE | DelegatePositionPEOPositionCode | ✅ |
| POSITION_CODE | ParentPositionPEOPositionCode | ✅ |
| POSITION_CODE | PositionPEOPositionCode | ✅ |
| POSITION_ID | DelegatePositionPEOPositionId | — |
| POSITION_ID | ParentPositionPEOPositionId | ✅ |
| POSITION_ID | PositionId | ✅ |
| POSITION_SYNCHRONIZATION_FLAG | PositionPEOPositionSynchronizationFlag | ✅ |
| POSITION_TYPE | PositionPEOPositionType | ✅ |
| PROBATION_PERIOD | PositionPEOProbationPeriod | ✅ |
| PROBATION_PERIOD_UNIT_CD | PositionPEOProbationPeriodUnitCd | ✅ |
| REQUISITION_TEMPLATE_ID | PositionPEORequisitionTemplateId | ✅ |
| SEASONAL_END_DATE | PositionPEOSeasonalEndDate | ✅ |
| SEASONAL_FLAG | PositionPEOSeasonalFlag | ✅ |
| SEASONAL_START_DATE | PositionPEOSeasonalStartDate | ✅ |
| SECURITY_CLEARANCE | PositionPEOSecurityClearance | ✅ |
| STANDARD_WORKING_FREQUENCY | PositionPEOStandardWorkingFrequency | ✅ |
| STANDARD_WORKING_HOURS | PositionPEOStandardWorkingHours | ✅ |
| STD_ANNUAL_WORKING_DURATION | PositionPEOStdAnnualWorkingDuration | — |
| SUPERVISOR_ASSIGNMENT_ID | PositionPEOSupervisorAssignmentId | ✅ |
| SUPERVISOR_ID | PositionPEOSupervisorId | ✅ |
| TIME_NORMAL_FINISH | PositionPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | PositionPEOTimeNormalStart | ✅ |
| UNION_ID | PositionPEOUnionId | — |
| WORKING_HOURS | PositionPEOWorkingHours | ✅ |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 56/70)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | PositionPEOActiveStatus | ✅ |
| ANNUAL_WORKING_DURATION | PositionPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | PositionPEOAnnualWorkingDurationUnits | — |
| ASSIGNMENT_CATEGORY | PositionPEOAssignmentCategory | ✅ |
| ATTRIBUTE_CATEGORY | PositionPEOAttributeCategory | ✅ |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | ✅ |
| BUDGET_AMOUNT | PositionPEOBudgetAmount | ✅ |
| BUDGET_AMOUNT_CURRENCY | PositionPEOBudgetAmountCurrency | ✅ |
| BUDGETED_POSITION_FLAG | PositionPEOBudgetedPositionFlag | ✅ |
| BUSINESS_GROUP_ID | ParentPositionPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | ✅ |
| CALCULATE_FTE | PositionPEOCalculateFte | — |
| CATEGORY_CODE | PositionPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | PositionPEOCollectiveAgreementId | — |
| COST_CENTER | PositionPEOCostCenter | — |
| CREATED_BY | PositionPEOCreatedBy | ✅ |
| CREATION_DATE | PositionPEOCreationDate | ✅ |
| DELEGATE_POSITION_ID | PositionPEODelegatePositionId | ✅ |
| EFFECTIVE_END_DATE | DelegatePositionPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | ParentPositionPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | DelegatePositionPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | ParentPositionPEOEffectiveStartDate | ✅ |
| ENTRY_GRADE_ID | PositionPEOEntryGradeId | ✅ |
| ENTRY_STEP_ID | PositionPEOEntryStepId | ✅ |
| FREQUENCY | PositionPEOFrequency | ✅ |
| FTE | PositionPEOFte | ✅ |
| FULL_PART_TIME | PositionPEOFullPartTime | ✅ |
| FUNDED_BY_EXISTING_POSITION | PositionPEOFundedByExistingPosition | ✅ |
| GRADE_LADDER_ID | PositionPEOGradeLadderId | — |
| HIRING_STATUS | PositionPEOHiringStatus | ✅ |
| JOB_ID | PositionPEOJobId | ✅ |
| LAST_UPDATE_DATE | DelegatePositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ParentPositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | ✅ |
| LOCATION_ID | PositionPEOLocationId | ✅ |
| MAX_PERSONS | PositionPEOMaxPersons | ✅ |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PositionPEOOrganizationId | ✅ |
| OVERLAP_ALLOWED | PositionPEOOverlapAllowed | ✅ |
| PERMANENT_TEMPORARY_FLAG | PositionPEOPermanentTemporaryFlag | ✅ |
| POSITION_CODE | DelegatePositionPEOPositionCode | ✅ |
| POSITION_CODE | ParentPositionPEOPositionCode | ✅ |
| POSITION_CODE | PositionPEOPositionCode | ✅ |
| POSITION_ID | DelegatePositionPEOPositionId | — |
| POSITION_ID | ParentPositionPEOPositionId | ✅ |
| POSITION_ID | PositionId | ✅ |
| POSITION_SYNCHRONIZATION_FLAG | PositionPEOPositionSynchronizationFlag | ✅ |
| POSITION_TYPE | PositionPEOPositionType | ✅ |
| PROBATION_PERIOD | PositionPEOProbationPeriod | ✅ |
| PROBATION_PERIOD_UNIT_CD | PositionPEOProbationPeriodUnitCd | ✅ |
| REQUISITION_TEMPLATE_ID | PositionPEORequisitionTemplateId | ✅ |
| SEASONAL_END_DATE | PositionPEOSeasonalEndDate | ✅ |
| SEASONAL_FLAG | PositionPEOSeasonalFlag | ✅ |
| SEASONAL_START_DATE | PositionPEOSeasonalStartDate | ✅ |
| SECURITY_CLEARANCE | PositionPEOSecurityClearance | ✅ |
| STANDARD_WORKING_FREQUENCY | PositionPEOStandardWorkingFrequency | ✅ |
| STANDARD_WORKING_HOURS | PositionPEOStandardWorkingHours | ✅ |
| STD_ANNUAL_WORKING_DURATION | PositionPEOStdAnnualWorkingDuration | — |
| SUPERVISOR_ASSIGNMENT_ID | PositionPEOSupervisorAssignmentId | ✅ |
| SUPERVISOR_ID | PositionPEOSupervisorId | ✅ |
| TIME_NORMAL_FINISH | PositionPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | PositionPEOTimeNormalStart | ✅ |
| UNION_ID | PositionPEOUnionId | — |
| WORKING_HOURS | PositionPEOWorkingHours | ✅ |

### [[positionrefpvo|PositionRefPVO]] (PO · BICC: 6/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | PositionPEOActionOccurrenceId | — |
| ACTIVE_STATUS | PositionPEOActiveStatus | ✅ |
| ATTRIBUTE_CATEGORY | PositionPEOAttributeCategory | — |
| BARGAINING_UNIT_CD | PositionPEOBargainingUnitCd | — |
| BUSINESS_GROUP_ID | PositionPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | PositionPEOBusinessUnitId | — |
| CALCULATE_FTE | PositionPEOCalculateFte | — |
| CREATED_BY | PositionPEOCreatedBy | — |
| CREATION_DATE | PositionPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_ID | PositionPEOJobId | — |
| LAST_UPDATE_DATE | PositionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PositionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PositionPEOLastUpdatedBy | — |
| LOCATION_ID | PositionPEOLocationId | — |
| OBJECT_VERSION_NUMBER | PositionPEOObjectVersionNumber | — |
| ORGANIZATION_ID | PositionPEOOrganizationId | — |
| POSITION_CODE | PositionPEOPositionCode | ✅ |
| POSITION_ID | PositionId | ✅ |
