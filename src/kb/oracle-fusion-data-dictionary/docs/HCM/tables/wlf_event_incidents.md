---
id: DOC-HCM-732
doc_type: system-doc
title: "WLF_EVENT_INCIDENTS — Incidentes de Eventos (Learning)"
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
  - incidentes-eventos
aliases:
  - WLF_EVENT_INCIDENTS
  - wlf_event_incidents
  - wlf-event-incidents
  - incidentes-de-eventos
  - event-incidents
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_EVENT_INCIDENTS

## Visão Geral

Armazena os **incidentes registrados** durante eventos de aprendizado, como problemas técnicos, cancelamentos, ou ocorrências que impactam a execução do treinamento.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de incidentes** — registra problemas ocorridos durante eventos de aprendizado.
- **Qualidade de treinamento** — identifica padrões de problemas recorrentes.
- **Auditoria** — evidência de ocorrências que impactaram a execução do evento.
- **Melhoria contínua** — base para ações corretivas nos processos de learning.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EVENT_INCIDENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do incidente | — | 🟡 75% |
| 2 | EVENT_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição de evento associada | WLF_EVENT_ASSIGNMENTS_F | 🟡 70% |
| 3 | LEARNING_ITEM_ID | NUMBER(18) | NULL | FK | Item de aprendizado associado | WLF_LEARNING_ITEMS_F | 🟡 70% |
| 4 | INCIDENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de incidente | — | 🟡 70% |
| 5 | INCIDENT_DATE | DATE | NULL | Data | Data de ocorrência do incidente | — | 🟡 75% |
| 6 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descrição detalhada do incidente | — | 🟡 70% |
| 7 | SEVERITY | VARCHAR2(30) | NULL | Classificação | Severidade do incidente | — | 🟡 65% |
| 8 | RESOLUTION_STATUS | VARCHAR2(30) | NULL | Status | Status de resolução | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_event_assignments_f]] — via `EVENT_ASSIGNMENT_ID` (atribuição de evento)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Incidentes por evento de aprendizado
```sql
SELECT ei.INCIDENT_TYPE, ei.INCIDENT_DATE, ei.SEVERITY, ei.RESOLUTION_STATUS
FROM   WLF_EVENT_INCIDENTS ei
WHERE  ei.LEARNING_ITEM_ID = :p_learning_item_id
ORDER BY ei.INCIDENT_DATE DESC;
```

### Filtros comuns
- `SEVERITY = 'HIGH'` — Apenas incidentes de alta severidade
- `RESOLUTION_STATUS = 'OPEN'` — Incidentes não resolvidos

---

## Observações

- Tabela transacional — sem sufixo _F (não é date-effective).
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Confiança geral mais baixa — estrutura inferida por naming conventions.
- Pode conter informações sensíveis em DESCRIPTION.

---

## Referências

- [Oracle Docs — WLF_EVENT_INCIDENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfeventincidents.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
