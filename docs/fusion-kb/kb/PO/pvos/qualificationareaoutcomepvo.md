---
id: DOC-PO-PVO-QualificationAreaOutcomePVO
doc_type: system-doc
title: "QualificationAreaOutcomePVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QualificationAreaOutcomePVO
  - qualificationareaoutcomepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualificationAreaOutcomePVO

## 📌 Visão Geral

Extrai os resultados por área de qualificação, indicando o desempenho do fornecedor em cada dimensão avaliada. Suporta decisões de homologação baseadas em análise multidimensional.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.QualificationAreaOutcomePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qual_area_outcomes|POQ_QUAL_AREA_OUTCOMES]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[poq_qual_area_outcomes|POQ_QUAL_AREA_OUTCOMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualAreaOutcomeActiveFlag | ACTIVE_FLAG | — | ✅ |
| 2 | QualAreaOutcomeCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualAreaOutcomeCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualAreaOutcomeDisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 5 | QualAreaOutcomeFromScore | FROM_SCORE | — | ✅ |
| 6 | QualAreaOutcomeId | QUAL_AREA_OUTCOME_ID | 🔑 | ✅ |
| 7 | QualAreaOutcomeKnockoutOutcomeFlag | KNOCKOUT_OUTCOME_FLAG | — | ✅ |
| 8 | QualAreaOutcomeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QualAreaOutcomeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QualAreaOutcomeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QualAreaOutcomeNotificationFlag | NOTIFICATION_FLAG | — | ✅ |
| 12 | QualAreaOutcomeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QualAreaOutcomeOutcomeName | OUTCOME_NAME | — | ✅ |
| 14 | QualAreaOutcomeQualAreaId | QUAL_AREA_ID | — | ✅ |
| 15 | QualAreaOutcomeToScore | TO_SCORE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
