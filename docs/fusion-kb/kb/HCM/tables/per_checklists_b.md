---
id: DOC-HCM-639
doc_type: system-doc
title: "PER_CHECKLISTS_B — Templates de Checklist (Base)"
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
  - templates
aliases:
  - PER_CHECKLISTS_B
  - per_checklists_b
  - per-checklists-b
  - templates-de-checklist-(base)
  - per-checklists-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CHECKLISTS_B

## 📌 Visão Geral

Armazena os **templates (modelos) de checklist** disponíveis no sistema. Define a estrutura base de checklists para processos como onboarding, offboarding e transferências.

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** — contém os dados principais do registro, independente de idioma.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Padronização** — define templates reutilizáveis de checklist.
- **Onboarding/Offboarding** — modelos específicos para cada processo de RH.
- **Configuração** — define a estrutura, tarefas e regras de cada checklist.
- **Compliance** — garante que processos obrigatórios sejam seguidos consistentemente.
- **Automação** — base para alocação automática de checklists em eventos de RH.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CHECKLIST_ID | NUMBER(18) | NOT NULL | PK | Identificador único do template de checklist | — | 🟢 95% |
| 2 | CHECKLIST_CATEGORY | VARCHAR2(30) | NOT NULL | Classificação | Categoria (ONBOARDING, OFFBOARDING, TRANSFER) | — | 🟢 90% |
| 3 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se o template está ativo (Y/N) | — | 🟢 85% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 85% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 7 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 8 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 9 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de templates de checklist.

### Tabelas-filha (FK de saída)
- [[per_checklists_tl]] — via `CHECKLIST_ID` (traduções do template de checklist)
- [[per_checklist_contacts]] — via `CHECKLIST_ID` (contatos do template)
- [[per_checklist_contents]] — via `CHECKLIST_ID` (conteúdos do template)
- [[per_allocated_checklists]] — via `CHECKLIST_ID` (instâncias alocadas)

---

## 📎 Uso Típico

### Templates de checklist ativos
```sql
SELECT pcb.CHECKLIST_ID, pcb.CHECKLIST_CATEGORY, pcb.LEGISLATION_CODE
FROM   PER_CHECKLISTS_B pcb
WHERE  pcb.ACTIVE_FLAG = 'Y'
ORDER BY pcb.CHECKLIST_CATEGORY;
```

### Filtros comuns
- `CHECKLIST_CATEGORY = 'ONBOARDING'` — Checklists de onboarding
- `ACTIVE_FLAG = 'Y'` — Templates ativos
---

## 🔒 Observações

- Tabela base (_B) — textos traduzidos ficam na tabela _TL correspondente.
- Cada template define a estrutura do checklist — as instâncias ficam em PER_ALLOCATED_CHECKLISTS.
- Templates podem ser específicos por legislação (país).
- A categoria determina quando o checklist é acionado automaticamente.
---

## 🔗 PVOs Relacionados

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 16/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_INACTIVE_FLAG | ChecklistTemplatePEOActiveInactiveFlag | ✅ |
| ALLOCATED_ON | ChecklistTemplatePEOAllocatedOn | ✅ |
| CHECKLIST_CATEGORY | ChecklistTemplatePEOChecklistCategory | ✅ |
| CHECKLIST_CODE | ChecklistTemplatePEOChecklistCode | ✅ |
| CHECKLIST_ID | ChecklistTemplatePEOChecklistId | — |
| COMPLETED_ON | ChecklistTemplatePEOCompletedOn | ✅ |
| COMPLETION_OFFSET_DAYS | ChecklistTemplatePEOCompletionOffsetDays | ✅ |
| CREATED_BY | ChecklistTemplatePEOCreatedBy | ✅ |
| CREATION_DATE | ChecklistTemplatePEOCreationDate | ✅ |
| DATE_FROM | ChecklistTemplatePEODateFrom | ✅ |
| DATE_TO | ChecklistTemplatePEODateTo | ✅ |
| ELIGIBILITY_PROFILE_ID | ChecklistTemplatePEOEligibilityProfileId | ✅ |
| EVENT_REASON_ID | ChecklistTemplatePEOEventReasonId | — |
| LAST_UPDATE_DATE | ChecklistTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ChecklistTemplatePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ChecklistTemplatePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ChecklistTemplatePEOLegislationCode | ✅ |
| OFFSET_DAYS | ChecklistTemplatePEOOffsetDays | ✅ |

### [[checklisttemplatepvo|ChecklistTemplatePVO]] (HCM · BICC: 17/122)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_INACTIVE_FLAG | ChecklistTemplatePEOActiveInactiveFlag | ✅ |
| ALLOCATED_ON | ChecklistTemplatePEOAllocatedOn | ✅ |
| ALLOW_ALLOCATION_CREATE | ChecklistTemplatePEOAllowAllocationCreate | — |
| ALLOW_ALLOCATION_DELETE | ChecklistTemplatePEOAllowAllocationDelete | — |
| ALLOW_ALLOCATION_UPDATE | ChecklistTemplatePEOAllowAllocationUpdate | — |
| ATTRIBUTE1 | ChecklistTemplatePEOAttribute1 | — |
| ATTRIBUTE10 | ChecklistTemplatePEOAttribute10 | — |
| ATTRIBUTE11 | ChecklistTemplatePEOAttribute11 | — |
| ATTRIBUTE12 | ChecklistTemplatePEOAttribute12 | — |
| ATTRIBUTE13 | ChecklistTemplatePEOAttribute13 | — |
| ATTRIBUTE14 | ChecklistTemplatePEOAttribute14 | — |
| ATTRIBUTE15 | ChecklistTemplatePEOAttribute15 | — |
| ATTRIBUTE16 | ChecklistTemplatePEOAttribute16 | — |
| ATTRIBUTE17 | ChecklistTemplatePEOAttribute17 | — |
| ATTRIBUTE18 | ChecklistTemplatePEOAttribute18 | — |
| ATTRIBUTE19 | ChecklistTemplatePEOAttribute19 | — |
| ATTRIBUTE2 | ChecklistTemplatePEOAttribute2 | — |
| ATTRIBUTE20 | ChecklistTemplatePEOAttribute20 | — |
| ATTRIBUTE21 | ChecklistTemplatePEOAttribute21 | — |
| ATTRIBUTE22 | ChecklistTemplatePEOAttribute22 | — |
| ATTRIBUTE23 | ChecklistTemplatePEOAttribute23 | — |
| ATTRIBUTE24 | ChecklistTemplatePEOAttribute24 | — |
| ATTRIBUTE25 | ChecklistTemplatePEOAttribute25 | — |
| ATTRIBUTE26 | ChecklistTemplatePEOAttribute26 | — |
| ATTRIBUTE27 | ChecklistTemplatePEOAttribute27 | — |
| ATTRIBUTE28 | ChecklistTemplatePEOAttribute28 | — |
| ATTRIBUTE29 | ChecklistTemplatePEOAttribute29 | — |
| ATTRIBUTE3 | ChecklistTemplatePEOAttribute3 | — |
| ATTRIBUTE30 | ChecklistTemplatePEOAttribute30 | — |
| ATTRIBUTE4 | ChecklistTemplatePEOAttribute4 | — |
| ATTRIBUTE5 | ChecklistTemplatePEOAttribute5 | — |
| ATTRIBUTE6 | ChecklistTemplatePEOAttribute6 | — |
| ATTRIBUTE7 | ChecklistTemplatePEOAttribute7 | — |
| ATTRIBUTE8 | ChecklistTemplatePEOAttribute8 | — |
| ATTRIBUTE9 | ChecklistTemplatePEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | ChecklistTemplatePEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | ChecklistTemplatePEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | ChecklistTemplatePEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | ChecklistTemplatePEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | ChecklistTemplatePEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | ChecklistTemplatePEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | ChecklistTemplatePEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | ChecklistTemplatePEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | ChecklistTemplatePEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ChecklistTemplatePEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ChecklistTemplatePEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ChecklistTemplatePEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | ChecklistTemplatePEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | ChecklistTemplatePEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | ChecklistTemplatePEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | ChecklistTemplatePEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | ChecklistTemplatePEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | ChecklistTemplatePEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | ChecklistTemplatePEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | ChecklistTemplatePEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | ChecklistTemplatePEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | ChecklistTemplatePEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | ChecklistTemplatePEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | ChecklistTemplatePEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | ChecklistTemplatePEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | ChecklistTemplatePEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | ChecklistTemplatePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ChecklistTemplatePEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | ChecklistTemplatePEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | ChecklistTemplatePEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ChecklistTemplatePEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ChecklistTemplatePEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | ChecklistTemplatePEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | ChecklistTemplatePEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | ChecklistTemplatePEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | ChecklistTemplatePEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | ChecklistTemplatePEOBusinessGroupId | — |
| CHECKLIST_CATEGORY | ChecklistTemplatePEOChecklistCategory | ✅ |
| CHECKLIST_CODE | ChecklistTemplatePEOChecklistCode | ✅ |
| CHECKLIST_ID | ChecklistId | ✅ |
| COMPLETED_ON | ChecklistTemplatePEOCompletedOn | ✅ |
| COMPLETION_OFFSET_DAYS | ChecklistTemplatePEOCompletionOffsetDays | ✅ |
| CREATED_BY | ChecklistTemplatePEOCreatedBy | ✅ |
| CREATION_DATE | ChecklistTemplatePEOCreationDate | ✅ |
| DATE_FROM | ChecklistTemplatePEODateFrom | ✅ |
| DATE_TO | ChecklistTemplatePEODateTo | ✅ |
| ELIGIBILITY_PROFILE_ID | ChecklistTemplatePEOEligibilityProfileId | ✅ |
| EVENT_REASON_ID | ChecklistTemplatePEOEventReasonId | — |
| INFORMATION1 | ChecklistTemplatePEOInformation1 | — |
| INFORMATION10 | ChecklistTemplatePEOInformation10 | — |
| INFORMATION11 | ChecklistTemplatePEOInformation11 | — |
| INFORMATION12 | ChecklistTemplatePEOInformation12 | — |
| INFORMATION13 | ChecklistTemplatePEOInformation13 | — |
| INFORMATION14 | ChecklistTemplatePEOInformation14 | — |
| INFORMATION15 | ChecklistTemplatePEOInformation15 | — |
| INFORMATION16 | ChecklistTemplatePEOInformation16 | — |
| INFORMATION17 | ChecklistTemplatePEOInformation17 | — |
| INFORMATION18 | ChecklistTemplatePEOInformation18 | — |
| INFORMATION19 | ChecklistTemplatePEOInformation19 | — |
| INFORMATION2 | ChecklistTemplatePEOInformation2 | — |
| INFORMATION20 | ChecklistTemplatePEOInformation20 | — |
| INFORMATION21 | ChecklistTemplatePEOInformation21 | — |
| INFORMATION22 | ChecklistTemplatePEOInformation22 | — |
| INFORMATION23 | ChecklistTemplatePEOInformation23 | — |
| INFORMATION24 | ChecklistTemplatePEOInformation24 | — |
| INFORMATION25 | ChecklistTemplatePEOInformation25 | — |
| INFORMATION26 | ChecklistTemplatePEOInformation26 | — |
| INFORMATION27 | ChecklistTemplatePEOInformation27 | — |
| INFORMATION28 | ChecklistTemplatePEOInformation28 | — |
| INFORMATION29 | ChecklistTemplatePEOInformation29 | — |
| INFORMATION3 | ChecklistTemplatePEOInformation3 | — |
| INFORMATION30 | ChecklistTemplatePEOInformation30 | — |
| INFORMATION4 | ChecklistTemplatePEOInformation4 | — |
| INFORMATION5 | ChecklistTemplatePEOInformation5 | — |
| INFORMATION6 | ChecklistTemplatePEOInformation6 | — |
| INFORMATION7 | ChecklistTemplatePEOInformation7 | — |
| INFORMATION8 | ChecklistTemplatePEOInformation8 | — |
| INFORMATION9 | ChecklistTemplatePEOInformation9 | — |
| INFORMATION_CATEGORY | ChecklistTemplatePEOInformationCategory | — |
| LAST_UPDATE_DATE | ChecklistTemplatePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ChecklistTemplatePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ChecklistTemplatePEOLastUpdatedBy | ✅ |
| LEGISLATION_CODE | ChecklistTemplatePEOLegislationCode | ✅ |
| MODULE_ID | ChecklistTemplatePEOModuleId | — |
| OBJECT_VERSION_NUMBER | ChecklistTemplatePEOObjectVersionNumber | — |
| OFFSET_DAYS | ChecklistTemplatePEOOffsetDays | ✅ |
| PROCESSING_MODE | ChecklistTemplatePEOProcessingMode | — |

---

## 📚 Referências

- [Oracle Docs — PER_CHECKLISTS_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perchecklistsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
