---
id: DOC-PO-PVO-PositionLegislativePVO
doc_type: system-doc
title: "PositionLegislativePVO — PVO Purchasing"
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
  - PositionLegislativePVO
  - positionlegislativepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PositionLegislativePVO

## 📌 Visão Geral

Extrai dados legislativos de posições organizacionais, incluindo enquadramento legal e regulatório. Suporta compliance trabalhista e análise de obrigações regulatórias associadas a cada cargo.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PositionAM.PositionLegislativePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 2 | 10 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[per_position_leg_f|PER_POSITION_LEG_F]] — 14 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[per_position_leg_f|PER_POSITION_LEG_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PositionLegId | POSITION_LEG_ID | 🔑 | ✅ |
| 4 | PositionLegislativePEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | — |
| 5 | PositionLegislativePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 6 | PositionLegislativePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PositionLegislativePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PositionLegislativePEOInformationCategory | INFORMATION_CATEGORY | — | — |
| 9 | PositionLegislativePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PositionLegislativePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | PositionLegislativePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | PositionLegislativePEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 13 | PositionLegislativePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | PositionLegislativePEOPositionId | POSITION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
