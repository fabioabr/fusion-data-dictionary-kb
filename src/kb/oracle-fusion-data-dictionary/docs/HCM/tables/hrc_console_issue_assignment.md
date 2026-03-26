---
id: DOC-HCM-157
doc_type: system-doc
title: "HRC_CONSOLE_ISSUE_ASSIGNMENT — Atribuições de Problemas do Console"
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
  - issue
  - assignment
aliases:
  - HRC_CONSOLE_ISSUE_ASSIGNMENT
  - hrc_console_issue_assignment
  - atribuições-de-problemas-do-console
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_CONSOLE_ISSUE_ASSIGNMENT

## 📌 Visão Geral

Armazena **atribuições de problemas** do console de transações HCM. Vincula issues a responsáveis.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de incidentes:** Atribui problemas a responsáveis.
- **Rastreamento:** Quem está tratando cada problema.
- **SLA de resolução:** Controle de prazo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ISSUE_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | CONSOLE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada do console | [[hrc_txn_console_entry]] | 🟢 85% |
| 3 | ASSIGNED_TO | VARCHAR2(64) | NOT NULL | Referência | Usuário atribuído | — | 🟡 75% |
| 4 | ASSIGNMENT_DATE | DATE | NOT NULL | Data | Data da atribuição | — | 🟡 80% |
| 5 | STATUS | VARCHAR2(30) | NULL | Classificação | Status (OPEN, IN_PROGRESS, RESOLVED) | — | 🟡 70% |
| 6 | RESOLUTION_DATE | DATE | NULL | Data | Data da resolução | — | 🟡 70% |
| 7 | NOTES | VARCHAR2(4000) | NULL | Texto livre | Notas | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_console_entry]] — via `CONSOLE_ENTRY_ID` (entrada de console da atribuicao de problema)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Problemas abertos
```sql
SELECT a.ASSIGNED_TO, a.ASSIGNMENT_DATE, a.STATUS
FROM   HRC_CONSOLE_ISSUE_ASSIGNMENT a
WHERE  a.STATUS IN ('OPEN', 'IN_PROGRESS')
ORDER BY a.ASSIGNMENT_DATE;
```

---

## 🔒 Observações

- Cada entrada pode ter múltiplas atribuições.
- `STATUS = 'RESOLVED'` com `RESOLUTION_DATE` = concluído.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
