---
id: DOC-HCM-161
doc_type: system-doc
title: "HRC_TXN_FND_BPM_TASK_VL — Tarefas BPM de Transações — Visão Traduzida"
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
  - transaction-console
  - bpm
  - task
aliases:
  - HRC_TXN_FND_BPM_TASK_VL
  - hrc_txn_fnd_bpm_task_vl
  - tarefas-bpm-de-transaçõesvisão-traduzida
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_TXN_FND_BPM_TASK_VL

## 📌 Visão Geral

View traduzida das **tarefas BPM** associadas a transações HCM. Integra Oracle BPM Worklist com transações de RH.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Monitoramento de aprovações:** Status de tarefas BPM.
- **Worklist integrado:** Contexto HCM + BPM.
- **SLA:** Tempos de resposta de aprovadores.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TASK_ID | NUMBER(18) | NOT NULL | PK | Identificador único da tarefa | — | 🟢 90% |
| 2 | TXN_ID | NUMBER(18) | NOT NULL | FK | Transação HCM | [[hrc_txn_header]] | 🟢 85% |
| 3 | TASK_NUMBER | VARCHAR2(240) | NULL | Identificação | Número da tarefa | — | 🟡 75% |
| 4 | TASK_STATUS | VARCHAR2(30) | NULL | Classificação | Status (ASSIGNED, COMPLETED, EXPIRED) | — | 🟡 75% |
| 5 | TASK_TITLE | VARCHAR2(2000) | NULL | Descrição | Título traduzido | — | 🟡 75% |
| 6 | ASSIGNEE | VARCHAR2(240) | NULL | Referência | Usuário/papel atribuído | — | 🟡 70% |
| 7 | ASSIGNED_DATE | TIMESTAMP | NULL | Data | Data de atribuição | — | 🟡 70% |
| 8 | EXPIRATION_DATE | TIMESTAMP | NULL | Data | Data de expiração | — | 🟡 70% |
| 9 | OUTCOME | VARCHAR2(30) | NULL | Classificação | Resultado (APPROVE, REJECT) | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_header]] — via `TXN_ID` (transacao da tarefa BPM)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Tarefas BPM pendentes
```sql
SELECT t.TASK_NUMBER, t.TASK_TITLE, t.ASSIGNEE, t.EXPIRATION_DATE
FROM   HRC_TXN_FND_BPM_TASK_VL t
WHERE  t.TASK_STATUS = 'ASSIGNED'
ORDER BY t.EXPIRATION_DATE;
```

---

## 🔒 Observações

- View traduzida (sufixo `_VL`).
- `TASK_STATUS = 'EXPIRED'` = aprovador não respondeu no prazo.
- `OUTCOME` preenchido após ação do aprovador.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
