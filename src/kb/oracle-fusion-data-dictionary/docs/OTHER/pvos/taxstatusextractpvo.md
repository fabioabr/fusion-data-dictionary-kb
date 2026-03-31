---
id: DOC-OTHER-PVO-TaxStatusExtractPVO
doc_type: system-doc
title: "TaxStatusExtractPVO — PVO Cross-Module"
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
  - TaxStatusExtractPVO
  - taxstatusextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxStatusExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Status Extract. Acessa as tabelas: ZX_STATUS_B, ZX_STATUS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxStatusExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 2 | 1 | 31 | 66% |

---

## 🔗 Tabelas Relacionadas

- [[zx_status_b|ZX_STATUS_B]] — 38 atributos (1 PKs, 22 BICC)
- [[zx_status_tl|ZX_STATUS_TL]] — 9 atributos (9 BICC)

---

## ⚙️ Atributos

### [[zx_status_b|ZX_STATUS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxStatusBaseAllowExceptionsFlag | ALLOW_EXCEPTIONS_FLAG | — | ✅ |
| 2 | TaxStatusBaseAllowExemptionsFlag | ALLOW_EXEMPTIONS_FLAG | — | ✅ |
| 3 | TaxStatusBaseAllowRateOverrideFlag | ALLOW_RATE_OVERRIDE_FLAG | — | ✅ |
| 4 | TaxStatusBaseAttribute1 | ATTRIBUTE1 | — | — |
| 5 | TaxStatusBaseAttribute10 | ATTRIBUTE10 | — | — |
| 6 | TaxStatusBaseAttribute11 | ATTRIBUTE11 | — | — |
| 7 | TaxStatusBaseAttribute12 | ATTRIBUTE12 | — | — |
| 8 | TaxStatusBaseAttribute13 | ATTRIBUTE13 | — | — |
| 9 | TaxStatusBaseAttribute14 | ATTRIBUTE14 | — | — |
| 10 | TaxStatusBaseAttribute15 | ATTRIBUTE15 | — | — |
| 11 | TaxStatusBaseAttribute2 | ATTRIBUTE2 | — | — |
| 12 | TaxStatusBaseAttribute3 | ATTRIBUTE3 | — | — |
| 13 | TaxStatusBaseAttribute4 | ATTRIBUTE4 | — | — |
| 14 | TaxStatusBaseAttribute5 | ATTRIBUTE5 | — | — |
| 15 | TaxStatusBaseAttribute6 | ATTRIBUTE6 | — | — |
| 16 | TaxStatusBaseAttribute7 | ATTRIBUTE7 | — | — |
| 17 | TaxStatusBaseAttribute8 | ATTRIBUTE8 | — | — |
| 18 | TaxStatusBaseAttribute9 | ATTRIBUTE9 | — | — |
| 19 | TaxStatusBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | TaxStatusBaseContentOwnerId | CONTENT_OWNER_ID | — | ✅ |
| 21 | TaxStatusBaseCreatedBy | CREATED_BY | — | ✅ |
| 22 | TaxStatusBaseCreationDate | CREATION_DATE | — | ✅ |
| 23 | TaxStatusBaseDefRecSettlementOptionCode | DEF_REC_SETTLEMENT_OPTION_CODE | — | ✅ |
| 24 | TaxStatusBaseDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | ✅ |
| 25 | TaxStatusBaseDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | ✅ |
| 26 | TaxStatusBaseDefaultStatusFlag | DEFAULT_STATUS_FLAG | — | ✅ |
| 27 | TaxStatusBaseEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 28 | TaxStatusBaseEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 29 | TaxStatusBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 30 | TaxStatusBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 31 | TaxStatusBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 32 | TaxStatusBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | TaxStatusBaseRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 34 | TaxStatusBaseRuleBasedRateFlag | RULE_BASED_RATE_FLAG | — | ✅ |
| 35 | TaxStatusBaseTax | TAX | — | ✅ |
| 36 | TaxStatusBaseTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 37 | TaxStatusBaseTaxStatusCode | TAX_STATUS_CODE | — | ✅ |
| 38 | TaxStatusBaseTaxStatusId | TAX_STATUS_ID | 🔑 | ✅ |

### [[zx_status_tl|ZX_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxStatusTLCreatedBy1 | CREATED_BY | — | ✅ |
| 2 | TaxStatusTLCreationDate1 | CREATION_DATE | — | ✅ |
| 3 | TaxStatusTLLanguage | LANGUAGE | — | ✅ |
| 4 | TaxStatusTLLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxStatusTLLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxStatusTLLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxStatusTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxStatusTLTaxStatusId1 | TAX_STATUS_ID | — | ✅ |
| 9 | TaxStatusTLTaxStatusName | TAX_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
