---
id: DOC-HCM-288
doc_type: system-doc
title: "HTS_LABOR_DEMAND_VIEW — Demanda de Mao de Obra (View)"
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
  - view
aliases:
  - HTS_LABOR_DEMAND_VIEW
  - hts_labor_demand_view
  - hts-labor-demand-view
  - labor-demand-view
  - demanda-mao-obra-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_LABOR_DEMAND_VIEW

## 📌 Visao Geral

View que consolida dados de **demanda de mao de obra** para scheduling e workforce planning.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Scheduling:** Visualizar demandas de staffing.
- **Workforce Planning:** Planejar alocacao de recursos.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LABOR_DEMAND_ID | NUMBER(18) | NOT NULL | PK | Identificador da demanda | — | 🟡 80% |
| 2 | DEMAND_DATE | DATE | NULL | Data | Data da demanda | — | 🟡 80% |
| 3 | DEPARTMENT_ID | NUMBER(18) | NULL | FK | Departamento | [[hr_all_organization_units_f]] | 🟡 80% |
| 4 | POSITION_ID | NUMBER(18) | NULL | FK | Posicao | [[hr_all_positions_f]] | 🟡 75% |
| 5 | REQUIRED_COUNT | NUMBER | NULL | Dados | Quantidade requerida | — | 🟡 75% |
| 6 | FILLED_COUNT | NUMBER | NULL | Dados | Quantidade preenchida | — | 🟡 70% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status da demanda | — | 🟡 70% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data de criacao | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hr_all_organization_units_f]] — via `DEPARTMENT_ID` (departamento da demanda de mao de obra)
- [[hr_all_positions_f]] — via `POSITION_ID` (posicao da demanda de mao de obra)

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Demandas pendentes
```sql
SELECT ld.DEMAND_DATE, ld.DEPARTMENT_ID,
       ld.REQUIRED_COUNT, ld.FILLED_COUNT
FROM   HTS_LABOR_DEMAND_VIEW ld
WHERE  ld.REQUIRED_COUNT > NVL(ld.FILLED_COUNT, 0);
```

---

## 🔒 Observacoes

- View somente leitura.
- Consolida dados de multiplas tabelas de scheduling.

---

## 📚 Referencias

- [Oracle Docs — HTS_LABOR_DEMAND_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htslabordemandview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[labordemandpvo|LaborDemandPVO]] (HCM · BICC: 3/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DEMAND_DATE | DemandDate | ✅ |
| RESOURCES_REQUIRED | ResourcesRequired | ✅ |
| SCHEDULER_PROFILE_ID | SchedulerProfileId | ✅ |
