---
id: DOC-OTHER-PVO-RateValuePVO
doc_type: system-doc
title: "RateValuePVO — PVO Cross-Module"
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
  - RateValuePVO
  - ratevaluepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RateValuePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Rate Value. Acessa as tabelas: PER_RATE_VALUES_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GradeAM.RateValuePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 2 | 17 | 89% |

---

## 🔗 Tabelas Relacionadas

- [[per_rate_values_f|PER_RATE_VALUES_F]] — 19 atributos (2 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[per_rate_values_f|PER_RATE_VALUES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | RateValueId | RATE_VALUE_ID | 🔑 | ✅ |
| 4 | RateValuePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 5 | RateValuePEOCreatedBy | CREATED_BY | — | ✅ |
| 6 | RateValuePEOCreationDate | CREATION_DATE | — | ✅ |
| 7 | RateValuePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | RateValuePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | RateValuePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RateValuePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 11 | RateValuePEOMaximum | MAXIMUM | — | ✅ |
| 12 | RateValuePEOMidValue | MID_VALUE | — | ✅ |
| 13 | RateValuePEOMinimum | MINIMUM | — | ✅ |
| 14 | RateValuePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | RateValuePEORateId | RATE_ID | — | ✅ |
| 16 | RateValuePEORateObjectId | RATE_OBJECT_ID | — | ✅ |
| 17 | RateValuePEORateObjectType | RATE_OBJECT_TYPE | — | ✅ |
| 18 | RateValuePEOSequence | SEQUENCE | — | ✅ |
| 19 | RateValuePEOValue | VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
