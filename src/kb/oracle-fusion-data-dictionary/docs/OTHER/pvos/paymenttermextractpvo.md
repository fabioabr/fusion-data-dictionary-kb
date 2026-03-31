---
id: DOC-OTHER-PVO-PaymentTermExtractPVO
doc_type: system-doc
title: "PaymentTermExtractPVO — PVO Cross-Module"
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
  - PaymentTermExtractPVO
  - paymenttermextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Term Extract. Acessa as tabelas: RA_TERMS_B, RA_TERMS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.PaymentTermExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 54 | 2 | 1 | 38 | 70% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_b|RA_TERMS_B]] — 41 atributos (1 PKs, 25 BICC)
- [[ra_terms_tl|RA_TERMS_TL]] — 13 atributos (13 BICC)

---

## ⚙️ Atributos

### [[ra_terms_b|RA_TERMS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermBAttribute1 | ATTRIBUTE1 | — | — |
| 2 | RaTermBAttribute10 | ATTRIBUTE10 | — | — |
| 3 | RaTermBAttribute11 | ATTRIBUTE11 | — | — |
| 4 | RaTermBAttribute12 | ATTRIBUTE12 | — | — |
| 5 | RaTermBAttribute13 | ATTRIBUTE13 | — | — |
| 6 | RaTermBAttribute14 | ATTRIBUTE14 | — | — |
| 7 | RaTermBAttribute15 | ATTRIBUTE15 | — | — |
| 8 | RaTermBAttribute2 | ATTRIBUTE2 | — | — |
| 9 | RaTermBAttribute3 | ATTRIBUTE3 | — | — |
| 10 | RaTermBAttribute4 | ATTRIBUTE4 | — | — |
| 11 | RaTermBAttribute5 | ATTRIBUTE5 | — | — |
| 12 | RaTermBAttribute6 | ATTRIBUTE6 | — | — |
| 13 | RaTermBAttribute7 | ATTRIBUTE7 | — | — |
| 14 | RaTermBAttribute8 | ATTRIBUTE8 | — | — |
| 15 | RaTermBAttribute9 | ATTRIBUTE9 | — | — |
| 16 | RaTermBAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | RaTermBBaseAmount | BASE_AMOUNT | — | ✅ |
| 18 | RaTermBBillingCycleId | BILLING_CYCLE_ID | — | ✅ |
| 19 | RaTermBCalcDiscountOnLinesFlag | CALC_DISCOUNT_ON_LINES_FLAG | — | ✅ |
| 20 | RaTermBCreatedBy | CREATED_BY | — | ✅ |
| 21 | RaTermBCreationDate | CREATION_DATE | — | ✅ |
| 22 | RaTermBCreditCheckFlag | CREDIT_CHECK_FLAG | — | ✅ |
| 23 | RaTermBDescription | DESCRIPTION | — | ✅ |
| 24 | RaTermBDiscountBasisDateType | DISCOUNT_BASIS_DATE_TYPE | — | ✅ |
| 25 | RaTermBDueCutoffDay | DUE_CUTOFF_DAY | — | ✅ |
| 26 | RaTermBEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 27 | RaTermBFirstInstallmentCode | FIRST_INSTALLMENT_CODE | — | ✅ |
| 28 | RaTermBInUse | IN_USE | — | ✅ |
| 29 | RaTermBLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | RaTermBLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | RaTermBLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | RaTermBModuleId | MODULE_ID | — | ✅ |
| 33 | RaTermBName | NAME | — | ✅ |
| 34 | RaTermBObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 35 | RaTermBPartialDiscountFlag | PARTIAL_DISCOUNT_FLAG | — | ✅ |
| 36 | RaTermBPrepaymentFlag | PREPAYMENT_FLAG | — | ✅ |
| 37 | RaTermBPrintingLeadDays | PRINTING_LEAD_DAYS | — | ✅ |
| 38 | RaTermBSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 39 | RaTermBSetId | SET_ID | — | ✅ |
| 40 | RaTermBStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 41 | RaTermBTermId | TERM_ID | 🔑 | ✅ |

### [[ra_terms_tl|RA_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | RaTermTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | RaTermTLDescription | DESCRIPTION | — | ✅ |
| 4 | RaTermTLLanguage | LANGUAGE | — | ✅ |
| 5 | RaTermTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RaTermTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RaTermTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RaTermTLName | NAME | — | ✅ |
| 9 | RaTermTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RaTermTLSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | RaTermTLSetId | SET_ID | — | ✅ |
| 12 | RaTermTLSourceLang | SOURCE_LANG | — | ✅ |
| 13 | RaTermTLTermId | TERM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
