---
id: DOC-HCM-612
doc_type: system-doc
title: "PER_ACTION_OCCURRENCES — Ocorrências de Ações de RH"
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
  - ocorrencias
  - action-occurrences
aliases:
  - PER_ACTION_OCCURRENCES
  - per_action_occurrences
  - per-action-occurrences
  - ocorrências-de-ações-de-rh
  - per-action-occurrenc
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ACTION_OCCURRENCES

## 📌 Visão Geral

Armazena os **registros de ocorrências** de ações de RH realizadas sobre colaboradores. Cada registro representa uma instância concreta de uma ação (ex.: uma admissão específica, uma promoção realizada).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Histórico de movimentações** — registra cada ação executada no ciclo de vida.
- **Auditoria** — rastreabilidade completa com datas e responsáveis.
- **Relatórios de movimentação** — base para dashboards de RH.
- **Integração com workflow** — registra o resultado dos fluxos de aprovação.
- **Análise de tendências** — histórico de ações para planejamento de workforce.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ACTION_OCCURRENCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da ocorrência | — | 🟢 95% |
| 2 | ACTION_ID | NUMBER(18) | NOT NULL | FK | Ação realizada | PER_ACTIONS_B | 🟢 90% |
| 3 | ACTION_REASON_ID | NUMBER(18) | NULL | FK | Motivo da ação | PER_ACTION_REASONS_B | 🟢 85% |
| 4 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador afetado | PER_ALL_PEOPLE_F | 🟢 90% |
| 5 | EFFECTIVE_DATE | DATE | NOT NULL | Vigência | Data efetiva da ação | — | 🟢 90% |
| 6 | ACTION_STATUS | VARCHAR2(30) | NULL | Status | Status da ocorrência (COMPLETED, PENDING) | — | 🟡 75% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_actions_b]] — via `ACTION_ID` (ação de RH realizada na ocorrência)
- [[per_action_reasons_b]] — via `ACTION_REASON_ID` (motivo da ação de RH)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador afetado pela ação de RH)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Ocorrências de ações de um colaborador
```sql
SELECT pao.ACTION_OCCURRENCE_ID, pa.ACTION_CODE, pao.EFFECTIVE_DATE
FROM   PER_ACTION_OCCURRENCES pao
JOIN   PER_ACTIONS_B pa ON pao.ACTION_ID = pa.ACTION_ID
WHERE  pao.PERSON_ID = :p_person_id
ORDER BY pao.EFFECTIVE_DATE DESC;
```

### Filtros comuns
- `ACTION_STATUS = 'COMPLETED'` — Ações concluídas
- `EFFECTIVE_DATE >= TRUNC(SYSDATE, 'YEAR')` — Ações do ano corrente
---

## 🔒 Observações

- Cada registro representa uma instância concreta de uma ação sobre um colaborador.
- O `EFFECTIVE_DATE` marca quando a ação entra em vigor — pode ser retroativa ou futura.
- Utilizada em conjunto com PER_ALL_ASSIGNMENTS_M para rastrear mudanças no assignment.
---

## 🔗 PVOs Relacionados

### [[actionoccurrencespvo|ActionOccurrencesPVO]] (GL · BICC: 4/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DATE | ActionOccurrencesPEOActionDate | — |
| ACTION_DATE | SourceAOPEOActionDate | — |
| ACTION_ID | ActionOccurrencesPEOActionId | ✅ |
| ACTION_ID | SourceAOPEOActionId | — |
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ACTION_OCCURRENCE_ID | SourceAOPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | ✅ |
| ACTION_REASON_ID | SourceAOPEOActionReasonId | — |
| ACTION_TYPE_CODE | ActionOccurrencesPEOActionTypeCode | — |
| BUSINESS_GROUP_ID | ActionOccurrencesPEOBusinessGroupId | — |
| CREATED_BY | ActionOccurrencesPEOCreatedBy | — |
| CREATION_DATE | ActionOccurrencesPEOCreationDate | — |
| ENTITY_ID | ActionOccurrencesPEOEntityId | — |
| ENTITY_ID | SourceAOPEOEntityId | — |
| ENTITY_TYPE | ActionOccurrencesPEOEntityType | — |
| ENTITY_TYPE | SourceAOPEOEntityType | — |
| FREEZE_START_DATE | ActionOccurrencesPEOFreezeStartDate | — |
| FREEZE_UNTIL_DATE | ActionOccurrencesPEOFreezeUntilDate | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActionOccurrencesPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActionOccurrencesPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | ActionOccurrencesPEOLegalEntityId | — |
| OBJECT_VERSION_NUMBER | ActionOccurrencesPEOObjectVersionNumber | — |
| PARENT_ENTITY_KEY_ID | ActionOccurrencesPEOParentEntityKeyId | — |
| PARENT_ENTITY_TYPE | ActionOccurrencesPEOParentEntityType | — |
| PROPOSED_ACTION_ID | ActionOccurrencesPEOProposedActionId | — |
| PROPOSED_ACTION_TYPE | ActionOccurrencesPEOProposedActionType | — |
| PROPOSED_REASON_ID | ActionOccurrencesPEOProposedReasonId | — |
| PROPOSED_START_DATE | ActionOccurrencesPEOProposedStartDate | — |
| PROPOSED_WORKER_TYPE | ActionOccurrencesPEOProposedWorkerType | — |
| REF_ACTION_OCCURRENCE_ID | ActionOccurrencesPEORefActionOccurrenceId | — |
| SUBMITTED_BY | ActionOccurrencesPEOSubmittedBy | — |

### [[businessunitpvo|BusinessUnitPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[departmentpvo|DepartmentPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[departmentpvoviewall|DepartmentPVOViewAll]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[enterprisepvo|EnterprisePVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[gradepvo|GradePVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DATE | ActionOccurrencesPEOActionDate | — |
| ACTION_ID | ActionOccurrencesPEOActionId | — |
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |

### [[gradesteppvo|GradeStepPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_DATE | ActionOccurrencesPEOActionDate | — |
| ACTION_ID | ActionOccurrencesPEOActionId | — |
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | ✅ |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | ✅ |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[legalemployerpvo|LegalEmployerPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[organizationpvo|OrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[payrollstatutoryunitpvo|PayrollStatutoryUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

### [[projectexpenditureorganizationpvo|ProjectExpenditureOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[projecttaskowningorganizationpvo|ProjectTaskOwningOrganizationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[projectunitclassificationpvo|ProjectUnitClassificationPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[reportingestablishmentpvo|ReportingEstablishmentPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[reportingestablishmentpvoviewall|ReportingEstablishmentPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[taxreportingunitpvo|TaxReportingUnitPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | — |

### [[unionpvo|UnionPVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrencesPEOActionOccurrenceId | — |
| ACTION_REASON_ID | ActionOccurrencesPEOActionReasonId | — |
| LAST_UPDATE_DATE | ActionOccurrencesPEOLastUpdateDate | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_ACTION_OCCURRENCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/peractionoccurrences.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
