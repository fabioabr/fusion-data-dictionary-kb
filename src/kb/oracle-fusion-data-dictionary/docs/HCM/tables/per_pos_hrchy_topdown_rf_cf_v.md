---
id: DOC-HCM-701
doc_type: system-doc
title: "PER_POS_HRCHY_TOPDOWN_RF_CF_V — View Top-Down de Hierarquia de Posições"
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
  - position-hierarchy-topdown
  - view
  - organograma
aliases:
  - PER_POS_HRCHY_TOPDOWN_RF_CF_V
  - per_pos_hrchy_topdown_rf_cf_v
  - view-hierarquia-posicoes-topdown
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_POS_HRCHY_TOPDOWN_RF_CF_V

## Visão Geral

**View** que apresenta a hierarquia de posições em ordem **top-down** (do topo para a base), combinando dados de referência (RF) e calculados (CF). Permite navegar a árvore de posições de cima para baixo de forma otimizada.

> [!note] Sufixo _V
> O sufixo `_V` indica **View** — consulta pré-definida que combina dados de referência e calculados.

---

## Propósito de Negócio

Esta view é utilizada nos seguintes processos:

- **Navegação top-down no organograma** — listar posições do topo para a base
- **Relatórios de estrutura organizacional** — visualizar cadeia completa de posições
- **Análise de span of control** — medir amplitude por nível
- **Dashboards executivos** — exibir organograma por posições

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | POSITION_ID | NUMBER(18) | NOT NULL | FK | Posição do nó | HR_ALL_POSITIONS_F | 🟡 80% |
| 2 | PARENT_POSITION_ID | NUMBER(18) | NULL | FK | Posição pai | HR_ALL_POSITIONS_F | 🟡 80% |
| 3 | TOP_POSITION_ID | NUMBER(18) | NULL | FK | Posição do topo da hierarquia | HR_ALL_POSITIONS_F | 🟡 70% |
| 4 | POSITION_HIERARCHY_ID | NUMBER(18) | NOT NULL | FK | Identificador da hierarquia | — | 🟡 75% |
| 5 | DEPTH | NUMBER | NULL | Hierarquia | Profundidade do nó na árvore | — | 🟡 75% |
| 6 | DISTANCE | NUMBER | NULL | Hierarquia | Distância ao nó de referência | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 75% |
| 8 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 75% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_positions_f]] — via `POSITION_ID`, `PARENT_POSITION_ID`
- [[per_position_hierarchy_f]] — via `POSITION_HIERARCHY_ID` (hierarquia de posições na visão top-down)

### Tabelas-filha (FK de saída)
- Nenhuma — views não possuem FKs diretas.

---

## Uso Típico

### Árvore completa a partir do topo
```sql
SELECT v.POSITION_ID, v.PARENT_POSITION_ID, v.DEPTH
FROM   PER_POS_HRCHY_TOPDOWN_RF_CF_V v
WHERE  v.POSITION_HIERARCHY_ID = :p_hierarchy_id
  AND  SYSDATE BETWEEN v.EFFECTIVE_START_DATE AND v.EFFECTIVE_END_DATE
ORDER BY v.DEPTH, v.POSITION_ID;
```

---

## Observações

- Por ser uma view, não aceita DML direto.
- Combina dados de referência (RF) e calculados (CF) para máxima performance.
- Ideal para construir organogramas visuais top-down.
- Pode conter grande volume de dados em organizações grandes — usar filtros.

---

## Referências

- [Oracle Docs — PER_POS_HRCHY_TOPDOWN_RF_CF_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perposhrhytopdownrfcfv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
