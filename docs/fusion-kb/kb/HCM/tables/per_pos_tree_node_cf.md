---
id: DOC-HCM-702
doc_type: system-doc
title: "PER_POS_TREE_NODE_CF — Nós de Árvore de Posições (Calculated/Flat)"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - arvore-posicoes
  - position-tree
  - calculated-flat
  - hierarquia
aliases:
  - PER_POS_TREE_NODE_CF
  - per_pos_tree_node_cf
  - nos-arvore-posicoes-cf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POS_TREE_NODE_CF

## Visão Geral

Armazena os **nós da árvore de posições** em formato achatado (flattened/calculated). Contém a estrutura hierárquica de posições/cargos pré-calculada, permitindo consultas de ancestralidade e descendência sem recursão.

> [!note] Sufixo _CF
> O sufixo `_CF` indica tabela **Calculated/Flat** — dados pré-calculados e desnormalizados para performance.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Navegação na árvore de posições** — acessar relações hierárquicas sem recursão
- **Relatórios por posição** — consolidar métricas por nível de cargo
- **Segurança baseada em posição** — controlar acesso por hierarquia de cargos
- **Análise de headcount** — contar posições por nível e ramificação

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do nó | — | 🟡 80% |
| 2 | TREE_STRUCTURE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da estrutura da árvore | — | 🟡 75% |
| 3 | TREE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da árvore específica | — | 🟡 75% |
| 4 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Posição no nó | HR_ALL_POSITIONS_F | 🟢 85% |
| 5 | ANCESTOR_POSITION_ID | NUMBER(18) | NULL | FK | Posição ancestral | HR_ALL_POSITIONS_F | 🟡 75% |
| 6 | DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó na árvore | — | 🟡 75% |
| 7 | DISTANCE | NUMBER | NULL | Hierarquia | Distância entre nó e ancestral | — | 🟡 70% |
| 8 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 9 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` e `ANCESTOR_POSITION_ID` (posição no nó da árvore de posições)

### Tabelas-filha (FK de saída)

---

## Uso Típico

### Posições descendentes de uma posição ancestral
```sql
SELECT cf.POSITION_ID, cf.DEPTH, cf.DISTANCE
FROM   PER_POS_TREE_NODE_CF cf
WHERE  cf.ANCESTOR_POSITION_ID = :p_position_id
  AND  cf.TREE_CODE = :p_tree_code
ORDER BY cf.DEPTH;
```

---

## Observações

- Tabela pré-calculada: dados gerados por processos batch.
- `DEPTH` indica profundidade absoluta; `DISTANCE` indica distância relativa ao ancestral.
- Suporta múltiplas versões de árvore via `TREE_STRUCTURE_CODE` e `TREE_CODE`.

---

## Referências

- [Oracle Docs — PER_POS_TREE_NODE_CF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpostreenodecf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[positiontreebicvo|PositionTreeBICVO]] (PO · BICC: 6/235)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CF_TREE_NODE_ID | CfTreeNodeId | ✅ |
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
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| TREE_CODE | TreeCode | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
