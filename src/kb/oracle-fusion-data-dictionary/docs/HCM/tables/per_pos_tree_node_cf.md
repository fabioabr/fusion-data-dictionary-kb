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
