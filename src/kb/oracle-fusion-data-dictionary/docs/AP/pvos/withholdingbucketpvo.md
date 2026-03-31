---
id: DOC-AP-PVO-WithholdingBucketPVO
doc_type: system-doc
title: "WithholdingBucketPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - WithholdingBucketPVO
  - withholdingbucketpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WithholdingBucketPVO

## 📌 Visão Geral

Extrai os buckets de retenção de impostos na fonte (withholding tax), incluindo regime fiscal, tipo de imposto, perfil tributário e unidade de negócio. Essencial para controle de retenções fiscais obrigatórias sobre pagamentos a fornecedores.

**Caminho:** `FscmTopModelAM.FinApShrdSetupWithTaxesAM.WithholdingBucketPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 5 | 1 | 10 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[fun_bu_perf_v|FUN_BU_PERF_V]] — 1 atributos
- [[zx_buckets_f|ZX_BUCKETS_F]] — 22 atributos (1 PKs, 9 BICC)
- [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]] — 3 atributos
- [[zx_taxes_b|ZX_TAXES_B]] — 1 atributos
- [[zx_taxes_tl|ZX_TAXES_TL]] — 3 atributos (1 BICC)

---

## ⚙️ Atributos

### [[fun_bu_perf_v|FUN_BU_PERF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessUnitBusinessUnitId | BU_ID | — | — |

### [[zx_buckets_f|ZX_BUCKETS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingBucketAccumulatedTaxAmount | ACCUMULATED_TAX_AMOUNT | — | ✅ |
| 2 | WithholdingBucketAccumulatedTaxableAmount | ACCUMULATED_TAXABLE_AMOUNT | — | ✅ |
| 3 | WithholdingBucketBucketType | BUCKET_TYPE | — | — |
| 4 | WithholdingBucketCalendarName | CALENDAR_NAME | — | — |
| 5 | WithholdingBucketCreatedBy | CREATED_BY | — | ✅ |
| 6 | WithholdingBucketCreationDate | CREATION_DATE | — | ✅ |
| 7 | WithholdingBucketEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | WithholdingBucketEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | WithholdingBucketFirstPartyTaxProfileId | FIRST_PARTY_TAX_PROFILE_ID | — | — |
| 10 | WithholdingBucketLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | WithholdingBucketLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | WithholdingBucketLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | WithholdingBucketObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | WithholdingBucketPeriodName | PERIOD_NAME | — | ✅ |
| 15 | WithholdingBucketRecordTypeCode | RECORD_TYPE_CODE | — | — |
| 16 | WithholdingBucketSupplierId | SUPPLIER_ID | — | — |
| 17 | WithholdingBucketTax | TAX | — | — |
| 18 | WithholdingBucketTaxBucketId | TAX_BUCKET_ID | 🔑 | ✅ |
| 19 | WithholdingBucketTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | — |
| 20 | WithholdingBucketTaxRegimeCode | TAX_REGIME_CODE | — | — |
| 21 | WithholdingBucketThirdPtySiteTaxProfId | THIRD_PTY_SITE_TAX_PROF_ID | — | — |
| 22 | WithholdingBucketThirdPtyTaxProfId | THIRD_PTY_TAX_PROF_ID | — | — |

### [[zx_party_tax_profile|ZX_PARTY_TAX_PROFILE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyTaxProfilePartyId | PARTY_ID | — | — |
| 2 | PartyTaxProfilePartyTaxProfileId | PARTY_TAX_PROFILE_ID | — | — |
| 3 | PartyTaxProfilePartyTypeCode | PARTY_TYPE_CODE | — | — |

### [[zx_taxes_b|ZX_TAXES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxesTaxId | TAX_ID | — | — |

### [[zx_taxes_tl|ZX_TAXES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxesTLLanguage | LANGUAGE | — | — |
| 2 | TaxesTLTaxId | TAX_ID | — | — |
| 3 | TaxesTaxFullName | TAX_FULL_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
