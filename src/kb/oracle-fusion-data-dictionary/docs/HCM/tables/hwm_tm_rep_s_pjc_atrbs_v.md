---
id: DOC-HCM-402
doc_type: system-doc
title: "HWM_TM_REP_S_PJC_ATRBS_V — View de Atributos Custeio de Projetos (PJC) de Sumario Reportado"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-management
  - reported-summary-attributes
  - sumario-pjc
  - view
aliases:
  - HWM_TM_REP_S_PJC_ATRBS_V
  - hwm_tm_rep_s_pjc_atrbs_v
  - hwm-tm-rep-s-pjc-atrbs-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_REP_S_PJC_ATRBS_V

## 📌 Visao Geral

View que consolida os **atributos de custeio de projetos (pjc)** no nivel de sumario das entradas reportadas de tempo. Foco em atributos de Project Costing (PJC) no sumario reportado.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta sumarizada:** atributos de custeio de projetos (pjc) consolidados por sumario.
- **Relatorios gerenciais:** visao agregada de atributos reportados.
- **Integracao:** fonte para sistemas consumidores de dados sumarizados.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REP_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada reportada | — | 🟡 65% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 65% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 60% |
| 4 | ENTRY_DATE | DATE | NULL | Periodo | Data da entrada | — | 🟡 65% |
| 5 | SUMMARY_MEASURE | NUMBER | NULL | Dados | Medida sumarizada | — | 🟡 55% |
| 6 | ATTRIBUTE_1 | VARCHAR2(240) | NULL | Dados | Atributo especifico 1 | — | 🟡 55% |
| 7 | ATTRIBUTE_2 | VARCHAR2(240) | NULL | Dados | Atributo especifico 2 | — | 🟡 55% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa dos atributos de projeto no tempo)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Consultar atributos de sumario custeio de projetos (pjc)
```sql
SELECT v.PERSON_ID, v.ENTRY_DATE, v.SUMMARY_MEASURE,
       v.ATTRIBUTE_1, v.STATUS
FROM   HWM_TM_REP_S_PJC_ATRBS_V v
WHERE  v.PERSON_ID = :p_person_id;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `ENTRY_DATE BETWEEN :dt_ini AND :dt_fim — Periodo`

---

## 🔒 Observacoes

- View somente leitura — nao suporta DML.
- Especifica para atributos de custeio de projetos (pjc) no nivel de sumario.
- Nomes de colunas podem variar; validar no ambiente.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_REP_S_PJC_ATRBS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrepspjcatrbsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[historicprocessedtimeentrypvo|HistoricProcessedTimeEntryPVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | PjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | PjcBillableFlag | ✅ |
| PJC_PROJECT_ID | PjcProjectId | ✅ |
| PJC_PROJECT_UNIT | PjcProjectUnit | ✅ |
| PJC_TASK_ID | PjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | PjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | PjcWorkType | ✅ |

### [[historicreportedtimeentrypvo|HistoricReportedTimeEntryPVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | PjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | PjcBillableFlag | ✅ |
| PJC_PROJECT_ID | PjcProjectId | ✅ |
| PJC_PROJECT_UNIT | PjcProjectUnit | ✅ |
| PJC_TASK_ID | PjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | PjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | PjcWorkType | ✅ |

### [[historicrptabstimeentrypvo|HistoricRptAbsTimeEntryPVO]] (HCM · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | SimpleProjectsAttributePEOPjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | SimpleProjectsAttributePEOPjcBillableFlag | ✅ |
| PJC_CAPITALIZABLE_FLAG | SimpleProjectsAttributePEOPjcCapitalizableFlag | ✅ |
| PJC_CONTRACT_ID | SimpleProjectsAttributePEOPjcContractId | ✅ |
| PJC_EXP_ORGANIZATION_ID | SimpleProjectsAttributePEOPjcExpOrganizationId | ✅ |
| PJC_FUNDING_SOURCE_ID | SimpleProjectsAttributePEOPjcFundingSourceId | ✅ |
| PJC_PROJECT_ID | SimpleProjectsAttributePEOPjcProjectId | ✅ |
| PJC_PROJECT_UNIT | SimpleProjectsAttributePEOPjcProjectUnit | ✅ |
| PJC_TASK_ID | SimpleProjectsAttributePEOPjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | SimpleProjectsAttributePEOPjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | SimpleProjectsAttributePEOPjcWorkType | ✅ |

### [[processedtimeentrypvo|ProcessedTimeEntryPVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | PjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | PjcBillableFlag | ✅ |
| PJC_PROJECT_ID | PjcProjectId | ✅ |
| PJC_PROJECT_UNIT | PjcProjectUnit | ✅ |
| PJC_TASK_ID | PjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | PjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | PjcWorkType | ✅ |

### [[reportedtimeentrypvo|ReportedTimeEntryPVO]] (HCM · BICC: 5/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | PjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | PjcBillableFlag | ✅ |
| PJC_PROJECT_ID | PjcProjectId | ✅ |
| PJC_PROJECT_UNIT | PjcProjectUnit | ✅ |
| PJC_TASK_ID | PjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | PjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | PjcWorkType | ✅ |

### [[rptabstimeentrypvo|RptAbsTimeEntryPVO]] (HCM · BICC: 9/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PJC_ATTRIBUTE_CATEGORY | SimpleProjectsAttributePEOPjcAttributeCategory | — |
| PJC_BILLABLE_FLAG | SimpleProjectsAttributePEOPjcBillableFlag | ✅ |
| PJC_CAPITALIZABLE_FLAG | SimpleProjectsAttributePEOPjcCapitalizableFlag | ✅ |
| PJC_CONTRACT_ID | SimpleProjectsAttributePEOPjcContractId | ✅ |
| PJC_EXP_ORGANIZATION_ID | SimpleProjectsAttributePEOPjcExpOrganizationId | ✅ |
| PJC_FUNDING_SOURCE_ID | SimpleProjectsAttributePEOPjcFundingSourceId | ✅ |
| PJC_PROJECT_ID | SimpleProjectsAttributePEOPjcProjectId | ✅ |
| PJC_PROJECT_UNIT | SimpleProjectsAttributePEOPjcProjectUnit | ✅ |
| PJC_TASK_ID | SimpleProjectsAttributePEOPjcTaskId | ✅ |
| PJC_TIME_REPOS_ATRB_ID | SimpleProjectsAttributePEOPjcTimeRepositoryAttributeId | — |
| PJC_WORK_TYPE | SimpleProjectsAttributePEOPjcWorkType | ✅ |
