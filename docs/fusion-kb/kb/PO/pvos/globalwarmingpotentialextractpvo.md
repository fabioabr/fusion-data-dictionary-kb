---
id: DOC-PO-PVO-GlobalWarmingPotentialExtractPVO
doc_type: system-doc
title: "GlobalWarmingPotentialExtractPVO — PVO Purchasing"
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
  - GlobalWarmingPotentialExtractPVO
  - globalwarmingpotentialextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GlobalWarmingPotentialExtractPVO

## 📌 Visão Geral

Extrai os potenciais de aquecimento global (GWP) por tipo de gás para cálculos de sustentabilidade. Permite conversão de emissões para CO2-equivalente nas métricas de procurement sustentável.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.GlobalWarmingPotentialExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_gwp|SUS_GWP]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[sus_gwp|SUS_GWP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | EmissionTypeCode | EMISSION_TYPE_CODE | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | GwpFactor | GWP_FACTOR | — | ✅ |
| 7 | GwpId | GWP_ID | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
