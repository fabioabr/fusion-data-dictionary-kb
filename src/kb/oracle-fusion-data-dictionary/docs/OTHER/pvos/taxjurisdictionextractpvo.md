---
id: DOC-OTHER-PVO-TaxJurisdictionExtractPVO
doc_type: system-doc
title: "TaxJurisdictionExtractPVO — PVO Cross-Module"
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
  - TaxJurisdictionExtractPVO
  - taxjurisdictionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxJurisdictionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Jurisdiction Extract. Acessa as tabelas: ZX_JURISDICTIONS_B, ZX_JURISDICTIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxJurisdictionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 39 | 2 | 1 | 38 | 97% |

---

## 🔗 Tabelas Relacionadas

- [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]] — 30 atributos (1 PKs, 29 BICC)
- [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]] — 9 atributos (9 BICC)

---

## ⚙️ Atributos

### [[zx_jurisdictions_b|ZX_JURISDICTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisdictionAllowTaxRegistrationsFlag | ALLOW_TAX_REGISTRATIONS_FLAG | — | ✅ |
| 2 | TaxJurisdictionAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 3 | TaxJurisdictionCollTaxAuthorityId | COLL_TAX_AUTHORITY_ID | — | ✅ |
| 4 | TaxJurisdictionCreatedBy | CREATED_BY | — | ✅ |
| 5 | TaxJurisdictionCreationDate | CREATION_DATE | — | ✅ |
| 6 | TaxJurisdictionDefaultFlgEffectiveFrom | DEFAULT_FLG_EFFECTIVE_FROM | — | ✅ |
| 7 | TaxJurisdictionDefaultFlgEffectiveTo | DEFAULT_FLG_EFFECTIVE_TO | — | ✅ |
| 8 | TaxJurisdictionDefaultJurisdictionFlag | DEFAULT_JURISDICTION_FLAG | — | ✅ |
| 9 | TaxJurisdictionEffectiveFrom | EFFECTIVE_FROM | — | ✅ |
| 10 | TaxJurisdictionEffectiveTo | EFFECTIVE_TO | — | ✅ |
| 11 | TaxJurisdictionInnerCityJurisdictionFlag | INNER_CITY_JURISDICTION_FLAG | — | ✅ |
| 12 | TaxJurisdictionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | TaxJurisdictionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | TaxJurisdictionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | TaxJurisdictionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | TaxJurisdictionPrecedenceLevel | PRECEDENCE_LEVEL | — | ✅ |
| 17 | TaxJurisdictionRecordTypeCode | RECORD_TYPE_CODE | — | ✅ |
| 18 | TaxJurisdictionRepTaxAuthorityId | REP_TAX_AUTHORITY_ID | — | ✅ |
| 19 | TaxJurisdictionTax | TAX | — | ✅ |
| 20 | TaxJurisdictionTaxAcctSrcJurisdictId | TAX_ACCT_SRC_JURISDICT_ID | — | ✅ |
| 21 | TaxJurisdictionTaxExmptSrcJurisdictId | TAX_EXMPT_SRC_JURISDICT_ID | — | ✅ |
| 22 | TaxJurisdictionTaxJurisdictionCode | TAX_JURISDICTION_CODE | — | ✅ |
| 23 | TaxJurisdictionTaxJurisdictionId | TAX_JURISDICTION_ID | 🔑 | ✅ |
| 24 | TaxJurisdictionTaxRegimeCode | TAX_REGIME_CODE | — | ✅ |
| 25 | TaxJurisdictionThrshldScheduleGrpLvlFlag | THRSHLD_SCHEDULE_GRP_LVL_FLAG | — | ✅ |
| 26 | TaxJurisdictionUniquenessValidationLevel | UNIQUENESS_VALIDATION_LEVEL | — | ✅ |
| 27 | TaxJurisdictionValidationLevel | VALIDATION_LEVEL | — | ✅ |
| 28 | TaxJurisdictionValidationType | VALIDATION_TYPE | — | ✅ |
| 29 | TaxJurisdictionWhtBucketLevelFlag | WHT_BUCKET_LEVEL_FLAG | — | ✅ |
| 30 | TaxJurisdictionZoneGeographyId | ZONE_GEOGRAPHY_ID | — | ✅ |

### [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisdictionTLCreatedBy1 | CREATED_BY | — | ✅ |
| 2 | TaxJurisdictionTLCreationDate1 | CREATION_DATE | — | ✅ |
| 3 | TaxJurisdictionTLLanguage | LANGUAGE | — | ✅ |
| 4 | TaxJurisdictionTLLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxJurisdictionTLLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxJurisdictionTLLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxJurisdictionTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxJurisdictionTLTaxJurisdictionId | TAX_JURISDICTION_ID | — | ✅ |
| 9 | TaxJurisdictionTLTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
