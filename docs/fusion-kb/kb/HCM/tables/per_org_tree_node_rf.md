---
id: DOC-HCM-684
doc_type: system-doc
title: "PER_ORG_TREE_NODE_RF — Nós de Árvore Organizacional (Reference/Flat)"
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
  - arvore-organizacional
  - org-tree
  - reference-flat
  - hierarquia
aliases:
  - PER_ORG_TREE_NODE_RF
  - per_org_tree_node_rf
  - nos-arvore-organizacional-rf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_ORG_TREE_NODE_RF

## Visão Geral

Armazena os **nós de referência da árvore organizacional** em formato achatado. Contém informações de referência cruzada e dados adicionais para cada nó da estrutura organizacional, complementando a tabela `PER_ORG_TREE_NODE_CF`.

> [!note] Sufixo _RF
> O sufixo `_RF` indica tabela **Reference/Flat** — dados de referência desnormalizados.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Referência cruzada organizacional** — mapear organizações entre diferentes árvores
- **Relatórios de estrutura organizacional** — complementar dados da árvore com referências
- **Integrações entre sistemas** — prover dados de referência para sincronização
- **Análise de reorganizações** — acompanhar mudanças na estrutura organizacional

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do nó na árvore | — | 🟡 80% |
| 2 | TREE_STRUCTURE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da estrutura da árvore | — | 🟡 75% |
| 3 | TREE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da árvore específica | — | 🟡 75% |
| 4 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Identificador da organização | HR_ALL_ORGANIZATION_UNITS | 🟢 85% |
| 5 | PARENT_TREE_NODE_ID | NUMBER(18) | NULL | FK | Nó pai na árvore | PER_ORG_TREE_NODE_RF | 🟡 75% |
| 6 | DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó | — | 🟡 75% |
| 7 | DISPLAY_ORDER | NUMBER | NULL | Apresentação | Ordem de exibição entre irmãos | — | 🟡 65% |
| 8 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 9 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units]] — via `ORGANIZATION_ID` (unidade organizacional do nó da árvore)
- [[per_org_tree_node_cf]] — via `TREE_NODE_ID` (nó filho da árvore organizacional)

### Tabelas-filha (FK de saída)
- Auto-referência via `PARENT_TREE_NODE_ID`

---

## Uso Típico

### Listar nós filhos diretos de uma organização na árvore
```sql
SELECT rf.TREE_NODE_ID, rf.ORGANIZATION_ID, rf.DEPTH, rf.DISPLAY_ORDER
FROM   PER_ORG_TREE_NODE_RF rf
WHERE  rf.PARENT_TREE_NODE_ID = :p_parent_node_id
  AND  rf.TREE_CODE = :p_tree_code
ORDER BY rf.DISPLAY_ORDER;
```

---

## Observações

- Tabela de referência desnormalizada para consultas diretas na hierarquia.
- `DISPLAY_ORDER` controla a ordem de exibição dos nós irmãos.
- Suporta auto-referência via `PARENT_TREE_NODE_ID`.

---

## Referências

- [Oracle Docs — PER_ORG_TREE_NODE_RF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perorgtreenoderf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[orgtreebirvoforfscm|OrgTreeBIRVOForFscm]] (HCM · BICC: 28/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ANCESTOR_DATA_SOURCE_ID | AncestorDataSourceId | ✅ |
| ANCESTOR_PK1_VALUE | AncestorPk1Value | ✅ |
| ANCESTOR_PK2_VALUE | AncestorPk2Value | ✅ |
| ANCESTOR_PK3_VALUE | AncestorPk3Value | ✅ |
| ANCESTOR_PK4_VALUE | AncestorPk4Value | ✅ |
| ANCESTOR_PK5_VALUE | AncestorPk5Value | ✅ |
| ANCESTOR_TREE_LABEL_ID | AncestorTreeLabelId | ✅ |
| ANCESTOR_TREE_NODE_ID | AncestorTreeNodeId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SOURCE_ID | DataSourceId | ✅ |
| DISTANCE | Distance | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| IS_LEAF | IsLeaf | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| PK1_VALUE | Pk1Value | ✅ |
| PK2_VALUE | Pk2Value | ✅ |
| PK3_VALUE | Pk3Value | ✅ |
| PK4_VALUE | Pk4Value | ✅ |
| PK5_VALUE | Pk5Value | ✅ |
| RF_TREE_NODE_ID | RfTreeNodeId | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_LABEL_ID | TreeLabelId | ✅ |
| TREE_NODE_ID | TreeNodeId | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |
