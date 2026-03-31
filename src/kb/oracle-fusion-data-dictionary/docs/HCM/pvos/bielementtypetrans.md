---
id: DOC-HCM-PVO-BIElementTypeTrans
doc_type: system-doc
title: "BIElementTypeTrans — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BIElementTypeTrans
  - bielementtypetrans
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BIElementTypeTrans

## 📌 Visão Geral

Fornece traducoes multilingue dos tipos de elementos de folha. Suporta exibicao localizada de nomes e descricoes de elementos de payroll.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.HcmElementSetupBiccExtractAM.BIElementTypeTrans`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pay_element_types_tl|PAY_ELEMENT_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ElementTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ElementTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ElementTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ElementTypeTranslationPEOElementName | ELEMENT_NAME | — | ✅ |
| 5 | ElementTypeTranslationPEOElementTypeId | ELEMENT_TYPE_ID | 🔑 | ✅ |
| 6 | ElementTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ElementTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | ElementTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ElementTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ElementTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ElementTypeTranslationPEOReportingName | REPORTING_NAME | — | ✅ |
| 12 | ElementTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
