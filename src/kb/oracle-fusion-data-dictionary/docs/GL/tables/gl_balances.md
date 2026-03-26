---
id: DOC-GL-001
doc_type: system-doc
title: "GL_BALANCES — Saldos Contábeis"
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
  - saldos
  - balances
  - contabilidade
aliases:
  - GL_BALANCES
  - gl_balances
  - saldos-contabeis
  - balances-gl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_BALANCES

## 📌 Visão Geral

Armazena os **saldos contábeis** de todas as combinações de conta (CCID) por período, moeda e tipo de saldo. É a tabela central de consulta financeira do General Ledger — toda consulta de balancete, DRE, balanço patrimonial ou relatório financeiro começa por ela. Cada registro representa o saldo de uma conta em um período específico.

> [!note] Tabela de alta volumetria
> Esta é uma das maiores tabelas do GL. Os saldos são armazenados por período (mês), moeda e tipo de saldo (Actual, Budget, Encumbrance), resultando em múltiplas linhas por combinação de conta.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Balancete:** Consulta de saldos por conta contábil, centro de custo ou segmento.
- **DRE e Balanço:** Base para geração de demonstrativos financeiros.
- **Reconciliação:** Comparação de saldos entre subledgers (AR, AP) e o GL.
- **Análise gerencial:** Saldos por período para análise de tendências e variações.
- **Budget vs Actual:** Comparação de saldos reais com orçamento.
- **Auditoria:** Rastreamento de saldos históricos por período.

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
| 2 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 3 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Classificação | Código da moeda do saldo (ex: BRL, USD) | — | 🟢 100% |
| 4 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Nome do período contábil (ex: JAN-26, FEB-26) | — | 🟢 100% |
| 5 | ACTUAL_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Tipo de saldo: A (Actual/Real), B (Budget/Orçamento), E (Encumbrance/Reserva) | — | 🟢 100% |
| 6 | BUDGET_VERSION_ID | NUMBER(18) | NULL | FK | Versão do orçamento (quando ACTUAL_FLAG = 'B') | — | 🟢 100% |
| 7 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de reserva (quando ACTUAL_FLAG = 'E') | [[gl_encumbrance_types_b]] | 🟢 100% |
| 8 | PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Período | Tipo de período (Month, Quarter, Year) | — | 🟢 100% |
| 9 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano do período contábil | — | 🟢 100% |
| 10 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano | — | 🟢 100% |
| 11 | PERIOD_NET_DR | NUMBER | NULL | Financeiro | Valor líquido a débito no período (moeda da transação) | — | 🟢 100% |
| 12 | PERIOD_NET_CR | NUMBER | NULL | Financeiro | Valor líquido a crédito no período (moeda da transação) | — | 🟢 100% |
| 13 | PERIOD_NET_DR_BEQ | NUMBER | NULL | Financeiro | Valor líquido a débito — moeda funcional (base equivalent) | — | 🟢 100% |
| 14 | PERIOD_NET_CR_BEQ | NUMBER | NULL | Financeiro | Valor líquido a crédito — moeda funcional (base equivalent) | — | 🟢 100% |
| 15 | BEGIN_BALANCE_DR | NUMBER | NULL | Financeiro | Saldo inicial a débito (acumulado desde abertura) | — | 🟢 100% |
| 16 | BEGIN_BALANCE_CR | NUMBER | NULL | Financeiro | Saldo inicial a crédito (acumulado desde abertura) | — | 🟢 100% |
| 17 | BEGIN_BALANCE_DR_BEQ | NUMBER | NULL | Financeiro | Saldo inicial a débito — moeda funcional | — | 🟢 100% |
| 18 | BEGIN_BALANCE_CR_BEQ | NUMBER | NULL | Financeiro | Saldo inicial a crédito — moeda funcional | — | 🟢 100% |
| 19 | QUARTER_TO_DATE_DR | NUMBER | NULL | Financeiro | Acumulado a débito no trimestre | — | 🟡 75% |
| 20 | QUARTER_TO_DATE_CR | NUMBER | NULL | Financeiro | Acumulado a crédito no trimestre | — | 🟡 75% |
| 21 | PROJECT_TO_DATE_DR | NUMBER | NULL | Financeiro | Acumulado a débito do projeto | — | 🟡 70% |
| 22 | PROJECT_TO_DATE_CR | NUMBER | NULL | Financeiro | Acumulado a crédito do projeto | — | 🟡 70% |
| 23 | TRANSLATED_FLAG | VARCHAR2(1) | NULL | Controle | Indica se o saldo foi convertido para moeda de reporte (Y/N/R) | — | 🟢 100% |
| 24 | TEMPLATE_ID | NUMBER(18) | NULL | Sistema | ID do template de alocação, se aplicável | — | 🟡 70% |
| 25 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 26 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 27 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 28 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (combinação de contas)
- [[gl_encumbrance_types_b]] — via `ENCUMBRANCE_TYPE_ID` (tipo de reserva)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de saldos consolidados (leaf table).

---

## 📎 Uso Típico

### Saldo de uma conta em um período
```sql
SELECT b.PERIOD_NAME,
       b.CURRENCY_CODE,
       (b.BEGIN_BALANCE_DR - b.BEGIN_BALANCE_CR) AS saldo_inicial,
       (b.PERIOD_NET_DR - b.PERIOD_NET_CR) AS movimento_periodo,
       (b.BEGIN_BALANCE_DR + b.PERIOD_NET_DR) - (b.BEGIN_BALANCE_CR + b.PERIOD_NET_CR) AS saldo_final
FROM   GL_BALANCES b
WHERE  b.CODE_COMBINATION_ID = :p_ccid
  AND  b.LEDGER_ID = :p_ledger_id
  AND  b.ACTUAL_FLAG = 'A'
  AND  b.CURRENCY_CODE = 'BRL'
  AND  b.PERIOD_NAME = 'MAR-26';
```

### Balancete por segmento (centro de custo)
```sql
SELECT gcc.SEGMENT3 AS centro_custo,
       SUM(b.BEGIN_BALANCE_DR + b.PERIOD_NET_DR) - SUM(b.BEGIN_BALANCE_CR + b.PERIOD_NET_CR) AS saldo
FROM   GL_BALANCES b
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = b.CODE_COMBINATION_ID
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.ACTUAL_FLAG = 'A'
  AND  b.CURRENCY_CODE = 'BRL'
  AND  b.PERIOD_NAME = 'MAR-26'
GROUP BY gcc.SEGMENT3
ORDER BY gcc.SEGMENT3;
```

### Filtros comuns
- `ACTUAL_FLAG = 'A'` — Saldos reais (Actual)
- `ACTUAL_FLAG = 'B'` — Saldos orçamentários (Budget)
- `ACTUAL_FLAG = 'E'` — Reservas (Encumbrance)
- `CURRENCY_CODE = 'BRL'` — Moeda funcional

---

## 🔒 Observações

- O saldo final de uma conta é calculado como `(BEGIN_BALANCE_DR + PERIOD_NET_DR) - (BEGIN_BALANCE_CR + PERIOD_NET_CR)`.
- Os campos `_BEQ` (Base Equivalent) contêm valores na moeda funcional do ledger — usar quando há transações multi-moeda.
- `ACTUAL_FLAG` = 'A' para saldos reais, 'B' para budget, 'E' para encumbrance. A maioria das consultas financeiras usa 'A'.
- Os saldos são **acumulados** — `BEGIN_BALANCE` é o saldo desde a abertura do exercício. `PERIOD_NET` é o movimento do período.
- `TRANSLATED_FLAG` indica se houve conversão para moeda de reporte (subsidiárias com moeda diferente da matriz).

---

## 📚 Referências

- [Oracle Docs — GL_BALANCES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glbalances-25702.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
