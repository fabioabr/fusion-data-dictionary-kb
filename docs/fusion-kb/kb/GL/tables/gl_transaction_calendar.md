---
id: DOC-GL-038
doc_type: system-doc
title: "GL_TRANSACTION_CALENDAR — Calendário de Transações"
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
  - calendario
  - transaction-calendar
  - dias-uteis
  - feriados
aliases:
  - GL_TRANSACTION_CALENDAR
  - gl_transaction_calendar
  - calendario-transacoes-gl
  - transaction-calendar
  - business-days
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_TRANSACTION_CALENDAR

## 📌 Visão Geral

Armazena o **calendário de transações** do General Ledger, definindo quais dias são **dias úteis (business days)** para fins de contabilização. Controla em quais dias transações podem ser contabilizadas e é utilizado para determinar o período contábil correto quando uma transação cai em um dia não-útil (fim de semana ou feriado).

> [!note] Encumbrance Accounting
> O calendário de transações é especialmente relevante para **Encumbrance Accounting** (reservas orçamentárias). Quando ativado, transações em dias não-úteis são automaticamente atribuídas ao próximo dia útil.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle de dias úteis:** Definição de quais dias permitem lançamentos contábeis.
- **Encumbrance Accounting:** Determinação do período contábil para reservas orçamentárias quando a data da transação cai em dia não-útil.
- **Validação de GL Date:** Verificação se uma data de lançamento é um dia útil válido.
- **Relatórios de aging:** Cálculo de aging baseado em dias úteis (não corridos).
- **Processos batch:** Agendamento de processos contábeis em dias úteis.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TRANSACTION_CALENDAR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do calendário de transações | — | 🟢 95% |
| 2 | TRANSACTION_CALENDAR_NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do calendário de transações | — | 🟢 95% |
| 3 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do conjunto de períodos (calendário contábil) | [[gl_period_sets]] | 🟢 90% |
| 4 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | FK | Tipo de período associado | [[gl_period_types]] | 🟢 90% |
| 5 | TRANSACTION_DATE | DATE | NOT NULL | Data | Data específica no calendário | — | 🟢 95% |
| 6 | BUSINESS_DAY_FLAG | VARCHAR2(1) | NOT NULL | Status | Indica se é dia útil: Y (sim) ou N (não) | — | 🟢 95% |
| 7 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do calendário ou do dia específico | — | 🟡 75% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 13 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |
| 14 | ATTRIBUTE1–5 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_period_sets]] — via `PERIOD_SET_NAME` (conjunto de períodos/calendário contábil)
- [[gl_period_types]] — via `PERIOD_TYPE` (tipo de período)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

### Verificar se uma data é dia útil
```sql
SELECT tc.TRANSACTION_DATE,
       tc.BUSINESS_DAY_FLAG
FROM   GL_TRANSACTION_CALENDAR tc
WHERE  tc.TRANSACTION_CALENDAR_NAME = :p_calendar_name
  AND  tc.TRANSACTION_DATE = :p_date;
```

### Listar dias não-úteis em um período
```sql
SELECT tc.TRANSACTION_DATE,
       tc.DESCRIPTION
FROM   GL_TRANSACTION_CALENDAR tc
WHERE  tc.TRANSACTION_CALENDAR_NAME = :p_calendar_name
  AND  tc.BUSINESS_DAY_FLAG = 'N'
  AND  tc.TRANSACTION_DATE BETWEEN :start_date AND :end_date
ORDER BY tc.TRANSACTION_DATE;
```

### Próximo dia útil após uma data
```sql
SELECT MIN(tc.TRANSACTION_DATE) AS proximo_dia_util
FROM   GL_TRANSACTION_CALENDAR tc
WHERE  tc.TRANSACTION_CALENDAR_NAME = :p_calendar_name
  AND  tc.BUSINESS_DAY_FLAG = 'Y'
  AND  tc.TRANSACTION_DATE > :p_date;
```

### Filtros comuns
- `BUSINESS_DAY_FLAG = 'Y'` — Dias úteis
- `BUSINESS_DAY_FLAG = 'N'` — Dias não-úteis (feriados/fins de semana)
- `TRANSACTION_CALENDAR_NAME` — Selecionar calendário específico

---

## 🔒 Observações

- O calendário de transações é **opcional** no Oracle Fusion GL. Só é obrigatório quando Encumbrance Accounting está ativado.
- Cada dia do ano tem uma linha na tabela, com `BUSINESS_DAY_FLAG = 'Y'` ou `'N'`. Isso resulta em ~365 linhas por ano por calendário.
- Quando uma transação é registrada em dia não-útil e o calendário de transações está ativo, o Oracle automaticamente reatribui a transação para o próximo dia útil.
- Instituições financeiras brasileiras tipicamente precisam configurar feriados nacionais, estaduais (SP) e feriados bancários (ANBIMA) neste calendário.
- O calendário de transações é diferente do calendário contábil (`GL_PERIOD_SETS` / `GL_PERIODS`) — o calendário contábil define os períodos (meses), enquanto o transaction calendar define dias úteis dentro desses períodos.

---

## 🔗 PVOs Relacionados

### [[ledgerpvo|LedgerPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TransactionCalendarDescription | — |
| FRI_BUSINESS_DAY_FLAG | TransactionCalendarFriBusinessDayFlag | — |
| MON_BUSINESS_DAY_FLAG | TransactionCalendarMonBusinessDayFlag | — |
| NAME | TransactionCalendarName | — |
| SAT_BUSINESS_DAY_FLAG | TransactionCalendarSatBusinessDayFlag | — |
| SECURITY_FLAG | TransactionCalendarSecurityFlag | — |
| SUN_BUSINESS_DAY_FLAG | TransactionCalendarSunBusinessDayFlag | — |
| THU_BUSINESS_DAY_FLAG | TransactionCalendarThuBusinessDayFlag | — |
| TRANSACTION_CALENDAR_ID | TransactionCalendarTransactionCalendarId | — |
| TUE_BUSINESS_DAY_FLAG | TransactionCalendarTueBusinessDayFlag | — |
| WED_BUSINESS_DAY_FLAG | TransactionCalendarWedBusinessDayFlag | — |

### [[ledgersetpvo|LedgerSetPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | TransactionCalendarDescription | — |
| FRI_BUSINESS_DAY_FLAG | TransactionCalendarFriBusinessDayFlag | — |
| MON_BUSINESS_DAY_FLAG | TransactionCalendarMonBusinessDayFlag | — |
| NAME | TransactionCalendarName | — |
| SAT_BUSINESS_DAY_FLAG | TransactionCalendarSatBusinessDayFlag | — |
| SECURITY_FLAG | TransactionCalendarSecurityFlag | — |
| SUN_BUSINESS_DAY_FLAG | TransactionCalendarSunBusinessDayFlag | — |
| THU_BUSINESS_DAY_FLAG | TransactionCalendarThuBusinessDayFlag | — |
| TRANSACTION_CALENDAR_ID | TransactionCalendarTransactionCalendarId | — |
| TUE_BUSINESS_DAY_FLAG | TransactionCalendarTueBusinessDayFlag | — |
| WED_BUSINESS_DAY_FLAG | TransactionCalendarWedBusinessDayFlag | — |

---

## 📚 Referências

- [Oracle Docs — GL_TRANSACTION_CALENDAR](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
