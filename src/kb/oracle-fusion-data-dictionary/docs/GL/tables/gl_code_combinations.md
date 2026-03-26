---
id: DOC-GL-002
doc_type: system-doc
title: "GL_CODE_COMBINATIONS — Combinações de Contas Contábeis"
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
  - ccid
  - plano-de-contas
  - chart-of-accounts
aliases:
  - GL_CODE_COMBINATIONS
  - gl_code_combinations
  - ccid
  - chart-of-accounts
  - plano-contas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_CODE_COMBINATIONS

## 📌 Visão Geral

Armazena todas as **combinações válidas de segmentos contábeis** (CCID — Code Combination ID) do plano de contas. Cada registro representa uma combinação única de segmentos (empresa, conta, centro de custo, projeto, etc.) utilizada em lançamentos contábeis. É a tabela de referência central do GL — praticamente toda tabela financeira do ERP aponta para ela via `CODE_COMBINATION_ID`.

> [!note] Tabela referenciada por todo o ERP
> `GL_CODE_COMBINATIONS` é a tabela mais referenciada do Oracle Fusion. Módulos como AP, AR, FA, PO e Cash Management apontam para ela via `CODE_COMBINATION_ID` em suas distribuições contábeis.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Plano de contas:** Armazena todas as combinações válidas de segmentos contábeis.
- **Lançamentos contábeis:** Todo lançamento no GL referencia um CCID desta tabela.
- **Distribuições de subledger:** AP, AR, FA usam CCID para contabilização.
- **Validação:** Controla quais combinações de conta/centro de custo/empresa são válidas.
- **Relatórios financeiros:** Base para agrupamento e drill-down por segmento.
- **Cross-validation rules:** Regras de validação cruzada entre segmentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da combinação de contas (CCID) | — | 🟢 100% |
| 2 | CHART_OF_ACCOUNTS_ID | NUMBER(18) | NOT NULL | FK | ID da estrutura do plano de contas (Key Flexfield) | — | 🟢 100% |
| 3 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Indica se a combinação está habilitada (Y/N) | — | 🟢 100% |
| 4 | SUMMARY_FLAG | VARCHAR2(1) | NOT NULL | Classificação | Indica se é conta de resumo/pai (Y) ou detalhe (N) | — | 🟢 100% |
| 5 | START_DATE_ACTIVE | DATE | NULL | Controle | Data de início de validade da combinação | — | 🟢 100% |
| 6 | END_DATE_ACTIVE | DATE | NULL | Controle | Data de fim de validade da combinação | — | 🟢 100% |
| 7 | SEGMENT1 | VARCHAR2(25) | NULL | Segmento | Segmento 1 — tipicamente Empresa/Entidade Legal | — | 🟢 100% |
| 8 | SEGMENT2 | VARCHAR2(25) | NULL | Segmento | Segmento 2 — tipicamente Conta Contábil (Natural Account) | — | 🟢 100% |
| 9 | SEGMENT3 | VARCHAR2(25) | NULL | Segmento | Segmento 3 — tipicamente Centro de Custo | — | 🟢 100% |
| 10 | SEGMENT4 | VARCHAR2(25) | NULL | Segmento | Segmento 4 — tipicamente Projeto ou Intercompany | — | 🟡 80% |
| 11 | SEGMENT5 | VARCHAR2(25) | NULL | Segmento | Segmento 5 — varia por implementação | — | 🟡 80% |
| 12 | SEGMENT6–30 | VARCHAR2(25) | NULL | Segmento | Segmentos adicionais (6 a 30) — configuráveis por implementação | — | 🟡 75% |
| 13 | ACCOUNT_TYPE | VARCHAR2(1) | NOT NULL | Classificação | Tipo de conta: A (Asset), L (Liability), O (Owner's Equity), R (Revenue), E (Expense) | — | 🟢 100% |
| 14 | DETAIL_POSTING_ALLOWED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Permite lançamento direto nesta combinação (Y/N) | — | 🟢 100% |
| 15 | DETAIL_BUDGETING_ALLOWED_FLAG | VARCHAR2(1) | NOT NULL | Controle | Permite orçamento direto nesta combinação (Y/N) | — | 🟢 100% |
| 16 | DESCRIPTION | VARCHAR2(240) | NULL | Identificação | Descrição textual da combinação de contas | — | 🟢 100% |
| 17 | TEMPLATE_ID | NUMBER(18) | NULL | Sistema | ID do template de alocação, se aplicável | — | 🟡 70% |
| 18 | REFERENCE1–5 | VARCHAR2(240) | NULL | Referência | Campos de referência genéricos | — | 🟡 70% |
| 19 | JGZ_RECONCILIATION_FLAG | VARCHAR2(1) | NULL | Controle | Flag de reconciliação (específico de localização) | — | 🟡 65% |
| 20 | PRESERVE_FLAG | VARCHAR2(1) | NULL | Controle | Preservar combinação durante reorganização do plano de contas | — | 🟡 65% |
| 21 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 22 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 23 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 24 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK direta — esta é uma tabela raiz (master data do plano de contas).

### Tabelas-filha (FK de saída)
- [[gl_balances]] — via `CODE_COMBINATION_ID` (saldos por combinação de conta)
- [[gl_je_lines]] — via `CODE_COMBINATION_ID` (linhas de lançamentos)
- [[ar_distributions_all]] — via `CODE_COMBINATION_ID` (distribuições AR)
- [[ar_adjustments_all]] — via `CODE_COMBINATION_ID` (ajustes de AR que utilizam esta combinação contábil)
- [[ar_misc_cash_distributions_all]] — via `CODE_COMBINATION_ID` (distribuições de misc receipts)

---

## 📎 Uso Típico

### Consultar combinação de conta por CCID
```sql
SELECT gcc.CODE_COMBINATION_ID,
       gcc.SEGMENT1 AS empresa,
       gcc.SEGMENT2 AS conta,
       gcc.SEGMENT3 AS centro_custo,
       gcc.ACCOUNT_TYPE,
       gcc.DESCRIPTION,
       gcc.ENABLED_FLAG
FROM   GL_CODE_COMBINATIONS gcc
WHERE  gcc.CODE_COMBINATION_ID = :p_ccid;
```

### Listar contas ativas de um segmento
```sql
SELECT gcc.CODE_COMBINATION_ID,
       gcc.SEGMENT1 || '.' || gcc.SEGMENT2 || '.' || gcc.SEGMENT3 AS conta_completa,
       gcc.DESCRIPTION,
       gcc.ACCOUNT_TYPE
FROM   GL_CODE_COMBINATIONS gcc
WHERE  gcc.CHART_OF_ACCOUNTS_ID = :p_coa_id
  AND  gcc.ENABLED_FLAG = 'Y'
  AND  gcc.SUMMARY_FLAG = 'N'
  AND  gcc.SEGMENT2 LIKE '4%'
ORDER BY gcc.SEGMENT1, gcc.SEGMENT2, gcc.SEGMENT3;
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Combinações ativas
- `SUMMARY_FLAG = 'N'` — Apenas contas de detalhe (não resumo)
- `ACCOUNT_TYPE = 'E'` — Contas de despesa
- `ACCOUNT_TYPE = 'R'` — Contas de receita

---

## 🔒 Observações

- O significado de cada `SEGMENT` depende da configuração do plano de contas (Key Flexfield). Os nomes típicos são: Empresa (SEGMENT1), Conta (SEGMENT2), Centro de Custo (SEGMENT3), mas podem variar por implementação.
- `ACCOUNT_TYPE` é derivado do segmento de conta natural (SEGMENT2 tipicamente): **A** (Ativo), **L** (Passivo), **O** (PL), **R** (Receita), **E** (Despesa).
- `SUMMARY_FLAG = 'Y'` indica contas-pai usadas apenas para rollup/consolidação — lançamentos são feitos apenas em contas de detalhe (`'N'`).
- `DETAIL_POSTING_ALLOWED_FLAG = 'N'` impede lançamentos diretos — usado para contas de controle.
- Esta tabela é **compartilhada** por todo o ERP — qualquer mudança impacta todos os módulos.

---

## 📚 Referências

- [Oracle Docs — GL_CODE_COMBINATIONS](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/glcodecombinations-25012.html)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
