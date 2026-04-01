---
id: DOC-OTHER-PVO-DeductionType
doc_type: system-doc
title: "DeductionType — PVO Cross-Module"
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
  - DeductionType
  - deductiontype
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DeductionType

## 📌 Visão Geral

View Object para extração BICC de dados de Deduction Type. Acessa as tabelas: PAY_DEDUCTION_TYPES, PAY_DEDUCTION_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayDeductionSetupAM.DeductionType`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 2 | 8 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[pay_deduction_types|PAY_DEDUCTION_TYPES]] — 16 atributos (1 PKs, 5 BICC)
- [[pay_deduction_types_tl|PAY_DEDUCTION_TYPES_TL]] — 4 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[pay_deduction_types|PAY_DEDUCTION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeductionTypeBasePEOBaseDeductionTypeId | BASE_DEDUCTION_TYPE_ID | — | — |
| 2 | DeductionTypeBasePEOBaseName | BASE_NAME | — | — |
| 3 | DeductionTypeBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | DeductionTypeBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | DeductionTypeBasePEODeductionCode | DEDUCTION_CODE | — | — |
| 6 | DeductionTypeBasePEODeductionGroupId | DEDUCTION_GROUP_ID | — | — |
| 7 | DeductionTypeBasePEODisplaySequence | DISPLAY_SEQUENCE | — | — |
| 8 | DeductionTypeBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | DeductionTypeBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | DeductionTypeBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | DeductionTypeBasePEOLegislationCode | LEGISLATION_CODE | — | — |
| 12 | DeductionTypeBasePEOLegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 13 | DeductionTypeBasePEOModuleId | MODULE_ID | — | — |
| 14 | DeductionTypeBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | DeductionTypeBasePEOUseAllTaxUnits | USE_ALL_TAX_UNITS | — | — |
| 16 | DeductionTypeId | DEDUCTION_TYPE_ID | 🔑 | ✅ |

### [[pay_deduction_types_tl|PAY_DEDUCTION_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DeductionTypeTranslationPEODeductionTypeId | DEDUCTION_TYPE_ID | — | — |
| 2 | DeductionTypeTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 3 | DeductionTypeTranslationPEOName | NAME | — | ✅ |
| 4 | DeductionTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
