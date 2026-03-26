---
id: DOC-HCM-158
doc_type: system-doc
title: "HRC_CONSOLE_ISSUE_COMMENTS — Comentários de Problemas do Console"
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
  - comments
aliases:
  - HRC_CONSOLE_ISSUE_COMMENTS
  - hrc_console_issue_comments
  - comentários-de-problemas-do-console
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRC_CONSOLE_ISSUE_COMMENTS

## 📌 Visão Geral

Armazena **comentários** sobre problemas do console de transações HCM.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Documentação:** Observações durante resolução.
- **Comunicação:** Troca de informações.
- **Histórico:** Trilha de auditoria.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ISSUE_COMMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | CONSOLE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada do console | [[hrc_txn_console_entry]] | 🟢 85% |
| 3 | COMMENT_TEXT | VARCHAR2(4000) | NOT NULL | Texto livre | Texto do comentário | — | 🟡 80% |
| 4 | COMMENTED_BY | VARCHAR2(64) | NOT NULL | Referência | Usuário que comentou | — | 🟡 75% |
| 5 | COMMENT_DATE | TIMESTAMP | NOT NULL | Data | Data/hora do comentário | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrc_txn_console_entry]] — via `CONSOLE_ENTRY_ID` (entrada de console do comentario)

---

## 📎 Uso Típico

### Comentários de um problema
```sql
SELECT c.COMMENT_TEXT, c.COMMENTED_BY, c.COMMENT_DATE
FROM   HRC_CONSOLE_ISSUE_COMMENTS c
WHERE  c.CONSOLE_ENTRY_ID = :p_entry_id
ORDER BY c.COMMENT_DATE;
```

---

## 🔒 Observações

- Comentários são imutáveis após criação.
- Ordenar por `COMMENT_DATE` para cronologia.

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
