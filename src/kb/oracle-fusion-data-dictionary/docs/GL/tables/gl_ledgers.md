---
id: DOC-GL-027
doc_type: system-doc
title: "GL_LEDGERS — Ledgers (Livros Contábeis)"
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
  - ledger
  - livro-contabil
  - configuracao
aliases:
  - GL_LEDGERS
  - gl_ledgers
  - ledgers
  - livros-contabeis
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_LEDGERS

## 📌 Visão Geral

Armazena a definição dos **ledgers (livros contábeis)** do General Ledger. É a tabela central de configuração do GL — define o plano de contas, moeda funcional, calendário contábil e método de subledger accounting para cada livro. Praticamente toda tabela transacional do GL referencia `LEDGER_ID` desta tabela. Suporta Primary Ledger, Secondary Ledger e Reporting Currency.

> [!note] Tabela central do GL
> Esta é a tabela mais referenciada do módulo GL. O `LEDGER_ID` é FK em [[gl_balances]], [[gl_je_headers]], [[gl_je_lines]], [[gl_periods]] e dezenas de outras tabelas do ERP.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração do GL:** Definição dos livros contábeis da organização (primary, secondary, reporting).
- **Multi-book accounting:** Suporte a múltiplos livros contábeis com diferentes planos de contas e moedas.
- **Consolidação:** Identificação dos ledgers para consolidação financeira.
- **Relatórios financeiros:** Filtro obrigatório por ledger em todas as consultas contábeis.
- **Subledger Accounting:** Configuração do método de contabilização (Standard Accrual, Cash etc.).
- **Compliance regulatório:** Ledgers separados para IFRS vs BRGAAP quando necessário.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LEDGER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do ledger | — | 🟢 100% |
| 2 | NAME | VARCHAR2(30) | NOT NULL | Identificação | Nome do ledger (ex: "Patria Primary Ledger") | — | 🟢 100% |
| 3 | SHORT_NAME | VARCHAR2(20) | NOT NULL | Identificação | Nome curto/código do ledger | — | 🟢 100% |
| 4 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual do ledger | — | 🟢 100% |
| 5 | LEDGER_CATEGORY_CODE | VARCHAR2(30) | NOT NULL | Classificação | Categoria: PRIMARY, SECONDARY, ALC (Reporting Currency), NONE | — | 🟢 100% |
| 6 | OBJECT_TYPE_CODE | VARCHAR2(1) | NOT NULL | Classificação | Tipo de objeto: L (Ledger), S (Ledger Set) | — | 🟢 95% |
| 7 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NOT NULL | FK | ID da estrutura do plano de contas (Key Flexfield) | — | 🟢 100% |
| 8 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Classificação | Moeda funcional do ledger (ex: BRL, USD) | — | 🟢 100% |
| 9 | PERIOD_SET_NAME | VARCHAR2(15) | NOT NULL | FK | Nome do calendário contábil (period set) | — | 🟢 100% |
| 10 | ACCOUNTED_PERIOD_TYPE | VARCHAR2(15) | NOT NULL | Classificação | Tipo de período contábil (Month, Quarter, Year) | — | 🟢 100% |
| 11 | FIRST_LEDGER_PERIOD_NAME | VARCHAR2(15) | NULL | Período | Primeiro período contábil do ledger | — | 🟢 90% |
| 12 | RET_EARN_CODE_COMBINATION_ID | NUMBER(18) | NULL | FK | CCID da conta de lucros/prejuízos acumulados (retained earnings) | [[gl_code_combinations]] | 🟢 95% |
| 13 | SLA_ACCOUNTING_METHOD_CODE | VARCHAR2(30) | NULL | Classificação | Método de contabilização SLA (Standard Accrual, Cash etc.) | — | 🟢 95% |
| 14 | SLA_ACCOUNTING_METHOD_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo do método SLA | — | 🟢 90% |
| 15 | SUSPENSE_ALLOWED_FLAG | VARCHAR2(1) | NULL | Controle | Permite lançamentos em conta suspense quando desbalanceado (Y/N) | — | 🟢 95% |
| 16 | ALLOW_INTERCOMPANY_POST_FLAG | VARCHAR2(1) | NULL | Controle | Permite lançamentos intercompany (Y/N) | — | 🟢 90% |
| 17 | ENABLE_AVERAGE_BALANCES_FLAG | VARCHAR2(1) | NULL | Controle | Habilita saldos médios diários (Y/N) | — | 🟢 90% |
| 18 | ENABLE_BUDGETARY_CONTROL_FLAG | VARCHAR2(1) | NULL | Controle | Habilita controle orçamentário (Y/N) | — | 🟢 95% |
| 19 | REQUIRE_BUDGET_JOURNALS_FLAG | VARCHAR2(1) | NULL | Controle | Requer journals de budget (Y/N) | — | 🟡 80% |
| 20 | ENABLE_JE_APPROVAL_FLAG | VARCHAR2(1) | NULL | Controle | Habilita workflow de aprovação de journals (Y/N) | — | 🟢 90% |
| 21 | ENABLE_AUTOMATIC_TAX_FLAG | VARCHAR2(1) | NULL | Controle | Habilita cálculo automático de imposto (Y/N) | — | 🟡 80% |
| 22 | CONSOLIDATION_LEDGER_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é ledger de consolidação (Y/N) | — | 🟢 90% |
| 23 | TRANSLATE_INTERCOMPANY_FLAG | VARCHAR2(1) | NULL | Controle | Traduzir transações intercompany (Y/N) | — | 🟡 75% |
| 24 | BAL_SEG_VALUE_OPTION_CODE | VARCHAR2(25) | NULL | Classificação | Opção de balancing segment: A (All Values), I (Selected Values) | — | 🟢 90% |
| 25 | BAL_SEG_COLUMN_NAME | VARCHAR2(25) | NULL | Classificação | Nome da coluna do balancing segment (ex: SEGMENT1) | — | 🟢 90% |
| 26 | MGT_SEG_COLUMN_NAME | VARCHAR2(25) | NULL | Classificação | Nome da coluna do management segment (ex: SEGMENT3) | — | 🟢 90% |
| 27 | COMPLETION_STATUS_CODE | VARCHAR2(1) | NULL | Controle | Status de completude da configuração do ledger | — | 🟡 75% |
| 28 | CONFIGURATION_ID | NUMBER(18) | NULL | FK | ID da configuração do ledger | [[gl_ledger_config_details]] | 🟡 80% |
| 29 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 30 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 31 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 32 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_code_combinations]] — via `RET_EARN_CODE_COMBINATION_ID` (conta de lucros acumulados)
- [[gl_ledger_config_details]] — via `CONFIGURATION_ID` (configuração do ledger)

### Tabelas-filha (FK de saída)
- [[gl_balances]] — via `LEDGER_ID` (saldos contábeis)
- [[gl_je_headers]] — via `LEDGER_ID` (headers de journals)
- [[gl_je_lines]] — via `LEDGER_ID` (linhas de journals)
- [[gl_ledger_segment_values]] — via `LEDGER_ID` (valores de segmento do ledger)
- [[gl_ledger_set_assignments]] — via `LEDGER_ID` (atribuições de ledger sets)
- [[gl_legal_entities_bsvs]] — via `LEDGER_ID` (BSVs por entidade legal)
- [[gl_periods]] — via `PERIOD_SET_NAME` (períodos contábeis)

---

## 📎 Uso Típico

### Listar todos os ledgers da organização
```sql
SELECT gl.LEDGER_ID,
       gl.NAME,
       gl.SHORT_NAME,
       gl.LEDGER_CATEGORY_CODE,
       gl.CURRENCY_CODE,
       gl.PERIOD_SET_NAME,
       gl.SLA_ACCOUNTING_METHOD_CODE
FROM   GL_LEDGERS gl
WHERE  gl.OBJECT_TYPE_CODE = 'L'
ORDER BY gl.LEDGER_CATEGORY_CODE, gl.NAME;
```

### Identificar o primary ledger e seus secondary ledgers
```sql
SELECT gl.LEDGER_ID,
       gl.NAME,
       gl.LEDGER_CATEGORY_CODE,
       gl.CURRENCY_CODE,
       gl.CHART_OF_ACCOUNTS_ID
FROM   GL_LEDGERS gl
WHERE  gl.LEDGER_CATEGORY_CODE IN ('PRIMARY', 'SECONDARY')
  AND  gl.OBJECT_TYPE_CODE = 'L'
ORDER BY gl.LEDGER_CATEGORY_CODE;
```

### Filtros comuns
- `OBJECT_TYPE_CODE = 'L'` — Apenas ledgers (não ledger sets)
- `LEDGER_CATEGORY_CODE = 'PRIMARY'` — Primary ledger
- `LEDGER_CATEGORY_CODE = 'SECONDARY'` — Secondary ledger
- `LEDGER_CATEGORY_CODE = 'ALC'` — Reporting currency (Automatic Ledger Currency)
- `CURRENCY_CODE = 'BRL'` — Ledgers em Real

---

## 🔒 Observações

- `LEDGER_ID` é a FK mais comum do módulo GL — presente em praticamente todas as tabelas transacionais.
- `LEDGER_CATEGORY_CODE` distingue: **PRIMARY** (livro principal), **SECONDARY** (livro secundário com regras contábeis diferentes), **ALC** (moeda de reporte).
- `OBJECT_TYPE_CODE = 'S'` indica um Ledger Set (agrupamento lógico de ledgers) — não é um ledger real, mas uma abstração para simplificar atribuições.
- O `CHART_OF_ACCOUNTS_ID` define qual estrutura de plano de contas o ledger usa — pode variar entre primary e secondary ledgers.
- `RET_EARN_CODE_COMBINATION_ID` aponta para a conta de lucros/prejuízos acumulados — usada no fechamento anual para transferir o resultado.
- A configuração do ledger é feita uma única vez no setup inicial — alterações posteriores têm impacto significativo.

---

## 📚 Referências

- [Oracle Docs — GL_LEDGERS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glledgers-25358.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
