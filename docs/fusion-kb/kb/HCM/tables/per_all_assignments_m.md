---
id: DOC-HCM-626
doc_type: system-doc
title: "PER_ALL_ASSIGNMENTS_M — Atribuições/Designações (Materializada)"
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
  - assignments
  - designacoes
  - workforce
aliases:
  - PER_ALL_ASSIGNMENTS_M
  - per_all_assignments_m
  - per-all-assignments-m
  - atribuições/designações-(materializada)
  - per-all-assignments-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALL_ASSIGNMENTS_M

## 📌 Visão Geral

Tabela **materializada** que armazena todas as **atribuições (assignments)** de colaboradores. Contém informações sobre cargo, departamento, localização, grade, gerente e status de cada designação. É a tabela central para dados de workforce.

> [!note] Sufixo _M
> O sufixo `_M` indica tabela **materializada** — combina dados de múltiplas fontes para otimização de consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de workforce** — dados centrais de cada vínculo empregatício/designação.
- **Hierarquia organizacional** — relaciona colaborador com departamento, cargo e gerente.
- **Folha de pagamento** — base para cálculos de remuneração por assignment.
- **Relatórios de headcount** — fonte principal para contagem de colaboradores.
- **Movimentações** — histórico completo de mudanças no assignment do colaborador.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do assignment | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | ASSIGNMENT_NUMBER | VARCHAR2(30) | NOT NULL | Identificação | Número do assignment (ex.: E12345) | — | 🟢 95% |
| 6 | ASSIGNMENT_TYPE | VARCHAR2(1) | NOT NULL | Classificação | Tipo (E=Employee, C=Contingent, N=Non-worker) | — | 🟢 95% |
| 7 | ASSIGNMENT_STATUS_TYPE_ID | NUMBER(18) | NOT NULL | FK | Status do assignment | PER_ASSIGNMENT_STATUS_TYPES | 🟢 90% |
| 8 | ORGANIZATION_ID | NUMBER(18) | NULL | FK | Departamento/Organização | — | 🟢 90% |
| 9 | JOB_ID | NUMBER(18) | NULL | FK | Cargo (Job) | PER_JOBS_F | 🟢 90% |
| 10 | POSITION_ID | NUMBER(18) | NULL | FK | Posição | — | 🟢 90% |
| 11 | GRADE_ID | NUMBER(18) | NULL | FK | Grade salarial | PER_GRADES_F | 🟢 90% |
| 12 | LOCATION_ID | NUMBER(18) | NULL | FK | Localização | PER_LOCATIONS | 🟢 90% |
| 13 | MANAGER_ID | NUMBER(18) | NULL | FK | Gerente direto | PER_ALL_PEOPLE_F | 🟢 85% |
| 14 | LEGAL_ENTITY_ID | NUMBER(18) | NULL | FK | Entidade legal | — | 🟢 90% |
| 15 | BUSINESS_UNIT_ID | NUMBER(18) | NULL | FK | Unidade de negócio | — | 🟢 90% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 20 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador titular do vínculo empregatício)
- [[per_assignment_status_types]] — via `ASSIGNMENT_STATUS_TYPE_ID` (status do vínculo empregatício)
- [[per_jobs_f]] — via `JOB_ID` (cargo do vínculo empregatício)
- [[per_grades_f]] — via `GRADE_ID` (grade salarial do vínculo)
- [[per_locations]] — via `LOCATION_ID` (localização de trabalho do vínculo)

### Tabelas-filha (FK de saída)
- [[per_assignment_extra_info_m]] — via `ASSIGNMENT_ID` (informações extras)
- [[per_asg_responsibilities]] — via `ASSIGNMENT_ID` (responsabilidades)
- [[per_assignment_supervisors_f]] — via `ASSIGNMENT_ID` (supervisores do vínculo empregatício)
- [[per_assign_grade_steps_f]] — via `ASSIGNMENT_ID` (steps de grade salarial do vínculo)
- [[per_assign_work_measures_f]] — via `ASSIGNMENT_ID` (medidas de trabalho)

---

## 📎 Uso Típico

### Colaboradores ativos com cargo e departamento
```sql
SELECT paam.ASSIGNMENT_NUMBER, paam.ASSIGNMENT_TYPE,
       paam.ORGANIZATION_ID, paam.JOB_ID, paam.GRADE_ID
FROM   PER_ALL_ASSIGNMENTS_M paam
WHERE  paam.PERSON_ID = :p_person_id
  AND  paam.ASSIGNMENT_TYPE = 'E'
  AND  SYSDATE BETWEEN paam.EFFECTIVE_START_DATE AND paam.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ASSIGNMENT_TYPE = 'E'` — Empregados
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
- `ASSIGNMENT_STATUS_TYPE_ID` com status ACTIVE_ASSIGN — Assignments ativos
---

## 🔒 Observações

- Tabela materializada (_M) — combina dados de múltiplas fontes para performance.
- É a tabela mais consultada do HCM — base para praticamente todos os relatórios de workforce.
- Um colaborador pode ter múltiplos assignments simultaneamente (ex.: empregado + consultor).
- O `ASSIGNMENT_TYPE` é fundamental: E=Employee, C=Contingent Worker, N=Non-Worker.
- Sempre filtrar por vigência para obter o assignment corrente.
---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 4/279)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentApplicantRank | — |
| ASG_INFORMATION1 | AssignmentAsgInformation1 | — |
| ASG_INFORMATION10 | AssignmentAsgInformation10 | — |
| ASG_INFORMATION11 | AssignmentAsgInformation11 | — |
| ASG_INFORMATION12 | AssignmentAsgInformation12 | — |
| ASG_INFORMATION13 | AssignmentAsgInformation13 | — |
| ASG_INFORMATION14 | AssignmentAsgInformation14 | — |
| ASG_INFORMATION15 | AssignmentAsgInformation15 | — |
| ASG_INFORMATION16 | AssignmentAsgInformation16 | — |
| ASG_INFORMATION17 | AssignmentAsgInformation17 | — |
| ASG_INFORMATION18 | AssignmentAsgInformation18 | — |
| ASG_INFORMATION19 | AssignmentAsgInformation19 | — |
| ASG_INFORMATION2 | AssignmentAsgInformation2 | — |
| ASG_INFORMATION20 | AssignmentAsgInformation20 | — |
| ASG_INFORMATION21 | AssignmentAsgInformation21 | — |
| ASG_INFORMATION22 | AssignmentAsgInformation22 | — |
| ASG_INFORMATION23 | AssignmentAsgInformation23 | — |
| ASG_INFORMATION24 | AssignmentAsgInformation24 | — |
| ASG_INFORMATION25 | AssignmentAsgInformation25 | — |
| ASG_INFORMATION26 | AssignmentAsgInformation26 | — |
| ASG_INFORMATION27 | AssignmentAsgInformation27 | — |
| ASG_INFORMATION28 | AssignmentAsgInformation28 | — |
| ASG_INFORMATION29 | AssignmentAsgInformation29 | — |
| ASG_INFORMATION3 | AssignmentAsgInformation3 | — |
| ASG_INFORMATION30 | AssignmentAsgInformation30 | — |
| ASG_INFORMATION31 | AssignmentAsgInformation31 | — |
| ASG_INFORMATION32 | AssignmentAsgInformation32 | — |
| ASG_INFORMATION33 | AssignmentAsgInformation33 | — |
| ASG_INFORMATION34 | AssignmentAsgInformation34 | — |
| ASG_INFORMATION35 | AssignmentAsgInformation35 | — |
| ASG_INFORMATION36 | AssignmentAsgInformation36 | — |
| ASG_INFORMATION37 | AssignmentAsgInformation37 | — |
| ASG_INFORMATION38 | AssignmentAsgInformation38 | — |
| ASG_INFORMATION39 | AssignmentAsgInformation39 | — |
| ASG_INFORMATION4 | AssignmentAsgInformation4 | — |
| ASG_INFORMATION40 | AssignmentAsgInformation40 | — |
| ASG_INFORMATION41 | AssignmentAsgInformation41 | — |
| ASG_INFORMATION42 | AssignmentAsgInformation42 | — |
| ASG_INFORMATION43 | AssignmentAsgInformation43 | — |
| ASG_INFORMATION44 | AssignmentAsgInformation44 | — |
| ASG_INFORMATION45 | AssignmentAsgInformation45 | — |
| ASG_INFORMATION46 | AssignmentAsgInformation46 | — |
| ASG_INFORMATION47 | AssignmentAsgInformation47 | — |
| ASG_INFORMATION48 | AssignmentAsgInformation48 | — |
| ASG_INFORMATION49 | AssignmentAsgInformation49 | — |
| ASG_INFORMATION5 | AssignmentAsgInformation5 | — |
| ASG_INFORMATION50 | AssignmentAsgInformation50 | — |
| ASG_INFORMATION6 | AssignmentAsgInformation6 | — |
| ASG_INFORMATION7 | AssignmentAsgInformation7 | — |
| ASG_INFORMATION8 | AssignmentAsgInformation8 | — |
| ASG_INFORMATION9 | AssignmentAsgInformation9 | — |
| ASG_INFORMATION_CATEGORY | AssignmentAsgInformationCategory | — |
| ASG_INFORMATION_DATE1 | AssignmentAsgInformationDate1 | — |
| ASG_INFORMATION_DATE10 | AssignmentAsgInformationDate10 | — |
| ASG_INFORMATION_DATE11 | AssignmentAsgInformationDate11 | — |
| ASG_INFORMATION_DATE12 | AssignmentAsgInformationDate12 | — |
| ASG_INFORMATION_DATE13 | AssignmentAsgInformationDate13 | — |
| ASG_INFORMATION_DATE14 | AssignmentAsgInformationDate14 | — |
| ASG_INFORMATION_DATE15 | AssignmentAsgInformationDate15 | — |
| ASG_INFORMATION_DATE2 | AssignmentAsgInformationDate2 | — |
| ASG_INFORMATION_DATE3 | AssignmentAsgInformationDate3 | — |
| ASG_INFORMATION_DATE4 | AssignmentAsgInformationDate4 | — |
| ASG_INFORMATION_DATE5 | AssignmentAsgInformationDate5 | — |
| ASG_INFORMATION_DATE6 | AssignmentAsgInformationDate6 | — |
| ASG_INFORMATION_DATE7 | AssignmentAsgInformationDate7 | — |
| ASG_INFORMATION_DATE8 | AssignmentAsgInformationDate8 | — |
| ASG_INFORMATION_DATE9 | AssignmentAsgInformationDate9 | — |
| ASG_INFORMATION_NUMBER1 | AssignmentAsgInformationNumber1 | — |
| ASG_INFORMATION_NUMBER10 | AssignmentAsgInformationNumber10 | — |
| ASG_INFORMATION_NUMBER11 | AssignmentAsgInformationNumber11 | — |
| ASG_INFORMATION_NUMBER12 | AssignmentAsgInformationNumber12 | — |
| ASG_INFORMATION_NUMBER13 | AssignmentAsgInformationNumber13 | — |
| ASG_INFORMATION_NUMBER14 | AssignmentAsgInformationNumber14 | — |
| ASG_INFORMATION_NUMBER15 | AssignmentAsgInformationNumber15 | — |
| ASG_INFORMATION_NUMBER16 | AssignmentAsgInformationNumber16 | — |
| ASG_INFORMATION_NUMBER17 | AssignmentAsgInformationNumber17 | — |
| ASG_INFORMATION_NUMBER18 | AssignmentAsgInformationNumber18 | — |
| ASG_INFORMATION_NUMBER19 | AssignmentAsgInformationNumber19 | — |
| ASG_INFORMATION_NUMBER2 | AssignmentAsgInformationNumber2 | — |
| ASG_INFORMATION_NUMBER20 | AssignmentAsgInformationNumber20 | — |
| ASG_INFORMATION_NUMBER3 | AssignmentAsgInformationNumber3 | — |
| ASG_INFORMATION_NUMBER4 | AssignmentAsgInformationNumber4 | — |
| ASG_INFORMATION_NUMBER5 | AssignmentAsgInformationNumber5 | — |
| ASG_INFORMATION_NUMBER6 | AssignmentAsgInformationNumber6 | — |
| ASG_INFORMATION_NUMBER7 | AssignmentAsgInformationNumber7 | — |
| ASG_INFORMATION_NUMBER8 | AssignmentAsgInformationNumber8 | — |
| ASG_INFORMATION_NUMBER9 | AssignmentAsgInformationNumber9 | — |
| ASS_ATTRIBUTE1 | AssignmentAssAttribute1 | — |
| ASS_ATTRIBUTE10 | AssignmentAssAttribute10 | — |
| ASS_ATTRIBUTE11 | AssignmentAssAttribute11 | — |
| ASS_ATTRIBUTE12 | AssignmentAssAttribute12 | — |
| ASS_ATTRIBUTE13 | AssignmentAssAttribute13 | — |
| ASS_ATTRIBUTE14 | AssignmentAssAttribute14 | — |
| ASS_ATTRIBUTE15 | AssignmentAssAttribute15 | — |
| ASS_ATTRIBUTE16 | AssignmentAssAttribute16 | — |
| ASS_ATTRIBUTE17 | AssignmentAssAttribute17 | — |
| ASS_ATTRIBUTE18 | AssignmentAssAttribute18 | — |
| ASS_ATTRIBUTE19 | AssignmentAssAttribute19 | — |
| ASS_ATTRIBUTE2 | AssignmentAssAttribute2 | — |
| ASS_ATTRIBUTE20 | AssignmentAssAttribute20 | — |
| ASS_ATTRIBUTE21 | AssignmentAssAttribute21 | — |
| ASS_ATTRIBUTE22 | AssignmentAssAttribute22 | — |
| ASS_ATTRIBUTE23 | AssignmentAssAttribute23 | — |
| ASS_ATTRIBUTE24 | AssignmentAssAttribute24 | — |
| ASS_ATTRIBUTE25 | AssignmentAssAttribute25 | — |
| ASS_ATTRIBUTE26 | AssignmentAssAttribute26 | — |
| ASS_ATTRIBUTE27 | AssignmentAssAttribute27 | — |
| ASS_ATTRIBUTE28 | AssignmentAssAttribute28 | — |
| ASS_ATTRIBUTE29 | AssignmentAssAttribute29 | — |
| ASS_ATTRIBUTE3 | AssignmentAssAttribute3 | — |
| ASS_ATTRIBUTE30 | AssignmentAssAttribute30 | — |
| ASS_ATTRIBUTE31 | AssignmentAssAttribute31 | — |
| ASS_ATTRIBUTE32 | AssignmentAssAttribute32 | — |
| ASS_ATTRIBUTE33 | AssignmentAssAttribute33 | — |
| ASS_ATTRIBUTE34 | AssignmentAssAttribute34 | — |
| ASS_ATTRIBUTE35 | AssignmentAssAttribute35 | — |
| ASS_ATTRIBUTE36 | AssignmentAssAttribute36 | — |
| ASS_ATTRIBUTE37 | AssignmentAssAttribute37 | — |
| ASS_ATTRIBUTE38 | AssignmentAssAttribute38 | — |
| ASS_ATTRIBUTE39 | AssignmentAssAttribute39 | — |
| ASS_ATTRIBUTE4 | AssignmentAssAttribute4 | — |
| ASS_ATTRIBUTE40 | AssignmentAssAttribute40 | — |
| ASS_ATTRIBUTE41 | AssignmentAssAttribute41 | — |
| ASS_ATTRIBUTE42 | AssignmentAssAttribute42 | — |
| ASS_ATTRIBUTE43 | AssignmentAssAttribute43 | — |
| ASS_ATTRIBUTE44 | AssignmentAssAttribute44 | — |
| ASS_ATTRIBUTE45 | AssignmentAssAttribute45 | — |
| ASS_ATTRIBUTE46 | AssignmentAssAttribute46 | — |
| ASS_ATTRIBUTE47 | AssignmentAssAttribute47 | — |
| ASS_ATTRIBUTE48 | AssignmentAssAttribute48 | — |
| ASS_ATTRIBUTE49 | AssignmentAssAttribute49 | — |
| ASS_ATTRIBUTE5 | AssignmentAssAttribute5 | — |
| ASS_ATTRIBUTE50 | AssignmentAssAttribute50 | — |
| ASS_ATTRIBUTE6 | AssignmentAssAttribute6 | — |
| ASS_ATTRIBUTE7 | AssignmentAssAttribute7 | — |
| ASS_ATTRIBUTE8 | AssignmentAssAttribute8 | — |
| ASS_ATTRIBUTE9 | AssignmentAssAttribute9 | — |
| ASS_ATTRIBUTE_CATEGORY | AssignmentAssAttributeCategory | — |
| ASS_ATTRIBUTE_DATE1 | AssignmentAssAttributeDate1 | — |
| ASS_ATTRIBUTE_DATE10 | AssignmentAssAttributeDate10 | — |
| ASS_ATTRIBUTE_DATE11 | AssignmentAssAttributeDate11 | — |
| ASS_ATTRIBUTE_DATE12 | AssignmentAssAttributeDate12 | — |
| ASS_ATTRIBUTE_DATE13 | AssignmentAssAttributeDate13 | — |
| ASS_ATTRIBUTE_DATE14 | AssignmentAssAttributeDate14 | — |
| ASS_ATTRIBUTE_DATE15 | AssignmentAssAttributeDate15 | — |
| ASS_ATTRIBUTE_DATE2 | AssignmentAssAttributeDate2 | — |
| ASS_ATTRIBUTE_DATE3 | AssignmentAssAttributeDate3 | — |
| ASS_ATTRIBUTE_DATE4 | AssignmentAssAttributeDate4 | — |
| ASS_ATTRIBUTE_DATE5 | AssignmentAssAttributeDate5 | — |
| ASS_ATTRIBUTE_DATE6 | AssignmentAssAttributeDate6 | — |
| ASS_ATTRIBUTE_DATE7 | AssignmentAssAttributeDate7 | — |
| ASS_ATTRIBUTE_DATE8 | AssignmentAssAttributeDate8 | — |
| ASS_ATTRIBUTE_DATE9 | AssignmentAssAttributeDate9 | — |
| ASS_ATTRIBUTE_NUMBER1 | AssignmentAssAttributeNumber1 | — |
| ASS_ATTRIBUTE_NUMBER10 | AssignmentAssAttributeNumber10 | — |
| ASS_ATTRIBUTE_NUMBER11 | AssignmentAssAttributeNumber11 | — |
| ASS_ATTRIBUTE_NUMBER12 | AssignmentAssAttributeNumber12 | — |
| ASS_ATTRIBUTE_NUMBER13 | AssignmentAssAttributeNumber13 | — |
| ASS_ATTRIBUTE_NUMBER14 | AssignmentAssAttributeNumber14 | — |
| ASS_ATTRIBUTE_NUMBER15 | AssignmentAssAttributeNumber15 | — |
| ASS_ATTRIBUTE_NUMBER16 | AssignmentAssAttributeNumber16 | — |
| ASS_ATTRIBUTE_NUMBER17 | AssignmentAssAttributeNumber17 | — |
| ASS_ATTRIBUTE_NUMBER18 | AssignmentAssAttributeNumber18 | — |
| ASS_ATTRIBUTE_NUMBER19 | AssignmentAssAttributeNumber19 | — |
| ASS_ATTRIBUTE_NUMBER2 | AssignmentAssAttributeNumber2 | — |
| ASS_ATTRIBUTE_NUMBER20 | AssignmentAssAttributeNumber20 | — |
| ASS_ATTRIBUTE_NUMBER3 | AssignmentAssAttributeNumber3 | — |
| ASS_ATTRIBUTE_NUMBER4 | AssignmentAssAttributeNumber4 | — |
| ASS_ATTRIBUTE_NUMBER5 | AssignmentAssAttributeNumber5 | — |
| ASS_ATTRIBUTE_NUMBER6 | AssignmentAssAttributeNumber6 | — |
| ASS_ATTRIBUTE_NUMBER7 | AssignmentAssAttributeNumber7 | — |
| ASS_ATTRIBUTE_NUMBER8 | AssignmentAssAttributeNumber8 | — |
| ASS_ATTRIBUTE_NUMBER9 | AssignmentAssAttributeNumber9 | — |
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentAssignmentType | — |
| AUTO_END_FLAG | AssignmentAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentBargainingUnitCode | — |
| BILLING_TITLE | AssignmentBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentContractId | — |
| CREATED_BY | AssignmentCreatedBy | — |
| CREATION_DATE | AssignmentCreationDate | — |
| DATE_PROBATION_END | AssignmentDateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentDefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentDutiesType | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentFreezeUntilDate | — |
| FREQUENCY | AssignmentFrequency | — |
| GRADE_ID | AssignmentGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentInternalFloor | — |
| INTERNAL_LOCATION | AssignmentInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentInternalOfficeNumber | — |
| JOB_ID | AssignmentJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| LEGISLATION_CODE | AssignmentLegislationCode | — |
| LINKAGE_TYPE | AssignmentLinkageType | — |
| LOCATION_ID | AssignmentLocationId | — |
| MANAGER_FLAG | AssignmentManagerFlag | — |
| NORMAL_HOURS | AssignmentNormalHours | — |
| NOTICE_PERIOD | AssignmentNoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentNoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPeriodOfServiceId | — |
| PERSON_ID | AssignmentPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPersonTypeId | — |
| PO_HEADER_ID | AssignmentPoHeaderId | — |
| PO_LINE_ID | AssignmentPoLineId | — |
| POSITION_ID | AssignmentPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentProbationPeriod | — |
| PROBATION_UNIT | AssignmentProbationUnit | — |
| PROJECT_TITLE | AssignmentProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentProposedWorkerType | — |
| REASON_CODE | AssignmentReasonCode | — |
| RECORD_CREATOR | AssignmentRecordCreator | — |
| RECRUITER_ID | AssignmentRecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentRecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentRetirementAge | — |
| RETIREMENT_DATE | AssignmentRetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentTimeNormalStart | — |
| VACANCY_ID | AssignmentVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentVendorId | — |
| VENDOR_SITE_ID | AssignmentVendorSiteId | — |
| WORK_AT_HOME | AssignmentWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentWorkTermsAssignmentId | — |

### [[assignmentdatefilterpvo|AssignmentDateFilterPVO]] (HCM · BICC: 6/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[assignmentfactpvo|AssignmentFactPVO]] (HCM · BICC: 73/127)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | ✅ |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | ✅ |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | ✅ |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | ✅ |
| BILLING_TITLE | AssignmentPEOBillingTitle | ✅ |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | ✅ |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentPEOCreationDate | ✅ |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | ✅ |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | ✅ |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | ✅ |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | ✅ |
| FREQUENCY | AssignmentPEOFrequency | ✅ |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | ✅ |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | ✅ |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | ✅ |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | ✅ |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | ✅ |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | ✅ |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | ✅ |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | ✅ |
| LAST_WORKING_DATE | AssignmentPEOLastWorkingDate | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | ✅ |
| LINKAGE_TYPE | AssignmentPEOLinkageType | ✅ |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | ✅ |
| NORMAL_HOURS | AssignmentPEONormalHours | ✅ |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | ✅ |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | ✅ |
| NOTIFICATION_DATE | AssignmentPEONotificationDate | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | ✅ |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | ✅ |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | ✅ |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | ✅ |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | ✅ |
| PROBATION_UNIT | AssignmentPEOProbationUnit | ✅ |
| PROJECT_TITLE | AssignmentPEOProjectTitle | ✅ |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | ✅ |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | ✅ |
| REASON_CODE | AssignmentPEOReasonCode | ✅ |
| RECORD_CREATOR | AssignmentPEORecordCreator | ✅ |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| REHIRE_AUTHORIZER_PERSON_ID | AssignmentPEORehireAuthorizerPersonId | — |
| REHIRE_REASON | AssignmentPEORehireReason | — |
| REHIRE_RECOMMENDATION | AssignmentPEORehireRecommendation | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | ✅ |
| RETIREMENT_DATE | AssignmentPEORetirementDate | ✅ |
| REVIEW_USER_ACCESS | AssignmentPEOReviewUserAccess | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | ✅ |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | ✅ |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | ✅ |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | ✅ |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | ✅ |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | ✅ |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TERMINATION_DATE | AssignmentPEOTerminationDate | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | ✅ |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | ✅ |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | ✅ |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | ✅ |

### [[assignmentnodepvo|AssignmentNoDePVO]] (HCM · BICC: 71/125)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentNoDePEOActionCode | ✅ |
| ACTION_OCCURRENCE_ID | AssignmentNoDePEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentNoDePEOAdjustedFte | — |
| ANNUAL_WORKING_DURATION | AssignmentNoDePEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentNoDePEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentNoDePEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentNoDePEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentNoDePEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentNoDePEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentNoDePEOAssignmentSequence | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentNoDePEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentNoDePEOAssignmentStatusTypeId | ✅ |
| ASSIGNMENT_TYPE | AssignmentNoDePEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentNoDePEOAutoEndFlag | ✅ |
| BARGAINING_UNIT_CODE | AssignmentNoDePEOBargainingUnitCode | ✅ |
| BILLING_TITLE | AssignmentNoDePEOBillingTitle | ✅ |
| BUSINESS_GROUP_ID | AssignmentNoDePEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentNoDePEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentNoDePEOCagrGradeDefId | — |
| CATEGORY_CODE | AssignmentNoDePEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentNoDePEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentNoDePEOContractId | — |
| CREATED_BY | AssignmentNoDePEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentNoDePEOCreationDate | ✅ |
| DATE_PROBATION_END | AssignmentNoDePEODateProbationEnd | ✅ |
| DEFAULT_CODE_COMB_ID | AssignmentNoDePEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentNoDePEODutiesType | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentNoDePEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentNoDePEOEmploymentCategory | ✅ |
| ESTABLISHMENT_ID | AssignmentNoDePEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentNoDePEOExpenseCheckAddress | ✅ |
| FREQUENCY | AssignmentNoDePEOFrequency | ✅ |
| FULL_PART_TIME | AssignmentNoDePEOFullPartTime | — |
| GRADE_ID | AssignmentNoDePEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentNoDePEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentNoDePEOGspEligibilityFlag | ✅ |
| HOURLY_SALARIED_CODE | AssignmentNoDePEOHourlySalariedCode | ✅ |
| ID_FLEX_NUM | AssignmentNoDePEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentNoDePEOInternalBuilding | ✅ |
| INTERNAL_FLOOR | AssignmentNoDePEOInternalFloor | ✅ |
| INTERNAL_LOCATION | AssignmentNoDePEOInternalLocation | ✅ |
| INTERNAL_MAILSTOP | AssignmentNoDePEOInternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | AssignmentNoDePEOInternalOfficeNumber | ✅ |
| JOB_ID | AssignmentNoDePEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentNoDePEOJobPostSourceName | ✅ |
| LABOUR_UNION_MEMBER_FLAG | AssignmentNoDePEOLabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | AssignmentNoDePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentNoDePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AssignmentNoDePEOLastUpdatedBy | ✅ |
| LAST_WORKING_DATE | AssignmentNoDePEOLastWorkingDate | — |
| LEGAL_ENTITY_ID | AssignmentNoDePEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentNoDePEOLegislationCode | ✅ |
| LINKAGE_TYPE | AssignmentNoDePEOLinkageType | ✅ |
| LOCATION_ID | AssignmentNoDePEOLocationId | — |
| MANAGER_FLAG | AssignmentNoDePEOManagerFlag | ✅ |
| NORMAL_HOURS | AssignmentNoDePEONormalHours | ✅ |
| NOTICE_PERIOD | AssignmentNoDePEONoticePeriod | ✅ |
| NOTICE_PERIOD_UOM | AssignmentNoDePEONoticePeriodUom | ✅ |
| NOTIFICATION_DATE | AssignmentNoDePEONotificationDate | — |
| OBJECT_VERSION_NUMBER | AssignmentNoDePEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentNoDePEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentNoDePEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentNoDePEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentNoDePEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentNoDePEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentNoDePEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentNoDePEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentNoDePEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentNoDePEOPersonTypeId | ✅ |
| PO_HEADER_ID | AssignmentNoDePEOPoHeaderId | — |
| PO_LINE_ID | AssignmentNoDePEOPoLineId | — |
| POSITION_ID | AssignmentNoDePEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentNoDePEOPositionOverrideFlag | ✅ |
| POSTING_CONTENT_ID | AssignmentNoDePEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentNoDePEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentNoDePEOPrimaryFlag | ✅ |
| PRIMARY_WORK_RELATION_FLAG | AssignmentNoDePEOPrimaryWorkRelationFlag | ✅ |
| PRIMARY_WORK_TERMS_FLAG | AssignmentNoDePEOPrimaryWorkTermsFlag | ✅ |
| PROBATION_PERIOD | AssignmentNoDePEOProbationPeriod | ✅ |
| PROBATION_UNIT | AssignmentNoDePEOProbationUnit | ✅ |
| PROJECT_TITLE | AssignmentNoDePEOProjectTitle | ✅ |
| PROJECTED_ASSIGNMENT_END | AssignmentNoDePEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentNoDePEOProjectedStartDate | ✅ |
| PROPOSED_WORKER_TYPE | AssignmentNoDePEOProposedWorkerType | ✅ |
| REASON_CODE | AssignmentNoDePEOReasonCode | ✅ |
| RECORD_CREATOR | AssignmentNoDePEORecordCreator | ✅ |
| RECRUITER_ID | AssignmentNoDePEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentNoDePEORecruitmentActivityId | — |
| REHIRE_AUTHORIZER_PERSON_ID | AssignmentNoDePEORehireAuthorizerPersonId | — |
| REHIRE_REASON | AssignmentNoDePEORehireReason | — |
| REHIRE_RECOMMENDATION | AssignmentNoDePEORehireRecommendation | — |
| RETIREMENT_AGE | AssignmentNoDePEORetirementAge | ✅ |
| RETIREMENT_DATE | AssignmentNoDePEORetirementDate | ✅ |
| REVIEW_USER_ACCESS | AssignmentNoDePEOReviewUserAccess | — |
| SAL_REVIEW_PERIOD | AssignmentNoDePEOSalReviewPeriod | ✅ |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentNoDePEOSalReviewPeriodFrequency | ✅ |
| SENIORITY_BASIS | AssignmentNoDePEOSeniorityBasis | ✅ |
| SET_OF_BOOKS_ID | AssignmentNoDePEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentNoDePEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentNoDePEOSourceAssignmentId | ✅ |
| SOURCE_ORGANIZATION_ID | AssignmentNoDePEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentNoDePEOSourceType | ✅ |
| SPECIAL_CEILING_STEP_ID | AssignmentNoDePEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentNoDePEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentNoDePEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentNoDePEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentNoDePEOStepEntryDate | ✅ |
| SYSTEM_PERSON_TYPE | AssignmentNoDePEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentNoDePEOTaxAddressId | — |
| TERMINATION_DATE | AssignmentNoDePEOTerminationDate | — |
| TIME_NORMAL_FINISH | AssignmentNoDePEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentNoDePEOTimeNormalStart | ✅ |
| UNION_ID | AssignmentNoDePEOUnionId | — |
| VACANCY_ID | AssignmentNoDePEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentNoDePEOVendorAssignmentNumber | ✅ |
| VENDOR_EMPLOYEE_NUMBER | AssignmentNoDePEOVendorEmployeeNumber | ✅ |
| VENDOR_ID | AssignmentNoDePEOVendorId | — |
| VENDOR_SITE_ID | AssignmentNoDePEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentNoDePEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentNoDePEOWorkTermsAssignmentId | ✅ |

### [[assignmentpvo|AssignmentPVO]] (HCM · BICC: 37/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | ✅ |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | ✅ |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | ✅ |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | ✅ |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | ✅ |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | ✅ |
| MANAGER_FLAG | AssignmentPEOManagerFlag | ✅ |
| NORMAL_HOURS | AssignmentPEONormalHours | ✅ |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | ✅ |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | ✅ |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | ✅ |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | ✅ |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | ✅ |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | ✅ |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | ✅ |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | ✅ |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | ✅ |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[assignmentpvoeffectivelatestchange|AssignmentPVOEffectiveLatestChange]] (HCM · BICC: 13/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | ✅ |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | ✅ |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[assignmentpvotermsrow|AssignmentPVOTermsRow]] (HCM · BICC: 7/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[depreciationextractpvo|DepreciationExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| ASSIGNMENT_NAME | AssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentNumber | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | EffectiveSequence | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| LOCATION_ID | LocationId1 | — |

### [[deviceeventpvo|DeviceEventPVO]] (GL · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |

### [[expenditureitempvo|ExpenditureItemPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentDPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentDPEOAssignmentName | ✅ |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |

### [[expenditureitemrefpvo|ExpenditureItemRefPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentDPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentDPEOAssignmentName | ✅ |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER · BICC: 1/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentApplicantRank | — |
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentAssignmentType | — |
| AUTO_END_FLAG | AssignmentAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentBargainingUnitCode | — |
| BILLING_TITLE | AssignmentBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentContractId | — |
| CREATED_BY | AssignmentCreatedBy | — |
| CREATION_DATE | AssignmentCreationDate | — |
| DATE_PROBATION_END | AssignmentDateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentDefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentDutiesType | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | ExpAssignmentEffectiveStartDate | — |
| EMPLOYEE_CATEGORY | AssignmentEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | ✅ |
| FREEZE_START_DATE | AssignmentFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentFreezeUntilDate | — |
| FREQUENCY | AssignmentFrequency | — |
| FULL_PART_TIME | AssignmentFullPartTime | — |
| GRADE_ID | AssignmentGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentInternalFloor | — |
| INTERNAL_LOCATION | AssignmentInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentInternalOfficeNumber | — |
| JOB_ID | AssignmentJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentLastUpdateDate | — |
| LAST_UPDATE_LOGIN | AssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| LEGISLATION_CODE | AssignmentLegislationCode | — |
| LINKAGE_TYPE | AssignmentLinkageType | — |
| LOCATION_ID | AssignmentLocationId | — |
| MANAGER_FLAG | AssignmentManagerFlag | — |
| NORMAL_HOURS | AssignmentNormalHours | — |
| NOTICE_PERIOD | AssignmentNoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentNoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPersonTypeId | — |
| PO_HEADER_ID | AssignmentPoHeaderId | — |
| PO_LINE_ID | AssignmentPoLineId | — |
| POSITION_ID | AssignmentPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentProbationPeriod | — |
| PROBATION_UNIT | AssignmentProbationUnit | — |
| PROJECT_TITLE | AssignmentProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentProposedWorkerType | — |
| REASON_CODE | AssignmentReasonCode | — |
| RECORD_CREATOR | AssignmentRecordCreator | — |
| RECRUITER_ID | AssignmentRecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentRecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentRetirementAge | — |
| RETIREMENT_DATE | AssignmentRetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentTimeNormalStart | — |
| VACANCY_ID | AssignmentVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentVendorId | — |
| VENDOR_SITE_ID | AssignmentVendorSiteId | — |
| WORK_AT_HOME | AssignmentWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentWorkTermsAssignmentId | — |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | ✅ |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| PERSON_ID | AssignmentPersonId | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | ExpAssignmentEffectiveStartDate | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | ✅ |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| PERSON_ID | AssignmentPersonId | — |

### [[expensereportpvo|ExpenseReportPVO]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | ✅ |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| PERSON_ID | AssignmentPersonId | — |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | ✅ |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| PERSON_ID | AssignmentPersonId | — |

### [[fabalancesextractpvo|FaBalancesExtractPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[fatransactionextractpvo|FaTransactionExtractPVO]] (OTHER · BICC: 1/113)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate1 | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange1 | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence1 | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate1 | — |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 119/128)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | ✅ |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | ✅ |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | ✅ |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentMgrPEOAssignmentId | ✅ |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentMgrPEOAssignmentNumber | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | ✅ |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | ✅ |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | ✅ |
| BILLING_TITLE | AssignmentPEOBillingTitle | ✅ |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | ✅ |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | ✅ |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | ✅ |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | ✅ |
| CONTRACT_ID | AssignmentPEOContractId | ✅ |
| CREATED_BY | AssignmentPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentPEOCreationDate | ✅ |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | ✅ |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | ✅ |
| DUTIES_TYPE | AssignmentPEODutiesType | ✅ |
| EFFECTIVE_END_DATE | AssignmentMgrPEOEffectiveEndDate | ✅ |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentMgrPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | AssignmentMgrPEOEffectiveSequence | ✅ |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | AssignmentMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | ✅ |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | ✅ |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | ✅ |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | ✅ |
| FREQUENCY | AssignmentPEOFrequency | ✅ |
| FULL_PART_TIME | AssignmentPEOFullPartTime | ✅ |
| GRADE_ID | AssignmentPEOGradeId | ✅ |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | ✅ |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | ✅ |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | ✅ |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | ✅ |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | ✅ |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | ✅ |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | ✅ |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | ✅ |
| JOB_ID | AssignmentPEOJobId | ✅ |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | ✅ |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | AssignmentMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | ✅ |
| LEGISLATION_CODE | AssignmentMgrPEOLegislativeCode | ✅ |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | ✅ |
| LINKAGE_TYPE | AssignmentPEOLinkageType | ✅ |
| LOCATION_ID | AssignmentPEOLocationId | ✅ |
| MANAGER_FLAG | AssignmentPEOManagerFlag | ✅ |
| NORMAL_HOURS | AssignmentPEONormalHours | ✅ |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | ✅ |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | ✅ |
| NOTIFICATION_DATE | AssignmentPEONotificationDate | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | ✅ |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | ✅ |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | ✅ |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | ✅ |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | ✅ |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | ✅ |
| PERSON_ID | AssignmentPEOPersonId | ✅ |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | ✅ |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | ✅ |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | ✅ |
| PO_LINE_ID | AssignmentPEOPoLineId | ✅ |
| POSITION_ID | AssignmentPEOPositionId | ✅ |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | ✅ |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | ✅ |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | ✅ |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | ✅ |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | ✅ |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | ✅ |
| PROBATION_UNIT | AssignmentPEOProbationUnit | ✅ |
| PROJECT_TITLE | AssignmentPEOProjectTitle | ✅ |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | ✅ |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | ✅ |
| REASON_CODE | AssignmentPEOReasonCode | ✅ |
| RECORD_CREATOR | AssignmentPEORecordCreator | ✅ |
| RECRUITER_ID | AssignmentPEORecruiterId | ✅ |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | ✅ |
| RETIREMENT_AGE | AssignmentPEORetirementAge | ✅ |
| RETIREMENT_DATE | AssignmentPEORetirementDate | ✅ |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | ✅ |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | ✅ |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | ✅ |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | ✅ |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | ✅ |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | ✅ |
| SOURCE_TYPE | AssignmentPEOSourceType | ✅ |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | ✅ |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | ✅ |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | ✅ |
| TERMINATION_DATE | AssignmentPEOTerminationDate | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | ✅ |
| VACANCY_ID | AssignmentPEOVacancyId | ✅ |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | ✅ |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | ✅ |
| VENDOR_ID | AssignmentPEOVendorId | ✅ |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | ✅ |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 70/128)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | ✅ |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | ✅ |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentMgrPEOAssignmentId | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentMgrPEOAssignmentNumber | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | ✅ |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | ✅ |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | ✅ |
| BILLING_TITLE | AssignmentPEOBillingTitle | ✅ |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | ✅ |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | ✅ |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | ✅ |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | ✅ |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | ✅ |
| EFFECTIVE_END_DATE | AssignmentMgrPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentMgrPEOEffectiveLatestChange | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | AssignmentMgrPEOEffectiveSequence | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | AssignmentMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | ✅ |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | ✅ |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | ✅ |
| FREQUENCY | AssignmentPEOFrequency | ✅ |
| FULL_PART_TIME | AssignmentPEOFullPartTime | ✅ |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | ✅ |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | ✅ |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | ✅ |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | ✅ |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | ✅ |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | ✅ |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | ✅ |
| LAST_UPDATE_DATE | AssignmentMgrPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentMgrPEOLegislativeCode | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | ✅ |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | ✅ |
| NORMAL_HOURS | AssignmentPEONormalHours | ✅ |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | ✅ |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | ✅ |
| NOTIFICATION_DATE | AssignmentPEONotificationDate | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | ✅ |
| PERSON_ID | AssignmentPEOPersonId | ✅ |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | ✅ |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | ✅ |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | ✅ |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | ✅ |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | ✅ |
| PROBATION_UNIT | AssignmentPEOProbationUnit | ✅ |
| PROJECT_TITLE | AssignmentPEOProjectTitle | ✅ |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | ✅ |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | ✅ |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | ✅ |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | ✅ |
| RETIREMENT_DATE | AssignmentPEORetirementDate | ✅ |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | ✅ |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | ✅ |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | ✅ |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | ✅ |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | ✅ |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TERMINATION_DATE | AssignmentPEOTerminationDate | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | ✅ |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | ✅ |

### [[goalplanassignmentfactp1|GoalPlanAssignmentFactP1]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[institutioncontactspvo|InstitutionContactsPVO]] (OTHER · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentDPEOAssignmentId | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentDPEOAssignmentStatusType | — |
| ASSIGNMENT_TYPE | AssignmentDPEOAssignmentType | — |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |
| JOB_ID | AssignmentDPEOJobId | — |
| OBJECT_VERSION_NUMBER | AssignmentDPEOObjectVersionNumber | — |
| PRIMARY_FLAG | AssignmentDPEOPrimaryFlag | — |

### [[offersalarypvo|OfferSalaryPVO]] (HCM · BICC: 2/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId1 | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate1 | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange1 | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_SEQUENCE | EffectiveSequence1 | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate1 | ✅ |
| PERSON_ID | AssignmentPEOPersonId | — |

### [[personabsdailydetailpvo|PersonAbsDailyDetailPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[personabsplanentrypvo|PersonAbsPlanEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[personabstypeentrypvo|PersonAbsTypeEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[personaccrualentrydtlpvo|PersonAccrualEntryDtlPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[personaccrualentrypvo|PersonAccrualEntryPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[persondonationentrydtlpvo|PersonDonationEntryDtlPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[personmanagerhierarchyassignmentpvo|PersonManagerHierarchyAssignmentPVO]] (HCM · BICC: 15/107)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | ✅ |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | ✅ |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentPEOCreationDate | ✅ |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | ✅ |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERSON_ID | AssignmentPEOPersonId | ✅ |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | ✅ |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | ✅ |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 27/113)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | ✅ |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | ✅ |
| ASSIGNMENT_ID | AssignmentMgrPEOAssignmentId | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | ✅ |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | ✅ |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | ✅ |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | ✅ |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | ✅ |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentMgrPEOEffectiveEndDate | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentMgrPEOEffectiveLatestChange | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | AssignmentMgrPEOEffectiveSequence | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | AssignmentMgrPEOEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | ✅ |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | ✅ |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | ✅ |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentMgrPEOLegislationCode | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | ✅ |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | ✅ |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | ✅ |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | ✅ |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | ✅ |
| RETIREMENT_DATE | AssignmentPEORetirementDate | ✅ |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | ✅ |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | ✅ |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | ✅ |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | ✅ |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[presalarypvo|PreSalaryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |
| PERSON_ID | AssignmentPEOPersonId | — |

### [[primaryassignmentpvo|PrimaryAssignmentPVO]] (HCM · BICC: 9/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ADJUSTED_FTE | AssignmentPEOAdjustedFte | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| ANNUAL_WORKING_DURATION | AssignmentPEOAnnualWorkingDuration | — |
| ANNUAL_WORKING_DURATION_UNITS | AssignmentPEOAnnualWorkingDurationUnits | — |
| ANNUAL_WORKING_RATIO | AssignmentPEOAnnualWorkingRatio | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | ✅ |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | ✅ |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| CATEGORY_CODE | AssignmentPEOCategoryCode | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| GSP_ELIGIBILITY_FLAG | AssignmentPEOGspEligibilityFlag | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| OVERTIME_PERIOD | AssignmentPEOOvertimePeriod | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | ✅ |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SENIORITY_BASIS | AssignmentPEOSeniorityBasis | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ASSIGNMENT_ID | AssignmentPEOSourceAssignmentId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STANDARD_FREQUENCY | AssignmentPEOStandardFrequency | — |
| STANDARD_HOURS | AssignmentPEOStandardHours | — |
| STD_ANNUAL_WORKING_DURATION | AssignmentPEOStdAnnualWorkingDuration | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| UNION_ID | AssignmentPEOUnionId | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[projectcostdistributionpvo|ProjectCostDistributionPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentDPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentDPEOAssignmentName | ✅ |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |

### [[projectunprocessedcosttransactionpvo|ProjectUnprocessedCostTransactionPVO]] (OTHER · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentDPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentDPEOAssignmentName | ✅ |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |

### [[qualityactionrelationship|QualityActionRelationship]] (OTHER · BICC: 2/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[qualityactions|QualityActions]] (OTHER · BICC: 2/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[qualityaffectedobjects|QualityAffectedObjects]] (OTHER · BICC: 1/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentApplicantRank | — |
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentAssignmentType | — |
| AUTO_END_FLAG | AssignmentAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentBargainingUnitCode | — |
| BILLING_TITLE | AssignmentBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentContractId | — |
| CREATED_BY | AssignmentCreatedBy | — |
| CREATION_DATE | AssignmentCreationDate | — |
| DATE_PROBATION_END | AssignmentDateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentDefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentDutiesType | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | — |
| EMPLOYEE_CATEGORY | AssignmentEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentFreezeUntilDate | — |
| FREQUENCY | AssignmentFrequency | — |
| FULL_PART_TIME | AssignmentFullPartTime | — |
| GRADE_ID | AssignmentGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentInternalFloor | — |
| INTERNAL_LOCATION | AssignmentInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentInternalOfficeNumber | — |
| JOB_ID | AssignmentJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| LEGISLATION_CODE | AssignmentLegislationCode | — |
| LINKAGE_TYPE | AssignmentLinkageType | — |
| LOCATION_ID | AssignmentLocationId | — |
| MANAGER_FLAG | AssignmentManagerFlag | — |
| NORMAL_HOURS | AssignmentNormalHours | — |
| NOTICE_PERIOD | AssignmentNoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentNoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPersonTypeId | — |
| PO_HEADER_ID | AssignmentPoHeaderId | — |
| PO_LINE_ID | AssignmentPoLineId | — |
| POSITION_ID | AssignmentPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentProbationPeriod | — |
| PROBATION_UNIT | AssignmentProbationUnit | — |
| PROJECT_TITLE | AssignmentProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentProposedWorkerType | — |
| REASON_CODE | AssignmentReasonCode | — |
| RECORD_CREATOR | AssignmentRecordCreator | — |
| RECRUITER_ID | AssignmentRecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentRecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentRetirementAge | — |
| RETIREMENT_DATE | AssignmentRetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentTimeNormalStart | — |
| VACANCY_ID | AssignmentVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentVendorId | — |
| VENDOR_SITE_ID | AssignmentVendorSiteId | — |
| WORK_AT_HOME | AssignmentWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentWorkTermsAssignmentId | — |

### [[qualityaffectedobjectsaction|QualityAffectedObjectsAction]] (OTHER · BICC: 2/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPAssignmentType | — |
| AUTO_END_FLAG | AssignmentPAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPContractId | — |
| CREATED_BY | AssignmentPCreatedBy | — |
| CREATION_DATE | AssignmentPCreationDate | — |
| DATE_PROBATION_END | AssignmentPDateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPDefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPDutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPFreezeUntilDate | — |
| FREQUENCY | AssignmentPFrequency | — |
| FULL_PART_TIME | AssignmentPFullPartTime | — |
| GRADE_ID | AssignmentPGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPInternalOfficeNumber | — |
| JOB_ID | AssignmentPJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPLegislationCode | — |
| LINKAGE_TYPE | AssignmentPLinkageType | — |
| LOCATION_ID | AssignmentPLocationId | — |
| MANAGER_FLAG | AssignmentPManagerFlag | — |
| NORMAL_HOURS | AssignmentPNormalHours | — |
| NOTICE_PERIOD | AssignmentPNoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPNoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPPersonTypeId | — |
| PO_HEADER_ID | AssignmentPPoHeaderId | — |
| PO_LINE_ID | AssignmentPPoLineId | — |
| POSITION_ID | AssignmentPPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPProbationPeriod | — |
| PROBATION_UNIT | AssignmentPProbationUnit | — |
| PROJECT_TITLE | AssignmentPProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPProposedWorkerType | — |
| REASON_CODE | AssignmentPReasonCode | — |
| RECORD_CREATOR | AssignmentPRecordCreator | — |
| RECRUITER_ID | AssignmentPRecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPRecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPRetirementAge | — |
| RETIREMENT_DATE | AssignmentPRetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPTimeNormalStart | — |
| VACANCY_ID | AssignmentPVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPVendorId | — |
| VENDOR_SITE_ID | AssignmentPVendorSiteId | — |
| WORK_AT_HOME | AssignmentPWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPWorkTermsAssignmentId | — |

### [[qualityissues|QualityIssues]] (OTHER · BICC: 2/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentApplicantRank | — |
| ASSIGNMENT_ID | AssignmentAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentAssignmentType | — |
| AUTO_END_FLAG | AssignmentAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentBargainingUnitCode | — |
| BILLING_TITLE | AssignmentBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentContractId | — |
| CREATED_BY | AssignmentCreatedBy1 | — |
| CREATION_DATE | AssignmentCreationDate1 | — |
| DATE_PROBATION_END | AssignmentDateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentDefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentDutiesType | — |
| EFFECTIVE_END_DATE | AssignmentEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentFreezeUntilDate | — |
| FREQUENCY | AssignmentFrequency | — |
| FULL_PART_TIME | AssignmentFullPartTime | — |
| GRADE_ID | AssignmentGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentInternalFloor | — |
| INTERNAL_LOCATION | AssignmentInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentInternalOfficeNumber | — |
| JOB_ID | AssignmentJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentLegalEntityId | — |
| LEGISLATION_CODE | AssignmentLegislationCode | — |
| LINKAGE_TYPE | AssignmentLinkageType | — |
| LOCATION_ID | AssignmentLocationId | — |
| MANAGER_FLAG | AssignmentManagerFlag | — |
| NORMAL_HOURS | AssignmentNormalHours | — |
| NOTICE_PERIOD | AssignmentNoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentNoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPersonTypeId | — |
| PO_HEADER_ID | AssignmentPoHeaderId | — |
| PO_LINE_ID | AssignmentPoLineId | — |
| POSITION_ID | AssignmentPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentProbationPeriod | — |
| PROBATION_UNIT | AssignmentProbationUnit | — |
| PROJECT_TITLE | AssignmentProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentProposedWorkerType | — |
| REASON_CODE | AssignmentReasonCode | — |
| RECORD_CREATOR | AssignmentRecordCreator | — |
| RECRUITER_ID | AssignmentRecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentRecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentRetirementAge | — |
| RETIREMENT_DATE | AssignmentRetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentTimeNormalStart | — |
| VACANCY_ID | AssignmentVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentVendorId | — |
| VENDOR_SITE_ID | AssignmentVendorSiteId | — |
| WORK_AT_HOME | AssignmentWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentWorkTermsAssignmentId | — |

### [[qualityrelationships|QualityRelationships]] (OTHER · BICC: 2/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASG_INFORMATION1 | AssignmentPEOAsgInformation1 | — |
| ASG_INFORMATION10 | AssignmentPEOAsgInformation10 | — |
| ASG_INFORMATION11 | AssignmentPEOAsgInformation11 | — |
| ASG_INFORMATION12 | AssignmentPEOAsgInformation12 | — |
| ASG_INFORMATION13 | AssignmentPEOAsgInformation13 | — |
| ASG_INFORMATION14 | AssignmentPEOAsgInformation14 | — |
| ASG_INFORMATION15 | AssignmentPEOAsgInformation15 | — |
| ASG_INFORMATION16 | AssignmentPEOAsgInformation16 | — |
| ASG_INFORMATION17 | AssignmentPEOAsgInformation17 | — |
| ASG_INFORMATION18 | AssignmentPEOAsgInformation18 | — |
| ASG_INFORMATION19 | AssignmentPEOAsgInformation19 | — |
| ASG_INFORMATION2 | AssignmentPEOAsgInformation2 | — |
| ASG_INFORMATION20 | AssignmentPEOAsgInformation20 | — |
| ASG_INFORMATION21 | AssignmentPEOAsgInformation21 | — |
| ASG_INFORMATION22 | AssignmentPEOAsgInformation22 | — |
| ASG_INFORMATION23 | AssignmentPEOAsgInformation23 | — |
| ASG_INFORMATION24 | AssignmentPEOAsgInformation24 | — |
| ASG_INFORMATION25 | AssignmentPEOAsgInformation25 | — |
| ASG_INFORMATION26 | AssignmentPEOAsgInformation26 | — |
| ASG_INFORMATION27 | AssignmentPEOAsgInformation27 | — |
| ASG_INFORMATION28 | AssignmentPEOAsgInformation28 | — |
| ASG_INFORMATION29 | AssignmentPEOAsgInformation29 | — |
| ASG_INFORMATION3 | AssignmentPEOAsgInformation3 | — |
| ASG_INFORMATION30 | AssignmentPEOAsgInformation30 | — |
| ASG_INFORMATION31 | AssignmentPEOAsgInformation31 | — |
| ASG_INFORMATION32 | AssignmentPEOAsgInformation32 | — |
| ASG_INFORMATION33 | AssignmentPEOAsgInformation33 | — |
| ASG_INFORMATION34 | AssignmentPEOAsgInformation34 | — |
| ASG_INFORMATION35 | AssignmentPEOAsgInformation35 | — |
| ASG_INFORMATION36 | AssignmentPEOAsgInformation36 | — |
| ASG_INFORMATION37 | AssignmentPEOAsgInformation37 | — |
| ASG_INFORMATION38 | AssignmentPEOAsgInformation38 | — |
| ASG_INFORMATION39 | AssignmentPEOAsgInformation39 | — |
| ASG_INFORMATION4 | AssignmentPEOAsgInformation4 | — |
| ASG_INFORMATION40 | AssignmentPEOAsgInformation40 | — |
| ASG_INFORMATION41 | AssignmentPEOAsgInformation41 | — |
| ASG_INFORMATION42 | AssignmentPEOAsgInformation42 | — |
| ASG_INFORMATION43 | AssignmentPEOAsgInformation43 | — |
| ASG_INFORMATION44 | AssignmentPEOAsgInformation44 | — |
| ASG_INFORMATION45 | AssignmentPEOAsgInformation45 | — |
| ASG_INFORMATION46 | AssignmentPEOAsgInformation46 | — |
| ASG_INFORMATION47 | AssignmentPEOAsgInformation47 | — |
| ASG_INFORMATION48 | AssignmentPEOAsgInformation48 | — |
| ASG_INFORMATION49 | AssignmentPEOAsgInformation49 | — |
| ASG_INFORMATION5 | AssignmentPEOAsgInformation5 | — |
| ASG_INFORMATION50 | AssignmentPEOAsgInformation50 | — |
| ASG_INFORMATION6 | AssignmentPEOAsgInformation6 | — |
| ASG_INFORMATION7 | AssignmentPEOAsgInformation7 | — |
| ASG_INFORMATION8 | AssignmentPEOAsgInformation8 | — |
| ASG_INFORMATION9 | AssignmentPEOAsgInformation9 | — |
| ASG_INFORMATION_CATEGORY | AssignmentPEOAsgInformationCategory | — |
| ASG_INFORMATION_DATE1 | AssignmentPEOAsgInformationDate1 | — |
| ASG_INFORMATION_DATE10 | AssignmentPEOAsgInformationDate10 | — |
| ASG_INFORMATION_DATE11 | AssignmentPEOAsgInformationDate11 | — |
| ASG_INFORMATION_DATE12 | AssignmentPEOAsgInformationDate12 | — |
| ASG_INFORMATION_DATE13 | AssignmentPEOAsgInformationDate13 | — |
| ASG_INFORMATION_DATE14 | AssignmentPEOAsgInformationDate14 | — |
| ASG_INFORMATION_DATE15 | AssignmentPEOAsgInformationDate15 | — |
| ASG_INFORMATION_DATE2 | AssignmentPEOAsgInformationDate2 | — |
| ASG_INFORMATION_DATE3 | AssignmentPEOAsgInformationDate3 | — |
| ASG_INFORMATION_DATE4 | AssignmentPEOAsgInformationDate4 | — |
| ASG_INFORMATION_DATE5 | AssignmentPEOAsgInformationDate5 | — |
| ASG_INFORMATION_DATE6 | AssignmentPEOAsgInformationDate6 | — |
| ASG_INFORMATION_DATE7 | AssignmentPEOAsgInformationDate7 | — |
| ASG_INFORMATION_DATE8 | AssignmentPEOAsgInformationDate8 | — |
| ASG_INFORMATION_DATE9 | AssignmentPEOAsgInformationDate9 | — |
| ASG_INFORMATION_NUMBER1 | AssignmentPEOAsgInformationNumber1 | — |
| ASG_INFORMATION_NUMBER10 | AssignmentPEOAsgInformationNumber10 | — |
| ASG_INFORMATION_NUMBER11 | AssignmentPEOAsgInformationNumber11 | — |
| ASG_INFORMATION_NUMBER12 | AssignmentPEOAsgInformationNumber12 | — |
| ASG_INFORMATION_NUMBER13 | AssignmentPEOAsgInformationNumber13 | — |
| ASG_INFORMATION_NUMBER14 | AssignmentPEOAsgInformationNumber14 | — |
| ASG_INFORMATION_NUMBER15 | AssignmentPEOAsgInformationNumber15 | — |
| ASG_INFORMATION_NUMBER16 | AssignmentPEOAsgInformationNumber16 | — |
| ASG_INFORMATION_NUMBER17 | AssignmentPEOAsgInformationNumber17 | — |
| ASG_INFORMATION_NUMBER18 | AssignmentPEOAsgInformationNumber18 | — |
| ASG_INFORMATION_NUMBER19 | AssignmentPEOAsgInformationNumber19 | — |
| ASG_INFORMATION_NUMBER2 | AssignmentPEOAsgInformationNumber2 | — |
| ASG_INFORMATION_NUMBER20 | AssignmentPEOAsgInformationNumber20 | — |
| ASG_INFORMATION_NUMBER3 | AssignmentPEOAsgInformationNumber3 | — |
| ASG_INFORMATION_NUMBER4 | AssignmentPEOAsgInformationNumber4 | — |
| ASG_INFORMATION_NUMBER5 | AssignmentPEOAsgInformationNumber5 | — |
| ASG_INFORMATION_NUMBER6 | AssignmentPEOAsgInformationNumber6 | — |
| ASG_INFORMATION_NUMBER7 | AssignmentPEOAsgInformationNumber7 | — |
| ASG_INFORMATION_NUMBER8 | AssignmentPEOAsgInformationNumber8 | — |
| ASG_INFORMATION_NUMBER9 | AssignmentPEOAsgInformationNumber9 | — |
| ASS_ATTRIBUTE1 | AssignmentPEOAssAttribute1 | — |
| ASS_ATTRIBUTE10 | AssignmentPEOAssAttribute10 | — |
| ASS_ATTRIBUTE11 | AssignmentPEOAssAttribute11 | — |
| ASS_ATTRIBUTE12 | AssignmentPEOAssAttribute12 | — |
| ASS_ATTRIBUTE13 | AssignmentPEOAssAttribute13 | — |
| ASS_ATTRIBUTE14 | AssignmentPEOAssAttribute14 | — |
| ASS_ATTRIBUTE15 | AssignmentPEOAssAttribute15 | — |
| ASS_ATTRIBUTE16 | AssignmentPEOAssAttribute16 | — |
| ASS_ATTRIBUTE17 | AssignmentPEOAssAttribute17 | — |
| ASS_ATTRIBUTE18 | AssignmentPEOAssAttribute18 | — |
| ASS_ATTRIBUTE19 | AssignmentPEOAssAttribute19 | — |
| ASS_ATTRIBUTE2 | AssignmentPEOAssAttribute2 | — |
| ASS_ATTRIBUTE20 | AssignmentPEOAssAttribute20 | — |
| ASS_ATTRIBUTE21 | AssignmentPEOAssAttribute21 | — |
| ASS_ATTRIBUTE22 | AssignmentPEOAssAttribute22 | — |
| ASS_ATTRIBUTE23 | AssignmentPEOAssAttribute23 | — |
| ASS_ATTRIBUTE24 | AssignmentPEOAssAttribute24 | — |
| ASS_ATTRIBUTE25 | AssignmentPEOAssAttribute25 | — |
| ASS_ATTRIBUTE26 | AssignmentPEOAssAttribute26 | — |
| ASS_ATTRIBUTE27 | AssignmentPEOAssAttribute27 | — |
| ASS_ATTRIBUTE28 | AssignmentPEOAssAttribute28 | — |
| ASS_ATTRIBUTE29 | AssignmentPEOAssAttribute29 | — |
| ASS_ATTRIBUTE3 | AssignmentPEOAssAttribute3 | — |
| ASS_ATTRIBUTE30 | AssignmentPEOAssAttribute30 | — |
| ASS_ATTRIBUTE31 | AssignmentPEOAssAttribute31 | — |
| ASS_ATTRIBUTE32 | AssignmentPEOAssAttribute32 | — |
| ASS_ATTRIBUTE33 | AssignmentPEOAssAttribute33 | — |
| ASS_ATTRIBUTE34 | AssignmentPEOAssAttribute34 | — |
| ASS_ATTRIBUTE35 | AssignmentPEOAssAttribute35 | — |
| ASS_ATTRIBUTE36 | AssignmentPEOAssAttribute36 | — |
| ASS_ATTRIBUTE37 | AssignmentPEOAssAttribute37 | — |
| ASS_ATTRIBUTE38 | AssignmentPEOAssAttribute38 | — |
| ASS_ATTRIBUTE39 | AssignmentPEOAssAttribute39 | — |
| ASS_ATTRIBUTE4 | AssignmentPEOAssAttribute4 | — |
| ASS_ATTRIBUTE40 | AssignmentPEOAssAttribute40 | — |
| ASS_ATTRIBUTE41 | AssignmentPEOAssAttribute41 | — |
| ASS_ATTRIBUTE42 | AssignmentPEOAssAttribute42 | — |
| ASS_ATTRIBUTE43 | AssignmentPEOAssAttribute43 | — |
| ASS_ATTRIBUTE44 | AssignmentPEOAssAttribute44 | — |
| ASS_ATTRIBUTE45 | AssignmentPEOAssAttribute45 | — |
| ASS_ATTRIBUTE46 | AssignmentPEOAssAttribute46 | — |
| ASS_ATTRIBUTE47 | AssignmentPEOAssAttribute47 | — |
| ASS_ATTRIBUTE48 | AssignmentPEOAssAttribute48 | — |
| ASS_ATTRIBUTE49 | AssignmentPEOAssAttribute49 | — |
| ASS_ATTRIBUTE5 | AssignmentPEOAssAttribute5 | — |
| ASS_ATTRIBUTE50 | AssignmentPEOAssAttribute50 | — |
| ASS_ATTRIBUTE6 | AssignmentPEOAssAttribute6 | — |
| ASS_ATTRIBUTE7 | AssignmentPEOAssAttribute7 | — |
| ASS_ATTRIBUTE8 | AssignmentPEOAssAttribute8 | — |
| ASS_ATTRIBUTE9 | AssignmentPEOAssAttribute9 | — |
| ASS_ATTRIBUTE_CATEGORY | AssignmentPEOAssAttributeCategory | — |
| ASS_ATTRIBUTE_DATE1 | AssignmentPEOAssAttributeDate1 | — |
| ASS_ATTRIBUTE_DATE10 | AssignmentPEOAssAttributeDate10 | — |
| ASS_ATTRIBUTE_DATE11 | AssignmentPEOAssAttributeDate11 | — |
| ASS_ATTRIBUTE_DATE12 | AssignmentPEOAssAttributeDate12 | — |
| ASS_ATTRIBUTE_DATE13 | AssignmentPEOAssAttributeDate13 | — |
| ASS_ATTRIBUTE_DATE14 | AssignmentPEOAssAttributeDate14 | — |
| ASS_ATTRIBUTE_DATE15 | AssignmentPEOAssAttributeDate15 | — |
| ASS_ATTRIBUTE_DATE2 | AssignmentPEOAssAttributeDate2 | — |
| ASS_ATTRIBUTE_DATE3 | AssignmentPEOAssAttributeDate3 | — |
| ASS_ATTRIBUTE_DATE4 | AssignmentPEOAssAttributeDate4 | — |
| ASS_ATTRIBUTE_DATE5 | AssignmentPEOAssAttributeDate5 | — |
| ASS_ATTRIBUTE_DATE6 | AssignmentPEOAssAttributeDate6 | — |
| ASS_ATTRIBUTE_DATE7 | AssignmentPEOAssAttributeDate7 | — |
| ASS_ATTRIBUTE_DATE8 | AssignmentPEOAssAttributeDate8 | — |
| ASS_ATTRIBUTE_DATE9 | AssignmentPEOAssAttributeDate9 | — |
| ASS_ATTRIBUTE_NUMBER1 | AssignmentPEOAssAttributeNumber1 | — |
| ASS_ATTRIBUTE_NUMBER10 | AssignmentPEOAssAttributeNumber10 | — |
| ASS_ATTRIBUTE_NUMBER11 | AssignmentPEOAssAttributeNumber11 | — |
| ASS_ATTRIBUTE_NUMBER12 | AssignmentPEOAssAttributeNumber12 | — |
| ASS_ATTRIBUTE_NUMBER13 | AssignmentPEOAssAttributeNumber13 | — |
| ASS_ATTRIBUTE_NUMBER14 | AssignmentPEOAssAttributeNumber14 | — |
| ASS_ATTRIBUTE_NUMBER15 | AssignmentPEOAssAttributeNumber15 | — |
| ASS_ATTRIBUTE_NUMBER16 | AssignmentPEOAssAttributeNumber16 | — |
| ASS_ATTRIBUTE_NUMBER17 | AssignmentPEOAssAttributeNumber17 | — |
| ASS_ATTRIBUTE_NUMBER18 | AssignmentPEOAssAttributeNumber18 | — |
| ASS_ATTRIBUTE_NUMBER19 | AssignmentPEOAssAttributeNumber19 | — |
| ASS_ATTRIBUTE_NUMBER2 | AssignmentPEOAssAttributeNumber2 | — |
| ASS_ATTRIBUTE_NUMBER20 | AssignmentPEOAssAttributeNumber20 | — |
| ASS_ATTRIBUTE_NUMBER3 | AssignmentPEOAssAttributeNumber3 | — |
| ASS_ATTRIBUTE_NUMBER4 | AssignmentPEOAssAttributeNumber4 | — |
| ASS_ATTRIBUTE_NUMBER5 | AssignmentPEOAssAttributeNumber5 | — |
| ASS_ATTRIBUTE_NUMBER6 | AssignmentPEOAssAttributeNumber6 | — |
| ASS_ATTRIBUTE_NUMBER7 | AssignmentPEOAssAttributeNumber7 | — |
| ASS_ATTRIBUTE_NUMBER8 | AssignmentPEOAssAttributeNumber8 | — |
| ASS_ATTRIBUTE_NUMBER9 | AssignmentPEOAssAttributeNumber9 | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId2 | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId1 | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId1 | — |
| CREATED_BY | AssignmentPEOCreatedBy15 | — |
| CREATION_DATE | AssignmentPEOCreationDate15 | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate2 | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate2 | — |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId3 | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate15 | — |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin15 | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy15 | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId2 | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode1 | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId1 | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber12 | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId2 | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId2 | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId8 | — |
| PO_LINE_ID | AssignmentPEOPoLineId6 | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId4 | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId5 | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId5 | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 2/281)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASG_INFORMATION1 | AssignmentPEOAsgInformation1 | — |
| ASG_INFORMATION10 | AssignmentPEOAsgInformation10 | — |
| ASG_INFORMATION11 | AssignmentPEOAsgInformation11 | — |
| ASG_INFORMATION12 | AssignmentPEOAsgInformation12 | — |
| ASG_INFORMATION13 | AssignmentPEOAsgInformation13 | — |
| ASG_INFORMATION14 | AssignmentPEOAsgInformation14 | — |
| ASG_INFORMATION15 | AssignmentPEOAsgInformation15 | — |
| ASG_INFORMATION16 | AssignmentPEOAsgInformation16 | — |
| ASG_INFORMATION17 | AssignmentPEOAsgInformation17 | — |
| ASG_INFORMATION18 | AssignmentPEOAsgInformation18 | — |
| ASG_INFORMATION19 | AssignmentPEOAsgInformation19 | — |
| ASG_INFORMATION2 | AssignmentPEOAsgInformation2 | — |
| ASG_INFORMATION20 | AssignmentPEOAsgInformation20 | — |
| ASG_INFORMATION21 | AssignmentPEOAsgInformation21 | — |
| ASG_INFORMATION22 | AssignmentPEOAsgInformation22 | — |
| ASG_INFORMATION23 | AssignmentPEOAsgInformation23 | — |
| ASG_INFORMATION24 | AssignmentPEOAsgInformation24 | — |
| ASG_INFORMATION25 | AssignmentPEOAsgInformation25 | — |
| ASG_INFORMATION26 | AssignmentPEOAsgInformation26 | — |
| ASG_INFORMATION27 | AssignmentPEOAsgInformation27 | — |
| ASG_INFORMATION28 | AssignmentPEOAsgInformation28 | — |
| ASG_INFORMATION29 | AssignmentPEOAsgInformation29 | — |
| ASG_INFORMATION3 | AssignmentPEOAsgInformation3 | — |
| ASG_INFORMATION30 | AssignmentPEOAsgInformation30 | — |
| ASG_INFORMATION31 | AssignmentPEOAsgInformation31 | — |
| ASG_INFORMATION32 | AssignmentPEOAsgInformation32 | — |
| ASG_INFORMATION33 | AssignmentPEOAsgInformation33 | — |
| ASG_INFORMATION34 | AssignmentPEOAsgInformation34 | — |
| ASG_INFORMATION35 | AssignmentPEOAsgInformation35 | — |
| ASG_INFORMATION36 | AssignmentPEOAsgInformation36 | — |
| ASG_INFORMATION37 | AssignmentPEOAsgInformation37 | — |
| ASG_INFORMATION38 | AssignmentPEOAsgInformation38 | — |
| ASG_INFORMATION39 | AssignmentPEOAsgInformation39 | — |
| ASG_INFORMATION4 | AssignmentPEOAsgInformation4 | — |
| ASG_INFORMATION40 | AssignmentPEOAsgInformation40 | — |
| ASG_INFORMATION41 | AssignmentPEOAsgInformation41 | — |
| ASG_INFORMATION42 | AssignmentPEOAsgInformation42 | — |
| ASG_INFORMATION43 | AssignmentPEOAsgInformation43 | — |
| ASG_INFORMATION44 | AssignmentPEOAsgInformation44 | — |
| ASG_INFORMATION45 | AssignmentPEOAsgInformation45 | — |
| ASG_INFORMATION46 | AssignmentPEOAsgInformation46 | — |
| ASG_INFORMATION47 | AssignmentPEOAsgInformation47 | — |
| ASG_INFORMATION48 | AssignmentPEOAsgInformation48 | — |
| ASG_INFORMATION49 | AssignmentPEOAsgInformation49 | — |
| ASG_INFORMATION5 | AssignmentPEOAsgInformation5 | — |
| ASG_INFORMATION50 | AssignmentPEOAsgInformation50 | — |
| ASG_INFORMATION6 | AssignmentPEOAsgInformation6 | — |
| ASG_INFORMATION7 | AssignmentPEOAsgInformation7 | — |
| ASG_INFORMATION8 | AssignmentPEOAsgInformation8 | — |
| ASG_INFORMATION9 | AssignmentPEOAsgInformation9 | — |
| ASG_INFORMATION_CATEGORY | AssignmentPEOAsgInformationCategory | — |
| ASG_INFORMATION_DATE1 | AssignmentPEOAsgInformationDate1 | — |
| ASG_INFORMATION_DATE10 | AssignmentPEOAsgInformationDate10 | — |
| ASG_INFORMATION_DATE11 | AssignmentPEOAsgInformationDate11 | — |
| ASG_INFORMATION_DATE12 | AssignmentPEOAsgInformationDate12 | — |
| ASG_INFORMATION_DATE13 | AssignmentPEOAsgInformationDate13 | — |
| ASG_INFORMATION_DATE14 | AssignmentPEOAsgInformationDate14 | — |
| ASG_INFORMATION_DATE15 | AssignmentPEOAsgInformationDate15 | — |
| ASG_INFORMATION_DATE2 | AssignmentPEOAsgInformationDate2 | — |
| ASG_INFORMATION_DATE3 | AssignmentPEOAsgInformationDate3 | — |
| ASG_INFORMATION_DATE4 | AssignmentPEOAsgInformationDate4 | — |
| ASG_INFORMATION_DATE5 | AssignmentPEOAsgInformationDate5 | — |
| ASG_INFORMATION_DATE6 | AssignmentPEOAsgInformationDate6 | — |
| ASG_INFORMATION_DATE7 | AssignmentPEOAsgInformationDate7 | — |
| ASG_INFORMATION_DATE8 | AssignmentPEOAsgInformationDate8 | — |
| ASG_INFORMATION_DATE9 | AssignmentPEOAsgInformationDate9 | — |
| ASG_INFORMATION_NUMBER1 | AssignmentPEOAsgInformationNumber1 | — |
| ASG_INFORMATION_NUMBER10 | AssignmentPEOAsgInformationNumber10 | — |
| ASG_INFORMATION_NUMBER11 | AssignmentPEOAsgInformationNumber11 | — |
| ASG_INFORMATION_NUMBER12 | AssignmentPEOAsgInformationNumber12 | — |
| ASG_INFORMATION_NUMBER13 | AssignmentPEOAsgInformationNumber13 | — |
| ASG_INFORMATION_NUMBER14 | AssignmentPEOAsgInformationNumber14 | — |
| ASG_INFORMATION_NUMBER15 | AssignmentPEOAsgInformationNumber15 | — |
| ASG_INFORMATION_NUMBER16 | AssignmentPEOAsgInformationNumber16 | — |
| ASG_INFORMATION_NUMBER17 | AssignmentPEOAsgInformationNumber17 | — |
| ASG_INFORMATION_NUMBER18 | AssignmentPEOAsgInformationNumber18 | — |
| ASG_INFORMATION_NUMBER19 | AssignmentPEOAsgInformationNumber19 | — |
| ASG_INFORMATION_NUMBER2 | AssignmentPEOAsgInformationNumber2 | — |
| ASG_INFORMATION_NUMBER20 | AssignmentPEOAsgInformationNumber20 | — |
| ASG_INFORMATION_NUMBER3 | AssignmentPEOAsgInformationNumber3 | — |
| ASG_INFORMATION_NUMBER4 | AssignmentPEOAsgInformationNumber4 | — |
| ASG_INFORMATION_NUMBER5 | AssignmentPEOAsgInformationNumber5 | — |
| ASG_INFORMATION_NUMBER6 | AssignmentPEOAsgInformationNumber6 | — |
| ASG_INFORMATION_NUMBER7 | AssignmentPEOAsgInformationNumber7 | — |
| ASG_INFORMATION_NUMBER8 | AssignmentPEOAsgInformationNumber8 | — |
| ASG_INFORMATION_NUMBER9 | AssignmentPEOAsgInformationNumber9 | — |
| ASS_ATTRIBUTE1 | AssignmentPEOAssAttribute1 | — |
| ASS_ATTRIBUTE10 | AssignmentPEOAssAttribute10 | — |
| ASS_ATTRIBUTE11 | AssignmentPEOAssAttribute11 | — |
| ASS_ATTRIBUTE12 | AssignmentPEOAssAttribute12 | — |
| ASS_ATTRIBUTE13 | AssignmentPEOAssAttribute13 | — |
| ASS_ATTRIBUTE14 | AssignmentPEOAssAttribute14 | — |
| ASS_ATTRIBUTE15 | AssignmentPEOAssAttribute15 | — |
| ASS_ATTRIBUTE16 | AssignmentPEOAssAttribute16 | — |
| ASS_ATTRIBUTE17 | AssignmentPEOAssAttribute17 | — |
| ASS_ATTRIBUTE18 | AssignmentPEOAssAttribute18 | — |
| ASS_ATTRIBUTE19 | AssignmentPEOAssAttribute19 | — |
| ASS_ATTRIBUTE2 | AssignmentPEOAssAttribute2 | — |
| ASS_ATTRIBUTE20 | AssignmentPEOAssAttribute20 | — |
| ASS_ATTRIBUTE21 | AssignmentPEOAssAttribute21 | — |
| ASS_ATTRIBUTE22 | AssignmentPEOAssAttribute22 | — |
| ASS_ATTRIBUTE23 | AssignmentPEOAssAttribute23 | — |
| ASS_ATTRIBUTE24 | AssignmentPEOAssAttribute24 | — |
| ASS_ATTRIBUTE25 | AssignmentPEOAssAttribute25 | — |
| ASS_ATTRIBUTE26 | AssignmentPEOAssAttribute26 | — |
| ASS_ATTRIBUTE27 | AssignmentPEOAssAttribute27 | — |
| ASS_ATTRIBUTE28 | AssignmentPEOAssAttribute28 | — |
| ASS_ATTRIBUTE29 | AssignmentPEOAssAttribute29 | — |
| ASS_ATTRIBUTE3 | AssignmentPEOAssAttribute3 | — |
| ASS_ATTRIBUTE30 | AssignmentPEOAssAttribute30 | — |
| ASS_ATTRIBUTE31 | AssignmentPEOAssAttribute31 | — |
| ASS_ATTRIBUTE32 | AssignmentPEOAssAttribute32 | — |
| ASS_ATTRIBUTE33 | AssignmentPEOAssAttribute33 | — |
| ASS_ATTRIBUTE34 | AssignmentPEOAssAttribute34 | — |
| ASS_ATTRIBUTE35 | AssignmentPEOAssAttribute35 | — |
| ASS_ATTRIBUTE36 | AssignmentPEOAssAttribute36 | — |
| ASS_ATTRIBUTE37 | AssignmentPEOAssAttribute37 | — |
| ASS_ATTRIBUTE38 | AssignmentPEOAssAttribute38 | — |
| ASS_ATTRIBUTE39 | AssignmentPEOAssAttribute39 | — |
| ASS_ATTRIBUTE4 | AssignmentPEOAssAttribute4 | — |
| ASS_ATTRIBUTE40 | AssignmentPEOAssAttribute40 | — |
| ASS_ATTRIBUTE41 | AssignmentPEOAssAttribute41 | — |
| ASS_ATTRIBUTE42 | AssignmentPEOAssAttribute42 | — |
| ASS_ATTRIBUTE43 | AssignmentPEOAssAttribute43 | — |
| ASS_ATTRIBUTE44 | AssignmentPEOAssAttribute44 | — |
| ASS_ATTRIBUTE45 | AssignmentPEOAssAttribute45 | — |
| ASS_ATTRIBUTE46 | AssignmentPEOAssAttribute46 | — |
| ASS_ATTRIBUTE47 | AssignmentPEOAssAttribute47 | — |
| ASS_ATTRIBUTE48 | AssignmentPEOAssAttribute48 | — |
| ASS_ATTRIBUTE49 | AssignmentPEOAssAttribute49 | — |
| ASS_ATTRIBUTE5 | AssignmentPEOAssAttribute5 | — |
| ASS_ATTRIBUTE50 | AssignmentPEOAssAttribute50 | — |
| ASS_ATTRIBUTE6 | AssignmentPEOAssAttribute6 | — |
| ASS_ATTRIBUTE7 | AssignmentPEOAssAttribute7 | — |
| ASS_ATTRIBUTE8 | AssignmentPEOAssAttribute8 | — |
| ASS_ATTRIBUTE9 | AssignmentPEOAssAttribute9 | — |
| ASS_ATTRIBUTE_CATEGORY | AssignmentPEOAssAttributeCategory | — |
| ASS_ATTRIBUTE_DATE1 | AssignmentPEOAssAttributeDate1 | — |
| ASS_ATTRIBUTE_DATE10 | AssignmentPEOAssAttributeDate10 | — |
| ASS_ATTRIBUTE_DATE11 | AssignmentPEOAssAttributeDate11 | — |
| ASS_ATTRIBUTE_DATE12 | AssignmentPEOAssAttributeDate12 | — |
| ASS_ATTRIBUTE_DATE13 | AssignmentPEOAssAttributeDate13 | — |
| ASS_ATTRIBUTE_DATE14 | AssignmentPEOAssAttributeDate14 | — |
| ASS_ATTRIBUTE_DATE15 | AssignmentPEOAssAttributeDate15 | — |
| ASS_ATTRIBUTE_DATE2 | AssignmentPEOAssAttributeDate2 | — |
| ASS_ATTRIBUTE_DATE3 | AssignmentPEOAssAttributeDate3 | — |
| ASS_ATTRIBUTE_DATE4 | AssignmentPEOAssAttributeDate4 | — |
| ASS_ATTRIBUTE_DATE5 | AssignmentPEOAssAttributeDate5 | — |
| ASS_ATTRIBUTE_DATE6 | AssignmentPEOAssAttributeDate6 | — |
| ASS_ATTRIBUTE_DATE7 | AssignmentPEOAssAttributeDate7 | — |
| ASS_ATTRIBUTE_DATE8 | AssignmentPEOAssAttributeDate8 | — |
| ASS_ATTRIBUTE_DATE9 | AssignmentPEOAssAttributeDate9 | — |
| ASS_ATTRIBUTE_NUMBER1 | AssignmentPEOAssAttributeNumber1 | — |
| ASS_ATTRIBUTE_NUMBER10 | AssignmentPEOAssAttributeNumber10 | — |
| ASS_ATTRIBUTE_NUMBER11 | AssignmentPEOAssAttributeNumber11 | — |
| ASS_ATTRIBUTE_NUMBER12 | AssignmentPEOAssAttributeNumber12 | — |
| ASS_ATTRIBUTE_NUMBER13 | AssignmentPEOAssAttributeNumber13 | — |
| ASS_ATTRIBUTE_NUMBER14 | AssignmentPEOAssAttributeNumber14 | — |
| ASS_ATTRIBUTE_NUMBER15 | AssignmentPEOAssAttributeNumber15 | — |
| ASS_ATTRIBUTE_NUMBER16 | AssignmentPEOAssAttributeNumber16 | — |
| ASS_ATTRIBUTE_NUMBER17 | AssignmentPEOAssAttributeNumber17 | — |
| ASS_ATTRIBUTE_NUMBER18 | AssignmentPEOAssAttributeNumber18 | — |
| ASS_ATTRIBUTE_NUMBER19 | AssignmentPEOAssAttributeNumber19 | — |
| ASS_ATTRIBUTE_NUMBER2 | AssignmentPEOAssAttributeNumber2 | — |
| ASS_ATTRIBUTE_NUMBER20 | AssignmentPEOAssAttributeNumber20 | — |
| ASS_ATTRIBUTE_NUMBER3 | AssignmentPEOAssAttributeNumber3 | — |
| ASS_ATTRIBUTE_NUMBER4 | AssignmentPEOAssAttributeNumber4 | — |
| ASS_ATTRIBUTE_NUMBER5 | AssignmentPEOAssAttributeNumber5 | — |
| ASS_ATTRIBUTE_NUMBER6 | AssignmentPEOAssAttributeNumber6 | — |
| ASS_ATTRIBUTE_NUMBER7 | AssignmentPEOAssAttributeNumber7 | — |
| ASS_ATTRIBUTE_NUMBER8 | AssignmentPEOAssAttributeNumber8 | — |
| ASS_ATTRIBUTE_NUMBER9 | AssignmentPEOAssAttributeNumber9 | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId2 | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId1 | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId1 | — |
| CREATED_BY | AssignmentPEOCreatedBy15 | — |
| CREATION_DATE | AssignmentPEOCreationDate15 | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate2 | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate2 | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId3 | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate15 | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin15 | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy15 | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId2 | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode1 | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId1 | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber12 | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId2 | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId2 | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId8 | — |
| PO_LINE_ID | AssignmentPEOPoLineId6 | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId4 | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId5 | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId5 | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[requisitionpvo|RequisitionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | — |

### [[resourcequalificationpvo|ResourceQualificationPVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentDPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentDPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentDPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentDPEOEffectiveStartDate | ✅ |

### [[salaryhistorypvo|SalaryHistoryPVO]] (HCM · BICC: 5/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentId1 | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | EffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | EffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| JOB_ID | JobId | — |
| LOCATION_ID | LocationId | — |
| PERSON_ID | PersonId | — |

### [[salarypvo|SalaryPVO]] (HCM · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | ✅ |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | ✅ |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | ✅ |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| JOB_ID | AssignmentPEOJobId | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| PERSON_ID | AssignmentPEOPersonId | — |

### [[scheduleassignmentpvo|ScheduleAssignmentPVO]] (GL · BICC: 2/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_CODE | AssignmentPEOActionCode | — |
| ACTION_OCCURRENCE_ID | AssignmentPEOActionOccurrenceId | — |
| ALLOW_ASG_OVERRIDE_FLAG | AssignmentPEOAllowAsgOverrideFlag | — |
| APPLICANT_RANK | AssignmentPEOApplicantRank | — |
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| ASSIGNMENT_NAME | AssignmentPEOAssignmentName | — |
| ASSIGNMENT_NUMBER | AssignmentPEOAssignmentNumber | — |
| ASSIGNMENT_SEQUENCE | AssignmentPEOAssignmentSequence | — |
| ASSIGNMENT_STATUS_TYPE | AssignmentPEOAssignmentStatusType | — |
| ASSIGNMENT_STATUS_TYPE_ID | AssignmentPEOAssignmentStatusTypeId | — |
| ASSIGNMENT_TYPE | AssignmentPEOAssignmentType | — |
| AUTO_END_FLAG | AssignmentPEOAutoEndFlag | — |
| BARGAINING_UNIT_CODE | AssignmentPEOBargainingUnitCode | — |
| BILLING_TITLE | AssignmentPEOBillingTitle | — |
| BUSINESS_GROUP_ID | AssignmentPEOBusinessGroupId | — |
| BUSINESS_UNIT_ID | AssignmentPEOBusinessUnitId | — |
| CAGR_GRADE_DEF_ID | AssignmentPEOCagrGradeDefId | — |
| CAGR_ID_FLEX_NUM | AssignmentPEOCagrIdFlexNum | — |
| COLLECTIVE_AGREEMENT_ID | AssignmentPEOCollectiveAgreementId | — |
| CONTRACT_ID | AssignmentPEOContractId | — |
| CREATED_BY | AssignmentPEOCreatedBy | — |
| CREATION_DATE | AssignmentPEOCreationDate | — |
| DATE_PROBATION_END | AssignmentPEODateProbationEnd | — |
| DEFAULT_CODE_COMB_ID | AssignmentPEODefaultCodeCombId | — |
| DUTIES_TYPE | AssignmentPEODutiesType | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| EMPLOYEE_CATEGORY | AssignmentPEOEmployeeCategory | — |
| EMPLOYMENT_CATEGORY | AssignmentPEOEmploymentCategory | — |
| ESTABLISHMENT_ID | AssignmentPEOEstablishmentId | — |
| EXPENSE_CHECK_ADDRESS | AssignmentPEOExpenseCheckAddress | — |
| FREEZE_START_DATE | AssignmentPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentPEOFreezeUntilDate | — |
| FREQUENCY | AssignmentPEOFrequency | — |
| FULL_PART_TIME | AssignmentPEOFullPartTime | — |
| GRADE_ID | AssignmentPEOGradeId | — |
| GRADE_LADDER_PGM_ID | AssignmentPEOGradeLadderPgmId | — |
| HOURLY_SALARIED_CODE | AssignmentPEOHourlySalariedCode | — |
| ID_FLEX_NUM | AssignmentPEOIdFlexNum | — |
| INTERNAL_BUILDING | AssignmentPEOInternalBuilding | — |
| INTERNAL_FLOOR | AssignmentPEOInternalFloor | — |
| INTERNAL_LOCATION | AssignmentPEOInternalLocation | — |
| INTERNAL_MAILSTOP | AssignmentPEOInternalMailstop | — |
| INTERNAL_OFFICE_NUMBER | AssignmentPEOInternalOfficeNumber | — |
| JOB_ID | AssignmentPEOJobId | — |
| JOB_POST_SOURCE_NAME | AssignmentPEOJobPostSourceName | — |
| LABOUR_UNION_MEMBER_FLAG | AssignmentPEOLabourUnionMemberFlag | — |
| LAST_UPDATE_DATE | AssignmentPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AssignmentPEOLegalEntityId | — |
| LEGISLATION_CODE | AssignmentPEOLegislationCode | — |
| LINKAGE_TYPE | AssignmentPEOLinkageType | — |
| LOCATION_ID | AssignmentPEOLocationId | — |
| MANAGER_FLAG | AssignmentPEOManagerFlag | — |
| NORMAL_HOURS | AssignmentPEONormalHours | — |
| NOTICE_PERIOD | AssignmentPEONoticePeriod | — |
| NOTICE_PERIOD_UOM | AssignmentPEONoticePeriodUom | — |
| OBJECT_VERSION_NUMBER | AssignmentPEOObjectVersionNumber | — |
| ORGANIZATION_ID | AssignmentPEOOrganizationId | — |
| PARENT_ASSIGNMENT_ID | AssignmentPEOParentAssignmentId | — |
| PEOPLE_GROUP_ID | AssignmentPEOPeopleGroupId | — |
| PERIOD_OF_SERVICE_ID | AssignmentPEOPeriodOfServiceId | — |
| PERMANENT_TEMPORARY_FLAG | AssignmentPEOPermanentTemporaryFlag | — |
| PERSON_ID | AssignmentPEOPersonId | — |
| PERSON_REFERRED_BY_ID | AssignmentPEOPersonReferredById | — |
| PERSON_TYPE_ID | AssignmentPEOPersonTypeId | — |
| PO_HEADER_ID | AssignmentPEOPoHeaderId | — |
| PO_LINE_ID | AssignmentPEOPoLineId | — |
| POSITION_ID | AssignmentPEOPositionId | — |
| POSITION_OVERRIDE_FLAG | AssignmentPEOPositionOverrideFlag | — |
| POSTING_CONTENT_ID | AssignmentPEOPostingContentId | — |
| PRIMARY_ASSIGNMENT_FLAG | AssignmentPEOPrimaryAssignmentFlag | — |
| PRIMARY_FLAG | AssignmentPEOPrimaryFlag | — |
| PRIMARY_WORK_RELATION_FLAG | AssignmentPEOPrimaryWorkRelationFlag | — |
| PRIMARY_WORK_TERMS_FLAG | AssignmentPEOPrimaryWorkTermsFlag | — |
| PROBATION_PERIOD | AssignmentPEOProbationPeriod | — |
| PROBATION_UNIT | AssignmentPEOProbationUnit | — |
| PROJECT_TITLE | AssignmentPEOProjectTitle | — |
| PROJECTED_ASSIGNMENT_END | AssignmentPEOProjectedAssignmentEnd | — |
| PROJECTED_START_DATE | AssignmentPEOProjectedStartDate | — |
| PROPOSED_WORKER_TYPE | AssignmentPEOProposedWorkerType | — |
| REASON_CODE | AssignmentPEOReasonCode | — |
| RECORD_CREATOR | AssignmentPEORecordCreator | — |
| RECRUITER_ID | AssignmentPEORecruiterId | — |
| RECRUITMENT_ACTIVITY_ID | AssignmentPEORecruitmentActivityId | — |
| RETIREMENT_AGE | AssignmentPEORetirementAge | — |
| RETIREMENT_DATE | AssignmentPEORetirementDate | — |
| SAL_REVIEW_PERIOD | AssignmentPEOSalReviewPeriod | — |
| SAL_REVIEW_PERIOD_FREQUENCY | AssignmentPEOSalReviewPeriodFrequency | — |
| SET_OF_BOOKS_ID | AssignmentPEOSetOfBooksId | — |
| SOFT_CODING_KEYFLEX_ID | AssignmentPEOSoftCodingKeyflexId | — |
| SOURCE_ORGANIZATION_ID | AssignmentPEOSourceOrganizationId | — |
| SOURCE_TYPE | AssignmentPEOSourceType | — |
| SPECIAL_CEILING_STEP_ID | AssignmentPEOSpecialCeilingStepId | — |
| STEP_ENTRY_DATE | AssignmentPEOStepEntryDate | — |
| SYSTEM_PERSON_TYPE | AssignmentPEOSystemPersonType | — |
| TAX_ADDRESS_ID | AssignmentPEOTaxAddressId | — |
| TIME_NORMAL_FINISH | AssignmentPEOTimeNormalFinish | — |
| TIME_NORMAL_START | AssignmentPEOTimeNormalStart | — |
| VACANCY_ID | AssignmentPEOVacancyId | — |
| VENDOR_ASSIGNMENT_NUMBER | AssignmentPEOVendorAssignmentNumber | — |
| VENDOR_EMPLOYEE_NUMBER | AssignmentPEOVendorEmployeeNumber | — |
| VENDOR_ID | AssignmentPEOVendorId | — |
| VENDOR_SITE_ID | AssignmentPEOVendorSiteId | — |
| WORK_AT_HOME | AssignmentPEOWorkAtHome | — |
| WORK_TERMS_ASSIGNMENT_ID | AssignmentPEOWorkTermsAssignmentId | — |

### [[scheduleexceptionpvo|ScheduleExceptionPVO]] (GL · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | AssignmentPEOAssignmentId | — |
| EFFECTIVE_END_DATE | AssignmentPEOEffectiveEndDate | — |
| EFFECTIVE_LATEST_CHANGE | AssignmentPEOEffectiveLatestChange | — |
| EFFECTIVE_SEQUENCE | AssignmentPEOEffectiveSequence | — |
| EFFECTIVE_START_DATE | AssignmentPEOEffectiveStartDate | ✅ |
| PERSON_ID | AssignmentPEOPersonId | — |

---

## 📚 Referências

- [Oracle Docs — PER_ALL_ASSIGNMENTS_M](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallassignmentsm.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
