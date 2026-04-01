---
id: DOC-HCM-634
doc_type: system-doc
title: "PER_ASSIGNMENT_SUPERVISORS_F — Supervisores de Assignment"
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
  - supervisores
  - assignment-supervisors
aliases:
  - PER_ASSIGNMENT_SUPERVISORS_F
  - per_assignment_supervisors_f
  - per-assignment-supervisors-f
  - supervisores-de-assignment
  - per-assignment-super
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_SUPERVISORS_F

## 📌 Visão Geral

Armazena os **supervisores/gestores** associados a cada assignment, com vigência temporal. Permite múltiplos supervisores por assignment (direto, matricial, funcional).

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Hierarquia de reporte** — define a cadeia de supervisão de cada colaborador.
- **Gestão matricial** — suporte a múltiplos tipos de supervisor por assignment.
- **Workflow de aprovação** — determina quem aprova solicitações do colaborador.
- **Relatórios gerenciais** — visualização de equipes por gestor.
- **Delegação** — registro de supervisores temporários.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_SUPERVISOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de supervisão | — | 🟢 95% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment supervisionado | PER_ALL_ASSIGNMENTS_M | 🟢 95% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | SUPERVISOR_ID | NUMBER(18) | NOT NULL | FK | Pessoa supervisora | PER_ALL_PEOPLE_F | 🟢 90% |
| 6 | SUPERVISOR_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de supervisão (LINE_MANAGER, PROJECT_MANAGER, etc.) | — | 🟢 90% |
| 7 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Configuração | Supervisor primário (Y/N) | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (assignment supervisionado)
- [[per_all_people_f]] — via `SUPERVISOR_ID` (pessoa que atua como supervisor do vínculo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Supervisor atual de um assignment
```sql
SELECT pasf.SUPERVISOR_ID, pasf.SUPERVISOR_TYPE, pasf.PRIMARY_FLAG
FROM   PER_ASSIGNMENT_SUPERVISORS_F pasf
WHERE  pasf.ASSIGNMENT_ID = :p_assignment_id
  AND  pasf.PRIMARY_FLAG = 'Y'
  AND  SYSDATE BETWEEN pasf.EFFECTIVE_START_DATE AND pasf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `SUPERVISOR_TYPE = 'LINE_MANAGER'` — Gestor direto
- `PRIMARY_FLAG = 'Y'` — Supervisor primário
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Registros vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Suporta múltiplos supervisores por assignment (ex.: gestor direto + gestor de projeto).
- O campo `SUPERVISOR_TYPE` define o tipo de relação de supervisão.
- A flag `PRIMARY_FLAG` identifica o supervisor principal para workflows de aprovação.
---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO · BICC: 4/102)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorActionOccurrenceId | — |
| ACTION_OCCURRENCE_ID | SupervisorNameActionOccurrenceId | — |
| ASSIGNMENT_ID | AssignmentSupervisorAssignmentId | — |
| ASSIGNMENT_ID | SupervisorNameAssignmentId | — |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorAssignmentSupervisorId | — |
| ASSIGNMENT_SUPERVISOR_ID | SupervisorNameAssignmentSupervisorId | — |
| BUSINESS_GROUP_ID | AssignmentSupervisorBusinessGroupId | — |
| BUSINESS_GROUP_ID | SupervisorNameBusinessGroupId | — |
| CREATED_BY | AssignmentSupervisorCreatedBy | — |
| CREATED_BY | SupervisorNameCreatedBy | — |
| CREATION_DATE | AssignmentSupervisorCreationDate | — |
| CREATION_DATE | SupervisorNameCreationDate | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorEffectiveEndDate | — |
| EFFECTIVE_END_DATE | SupervisorNameEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorEffectiveStartDate | ✅ |
| EFFECTIVE_START_DATE | SupervisorNameEffectiveStartDate | ✅ |
| FREEZE_START_DATE | AssignmentSupervisorFreezeStartDate | — |
| FREEZE_START_DATE | SupervisorNameFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentSupervisorFreezeUntilDate | — |
| FREEZE_UNTIL_DATE | SupervisorNameFreezeUntilDate | — |
| LAST_UPDATE_DATE | AssignmentSupervisorLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | SupervisorNameLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentSupervisorLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | SupervisorNameLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentSupervisorLastUpdatedBy | — |
| LAST_UPDATED_BY | SupervisorNameLastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorManagerAssignmentId | — |
| MANAGER_ASSIGNMENT_ID | SupervisorNameManagerAssignmentId | — |
| MANAGER_ID | AssignmentSupervisorManagerId | — |
| MANAGER_ID | SupervisorNameManagerId | — |
| MANAGER_TYPE | AssignmentSupervisorManagerType | — |
| MANAGER_TYPE | SupervisorNameManagerType | — |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | SupervisorNameObjectVersionNumber | — |
| PERSON_ID | AssignmentSupervisorPersonId | — |
| PERSON_ID | SupervisorNamePersonId | — |
| PRIMARY_FLAG | AssignmentSupervisorPrimaryFlag | — |
| PRIMARY_FLAG | SupervisorNamePrimaryFlag | — |
| SUP_ATTRIBUTE1 | AssignmentSupervisorSupAttribute1 | — |
| SUP_ATTRIBUTE1 | SupervisorNameSupAttribute1 | — |
| SUP_ATTRIBUTE10 | AssignmentSupervisorSupAttribute10 | — |
| SUP_ATTRIBUTE10 | SupervisorNameSupAttribute10 | — |
| SUP_ATTRIBUTE11 | AssignmentSupervisorSupAttribute11 | — |
| SUP_ATTRIBUTE11 | SupervisorNameSupAttribute11 | — |
| SUP_ATTRIBUTE12 | AssignmentSupervisorSupAttribute12 | — |
| SUP_ATTRIBUTE12 | SupervisorNameSupAttribute12 | — |
| SUP_ATTRIBUTE13 | AssignmentSupervisorSupAttribute13 | — |
| SUP_ATTRIBUTE13 | SupervisorNameSupAttribute13 | — |
| SUP_ATTRIBUTE14 | AssignmentSupervisorSupAttribute14 | — |
| SUP_ATTRIBUTE14 | SupervisorNameSupAttribute14 | — |
| SUP_ATTRIBUTE15 | AssignmentSupervisorSupAttribute15 | — |
| SUP_ATTRIBUTE15 | SupervisorNameSupAttribute15 | — |
| SUP_ATTRIBUTE16 | AssignmentSupervisorSupAttribute16 | — |
| SUP_ATTRIBUTE16 | SupervisorNameSupAttribute16 | — |
| SUP_ATTRIBUTE17 | AssignmentSupervisorSupAttribute17 | — |
| SUP_ATTRIBUTE17 | SupervisorNameSupAttribute17 | — |
| SUP_ATTRIBUTE18 | AssignmentSupervisorSupAttribute18 | — |
| SUP_ATTRIBUTE18 | SupervisorNameSupAttribute18 | — |
| SUP_ATTRIBUTE19 | AssignmentSupervisorSupAttribute19 | — |
| SUP_ATTRIBUTE19 | SupervisorNameSupAttribute19 | — |
| SUP_ATTRIBUTE2 | AssignmentSupervisorSupAttribute2 | — |
| SUP_ATTRIBUTE2 | SupervisorNameSupAttribute2 | — |
| SUP_ATTRIBUTE20 | AssignmentSupervisorSupAttribute20 | — |
| SUP_ATTRIBUTE20 | SupervisorNameSupAttribute20 | — |
| SUP_ATTRIBUTE21 | AssignmentSupervisorSupAttribute21 | — |
| SUP_ATTRIBUTE21 | SupervisorNameSupAttribute21 | — |
| SUP_ATTRIBUTE22 | AssignmentSupervisorSupAttribute22 | — |
| SUP_ATTRIBUTE22 | SupervisorNameSupAttribute22 | — |
| SUP_ATTRIBUTE23 | AssignmentSupervisorSupAttribute23 | — |
| SUP_ATTRIBUTE23 | SupervisorNameSupAttribute23 | — |
| SUP_ATTRIBUTE24 | AssignmentSupervisorSupAttribute24 | — |
| SUP_ATTRIBUTE24 | SupervisorNameSupAttribute24 | — |
| SUP_ATTRIBUTE25 | AssignmentSupervisorSupAttribute25 | — |
| SUP_ATTRIBUTE25 | SupervisorNameSupAttribute25 | — |
| SUP_ATTRIBUTE26 | AssignmentSupervisorSupAttribute26 | — |
| SUP_ATTRIBUTE26 | SupervisorNameSupAttribute26 | — |
| SUP_ATTRIBUTE27 | AssignmentSupervisorSupAttribute27 | — |
| SUP_ATTRIBUTE27 | SupervisorNameSupAttribute27 | — |
| SUP_ATTRIBUTE28 | AssignmentSupervisorSupAttribute28 | — |
| SUP_ATTRIBUTE28 | SupervisorNameSupAttribute28 | — |
| SUP_ATTRIBUTE29 | AssignmentSupervisorSupAttribute29 | — |
| SUP_ATTRIBUTE29 | SupervisorNameSupAttribute29 | — |
| SUP_ATTRIBUTE3 | AssignmentSupervisorSupAttribute3 | — |
| SUP_ATTRIBUTE3 | SupervisorNameSupAttribute3 | — |
| SUP_ATTRIBUTE30 | AssignmentSupervisorSupAttribute30 | — |
| SUP_ATTRIBUTE30 | SupervisorNameSupAttribute30 | — |
| SUP_ATTRIBUTE4 | AssignmentSupervisorSupAttribute4 | — |
| SUP_ATTRIBUTE4 | SupervisorNameSupAttribute4 | — |
| SUP_ATTRIBUTE5 | AssignmentSupervisorSupAttribute5 | — |
| SUP_ATTRIBUTE5 | SupervisorNameSupAttribute5 | — |
| SUP_ATTRIBUTE6 | AssignmentSupervisorSupAttribute6 | — |
| SUP_ATTRIBUTE6 | SupervisorNameSupAttribute6 | — |
| SUP_ATTRIBUTE7 | AssignmentSupervisorSupAttribute7 | — |
| SUP_ATTRIBUTE7 | SupervisorNameSupAttribute7 | — |
| SUP_ATTRIBUTE8 | AssignmentSupervisorSupAttribute8 | — |
| SUP_ATTRIBUTE8 | SupervisorNameSupAttribute8 | — |
| SUP_ATTRIBUTE9 | AssignmentSupervisorSupAttribute9 | — |
| SUP_ATTRIBUTE9 | SupervisorNameSupAttribute9 | — |
| SUP_ATTRIBUTE_CATEGORY | AssignmentSupervisorSupAttributeCategory | — |
| SUP_ATTRIBUTE_CATEGORY | SupervisorNameSupAttributeCategory | — |
| WORKING_PERCENTAGE | AssignmentSupervisorWorkingPercentage | — |
| WORKING_PERCENTAGE | SupervisorNameWorkingPercentage | — |

### [[assignmentsupervisorextractpvo|AssignmentSupervisorExtractPVO]] (HCM · BICC: 20/51)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FREEZE_START_DATE | FreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | FreezeUntilDate | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MANAGER_ASSIGNMENT_ID | ManagerAssignmentId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| MANAGER_TYPE | ManagerType | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERSON_ID | PersonId | ✅ |
| PRIMARY_FLAG | PrimaryFlag | ✅ |
| SUP_ATTRIBUTE1 | SupAttribute1 | — |
| SUP_ATTRIBUTE10 | SupAttribute10 | — |
| SUP_ATTRIBUTE11 | SupAttribute11 | — |
| SUP_ATTRIBUTE12 | SupAttribute12 | — |
| SUP_ATTRIBUTE13 | SupAttribute13 | — |
| SUP_ATTRIBUTE14 | SupAttribute14 | — |
| SUP_ATTRIBUTE15 | SupAttribute15 | — |
| SUP_ATTRIBUTE16 | SupAttribute16 | — |
| SUP_ATTRIBUTE17 | SupAttribute17 | — |
| SUP_ATTRIBUTE18 | SupAttribute18 | — |
| SUP_ATTRIBUTE19 | SupAttribute19 | — |
| SUP_ATTRIBUTE2 | SupAttribute2 | — |
| SUP_ATTRIBUTE20 | SupAttribute20 | — |
| SUP_ATTRIBUTE21 | SupAttribute21 | — |
| SUP_ATTRIBUTE22 | SupAttribute22 | — |
| SUP_ATTRIBUTE23 | SupAttribute23 | — |
| SUP_ATTRIBUTE24 | SupAttribute24 | — |
| SUP_ATTRIBUTE25 | SupAttribute25 | — |
| SUP_ATTRIBUTE26 | SupAttribute26 | — |
| SUP_ATTRIBUTE27 | SupAttribute27 | — |
| SUP_ATTRIBUTE28 | SupAttribute28 | — |
| SUP_ATTRIBUTE29 | SupAttribute29 | — |
| SUP_ATTRIBUTE3 | SupAttribute3 | — |
| SUP_ATTRIBUTE30 | SupAttribute30 | — |
| SUP_ATTRIBUTE4 | SupAttribute4 | — |
| SUP_ATTRIBUTE5 | SupAttribute5 | — |
| SUP_ATTRIBUTE6 | SupAttribute6 | — |
| SUP_ATTRIBUTE7 | SupAttribute7 | — |
| SUP_ATTRIBUTE8 | SupAttribute8 | — |
| SUP_ATTRIBUTE9 | SupAttribute9 | — |
| SUP_ATTRIBUTE_CATEGORY | SupAttributeCategory | — |
| WORKING_PERCENTAGE | WorkingPercentage | ✅ |

### [[assignmentsupervisorpvo|AssignmentSupervisorPVO]] (HCM · BICC: 18/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId | ✅ |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId | ✅ |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorId | ✅ |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId | ✅ |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate | ✅ |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy | ✅ |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | ✅ |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | ✅ |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | ✅ |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber | — |
| PERSON_ID | AssignmentSupervisorPEOPersonId | ✅ |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag | ✅ |
| WORKING_PERCENTAGE | AssignmentSupervisorPEOWorkingPercentage | ✅ |

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 19/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId | ✅ |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId | ✅ |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | ✅ |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId | ✅ |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy | ✅ |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate | ✅ |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate | ✅ |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate | ✅ |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy | ✅ |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | ✅ |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | ✅ |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | ✅ |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber | ✅ |
| PERSON_ID | AssignmentSupervisorPEOPersonId | ✅ |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 6/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId | — |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId | — |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | — |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId | — |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy | — |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate | ✅ |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate | — |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | ✅ |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | ✅ |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | ✅ |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber | — |
| PERSON_ID | AssignmentSupervisorPEOPersonId | — |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag | ✅ |

### [[personmanagerhierarchyassignmentpvo|PersonManagerHierarchyAssignmentPVO]] (HCM · BICC: 4/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId | — |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId | — |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | — |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId | — |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy | — |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate | ✅ |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate | — |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy | — |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | — |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | ✅ |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | ✅ |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber | — |
| PERSON_ID | AssignmentSupervisorPEOPersonId | — |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag | — |
| WORKING_PERCENTAGE | AssignmentSupervisorPEOWorkingPercentage | — |

### [[personrefpvo|PersonRefPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate | ✅ |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | — |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | ✅ |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | — |

### [[plannedscheduleshiftentrypvo|PlannedScheduleShiftEntryPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorId | — |
| EFFECTIVE_END_DATE | mgrEffectiveEndDate | — |
| EFFECTIVE_START_DATE | mgrEffectiveStartDate | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | — |

### [[publishedscheduleshiftentrypvo|PublishedScheduleShiftEntryPVO]] (HCM · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorId | — |
| EFFECTIVE_END_DATE | mgrEffectiveEndDate | — |
| EFFECTIVE_START_DATE | mgrEffectiveStartDate | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERSON_ID | PersonId | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId1 | — |
| ACTION_OCCURRENCE_ID | SupervisorNamePEOActionOccurrenceId2 | — |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId1 | — |
| ASSIGNMENT_ID | SupervisorNamePEOAssignmentId2 | — |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | — |
| ASSIGNMENT_SUPERVISOR_ID | SupervisorNamePEOAssignmentSupervisorId1 | — |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | SupervisorNamePEOBusinessGroupId4 | — |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy16 | — |
| CREATED_BY | SupervisorNamePEOCreatedBy17 | — |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate16 | — |
| CREATION_DATE | SupervisorNamePEOCreationDate17 | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate3 | — |
| EFFECTIVE_END_DATE | SupervisorNamePEOEffectiveEndDate4 | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate3 | — |
| EFFECTIVE_START_DATE | SupervisorNamePEOEffectiveStartDate4 | — |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate1 | — |
| FREEZE_START_DATE | SupervisorNamePEOFreezeStartDate2 | — |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate1 | — |
| FREEZE_UNTIL_DATE | SupervisorNamePEOFreezeUntilDate2 | — |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate16 | — |
| LAST_UPDATE_DATE | SupervisorNamePEOLastUpdateDate17 | — |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin16 | — |
| LAST_UPDATE_LOGIN | SupervisorNamePEOLastUpdateLogin17 | — |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy16 | — |
| LAST_UPDATED_BY | SupervisorNamePEOLastUpdatedBy17 | — |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | — |
| MANAGER_ASSIGNMENT_ID | SupervisorNamePEOManagerAssignmentId1 | — |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | — |
| MANAGER_ID | SupervisorNamePEOManagerId1 | — |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | — |
| MANAGER_TYPE | SupervisorNamePEOManagerType1 | — |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber13 | — |
| OBJECT_VERSION_NUMBER | SupervisorNamePEOObjectVersionNumber14 | — |
| PERSON_ID | AssignmentSupervisorPEOPersonId3 | — |
| PERSON_ID | SupervisorNamePEOPersonId4 | — |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag1 | — |
| PRIMARY_FLAG | SupervisorNamePEOPrimaryFlag2 | — |
| SUP_ATTRIBUTE1 | AssignmentSupervisorPEOSupAttribute1 | — |
| SUP_ATTRIBUTE1 | SupervisorNamePEOSupAttribute110 | — |
| SUP_ATTRIBUTE10 | AssignmentSupervisorPEOSupAttribute10 | — |
| SUP_ATTRIBUTE10 | SupervisorNamePEOSupAttribute101 | — |
| SUP_ATTRIBUTE11 | AssignmentSupervisorPEOSupAttribute11 | — |
| SUP_ATTRIBUTE11 | SupervisorNamePEOSupAttribute111 | — |
| SUP_ATTRIBUTE12 | AssignmentSupervisorPEOSupAttribute12 | — |
| SUP_ATTRIBUTE12 | SupervisorNamePEOSupAttribute121 | — |
| SUP_ATTRIBUTE13 | AssignmentSupervisorPEOSupAttribute13 | — |
| SUP_ATTRIBUTE13 | SupervisorNamePEOSupAttribute131 | — |
| SUP_ATTRIBUTE14 | AssignmentSupervisorPEOSupAttribute14 | — |
| SUP_ATTRIBUTE14 | SupervisorNamePEOSupAttribute141 | — |
| SUP_ATTRIBUTE15 | AssignmentSupervisorPEOSupAttribute15 | — |
| SUP_ATTRIBUTE15 | SupervisorNamePEOSupAttribute151 | — |
| SUP_ATTRIBUTE16 | AssignmentSupervisorPEOSupAttribute16 | — |
| SUP_ATTRIBUTE16 | SupervisorNamePEOSupAttribute161 | — |
| SUP_ATTRIBUTE17 | AssignmentSupervisorPEOSupAttribute17 | — |
| SUP_ATTRIBUTE17 | SupervisorNamePEOSupAttribute171 | — |
| SUP_ATTRIBUTE18 | AssignmentSupervisorPEOSupAttribute18 | — |
| SUP_ATTRIBUTE18 | SupervisorNamePEOSupAttribute181 | — |
| SUP_ATTRIBUTE19 | AssignmentSupervisorPEOSupAttribute19 | — |
| SUP_ATTRIBUTE19 | SupervisorNamePEOSupAttribute191 | — |
| SUP_ATTRIBUTE2 | AssignmentSupervisorPEOSupAttribute2 | — |
| SUP_ATTRIBUTE2 | SupervisorNamePEOSupAttribute210 | — |
| SUP_ATTRIBUTE20 | AssignmentSupervisorPEOSupAttribute20 | — |
| SUP_ATTRIBUTE20 | SupervisorNamePEOSupAttribute201 | — |
| SUP_ATTRIBUTE21 | AssignmentSupervisorPEOSupAttribute21 | — |
| SUP_ATTRIBUTE21 | SupervisorNamePEOSupAttribute211 | — |
| SUP_ATTRIBUTE22 | AssignmentSupervisorPEOSupAttribute22 | — |
| SUP_ATTRIBUTE22 | SupervisorNamePEOSupAttribute221 | — |
| SUP_ATTRIBUTE23 | AssignmentSupervisorPEOSupAttribute23 | — |
| SUP_ATTRIBUTE23 | SupervisorNamePEOSupAttribute231 | — |
| SUP_ATTRIBUTE24 | AssignmentSupervisorPEOSupAttribute24 | — |
| SUP_ATTRIBUTE24 | SupervisorNamePEOSupAttribute241 | — |
| SUP_ATTRIBUTE25 | AssignmentSupervisorPEOSupAttribute25 | — |
| SUP_ATTRIBUTE25 | SupervisorNamePEOSupAttribute251 | — |
| SUP_ATTRIBUTE26 | AssignmentSupervisorPEOSupAttribute26 | — |
| SUP_ATTRIBUTE26 | SupervisorNamePEOSupAttribute261 | — |
| SUP_ATTRIBUTE27 | AssignmentSupervisorPEOSupAttribute27 | — |
| SUP_ATTRIBUTE27 | SupervisorNamePEOSupAttribute271 | — |
| SUP_ATTRIBUTE28 | AssignmentSupervisorPEOSupAttribute28 | — |
| SUP_ATTRIBUTE28 | SupervisorNamePEOSupAttribute281 | — |
| SUP_ATTRIBUTE29 | AssignmentSupervisorPEOSupAttribute29 | — |
| SUP_ATTRIBUTE29 | SupervisorNamePEOSupAttribute291 | — |
| SUP_ATTRIBUTE3 | AssignmentSupervisorPEOSupAttribute3 | — |
| SUP_ATTRIBUTE3 | SupervisorNamePEOSupAttribute31 | — |
| SUP_ATTRIBUTE30 | AssignmentSupervisorPEOSupAttribute30 | — |
| SUP_ATTRIBUTE30 | SupervisorNamePEOSupAttribute301 | — |
| SUP_ATTRIBUTE4 | AssignmentSupervisorPEOSupAttribute4 | — |
| SUP_ATTRIBUTE4 | SupervisorNamePEOSupAttribute41 | — |
| SUP_ATTRIBUTE5 | AssignmentSupervisorPEOSupAttribute5 | — |
| SUP_ATTRIBUTE5 | SupervisorNamePEOSupAttribute51 | — |
| SUP_ATTRIBUTE6 | AssignmentSupervisorPEOSupAttribute6 | — |
| SUP_ATTRIBUTE6 | SupervisorNamePEOSupAttribute61 | — |
| SUP_ATTRIBUTE7 | AssignmentSupervisorPEOSupAttribute7 | — |
| SUP_ATTRIBUTE7 | SupervisorNamePEOSupAttribute71 | — |
| SUP_ATTRIBUTE8 | AssignmentSupervisorPEOSupAttribute8 | — |
| SUP_ATTRIBUTE8 | SupervisorNamePEOSupAttribute81 | — |
| SUP_ATTRIBUTE9 | AssignmentSupervisorPEOSupAttribute9 | — |
| SUP_ATTRIBUTE9 | SupervisorNamePEOSupAttribute91 | — |
| SUP_ATTRIBUTE_CATEGORY | AssignmentSupervisorPEOSupAttributeCategory | — |
| SUP_ATTRIBUTE_CATEGORY | SupervisorNamePEOSupAttributeCategory1 | — |
| WORKING_PERCENTAGE | AssignmentSupervisorPEOWorkingPercentage | — |
| WORKING_PERCENTAGE | SupervisorNamePEOWorkingPercentage1 | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 2/102)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | AssignmentSupervisorPEOActionOccurrenceId1 | — |
| ACTION_OCCURRENCE_ID | SupervisorNamePEOActionOccurrenceId2 | — |
| ASSIGNMENT_ID | AssignmentSupervisorPEOAssignmentId1 | — |
| ASSIGNMENT_ID | SupervisorNamePEOAssignmentId2 | — |
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorPEOAssignmentSupervisorId | — |
| ASSIGNMENT_SUPERVISOR_ID | SupervisorNamePEOAssignmentSupervisorId1 | — |
| BUSINESS_GROUP_ID | AssignmentSupervisorPEOBusinessGroupId3 | — |
| BUSINESS_GROUP_ID | SupervisorNamePEOBusinessGroupId4 | — |
| CREATED_BY | AssignmentSupervisorPEOCreatedBy16 | — |
| CREATED_BY | SupervisorNamePEOCreatedBy17 | — |
| CREATION_DATE | AssignmentSupervisorPEOCreationDate16 | — |
| CREATION_DATE | SupervisorNamePEOCreationDate17 | — |
| EFFECTIVE_END_DATE | AssignmentSupervisorPEOEffectiveEndDate3 | — |
| EFFECTIVE_END_DATE | SupervisorNamePEOEffectiveEndDate4 | — |
| EFFECTIVE_START_DATE | AssignmentSupervisorPEOEffectiveStartDate3 | ✅ |
| EFFECTIVE_START_DATE | SupervisorNamePEOEffectiveStartDate4 | — |
| FREEZE_START_DATE | AssignmentSupervisorPEOFreezeStartDate1 | — |
| FREEZE_START_DATE | SupervisorNamePEOFreezeStartDate2 | — |
| FREEZE_UNTIL_DATE | AssignmentSupervisorPEOFreezeUntilDate1 | — |
| FREEZE_UNTIL_DATE | SupervisorNamePEOFreezeUntilDate2 | — |
| LAST_UPDATE_DATE | AssignmentSupervisorPEOLastUpdateDate16 | ✅ |
| LAST_UPDATE_DATE | SupervisorNamePEOLastUpdateDate17 | — |
| LAST_UPDATE_LOGIN | AssignmentSupervisorPEOLastUpdateLogin16 | — |
| LAST_UPDATE_LOGIN | SupervisorNamePEOLastUpdateLogin17 | — |
| LAST_UPDATED_BY | AssignmentSupervisorPEOLastUpdatedBy16 | — |
| LAST_UPDATED_BY | SupervisorNamePEOLastUpdatedBy17 | — |
| MANAGER_ASSIGNMENT_ID | AssignmentSupervisorPEOManagerAssignmentId | — |
| MANAGER_ASSIGNMENT_ID | SupervisorNamePEOManagerAssignmentId1 | — |
| MANAGER_ID | AssignmentSupervisorPEOManagerId | — |
| MANAGER_ID | SupervisorNamePEOManagerId1 | — |
| MANAGER_TYPE | AssignmentSupervisorPEOManagerType | — |
| MANAGER_TYPE | SupervisorNamePEOManagerType1 | — |
| OBJECT_VERSION_NUMBER | AssignmentSupervisorPEOObjectVersionNumber13 | — |
| OBJECT_VERSION_NUMBER | SupervisorNamePEOObjectVersionNumber14 | — |
| PERSON_ID | AssignmentSupervisorPEOPersonId3 | — |
| PERSON_ID | SupervisorNamePEOPersonId4 | — |
| PRIMARY_FLAG | AssignmentSupervisorPEOPrimaryFlag1 | — |
| PRIMARY_FLAG | SupervisorNamePEOPrimaryFlag2 | — |
| SUP_ATTRIBUTE1 | AssignmentSupervisorPEOSupAttribute1 | — |
| SUP_ATTRIBUTE1 | SupervisorNamePEOSupAttribute110 | — |
| SUP_ATTRIBUTE10 | AssignmentSupervisorPEOSupAttribute10 | — |
| SUP_ATTRIBUTE10 | SupervisorNamePEOSupAttribute101 | — |
| SUP_ATTRIBUTE11 | AssignmentSupervisorPEOSupAttribute11 | — |
| SUP_ATTRIBUTE11 | SupervisorNamePEOSupAttribute111 | — |
| SUP_ATTRIBUTE12 | AssignmentSupervisorPEOSupAttribute12 | — |
| SUP_ATTRIBUTE12 | SupervisorNamePEOSupAttribute121 | — |
| SUP_ATTRIBUTE13 | AssignmentSupervisorPEOSupAttribute13 | — |
| SUP_ATTRIBUTE13 | SupervisorNamePEOSupAttribute131 | — |
| SUP_ATTRIBUTE14 | AssignmentSupervisorPEOSupAttribute14 | — |
| SUP_ATTRIBUTE14 | SupervisorNamePEOSupAttribute141 | — |
| SUP_ATTRIBUTE15 | AssignmentSupervisorPEOSupAttribute15 | — |
| SUP_ATTRIBUTE15 | SupervisorNamePEOSupAttribute151 | — |
| SUP_ATTRIBUTE16 | AssignmentSupervisorPEOSupAttribute16 | — |
| SUP_ATTRIBUTE16 | SupervisorNamePEOSupAttribute161 | — |
| SUP_ATTRIBUTE17 | AssignmentSupervisorPEOSupAttribute17 | — |
| SUP_ATTRIBUTE17 | SupervisorNamePEOSupAttribute171 | — |
| SUP_ATTRIBUTE18 | AssignmentSupervisorPEOSupAttribute18 | — |
| SUP_ATTRIBUTE18 | SupervisorNamePEOSupAttribute181 | — |
| SUP_ATTRIBUTE19 | AssignmentSupervisorPEOSupAttribute19 | — |
| SUP_ATTRIBUTE19 | SupervisorNamePEOSupAttribute191 | — |
| SUP_ATTRIBUTE2 | AssignmentSupervisorPEOSupAttribute2 | — |
| SUP_ATTRIBUTE2 | SupervisorNamePEOSupAttribute210 | — |
| SUP_ATTRIBUTE20 | AssignmentSupervisorPEOSupAttribute20 | — |
| SUP_ATTRIBUTE20 | SupervisorNamePEOSupAttribute201 | — |
| SUP_ATTRIBUTE21 | AssignmentSupervisorPEOSupAttribute21 | — |
| SUP_ATTRIBUTE21 | SupervisorNamePEOSupAttribute211 | — |
| SUP_ATTRIBUTE22 | AssignmentSupervisorPEOSupAttribute22 | — |
| SUP_ATTRIBUTE22 | SupervisorNamePEOSupAttribute221 | — |
| SUP_ATTRIBUTE23 | AssignmentSupervisorPEOSupAttribute23 | — |
| SUP_ATTRIBUTE23 | SupervisorNamePEOSupAttribute231 | — |
| SUP_ATTRIBUTE24 | AssignmentSupervisorPEOSupAttribute24 | — |
| SUP_ATTRIBUTE24 | SupervisorNamePEOSupAttribute241 | — |
| SUP_ATTRIBUTE25 | AssignmentSupervisorPEOSupAttribute25 | — |
| SUP_ATTRIBUTE25 | SupervisorNamePEOSupAttribute251 | — |
| SUP_ATTRIBUTE26 | AssignmentSupervisorPEOSupAttribute26 | — |
| SUP_ATTRIBUTE26 | SupervisorNamePEOSupAttribute261 | — |
| SUP_ATTRIBUTE27 | AssignmentSupervisorPEOSupAttribute27 | — |
| SUP_ATTRIBUTE27 | SupervisorNamePEOSupAttribute271 | — |
| SUP_ATTRIBUTE28 | AssignmentSupervisorPEOSupAttribute28 | — |
| SUP_ATTRIBUTE28 | SupervisorNamePEOSupAttribute281 | — |
| SUP_ATTRIBUTE29 | AssignmentSupervisorPEOSupAttribute29 | — |
| SUP_ATTRIBUTE29 | SupervisorNamePEOSupAttribute291 | — |
| SUP_ATTRIBUTE3 | AssignmentSupervisorPEOSupAttribute3 | — |
| SUP_ATTRIBUTE3 | SupervisorNamePEOSupAttribute31 | — |
| SUP_ATTRIBUTE30 | AssignmentSupervisorPEOSupAttribute30 | — |
| SUP_ATTRIBUTE30 | SupervisorNamePEOSupAttribute301 | — |
| SUP_ATTRIBUTE4 | AssignmentSupervisorPEOSupAttribute4 | — |
| SUP_ATTRIBUTE4 | SupervisorNamePEOSupAttribute41 | — |
| SUP_ATTRIBUTE5 | AssignmentSupervisorPEOSupAttribute5 | — |
| SUP_ATTRIBUTE5 | SupervisorNamePEOSupAttribute51 | — |
| SUP_ATTRIBUTE6 | AssignmentSupervisorPEOSupAttribute6 | — |
| SUP_ATTRIBUTE6 | SupervisorNamePEOSupAttribute61 | — |
| SUP_ATTRIBUTE7 | AssignmentSupervisorPEOSupAttribute7 | — |
| SUP_ATTRIBUTE7 | SupervisorNamePEOSupAttribute71 | — |
| SUP_ATTRIBUTE8 | AssignmentSupervisorPEOSupAttribute8 | — |
| SUP_ATTRIBUTE8 | SupervisorNamePEOSupAttribute81 | — |
| SUP_ATTRIBUTE9 | AssignmentSupervisorPEOSupAttribute9 | — |
| SUP_ATTRIBUTE9 | SupervisorNamePEOSupAttribute91 | — |
| SUP_ATTRIBUTE_CATEGORY | AssignmentSupervisorPEOSupAttributeCategory | — |
| SUP_ATTRIBUTE_CATEGORY | SupervisorNamePEOSupAttributeCategory1 | — |
| WORKING_PERCENTAGE | AssignmentSupervisorPEOWorkingPercentage | — |
| WORKING_PERCENTAGE | SupervisorNamePEOWorkingPercentage1 | — |

### [[scheduledaypvo|ScheduleDayPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_SUPERVISOR_ID | AssignmentSupervisorId | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_SUPERVISORS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentsupervisorsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
