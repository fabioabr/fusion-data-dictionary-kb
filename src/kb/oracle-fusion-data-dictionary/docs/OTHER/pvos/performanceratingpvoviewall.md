---
id: DOC-OTHER-PVO-PerformanceRatingPVOViewAll
doc_type: system-doc
title: "PerformanceRatingPVOViewAll — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - PerformanceRatingPVOViewAll
  - performanceratingpvoviewall
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PerformanceRatingPVOViewAll

## 📌 Visão Geral

View Object para extração BICC de dados de Performance Rating View All. Acessa as tabelas: CMP_CWB_PERF_RATINGS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.CompensationAM.PerformanceRatingPVOViewAll`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 14 | 93% |

---

## 🔗 Tabelas Relacionadas

- [[cmp_cwb_perf_ratings|CMP_CWB_PERF_RATINGS]] — 15 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cmp_cwb_perf_ratings|CMP_CWB_PERF_RATINGS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerfRatingId | PERF_RATING_ID | 🔑 | ✅ |
| 2 | PerformanceRatingPEOAssignmentId | ASSIGNMENT_ID | — | ✅ |
| 3 | PerformanceRatingPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | PerformanceRatingPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | PerformanceRatingPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PerformanceRatingPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PerformanceRatingPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PerformanceRatingPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PerformanceRatingPEOPerfComments | PERF_COMMENTS | — | — |
| 10 | PerformanceRatingPEOPerfDate | PERF_DATE | — | ✅ |
| 11 | PerformanceRatingPEOPerfRating | PERF_RATING | — | ✅ |
| 12 | PerformanceRatingPEOPerfUpdateDate | PERF_UPDATE_DATE | — | ✅ |
| 13 | PerformanceRatingPEOPerfUpdatedBy | PERF_UPDATED_BY | — | ✅ |
| 14 | PerformanceRatingPEOPersonId | PERSON_ID | — | ✅ |
| 15 | PerformanceRatingPerfOrigUpdatedBy | PERF_ORIG_UPDATED_BY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
