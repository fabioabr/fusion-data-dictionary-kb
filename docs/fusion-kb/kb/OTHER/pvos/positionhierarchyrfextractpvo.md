---
id: DOC-OTHER-PVO-PositionHierarchyRFExtractPVO
doc_type: system-doc
title: "PositionHierarchyRFExtractPVO — PVO Cross-Module"
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
  - PositionHierarchyRFExtractPVO
  - positionhierarchyrfextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PositionHierarchyRFExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Position Hierarchy RFExtract. Acessa as tabelas: PER_POSITION_HRCHY_RF.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.PositionBiccExtractAM.PositionHierarchyRFExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 6 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[per_position_hrchy_rf|PER_POSITION_HRCHY_RF]] — 11 atributos (6 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[per_position_hrchy_rf|PER_POSITION_HRCHY_RF]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AncestorPositionId | ANCESTOR_POSITION_ID | 🔑 | ✅ |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | NodeLevel | NODE_LEVEL | 🔑 | ✅ |
| 11 | PositionId | POSITION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
