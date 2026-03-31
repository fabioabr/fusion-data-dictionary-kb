---
id: DOC-HCM-531
doc_type: system-doc
title: "IRC_ROUTING_STEPS_B — Etapas de Roteamento de Recrutamento (Base)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: "Técnico"
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - recruiting
  - routing-steps
  - fluxo-selecao
  - irc-routing
aliases:
  - IRC_ROUTING_STEPS_B
  - irc_routing_steps_b
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# IRC_ROUTING_STEPS_B

## 📌 Visão Geral

Armazena as **etapas de roteamento** (routing steps) do processo seletivo. Define a sequencia de fases que uma candidatura percorre (triagem, entrevista, oferta, etc.).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Configuracao do fluxo de selecao por requisicao
- Definicao de etapas obrigatorias e opcionais do processo
- Controle de progressao de candidatos entre fases

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ROUTING_STEP_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da etapa | --- | 🟢 90% |
| 2 | ROUTING_ID | NUMBER(18) | NOT NULL | FK | ID do modelo de roteamento | --- | 🟡 75% |
| 3 | STEP_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da etapa de roteamento | --- | 🟡 70% |
| 4 | STEP_ORDER | NUMBER | NULL | Dados | Ordem sequencial da etapa | --- | 🟡 70% |
| 5 | STEP_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo da etapa (screening, interview, offer) | --- | 🟡 70% |
| 6 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Classificacao | Indica se a etapa esta ativa (Y/N) | --- | 🟡 65% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Modelo de roteamento do Recruiting

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Etapas de um modelo de roteamento
```sql
SELECT rs.ROUTING_STEP_ID, rs.STEP_NAME, rs.STEP_ORDER
FROM   IRC_ROUTING_STEPS_B rs
WHERE  rs.ROUTING_ID = :p_routing_id
ORDER BY rs.STEP_ORDER;
```

---

## 🔒 Observações

- Tabela do modulo Recruiting do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[jobapphisteventpvo|JobAppHistEventPVO]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ROUTING_STEP_ID | RoutingStepBPEORoutingStepId | — |
| SEQUENCE_NUMBER | RoutingStepBPEOSequenceNumber | ✅ |

### [[poolmgmtprocesspvo|PoolMgmtProcessPVO]] (HCM · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PHASE_ID | RoutingStepPhaseBPEOPhaseId | ✅ |
| PHASE_ID | RoutingStepStateBPEOPhaseId | ✅ |
| PROCESS_ID | RoutingStepPhaseBPEOProcessId | — |
| PROCESS_ID | RoutingStepStateBPEOProcessId | — |
| PUBLIC_STATE_ID | RoutingStepStateBPEOPublicStateId | — |
| ROUTING_STEP_ID | RoutingStepPhaseBPEORoutingStepId | — |
| ROUTING_STEP_ID | RoutingStepStateBPEORoutingStepId | — |
| SEQUENCE_NUMBER | RoutingStepPhaseBPEOSequenceNumber | ✅ |
| SEQUENCE_NUMBER | RoutingStepStateBPEOSequenceNumber | ✅ |
| STATE_ID | RoutingStepPhaseBPEOStateId | ✅ |
| STATE_ID | RoutingStepStateBPEOStateId | ✅ |
| STEP_STATUS | RoutingStepPhaseBPEOStepStatus | — |
| STEP_STATUS | RoutingStepStateBPEOStepStatus | — |
| SUB_PROCESS_ID | RoutingStepPhaseBPEOSubProcessId | — |
| SUB_PROCESS_ID | RoutingStepStateBPEOSubProcessId | — |
| TYPE_CODE | RoutingStepPhaseBPEOTypeCode | — |
| TYPE_CODE | RoutingStepStateBPEOTypeCode | — |

### [[routingstepphasepvo|RoutingStepPhasePVO]] (HCM · BICC: 4/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | Code | ✅ |
| IS_COMPLETION_FLAG | IsCompletionFlag | — |
| IS_INITIAL_FLAG | IsInitialFlag | — |
| LAST_ACTIVATION_DATE | LastActivationDate | — |
| LAST_DEACTIVATION_DATE | LastDeactivationDate | — |
| PHASE_ID | PhaseId | ✅ |
| PROCESS_ID | ProcessId | — |
| PUBLIC_STATE_ID | PublicStateId | — |
| ROUTING_STEP_ID | RoutingStepId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| SETTING_ID | SettingId | — |
| STEP_STATUS | StepStatus | — |
| SUB_PROCESS_ID | SubProcessId | — |
| TYPE_CODE | TypeCode | — |

### [[routingstepstatepvo|RoutingStepStatePVO]] (HCM · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CODE | Code | ✅ |
| IS_COMPLETION_FLAG | IsCompletionFlag | — |
| IS_INITIAL_FLAG | IsInitialFlag | — |
| LAST_ACTIVATION_DATE | LastActivationDate | — |
| LAST_DEACTIVATION_DATE | LastDeactivationDate | — |
| PROCESS_ID | ProcessId | — |
| PUBLIC_STATE_ID | PublicStateId | ✅ |
| ROUTING_STEP_ID | RoutingStepId | ✅ |
| SEQUENCE_NUMBER | SequenceNumber | ✅ |
| SETTING_ID | SettingId | — |
| STATE_ID | StateId | ✅ |
| STEP_STATUS | StepStatus | — |
| SUB_PROCESS_ID | SubProcessId | — |
| TYPE_CODE | TypeCode | — |

---

## 📚 Referências

- [Oracle Docs — IRC_ROUTING_STEPS_B](https://docs.oracle.com/en/cloud/saas/talent-management/25a/oedmf/ircroutingstepsb.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
