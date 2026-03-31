---
id: DOC-HCM-683
doc_type: system-doc
title: "PER_ORG_TREE_NODE_CF — Nós de Árvore Organizacional (Calculated/Flat)"
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
  - calculated-flat
  - hierarquia
aliases:
  - PER_ORG_TREE_NODE_CF
  - per_org_tree_node_cf
  - nos-arvore-organizacional-cf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_ORG_TREE_NODE_CF

## Visão Geral

Armazena os **nós da árvore organizacional** em formato achatado (flattened/calculated). Contém a estrutura hierárquica das organizações pré-calculada, permitindo consultas de ancestralidade e descendência sem recursão.

> [!note] Sufixo _CF
> O sufixo `_CF` indica tabela **Calculated/Flat** — dados pré-calculados e desnormalizados para performance.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Navegação na estrutura organizacional** — visualizar a árvore de organizações
- **Relatórios de headcount por unidade organizacional**
- **Segurança baseada em organização** — controlar acesso por departamento/divisão
- **Consolidação financeira** — agregar dados por nível organizacional
- **Análise de estrutura organizacional** — identificar níveis e amplitude

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
| 4 | ORGANIZATION_ID | NUMBER(18) | NOT NULL | FK | Identificador da organização no nó | HR_ALL_ORGANIZATION_UNITS | 🟢 85% |
| 5 | PARENT_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização pai na hierarquia | HR_ALL_ORGANIZATION_UNITS | 🟡 80% |
| 6 | DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó na árvore | — | 🟡 75% |
| 7 | ANCESTOR_ORGANIZATION_ID | NUMBER(18) | NULL | FK | Organização ancestral | HR_ALL_ORGANIZATION_UNITS | 🟡 70% |
| 8 | DISTANCE | NUMBER | NULL | Hierarquia | Distância entre o nó e o ancestral | — | 🟡 70% |
| 9 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 10 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 11 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 12 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 13 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 14 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units]] — via `ORGANIZATION_ID`, `PARENT_ORGANIZATION_ID`, `ANCESTOR_ORGANIZATION_ID`

### Tabelas-filha (FK de saída)
- [[per_org_tree_node_rf]] — via `TREE_NODE_ID` (nó de referência da árvore organizacional)

---

## Uso Típico

### Listar todas as organizações filhas de uma organização
```sql
SELECT cf.ORGANIZATION_ID, cf.DEPTH, cf.DISTANCE
FROM   PER_ORG_TREE_NODE_CF cf
WHERE  cf.ANCESTOR_ORGANIZATION_ID = :p_org_id
  AND  cf.TREE_CODE = :p_tree_code
ORDER BY cf.DEPTH;
```

---

## Observações

- Tabela pré-calculada: dados são gerados por processos batch de árvore organizacional.
- O campo `DEPTH` indica a profundidade absoluta do nó; `DISTANCE` indica a distância relativa ao ancestral consultado.
- Suporta múltiplas versões de árvore via `TREE_STRUCTURE_CODE` e `TREE_CODE`.

---

## Referências

- [Oracle Docs — PER_ORG_TREE_NODE_CF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perorgtreenodecf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
