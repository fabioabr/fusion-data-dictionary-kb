---
id: DOC-HCM-286
doc_type: system-doc
title: "HTS_LABOR_DEMAND_PRFL_DEFSETS — Conjuntos de Definicoes de Perfil de Demanda"
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
  - labor-demand
  - scheduling
  - conjuntos
aliases:
  - HTS_LABOR_DEMAND_PRFL_DEFSETS
  - hts_labor_demand_prfl_defsets
  - hts-labor-demand-prfl-defsets
  - labor-demand-prfl-defsets
  - conjuntos-definicoes-demanda
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_LABOR_DEMAND_PRFL_DEFSETS

## 📌 Visao Geral

Armazena os **conjuntos de definicoes** que agrupam perfis de demanda de mao de obra.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Agrupamento:** Organizar perfis de demanda em conjuntos reutilizaveis.
- **Scheduling:** Associar conjuntos de perfis a demandas.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LABOR_DEMAND_PRFL_DEFSET_ID | NUMBER(18) | NOT NULL | PK | Identificador do conjunto | — | 🟢 85% |
| 2 | DEFSET_NAME | VARCHAR2(240) | NULL | Dados | Nome do conjunto | — | 🟡 80% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao | — | 🟡 75% |
| 4 | LABOR_DEMAND_PRFL_DEF_ID | NUMBER(18) | NULL | FK | Definicao de perfil | [[hts_labor_demand_prfl_defs]] | 🟡 80% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hts_labor_demand_prfl_defs]] — via `LABOR_DEMAND_PRFL_DEF_ID` (definicao de perfil do conjunto de demanda)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Conjuntos de definicao
```sql
SELECT ds.DEFSET_NAME, ds.LABOR_DEMAND_PRFL_DEF_ID
FROM   HTS_LABOR_DEMAND_PRFL_DEFSETS ds;
```

---

## 🔒 Observacoes

- Tabela de agrupamento de perfis de demanda.

---

## 📚 Referencias

- [Oracle Docs — HTS_LABOR_DEMAND_PRFL_DEFSETS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htslabordemandprfldefsets.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
