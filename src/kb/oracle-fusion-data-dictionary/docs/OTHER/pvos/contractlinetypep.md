---
id: DOC-OTHER-PVO-ContractLineTypeP
doc_type: system-doc
title: "ContractLineTypeP — PVO Cross-Module"
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
  - ContractLineTypeP
  - contractlinetypep
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractLineTypeP

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Line Type P. Acessa as tabelas: OKC_LINE_TYPES_VL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractLineTypeP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[okc_line_types_vl|OKC_LINE_TYPES_VL]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[okc_line_types_vl|OKC_LINE_TYPES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LineTypeCreatedBy | CREATED_BY | — | ✅ |
| 2 | LineTypeCreationDate | CREATION_DATE | — | ✅ |
| 3 | LineTypeDescription | DESCRIPTION | — | ✅ |
| 4 | LineTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LineTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LineTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LineTypeLineTypeId | LINE_TYPE_ID | 🔑 | ✅ |
| 8 | LineTypeName | NAME | — | ✅ |
| 9 | LineTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | LineTypeParentLineTypeId | PARENT_LINE_TYPE_ID | — | ✅ |
| 11 | LineTypeRecursiveYn | RECURSIVE_YN | — | ✅ |
| 12 | LineTypeSourceCode | SOURCE_CODE | — | ✅ |
| 13 | LineTypeSourceCodeClass | SOURCE_CODE_CLASS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
