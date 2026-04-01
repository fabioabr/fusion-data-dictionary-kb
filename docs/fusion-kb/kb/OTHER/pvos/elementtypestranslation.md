---
id: DOC-OTHER-PVO-ElementTypesTranslation
doc_type: system-doc
title: "ElementTypesTranslation — PVO Cross-Module"
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
  - ElementTypesTranslation
  - elementtypestranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ElementTypesTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Element Types Translation. Acessa as tabelas: PAY_ELEMENT_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmElementSetupAM.ElementTypesTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 3 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementTypeId | ELEMENT_TYPE_ID | 🔑 | ✅ |
| 2 | ElementTypeTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ElementTypeTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ElementTypeTranslationDescription | DESCRIPTION | — | — |
| 5 | ElementTypeTranslationElementName | ELEMENT_NAME | — | — |
| 6 | ElementTypeTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ElementTypeTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ElementTypeTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ElementTypeTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ElementTypeTranslationReportingName | REPORTING_NAME | — | — |
| 11 | ElementTypeTranslationSourceLang | SOURCE_LANG | — | — |
| 12 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
