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

## 🔗 PVOs Relacionados

### [[flex_tree_vs_fa_cost_ctr_vi|FLEX_TREE_VS_FA_COST_CTR_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DEP0_DATA_SOURCE_ID | Dep0DataSourceId | — |
| DEP0_PK1_VALUE | Dep0Pk1Value | — |
| DEP0_PK2_VALUE | Dep0Pk2Value | — |
| DEP0_PK3_VALUE | Dep0Pk3Value | — |
| DEP0_PK4_VALUE | Dep0Pk4Value | — |
| DEP0_PK5_VALUE | Dep0Pk5Value | — |
| DEP0_TREE_NODE_ID | Dep0TreeNodeId | — |
| DEP10_DATA_SOURCE_ID | Dep10DataSourceId | — |
| DEP10_PK1_VALUE | Dep10Pk1Value | — |
| DEP10_PK2_VALUE | Dep10Pk2Value | — |
| DEP10_PK3_VALUE | Dep10Pk3Value | — |
| DEP10_PK4_VALUE | Dep10Pk4Value | — |
| DEP10_PK5_VALUE | Dep10Pk5Value | — |
| DEP10_TREE_NODE_ID | Dep10TreeNodeId | — |
| DEP11_DATA_SOURCE_ID | Dep11DataSourceId | — |
| DEP11_PK1_VALUE | Dep11Pk1Value | — |
| DEP11_PK2_VALUE | Dep11Pk2Value | — |
| DEP11_PK3_VALUE | Dep11Pk3Value | — |
| DEP11_PK4_VALUE | Dep11Pk4Value | — |
| DEP11_PK5_VALUE | Dep11Pk5Value | — |
| DEP11_TREE_NODE_ID | Dep11TreeNodeId | — |
| DEP12_DATA_SOURCE_ID | Dep12DataSourceId | — |
| DEP12_PK1_VALUE | Dep12Pk1Value | — |
| DEP12_PK2_VALUE | Dep12Pk2Value | — |
| DEP12_PK3_VALUE | Dep12Pk3Value | — |
| DEP12_PK4_VALUE | Dep12Pk4Value | — |
| DEP12_PK5_VALUE | Dep12Pk5Value | — |
| DEP12_TREE_NODE_ID | Dep12TreeNodeId | — |
| DEP13_DATA_SOURCE_ID | Dep13DataSourceId | — |
| DEP13_PK1_VALUE | Dep13Pk1Value | — |
| DEP13_PK2_VALUE | Dep13Pk2Value | — |
| DEP13_PK3_VALUE | Dep13Pk3Value | — |
| DEP13_PK4_VALUE | Dep13Pk4Value | — |
| DEP13_PK5_VALUE | Dep13Pk5Value | — |
| DEP13_TREE_NODE_ID | Dep13TreeNodeId | — |
| DEP14_DATA_SOURCE_ID | Dep14DataSourceId | — |
| DEP14_PK1_VALUE | Dep14Pk1Value | — |
| DEP14_PK2_VALUE | Dep14Pk2Value | — |
| DEP14_PK3_VALUE | Dep14Pk3Value | — |
| DEP14_PK4_VALUE | Dep14Pk4Value | — |
| DEP14_PK5_VALUE | Dep14Pk5Value | — |
| DEP14_TREE_NODE_ID | Dep14TreeNodeId | — |
| DEP15_DATA_SOURCE_ID | Dep15DataSourceId | — |
| DEP15_PK1_VALUE | Dep15Pk1Value | — |
| DEP15_PK2_VALUE | Dep15Pk2Value | — |
| DEP15_PK3_VALUE | Dep15Pk3Value | — |
| DEP15_PK4_VALUE | Dep15Pk4Value | — |
| DEP15_PK5_VALUE | Dep15Pk5Value | — |
| DEP15_TREE_NODE_ID | Dep15TreeNodeId | — |
| DEP16_DATA_SOURCE_ID | Dep16DataSourceId | — |
| DEP16_PK1_VALUE | Dep16Pk1Value | — |
| DEP16_PK2_VALUE | Dep16Pk2Value | — |
| DEP16_PK3_VALUE | Dep16Pk3Value | — |
| DEP16_PK4_VALUE | Dep16Pk4Value | — |
| DEP16_PK5_VALUE | Dep16Pk5Value | — |
| DEP16_TREE_NODE_ID | Dep16TreeNodeId | — |
| DEP17_DATA_SOURCE_ID | Dep17DataSourceId | — |
| DEP17_PK1_VALUE | Dep17Pk1Value | — |
| DEP17_PK2_VALUE | Dep17Pk2Value | — |
| DEP17_PK3_VALUE | Dep17Pk3Value | — |
| DEP17_PK4_VALUE | Dep17Pk4Value | — |
| DEP17_PK5_VALUE | Dep17Pk5Value | — |
| DEP17_TREE_NODE_ID | Dep17TreeNodeId | — |
| DEP18_DATA_SOURCE_ID | Dep18DataSourceId | — |
| DEP18_PK1_VALUE | Dep18Pk1Value | — |
| DEP18_PK2_VALUE | Dep18Pk2Value | — |
| DEP18_PK3_VALUE | Dep18Pk3Value | — |
| DEP18_PK4_VALUE | Dep18Pk4Value | — |
| DEP18_PK5_VALUE | Dep18Pk5Value | — |
| DEP18_TREE_NODE_ID | Dep18TreeNodeId | — |
| DEP19_DATA_SOURCE_ID | Dep19DataSourceId | — |
| DEP19_PK1_VALUE | Dep19Pk1Value | — |
| DEP19_PK2_VALUE | Dep19Pk2Value | — |
| DEP19_PK3_VALUE | Dep19Pk3Value | — |
| DEP19_PK4_VALUE | Dep19Pk4Value | — |
| DEP19_PK5_VALUE | Dep19Pk5Value | — |
| DEP19_TREE_NODE_ID | Dep19TreeNodeId | — |
| DEP1_DATA_SOURCE_ID | Dep1DataSourceId | — |
| DEP1_PK1_VALUE | Dep1Pk1Value | — |
| DEP1_PK2_VALUE | Dep1Pk2Value | — |
| DEP1_PK3_VALUE | Dep1Pk3Value | — |
| DEP1_PK4_VALUE | Dep1Pk4Value | — |
| DEP1_PK5_VALUE | Dep1Pk5Value | — |
| DEP1_TREE_NODE_ID | Dep1TreeNodeId | — |
| DEP20_DATA_SOURCE_ID | Dep20DataSourceId | — |
| DEP20_PK1_VALUE | Dep20Pk1Value | — |
| DEP20_PK2_VALUE | Dep20Pk2Value | — |
| DEP20_PK3_VALUE | Dep20Pk3Value | — |
| DEP20_PK4_VALUE | Dep20Pk4Value | — |
| DEP20_PK5_VALUE | Dep20Pk5Value | — |
| DEP20_TREE_NODE_ID | Dep20TreeNodeId | — |
| DEP21_DATA_SOURCE_ID | Dep21DataSourceId | — |
| DEP21_PK1_VALUE | Dep21Pk1Value | — |
| DEP21_PK2_VALUE | Dep21Pk2Value | — |
| DEP21_PK3_VALUE | Dep21Pk3Value | — |
| DEP21_PK4_VALUE | Dep21Pk4Value | — |
| DEP21_PK5_VALUE | Dep21Pk5Value | — |
| DEP21_TREE_NODE_ID | Dep21TreeNodeId | — |
| DEP22_DATA_SOURCE_ID | Dep22DataSourceId | — |
| DEP22_PK1_VALUE | Dep22Pk1Value | — |
| DEP22_PK2_VALUE | Dep22Pk2Value | — |
| DEP22_PK3_VALUE | Dep22Pk3Value | — |
| DEP22_PK4_VALUE | Dep22Pk4Value | — |
| DEP22_PK5_VALUE | Dep22Pk5Value | — |
| DEP22_TREE_NODE_ID | Dep22TreeNodeId | — |
| DEP23_DATA_SOURCE_ID | Dep23DataSourceId | — |
| DEP23_PK1_VALUE | Dep23Pk1Value | — |
| DEP23_PK2_VALUE | Dep23Pk2Value | — |
| DEP23_PK3_VALUE | Dep23Pk3Value | — |
| DEP23_PK4_VALUE | Dep23Pk4Value | — |
| DEP23_PK5_VALUE | Dep23Pk5Value | — |
| DEP23_TREE_NODE_ID | Dep23TreeNodeId | — |
| DEP24_DATA_SOURCE_ID | Dep24DataSourceId | — |
| DEP24_PK1_VALUE | Dep24Pk1Value | — |
| DEP24_PK2_VALUE | Dep24Pk2Value | — |
| DEP24_PK3_VALUE | Dep24Pk3Value | — |
| DEP24_PK4_VALUE | Dep24Pk4Value | — |
| DEP24_PK5_VALUE | Dep24Pk5Value | — |
| DEP24_TREE_NODE_ID | Dep24TreeNodeId | — |
| DEP25_DATA_SOURCE_ID | Dep25DataSourceId | — |
| DEP25_PK1_VALUE | Dep25Pk1Value | — |
| DEP25_PK2_VALUE | Dep25Pk2Value | — |
| DEP25_PK3_VALUE | Dep25Pk3Value | — |
| DEP25_PK4_VALUE | Dep25Pk4Value | — |
| DEP25_PK5_VALUE | Dep25Pk5Value | — |
| DEP25_TREE_NODE_ID | Dep25TreeNodeId | — |
| DEP26_DATA_SOURCE_ID | Dep26DataSourceId | — |
| DEP26_PK1_VALUE | Dep26Pk1Value | — |
| DEP26_PK2_VALUE | Dep26Pk2Value | — |
| DEP26_PK3_VALUE | Dep26Pk3Value | — |
| DEP26_PK4_VALUE | Dep26Pk4Value | — |
| DEP26_PK5_VALUE | Dep26Pk5Value | — |
| DEP26_TREE_NODE_ID | Dep26TreeNodeId | — |
| DEP27_DATA_SOURCE_ID | Dep27DataSourceId | — |
| DEP27_PK1_VALUE | Dep27Pk1Value | — |
| DEP27_PK2_VALUE | Dep27Pk2Value | — |
| DEP27_PK3_VALUE | Dep27Pk3Value | — |
| DEP27_PK4_VALUE | Dep27Pk4Value | — |
| DEP27_PK5_VALUE | Dep27Pk5Value | — |
| DEP27_TREE_NODE_ID | Dep27TreeNodeId | — |
| DEP28_DATA_SOURCE_ID | Dep28DataSourceId | — |
| DEP28_PK1_VALUE | Dep28Pk1Value | — |
| DEP28_PK2_VALUE | Dep28Pk2Value | — |
| DEP28_PK3_VALUE | Dep28Pk3Value | — |
| DEP28_PK4_VALUE | Dep28Pk4Value | — |
| DEP28_PK5_VALUE | Dep28Pk5Value | — |
| DEP28_TREE_NODE_ID | Dep28TreeNodeId | — |
| DEP29_DATA_SOURCE_ID | Dep29DataSourceId | — |
| DEP29_PK1_VALUE | Dep29Pk1Value | — |
| DEP29_PK2_VALUE | Dep29Pk2Value | — |
| DEP29_PK3_VALUE | Dep29Pk3Value | — |
| DEP29_PK4_VALUE | Dep29Pk4Value | — |
| DEP29_PK5_VALUE | Dep29Pk5Value | — |
| DEP29_TREE_NODE_ID | Dep29TreeNodeId | — |
| DEP2_DATA_SOURCE_ID | Dep2DataSourceId | — |
| DEP2_PK1_VALUE | Dep2Pk1Value | — |
| DEP2_PK2_VALUE | Dep2Pk2Value | — |
| DEP2_PK3_VALUE | Dep2Pk3Value | — |
| DEP2_PK4_VALUE | Dep2Pk4Value | — |
| DEP2_PK5_VALUE | Dep2Pk5Value | — |
| DEP2_TREE_NODE_ID | Dep2TreeNodeId | — |
| DEP30_DATA_SOURCE_ID | Dep30DataSourceId | — |
| DEP30_PK1_VALUE | Dep30Pk1Value | — |
| DEP30_PK2_VALUE | Dep30Pk2Value | — |
| DEP30_PK3_VALUE | Dep30Pk3Value | — |
| DEP30_PK4_VALUE | Dep30Pk4Value | — |
| DEP30_PK5_VALUE | Dep30Pk5Value | — |
| DEP30_TREE_NODE_ID | Dep30TreeNodeId | — |
| DEP31_DATA_SOURCE_ID | Dep31DataSourceId | — |
| DEP31_PK1_VALUE | Dep31Pk1Value | — |
| DEP31_PK2_VALUE | Dep31Pk2Value | — |
| DEP31_PK3_VALUE | Dep31Pk3Value | — |
| DEP31_PK4_VALUE | Dep31Pk4Value | — |
| DEP31_PK5_VALUE | Dep31Pk5Value | — |
| DEP31_TREE_NODE_ID | Dep31TreeNodeId | — |
| DEP3_DATA_SOURCE_ID | Dep3DataSourceId | — |
| DEP3_PK1_VALUE | Dep3Pk1Value | — |
| DEP3_PK2_VALUE | Dep3Pk2Value | — |
| DEP3_PK3_VALUE | Dep3Pk3Value | — |
| DEP3_PK4_VALUE | Dep3Pk4Value | — |
| DEP3_PK5_VALUE | Dep3Pk5Value | — |
| DEP3_TREE_NODE_ID | Dep3TreeNodeId | — |
| DEP4_DATA_SOURCE_ID | Dep4DataSourceId | — |
| DEP4_PK1_VALUE | Dep4Pk1Value | — |
| DEP4_PK2_VALUE | Dep4Pk2Value | — |
| DEP4_PK3_VALUE | Dep4Pk3Value | — |
| DEP4_PK4_VALUE | Dep4Pk4Value | — |
| DEP4_PK5_VALUE | Dep4Pk5Value | — |
| DEP4_TREE_NODE_ID | Dep4TreeNodeId | — |
| DEP5_DATA_SOURCE_ID | Dep5DataSourceId | — |
| DEP5_PK1_VALUE | Dep5Pk1Value | — |
| DEP5_PK2_VALUE | Dep5Pk2Value | — |
| DEP5_PK3_VALUE | Dep5Pk3Value | — |
| DEP5_PK4_VALUE | Dep5Pk4Value | — |
| DEP5_PK5_VALUE | Dep5Pk5Value | — |
| DEP5_TREE_NODE_ID | Dep5TreeNodeId | — |
| DEP6_DATA_SOURCE_ID | Dep6DataSourceId | — |
| DEP6_PK1_VALUE | Dep6Pk1Value | — |
| DEP6_PK2_VALUE | Dep6Pk2Value | — |
| DEP6_PK3_VALUE | Dep6Pk3Value | — |
| DEP6_PK4_VALUE | Dep6Pk4Value | — |
| DEP6_PK5_VALUE | Dep6Pk5Value | — |
| DEP6_TREE_NODE_ID | Dep6TreeNodeId | — |
| DEP7_DATA_SOURCE_ID | Dep7DataSourceId | — |
| DEP7_PK1_VALUE | Dep7Pk1Value | — |
| DEP7_PK2_VALUE | Dep7Pk2Value | — |
| DEP7_PK3_VALUE | Dep7Pk3Value | — |
| DEP7_PK4_VALUE | Dep7Pk4Value | — |
| DEP7_PK5_VALUE | Dep7Pk5Value | — |
| DEP7_TREE_NODE_ID | Dep7TreeNodeId | — |
| DEP8_DATA_SOURCE_ID | Dep8DataSourceId | — |
| DEP8_PK1_VALUE | Dep8Pk1Value | — |
| DEP8_PK2_VALUE | Dep8Pk2Value | — |
| DEP8_PK3_VALUE | Dep8Pk3Value | — |
| DEP8_PK4_VALUE | Dep8Pk4Value | — |
| DEP8_PK5_VALUE | Dep8Pk5Value | — |
| DEP8_TREE_NODE_ID | Dep8TreeNodeId | — |
| DEP9_DATA_SOURCE_ID | Dep9DataSourceId | — |
| DEP9_PK1_VALUE | Dep9Pk1Value | — |
| DEP9_PK2_VALUE | Dep9Pk2Value | — |
| DEP9_PK3_VALUE | Dep9Pk3Value | — |
| DEP9_PK4_VALUE | Dep9Pk4Value | — |
| DEP9_PK5_VALUE | Dep9Pk5Value | — |
| DEP9_TREE_NODE_ID | Dep9TreeNodeId | — |
| DISTANCE | Distance | — |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| TREE_CODE | TreeCode | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |

### [[flex_tree_vs_gl_account_vi|FLEX_TREE_VS_GL_ACCOUNT_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DEP0_DATA_SOURCE_ID | Dep0DataSourceId | — |
| DEP0_PK1_VALUE | Dep0Pk1Value | — |
| DEP0_PK2_VALUE | Dep0Pk2Value | — |
| DEP0_PK3_VALUE | Dep0Pk3Value | — |
| DEP0_PK4_VALUE | Dep0Pk4Value | — |
| DEP0_PK5_VALUE | Dep0Pk5Value | — |
| DEP0_TREE_NODE_ID | Dep0TreeNodeId | — |
| DEP10_DATA_SOURCE_ID | Dep10DataSourceId | — |
| DEP10_PK1_VALUE | Dep10Pk1Value | — |
| DEP10_PK2_VALUE | Dep10Pk2Value | — |
| DEP10_PK3_VALUE | Dep10Pk3Value | — |
| DEP10_PK4_VALUE | Dep10Pk4Value | — |
| DEP10_PK5_VALUE | Dep10Pk5Value | — |
| DEP10_TREE_NODE_ID | Dep10TreeNodeId | — |
| DEP11_DATA_SOURCE_ID | Dep11DataSourceId | — |
| DEP11_PK1_VALUE | Dep11Pk1Value | — |
| DEP11_PK2_VALUE | Dep11Pk2Value | — |
| DEP11_PK3_VALUE | Dep11Pk3Value | — |
| DEP11_PK4_VALUE | Dep11Pk4Value | — |
| DEP11_PK5_VALUE | Dep11Pk5Value | — |
| DEP11_TREE_NODE_ID | Dep11TreeNodeId | — |
| DEP12_DATA_SOURCE_ID | Dep12DataSourceId | — |
| DEP12_PK1_VALUE | Dep12Pk1Value | — |
| DEP12_PK2_VALUE | Dep12Pk2Value | — |
| DEP12_PK3_VALUE | Dep12Pk3Value | — |
| DEP12_PK4_VALUE | Dep12Pk4Value | — |
| DEP12_PK5_VALUE | Dep12Pk5Value | — |
| DEP12_TREE_NODE_ID | Dep12TreeNodeId | — |
| DEP13_DATA_SOURCE_ID | Dep13DataSourceId | — |
| DEP13_PK1_VALUE | Dep13Pk1Value | — |
| DEP13_PK2_VALUE | Dep13Pk2Value | — |
| DEP13_PK3_VALUE | Dep13Pk3Value | — |
| DEP13_PK4_VALUE | Dep13Pk4Value | — |
| DEP13_PK5_VALUE | Dep13Pk5Value | — |
| DEP13_TREE_NODE_ID | Dep13TreeNodeId | — |
| DEP14_DATA_SOURCE_ID | Dep14DataSourceId | — |
| DEP14_PK1_VALUE | Dep14Pk1Value | — |
| DEP14_PK2_VALUE | Dep14Pk2Value | — |
| DEP14_PK3_VALUE | Dep14Pk3Value | — |
| DEP14_PK4_VALUE | Dep14Pk4Value | — |
| DEP14_PK5_VALUE | Dep14Pk5Value | — |
| DEP14_TREE_NODE_ID | Dep14TreeNodeId | — |
| DEP15_DATA_SOURCE_ID | Dep15DataSourceId | — |
| DEP15_PK1_VALUE | Dep15Pk1Value | — |
| DEP15_PK2_VALUE | Dep15Pk2Value | — |
| DEP15_PK3_VALUE | Dep15Pk3Value | — |
| DEP15_PK4_VALUE | Dep15Pk4Value | — |
| DEP15_PK5_VALUE | Dep15Pk5Value | — |
| DEP15_TREE_NODE_ID | Dep15TreeNodeId | — |
| DEP16_DATA_SOURCE_ID | Dep16DataSourceId | — |
| DEP16_PK1_VALUE | Dep16Pk1Value | — |
| DEP16_PK2_VALUE | Dep16Pk2Value | — |
| DEP16_PK3_VALUE | Dep16Pk3Value | — |
| DEP16_PK4_VALUE | Dep16Pk4Value | — |
| DEP16_PK5_VALUE | Dep16Pk5Value | — |
| DEP16_TREE_NODE_ID | Dep16TreeNodeId | — |
| DEP17_DATA_SOURCE_ID | Dep17DataSourceId | — |
| DEP17_PK1_VALUE | Dep17Pk1Value | — |
| DEP17_PK2_VALUE | Dep17Pk2Value | — |
| DEP17_PK3_VALUE | Dep17Pk3Value | — |
| DEP17_PK4_VALUE | Dep17Pk4Value | — |
| DEP17_PK5_VALUE | Dep17Pk5Value | — |
| DEP17_TREE_NODE_ID | Dep17TreeNodeId | — |
| DEP18_DATA_SOURCE_ID | Dep18DataSourceId | — |
| DEP18_PK1_VALUE | Dep18Pk1Value | — |
| DEP18_PK2_VALUE | Dep18Pk2Value | — |
| DEP18_PK3_VALUE | Dep18Pk3Value | — |
| DEP18_PK4_VALUE | Dep18Pk4Value | — |
| DEP18_PK5_VALUE | Dep18Pk5Value | — |
| DEP18_TREE_NODE_ID | Dep18TreeNodeId | — |
| DEP19_DATA_SOURCE_ID | Dep19DataSourceId | — |
| DEP19_PK1_VALUE | Dep19Pk1Value | — |
| DEP19_PK2_VALUE | Dep19Pk2Value | — |
| DEP19_PK3_VALUE | Dep19Pk3Value | — |
| DEP19_PK4_VALUE | Dep19Pk4Value | — |
| DEP19_PK5_VALUE | Dep19Pk5Value | — |
| DEP19_TREE_NODE_ID | Dep19TreeNodeId | — |
| DEP1_DATA_SOURCE_ID | Dep1DataSourceId | — |
| DEP1_PK1_VALUE | Dep1Pk1Value | — |
| DEP1_PK2_VALUE | Dep1Pk2Value | — |
| DEP1_PK3_VALUE | Dep1Pk3Value | — |
| DEP1_PK4_VALUE | Dep1Pk4Value | — |
| DEP1_PK5_VALUE | Dep1Pk5Value | — |
| DEP1_TREE_NODE_ID | Dep1TreeNodeId | — |
| DEP20_DATA_SOURCE_ID | Dep20DataSourceId | — |
| DEP20_PK1_VALUE | Dep20Pk1Value | — |
| DEP20_PK2_VALUE | Dep20Pk2Value | — |
| DEP20_PK3_VALUE | Dep20Pk3Value | — |
| DEP20_PK4_VALUE | Dep20Pk4Value | — |
| DEP20_PK5_VALUE | Dep20Pk5Value | — |
| DEP20_TREE_NODE_ID | Dep20TreeNodeId | — |
| DEP21_DATA_SOURCE_ID | Dep21DataSourceId | — |
| DEP21_PK1_VALUE | Dep21Pk1Value | — |
| DEP21_PK2_VALUE | Dep21Pk2Value | — |
| DEP21_PK3_VALUE | Dep21Pk3Value | — |
| DEP21_PK4_VALUE | Dep21Pk4Value | — |
| DEP21_PK5_VALUE | Dep21Pk5Value | — |
| DEP21_TREE_NODE_ID | Dep21TreeNodeId | — |
| DEP22_DATA_SOURCE_ID | Dep22DataSourceId | — |
| DEP22_PK1_VALUE | Dep22Pk1Value | — |
| DEP22_PK2_VALUE | Dep22Pk2Value | — |
| DEP22_PK3_VALUE | Dep22Pk3Value | — |
| DEP22_PK4_VALUE | Dep22Pk4Value | — |
| DEP22_PK5_VALUE | Dep22Pk5Value | — |
| DEP22_TREE_NODE_ID | Dep22TreeNodeId | — |
| DEP23_DATA_SOURCE_ID | Dep23DataSourceId | — |
| DEP23_PK1_VALUE | Dep23Pk1Value | — |
| DEP23_PK2_VALUE | Dep23Pk2Value | — |
| DEP23_PK3_VALUE | Dep23Pk3Value | — |
| DEP23_PK4_VALUE | Dep23Pk4Value | — |
| DEP23_PK5_VALUE | Dep23Pk5Value | — |
| DEP23_TREE_NODE_ID | Dep23TreeNodeId | — |
| DEP24_DATA_SOURCE_ID | Dep24DataSourceId | — |
| DEP24_PK1_VALUE | Dep24Pk1Value | — |
| DEP24_PK2_VALUE | Dep24Pk2Value | — |
| DEP24_PK3_VALUE | Dep24Pk3Value | — |
| DEP24_PK4_VALUE | Dep24Pk4Value | — |
| DEP24_PK5_VALUE | Dep24Pk5Value | — |
| DEP24_TREE_NODE_ID | Dep24TreeNodeId | — |
| DEP25_DATA_SOURCE_ID | Dep25DataSourceId | — |
| DEP25_PK1_VALUE | Dep25Pk1Value | — |
| DEP25_PK2_VALUE | Dep25Pk2Value | — |
| DEP25_PK3_VALUE | Dep25Pk3Value | — |
| DEP25_PK4_VALUE | Dep25Pk4Value | — |
| DEP25_PK5_VALUE | Dep25Pk5Value | — |
| DEP25_TREE_NODE_ID | Dep25TreeNodeId | — |
| DEP26_DATA_SOURCE_ID | Dep26DataSourceId | — |
| DEP26_PK1_VALUE | Dep26Pk1Value | — |
| DEP26_PK2_VALUE | Dep26Pk2Value | — |
| DEP26_PK3_VALUE | Dep26Pk3Value | — |
| DEP26_PK4_VALUE | Dep26Pk4Value | — |
| DEP26_PK5_VALUE | Dep26Pk5Value | — |
| DEP26_TREE_NODE_ID | Dep26TreeNodeId | — |
| DEP27_DATA_SOURCE_ID | Dep27DataSourceId | — |
| DEP27_PK1_VALUE | Dep27Pk1Value | — |
| DEP27_PK2_VALUE | Dep27Pk2Value | — |
| DEP27_PK3_VALUE | Dep27Pk3Value | — |
| DEP27_PK4_VALUE | Dep27Pk4Value | — |
| DEP27_PK5_VALUE | Dep27Pk5Value | — |
| DEP27_TREE_NODE_ID | Dep27TreeNodeId | — |
| DEP28_DATA_SOURCE_ID | Dep28DataSourceId | — |
| DEP28_PK1_VALUE | Dep28Pk1Value | — |
| DEP28_PK2_VALUE | Dep28Pk2Value | — |
| DEP28_PK3_VALUE | Dep28Pk3Value | — |
| DEP28_PK4_VALUE | Dep28Pk4Value | — |
| DEP28_PK5_VALUE | Dep28Pk5Value | — |
| DEP28_TREE_NODE_ID | Dep28TreeNodeId | — |
| DEP29_DATA_SOURCE_ID | Dep29DataSourceId | — |
| DEP29_PK1_VALUE | Dep29Pk1Value | — |
| DEP29_PK2_VALUE | Dep29Pk2Value | — |
| DEP29_PK3_VALUE | Dep29Pk3Value | — |
| DEP29_PK4_VALUE | Dep29Pk4Value | — |
| DEP29_PK5_VALUE | Dep29Pk5Value | — |
| DEP29_TREE_NODE_ID | Dep29TreeNodeId | — |
| DEP2_DATA_SOURCE_ID | Dep2DataSourceId | — |
| DEP2_PK1_VALUE | Dep2Pk1Value | — |
| DEP2_PK2_VALUE | Dep2Pk2Value | — |
| DEP2_PK3_VALUE | Dep2Pk3Value | — |
| DEP2_PK4_VALUE | Dep2Pk4Value | — |
| DEP2_PK5_VALUE | Dep2Pk5Value | — |
| DEP2_TREE_NODE_ID | Dep2TreeNodeId | — |
| DEP30_DATA_SOURCE_ID | Dep30DataSourceId | — |
| DEP30_PK1_VALUE | Dep30Pk1Value | — |
| DEP30_PK2_VALUE | Dep30Pk2Value | — |
| DEP30_PK3_VALUE | Dep30Pk3Value | — |
| DEP30_PK4_VALUE | Dep30Pk4Value | — |
| DEP30_PK5_VALUE | Dep30Pk5Value | — |
| DEP30_TREE_NODE_ID | Dep30TreeNodeId | — |
| DEP31_DATA_SOURCE_ID | Dep31DataSourceId | — |
| DEP31_PK1_VALUE | Dep31Pk1Value | — |
| DEP31_PK2_VALUE | Dep31Pk2Value | — |
| DEP31_PK3_VALUE | Dep31Pk3Value | — |
| DEP31_PK4_VALUE | Dep31Pk4Value | — |
| DEP31_PK5_VALUE | Dep31Pk5Value | — |
| DEP31_TREE_NODE_ID | Dep31TreeNodeId | — |
| DEP3_DATA_SOURCE_ID | Dep3DataSourceId | — |
| DEP3_PK1_VALUE | Dep3Pk1Value | — |
| DEP3_PK2_VALUE | Dep3Pk2Value | — |
| DEP3_PK3_VALUE | Dep3Pk3Value | — |
| DEP3_PK4_VALUE | Dep3Pk4Value | — |
| DEP3_PK5_VALUE | Dep3Pk5Value | — |
| DEP3_TREE_NODE_ID | Dep3TreeNodeId | — |
| DEP4_DATA_SOURCE_ID | Dep4DataSourceId | — |
| DEP4_PK1_VALUE | Dep4Pk1Value | — |
| DEP4_PK2_VALUE | Dep4Pk2Value | — |
| DEP4_PK3_VALUE | Dep4Pk3Value | — |
| DEP4_PK4_VALUE | Dep4Pk4Value | — |
| DEP4_PK5_VALUE | Dep4Pk5Value | — |
| DEP4_TREE_NODE_ID | Dep4TreeNodeId | — |
| DEP5_DATA_SOURCE_ID | Dep5DataSourceId | — |
| DEP5_PK1_VALUE | Dep5Pk1Value | — |
| DEP5_PK2_VALUE | Dep5Pk2Value | — |
| DEP5_PK3_VALUE | Dep5Pk3Value | — |
| DEP5_PK4_VALUE | Dep5Pk4Value | — |
| DEP5_PK5_VALUE | Dep5Pk5Value | — |
| DEP5_TREE_NODE_ID | Dep5TreeNodeId | — |
| DEP6_DATA_SOURCE_ID | Dep6DataSourceId | — |
| DEP6_PK1_VALUE | Dep6Pk1Value | — |
| DEP6_PK2_VALUE | Dep6Pk2Value | — |
| DEP6_PK3_VALUE | Dep6Pk3Value | — |
| DEP6_PK4_VALUE | Dep6Pk4Value | — |
| DEP6_PK5_VALUE | Dep6Pk5Value | — |
| DEP6_TREE_NODE_ID | Dep6TreeNodeId | — |
| DEP7_DATA_SOURCE_ID | Dep7DataSourceId | — |
| DEP7_PK1_VALUE | Dep7Pk1Value | — |
| DEP7_PK2_VALUE | Dep7Pk2Value | — |
| DEP7_PK3_VALUE | Dep7Pk3Value | — |
| DEP7_PK4_VALUE | Dep7Pk4Value | — |
| DEP7_PK5_VALUE | Dep7Pk5Value | — |
| DEP7_TREE_NODE_ID | Dep7TreeNodeId | — |
| DEP8_DATA_SOURCE_ID | Dep8DataSourceId | — |
| DEP8_PK1_VALUE | Dep8Pk1Value | — |
| DEP8_PK2_VALUE | Dep8Pk2Value | — |
| DEP8_PK3_VALUE | Dep8Pk3Value | — |
| DEP8_PK4_VALUE | Dep8Pk4Value | — |
| DEP8_PK5_VALUE | Dep8Pk5Value | — |
| DEP8_TREE_NODE_ID | Dep8TreeNodeId | — |
| DEP9_DATA_SOURCE_ID | Dep9DataSourceId | — |
| DEP9_PK1_VALUE | Dep9Pk1Value | — |
| DEP9_PK2_VALUE | Dep9Pk2Value | — |
| DEP9_PK3_VALUE | Dep9Pk3Value | — |
| DEP9_PK4_VALUE | Dep9Pk4Value | — |
| DEP9_PK5_VALUE | Dep9Pk5Value | — |
| DEP9_TREE_NODE_ID | Dep9TreeNodeId | — |
| DISTANCE | Distance | — |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| TREE_CODE | TreeCode | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |

### [[flex_tree_vs_gl_balancing_vi|FLEX_TREE_VS_GL_BALANCING_VI]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DEP0_DATA_SOURCE_ID | Dep0DataSourceId | — |
| DEP0_PK1_VALUE | Dep0Pk1Value | — |
| DEP0_PK2_VALUE | Dep0Pk2Value | — |
| DEP0_PK3_VALUE | Dep0Pk3Value | — |
| DEP0_PK4_VALUE | Dep0Pk4Value | — |
| DEP0_PK5_VALUE | Dep0Pk5Value | — |
| DEP0_TREE_NODE_ID | Dep0TreeNodeId | — |
| DEP10_DATA_SOURCE_ID | Dep10DataSourceId | — |
| DEP10_PK1_VALUE | Dep10Pk1Value | — |
| DEP10_PK2_VALUE | Dep10Pk2Value | — |
| DEP10_PK3_VALUE | Dep10Pk3Value | — |
| DEP10_PK4_VALUE | Dep10Pk4Value | — |
| DEP10_PK5_VALUE | Dep10Pk5Value | — |
| DEP10_TREE_NODE_ID | Dep10TreeNodeId | — |
| DEP11_DATA_SOURCE_ID | Dep11DataSourceId | — |
| DEP11_PK1_VALUE | Dep11Pk1Value | — |
| DEP11_PK2_VALUE | Dep11Pk2Value | — |
| DEP11_PK3_VALUE | Dep11Pk3Value | — |
| DEP11_PK4_VALUE | Dep11Pk4Value | — |
| DEP11_PK5_VALUE | Dep11Pk5Value | — |
| DEP11_TREE_NODE_ID | Dep11TreeNodeId | — |
| DEP12_DATA_SOURCE_ID | Dep12DataSourceId | — |
| DEP12_PK1_VALUE | Dep12Pk1Value | — |
| DEP12_PK2_VALUE | Dep12Pk2Value | — |
| DEP12_PK3_VALUE | Dep12Pk3Value | — |
| DEP12_PK4_VALUE | Dep12Pk4Value | — |
| DEP12_PK5_VALUE | Dep12Pk5Value | — |
| DEP12_TREE_NODE_ID | Dep12TreeNodeId | — |
| DEP13_DATA_SOURCE_ID | Dep13DataSourceId | — |
| DEP13_PK1_VALUE | Dep13Pk1Value | — |
| DEP13_PK2_VALUE | Dep13Pk2Value | — |
| DEP13_PK3_VALUE | Dep13Pk3Value | — |
| DEP13_PK4_VALUE | Dep13Pk4Value | — |
| DEP13_PK5_VALUE | Dep13Pk5Value | — |
| DEP13_TREE_NODE_ID | Dep13TreeNodeId | — |
| DEP14_DATA_SOURCE_ID | Dep14DataSourceId | — |
| DEP14_PK1_VALUE | Dep14Pk1Value | — |
| DEP14_PK2_VALUE | Dep14Pk2Value | — |
| DEP14_PK3_VALUE | Dep14Pk3Value | — |
| DEP14_PK4_VALUE | Dep14Pk4Value | — |
| DEP14_PK5_VALUE | Dep14Pk5Value | — |
| DEP14_TREE_NODE_ID | Dep14TreeNodeId | — |
| DEP15_DATA_SOURCE_ID | Dep15DataSourceId | — |
| DEP15_PK1_VALUE | Dep15Pk1Value | — |
| DEP15_PK2_VALUE | Dep15Pk2Value | — |
| DEP15_PK3_VALUE | Dep15Pk3Value | — |
| DEP15_PK4_VALUE | Dep15Pk4Value | — |
| DEP15_PK5_VALUE | Dep15Pk5Value | — |
| DEP15_TREE_NODE_ID | Dep15TreeNodeId | — |
| DEP16_DATA_SOURCE_ID | Dep16DataSourceId | — |
| DEP16_PK1_VALUE | Dep16Pk1Value | — |
| DEP16_PK2_VALUE | Dep16Pk2Value | — |
| DEP16_PK3_VALUE | Dep16Pk3Value | — |
| DEP16_PK4_VALUE | Dep16Pk4Value | — |
| DEP16_PK5_VALUE | Dep16Pk5Value | — |
| DEP16_TREE_NODE_ID | Dep16TreeNodeId | — |
| DEP17_DATA_SOURCE_ID | Dep17DataSourceId | — |
| DEP17_PK1_VALUE | Dep17Pk1Value | — |
| DEP17_PK2_VALUE | Dep17Pk2Value | — |
| DEP17_PK3_VALUE | Dep17Pk3Value | — |
| DEP17_PK4_VALUE | Dep17Pk4Value | — |
| DEP17_PK5_VALUE | Dep17Pk5Value | — |
| DEP17_TREE_NODE_ID | Dep17TreeNodeId | — |
| DEP18_DATA_SOURCE_ID | Dep18DataSourceId | — |
| DEP18_PK1_VALUE | Dep18Pk1Value | — |
| DEP18_PK2_VALUE | Dep18Pk2Value | — |
| DEP18_PK3_VALUE | Dep18Pk3Value | — |
| DEP18_PK4_VALUE | Dep18Pk4Value | — |
| DEP18_PK5_VALUE | Dep18Pk5Value | — |
| DEP18_TREE_NODE_ID | Dep18TreeNodeId | — |
| DEP19_DATA_SOURCE_ID | Dep19DataSourceId | — |
| DEP19_PK1_VALUE | Dep19Pk1Value | — |
| DEP19_PK2_VALUE | Dep19Pk2Value | — |
| DEP19_PK3_VALUE | Dep19Pk3Value | — |
| DEP19_PK4_VALUE | Dep19Pk4Value | — |
| DEP19_PK5_VALUE | Dep19Pk5Value | — |
| DEP19_TREE_NODE_ID | Dep19TreeNodeId | — |
| DEP1_DATA_SOURCE_ID | Dep1DataSourceId | — |
| DEP1_PK1_VALUE | Dep1Pk1Value | — |
| DEP1_PK2_VALUE | Dep1Pk2Value | — |
| DEP1_PK3_VALUE | Dep1Pk3Value | — |
| DEP1_PK4_VALUE | Dep1Pk4Value | — |
| DEP1_PK5_VALUE | Dep1Pk5Value | — |
| DEP1_TREE_NODE_ID | Dep1TreeNodeId | — |
| DEP20_DATA_SOURCE_ID | Dep20DataSourceId | — |
| DEP20_PK1_VALUE | Dep20Pk1Value | — |
| DEP20_PK2_VALUE | Dep20Pk2Value | — |
| DEP20_PK3_VALUE | Dep20Pk3Value | — |
| DEP20_PK4_VALUE | Dep20Pk4Value | — |
| DEP20_PK5_VALUE | Dep20Pk5Value | — |
| DEP20_TREE_NODE_ID | Dep20TreeNodeId | — |
| DEP21_DATA_SOURCE_ID | Dep21DataSourceId | — |
| DEP21_PK1_VALUE | Dep21Pk1Value | — |
| DEP21_PK2_VALUE | Dep21Pk2Value | — |
| DEP21_PK3_VALUE | Dep21Pk3Value | — |
| DEP21_PK4_VALUE | Dep21Pk4Value | — |
| DEP21_PK5_VALUE | Dep21Pk5Value | — |
| DEP21_TREE_NODE_ID | Dep21TreeNodeId | — |
| DEP22_DATA_SOURCE_ID | Dep22DataSourceId | — |
| DEP22_PK1_VALUE | Dep22Pk1Value | — |
| DEP22_PK2_VALUE | Dep22Pk2Value | — |
| DEP22_PK3_VALUE | Dep22Pk3Value | — |
| DEP22_PK4_VALUE | Dep22Pk4Value | — |
| DEP22_PK5_VALUE | Dep22Pk5Value | — |
| DEP22_TREE_NODE_ID | Dep22TreeNodeId | — |
| DEP23_DATA_SOURCE_ID | Dep23DataSourceId | — |
| DEP23_PK1_VALUE | Dep23Pk1Value | — |
| DEP23_PK2_VALUE | Dep23Pk2Value | — |
| DEP23_PK3_VALUE | Dep23Pk3Value | — |
| DEP23_PK4_VALUE | Dep23Pk4Value | — |
| DEP23_PK5_VALUE | Dep23Pk5Value | — |
| DEP23_TREE_NODE_ID | Dep23TreeNodeId | — |
| DEP24_DATA_SOURCE_ID | Dep24DataSourceId | — |
| DEP24_PK1_VALUE | Dep24Pk1Value | — |
| DEP24_PK2_VALUE | Dep24Pk2Value | — |
| DEP24_PK3_VALUE | Dep24Pk3Value | — |
| DEP24_PK4_VALUE | Dep24Pk4Value | — |
| DEP24_PK5_VALUE | Dep24Pk5Value | — |
| DEP24_TREE_NODE_ID | Dep24TreeNodeId | — |
| DEP25_DATA_SOURCE_ID | Dep25DataSourceId | — |
| DEP25_PK1_VALUE | Dep25Pk1Value | — |
| DEP25_PK2_VALUE | Dep25Pk2Value | — |
| DEP25_PK3_VALUE | Dep25Pk3Value | — |
| DEP25_PK4_VALUE | Dep25Pk4Value | — |
| DEP25_PK5_VALUE | Dep25Pk5Value | — |
| DEP25_TREE_NODE_ID | Dep25TreeNodeId | — |
| DEP26_DATA_SOURCE_ID | Dep26DataSourceId | — |
| DEP26_PK1_VALUE | Dep26Pk1Value | — |
| DEP26_PK2_VALUE | Dep26Pk2Value | — |
| DEP26_PK3_VALUE | Dep26Pk3Value | — |
| DEP26_PK4_VALUE | Dep26Pk4Value | — |
| DEP26_PK5_VALUE | Dep26Pk5Value | — |
| DEP26_TREE_NODE_ID | Dep26TreeNodeId | — |
| DEP27_DATA_SOURCE_ID | Dep27DataSourceId | — |
| DEP27_PK1_VALUE | Dep27Pk1Value | — |
| DEP27_PK2_VALUE | Dep27Pk2Value | — |
| DEP27_PK3_VALUE | Dep27Pk3Value | — |
| DEP27_PK4_VALUE | Dep27Pk4Value | — |
| DEP27_PK5_VALUE | Dep27Pk5Value | — |
| DEP27_TREE_NODE_ID | Dep27TreeNodeId | — |
| DEP28_DATA_SOURCE_ID | Dep28DataSourceId | — |
| DEP28_PK1_VALUE | Dep28Pk1Value | — |
| DEP28_PK2_VALUE | Dep28Pk2Value | — |
| DEP28_PK3_VALUE | Dep28Pk3Value | — |
| DEP28_PK4_VALUE | Dep28Pk4Value | — |
| DEP28_PK5_VALUE | Dep28Pk5Value | — |
| DEP28_TREE_NODE_ID | Dep28TreeNodeId | — |
| DEP29_DATA_SOURCE_ID | Dep29DataSourceId | — |
| DEP29_PK1_VALUE | Dep29Pk1Value | — |
| DEP29_PK2_VALUE | Dep29Pk2Value | — |
| DEP29_PK3_VALUE | Dep29Pk3Value | — |
| DEP29_PK4_VALUE | Dep29Pk4Value | — |
| DEP29_PK5_VALUE | Dep29Pk5Value | — |
| DEP29_TREE_NODE_ID | Dep29TreeNodeId | — |
| DEP2_DATA_SOURCE_ID | Dep2DataSourceId | — |
| DEP2_PK1_VALUE | Dep2Pk1Value | — |
| DEP2_PK2_VALUE | Dep2Pk2Value | — |
| DEP2_PK3_VALUE | Dep2Pk3Value | — |
| DEP2_PK4_VALUE | Dep2Pk4Value | — |
| DEP2_PK5_VALUE | Dep2Pk5Value | — |
| DEP2_TREE_NODE_ID | Dep2TreeNodeId | — |
| DEP30_DATA_SOURCE_ID | Dep30DataSourceId | — |
| DEP30_PK1_VALUE | Dep30Pk1Value | — |
| DEP30_PK2_VALUE | Dep30Pk2Value | — |
| DEP30_PK3_VALUE | Dep30Pk3Value | — |
| DEP30_PK4_VALUE | Dep30Pk4Value | — |
| DEP30_PK5_VALUE | Dep30Pk5Value | — |
| DEP30_TREE_NODE_ID | Dep30TreeNodeId | — |
| DEP31_DATA_SOURCE_ID | Dep31DataSourceId | — |
| DEP31_PK1_VALUE | Dep31Pk1Value | — |
| DEP31_PK2_VALUE | Dep31Pk2Value | — |
| DEP31_PK3_VALUE | Dep31Pk3Value | — |
| DEP31_PK4_VALUE | Dep31Pk4Value | — |
| DEP31_PK5_VALUE | Dep31Pk5Value | — |
| DEP31_TREE_NODE_ID | Dep31TreeNodeId | — |
| DEP3_DATA_SOURCE_ID | Dep3DataSourceId | — |
| DEP3_PK1_VALUE | Dep3Pk1Value | — |
| DEP3_PK2_VALUE | Dep3Pk2Value | — |
| DEP3_PK3_VALUE | Dep3Pk3Value | — |
| DEP3_PK4_VALUE | Dep3Pk4Value | — |
| DEP3_PK5_VALUE | Dep3Pk5Value | — |
| DEP3_TREE_NODE_ID | Dep3TreeNodeId | — |
| DEP4_DATA_SOURCE_ID | Dep4DataSourceId | — |
| DEP4_PK1_VALUE | Dep4Pk1Value | — |
| DEP4_PK2_VALUE | Dep4Pk2Value | — |
| DEP4_PK3_VALUE | Dep4Pk3Value | — |
| DEP4_PK4_VALUE | Dep4Pk4Value | — |
| DEP4_PK5_VALUE | Dep4Pk5Value | — |
| DEP4_TREE_NODE_ID | Dep4TreeNodeId | — |
| DEP5_DATA_SOURCE_ID | Dep5DataSourceId | — |
| DEP5_PK1_VALUE | Dep5Pk1Value | — |
| DEP5_PK2_VALUE | Dep5Pk2Value | — |
| DEP5_PK3_VALUE | Dep5Pk3Value | — |
| DEP5_PK4_VALUE | Dep5Pk4Value | — |
| DEP5_PK5_VALUE | Dep5Pk5Value | — |
| DEP5_TREE_NODE_ID | Dep5TreeNodeId | — |
| DEP6_DATA_SOURCE_ID | Dep6DataSourceId | — |
| DEP6_PK1_VALUE | Dep6Pk1Value | — |
| DEP6_PK2_VALUE | Dep6Pk2Value | — |
| DEP6_PK3_VALUE | Dep6Pk3Value | — |
| DEP6_PK4_VALUE | Dep6Pk4Value | — |
| DEP6_PK5_VALUE | Dep6Pk5Value | — |
| DEP6_TREE_NODE_ID | Dep6TreeNodeId | — |
| DEP7_DATA_SOURCE_ID | Dep7DataSourceId | — |
| DEP7_PK1_VALUE | Dep7Pk1Value | — |
| DEP7_PK2_VALUE | Dep7Pk2Value | — |
| DEP7_PK3_VALUE | Dep7Pk3Value | — |
| DEP7_PK4_VALUE | Dep7Pk4Value | — |
| DEP7_PK5_VALUE | Dep7Pk5Value | — |
| DEP7_TREE_NODE_ID | Dep7TreeNodeId | — |
| DEP8_DATA_SOURCE_ID | Dep8DataSourceId | — |
| DEP8_PK1_VALUE | Dep8Pk1Value | — |
| DEP8_PK2_VALUE | Dep8Pk2Value | — |
| DEP8_PK3_VALUE | Dep8Pk3Value | — |
| DEP8_PK4_VALUE | Dep8Pk4Value | — |
| DEP8_PK5_VALUE | Dep8Pk5Value | — |
| DEP8_TREE_NODE_ID | Dep8TreeNodeId | — |
| DEP9_DATA_SOURCE_ID | Dep9DataSourceId | — |
| DEP9_PK1_VALUE | Dep9Pk1Value | — |
| DEP9_PK2_VALUE | Dep9Pk2Value | — |
| DEP9_PK3_VALUE | Dep9Pk3Value | — |
| DEP9_PK4_VALUE | Dep9Pk4Value | — |
| DEP9_PK5_VALUE | Dep9Pk5Value | — |
| DEP9_TREE_NODE_ID | Dep9TreeNodeId | — |
| DISTANCE | Distance | — |
| ENTERPRISE_ID | EnterpriseId | — |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| TREE_CODE | TreeCode | — |
| TREE_STRUCTURE_CODE | TreeStructureCode | — |
| TREE_VERSION_ID | TreeVersionId | — |

### [[segmentvaluehierarchyextractpvo|SegmentValueHierarchyExtractPVO]] (OTHER · BICC: 107/107)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEP0_DATA_SOURCE_ID | Dep0DataSourceId | ✅ |
| DEP0_PK1_VALUE | Dep0Pk1Value | ✅ |
| DEP0_PK2_VALUE | Dep0Pk2Value | ✅ |
| DEP10_DATA_SOURCE_ID | Dep10DataSourceId | ✅ |
| DEP10_PK1_VALUE | Dep10Pk1Value | ✅ |
| DEP10_PK2_VALUE | Dep10Pk2Value | ✅ |
| DEP11_DATA_SOURCE_ID | Dep11DataSourceId | ✅ |
| DEP11_PK1_VALUE | Dep11Pk1Value | ✅ |
| DEP11_PK2_VALUE | Dep11Pk2Value | ✅ |
| DEP12_DATA_SOURCE_ID | Dep12DataSourceId | ✅ |
| DEP12_PK1_VALUE | Dep12Pk1Value | ✅ |
| DEP12_PK2_VALUE | Dep12Pk2Value | ✅ |
| DEP13_DATA_SOURCE_ID | Dep13DataSourceId | ✅ |
| DEP13_PK1_VALUE | Dep13Pk1Value | ✅ |
| DEP13_PK2_VALUE | Dep13Pk2Value | ✅ |
| DEP14_DATA_SOURCE_ID | Dep14DataSourceId | ✅ |
| DEP14_PK1_VALUE | Dep14Pk1Value | ✅ |
| DEP14_PK2_VALUE | Dep14Pk2Value | ✅ |
| DEP15_DATA_SOURCE_ID | Dep15DataSourceId | ✅ |
| DEP15_PK1_VALUE | Dep15Pk1Value | ✅ |
| DEP15_PK2_VALUE | Dep15Pk2Value | ✅ |
| DEP16_DATA_SOURCE_ID | Dep16DataSourceId | ✅ |
| DEP16_PK1_VALUE | Dep16Pk1Value | ✅ |
| DEP16_PK2_VALUE | Dep16Pk2Value | ✅ |
| DEP17_DATA_SOURCE_ID | Dep17DataSourceId | ✅ |
| DEP17_PK1_VALUE | Dep17Pk1Value | ✅ |
| DEP17_PK2_VALUE | Dep17Pk2Value | ✅ |
| DEP18_DATA_SOURCE_ID | Dep18DataSourceId | ✅ |
| DEP18_PK1_VALUE | Dep18Pk1Value | ✅ |
| DEP18_PK2_VALUE | Dep18Pk2Value | ✅ |
| DEP19_DATA_SOURCE_ID | Dep19DataSourceId | ✅ |
| DEP19_PK1_VALUE | Dep19Pk1Value | ✅ |
| DEP19_PK2_VALUE | Dep19Pk2Value | ✅ |
| DEP1_DATA_SOURCE_ID | Dep1DataSourceId | ✅ |
| DEP1_PK1_VALUE | Dep1Pk1Value | ✅ |
| DEP1_PK2_VALUE | Dep1Pk2Value | ✅ |
| DEP20_DATA_SOURCE_ID | Dep20DataSourceId | ✅ |
| DEP20_PK1_VALUE | Dep20Pk1Value | ✅ |
| DEP20_PK2_VALUE | Dep20Pk2Value | ✅ |
| DEP21_DATA_SOURCE_ID | Dep21DataSourceId | ✅ |
| DEP21_PK1_VALUE | Dep21Pk1Value | ✅ |
| DEP21_PK2_VALUE | Dep21Pk2Value | ✅ |
| DEP22_DATA_SOURCE_ID | Dep22DataSourceId | ✅ |
| DEP22_PK1_VALUE | Dep22Pk1Value | ✅ |
| DEP22_PK2_VALUE | Dep22Pk2Value | ✅ |
| DEP23_DATA_SOURCE_ID | Dep23DataSourceId | ✅ |
| DEP23_PK1_VALUE | Dep23Pk1Value | ✅ |
| DEP23_PK2_VALUE | Dep23Pk2Value | ✅ |
| DEP24_DATA_SOURCE_ID | Dep24DataSourceId | ✅ |
| DEP24_PK1_VALUE | Dep24Pk1Value | ✅ |
| DEP24_PK2_VALUE | Dep24Pk2Value | ✅ |
| DEP25_DATA_SOURCE_ID | Dep25DataSourceId | ✅ |
| DEP25_PK1_VALUE | Dep25Pk1Value | ✅ |
| DEP25_PK2_VALUE | Dep25Pk2Value | ✅ |
| DEP26_DATA_SOURCE_ID | Dep26DataSourceId | ✅ |
| DEP26_PK1_VALUE | Dep26Pk1Value | ✅ |
| DEP26_PK2_VALUE | Dep26Pk2Value | ✅ |
| DEP27_DATA_SOURCE_ID | Dep27DataSourceId | ✅ |
| DEP27_PK1_VALUE | Dep27Pk1Value | ✅ |
| DEP27_PK2_VALUE | Dep27Pk2Value | ✅ |
| DEP28_DATA_SOURCE_ID | Dep28DataSourceId | ✅ |
| DEP28_PK1_VALUE | Dep28Pk1Value | ✅ |
| DEP28_PK2_VALUE | Dep28Pk2Value | ✅ |
| DEP29_DATA_SOURCE_ID | Dep29DataSourceId | ✅ |
| DEP29_PK1_VALUE | Dep29Pk1Value | ✅ |
| DEP29_PK2_VALUE | Dep29Pk2Value | ✅ |
| DEP2_DATA_SOURCE_ID | Dep2DataSourceId | ✅ |
| DEP2_PK1_VALUE | Dep2Pk1Value | ✅ |
| DEP2_PK2_VALUE | Dep2Pk2Value | ✅ |
| DEP30_DATA_SOURCE_ID | Dep30DataSourceId | ✅ |
| DEP30_PK1_VALUE | Dep30Pk1Value | ✅ |
| DEP30_PK2_VALUE | Dep30Pk2Value | ✅ |
| DEP31_DATA_SOURCE_ID | Dep31DataSourceId | ✅ |
| DEP31_PK1_VALUE | Dep31Pk1Value | ✅ |
| DEP31_PK2_VALUE | Dep31Pk2Value | ✅ |
| DEP3_DATA_SOURCE_ID | Dep3DataSourceId | ✅ |
| DEP3_PK1_VALUE | Dep3Pk1Value | ✅ |
| DEP3_PK2_VALUE | Dep3Pk2Value | ✅ |
| DEP4_DATA_SOURCE_ID | Dep4DataSourceId | ✅ |
| DEP4_PK1_VALUE | Dep4Pk1Value | ✅ |
| DEP4_PK2_VALUE | Dep4Pk2Value | ✅ |
| DEP5_DATA_SOURCE_ID | Dep5DataSourceId | ✅ |
| DEP5_PK1_VALUE | Dep5Pk1Value | ✅ |
| DEP5_PK2_VALUE | Dep5Pk2Value | ✅ |
| DEP6_DATA_SOURCE_ID | Dep6DataSourceId | ✅ |
| DEP6_PK1_VALUE | Dep6Pk1Value | ✅ |
| DEP6_PK2_VALUE | Dep6Pk2Value | ✅ |
| DEP7_DATA_SOURCE_ID | Dep7DataSourceId | ✅ |
| DEP7_PK1_VALUE | Dep7Pk1Value | ✅ |
| DEP7_PK2_VALUE | Dep7Pk2Value | ✅ |
| DEP8_DATA_SOURCE_ID | Dep8DataSourceId | ✅ |
| DEP8_PK1_VALUE | Dep8Pk1Value | ✅ |
| DEP8_PK2_VALUE | Dep8Pk2Value | ✅ |
| DEP9_DATA_SOURCE_ID | Dep9DataSourceId | ✅ |
| DEP9_PK1_VALUE | Dep9Pk1Value | ✅ |
| DEP9_PK2_VALUE | Dep9Pk2Value | ✅ |
| DISTANCE | Distance | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |

### [[segmentvaluehierarchypvo|SegmentValueHierarchyPVO]] (GL · BICC: 203/203)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEP0_DATA_SOURCE_ID | Dep0DataSourceId | ✅ |
| DEP0_PK1_VALUE | Dep0Pk1Value | ✅ |
| DEP0_PK2_VALUE | Dep0Pk2Value | ✅ |
| DEP0_PK3_VALUE | Dep0Pk3Value | ✅ |
| DEP0_PK4_VALUE | Dep0Pk4Value | ✅ |
| DEP0_PK5_VALUE | Dep0Pk5Value | ✅ |
| DEP10_DATA_SOURCE_ID | Dep10DataSourceId | ✅ |
| DEP10_PK1_VALUE | Dep10Pk1Value | ✅ |
| DEP10_PK2_VALUE | Dep10Pk2Value | ✅ |
| DEP10_PK3_VALUE | Dep10Pk3Value | ✅ |
| DEP10_PK4_VALUE | Dep10Pk4Value | ✅ |
| DEP10_PK5_VALUE | Dep10Pk5Value | ✅ |
| DEP11_DATA_SOURCE_ID | Dep11DataSourceId | ✅ |
| DEP11_PK1_VALUE | Dep11Pk1Value | ✅ |
| DEP11_PK2_VALUE | Dep11Pk2Value | ✅ |
| DEP11_PK3_VALUE | Dep11Pk3Value | ✅ |
| DEP11_PK4_VALUE | Dep11Pk4Value | ✅ |
| DEP11_PK5_VALUE | Dep11Pk5Value | ✅ |
| DEP12_DATA_SOURCE_ID | Dep12DataSourceId | ✅ |
| DEP12_PK1_VALUE | Dep12Pk1Value | ✅ |
| DEP12_PK2_VALUE | Dep12Pk2Value | ✅ |
| DEP12_PK3_VALUE | Dep12Pk3Value | ✅ |
| DEP12_PK4_VALUE | Dep12Pk4Value | ✅ |
| DEP12_PK5_VALUE | Dep12Pk5Value | ✅ |
| DEP13_DATA_SOURCE_ID | Dep13DataSourceId | ✅ |
| DEP13_PK1_VALUE | Dep13Pk1Value | ✅ |
| DEP13_PK2_VALUE | Dep13Pk2Value | ✅ |
| DEP13_PK3_VALUE | Dep13Pk3Value | ✅ |
| DEP13_PK4_VALUE | Dep13Pk4Value | ✅ |
| DEP13_PK5_VALUE | Dep13Pk5Value | ✅ |
| DEP14_DATA_SOURCE_ID | Dep14DataSourceId | ✅ |
| DEP14_PK1_VALUE | Dep14Pk1Value | ✅ |
| DEP14_PK2_VALUE | Dep14Pk2Value | ✅ |
| DEP14_PK3_VALUE | Dep14Pk3Value | ✅ |
| DEP14_PK4_VALUE | Dep14Pk4Value | ✅ |
| DEP14_PK5_VALUE | Dep14Pk5Value | ✅ |
| DEP15_DATA_SOURCE_ID | Dep15DataSourceId | ✅ |
| DEP15_PK1_VALUE | Dep15Pk1Value | ✅ |
| DEP15_PK2_VALUE | Dep15Pk2Value | ✅ |
| DEP15_PK3_VALUE | Dep15Pk3Value | ✅ |
| DEP15_PK4_VALUE | Dep15Pk4Value | ✅ |
| DEP15_PK5_VALUE | Dep15Pk5Value | ✅ |
| DEP16_DATA_SOURCE_ID | Dep16DataSourceId | ✅ |
| DEP16_PK1_VALUE | Dep16Pk1Value | ✅ |
| DEP16_PK2_VALUE | Dep16Pk2Value | ✅ |
| DEP16_PK3_VALUE | Dep16Pk3Value | ✅ |
| DEP16_PK4_VALUE | Dep16Pk4Value | ✅ |
| DEP16_PK5_VALUE | Dep16Pk5Value | ✅ |
| DEP17_DATA_SOURCE_ID | Dep17DataSourceId | ✅ |
| DEP17_PK1_VALUE | Dep17Pk1Value | ✅ |
| DEP17_PK2_VALUE | Dep17Pk2Value | ✅ |
| DEP17_PK3_VALUE | Dep17Pk3Value | ✅ |
| DEP17_PK4_VALUE | Dep17Pk4Value | ✅ |
| DEP17_PK5_VALUE | Dep17Pk5Value | ✅ |
| DEP18_DATA_SOURCE_ID | Dep18DataSourceId | ✅ |
| DEP18_PK1_VALUE | Dep18Pk1Value | ✅ |
| DEP18_PK2_VALUE | Dep18Pk2Value | ✅ |
| DEP18_PK3_VALUE | Dep18Pk3Value | ✅ |
| DEP18_PK4_VALUE | Dep18Pk4Value | ✅ |
| DEP18_PK5_VALUE | Dep18Pk5Value | ✅ |
| DEP19_DATA_SOURCE_ID | Dep19DataSourceId | ✅ |
| DEP19_PK1_VALUE | Dep19Pk1Value | ✅ |
| DEP19_PK2_VALUE | Dep19Pk2Value | ✅ |
| DEP19_PK3_VALUE | Dep19Pk3Value | ✅ |
| DEP19_PK4_VALUE | Dep19Pk4Value | ✅ |
| DEP19_PK5_VALUE | Dep19Pk5Value | ✅ |
| DEP1_DATA_SOURCE_ID | Dep1DataSourceId | ✅ |
| DEP1_PK1_VALUE | Dep1Pk1Value | ✅ |
| DEP1_PK2_VALUE | Dep1Pk2Value | ✅ |
| DEP1_PK3_VALUE | Dep1Pk3Value | ✅ |
| DEP1_PK4_VALUE | Dep1Pk4Value | ✅ |
| DEP1_PK5_VALUE | Dep1Pk5Value | ✅ |
| DEP20_DATA_SOURCE_ID | Dep20DataSourceId | ✅ |
| DEP20_PK1_VALUE | Dep20Pk1Value | ✅ |
| DEP20_PK2_VALUE | Dep20Pk2Value | ✅ |
| DEP20_PK3_VALUE | Dep20Pk3Value | ✅ |
| DEP20_PK4_VALUE | Dep20Pk4Value | ✅ |
| DEP20_PK5_VALUE | Dep20Pk5Value | ✅ |
| DEP21_DATA_SOURCE_ID | Dep21DataSourceId | ✅ |
| DEP21_PK1_VALUE | Dep21Pk1Value | ✅ |
| DEP21_PK2_VALUE | Dep21Pk2Value | ✅ |
| DEP21_PK3_VALUE | Dep21Pk3Value | ✅ |
| DEP21_PK4_VALUE | Dep21Pk4Value | ✅ |
| DEP21_PK5_VALUE | Dep21Pk5Value | ✅ |
| DEP22_DATA_SOURCE_ID | Dep22DataSourceId | ✅ |
| DEP22_PK1_VALUE | Dep22Pk1Value | ✅ |
| DEP22_PK2_VALUE | Dep22Pk2Value | ✅ |
| DEP22_PK3_VALUE | Dep22Pk3Value | ✅ |
| DEP22_PK4_VALUE | Dep22Pk4Value | ✅ |
| DEP22_PK5_VALUE | Dep22Pk5Value | ✅ |
| DEP23_DATA_SOURCE_ID | Dep23DataSourceId | ✅ |
| DEP23_PK1_VALUE | Dep23Pk1Value | ✅ |
| DEP23_PK2_VALUE | Dep23Pk2Value | ✅ |
| DEP23_PK3_VALUE | Dep23Pk3Value | ✅ |
| DEP23_PK4_VALUE | Dep23Pk4Value | ✅ |
| DEP23_PK5_VALUE | Dep23Pk5Value | ✅ |
| DEP24_DATA_SOURCE_ID | Dep24DataSourceId | ✅ |
| DEP24_PK1_VALUE | Dep24Pk1Value | ✅ |
| DEP24_PK2_VALUE | Dep24Pk2Value | ✅ |
| DEP24_PK3_VALUE | Dep24Pk3Value | ✅ |
| DEP24_PK4_VALUE | Dep24Pk4Value | ✅ |
| DEP24_PK5_VALUE | Dep24Pk5Value | ✅ |
| DEP25_DATA_SOURCE_ID | Dep25DataSourceId | ✅ |
| DEP25_PK1_VALUE | Dep25Pk1Value | ✅ |
| DEP25_PK2_VALUE | Dep25Pk2Value | ✅ |
| DEP25_PK3_VALUE | Dep25Pk3Value | ✅ |
| DEP25_PK4_VALUE | Dep25Pk4Value | ✅ |
| DEP25_PK5_VALUE | Dep25Pk5Value | ✅ |
| DEP26_DATA_SOURCE_ID | Dep26DataSourceId | ✅ |
| DEP26_PK1_VALUE | Dep26Pk1Value | ✅ |
| DEP26_PK2_VALUE | Dep26Pk2Value | ✅ |
| DEP26_PK3_VALUE | Dep26Pk3Value | ✅ |
| DEP26_PK4_VALUE | Dep26Pk4Value | ✅ |
| DEP26_PK5_VALUE | Dep26Pk5Value | ✅ |
| DEP27_DATA_SOURCE_ID | Dep27DataSourceId | ✅ |
| DEP27_PK1_VALUE | Dep27Pk1Value | ✅ |
| DEP27_PK2_VALUE | Dep27Pk2Value | ✅ |
| DEP27_PK3_VALUE | Dep27Pk3Value | ✅ |
| DEP27_PK4_VALUE | Dep27Pk4Value | ✅ |
| DEP27_PK5_VALUE | Dep27Pk5Value | ✅ |
| DEP28_DATA_SOURCE_ID | Dep28DataSourceId | ✅ |
| DEP28_PK1_VALUE | Dep28Pk1Value | ✅ |
| DEP28_PK2_VALUE | Dep28Pk2Value | ✅ |
| DEP28_PK3_VALUE | Dep28Pk3Value | ✅ |
| DEP28_PK4_VALUE | Dep28Pk4Value | ✅ |
| DEP28_PK5_VALUE | Dep28Pk5Value | ✅ |
| DEP29_DATA_SOURCE_ID | Dep29DataSourceId | ✅ |
| DEP29_PK1_VALUE | Dep29Pk1Value | ✅ |
| DEP29_PK2_VALUE | Dep29Pk2Value | ✅ |
| DEP29_PK3_VALUE | Dep29Pk3Value | ✅ |
| DEP29_PK4_VALUE | Dep29Pk4Value | ✅ |
| DEP29_PK5_VALUE | Dep29Pk5Value | ✅ |
| DEP2_DATA_SOURCE_ID | Dep2DataSourceId | ✅ |
| DEP2_PK1_VALUE | Dep2Pk1Value | ✅ |
| DEP2_PK2_VALUE | Dep2Pk2Value | ✅ |
| DEP2_PK3_VALUE | Dep2Pk3Value | ✅ |
| DEP2_PK4_VALUE | Dep2Pk4Value | ✅ |
| DEP2_PK5_VALUE | Dep2Pk5Value | ✅ |
| DEP30_DATA_SOURCE_ID | Dep30DataSourceId | ✅ |
| DEP30_PK1_VALUE | Dep30Pk1Value | ✅ |
| DEP30_PK2_VALUE | Dep30Pk2Value | ✅ |
| DEP30_PK3_VALUE | Dep30Pk3Value | ✅ |
| DEP30_PK4_VALUE | Dep30Pk4Value | ✅ |
| DEP30_PK5_VALUE | Dep30Pk5Value | ✅ |
| DEP31_DATA_SOURCE_ID | Dep31DataSourceId | ✅ |
| DEP31_PK1_VALUE | Dep31Pk1Value | ✅ |
| DEP31_PK2_VALUE | Dep31Pk2Value | ✅ |
| DEP31_PK3_VALUE | Dep31Pk3Value | ✅ |
| DEP31_PK4_VALUE | Dep31Pk4Value | ✅ |
| DEP31_PK5_VALUE | Dep31Pk5Value | ✅ |
| DEP3_DATA_SOURCE_ID | Dep3DataSourceId | ✅ |
| DEP3_PK1_VALUE | Dep3Pk1Value | ✅ |
| DEP3_PK2_VALUE | Dep3Pk2Value | ✅ |
| DEP3_PK3_VALUE | Dep3Pk3Value | ✅ |
| DEP3_PK4_VALUE | Dep3Pk4Value | ✅ |
| DEP3_PK5_VALUE | Dep3Pk5Value | ✅ |
| DEP4_DATA_SOURCE_ID | Dep4DataSourceId | ✅ |
| DEP4_PK1_VALUE | Dep4Pk1Value | ✅ |
| DEP4_PK2_VALUE | Dep4Pk2Value | ✅ |
| DEP4_PK3_VALUE | Dep4Pk3Value | ✅ |
| DEP4_PK4_VALUE | Dep4Pk4Value | ✅ |
| DEP4_PK5_VALUE | Dep4Pk5Value | ✅ |
| DEP5_DATA_SOURCE_ID | Dep5DataSourceId | ✅ |
| DEP5_PK1_VALUE | Dep5Pk1Value | ✅ |
| DEP5_PK2_VALUE | Dep5Pk2Value | ✅ |
| DEP5_PK3_VALUE | Dep5Pk3Value | ✅ |
| DEP5_PK4_VALUE | Dep5Pk4Value | ✅ |
| DEP5_PK5_VALUE | Dep5Pk5Value | ✅ |
| DEP6_DATA_SOURCE_ID | Dep6DataSourceId | ✅ |
| DEP6_PK1_VALUE | Dep6Pk1Value | ✅ |
| DEP6_PK2_VALUE | Dep6Pk2Value | ✅ |
| DEP6_PK3_VALUE | Dep6Pk3Value | ✅ |
| DEP6_PK4_VALUE | Dep6Pk4Value | ✅ |
| DEP6_PK5_VALUE | Dep6Pk5Value | ✅ |
| DEP7_DATA_SOURCE_ID | Dep7DataSourceId | ✅ |
| DEP7_PK1_VALUE | Dep7Pk1Value | ✅ |
| DEP7_PK2_VALUE | Dep7Pk2Value | ✅ |
| DEP7_PK3_VALUE | Dep7Pk3Value | ✅ |
| DEP7_PK4_VALUE | Dep7Pk4Value | ✅ |
| DEP7_PK5_VALUE | Dep7Pk5Value | ✅ |
| DEP8_DATA_SOURCE_ID | Dep8DataSourceId | ✅ |
| DEP8_PK1_VALUE | Dep8Pk1Value | ✅ |
| DEP8_PK2_VALUE | Dep8Pk2Value | ✅ |
| DEP8_PK3_VALUE | Dep8Pk3Value | ✅ |
| DEP8_PK4_VALUE | Dep8Pk4Value | ✅ |
| DEP8_PK5_VALUE | Dep8Pk5Value | ✅ |
| DEP9_DATA_SOURCE_ID | Dep9DataSourceId | ✅ |
| DEP9_PK1_VALUE | Dep9Pk1Value | ✅ |
| DEP9_PK2_VALUE | Dep9Pk2Value | ✅ |
| DEP9_PK3_VALUE | Dep9Pk3Value | ✅ |
| DEP9_PK4_VALUE | Dep9Pk4Value | ✅ |
| DEP9_PK5_VALUE | Dep9Pk5Value | ✅ |
| DISTANCE | Distance | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — GL Segment Value Hierarchies](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/)
- [[gl-module-data-dictionary]] — Dossiê do módulo GL
