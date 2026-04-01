---
id: DOC-HCM-503
doc_type: system-doc
title: "IRC_LC_ACTION_USAGES_B — Usos de Acoes (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - lc-action-usages
  - irc-recruiting
aliases:
  - IRC_LC_ACTION_USAGES_B
  - irc_lc_action_usages_b
  - lc-action-usages-b
  - lc-action-hcm
  - irc-lc-action-usages-b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_LC_ACTION_USAGES_B

## Visao Geral

**Configuracao de uso** de acoes do ciclo de vida. Tabela base (`_B`).

> [!note] Sufixo _B
> O sufixo `_B` indica tabela **base** (Base Table) — armazena dados independentes de idioma. Traducoes ficam na tabela `_TL` correspondente.

---

## Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Workflow:** Quais acoes disponiveis em cada fase.
- **Governanca:** Controle de acoes permitidas.
---

## Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% -- grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81-100%** -- Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51-80%** -- Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0-50%** -- Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LC_ACTION_USAGE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico | — | 🟢 85% |
| 2 | LC_ACTION_ID | NUMBER(18) | NOT NULL | FK | Acao | — | 🟢 85% |
| 3 | CONTEXT_TYPE | VARCHAR2(30) | NULL | Classificacao | Contexto | — | 🟡 70% |
| 4 | CONTEXT_ID | NUMBER(18) | NULL | FK | ID do contexto | — | 🟡 70% |
| 5 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 6 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora ultima alteracao | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Versao otimista | — | 🟢 90% |
---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)

---

## Uso Tipico

### Acoes de um contexto
```sql
SELECT au.LC_ACTION_ID, au.CONTEXT_TYPE
FROM   IRC_LC_ACTION_USAGES_B au WHERE au.CONTEXT_ID = :p_id;
```

### Filtros comuns
- `CONTEXT_TYPE = :tipo` — Por contexto
---

## Observacoes

- Tabela base (_B).
---

## Referencias

- [Oracle Docs -- IRC_LC_ACTION_USAGES_B](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/irclcactionusagesb.html)
- [[hcm-module-data-dictionary]] -- Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[routingstependactionpvo|RoutingStepEndActionPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ActionId | ✅ |
| LAST_EXECUTION_DATE | LastExecutionDate | — |
| LAST_EXECUTION_RESULT | LastExecutionResult | — |
| ROUTING_STEP_ID | RoutingStepId | — |
| STEP_ACTION_USAGE_CODE | StepActionUsageCode | — |
| STEP_ACTION_USAGE_ID | StepActionUsageId | ✅ |
| TRIGGER_EVENT_CODE | TriggerEventCode | — |

### [[routingstepstartactionpvo|RoutingStepStartActionPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ActionId | ✅ |
| LAST_EXECUTION_DATE | LastExecutionDate | — |
| LAST_EXECUTION_RESULT | LastExecutionResult | — |
| ROUTING_STEP_ID | RoutingStepId | — |
| STEP_ACTION_USAGE_CODE | StepActionUsageCode | — |
| STEP_ACTION_USAGE_ID | StepActionUsageId | ✅ |
| TRIGGER_EVENT_CODE | TriggerEventCode | — |

### [[routingstepstateactionpvo|RoutingStepStateActionPVO]] (HCM · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_ID | ActionId | ✅ |
| LAST_EXECUTION_DATE | LastExecutionDate | — |
| LAST_EXECUTION_RESULT | LastExecutionResult | — |
| ROUTING_STEP_ID | RoutingStepId | — |
| STEP_ACTION_USAGE_CODE | StepActionUsageCode | — |
| STEP_ACTION_USAGE_ID | StepActionUsageId | ✅ |
| TRIGGER_EVENT_CODE | TriggerEventCode | — |
