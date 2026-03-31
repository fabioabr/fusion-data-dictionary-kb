---
id: DOC-HCM-651
doc_type: system-doc
title: "PER_DEPT_TREE_NODE_CF — Classificações de Nós da Árvore Departamental"
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
  - dept-tree-classifications
aliases:
  - PER_DEPT_TREE_NODE_CF
  - per_dept_tree_node_cf
  - per-dept-tree-node-cf
  - classificações-de-nós-da-árvore-departamental
  - per-dept-tree-node-c
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_DEPT_TREE_NODE_CF

## 📌 Visão Geral

Armazena **classificações (classifications)** adicionais para nós da árvore departamental. Permite adicionar atributos de classificação a cada nó da hierarquia.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Classificação de departamentos** — atributos adicionais por nó da árvore.
- **Flexibilidade** — permite categorizar nós sem alterar a estrutura base.
- **Relatórios** — segmentação por classificação de departamento.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | TREE_NODE_CF_ID | NUMBER(18) | NOT NULL | PK | Identificador único da classificação | — | 🟢 85% |
| 2 | TREE_NODE_ID | NUMBER(18) | NOT NULL | FK | Nó da árvore | PER_DEPT_TREE_NODE | 🟢 85% |
| 3 | CLASSIFICATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da classificação | — | 🟡 75% |
| 4 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 5 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 6 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 7 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_dept_tree_node]] — via `TREE_NODE_ID` (nó da árvore hierárquica de departamentos)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Classificações de um nó
```sql
SELECT pcf.CLASSIFICATION_CODE
FROM   PER_DEPT_TREE_NODE_CF pcf
WHERE  pcf.TREE_NODE_ID = :p_tree_node_id;
```

### Filtros comuns
- `CLASSIFICATION_CODE = :p_code` — Classificação específica
---

## 🔒 Observações

- Permite adicionar metadados de classificação aos nós da árvore departamental.
- Utilizada para filtros avançados em relatórios hierárquicos.
---

## 📚 Referências

- [Oracle Docs — PER_DEPT_TREE_NODE_CF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perdeptreenodecf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
