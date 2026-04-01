---
id: DOC-OTHER-PVO-PayConsolidationSetsPVO
doc_type: system-doc
title: "PayConsolidationSetsPVO — PVO Cross-Module"
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
  - PayConsolidationSetsPVO
  - payconsolidationsetspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PayConsolidationSetsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Pay Consolidation Sets. Acessa as tabelas: PAY_CONSOLIDATION_SETS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayCoreAM.PayConsolidationSetsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 9 | 90% |

---

## 🔗 Tabelas Relacionadas

- [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]] — 10 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pay_consolidation_sets|PAY_CONSOLIDATION_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PayConsolidationSetPEOComments | COMMENTS | — | — |
| 2 | PayConsolidationSetPEOConsolidationSetId | CONSOLIDATION_SET_ID | 🔑 | ✅ |
| 3 | PayConsolidationSetPEOConsolidationSetName | CONSOLIDATION_SET_NAME | — | ✅ |
| 4 | PayConsolidationSetPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | PayConsolidationSetPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | PayConsolidationSetPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PayConsolidationSetPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PayConsolidationSetPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PayConsolidationSetPEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 10 | PayConsolidationSetPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
