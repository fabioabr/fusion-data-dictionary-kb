---
id: DOC-OTHER-PVO-CeilingTypeExtractPVO
doc_type: system-doc
title: "CeilingTypeExtractPVO — PVO Cross-Module"
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
  - CeilingTypeExtractPVO
  - ceilingtypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CeilingTypeExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Ceiling Type Extract. Acessa as tabelas: FA_CEILING_TYPES.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.CeilingTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 1 | 1 | 12 | 43% |

---

## 🔗 Tabelas Relacionadas

- [[fa_ceiling_types|FA_CEILING_TYPES]] — 28 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[fa_ceiling_types|FA_CEILING_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CeilingTypeAttribute1 | ATTRIBUTE1 | — | — |
| 2 | CeilingTypeAttribute10 | ATTRIBUTE10 | — | — |
| 3 | CeilingTypeAttribute11 | ATTRIBUTE11 | — | — |
| 4 | CeilingTypeAttribute12 | ATTRIBUTE12 | — | — |
| 5 | CeilingTypeAttribute13 | ATTRIBUTE13 | — | — |
| 6 | CeilingTypeAttribute14 | ATTRIBUTE14 | — | — |
| 7 | CeilingTypeAttribute15 | ATTRIBUTE15 | — | — |
| 8 | CeilingTypeAttribute2 | ATTRIBUTE2 | — | — |
| 9 | CeilingTypeAttribute3 | ATTRIBUTE3 | — | — |
| 10 | CeilingTypeAttribute4 | ATTRIBUTE4 | — | — |
| 11 | CeilingTypeAttribute5 | ATTRIBUTE5 | — | — |
| 12 | CeilingTypeAttribute6 | ATTRIBUTE6 | — | — |
| 13 | CeilingTypeAttribute7 | ATTRIBUTE7 | — | — |
| 14 | CeilingTypeAttribute8 | ATTRIBUTE8 | — | — |
| 15 | CeilingTypeAttribute9 | ATTRIBUTE9 | — | — |
| 16 | CeilingTypeAttributeCategoryCode | ATTRIBUTE_CATEGORY_CODE | — | — |
| 17 | CeilingTypeCeilingName | CEILING_NAME | — | ✅ |
| 18 | CeilingTypeCeilingType1 | CEILING_TYPE | — | ✅ |
| 19 | CeilingTypeCeilingTypeId | CEILING_TYPE_ID | 🔑 | ✅ |
| 20 | CeilingTypeCreatedBy | CREATED_BY | — | ✅ |
| 21 | CeilingTypeCreationDate | CREATION_DATE | — | ✅ |
| 22 | CeilingTypeCurrencyCode | CURRENCY_CODE | — | ✅ |
| 23 | CeilingTypeDescription | DESCRIPTION | — | ✅ |
| 24 | CeilingTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | CeilingTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | CeilingTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | CeilingTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 28 | CeilingTypeSetId | SET_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
