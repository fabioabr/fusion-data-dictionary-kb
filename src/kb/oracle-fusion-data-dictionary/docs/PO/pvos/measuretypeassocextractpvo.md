---
id: DOC-PO-PVO-MeasureTypeAssocExtractPVO
doc_type: system-doc
title: "MeasureTypeAssocExtractPVO — PVO Purchasing"
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
  - MeasureTypeAssocExtractPVO
  - measuretypeassocextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeasureTypeAssocExtractPVO

## 📌 Visão Geral

Extrai as associações entre tipos de medida e atividades de sustentabilidade, definindo unidades de mensuração (kg, km, kWh). Suporta padronização de métricas ambientais na cadeia de compras.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.MeasureTypeAssocExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_measure_type_assocs|SUS_MEASURE_TYPE_ASSOCS]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[sus_measure_type_assocs|SUS_MEASURE_TYPE_ASSOCS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | MeasureTypeAssocId | MEASURE_TYPE_ASSOCS_ID | 🔑 | ✅ |
| 8 | MeasureTypeCode | MEASURE_TYPE_CODE | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
