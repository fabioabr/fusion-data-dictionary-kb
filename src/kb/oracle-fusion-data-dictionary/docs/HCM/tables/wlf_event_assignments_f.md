---
id: DOC-HCM-729
doc_type: system-doc
title: "WLF_EVENT_ASSIGNMENTS_F — Atribuições de Eventos (Learning)"
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
  - learning
  - workforce-learning
  - eventos-atribuição
aliases:
  - WLF_EVENT_ASSIGNMENTS_F
  - wlf_event_assignments_f
  - wlf-event-assignments-f
  - atribuições-de-eventos-learning
  - event-assignments
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_EVENT_ASSIGNMENTS_F

## Visão Geral

Armazena as **atribuições de eventos de aprendizado**, vinculando eventos (cursos, seminários, workshops) a colaboradores ou grupos. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Inscrição em eventos** — registra a atribuição de colaboradores a eventos de aprendizado.
- **Gestão de turmas** — controla a participação em eventos presenciais/virtuais.
- **Tracking de presença** — base para controle de frequência em eventos.
- **Compliance** — evidência de participação em treinamentos obrigatórios.
- **Relatórios de participação** — análise de adesão a programas de capacitação.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atribuição de evento | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado (evento) | WLF_LEARNING_ITEMS_F | 🟡 80% |
| 5 | PERSON_ID | NUMBER(18) | NULL | FK | Pessoa atribuída ao evento | PER_ALL_PEOPLE_F | 🟢 85% |
| 6 | ASSIGNMENT_STATUS | VARCHAR2(30) | NULL | Status | Status da atribuição (enrolled, attended, etc.) | — | 🟡 80% |
| 7 | ENROLLMENT_DATE | DATE | NULL | Data | Data da inscrição | — | 🟡 75% |
| 8 | ATTENDANCE_STATUS | VARCHAR2(30) | NULL | Status | Status de presença (present, absent, excused) | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa inscrita)

### Tabelas-filha (FK de saída)
- [[wlf_event_assignments_f_tl]] — via `EVENT_ASSIGNMENT_ID` (traduções da atribuição de evento de aprendizado)
- [[wlf_assignment_destinations_f]] — via `EVENT_ASSIGNMENT_ID` (destinos da atribuição de evento de aprendizado)

---

## Uso Típico

### Inscrições em um evento de aprendizado
```sql
SELECT ea.PERSON_ID, p.FULL_NAME, ea.ASSIGNMENT_STATUS, ea.ENROLLMENT_DATE
FROM   WLF_EVENT_ASSIGNMENTS_F ea
JOIN   PER_ALL_PEOPLE_F p ON ea.PERSON_ID = p.PERSON_ID
WHERE  ea.LEARNING_ITEM_ID = :p_learning_item_id
  AND  SYSDATE BETWEEN ea.EFFECTIVE_START_DATE AND ea.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Atribuições de um evento
- `ASSIGNMENT_STATUS = 'ENROLLED'` — Apenas inscritos

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Traduções disponíveis em WLF_EVENT_ASSIGNMENTS_F_TL.
- Cada registro representa uma inscrição individual em um evento.

---

## Referências

- [Oracle Docs — WLF_EVENT_ASSIGNMENTS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfeventassignmentsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[eventassignmentpvo|EventAssignmentPVO]] (HCM · BICC: 5/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_PROFILE_NUMBER | EventAssignmentDEOAssignmentProfileNumber | — |
| ASSIGNMENT_RULE_ID | EventAssignmentDEOAssignmentRuleId | — |
| ASSIGNMENT_START_DATE | EventAssignmentDEOAssignmentStartDate | — |
| COMMENTS | EventAssignmentDEOComments | — |
| CREATED_BY | EventAssignmentDEOCreatedBy | — |
| CREATION_DATE | EventAssignmentDEOCreationDate | — |
| EFFECTIVE_END_DATE | EventAssignmentDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EventAssignmentDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | EventAssignmentDEOEnterpriseId | — |
| EVENT_ASSIGNMENT_ID | EventAssignmentDEOEventAssignmentId | ✅ |
| EVENT_ID | EventAssignmentDEOEventId | — |
| LAST_UPDATE_DATE | EventAssignmentDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | EventAssignmentDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EventAssignmentDEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EventAssignmentDEOObjectVersionNumber | — |
| PROCESSED_DATE | EventAssignmentDEOProcessedDate | — |
| REQUEST_DETAIL_ID | EventAssignmentDEORequestDetailId | — |
| STATUS | EventAssignmentDEOStatus | ✅ |

### [[eventassignmentrecordpvo|EventAssignmentRecordPVO]] (HCM · BICC: 6/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_PROFILE_NUMBER | EventAssignmentDEOAssignmentProfileNumber | ✅ |
| ASSIGNMENT_RULE_ID | EventAssignmentDEOAssignmentRuleId | ✅ |
| ASSIGNMENT_START_DATE | EventAssignmentDEOAssignmentStartDate | — |
| COMMENTS | EventAssignmentDEOComments | — |
| CREATED_BY | EventAssignmentDEOCreatedBy | — |
| CREATION_DATE | EventAssignmentDEOCreationDate | — |
| EFFECTIVE_END_DATE | EventAssignmentDEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | EventAssignmentDEOEffectiveStartDate | — |
| ENTERPRISE_ID | EventAssignmentDEOEnterpriseId | — |
| EVENT_ASSIGNMENT_ID | EventAssignmentDEOEventAssignmentId | ✅ |
| EVENT_ID | EventAssignmentDEOEventId | ✅ |
| LAST_UPDATE_DATE | EventAssignmentDEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | EventAssignmentDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | EventAssignmentDEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | EventAssignmentDEOObjectVersionNumber | — |
| PROCESSED_DATE | EventAssignmentDEOProcessedDate | ✅ |
| REQUEST_DETAIL_ID | EventAssignmentDEORequestDetailId | — |
| STATUS | EventAssignmentDEOStatus | ✅ |
