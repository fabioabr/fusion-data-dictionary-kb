---
id: DOC-HCM-578
doc_type: system-doc
title: "PAY_FLOW_TASK_INSTANCES — Instancias de Tarefas de Fluxo de Folha"
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
  - payroll
  - flow-tasks
  - tarefas-fluxo
  - pay-flow-tasks
aliases:
  - PAY_FLOW_TASK_INSTANCES
  - pay_flow_task_instances
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PAY_FLOW_TASK_INSTANCES

## 📌 Visão Geral

Armazena as **instancias de tarefas** executadas dentro de fluxos de processamento de folha (payroll flows). Cada registro representa uma execucao especifica de uma tarefa (calculo, validacao, pagamento, contabilizacao).

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- Rastreamento de execucao de tarefas de folha
- Monitoramento de status de processamento
- Auditoria do pipeline de processamento de payroll

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | FLOW_TASK_INSTANCE_ID | NUMBER(18) | NOT NULL | PK | Identificador unico da instancia | --- | 🟢 85% |
| 2 | FLOW_INSTANCE_ID | NUMBER(18) | NOT NULL | FK | ID da instancia do fluxo | --- | 🟡 75% |
| 3 | TASK_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da tarefa | --- | 🟡 75% |
| 4 | TASK_STATUS | VARCHAR2(30) | NULL | Classificacao | Status da tarefa (pending, running, completed, error) | --- | 🟡 75% |
| 5 | START_DATE | TIMESTAMP | NULL | Dados | Data/hora de inicio da tarefa | --- | 🟡 70% |
| 6 | END_DATE | TIMESTAMP | NULL | Dados | Data/hora de fim da tarefa | --- | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou o registro | --- | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | --- | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- --- Instancia de fluxo de folha (via `FLOW_INSTANCE_ID`)

### Tabelas-filha (FK de saída)
- --- Tabela de instancia, sem filhas conhecidas

---

## 📎 Uso Típico

### Tarefas de um fluxo de folha
```sql
SELECT fti.TASK_NAME, fti.TASK_STATUS, fti.START_DATE, fti.END_DATE
FROM   PAY_FLOW_TASK_INSTANCES fti
WHERE  fti.FLOW_INSTANCE_ID = :p_flow_id
ORDER BY fti.START_DATE;
```

---

## 🔒 Observações

- Tabela do modulo Payroll do Oracle Fusion HCM.
- Campos de auditoria (`CREATED_BY`, `CREATION_DATE`, `LAST_UPDATED_BY`, `LAST_UPDATE_DATE`) seguem o padrao Oracle.
- Consultar documentacao oficial Oracle para validacao de colunas no release especifico.

---

## 🔗 PVOs Relacionados

### [[retroelemententry|RetroElementEntry]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_FLOW_TASK_ID | FlowTaskInstanceBaseFlowTaskId | — |
| ESS_SERVICE_EXEC_ID | FlowTaskInstanceEssServiceExecId | — |
| FLOW_INSTANCE_ID | FlowTaskInstanceFlowInstanceId | — |
| FLOW_TASK_INSTANCE_ID | FlowTaskInstanceFlowTaskInstanceId | — |
| STATUS | FlowTaskInstanceStatus | — |

---

## 📚 Referências

- [Oracle Docs — PAY_FLOW_TASK_INSTANCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/payflowtaskinstances.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
