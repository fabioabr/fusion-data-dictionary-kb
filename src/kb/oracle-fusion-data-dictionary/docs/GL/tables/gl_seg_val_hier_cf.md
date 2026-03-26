---
id: DOC-GL-036
doc_type: system-doc
title: "GL_SEG_VAL_HIER_CF — Hierarquias de Valores de Segmento"
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
  - hierarquias
  - segment-values
  - rollup
  - chart-of-accounts
aliases:
  - GL_SEG_VAL_HIER_CF
  - gl_seg_val_hier_cf
  - hierarquia-segmentos-gl
  - segment-hierarchy
  - rollup-groups
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# GL_SEG_VAL_HIER_CF

## 📌 Visão Geral

Armazena as **hierarquias (rollup) de valores de segmento** do plano de contas contábil. Define a estrutura pai-filho (parent-child) dos valores de cada segmento, permitindo a construção de árvores hierárquicas para relatórios agregados — por exemplo, agrupar contas analíticas em contas sintéticas, ou centros de custo em departamentos e divisões.

> [!note] Sufixo _CF
> O sufixo `_CF` indica uma tabela "Cross-Reference/Flattened" — armazena a hierarquia de forma desnormalizada para facilitar consultas de rollup sem navegação recursiva.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Relatórios consolidados:** Agregação de saldos contábeis por hierarquia (ex: saldo de uma divisão = soma de todos os centros de custo filhos).
- **Financial Reporting (FR):** O Oracle Financial Reporting Studio utiliza estas hierarquias para drill-down/drill-up em relatórios.
- **Orçamento:** Distribuição (top-down) e consolidação (bottom-up) de budget por hierarquia.
- **Segurança por dados:** Controle de acesso baseado em nós da hierarquia (ex: gestor vê apenas seu departamento e filhos).
- **Alocações:** Regras de alocação que distribuem valores entre nós filhos.
- **Smart View / OTBI:** Consultas que utilizam hierarquias para agrupamento dinâmico.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_STRUCTURE_CODE | VARCHAR2(30) | NOT NULL | PK | Código da estrutura de árvore (tree structure) | — | 🟢 95% |
| 2 | TREE_CODE | VARCHAR2(30) | NOT NULL | PK | Código da árvore/hierarquia específica | — | 🟢 95% |
| 3 | TREE_VERSION_ID | NUMBER(18) | NOT NULL | PK | Versão da árvore (múltiplas versões podem coexistir) | — | 🟢 95% |
| 4 | PARENT_VALUE | VARCHAR2(60) | NOT NULL | Hierarquia | Valor do segmento pai (nó agrupador) | — | 🟢 90% |
| 5 | PARENT_DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó pai na árvore (0 = raiz) | — | 🟡 75% |
| 6 | CHILD_VALUE | VARCHAR2(60) | NOT NULL | Hierarquia | Valor do segmento filho | — | 🟢 90% |
| 7 | CHILD_DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó filho na árvore | — | 🟡 75% |
| 8 | CHILD_VALUE_SET_ID | NUMBER(18) | NULL | FK | ID do value set do valor filho | [[fnd_flex_value_sets]] | 🟡 80% |
| 9 | PARENT_VALUE_SET_ID | NUMBER(18) | NULL | FK | ID do value set do valor pai | [[fnd_flex_value_sets]] | 🟡 80% |
| 10 | RANGE_LOW | VARCHAR2(60) | NULL | Filtro | Valor inicial do range de filhos (para nós tipo range) | — | 🟡 70% |
| 11 | RANGE_HIGH | VARCHAR2(60) | NULL | Filtro | Valor final do range de filhos | — | 🟡 70% |
| 12 | LEAF_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se o nó filho é uma folha (Y) ou nó intermediário (N) | — | 🟡 75% |
| 13 | ENABLED_FLAG | VARCHAR2(1) | NULL | Status | Indica se o relacionamento está ativo (Y/N) | — | 🟢 90% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[fnd_flex_value_sets]] — via `CHILD_VALUE_SET_ID` e `PARENT_VALUE_SET_ID` (value sets dos segmentos)

### Tabelas-filha (FK de saída)
- Nenhuma FK direta — esta é uma tabela de hierarquia consumida por relatórios e processos de rollup.

---

## 📎 Uso Típico

### Filhos diretos de um nó pai
```sql
SELECT h.CHILD_VALUE,
       h.CHILD_DEPTH,
       h.LEAF_FLAG
FROM   GL_SEG_VAL_HIER_CF h
WHERE  h.TREE_CODE = :p_tree_code
  AND  h.TREE_VERSION_ID = :p_version_id
  AND  h.PARENT_VALUE = :p_parent_value
  AND  h.ENABLED_FLAG = 'Y'
ORDER BY h.CHILD_VALUE;
```

### Todos os nós folha de uma hierarquia
```sql
SELECT h.PARENT_VALUE,
       h.CHILD_VALUE
FROM   GL_SEG_VAL_HIER_CF h
WHERE  h.TREE_CODE = :p_tree_code
  AND  h.TREE_VERSION_ID = :p_version_id
  AND  h.LEAF_FLAG = 'Y'
ORDER BY h.PARENT_VALUE, h.CHILD_VALUE;
```

### Saldo consolidado por nó da hierarquia
```sql
SELECT h.PARENT_VALUE AS grupo,
       SUM(b.PERIOD_NET_DR - b.PERIOD_NET_CR) AS saldo_periodo
FROM   GL_BALANCES b
JOIN   GL_CODE_COMBINATIONS gcc ON gcc.CODE_COMBINATION_ID = b.CODE_COMBINATION_ID
JOIN   GL_SEG_VAL_HIER_CF h ON h.CHILD_VALUE = gcc.SEGMENT1
  AND  h.TREE_CODE = :p_tree_code
  AND  h.TREE_VERSION_ID = :p_version_id
  AND  h.LEAF_FLAG = 'Y'
WHERE  b.LEDGER_ID = :p_ledger_id
  AND  b.ACTUAL_FLAG = 'A'
  AND  b.PERIOD_NAME = 'MAR-26'
GROUP BY h.PARENT_VALUE;
```

### Filtros comuns
- `LEAF_FLAG = 'Y'` — Apenas nós folha (valores analíticos)
- `ENABLED_FLAG = 'Y'` — Apenas relacionamentos ativos
- `TREE_CODE` — Selecionar hierarquia específica (pode haver múltiplas por segmento)

---

## 🔒 Observações

- A tabela é **desnormalizada** (flattened) — cada par pai-filho é uma linha, facilitando JOINs diretos sem recursão. Para hierarquias profundas, um mesmo valor folha pode aparecer múltiplas vezes (uma para cada ancestral).
- O Oracle Fusion utiliza o framework **Tree Management** para gerenciar hierarquias. As árvores são versionadas (`TREE_VERSION_ID`), permitindo manter hierarquias históricas.
- O `TREE_STRUCTURE_CODE` identifica o tipo de estrutura (ex: GL_ACCT_FLEX para plano de contas). O `TREE_CODE` identifica a hierarquia específica dentro dessa estrutura.
- Nós do tipo **range** (`RANGE_LOW` / `RANGE_HIGH`) incluem todos os valores dentro do intervalo como filhos, sem necessidade de listá-los individualmente.
- Hierarquias são fundamentais para o Financial Reporting Studio e para a segurança por dados (Data Access Sets) do Oracle Fusion.

---

## 📚 Referências

- [Oracle Docs — GL Segment Value Hierarchies](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
