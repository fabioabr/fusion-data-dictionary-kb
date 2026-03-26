---
id: DOC-GL-023
doc_type: system-doc
title: "GL_JE_LINES — Linhas de Lançamentos Contábeis"
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
  - journal-lines
  - lancamentos
  - contabilidade
aliases:
  - GL_JE_LINES
  - gl_je_lines
  - linhas-lancamentos
  - journal-lines
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_LINES

## 📌 Visão Geral

Armazena as **linhas de detalhe dos lançamentos contábeis** (journal entries) no General Ledger. Cada registro representa uma linha individual de um journal, contendo a conta contábil (CCID), valores a débito/crédito, moeda e descrição. É a tabela de maior granularidade transacional do GL — complementar ao header em [[gl_je_headers]].

> [!note] Tabela de alta volumetria
> Esta é uma das maiores tabelas transacionais do GL. Cada journal header pode ter centenas de linhas. O volume cresce proporcionalmente ao número de lançamentos contábeis da organização.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Lançamentos contábeis:** Detalhe de cada linha de débito/crédito de um journal entry.
- **Reconciliação:** Rastreamento de valores por conta, período e fonte.
- **Drill-down financeiro:** A partir de saldos em [[gl_balances]], rastrear os lançamentos que os compõem.
- **Auditoria:** Identificação de cada transação que afetou uma conta contábil.
- **Subledger Accounting:** Linhas geradas automaticamente pelo SLA a partir de AP, AR, FA etc.
- **Relatórios analíticos:** Agrupamento por conta, centro de custo, período e fonte.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_HEADER_ID | NUMBER(18) | NOT NULL | FK | Identificador do header do journal entry | [[gl_je_headers]] | 🟢 100% |
| 2 | JE_LINE_NUM | NUMBER(18) | NOT NULL | PK | Número sequencial da linha dentro do journal | — | 🟢 100% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger (livro contábil) | [[gl_ledgers]] | 🟢 100% |
| 4 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | FK | Combinação de contas contábeis (CCID) | [[gl_code_combinations]] | 🟢 100% |
| 5 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Nome do período contábil (ex: JAN-26) | — | 🟢 100% |
| 6 | EFFECTIVE_DATE | DATE | NOT NULL | Período | Data efetiva do lançamento (accounting date) | — | 🟢 100% |
| 7 | STATUS | VARCHAR2(1) | NOT NULL | Controle | Status da linha: U (Unposted), P (Posted) | — | 🟢 100% |
| 8 | ENTERED_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda da transação (entered) | — | 🟢 100% |
| 9 | ENTERED_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda da transação (entered) | — | 🟢 100% |
| 10 | ACCOUNTED_DR | NUMBER | NULL | Financeiro | Valor a débito na moeda funcional (accounted) | — | 🟢 100% |
| 11 | ACCOUNTED_CR | NUMBER | NULL | Financeiro | Valor a crédito na moeda funcional (accounted) | — | 🟢 100% |
| 12 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Classificação | Código da moeda da transação (ex: BRL, USD) | — | 🟢 100% |
| 13 | CURRENCY_CONVERSION_TYPE | VARCHAR2(30) | NULL | Conversão | Tipo de conversão cambial (Corporate, Spot, User) | — | 🟢 95% |
| 14 | CURRENCY_CONVERSION_DATE | DATE | NULL | Conversão | Data da taxa de conversão cambial | — | 🟢 95% |
| 15 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Conversão | Taxa de conversão utilizada | — | 🟢 95% |
| 16 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual da linha do lançamento | — | 🟢 100% |
| 17 | REFERENCE_1 | VARCHAR2(240) | NULL | Referência | Referência genérica 1 (batch name, subledger ref) | — | 🟢 90% |
| 18 | REFERENCE_2 | VARCHAR2(240) | NULL | Referência | Referência genérica 2 | — | 🟢 90% |
| 19 | REFERENCE_4 | VARCHAR2(240) | NULL | Referência | Referência 4 — tipicamente journal name | — | 🟢 90% |
| 20 | REFERENCE_5 | VARCHAR2(240) | NULL | Referência | Referência 5 — tipicamente line description do subledger | — | 🟢 90% |
| 21 | REFERENCE_10 | VARCHAR2(240) | NULL | Referência | Referência 10 — tipicamente ID do documento original do subledger | — | 🟢 90% |
| 22 | ATTRIBUTE_CATEGORY | VARCHAR2(150) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟡 80% |
| 23 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Campos de atributo descritivo (DFF) configuráveis | — | 🟡 80% |
| 24 | TAX_CODE_ID | NUMBER(18) | NULL | FK | Identificador do código tributário, se aplicável | — | 🟡 70% |
| 25 | SUBLEDGER_DOC_SEQUENCE_VALUE | NUMBER | NULL | Referência | Número sequencial do documento no subledger de origem | — | 🟡 75% |
| 26 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 27 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 29 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_headers]] — via `JE_HEADER_ID` (header do journal entry)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (combinação de contas)

### Tabelas-filha (FK de saída)
- [[gl_je_lines_recon]] — via `JE_HEADER_ID` + `JE_LINE_NUM` (reconciliação de linhas)
- [[gl_import_references]] — via `JE_HEADER_ID` + `JE_LINE_NUM` (referências de importação do subledger)

---

## 📎 Uso Típico

### Consultar linhas de um journal entry
```sql
SELECT jl.JE_LINE_NUM,
       gcc.SEGMENT1 || '.' || gcc.SEGMENT2 || '.' || gcc.SEGMENT3 AS conta,
       jl.ENTERED_DR,
       jl.ENTERED_CR,
       jl.ACCOUNTED_DR,
       jl.ACCOUNTED_CR,
       jl.DESCRIPTION
FROM   GL_JE_LINES jl
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = jl.CODE_COMBINATION_ID
WHERE  jl.JE_HEADER_ID = :p_header_id
ORDER BY jl.JE_LINE_NUM;
```

### Lançamentos postados em uma conta no período
```sql
SELECT jh.NAME AS journal_name,
       jl.JE_LINE_NUM,
       jl.EFFECTIVE_DATE,
       jl.ENTERED_DR,
       jl.ENTERED_CR,
       jl.DESCRIPTION
FROM   GL_JE_LINES jl
JOIN   GL_JE_HEADERS jh ON jh.JE_HEADER_ID = jl.JE_HEADER_ID
WHERE  jl.CODE_COMBINATION_ID = :p_ccid
  AND  jl.LEDGER_ID = :p_ledger_id
  AND  jl.PERIOD_NAME = 'MAR-26'
  AND  jl.STATUS = 'P'
ORDER BY jl.EFFECTIVE_DATE, jl.JE_HEADER_ID;
```

### Filtros comuns
- `STATUS = 'P'` — Apenas linhas postadas (Posted)
- `STATUS = 'U'` — Linhas não postadas (Unposted)
- `CURRENCY_CODE = 'BRL'` — Transações em moeda funcional
- `ENTERED_DR IS NOT NULL` — Apenas linhas de débito

---

## 🔒 Observações

- A PK composta é `JE_HEADER_ID` + `JE_LINE_NUM`. Não há um ID único de linha isolado.
- Os valores `ENTERED_*` são na moeda da transação; `ACCOUNTED_*` são na moeda funcional do ledger. Em transações single-currency (BRL→BRL), ambos são iguais.
- Os campos `REFERENCE_*` contêm informações do subledger de origem (AP, AR, FA) — essenciais para drill-down até o documento original.
- `EFFECTIVE_DATE` é a data contábil (accounting date), que pode diferir da data da transação no subledger.
- Linhas com `STATUS = 'U'` ainda não foram postadas e não afetam os saldos em [[gl_balances]].

---

## 📚 Referências

- [Oracle Docs — GL_JE_LINES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljelines-25050.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
