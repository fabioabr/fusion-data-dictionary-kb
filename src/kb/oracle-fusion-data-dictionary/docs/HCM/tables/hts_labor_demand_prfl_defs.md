---
id: DOC-HCM-285
doc_type: system-doc
title: "HTS_LABOR_DEMAND_PRFL_DEFS — Definicoes de Perfil de Demanda de Mao de Obra"
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
  - workforce
aliases:
  - HTS_LABOR_DEMAND_PRFL_DEFS
  - hts_labor_demand_prfl_defs
  - hts-labor-demand-prfl-defs
  - labor-demand-prfl-defs
  - definicoes-perfil-demanda
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_LABOR_DEMAND_PRFL_DEFS

## 📌 Visao Geral

Armazena as **definicoes de perfil de demanda de mao de obra** para o modulo de scheduling/workforce management.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Workforce Planning:** Definir requisitos de perfil para demandas.
- **Scheduling:** Associar perfis a shifts e schedules.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LABOR_DEMAND_PRFL_DEF_ID | NUMBER(18) | NOT NULL | PK | Identificador da definicao | — | 🟢 85% |
| 2 | PROFILE_NAME | VARCHAR2(240) | NULL | Dados | Nome do perfil | — | 🟡 80% |
| 3 | DESCRIPTION | VARCHAR2(2000) | NULL | Dados | Descricao | — | 🟡 75% |
| 4 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status (ACTIVE, INACTIVE) | — | 🟡 75% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versao otimista | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo usuario que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data da ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- [[hts_labor_demand_prfl_vals]] — via `LABOR_DEMAND_PRFL_DEF_ID` (valores da definicao de perfil de demanda)

---

## 📎 Uso Tipico

### Definicoes ativas
```sql
SELECT ld.LABOR_DEMAND_PRFL_DEF_ID, ld.PROFILE_NAME
FROM   HTS_LABOR_DEMAND_PRFL_DEFS ld
WHERE  ld.STATUS = 'ACTIVE';
```

---

## 🔒 Observacoes

- Modulo Time and Labor / Workforce Scheduling.
- Perfis definem combinacoes de requisitos para staffing.

---

## 📚 Referencias

- [Oracle Docs — HTS_LABOR_DEMAND_PRFL_DEFS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htslabordemandprfldefs.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
