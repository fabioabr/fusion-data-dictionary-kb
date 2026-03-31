---
id: DOC-HCM-698
doc_type: system-doc
title: "PER_POSITION_HRCHY_RF — Hierarquia de Posições (Reference/Flat)"
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
  - hierarquia-posicoes
  - position-hierarchy-rf
  - reference-flat
aliases:
  - PER_POSITION_HRCHY_RF
  - per_position_hrchy_rf
  - hierarquia-posicoes-rf
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POSITION_HRCHY_RF

## Visão Geral

Armazena dados de **referência achatados** (flattened) da hierarquia de posições. Contém relações pré-calculadas entre posições para consultas rápidas, eliminando a necessidade de recursão na árvore hierárquica.

> [!note] Sufixo _RF
> O sufixo `_RF` indica tabela **Reference/Flat** — dados de referência desnormalizados para performance.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consultas rápidas de hierarquia** — acessar relações posição-pai sem recursão
- **Relatórios OTBI** — fonte otimizada para análises hierárquicas de posições
- **Segurança baseada em posição** — controlar acesso por hierarquia de cargos
- **Análise de span of control** — métricas por nível na árvore de posições

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POS_HRCHY_NODE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do nó | — | 🟡 75% |
| 2 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Posição do nó | HR_ALL_POSITIONS_F | 🟢 85% |
| 3 | ANCESTOR_POSITION_ID | NUMBER(18) | NULL | FK | Posição ancestral | HR_ALL_POSITIONS_F | 🟡 75% |
| 4 | POSITION_HIERARCHY_ID | NUMBER(18) | NOT NULL | FK | Identificador da hierarquia | — | 🟡 75% |
| 5 | DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó | — | 🟡 70% |
| 6 | DISTANCE | NUMBER | NULL | Hierarquia | Distância ao ancestral | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 8 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID` e `ANCESTOR_POSITION_ID` (posição no nó da hierarquia)
- [[per_position_hierarchy_f]] — via `POSITION_HIERARCHY_ID` (hierarquia à qual o nó de posição pertence)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Todas as posições abaixo de uma posição ancestral
```sql
SELECT rf.POSITION_ID, rf.DEPTH, rf.DISTANCE
FROM   PER_POSITION_HRCHY_RF rf
WHERE  rf.ANCESTOR_POSITION_ID = :p_position_id
  AND  rf.POSITION_HIERARCHY_ID = :p_hierarchy_id
ORDER BY rf.DEPTH;
```

---

## Observações

- Tabela pré-calculada: atualizada por processos batch.
- `DISTANCE` = 1 indica subordinado direto; valores maiores indicam níveis mais abaixo.
- Ideal para relatórios onde performance é prioridade.

---

## Referências

- [Oracle Docs — PER_POSITION_HRCHY_RF](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perpositionhrhyrf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
