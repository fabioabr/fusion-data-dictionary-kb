---
id: DOC-GL-033
doc_type: system-doc
title: "GL_PERIOD_STATUSES — Status dos Períodos Contábeis"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - general-ledger
  - data-dictionary
  - periodos
  - period-statuses
  - contabilidade
aliases:
  - GL_PERIOD_STATUSES
  - gl_period_statuses
  - status-periodos-gl
  - period-statuses
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_PERIOD_STATUSES

## 📌 Visão Geral

Armazena o **status de cada período contábil** por ledger e application (módulo). Controla se um período está aberto, fechado, nunca aberto ou permanentemente fechado para lançamentos. É a tabela que governa a janela temporal de contabilização — nenhum lançamento pode ser feito em um período que não esteja com status "Open" (O).

> [!note] Granularidade por Application
> O status do período é controlado **por aplicação** (Application ID). Um mesmo período pode estar aberto para o GL e fechado para o AP, por exemplo. Isso permite controle granular de fechamento por módulo.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Abertura de período:** Transição de "Never Opened" para "Open" para permitir lançamentos.
- **Fechamento contábil:** Transição de "Open" para "Closed" no processo de month-end close.
- **Controle de posting:** O processo de contabilização valida se o período está aberto antes de aceitar journals.
- **Reopen de períodos:** Reabertura de períodos já fechados para ajustes (requer permissão especial).
- **Auditoria:** Rastreamento de quem abriu/fechou cada período e quando.
- **Subledger Accounting:** Os subledgers consultam esta tabela para validar se podem transferir journals ao GL.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger (livro contábil) | [[gl_ledgers]] | 🟢 100% |
| 2 | APPLICATION_ID | NUMBER(18) | NOT NULL | FK | Identificador da aplicação/módulo Oracle (101=GL, 200=AP, 222=AR) | [[fnd_application]] | 🟢 100% |
| 3 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | PK | Nome do período contábil (ex: JAN-26, FEB-26) | — | 🟢 100% |
| 4 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano do período contábil | — | 🟢 100% |
| 5 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano | — | 🟢 100% |
| 6 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Período | Tipo do período (Month, Quarter, Year) | [[gl_period_types]] | 🟢 100% |
| 7 | CLOSING_STATUS | VARCHAR2(1) | NOT NULL | Status | Status do período: O (Open), C (Closed), F (Future Enterable), N (Never Opened), P (Permanently Closed) | — | 🟢 100% |
| 8 | START_DATE | DATE | NOT NULL | Data | Data de início do período | — | 🟢 100% |
| 9 | END_DATE | DATE | NOT NULL | Data | Data de fim do período | — | 🟢 100% |
| 10 | EFFECTIVE_PERIOD_NUM | NUMBER(15) | NULL | Período | Número efetivo do período (para ordenação cross-year) | — | 🟢 90% |
| 11 | ADJUSTMENT_PERIOD_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se é um período de ajuste (Y/N) — usado no fechamento anual | — | 🟢 100% |
| 12 | ELIMINATION_CONFIRMED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se eliminações intercompany foram confirmadas (Y/N) | — | 🟡 75% |
| 13 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 14 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 15 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 16 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 17 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[fnd_application]] — via `APPLICATION_ID` (aplicação/módulo Oracle)
- [[gl_period_types]] — via `PERIOD_TYPE` (tipo de período)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de controle/status consultada por validação.

---

## 📎 Uso Típico

### Períodos abertos para o GL
```sql
SELECT ps.PERIOD_NAME, ps.PERIOD_YEAR, ps.PERIOD_NUM,
       ps.START_DATE, ps.END_DATE, ps.CLOSING_STATUS
FROM   GL_PERIOD_STATUSES ps
WHERE  ps.LEDGER_ID = :p_ledger_id
  AND  ps.APPLICATION_ID = 101   -- General Ledger
  AND  ps.CLOSING_STATUS = 'O';
```

### Histórico de status por período
```sql
SELECT ps.PERIOD_NAME, ps.CLOSING_STATUS,
       DECODE(ps.CLOSING_STATUS, 'O','Aberto', 'C','Fechado',
              'F','Future Entry', 'N','Nunca Aberto', 'P','Permanente') AS descricao
FROM   GL_PERIOD_STATUSES ps
WHERE  ps.LEDGER_ID = :p_ledger_id
  AND  ps.APPLICATION_ID = 101
  AND  ps.PERIOD_YEAR = 2026
ORDER BY ps.PERIOD_NUM;
```

### Filtros comuns
- `CLOSING_STATUS = 'O'` — Períodos abertos para lançamento
- `CLOSING_STATUS = 'C'` — Períodos fechados
- `CLOSING_STATUS = 'N'` — Períodos nunca abertos
- `APPLICATION_ID = 101` — General Ledger
- `ADJUSTMENT_PERIOD_FLAG = 'Y'` — Períodos de ajuste (13º período)

---

## 🔒 Observações

- A chave composta é `LEDGER_ID + APPLICATION_ID + PERIOD_NAME` — o mesmo período pode ter status diferentes por aplicação.
- O fluxo normal de status é: **N** (Never Opened) → **F** (Future Enterable) → **O** (Open) → **C** (Closed). O status **P** (Permanently Closed) impede reabertura.
- Períodos de ajuste (`ADJUSTMENT_PERIOD_FLAG = 'Y'`) são usados para lançamentos de fechamento anual e não aparecem em relatórios mensais regulares.
- O `APPLICATION_ID = 101` é o General Ledger. Para verificar se um subledger pode postar, consultar com o APPLICATION_ID correspondente (200=AP, 222=AR, etc.).
- O processo de "Close Period" no Oracle Fusion altera o `CLOSING_STATUS` e atualiza `LAST_UPDATE_DATE` — útil para rastrear quando cada período foi fechado.

---

## 📚 Referências

- [Oracle Docs — GL_PERIOD_STATUSES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glperiodstatuses-25788.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
