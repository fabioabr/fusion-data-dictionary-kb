---
id: DOC-GL-037
doc_type: system-doc
title: "GL_STAT_ACCOUNT_UOM — Unidades de Medida para Contas Estatísticas"
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
  - contas-estatisticas
  - unidade-medida
  - uom
  - statistical
aliases:
  - GL_STAT_ACCOUNT_UOM
  - gl_stat_account_uom
  - uom-contas-estatisticas
  - statistical-accounts-uom
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_STAT_ACCOUNT_UOM

## 📌 Visão Geral

Armazena a **associação entre contas estatísticas e suas unidades de medida (UOM)** no General Ledger. Contas estatísticas registram quantidades não-monetárias (headcount, m², MWh, etc.) no GL, e esta tabela define qual unidade de medida é válida para cada conta estatística.

> [!note] Contas Estatísticas
> Contas estatísticas são contas do plano de contas que aceitam valores em unidades não-monetárias. São usadas para cálculos de KPIs (ex: receita por funcionário = receita / headcount) e alocações baseadas em drivers estatísticos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Lançamentos estatísticos:** Validação da unidade de medida ao registrar journals em contas estatísticas.
- **Alocações:** Drivers estatísticos para regras de alocação de custos (ex: distribuir custo de aluguel por m² de cada departamento).
- **KPIs financeiros:** Cálculos que combinam saldos monetários com quantidades estatísticas (ex: custo por FTE).
- **Reporting:** Relatórios que exibem métricas não-financeiras ao lado de dados contábeis.
- **Orçamento estatístico:** Planejamento de quantidades (headcount, unidades produzidas) associadas ao orçamento financeiro.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | STAT_ACCOUNT_UOM_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro | — | 🟡 80% |
| 2 | LEDGER_ID | NUMBER(18) | NOT NULL | FK | Identificador do ledger | [[gl_ledgers]] | 🟢 90% |
| 3 | CODE_COMBINATION_ID | NUMBER(18) | NOT NULL | FK | Combinação de contas contábeis (conta estatística) | [[gl_code_combinations]] | 🟢 90% |
| 4 | ACCOUNT_SEGMENT_VALUE | VARCHAR2(25) | NOT NULL | Identificação | Valor do segmento de conta natural (conta estatística) | — | 🟡 80% |
| 5 | UNIT_OF_MEASURE | VARCHAR2(25) | NOT NULL | Classificação | Código da unidade de medida (ex: FTE, SQM, KWH, UNIT) | — | 🟢 90% |
| 6 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição da associação conta/UOM | — | 🟡 75% |
| 7 | ENABLED_FLAG | VARCHAR2(1) | NULL | Status | Indica se a associação está ativa (Y/N) | — | 🟡 80% |
| 8 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 70% |
| 9 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de fim da vigência (NULL = sem expiração) | — | 🟡 70% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[gl_ledgers]] — via `LEDGER_ID` (ledger/livro contábil)
- [[gl_code_combinations]] — via `CODE_COMBINATION_ID` (combinação de contas)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de configuração consultada na validação de lançamentos estatísticos.

---

## 📎 Uso Típico

### UOMs configuradas para contas estatísticas
```sql
SELECT sau.ACCOUNT_SEGMENT_VALUE,
       sau.UNIT_OF_MEASURE,
       sau.DESCRIPTION
FROM   GL_STAT_ACCOUNT_UOM sau
WHERE  sau.LEDGER_ID = :p_ledger_id
  AND  (sau.ENABLED_FLAG = 'Y' OR sau.ENABLED_FLAG IS NULL)
ORDER BY sau.ACCOUNT_SEGMENT_VALUE;
```

### Validar UOM de uma conta
```sql
SELECT sau.UNIT_OF_MEASURE
FROM   GL_STAT_ACCOUNT_UOM sau
WHERE  sau.LEDGER_ID = :p_ledger_id
  AND  sau.ACCOUNT_SEGMENT_VALUE = :p_account_value
  AND  (sau.END_DATE_ACTIVE IS NULL OR sau.END_DATE_ACTIVE >= SYSDATE);
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Associações ativas
- `UNIT_OF_MEASURE = 'FTE'` — Contas de headcount (Full-Time Equivalent)
- `END_DATE_ACTIVE IS NULL` — Associações sem data de expiração

---

## 🔒 Observações

- Cada conta estatística deve ter exatamente uma UOM associada. Lançamentos em contas estatísticas sem UOM configurada serão rejeitados.
- As UOMs mais comuns em instituições financeiras são: **FTE** (headcount), **UNIT** (unidades genéricas), **SQM** (metros quadrados), **HOUR** (horas).
- O valor na coluna `ENTERED_DR` / `ENTERED_CR` de `GL_JE_LINES` para contas estatísticas representa a **quantidade** na UOM configurada, não um valor monetário.
- A moeda "STAT" é usada no `GL_BALANCES` para identificar saldos estatísticos — o valor é a quantidade na UOM.
- Esta tabela tem confiança moderada (70-80%) em algumas colunas porque a documentação oficial é escassa para este recurso específico. Validar estrutura no ambiente real.

---

## 📚 Referências

- [Oracle Docs — Statistical Accounts](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
