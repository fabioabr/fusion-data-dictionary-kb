---
id: DOC-HCM-073
doc_type: system-doc
title: "CMP_CWB_PERF_RATINGS — Ratings de Performance no CWB"
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
  - compensation
  - performance-ratings
  - cwb-performance
  - avaliacao
aliases:
  - CMP_CWB_PERF_RATINGS
  - cmp_cwb_perf_ratings
  - performance-ratings-cwb
  - cwb-perf-ratings
  - cmp-cwb-perf-ratings
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# CMP_CWB_PERF_RATINGS

## 📌 Visão Geral

Armazena os **ratings de performance** dos colaboradores utilizados no Compensation Workbench para orientar decisões de compensação. Vincula avaliações de desempenho ao ciclo de compensação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Merit increase:** Ratings orientam percentuais de aumento salarial.
- **Bônus por performance:** Base para cálculo de bônus variavel.
- **Equity:** Distribuição de stock options baseada em performance.
- **Relatórios:** Análise de distribuição de compensação vs. performance.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CWB_PERF_RATING_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟡 80% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | PLAN_ID | NUMBER(18) | NULL | FK | Plano de compensação | — | 🟡 80% |
| 4 | PERFORMANCE_RATING | VARCHAR2(30) | NULL | Avaliação | Rating de performance (1-5, A-E, etc.) | — | 🟡 80% |
| 5 | RATING_LEVEL_ID | NUMBER(18) | NULL | FK | Nível do rating | — | 🟡 70% |
| 6 | REVIEW_PERIOD_ID | NUMBER(18) | NULL | FK | Período de avaliação | — | 🟡 70% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da avaliacao de desempenho CWB)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Ratings por plano de compensação
```sql
SELECT pr.PERSON_ID, pr.PERFORMANCE_RATING
FROM   CMP_CWB_PERF_RATINGS pr
WHERE  pr.PLAN_ID = :p_plan_id
ORDER BY pr.PERFORMANCE_RATING;
```

### Filtros comuns
- `PERFORMANCE_RATING = '5'` — Top performers
- `PLAN_ID = :p_plan_id` — Ratings de um ciclo específico

---

## 🔒 Observações

- Ratings são importados do módulo de Performance Management.
- O rating orienta a matriz de merit increase (rating x compa-ratio).
- Contém dados sensíveis — classificar como `restricted`.

---

## 🔗 PVOs Relacionados

### [[performanceratingpvo|PerformanceRatingPVO]] (HCM · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | PerformanceRatingPEOAssignmentId | ✅ |
| CREATED_BY | PerformanceRatingPEOCreatedBy | ✅ |
| CREATION_DATE | PerformanceRatingPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PerformanceRatingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PerformanceRatingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PerformanceRatingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PerformanceRatingPEOObjectVersionNumber | ✅ |
| PERF_COMMENTS | PerformanceRatingPEOPerfComments | — |
| PERF_DATE | PerformanceRatingPEOPerfDate | ✅ |
| PERF_ORIG_UPDATED_BY | PerformanceRatingPerfOrigUpdatedBy | ✅ |
| PERF_RATING | PerformanceRatingPEOPerfRating | ✅ |
| PERF_RATING_ID | PerfRatingId | ✅ |
| PERF_UPDATE_DATE | PerformanceRatingPEOPerfUpdateDate | ✅ |
| PERF_UPDATED_BY | PerformanceRatingPEOPerfUpdatedBy | ✅ |
| PERSON_ID | PerformanceRatingPEOPersonId | ✅ |

### [[performanceratingpvoviewall|PerformanceRatingPVOViewAll]] (HCM · BICC: 14/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGNMENT_ID | PerformanceRatingPEOAssignmentId | ✅ |
| CREATED_BY | PerformanceRatingPEOCreatedBy | ✅ |
| CREATION_DATE | PerformanceRatingPEOCreationDate | ✅ |
| LAST_UPDATE_DATE | PerformanceRatingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PerformanceRatingPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | PerformanceRatingPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | PerformanceRatingPEOObjectVersionNumber | ✅ |
| PERF_COMMENTS | PerformanceRatingPEOPerfComments | — |
| PERF_DATE | PerformanceRatingPEOPerfDate | ✅ |
| PERF_ORIG_UPDATED_BY | PerformanceRatingPerfOrigUpdatedBy | ✅ |
| PERF_RATING | PerformanceRatingPEOPerfRating | ✅ |
| PERF_RATING_ID | PerfRatingId | ✅ |
| PERF_UPDATE_DATE | PerformanceRatingPEOPerfUpdateDate | ✅ |
| PERF_UPDATED_BY | PerformanceRatingPEOPerfUpdatedBy | ✅ |
| PERSON_ID | PerformanceRatingPEOPersonId | ✅ |

---

## 📚 Referências

- [Oracle Docs — CMP_CWB_PERF_RATINGS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/cmpcwbperfratings.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
