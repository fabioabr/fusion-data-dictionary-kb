---
id: DOC-GL-022
doc_type: system-doc
title: "GL_JE_HEADERS — Cabeçalhos de Lançamentos Contábeis"
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
  - lancamentos
  - journal-entries
  - journal-headers
aliases:
  - GL_JE_HEADERS
  - gl_je_headers
  - cabecalhos-lancamento-gl
  - journal-headers
  - journal-entries
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_JE_HEADERS

## 📌 Visão Geral

Armazena os **cabeçalhos de lançamentos contábeis** (journal entries) do General Ledger. Cada registro representa um journal individual com seu nome, categoria, fonte, período, moeda e status. É o nível intermediário da hierarquia de lançamentos: Batch → **Header** → Lines. Esta é uma das tabelas mais consultadas do GL para análise de lançamentos.

> [!note] Hierarquia de lançamentos
> A estrutura de lançamentos no GL segue três níveis: **GL_JE_BATCHES** (lote) → **GL_JE_HEADERS** (cabeçalho/journal) → **GL_JE_LINES** (linhas/partidas). Um journal pertence a exatamente um lote e contém múltiplas linhas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Lançamentos contábeis:** Registro de todos os journals (manuais e importados de subledgers).
- **Classificação:** Categorização dos lançamentos por fonte (source) e categoria (category).
- **Workflow de aprovação:** Controle de status individual do journal dentro do lote.
- **Reconciliação:** Identificação de lançamentos por período, moeda e origem.
- **Reversão:** Journals podem ser revertidos individualmente, com referência ao header original.
- **Auditoria:** Rastreamento completo de quem criou o lançamento, quando e de qual fonte.
- **Relatórios gerenciais:** Análise de volumes e valores por categoria, fonte e período.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JE_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cabeçalho do lançamento | — | 🟢 100% |
| 2 | JE_BATCH_ID | NUMBER(18) | NOT NULL | FK | ID do lote ao qual o journal pertence | [[gl_je_batches]] | 🟢 100% |
| 3 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 100% |
| 4 | NAME | VARCHAR2(100) | NOT NULL | Identificação | Nome do journal (visível ao usuário) | — | 🟢 100% |
| 5 | JE_CATEGORY | VARCHAR2(25) | NOT NULL | FK | Categoria do lançamento | [[gl_je_categories_b]] | 🟢 100% |
| 6 | JE_SOURCE | VARCHAR2(25) | NOT NULL | FK | Fonte do lançamento (ex: Manual, Payables, Receivables) | [[gl_je_sources_b]] | 🟢 100% |
| 7 | PERIOD_NAME | VARCHAR2(15) | NOT NULL | Período | Período contábil do lançamento | — | 🟢 100% |
| 8 | DEFAULT_EFFECTIVE_DATE | DATE | NOT NULL | Data | Data efetiva padrão (GL Date) | — | 🟢 100% |
| 9 | STATUS | VARCHAR2(1) | NOT NULL | Classificação | Status do journal: U (Unposted), P (Posted), S (Selected), I (Error) | — | 🟢 100% |
| 10 | ACTUAL_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Tipo: A (Actual), B (Budget), E (Encumbrance) | — | 🟢 100% |
| 11 | CURRENCY_CODE | VARCHAR2(15) | NOT NULL | Financeiro | Código da moeda do lançamento (ex: BRL, USD) | — | 🟢 100% |
| 12 | CURRENCY_CONVERSION_RATE | NUMBER | NULL | Financeiro | Taxa de câmbio aplicada | — | 🟢 95% |
| 13 | CURRENCY_CONVERSION_TYPE | VARCHAR2(30) | NULL | Financeiro | Tipo de taxa de câmbio (ex: Corporate, Spot, User) | — | 🟢 95% |
| 14 | CURRENCY_CONVERSION_DATE | DATE | NULL | Financeiro | Data da taxa de câmbio | — | 🟢 95% |
| 15 | RUNNING_TOTAL_DR | NUMBER | NULL | Financeiro | Total acumulado a débito do journal | — | 🟢 95% |
| 16 | RUNNING_TOTAL_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito do journal | — | 🟢 95% |
| 17 | RUNNING_TOTAL_ACCOUNTED_DR | NUMBER | NULL | Financeiro | Total acumulado a débito — moeda funcional | — | 🟡 80% |
| 18 | RUNNING_TOTAL_ACCOUNTED_CR | NUMBER | NULL | Financeiro | Total acumulado a crédito — moeda funcional | — | 🟡 80% |
| 19 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição do journal | — | 🟢 100% |
| 20 | CONTROL_TOTAL | NUMBER | NULL | Financeiro | Total de controle informado pelo usuário | — | 🟢 95% |
| 21 | ACCRUAL_REV_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é um journal de reversão de accrual (Y/N) | — | 🟢 90% |
| 22 | ACCRUAL_REV_PERIOD_NAME | VARCHAR2(15) | NULL | Período | Período da reversão de accrual | — | 🟢 90% |
| 23 | ACCRUAL_REV_EFFECTIVE_DATE | DATE | NULL | Data | Data efetiva da reversão de accrual | — | 🟢 90% |
| 24 | REVERSED_JE_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | ID do header original (quando este é um journal de reversão) | [[gl_je_headers]] | 🟢 90% |
| 25 | REVERSAL_FLAG | VARCHAR2(1) | NULL | Controle | Indica se é um journal de reversão (Y/N) | — | 🟢 90% |
| 26 | REVERSAL_PERIOD | VARCHAR2(15) | NULL | Período | Período em que a reversão foi efetuada | — | 🟢 90% |
| 27 | REVERSAL_METHOD | VARCHAR2(1) | NULL | Classificação | Método de reversão: C (Change sign), S (Switch DR/CR) | — | 🟡 80% |
| 28 | EXTERNAL_REFERENCE | VARCHAR2(80) | NULL | Referência cruzada | Referência externa (ex: número do documento no sistema de origem) | — | 🟢 90% |
| 29 | POSTED_DATE | DATE | NULL | Data | Data em que o journal foi postado | — | 🟢 100% |
| 30 | DOC_SEQUENCE_ID | NUMBER(18) | NULL | Identificação | ID da sequência de documento | [[fnd_document_sequences]] | 🟢 90% |
| 31 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 90% |
| 32 | TAX_STATUS_CODE | VARCHAR2(1) | NULL | Classificação | Status fiscal do lançamento | — | 🟡 70% |
| 33 | BUDGET_VERSION_ID | NUMBER(18) | NULL | FK | Versão do orçamento (quando ACTUAL_FLAG = 'B') | — | 🟢 90% |
| 34 | ENCUMBRANCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de reserva (quando ACTUAL_FLAG = 'E') | [[gl_encumbrance_types_b]] | 🟢 90% |
| 35 | PARENT_JE_HEADER_ID | NUMBER(18) | NULL | Referência cruzada | ID do header pai (em caso de alocação ou geração automática) | [[gl_je_headers]] | 🟡 75% |
| 36 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 80% |
| 37 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 38 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 39 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 40 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 41 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |
| 42 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 100% |
| 43 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_je_batches]] — via `JE_BATCH_ID` (lote ao qual pertence)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_je_categories_b]] — via `JE_CATEGORY` (categoria do lançamento)
- [[gl_je_sources_b]] — via `JE_SOURCE` (fonte do lançamento)
- [[gl_je_headers]] — via `REVERSED_JE_HEADER_ID` (journal original em reversões — auto-referência)
- [[gl_je_headers]] — via `PARENT_JE_HEADER_ID` (journal pai — auto-referência)
- [[gl_encumbrance_types_b]] — via `ENCUMBRANCE_TYPE_ID` (tipo de reserva)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit proprietária do journal)

### Tabelas-filha (FK de saída)
- [[gl_je_lines]] — via `JE_HEADER_ID` (linhas do lançamento)
- [[gl_import_references]] — via `JE_HEADER_ID` (referências de importação/subledger)

---

## 📎 Uso Típico

### Journals de um período por categoria
```sql
SELECT h.JE_HEADER_ID, h.NAME, h.JE_CATEGORY, h.JE_SOURCE,
       h.STATUS, h.CURRENCY_CODE,
       h.RUNNING_TOTAL_DR, h.RUNNING_TOTAL_CR
FROM   GL_JE_HEADERS h
WHERE  h.LEDGER_ID = :p_ledger_id
  AND  h.PERIOD_NAME = 'MAR-26'
  AND  h.ACTUAL_FLAG = 'A'
ORDER BY h.JE_CATEGORY, h.NAME;
```

### Journals não postados pendentes
```sql
SELECT h.NAME, h.JE_CATEGORY, h.JE_SOURCE,
       h.DEFAULT_EFFECTIVE_DATE,
       h.RUNNING_TOTAL_DR, h.RUNNING_TOTAL_CR
FROM   GL_JE_HEADERS h
WHERE  h.LEDGER_ID = :p_ledger_id
  AND  h.STATUS = 'U'
  AND  h.PERIOD_NAME = 'MAR-26'
ORDER BY h.DEFAULT_EFFECTIVE_DATE;
```

### Journals de reversão
```sql
SELECT h.NAME AS reversal_journal,
       h.REVERSED_JE_HEADER_ID,
       orig.NAME AS original_journal,
       h.REVERSAL_METHOD
FROM   GL_JE_HEADERS h
JOIN   GL_JE_HEADERS orig ON orig.JE_HEADER_ID = h.REVERSED_JE_HEADER_ID
WHERE  h.REVERSAL_FLAG = 'Y'
  AND  h.LEDGER_ID = :p_ledger_id
  AND  h.PERIOD_NAME = 'MAR-26';
```

### Filtros comuns
- `STATUS = 'U'` — Não postados (Unposted)
- `STATUS = 'P'` — Postados (Posted)
- `ACTUAL_FLAG = 'A'` — Lançamentos reais
- `JE_SOURCE = 'Manual'` — Lançamentos manuais
- `JE_SOURCE = 'Payables'` — Importados do AP
- `JE_SOURCE = 'Receivables'` — Importados do AR
- `JE_CATEGORY = 'Adjustment'` — Categoria: ajuste

---

## 🔒 Observações

- O `STATUS` segue o mesmo padrão do batch: **U** (não postado), **S** (selecionado), **P** (postado), **I** (erro).
- `JE_SOURCE` identifica a origem: **Manual** (usuário), **Payables** (AP), **Receivables** (AR), **Assets** (FA), **Subledger Accounting** (SLA), etc.
- `JE_CATEGORY` classifica o tipo: **Adjustment**, **Accrual**, **Revaluation**, **Opening**, **Closing**, etc.
- Journals de reversão preenchem `REVERSED_JE_HEADER_ID` e `REVERSAL_FLAG = 'Y'`.
- `REVERSAL_METHOD`: **C** (Change sign) inverte o sinal dos valores; **S** (Switch) troca débito por crédito.
- O `CURRENCY_CODE` pode ser diferente da moeda funcional do ledger — neste caso, `CURRENCY_CONVERSION_RATE` indica a taxa aplicada.
- Journals com `ACCRUAL_REV_FLAG = 'Y'` são marcados para reversão automática no período indicado em `ACCRUAL_REV_PERIOD_NAME`.

---

## 📚 Referências

- [Oracle Docs — GL_JE_HEADERS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/gljeheaders-25722.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
