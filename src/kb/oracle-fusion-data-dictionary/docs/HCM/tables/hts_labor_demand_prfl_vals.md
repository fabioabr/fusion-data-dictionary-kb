---
id: DOC-HCM-287
doc_type: system-doc
title: "HTS_LABOR_DEMAND_PRFL_VALS — Valores de Perfil de Demanda de Mao de Obra"
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
  - valores
aliases:
  - HTS_LABOR_DEMAND_PRFL_VALS
  - hts_labor_demand_prfl_vals
  - hts-labor-demand-prfl-vals
  - labor-demand-prfl-vals
  - valores-perfil-demanda
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_LABOR_DEMAND_PRFL_VALS

## 📌 Visao Geral

Armazena os **valores** (atributos) associados a cada perfil de demanda de mao de obra.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Requisitos:** Definir atributos especificos de cada perfil.
- **Matching:** Comparar requisitos do perfil com habilidades dos colaboradores.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LABOR_DEMAND_PRFL_VAL_ID | NUMBER(18) | NOT NULL | PK | Identificador do valor | — | 🟢 85% |
| 2 | LABOR_DEMAND_PRFL_DEF_ID | NUMBER(18) | NOT NULL | FK | Definicao de perfil | [[hts_labor_demand_prfl_defs]] | 🟢 85% |
| 3 | ATTRIBUTE_NAME | VARCHAR2(240) | NULL | Dados | Nome do atributo | — | 🟡 75% |
| 4 | ATTRIBUTE_VALUE | VARCHAR2(240) | NULL | Dados | Valor do atributo | — | 🟡 75% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hts_labor_demand_prfl_defs]] — via `LABOR_DEMAND_PRFL_DEF_ID` (definicao de perfil do valor de demanda)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Valores de um perfil
```sql
SELECT v.ATTRIBUTE_NAME, v.ATTRIBUTE_VALUE
FROM   HTS_LABOR_DEMAND_PRFL_VALS v
WHERE  v.LABOR_DEMAND_PRFL_DEF_ID = :p_def_id;
```

---

## 🔒 Observacoes

- Estrutura EAV — atributo/valor flexivel por perfil.

---

## 📚 Referencias

- [Oracle Docs — HTS_LABOR_DEMAND_PRFL_VALS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htslabordemandprflvals.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
