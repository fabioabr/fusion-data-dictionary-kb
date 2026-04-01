---
id: DOC-OTHER-PVO-HNSInjuredPersonPartsPVO
doc_type: system-doc
title: "HNSInjuredPersonPartsPVO — PVO Cross-Module"
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
  - HNSInjuredPersonPartsPVO
  - hnsinjuredpersonpartspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HNSInjuredPersonPartsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de HNSInjured Person Parts. Acessa as tabelas: HNS_INJURED_PERSON_PARTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HealthandSafetyAM.HNSInjuredPersonPartsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hns_injured_person_parts|HNS_INJURED_PERSON_PARTS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[hns_injured_person_parts|HNS_INJURED_PERSON_PARTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HNSInjuredPersonPartsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | HNSInjuredPersonPartsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | HNSInjuredPersonPartsPEODeletedFlag | DELETED_FLAG | — | ✅ |
| 4 | HNSInjuredPersonPartsPEOInjuredPartCode | INJURED_PART_CODE | — | ✅ |
| 5 | HNSInjuredPersonPartsPEOInjuredPersonId | INJURED_PERSON_ID | — | ✅ |
| 6 | HNSInjuredPersonPartsPEOInjuredPersonPartId | INJURED_PERSON_PART_ID | 🔑 | ✅ |
| 7 | HNSInjuredPersonPartsPEOInjuryNatureCode | INJURY_NATURE_CODE | — | ✅ |
| 8 | HNSInjuredPersonPartsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | HNSInjuredPersonPartsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | HNSInjuredPersonPartsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | HNSInjuredPersonPartsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
