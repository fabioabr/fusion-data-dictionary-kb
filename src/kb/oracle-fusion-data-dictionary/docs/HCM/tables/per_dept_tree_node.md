---
id: DOC-HCM-650
doc_type: system-doc
title: "PER_DEPT_TREE_NODE — Nós da Árvore Departamental"
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
  - department-tree
aliases:
  - PER_DEPT_TREE_NODE
  - per_dept_tree_node
  - per-dept-tree-node
  - nós-da-árvore-departamental
  - per-dept-tree-node
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DEPT_TREE_NODE

## 📌 Visão Geral

Armazena os **nós da árvore hierárquica departamental**. Define a estrutura organizacional em formato de árvore, com relações pai-filho entre departamentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Hierarquia organizacional** — define a estrutura de departamentos em árvore.
- **Relatórios** — base para relatórios hierárquicos de departamentos.
- **Navegação** — permite navegação drill-down pela estrutura organizacional.
- **Orçamento** — alocação de orçamento por nível hierárquico.
- **Segurança** — controle de acesso por posição na árvore.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do nó | — | 🟢 90% |
| 2 | TREE_STRUCTURE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da estrutura da árvore | — | 🟢 85% |
| 3 | TREE_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da árvore | — | 🟢 85% |
| 4 | PARENT_TREE_NODE_ID | NUMBER(18) | NULL | FK | Nó pai na hierarquia | PER_DEPT_TREE_NODE | 🟢 85% |
| 5 | DEPTH | NUMBER | NULL | Dados | Profundidade na árvore (nível) | — | 🟢 80% |
| 6 | PK1_START_VALUE | NUMBER(18) | NULL | FK | ID do departamento (início da faixa) | — | 🟢 80% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_dept_tree_node]] — via `PARENT_TREE_NODE_ID` (nó pai — auto-referência)

### Tabelas-filha (FK de saída)
- [[per_dept_tree_node]] — via `PARENT_TREE_NODE_ID` (nós filhos)
- [[per_dept_tree_node_cf]] — via `TREE_NODE_ID` (classificações do nó)
- [[per_dept_tree_node_rf]] — via `TREE_NODE_ID` (referências do nó)

---

## 📎 Uso Típico

### Hierarquia departamental
```sql
SELECT pdn.TREE_NODE_ID, pdn.PARENT_TREE_NODE_ID, pdn.DEPTH,
       pdn.PK1_START_VALUE AS DEPARTMENT_ID
FROM   PER_DEPT_TREE_NODE pdn
WHERE  pdn.TREE_CODE = :p_tree_code
ORDER BY pdn.DEPTH, pdn.TREE_NODE_ID;
```

### Filtros comuns
- `DEPTH = 1` — Nós do primeiro nível
- `PARENT_TREE_NODE_ID IS NULL` — Nó raiz
---

## 🔒 Observações

- Tabela auto-referenciável — cada nó pode ter um pai na mesma tabela.
- O `PK1_START_VALUE` tipicamente contém o ORGANIZATION_ID do departamento.
- A `DEPTH` indica o nível na hierarquia (0=raiz, 1=primeiro nível, etc.).
- Utilizada em conjunto com tabelas de organização para construir organogramas.
---

## 🔗 PVOs Relacionados

### [[depttreenodeextractpvo|DeptTreeNodeExtractPVO]] (HCM · BICC: 35/35)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CHILD_COUNT | ChildCount | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DATA_SOURCE_ID | DataSourceId | ✅ |
| DEPTH | Depth | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| PARENT_DATA_SOURCE_ID | ParentDataSourceId | ✅ |
| PARENT_PK1_VALUE | ParentPk1Value | ✅ |
| PARENT_PK2_VALUE | ParentPk2Value | ✅ |
| PARENT_PK3_VALUE | ParentPk3Value | ✅ |
| PARENT_PK4_VALUE | ParentPk4Value | ✅ |
| PARENT_PK5_VALUE | ParentPk5Value | ✅ |
| PARENT_TREE_LABEL_ID | ParentTreeLabelId | ✅ |
| PARENT_TREE_NODE_ID | ParentTreeNodeId | ✅ |
| PK1_END_VALUE | Pk1EndValue | ✅ |
| PK1_START_VALUE | Pk1StartValue | ✅ |
| PK2_END_VALUE | Pk2EndValue | ✅ |
| PK2_START_VALUE | Pk2StartValue | ✅ |
| PK3_END_VALUE | Pk3EndValue | ✅ |
| PK3_START_VALUE | Pk3StartValue | ✅ |
| PK4_END_VALUE | Pk4EndValue | ✅ |
| PK4_START_VALUE | Pk4StartValue | ✅ |
| PK5_END_VALUE | Pk5EndValue | ✅ |
| PK5_START_VALUE | Pk5StartValue | ✅ |
| REFERENCE_TREE_CODE | ReferenceTreeCode | ✅ |
| REFERENCE_TREE_VERSION_ID | ReferenceTreeVersionId | ✅ |
| SORT_ORDER | SortOrder | ✅ |
| TREE_CODE | TreeCode | ✅ |
| TREE_LABEL_ID | TreeLabelId | ✅ |
| TREE_NODE_ID | TreeNodeId | ✅ |
| TREE_STRUCTURE_CODE | TreeStructureCode | ✅ |
| TREE_VERSION_ID | TreeVersionId | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_DEPT_TREE_NODE](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdepttreenode.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
