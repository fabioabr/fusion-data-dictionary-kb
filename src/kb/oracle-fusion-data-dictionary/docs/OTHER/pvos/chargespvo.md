---
id: DOC-OTHER-PVO-ChargesPVO
doc_type: system-doc
title: "ChargesPVO — PVO Cross-Module"
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
  - ChargesPVO
  - chargespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChargesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Charges. Acessa as tabelas: CML_CHARGES_B, CML_CHARGES_TL.

**Caminho:** `FscmTopModelAM.LandedCostChargeAM.ChargesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 69 | 2 | 2 | 69 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cml_charges_b|CML_CHARGES_B]] — 58 atributos (1 PKs, 58 BICC)
- [[cml_charges_tl|CML_CHARGES_TL]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cml_charges_b|CML_CHARGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargesPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | ChargesPEOAttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | ChargesPEOAttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | ChargesPEOAttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | ChargesPEOAttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | ChargesPEOAttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | ChargesPEOAttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | ChargesPEOAttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | ChargesPEOAttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | ChargesPEOAttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | ChargesPEOAttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | ChargesPEOAttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | ChargesPEOAttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | ChargesPEOAttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | ChargesPEOAttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | ChargesPEOAttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | ChargesPEOAttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | ChargesPEOAttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | ChargesPEOAttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | ChargesPEOAttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | ChargesPEOAttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | ChargesPEOAttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | ChargesPEOAttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | ChargesPEOAttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | ChargesPEOAttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | ChargesPEOAttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | ChargesPEOAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | ChargesPEOAttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | ChargesPEOAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | ChargesPEOAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | ChargesPEOAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | ChargesPEOAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | ChargesPEOAttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | ChargesPEOAttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | ChargesPEOAttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | ChargesPEOAttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | ChargesPEOAttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | ChargesPEOAttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | ChargesPEOAttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | ChargesPEOAttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | ChargesPEOAttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | ChargesPEOAutoTaxCalculation | AUTO_TAX_CALCULATION | — | ✅ |
| 43 | ChargesPEOChargeCode | CHARGE_CODE | — | ✅ |
| 44 | ChargesPEOChargeId | CHARGE_ID | 🔑 | ✅ |
| 45 | ChargesPEOCreatedBy | CREATED_BY | — | ✅ |
| 46 | ChargesPEOCreationDate | CREATION_DATE | — | ✅ |
| 47 | ChargesPEODefaultAccrualOption | DEFAULT_ACCRUAL_OPTION | — | ✅ |
| 48 | ChargesPEODefaultAllocBasisCode | DEFAULT_ALLOC_BASIS_CODE | — | ✅ |
| 49 | ChargesPEODefaultAllocBasisUomCode | DEFAULT_ALLOC_BASIS_UOM_CODE | — | ✅ |
| 50 | ChargesPEOIsSeed | IS_SEED | — | ✅ |
| 51 | ChargesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 52 | ChargesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 53 | ChargesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 54 | ChargesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 55 | ChargesPEOSetId | SET_ID | — | ✅ |
| 56 | ChargesPEOTaxApplicableFlag | TAX_APPLICABLE_FLAG | — | ✅ |
| 57 | ChargesPEOTaxType | TAX_TYPE | — | ✅ |
| 58 | ChargesPEOTrackMissingInvoicesFlag | TRACK_MISSING_INVOICES_FLAG | — | ✅ |

### [[cml_charges_tl|CML_CHARGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChargerTLPEOSourceLang | SOURCE_LANG | — | ✅ |
| 2 | ChargesTLPEOChargeDesc | CHARGE_DESC | — | ✅ |
| 3 | ChargesTLPEOChargeId1 | CHARGE_ID | — | ✅ |
| 4 | ChargesTLPEOCreatedBy1 | CREATED_BY | — | ✅ |
| 5 | ChargesTLPEOCreationDate1 | CREATION_DATE | — | ✅ |
| 6 | ChargesTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 7 | ChargesTLPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 8 | ChargesTLPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | ChargesTLPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 10 | ChargesTLPEOName | NAME | — | ✅ |
| 11 | ChargesTLPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
