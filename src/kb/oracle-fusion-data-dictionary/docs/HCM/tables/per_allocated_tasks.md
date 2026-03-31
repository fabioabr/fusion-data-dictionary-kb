---
id: DOC-HCM-621
doc_type: system-doc
title: "PER_ALLOCATED_TASKS — Tarefas Alocadas"
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
  - tarefas
  - checklist-tasks
aliases:
  - PER_ALLOCATED_TASKS
  - per_allocated_tasks
  - per-allocated-tasks
  - tarefas-alocadas
  - per-allocated-tasks
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_TASKS

## 📌 Visão Geral

Armazena as **tarefas individuais** alocadas dentro de um checklist. Cada registro representa uma tarefa específica que deve ser concluída como parte de um processo de checklist.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de tarefas** — rastreamento individual de cada item do checklist.
- **Atribuição de responsáveis** — cada tarefa pode ter um responsável diferente.
- **Prazos** — controle de datas-limite para cada tarefa.
- **Status granular** — acompanhamento do progresso tarefa a tarefa.
- **Compliance** — evidência de conclusão de itens obrigatórios.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_TASK_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa alocada | — | 🟢 95% |
| 2 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist ao qual pertence | PER_ALLOCATED_CHECKLISTS | 🟢 90% |
| 3 | TASK_STATUS | VARCHAR2(30) | NULL | Status | Status da tarefa (OPEN, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 4 | PERFORMER_PERSON_ID | NUMBER(18) | NULL | FK | Responsável pela execução | PER_ALL_PEOPLE_F | 🟢 85% |
| 5 | TARGET_END_DATE | DATE | NULL | Período | Data limite para conclusão | — | 🟢 85% |
| 6 | ACTUAL_END_DATE | DATE | NULL | Período | Data real de conclusão | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_allocated_checklists]] — via `ALLOCATED_CHECKLIST_ID` (checklist pai)
- [[per_all_people_f]] — via `PERFORMER_PERSON_ID` (responsável pela execução da tarefa)

### Tabelas-filha (FK de saída)
- [[per_allocated_tasks_tl]] — via `ALLOCATED_TASK_ID` (traduções da tarefa alocada)
- [[per_alloc_task_notifs]] — via `ALLOCATED_TASK_ID` (notificações da tarefa alocada)

---

## 📎 Uso Típico

### Tarefas pendentes de um checklist
```sql
SELECT pat.ALLOCATED_TASK_ID, pat.TASK_STATUS, pat.TARGET_END_DATE
FROM   PER_ALLOCATED_TASKS pat
WHERE  pat.ALLOCATED_CHECKLIST_ID = :p_checklist_id
  AND  pat.TASK_STATUS != 'COMPLETED'
ORDER BY pat.TARGET_END_DATE;
```

### Filtros comuns
- `TASK_STATUS = 'OPEN'` — Tarefas abertas
- `TARGET_END_DATE < SYSDATE` — Tarefas atrasadas
---

## 🔒 Observações

- Cada tarefa é uma instância dentro de um checklist alocado.
- O `PERFORMER_PERSON_ID` identifica quem deve executar a tarefa.
- A diferença entre `TARGET_END_DATE` e `ACTUAL_END_DATE` permite medir atrasos.
---

## 🔗 PVOs Relacionados

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 48/173)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_ALLOCATED_CHECKLIST_ID | AllocatedChecklistTasksPEOAbsAllocatedChecklistId | — |
| ACTION_TYPE | AllocatedChecklistTasksPEOActionType | ✅ |
| ACTUAL_END_DATE | AllocatedChecklistTasksPEOActualEndDate | ✅ |
| ACTUAL_START_DATE | AllocatedChecklistTasksPEOActualStartDate | ✅ |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistTasksPEOAllocatedChecklistId | ✅ |
| ALLOCATED_TASK_ID | AllocatedTaskId | ✅ |
| ATTRIBUTE1 | AllocatedChecklistTasksPEOAttribute1 | — |
| ATTRIBUTE10 | AllocatedChecklistTasksPEOAttribute10 | — |
| ATTRIBUTE11 | AllocatedChecklistTasksPEOAttribute11 | — |
| ATTRIBUTE12 | AllocatedChecklistTasksPEOAttribute12 | — |
| ATTRIBUTE13 | AllocatedChecklistTasksPEOAttribute13 | — |
| ATTRIBUTE14 | AllocatedChecklistTasksPEOAttribute14 | — |
| ATTRIBUTE15 | AllocatedChecklistTasksPEOAttribute15 | — |
| ATTRIBUTE16 | AllocatedChecklistTasksPEOAttribute16 | — |
| ATTRIBUTE17 | AllocatedChecklistTasksPEOAttribute17 | — |
| ATTRIBUTE18 | AllocatedChecklistTasksPEOAttribute18 | — |
| ATTRIBUTE19 | AllocatedChecklistTasksPEOAttribute19 | — |
| ATTRIBUTE2 | AllocatedChecklistTasksPEOAttribute2 | — |
| ATTRIBUTE20 | AllocatedChecklistTasksPEOAttribute20 | — |
| ATTRIBUTE21 | AllocatedChecklistTasksPEOAttribute21 | — |
| ATTRIBUTE22 | AllocatedChecklistTasksPEOAttribute22 | — |
| ATTRIBUTE23 | AllocatedChecklistTasksPEOAttribute23 | — |
| ATTRIBUTE24 | AllocatedChecklistTasksPEOAttribute24 | — |
| ATTRIBUTE25 | AllocatedChecklistTasksPEOAttribute25 | — |
| ATTRIBUTE26 | AllocatedChecklistTasksPEOAttribute26 | — |
| ATTRIBUTE27 | AllocatedChecklistTasksPEOAttribute27 | — |
| ATTRIBUTE28 | AllocatedChecklistTasksPEOAttribute28 | — |
| ATTRIBUTE29 | AllocatedChecklistTasksPEOAttribute29 | — |
| ATTRIBUTE3 | AllocatedChecklistTasksPEOAttribute3 | — |
| ATTRIBUTE30 | AllocatedChecklistTasksPEOAttribute30 | — |
| ATTRIBUTE4 | AllocatedChecklistTasksPEOAttribute4 | — |
| ATTRIBUTE5 | AllocatedChecklistTasksPEOAttribute5 | — |
| ATTRIBUTE6 | AllocatedChecklistTasksPEOAttribute6 | — |
| ATTRIBUTE7 | AllocatedChecklistTasksPEOAttribute7 | — |
| ATTRIBUTE8 | AllocatedChecklistTasksPEOAttribute8 | — |
| ATTRIBUTE9 | AllocatedChecklistTasksPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | AllocatedChecklistTasksPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | AllocatedChecklistTasksPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | AllocatedChecklistTasksPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | AllocatedChecklistTasksPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | AllocatedChecklistTasksPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | AllocatedChecklistTasksPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | AllocatedChecklistTasksPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | AllocatedChecklistTasksPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | AllocatedChecklistTasksPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | AllocatedChecklistTasksPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | AllocatedChecklistTasksPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | AllocatedChecklistTasksPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | AllocatedChecklistTasksPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | AllocatedChecklistTasksPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | AllocatedChecklistTasksPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | AllocatedChecklistTasksPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AllocatedChecklistTasksPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AllocatedChecklistTasksPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AllocatedChecklistTasksPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AllocatedChecklistTasksPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AllocatedChecklistTasksPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AllocatedChecklistTasksPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AllocatedChecklistTasksPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AllocatedChecklistTasksPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AllocatedChecklistTasksPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AllocatedChecklistTasksPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AllocatedChecklistTasksPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AllocatedChecklistTasksPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AllocatedChecklistTasksPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AllocatedChecklistTasksPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AllocatedChecklistTasksPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AllocatedChecklistTasksPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AllocatedChecklistTasksPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AllocatedChecklistTasksPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AllocatedChecklistTasksPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AllocatedChecklistTasksPEOAttributeNumber9 | — |
| COMPLETED_BY | AllocatedChecklistTasksPEOCompletedBy | — |
| COMPLETION_DATE | AllocatedChecklistTasksPEOCompletionDate | — |
| CONTACT_DETAILS | AllocatedChecklistTasksPEOContactDetails | ✅ |
| CREATED_BY | AllocatedChecklistTasksPEOCreatedBy | ✅ |
| CREATION_DATE | AllocatedChecklistTasksPEOCreationDate | ✅ |
| DEF_ALLOCATION_DATE | AllocatedChecklistTasksPEODefAllocationDate | ✅ |
| DEFAULT_PERF_RESP_TYPE | AllocatedChecklistTasksPEODefaultPerfRespType | ✅ |
| DEPENDENT_ON_TASKS | AllocatedChecklistTasksPEODependentOnTasks | ✅ |
| DETAIL_ALLOC_CHECKLIST_ID | AllocatedChecklistTasksPEODetailAllocChecklistId | — |
| DETAIL_CHECKLIST_ID | AllocatedChecklistTasksPEODetailChecklistId | — |
| DOCUMENT_ENTITY_ID | AllocatedChecklistTasksPEODocumentEntityId | — |
| DOCUMENT_TYPE_ID | AllocatedChecklistTasksPEODocumentTypeId | ✅ |
| ENTERPRISE_ID | AllocatedChecklistTasksPEOEnterpriseId | — |
| ESIGN_TYPE | AllocatedChecklistTasksPEOEsignType | ✅ |
| EXPIRY_DAYS | AllocatedChecklistTasksPEOExpiryDays | ✅ |
| FLEX_CONTEXT_CODE | AllocatedChecklistTasksPEOFlexContextCode | — |
| GENERATE_ATOM_FEED | AllocatedChecklistTasksPEOGenerateAtomFeed | — |
| INFORMATION1 | AllocatedChecklistTasksPEOInformation1 | — |
| INFORMATION10 | AllocatedChecklistTasksPEOInformation10 | — |
| INFORMATION11 | AllocatedChecklistTasksPEOInformation11 | — |
| INFORMATION12 | AllocatedChecklistTasksPEOInformation12 | — |
| INFORMATION13 | AllocatedChecklistTasksPEOInformation13 | — |
| INFORMATION14 | AllocatedChecklistTasksPEOInformation14 | — |
| INFORMATION15 | AllocatedChecklistTasksPEOInformation15 | — |
| INFORMATION16 | AllocatedChecklistTasksPEOInformation16 | — |
| INFORMATION17 | AllocatedChecklistTasksPEOInformation17 | — |
| INFORMATION18 | AllocatedChecklistTasksPEOInformation18 | — |
| INFORMATION19 | AllocatedChecklistTasksPEOInformation19 | — |
| INFORMATION2 | AllocatedChecklistTasksPEOInformation2 | — |
| INFORMATION20 | AllocatedChecklistTasksPEOInformation20 | — |
| INFORMATION21 | AllocatedChecklistTasksPEOInformation21 | — |
| INFORMATION22 | AllocatedChecklistTasksPEOInformation22 | — |
| INFORMATION23 | AllocatedChecklistTasksPEOInformation23 | — |
| INFORMATION24 | AllocatedChecklistTasksPEOInformation24 | — |
| INFORMATION25 | AllocatedChecklistTasksPEOInformation25 | — |
| INFORMATION26 | AllocatedChecklistTasksPEOInformation26 | — |
| INFORMATION27 | AllocatedChecklistTasksPEOInformation27 | — |
| INFORMATION28 | AllocatedChecklistTasksPEOInformation28 | — |
| INFORMATION29 | AllocatedChecklistTasksPEOInformation29 | — |
| INFORMATION3 | AllocatedChecklistTasksPEOInformation3 | — |
| INFORMATION30 | AllocatedChecklistTasksPEOInformation30 | — |
| INFORMATION4 | AllocatedChecklistTasksPEOInformation4 | — |
| INFORMATION5 | AllocatedChecklistTasksPEOInformation5 | — |
| INFORMATION6 | AllocatedChecklistTasksPEOInformation6 | — |
| INFORMATION7 | AllocatedChecklistTasksPEOInformation7 | — |
| INFORMATION8 | AllocatedChecklistTasksPEOInformation8 | — |
| INFORMATION9 | AllocatedChecklistTasksPEOInformation9 | — |
| INFORMATION_CATEGORY | AllocatedChecklistTasksPEOInformationCategory | — |
| LAST_UPDATE_DATE | AllocatedChecklistTasksPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AllocatedChecklistTasksPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AllocatedChecklistTasksPEOLastUpdatedBy | ✅ |
| MANDATORY_FLAG | AllocatedChecklistTasksPEOMandatoryFlag | ✅ |
| MEETING_OFFSET | AllocatedChecklistTasksPEOMeetingOffset | ✅ |
| MEETING_TIME | AllocatedChecklistTasksPEOMeetingTime | ✅ |
| NEXT_REMINDER_DATE | AllocatedChecklistTasksPEONextReminderDate | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistTasksPEOObjectVersionNumber | — |
| OWNER_RESP_TYPE | AllocatedChecklistTasksPEOOwnerRespType | ✅ |
| OWNER_RESP_TYPE_USERS | AllocatedChecklistTasksPEOOwnerRespTypeUsers | — |
| PERFORMER_ORIG_SYS_ID | AllocatedChecklistTasksPEOPerformerOrigSysId | ✅ |
| PERFORMER_ORIG_SYSTEM | AllocatedChecklistTasksPEOPerformerOrigSystem | — |
| PROCESSING_MODE | AllocatedChecklistTasksPEOProcessingMode | — |
| QUESTIONNAIRE_ID | AllocatedChecklistTasksPEOQuestionnaireId | ✅ |
| REASSIGNED_BY | AllocatedChecklistTasksPEOReassignedBy | — |
| REASSIGNED_DATE | AllocatedChecklistTasksPEOReassignedDate | — |
| REMINDER_COUNT | AllocatedChecklistTasksPEOReminderCount | — |
| REMINDER_DURATION | AllocatedChecklistTasksPEOReminderDuration | ✅ |
| REMINDER_RECURRENCE | AllocatedChecklistTasksPEOReminderRecurrence | ✅ |
| REMINDER_RELATIVE_TO | AllocatedChecklistTasksPEOReminderRelativeTo | ✅ |
| REMINDER_TEMPLATE_ID | AllocatedChecklistTasksPEOReminderTemplateId | — |
| REOPEN_DATE | AllocatedChecklistTasksPEOReopenDate | ✅ |
| REOPENED_BY | AllocatedChecklistTasksPEOReopenedBy | ✅ |
| REPORT_PATH | AllocatedChecklistTasksPEOReportPath | ✅ |
| RESP_PERFORMER_AVAILABILITY | AllocatedChecklistTasksPEORespPerformerAvailability | ✅ |
| RESPONSIBILITY_TYPE | AllocatedChecklistTasksPEOResponsibilityType | ✅ |
| RESPONSIBILITY_TYPE_GUID | AllocatedChecklistTasksPEOResponsibilityTypeGuid | — |
| SIGN_DATE | AllocatedChecklistTasksPEOSignDate | ✅ |
| SIGN_DOCUMENT | AllocatedChecklistTasksPEOSignDocument | ✅ |
| SIGN_TEMPLATE | AllocatedChecklistTasksPEOSignTemplate | ✅ |
| SIGNER_EMAIL | AllocatedChecklistTasksPEOSignerEmail | ✅ |
| SIGNER_NAME | AllocatedChecklistTasksPEOSignerName | ✅ |
| STATUS | AllocatedChecklistTasksPEOStatus | ✅ |
| TARGET_DURATION | AllocatedChecklistTasksPEOTargetDuration | ✅ |
| TARGET_DURATION_UOM | AllocatedChecklistTasksPEOTargetDurationUom | ✅ |
| TARGET_END_DATE | AllocatedChecklistTasksPEOTargetEndDate | ✅ |
| TARGET_START_DATE | AllocatedChecklistTasksPEOTargetStartDate | ✅ |
| TASK_ACTION_CODE | AllocatedChecklistTasksPEOTaskActionCode | ✅ |
| TASK_ACTION_ID | AllocatedChecklistTasksPEOTaskActionId | ✅ |
| TASK_COMMENTS | AllocatedChecklistTasksPEOTaskComments | ✅ |
| TASK_CONFIGURATION | AllocatedChecklistTasksPEOTaskConfiguration | ✅ |
| TASK_DELAY_DURATION | AllocatedChecklistTasksPEOTaskDelayDuration | ✅ |
| TASK_DELAY_DURATION_UOM | AllocatedChecklistTasksPEOTaskDelayDurationUom | ✅ |
| TASK_FEATURE1 | AllocatedChecklistTasksPEOTaskFeature1 | — |
| TASK_IN_CHECKLIST_ID | AllocatedChecklistTasksPEOTaskInChecklistId | — |
| TASK_INITIATOR | AllocatedChecklistTasksPEOTaskInitiator | — |
| TASK_INITIATOR_PERSON_ID | AllocatedChecklistTasksPEOTaskInitiatorPersonId | — |
| TASK_OWNER_PERSON_ID | AllocatedChecklistTasksPEOTaskOwnerPersonId | ✅ |
| TASK_OWNER_USERNAME | AllocatedChecklistTasksPEOTaskOwnerUsername | — |
| TASK_OWNERS | AllocatedChecklistTasksPEOTaskOwners | — |
| TASK_PERCENTAGE_COMPLETE | AllocatedChecklistTasksPEOTaskPercentageComplete | — |
| TASK_PERFORMERS | AllocatedChecklistTasksPEOTaskPerformers | — |
| TASK_SEQUENCE | AllocatedChecklistTasksPEOTaskSequence | — |

---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_TASKS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedtasks.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
