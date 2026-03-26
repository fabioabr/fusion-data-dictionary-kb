---
id: DOC-GL-007
doc_type: system-doc
title: "GL_BUDGET_BALANCES — Saldos Orçamentários"
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
  - orcamento
  - budget
  - saldos
aliases:
  - GL_BUDGET_BALANCES
  - gl_budget_balances
  - saldos-orcamentarios
  - budget-balances-gl
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_BUDGET_BALANCES

## Visao Geral

Armazena os **saldos orçamentários** por conta contábil, período e moeda no General Ledger. Cada registro representa o valor orçado para uma combinação de conta (CCID) em um período específico, vinculado a um orçamento e sua versão. É a tabela central para análises de **Budget vs Actual** e controle orçamentário.

> [!note] Relação com GL_BALANCES
> Os saldos orçamentários também podem ser consultados via [[gl_balances]] com `ACTUAL_FLAG = 'B'`. Esta tabela dedicada oferece colunas adicionais específicas de orçamento, como versão e organização orçamentária.

---

## Proposito de Negocio

Esta tabela é utilizada nos seguintes processos:

- **Controle orçamentário:** Acompanhamento de valores orçados por conta contábil e período.
- **Budget vs Actual:** Comparação entre valores orçados e realizados para análise de variações.
- **Planejamento financeiro:** Base para revisões orçamentárias e projeções.
- **Relatórios gerenciais:** Geração de relatórios de consumo orçamentário por departamento ou projeto.
- **Aprovação de despesas:** Validação de disponibilidade orçamentária antes de autorizar gastos.
- **Auditoria:** Registro histórico de saldos orçamentários por versão e período.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 95% |
| 2 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 95% |
| 3 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Classificação | Código da moeda do saldo orçado | — | 🟢 95% |
| 4 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Nome do período contábil (ex: JAN-26) | — | 🟢 95% |
| 5 | BUDGET_VERSION_ID | NUMBER(18) | NOT NULL | FK | Versão do orçamento | — | 🟢 90% |
| 6 | BUDGET_NAME | VARCHAR2(15) | NULL | Identificação | Nome do orçamento | — | 🟢 85% |
| 7 | PERIOD_YEAR | NUMBER(15) | NOT NULL | Período | Ano do período contábil | — | 🟢 90% |
| 8 | PERIOD_NUM | NUMBER(15) | NOT NULL | Período | Número sequencial do período no ano | — | 🟢 90% |
| 9 | PERIOD_NET_DR | NUMBER | NULL | Financeiro | Valor líquido a débito orçado no período | — | 🟢 90% |
| 10 | PERIOD_NET_CR | NUMBER | NULL | Financeiro | Valor líquido a crédito orçado no período | — | 🟢 90% |
| 11 | BEGIN_BALANCE_DR | NUMBER | NULL | Financeiro | Saldo inicial a débito (acumulado) | — | 🟢 85% |
| 12 | BEGIN_BALANCE_CR | NUMBER | NULL | Financeiro | Saldo inicial a crédito (acumulado) | — | 🟢 85% |
| 13 | QUARTER_TO_DATE_DR | NUMBER | NULL | Financeiro | Acumulado a débito no trimestre | — | 🟡 70% |
| 14 | QUARTER_TO_DATE_CR | NUMBER | NULL | Financeiro | Acumulado a crédito no trimestre | — | 🟡 70% |
| 15 | PROJECT_TO_DATE_DR | NUMBER | NULL | Financeiro | Acumulado a débito do projeto | — | 🟡 65% |
| 16 | PROJECT_TO_DATE_CR | NUMBER | NULL | Financeiro | Acumulado a crédito do projeto | — | 🟡 65% |
| 17 | BUDGET_ENTITY_ID | NUMBER(18) | NULL | FK | ID da entidade orçamentária | — | 🟡 70% |
| 18 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 19 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 20 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 21 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger ao qual o saldo orçamentário pertence)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (combinação de contas)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de saldos (leaf table).

---

## Uso Tipico

### Saldo orçado por conta e período
```sql
SELECT bb.PERIOD_NAME, bb.CURRENCY_CODE,
       bb.PERIOD_NET_DR, bb.PERIOD_NET_CR,
       (bb.PERIOD_NET_DR - bb.PERIOD_NET_CR) AS orcado_liquido
FROM   GL_BUDGET_BALANCES bb
WHERE  bb.CODE_COMBINATION_ID = :p_ccid
  AND  bb.LEDGER_ID = :p_ledger_id
  AND  bb.BUDGET_VERSION_ID = :p_budget_version_id
  AND  bb.CURRENCY_CODE = 'BRL'
ORDER BY bb.PERIOD_YEAR, bb.PERIOD_NUM;
```

### Budget vs Actual
```sql
SELECT bb.PERIOD_NAME,
       (bb.PERIOD_NET_DR - bb.PERIOD_NET_CR) AS orcado,
       (b.PERIOD_NET_DR - b.PERIOD_NET_CR) AS realizado,
       (b.PERIOD_NET_DR - b.PERIOD_NET_CR) - (bb.PERIOD_NET_DR - bb.PERIOD_NET_CR) AS variacao
FROM   GL_BUDGET_BALANCES bb
JOIN   GL_BALANCES b ON b.CODE_COMBINATION_ID = bb.CODE_COMBINATION_ID
                    AND b.LEDGER_ID = bb.LEDGER_ID
                    AND b.PERIOD_NAME = bb.PERIOD_NAME
                    AND b.CURRENCY_CODE = bb.CURRENCY_CODE
                    AND b.ACTUAL_FLAG = 'A'
WHERE  bb.CODE_COMBINATION_ID = :p_ccid
  AND  bb.LEDGER_ID = :p_ledger_id
  AND  bb.CURRENCY_CODE = 'BRL';
```

### Filtros comuns
- `BUDGET_VERSION_ID = :p_version` — Filtrar por versão de orçamento
- `CURRENCY_CODE = 'BRL'` — Moeda funcional
- `PERIOD_YEAR = 2026` — Ano fiscal específico

---

## Observacoes

- O `BUDGET_VERSION_ID` distingue diferentes versões do mesmo orçamento (ex: versão original, revisão 1, revisão 2).
- Os campos `BEGIN_BALANCE_DR/CR` representam o saldo acumulado do orçamento desde o início do exercício, enquanto `PERIOD_NET_DR/CR` é o valor orçado apenas para aquele período.
- Para comparação Budget vs Actual, cruzar com [[gl_balances]] usando `CODE_COMBINATION_ID`, `LEDGER_ID`, `PERIOD_NAME` e `CURRENCY_CODE`.
- Em implementações que usam Oracle Planning (EPBCS), os orçamentos podem ser carregados via integração, e esta tabela reflete os valores importados.
- Diferentemente de [[gl_balances]], esta tabela armazena exclusivamente saldos de orçamento — não há flag de tipo.

---

## Referencias

- [Oracle Docs — GL_BUDGET_BALANCES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glbudgetbalances-25708.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
