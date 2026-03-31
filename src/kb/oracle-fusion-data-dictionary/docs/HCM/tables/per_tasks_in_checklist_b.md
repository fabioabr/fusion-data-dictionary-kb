---
id: DOC-HCM-713
doc_type: system-doc
title: "PER_TASKS_IN_CHECKLIST_B — Tarefas em Checklist (Base)"
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
  - checklist
  - tarefas-checklist
  - onboarding
aliases:
  - PER_TASKS_IN_CHECKLIST_B
  - per_tasks_in_checklist_b
  - per-tasks-in-checklist-b
  - tarefas-em-checklist-base
  - tasks-in-checklist-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_TASKS_IN_CHECKLIST_B

## Visão Geral

Armazena as **tarefas base** que compõem um checklist de onboarding, offboarding ou qualquer outro processo de RH estruturado em etapas. Tabela base (_B), independente de idioma.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Onboarding/Offboarding** — define as tarefas obrigatórias que o colaborador ou gestor deve completar.
- **Checklists operacionais** — cada item do checklist é uma tarefa rastreável.
- **Compliance** — garante que todas as etapas foram cumpridas antes da conclusão do processo.
- **Automação de processos** — tarefas podem disparar notificações e dependências.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_IN_CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa no checklist | — | 🟢 90% |
| 2 | CHECKLIST_ID | NUMBER(18) | NOT NULL | FK | Checklist ao qual a tarefa pertence | PER_CHECKLISTS_B | 🟢 85% |
| 3 | TASK_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome interno da tarefa | — | 🟡 80% |
| 4 | TASK_TYPE_CD | VARCHAR2(30) | NULL | Classificação | Tipo/categoria da tarefa | — | 🟡 75% |
| 5 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem de exibição da tarefa no checklist | — | 🟡 80% |
| 6 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Indica se a tarefa é obrigatória (Y/N) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_checklists_b]] — via `CHECKLIST_ID` (checklist pai)

### Tabelas-filha (FK de saída)
- [[per_tasks_in_checklist_tl]] — via `TASK_IN_CHECKLIST_ID` (traduções da tarefa)
- [[per_task_dependencies]] — via `TASK_IN_CHECKLIST_ID` (dependências entre tarefas)
- [[per_task_notifications]] — via `TASK_IN_CHECKLIST_ID` (notificações associadas)

---

## Uso Típico

### Tarefas de um checklist
```sql
SELECT tcb.TASK_NAME, tcb.SEQUENCE, tcb.MANDATORY_FLAG
FROM   PER_TASKS_IN_CHECKLIST_B tcb
JOIN   PER_CHECKLISTS_B cb ON tcb.CHECKLIST_ID = cb.CHECKLIST_ID
WHERE  cb.CHECKLIST_ID = :p_checklist_id
ORDER BY tcb.SEQUENCE;
```

### Filtros comuns
- `CHECKLIST_ID = :p_checklist_id` — Tarefas de um checklist específico
- `MANDATORY_FLAG = 'Y'` — Apenas tarefas obrigatórias

---

## Observações

- Tabela base (_B) — contém dados independentes de idioma.
- Cada tarefa pode ter dependências definidas em PER_TASK_DEPENDENCIES.
- Traduções disponíveis na tabela PER_TASKS_IN_CHECKLIST_TL.
- O campo SEQUENCE determina a ordem de apresentação ao usuário.

---

## Referências

- [Oracle Docs — PER_TASKS_IN_CHECKLIST_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pertasksinchecklist.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 23/136)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_TYPE | ChecklistTaskTemplatePEOActionType | ✅ |
| ACTIVE_INACTIVE_FLAG | ChecklistTaskTemplatePEOActiveInactiveFlag | ✅ |
| ALLOW_ALLC_TASK_CREATE | ChecklistTaskTemplatePEOAllowAllcTaskCreate | — |
| ALLOW_ALLC_TASK_DELETE | ChecklistTaskTemplatePEOAllowAllcTaskDelete | — |
| ALLOW_ALLC_TASK_UPDATE | ChecklistTaskTemplatePEOAllowAllcTaskUpdate | — |
| AME_ATTRIBUTE_IDENTIFIER | ChecklistTaskTemplatePEOAmeAttributeIdentifier | — |
| ATTRIBUTE1 | ChecklistTaskTemplatePEOAttribute1 | — |
| ATTRIBUTE10 | ChecklistTaskTemplatePEOAttribute10 | — |
| ATTRIBUTE11 | ChecklistTaskTemplatePEOAttribute11 | — |
| ATTRIBUTE12 | ChecklistTaskTemplatePEOAttribute12 | — |
| ATTRIBUTE13 | ChecklistTaskTemplatePEOAttribute13 | — |
| ATTRIBUTE14 | ChecklistTaskTemplatePEOAttribute14 | — |
| ATTRIBUTE15 | ChecklistTaskTemplatePEOAttribute15 | — |
| ATTRIBUTE16 | ChecklistTaskTemplatePEOAttribute16 | — |
| ATTRIBUTE17 | ChecklistTaskTemplatePEOAttribute17 | — |
| ATTRIBUTE18 | ChecklistTaskTemplatePEOAttribute18 | — |
| ATTRIBUTE19 | ChecklistTaskTemplatePEOAttribute19 | — |
| ATTRIBUTE2 | ChecklistTaskTemplatePEOAttribute2 | — |
| ATTRIBUTE20 | ChecklistTaskTemplatePEOAttribute20 | — |
| ATTRIBUTE21 | ChecklistTaskTemplatePEOAttribute21 | — |
| ATTRIBUTE22 | ChecklistTaskTemplatePEOAttribute22 | — |
| ATTRIBUTE23 | ChecklistTaskTemplatePEOAttribute23 | — |
| ATTRIBUTE24 | ChecklistTaskTemplatePEOAttribute24 | — |
| ATTRIBUTE25 | ChecklistTaskTemplatePEOAttribute25 | — |
| ATTRIBUTE26 | ChecklistTaskTemplatePEOAttribute26 | — |
| ATTRIBUTE27 | ChecklistTaskTemplatePEOAttribute27 | — |
| ATTRIBUTE28 | ChecklistTaskTemplatePEOAttribute28 | — |
| ATTRIBUTE29 | ChecklistTaskTemplatePEOAttribute29 | — |
| ATTRIBUTE3 | ChecklistTaskTemplatePEOAttribute3 | — |
| ATTRIBUTE30 | ChecklistTaskTemplatePEOAttribute30 | — |
| ATTRIBUTE4 | ChecklistTaskTemplatePEOAttribute4 | — |
| ATTRIBUTE5 | ChecklistTaskTemplatePEOAttribute5 | — |
| ATTRIBUTE6 | ChecklistTaskTemplatePEOAttribute6 | — |
| ATTRIBUTE7 | ChecklistTaskTemplatePEOAttribute7 | — |
| ATTRIBUTE8 | ChecklistTaskTemplatePEOAttribute8 | — |
| ATTRIBUTE9 | ChecklistTaskTemplatePEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | ChecklistTaskTemplatePEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | ChecklistTaskTemplatePEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | ChecklistTaskTemplatePEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | ChecklistTaskTemplatePEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | ChecklistTaskTemplatePEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | ChecklistTaskTemplatePEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | ChecklistTaskTemplatePEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | ChecklistTaskTemplatePEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | ChecklistTaskTemplatePEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ChecklistTaskTemplatePEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ChecklistTaskTemplatePEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ChecklistTaskTemplatePEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | ChecklistTaskTemplatePEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | ChecklistTaskTemplatePEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | ChecklistTaskTemplatePEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | ChecklistTaskTemplatePEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | ChecklistTaskTemplatePEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | ChecklistTaskTemplatePEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | ChecklistTaskTemplatePEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | ChecklistTaskTemplatePEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | ChecklistTaskTemplatePEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | ChecklistTaskTemplatePEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | ChecklistTaskTemplatePEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | ChecklistTaskTemplatePEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | ChecklistTaskTemplatePEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | ChecklistTaskTemplatePEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | ChecklistTaskTemplatePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ChecklistTaskTemplatePEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | ChecklistTaskTemplatePEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | ChecklistTaskTemplatePEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ChecklistTaskTemplatePEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ChecklistTaskTemplatePEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | ChecklistTaskTemplatePEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | ChecklistTaskTemplatePEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | ChecklistTaskTemplatePEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | ChecklistTaskTemplatePEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | ChecklistTaskTemplatePEOBusinessGroupId | — |
| CHECKLIST_ID | ChecklistTaskTemplatePEOChecklistId | ✅ |
| CREATED_BY | ChecklistTaskTemplatePEOCreatedBy | ✅ |
| CREATION_DATE | ChecklistTaskTemplatePEOCreationDate | ✅ |
| DOCUMENT_TYPE_ID | ChecklistTaskTemplatePEODocumentTypeId | ✅ |
| ELIGIBILITY_OBJECT_ID | ChecklistTaskTemplatePEOEligibilityObjectId | — |
| ELIGIBILITY_PROFILE_ID | ChecklistTaskTemplatePEOEligibilityProfileId | ✅ |
| ESIGN_TYPE | ChecklistTaskTemplatePEOEsignType | ✅ |
| EXPIRY_AFTER_DAYS | ChecklistTaskTemplatePEOExpiryAfterDays | — |
| GENERATE_ATOM_FEED | ChecklistTaskTemplatePEOGenerateAtomFeed | — |
| INFORMATION1 | ChecklistTaskTemplatePEOInformation1 | — |
| INFORMATION10 | ChecklistTaskTemplatePEOInformation10 | — |
| INFORMATION11 | ChecklistTaskTemplatePEOInformation11 | — |
| INFORMATION12 | ChecklistTaskTemplatePEOInformation12 | — |
| INFORMATION13 | ChecklistTaskTemplatePEOInformation13 | — |
| INFORMATION14 | ChecklistTaskTemplatePEOInformation14 | — |
| INFORMATION15 | ChecklistTaskTemplatePEOInformation15 | — |
| INFORMATION16 | ChecklistTaskTemplatePEOInformation16 | — |
| INFORMATION17 | ChecklistTaskTemplatePEOInformation17 | — |
| INFORMATION18 | ChecklistTaskTemplatePEOInformation18 | — |
| INFORMATION19 | ChecklistTaskTemplatePEOInformation19 | — |
| INFORMATION2 | ChecklistTaskTemplatePEOInformation2 | — |
| INFORMATION20 | ChecklistTaskTemplatePEOInformation20 | — |
| INFORMATION21 | ChecklistTaskTemplatePEOInformation21 | — |
| INFORMATION22 | ChecklistTaskTemplatePEOInformation22 | — |
| INFORMATION23 | ChecklistTaskTemplatePEOInformation23 | — |
| INFORMATION24 | ChecklistTaskTemplatePEOInformation24 | — |
| INFORMATION25 | ChecklistTaskTemplatePEOInformation25 | — |
| INFORMATION26 | ChecklistTaskTemplatePEOInformation26 | — |
| INFORMATION27 | ChecklistTaskTemplatePEOInformation27 | — |
| INFORMATION28 | ChecklistTaskTemplatePEOInformation28 | — |
| INFORMATION29 | ChecklistTaskTemplatePEOInformation29 | — |
| INFORMATION3 | ChecklistTaskTemplatePEOInformation3 | — |
| INFORMATION30 | ChecklistTaskTemplatePEOInformation30 | — |
| INFORMATION4 | ChecklistTaskTemplatePEOInformation4 | — |
| INFORMATION5 | ChecklistTaskTemplatePEOInformation5 | — |
| INFORMATION6 | ChecklistTaskTemplatePEOInformation6 | — |
| INFORMATION7 | ChecklistTaskTemplatePEOInformation7 | — |
| INFORMATION8 | ChecklistTaskTemplatePEOInformation8 | — |
| INFORMATION9 | ChecklistTaskTemplatePEOInformation9 | — |
| INFORMATION_CATEGORY | ChecklistTaskTemplatePEOInformationCategory | — |
| LAST_UPDATE_DATE | ChecklistTaskTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ChecklistTaskTemplatePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ChecklistTaskTemplatePEOLastUpdatedBy | ✅ |
| MANDATORY_FLAG | ChecklistTaskTemplatePEOMandatoryFlag | ✅ |
| MEETING_TIME | ChecklistTaskTemplatePEOMeetingTime | — |
| OBJECT_VERSION_NUMBER | ChecklistTaskTemplatePEOObjectVersionNumber | — |
| OWNER_RESP_TYPE | ChecklistTaskTemplatePEOOwnerRespType | — |
| QUESTIONNAIRE_ID | ChecklistTaskTemplatePEOQuestionnaireId | ✅ |
| REMINDER_RECURRENCE | ChecklistTaskTemplatePEOReminderRecurrence | — |
| REMINDER_RELATIVE_TO | ChecklistTaskTemplatePEOReminderRelativeTo | — |
| REPORT_PATH | ChecklistTaskTemplatePEOReportPath | ✅ |
| RESPONSIBILITY_TYPE | ChecklistTaskTemplatePEOResponsibilityType | ✅ |
| SIGN_TEMPLATE | ChecklistTaskTemplatePEOSignTemplate | ✅ |
| TARGET_DURATION | ChecklistTaskTemplatePEOTargetDuration | ✅ |
| TARGET_DURATION_UOM | ChecklistTaskTemplatePEOTargetDurationUom | ✅ |
| TASK_ACTION_CODE | ChecklistTaskTemplatePEOTaskActionCode | — |
| TASK_CATEGORY | ChecklistTaskTemplatePEOTaskCategory | ✅ |
| TASK_CONFIGURATION | ChecklistTaskTemplatePEOTaskConfiguration | — |
| TASK_DELAY_DURATION | ChecklistTaskTemplatePEOTaskDelayDuration | ✅ |
| TASK_DELAY_DURATION_UOM | ChecklistTaskTemplatePEOTaskDelayDurationUom | ✅ |
| TASK_IN_CHECKLIST_CODE | ChecklistTaskTemplatePEOTaskInChecklistCode | ✅ |
| TASK_IN_CHECKLIST_ID | TaskInChecklistId | ✅ |
| TASK_SEQUENCE | ChecklistTaskTemplatePEOTaskSequence | — |
