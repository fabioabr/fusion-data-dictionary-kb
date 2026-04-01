---
id: DOC-PO-PVO-EmissionTypeAssocExtractPVO
doc_type: system-doc
title: "EmissionTypeAssocExtractPVO — PVO Purchasing"
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
  - EmissionTypeAssocExtractPVO
  - emissiontypeassocextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EmissionTypeAssocExtractPVO

## 📌 Visão Geral

Extrai as associações entre tipos de emissão (CO2, CH4, N2O) e atividades de procurement. Define quais gases de efeito estufa são rastreados para cada tipo de atividade de compras.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.EmissionTypeAssocExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_emission_type_assocs|SUS_EMISSION_TYPE_ASSOCS]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[sus_emission_type_assocs|SUS_EMISSION_TYPE_ASSOCS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EmissionTypeAssocId | EMISSION_TYPE_ASSOC_ID | 🔑 | ✅ |
| 5 | EmissionTypeCode | EMISSION_TYPE_CODE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
