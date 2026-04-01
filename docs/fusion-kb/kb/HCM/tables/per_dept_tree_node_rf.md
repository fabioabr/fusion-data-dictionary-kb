---
id: DOC-HCM-652
doc_type: system-doc
title: "PER_DEPT_TREE_NODE_RF — Referências de Nós da Árvore Departamental"
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
  - organization
  - hierarquia
  - dept-tree-references
aliases:
  - PER_DEPT_TREE_NODE_RF
  - per_dept_tree_node_rf
  - per-dept-tree-node-rf
  - referências-de-nós-da-árvore-departamental
  - per-dept-tree-node-r
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DEPT_TREE_NODE_RF

## 📌 Visão Geral

Armazena **referências** adicionais associadas aos nós da árvore departamental. Permite vincular referências externas ou documentos a nós específicos da hierarquia.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Referências cruzadas** — vincula nós da árvore a entidades externas.
- **Mapeamento** — associação de departamentos com referências de outros sistemas.
- **Integração** — suporte a integrações com estruturas organizacionais externas.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_NODE_RF_ID | NUMBER(18) | NOT NULL | PK | Identificador único da referência | — | 🟢 85% |
| 2 | TREE_NODE_ID | NUMBER(18) | NOT NULL | FK | Nó da árvore | PER_DEPT_TREE_NODE | 🟢 85% |
| 3 | REF_PK1_VALUE | NUMBER(18) | NULL | FK | Valor de referência (chave estrangeira genérica) | — | 🟡 70% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_dept_tree_node]] — via `TREE_NODE_ID` (nó da árvore de departamentos (referência))

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Referências de um nó
```sql
SELECT prf.REF_PK1_VALUE
FROM   PER_DEPT_TREE_NODE_RF prf
WHERE  prf.TREE_NODE_ID = :p_tree_node_id;
```

### Filtros comuns
- `TREE_NODE_ID = :p_node_id` — Referências de um nó específico
---

## 🔒 Observações

- Tabela de referências genéricas — o significado de `REF_PK1_VALUE` depende do contexto.
- Utilizada para associar nós da árvore com entidades de outros módulos.
---

## 🔗 PVOs Relacionados

### [[depttreenoderfextractpvo|DeptTreeNodeRFExtractPVO]] (HCM · BICC: 28/28)

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

---

## 📚 Referências

- [Oracle Docs — PER_DEPT_TREE_NODE_RF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdeptreenoderf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
