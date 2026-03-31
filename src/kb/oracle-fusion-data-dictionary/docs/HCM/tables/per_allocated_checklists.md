---
id: DOC-HCM-619
doc_type: system-doc
title: "PER_ALLOCATED_CHECKLISTS — Checklists Alocados"
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
  - checklists
  - onboarding
aliases:
  - PER_ALLOCATED_CHECKLISTS
  - per_allocated_checklists
  - per-allocated-checklists
  - checklists-alocados
  - per-allocated-checkl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ALLOCATED_CHECKLISTS

## 📌 Visão Geral

Armazena os **checklists alocados** a colaboradores para processos específicos (onboarding, offboarding, transferência). Cada registro representa uma instância de checklist atribuída a uma pessoa.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding** — acompanhamento de tarefas para novos colaboradores.
- **Offboarding** — checklist de desligamento com itens obrigatórios.
- **Transferências** — tarefas necessárias para mudança de área.
- **Compliance** — garantia de que todos os itens obrigatórios foram completados.
- **Gestão de progresso** — acompanhamento do status de cada checklist.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOCATED_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único do checklist alocado | — | 🟢 95% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Template de checklist | PER_CHECKLISTS_B | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador associado | PER_ALL_PEOPLE_F | 🟢 90% |
| 4 | CHECKLIST_STATUS | VARCHAR2(30) | NULL | Status | Status do checklist (NOT_STARTED, IN_PROGRESS, COMPLETED) | — | 🟢 85% |
| 5 | ALLOCATION_DATE | DATE | NOT NULL | Período | Data de alocação do checklist | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (template de checklist)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador responsável pelo checklist)

### Tabelas-filha (FK de saída)
- [[per_allocated_checklists_tl]] — via `ALLOCATED_CHECKLIST_ID` (traduções do checklist alocado)
- [[per_allocated_tasks]] — via `ALLOCATED_CHECKLIST_ID` (tarefas alocadas)
- [[per_alloc_chklst_contacts]] — via `ALLOCATED_CHECKLIST_ID` (contatos do checklist alocado)
- [[per_alloc_chklst_contents]] — via `ALLOCATED_CHECKLIST_ID` (conteúdos do checklist alocado)

---

## 📎 Uso Típico

### Checklists em andamento de um colaborador
```sql
SELECT pac.ALLOCATED_CHECKLIST_ID, pac.CHECKLIST_STATUS, pac.ALLOCATION_DATE
FROM   PER_ALLOCATED_CHECKLISTS pac
WHERE  pac.PERSON_ID = :p_person_id
  AND  pac.CHECKLIST_STATUS != 'COMPLETED';
```

### Filtros comuns
- `CHECKLIST_STATUS = 'IN_PROGRESS'` — Checklists em andamento
- `ALLOCATION_DATE >= TRUNC(SYSDATE, 'MONTH')` — Alocados no mês corrente
---

## 🔒 Observações

- Cada checklist alocado é uma instância do template definido em PER_CHECKLISTS_B.
- O status do checklist é atualizado conforme as tarefas individuais são completadas.
- Contatos e conteúdos específicos podem ser adicionados a cada instância.
---

## 🔗 PVOs Relacionados

### [[allocatedchecklistspvo|AllocatedChecklistsPVO]] (HCM · BICC: 18/133)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DATE | AllocatedChecklistsPEOActionDate | ✅ |
| ACTION_OCCURRENCE_ID | AllocatedChecklistsPEOActionOccurrenceId | — |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistId | ✅ |
| ALLOCATION_DATE | AllocatedChecklistsPEOAllocationDate | ✅ |
| ALLOCATION_DETAILS | AllocatedChecklistsPEOAllocationDetails | ✅ |
| ALLOCATION_NOTIFIED_FLAG | AllocatedChecklistsPEOAllocationNotifiedFlag | — |
| ASSIGNMENT_ID | AllocatedChecklistsPEOAssignmentId | — |
| ATTRIBUTE1 | AllocatedChecklistsPEOAttribute1 | — |
| ATTRIBUTE10 | AllocatedChecklistsPEOAttribute10 | — |
| ATTRIBUTE11 | AllocatedChecklistsPEOAttribute11 | — |
| ATTRIBUTE12 | AllocatedChecklistsPEOAttribute12 | — |
| ATTRIBUTE13 | AllocatedChecklistsPEOAttribute13 | — |
| ATTRIBUTE14 | AllocatedChecklistsPEOAttribute14 | — |
| ATTRIBUTE15 | AllocatedChecklistsPEOAttribute15 | — |
| ATTRIBUTE16 | AllocatedChecklistsPEOAttribute16 | — |
| ATTRIBUTE17 | AllocatedChecklistsPEOAttribute17 | — |
| ATTRIBUTE18 | AllocatedChecklistsPEOAttribute18 | — |
| ATTRIBUTE19 | AllocatedChecklistsPEOAttribute19 | — |
| ATTRIBUTE2 | AllocatedChecklistsPEOAttribute2 | — |
| ATTRIBUTE20 | AllocatedChecklistsPEOAttribute20 | — |
| ATTRIBUTE21 | AllocatedChecklistsPEOAttribute21 | — |
| ATTRIBUTE22 | AllocatedChecklistsPEOAttribute22 | — |
| ATTRIBUTE23 | AllocatedChecklistsPEOAttribute23 | — |
| ATTRIBUTE24 | AllocatedChecklistsPEOAttribute24 | — |
| ATTRIBUTE25 | AllocatedChecklistsPEOAttribute25 | — |
| ATTRIBUTE26 | AllocatedChecklistsPEOAttribute26 | — |
| ATTRIBUTE27 | AllocatedChecklistsPEOAttribute27 | — |
| ATTRIBUTE28 | AllocatedChecklistsPEOAttribute28 | — |
| ATTRIBUTE29 | AllocatedChecklistsPEOAttribute29 | — |
| ATTRIBUTE3 | AllocatedChecklistsPEOAttribute3 | — |
| ATTRIBUTE30 | AllocatedChecklistsPEOAttribute30 | — |
| ATTRIBUTE4 | AllocatedChecklistsPEOAttribute4 | — |
| ATTRIBUTE5 | AllocatedChecklistsPEOAttribute5 | — |
| ATTRIBUTE6 | AllocatedChecklistsPEOAttribute6 | — |
| ATTRIBUTE7 | AllocatedChecklistsPEOAttribute7 | — |
| ATTRIBUTE8 | AllocatedChecklistsPEOAttribute8 | — |
| ATTRIBUTE9 | AllocatedChecklistsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | AllocatedChecklistsPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | AllocatedChecklistsPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | AllocatedChecklistsPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | AllocatedChecklistsPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | AllocatedChecklistsPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | AllocatedChecklistsPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | AllocatedChecklistsPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | AllocatedChecklistsPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | AllocatedChecklistsPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | AllocatedChecklistsPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | AllocatedChecklistsPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | AllocatedChecklistsPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | AllocatedChecklistsPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | AllocatedChecklistsPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | AllocatedChecklistsPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | AllocatedChecklistsPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AllocatedChecklistsPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AllocatedChecklistsPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AllocatedChecklistsPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AllocatedChecklistsPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AllocatedChecklistsPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AllocatedChecklistsPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AllocatedChecklistsPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AllocatedChecklistsPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AllocatedChecklistsPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AllocatedChecklistsPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AllocatedChecklistsPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AllocatedChecklistsPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AllocatedChecklistsPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AllocatedChecklistsPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AllocatedChecklistsPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AllocatedChecklistsPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AllocatedChecklistsPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AllocatedChecklistsPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AllocatedChecklistsPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AllocatedChecklistsPEOAttributeNumber9 | — |
| BACKGROUND_IMAGE_URL | AllocatedChecklistsPEOBackgroundImageUrl | — |
| BACKGROUND_THUMBNAIL_URL | AllocatedChecklistsPEOBackgroundThumbnailUrl | — |
| CHECKLIST_ACTION_ID | AllocatedChecklistsPEOChecklistActionId | — |
| CHECKLIST_ACTION_OCCURRENCE_ID | AllocatedChecklistsPEOChecklistActionOccurrenceId | — |
| CHECKLIST_CATEGORY | AllocatedChecklistsPEOChecklistCategory | ✅ |
| CHECKLIST_ID | AllocatedChecklistsPEOChecklistId | ✅ |
| CHECKLIST_INSTANCE | AllocatedChecklistsPEOChecklistInstance | ✅ |
| CHECKLIST_STATUS | AllocatedChecklistsPEOChecklistStatus | ✅ |
| COMBINED_TASK_TEMPLATE_ID | AllocatedChecklistsPEOCombinedTaskTemplateId | — |
| COMPLETED_ON | AllocatedChecklistsPEOCompletedOn | ✅ |
| COMPLETION_DATE | AllocatedChecklistsPEOCompletionDate | ✅ |
| COMPLETION_OFFSET_DAYS | AllocatedChecklistsPEOCompletionOffsetDays | ✅ |
| CREATED_BY | AllocatedChecklistsPEOCreatedBy | ✅ |
| CREATION_DATE | AllocatedChecklistsPEOCreationDate | ✅ |
| DEF_COMPLETION_DATE | AllocatedChecklistsPEODefCompletionDate | — |
| ENTERPRISE_ID | AllocatedChecklistsPEOEnterpriseId | — |
| EVENT_DATE | AllocatedChecklistsPEOEventDate | ✅ |
| INFORMATION1 | AllocatedChecklistsPEOInformation1 | — |
| INFORMATION10 | AllocatedChecklistsPEOInformation10 | — |
| INFORMATION11 | AllocatedChecklistsPEOInformation11 | — |
| INFORMATION12 | AllocatedChecklistsPEOInformation12 | — |
| INFORMATION13 | AllocatedChecklistsPEOInformation13 | — |
| INFORMATION14 | AllocatedChecklistsPEOInformation14 | — |
| INFORMATION15 | AllocatedChecklistsPEOInformation15 | — |
| INFORMATION16 | AllocatedChecklistsPEOInformation16 | — |
| INFORMATION17 | AllocatedChecklistsPEOInformation17 | — |
| INFORMATION18 | AllocatedChecklistsPEOInformation18 | — |
| INFORMATION19 | AllocatedChecklistsPEOInformation19 | — |
| INFORMATION2 | AllocatedChecklistsPEOInformation2 | — |
| INFORMATION20 | AllocatedChecklistsPEOInformation20 | — |
| INFORMATION21 | AllocatedChecklistsPEOInformation21 | — |
| INFORMATION22 | AllocatedChecklistsPEOInformation22 | — |
| INFORMATION23 | AllocatedChecklistsPEOInformation23 | — |
| INFORMATION24 | AllocatedChecklistsPEOInformation24 | — |
| INFORMATION25 | AllocatedChecklistsPEOInformation25 | — |
| INFORMATION26 | AllocatedChecklistsPEOInformation26 | — |
| INFORMATION27 | AllocatedChecklistsPEOInformation27 | — |
| INFORMATION28 | AllocatedChecklistsPEOInformation28 | — |
| INFORMATION29 | AllocatedChecklistsPEOInformation29 | — |
| INFORMATION3 | AllocatedChecklistsPEOInformation3 | — |
| INFORMATION30 | AllocatedChecklistsPEOInformation30 | — |
| INFORMATION4 | AllocatedChecklistsPEOInformation4 | — |
| INFORMATION5 | AllocatedChecklistsPEOInformation5 | — |
| INFORMATION6 | AllocatedChecklistsPEOInformation6 | — |
| INFORMATION7 | AllocatedChecklistsPEOInformation7 | — |
| INFORMATION8 | AllocatedChecklistsPEOInformation8 | — |
| INFORMATION9 | AllocatedChecklistsPEOInformation9 | — |
| INFORMATION_CATEGORY | AllocatedChecklistsPEOInformationCategory | — |
| INITIATOR_PERSON_ID | AllocatedChecklistsPEOInitiatorPersonId | — |
| INITIATOR_USER | AllocatedChecklistsPEOInitiatorUser | — |
| LAST_UPDATE_DATE | AllocatedChecklistsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AllocatedChecklistsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AllocatedChecklistsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | AllocatedChecklistsPEOLegislationCode | ✅ |
| OBJECT_ID | AllocatedChecklistsPEOObjectId | — |
| OBJECT_VERSION_NUMBER | AllocatedChecklistsPEOObjectVersionNumber | — |
| PERIOD_OF_SERVICE_ID | AllocatedChecklistsPEOPeriodOfServiceId | — |
| PERSON_ID | AllocatedChecklistsPEOPersonId | — |
| PROCESSING_MODE | AllocatedChecklistsPEOProcessingMode | — |
| SELF_ASSIGNED_FLAG | AllocatedChecklistsPEOSelfAssignedFlag | — |

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 18/119)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DATE | AllocatedChecklistsPEOActionDate | ✅ |
| ALLOCATED_CHECKLIST_ID | AllocatedChecklistsPEOAllocatedChecklistId | ✅ |
| ALLOCATION_DATE | AllocatedChecklistsPEOAllocationDate | ✅ |
| ALLOCATION_DETAILS | AllocatedChecklistsPEOAllocationDetails | ✅ |
| ASSIGNMENT_ID | AllocatedChecklistsPEOAssignmentId | — |
| ATTRIBUTE1 | AllocatedChecklistsPEOAttribute1 | — |
| ATTRIBUTE10 | AllocatedChecklistsPEOAttribute10 | — |
| ATTRIBUTE11 | AllocatedChecklistsPEOAttribute11 | — |
| ATTRIBUTE12 | AllocatedChecklistsPEOAttribute12 | — |
| ATTRIBUTE13 | AllocatedChecklistsPEOAttribute13 | — |
| ATTRIBUTE14 | AllocatedChecklistsPEOAttribute14 | — |
| ATTRIBUTE15 | AllocatedChecklistsPEOAttribute15 | — |
| ATTRIBUTE16 | AllocatedChecklistsPEOAttribute16 | — |
| ATTRIBUTE17 | AllocatedChecklistsPEOAttribute17 | — |
| ATTRIBUTE18 | AllocatedChecklistsPEOAttribute18 | — |
| ATTRIBUTE19 | AllocatedChecklistsPEOAttribute19 | — |
| ATTRIBUTE2 | AllocatedChecklistsPEOAttribute2 | — |
| ATTRIBUTE20 | AllocatedChecklistsPEOAttribute20 | — |
| ATTRIBUTE21 | AllocatedChecklistsPEOAttribute21 | — |
| ATTRIBUTE22 | AllocatedChecklistsPEOAttribute22 | — |
| ATTRIBUTE23 | AllocatedChecklistsPEOAttribute23 | — |
| ATTRIBUTE24 | AllocatedChecklistsPEOAttribute24 | — |
| ATTRIBUTE25 | AllocatedChecklistsPEOAttribute25 | — |
| ATTRIBUTE26 | AllocatedChecklistsPEOAttribute26 | — |
| ATTRIBUTE27 | AllocatedChecklistsPEOAttribute27 | — |
| ATTRIBUTE28 | AllocatedChecklistsPEOAttribute28 | — |
| ATTRIBUTE29 | AllocatedChecklistsPEOAttribute29 | — |
| ATTRIBUTE3 | AllocatedChecklistsPEOAttribute3 | — |
| ATTRIBUTE30 | AllocatedChecklistsPEOAttribute30 | — |
| ATTRIBUTE4 | AllocatedChecklistsPEOAttribute4 | — |
| ATTRIBUTE5 | AllocatedChecklistsPEOAttribute5 | — |
| ATTRIBUTE6 | AllocatedChecklistsPEOAttribute6 | — |
| ATTRIBUTE7 | AllocatedChecklistsPEOAttribute7 | — |
| ATTRIBUTE8 | AllocatedChecklistsPEOAttribute8 | — |
| ATTRIBUTE9 | AllocatedChecklistsPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | AllocatedChecklistsPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | AllocatedChecklistsPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | AllocatedChecklistsPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | AllocatedChecklistsPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | AllocatedChecklistsPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | AllocatedChecklistsPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | AllocatedChecklistsPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | AllocatedChecklistsPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | AllocatedChecklistsPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | AllocatedChecklistsPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | AllocatedChecklistsPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | AllocatedChecklistsPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | AllocatedChecklistsPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | AllocatedChecklistsPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | AllocatedChecklistsPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | AllocatedChecklistsPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AllocatedChecklistsPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AllocatedChecklistsPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AllocatedChecklistsPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AllocatedChecklistsPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AllocatedChecklistsPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AllocatedChecklistsPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AllocatedChecklistsPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AllocatedChecklistsPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AllocatedChecklistsPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AllocatedChecklistsPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AllocatedChecklistsPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AllocatedChecklistsPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AllocatedChecklistsPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AllocatedChecklistsPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AllocatedChecklistsPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AllocatedChecklistsPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AllocatedChecklistsPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AllocatedChecklistsPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AllocatedChecklistsPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AllocatedChecklistsPEOAttributeNumber9 | — |
| CHECKLIST_CATEGORY | AllocatedChecklistsPEOChecklistCategory | ✅ |
| CHECKLIST_ID | AllocatedChecklistsPEOChecklistId | ✅ |
| CHECKLIST_INSTANCE | AllocatedChecklistsPEOChecklistInstance | ✅ |
| CHECKLIST_STATUS | AllocatedChecklistsPEOChecklistStatus | ✅ |
| COMPLETED_ON | AllocatedChecklistsPEOCompletedOn | ✅ |
| COMPLETION_DATE | AllocatedChecklistsPEOCompletionDate | ✅ |
| COMPLETION_OFFSET_DAYS | AllocatedChecklistsPEOCompletionOffsetDays | ✅ |
| CREATED_BY | AllocatedChecklistsPEOCreatedBy | ✅ |
| CREATION_DATE | AllocatedChecklistsPEOCreationDate | ✅ |
| ENTERPRISE_ID | AllocatedChecklistsPEOEnterpriseId | — |
| EVENT_DATE | AllocatedChecklistsPEOEventDate | ✅ |
| INFORMATION1 | AllocatedChecklistsPEOInformation1 | — |
| INFORMATION10 | AllocatedChecklistsPEOInformation10 | — |
| INFORMATION11 | AllocatedChecklistsPEOInformation11 | — |
| INFORMATION12 | AllocatedChecklistsPEOInformation12 | — |
| INFORMATION13 | AllocatedChecklistsPEOInformation13 | — |
| INFORMATION14 | AllocatedChecklistsPEOInformation14 | — |
| INFORMATION15 | AllocatedChecklistsPEOInformation15 | — |
| INFORMATION16 | AllocatedChecklistsPEOInformation16 | — |
| INFORMATION17 | AllocatedChecklistsPEOInformation17 | — |
| INFORMATION18 | AllocatedChecklistsPEOInformation18 | — |
| INFORMATION19 | AllocatedChecklistsPEOInformation19 | — |
| INFORMATION2 | AllocatedChecklistsPEOInformation2 | — |
| INFORMATION20 | AllocatedChecklistsPEOInformation20 | — |
| INFORMATION21 | AllocatedChecklistsPEOInformation21 | — |
| INFORMATION22 | AllocatedChecklistsPEOInformation22 | — |
| INFORMATION23 | AllocatedChecklistsPEOInformation23 | — |
| INFORMATION24 | AllocatedChecklistsPEOInformation24 | — |
| INFORMATION25 | AllocatedChecklistsPEOInformation25 | — |
| INFORMATION26 | AllocatedChecklistsPEOInformation26 | — |
| INFORMATION27 | AllocatedChecklistsPEOInformation27 | — |
| INFORMATION28 | AllocatedChecklistsPEOInformation28 | — |
| INFORMATION29 | AllocatedChecklistsPEOInformation29 | — |
| INFORMATION3 | AllocatedChecklistsPEOInformation3 | — |
| INFORMATION30 | AllocatedChecklistsPEOInformation30 | — |
| INFORMATION4 | AllocatedChecklistsPEOInformation4 | — |
| INFORMATION5 | AllocatedChecklistsPEOInformation5 | — |
| INFORMATION6 | AllocatedChecklistsPEOInformation6 | — |
| INFORMATION7 | AllocatedChecklistsPEOInformation7 | — |
| INFORMATION8 | AllocatedChecklistsPEOInformation8 | — |
| INFORMATION9 | AllocatedChecklistsPEOInformation9 | — |
| INFORMATION_CATEGORY | AllocatedChecklistsPEOInformationCategory | — |
| LAST_UPDATE_DATE | AllocatedChecklistsPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AllocatedChecklistsPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | AllocatedChecklistsPEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | AllocatedChecklistsPEOLegislationCode | ✅ |
| OBJECT_VERSION_NUMBER | AllocatedChecklistsPEOObjectVersionNumber | — |
| PERSON_ID | AllocatedChecklistsPEOPersonId | — |

---

## 📚 Referências

- [Oracle Docs — PER_ALLOCATED_CHECKLISTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perallocatedchecklists.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
