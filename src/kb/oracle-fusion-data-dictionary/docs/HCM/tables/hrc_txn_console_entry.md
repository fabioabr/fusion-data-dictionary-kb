---
id: DOC-HCM-159
doc_type: system-doc
title: "HRC_TXN_CONSOLE_ENTRY — Entradas do Console de Transações HCM"
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
  - entry
aliases:
  - HRC_TXN_CONSOLE_ENTRY
  - hrc_txn_console_entry
  - entradas-do-console-de-transações-hcm
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_TXN_CONSOLE_ENTRY

## 📌 Visão Geral

Tabela central do **console de transações HCM**. Cada registro representa uma entrada para monitoramento e resolução de problemas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Monitoramento centralizado:** Transações que requerem atenção.
- **Diagnóstico:** Ponto central de falhas.
- **Gestão de backlog:** Priorização de pendentes.
- **Auditoria operacional:** Ciclo de vida de transações.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONSOLE_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da entrada | — | 🟢 95% |
| 2 | TXN_ID | NUMBER(18) | NOT NULL | FK | Transação HCM | [[hrc_txn_header]] | 🟢 90% |
| 3 | ENTRY_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (ERROR, WARNING, INFO) | — | 🟡 75% |
| 4 | ENTRY_STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status (NEW, IN_PROGRESS, RESOLVED) | — | 🟡 75% |
| 5 | PRIORITY | VARCHAR2(30) | NULL | Classificação | Prioridade (HIGH, MEDIUM, LOW) | — | 🟡 70% |
| 6 | SUMMARY | VARCHAR2(2000) | NULL | Descrição | Resumo do problema | — | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_header]] — via `TXN_ID` (transacao da entrada de console)

### Tabelas-filha (FK de saída)
- [[hrc_console_fault_details_vl]] — via `CONSOLE_ENTRY_ID` (detalhes de falha da entrada de console)
- [[hrc_console_issue_assignment]] — via `CONSOLE_ENTRY_ID` (atribuicoes de problema da entrada de console)
- [[hrc_console_issue_comments]] — via `CONSOLE_ENTRY_ID` (comentarios da entrada de console)

---

## 📎 Uso Típico

### Entradas pendentes
```sql
SELECT e.CONSOLE_ENTRY_ID, e.TXN_ID, e.ENTRY_TYPE, e.PRIORITY, e.SUMMARY
FROM   HRC_TXN_CONSOLE_ENTRY e
WHERE  e.ENTRY_STATUS IN ('NEW', 'IN_PROGRESS')
ORDER BY DECODE(e.PRIORITY, 'HIGH', 1, 'MEDIUM', 2, 'LOW', 3);
```

---

## 🔒 Observações

- Tabela central de monitoramento.
- Ciclo: NEW -> IN_PROGRESS -> RESOLVED.
- Prioridade HIGH deve ser tratada primeiro.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
