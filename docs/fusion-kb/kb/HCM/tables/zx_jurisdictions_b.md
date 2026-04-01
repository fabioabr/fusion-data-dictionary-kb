---
id: DOC-HCM-890
doc_type: system-doc
title: "ZX_JURISDICTIONS_B — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - ZX_JURISDICTIONS_B
  - zx_jurisdictions_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_JURISDICTIONS_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOW_TAX_REGISTRATIONS_FLAG | — | — | — | — | — | — |
| 2 | ATTRIBUTE_CATEGORY | — | — | — | — | — | — |
| 3 | COLL_TAX_AUTHORITY_ID | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | DEFAULT_FLG_EFFECTIVE_FROM | — | — | — | — | — | — |
| 7 | DEFAULT_FLG_EFFECTIVE_TO | — | — | — | — | — | — |
| 8 | DEFAULT_JURISDICTION_FLAG | — | — | — | — | — | — |
| 9 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 10 | EFFECTIVE_TO | — | — | — | — | — | — |
| 11 | INNER_CITY_JURISDICTION_FLAG | — | — | — | — | — | — |
| 12 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 15 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 16 | PRECEDENCE_LEVEL | — | — | — | — | — | — |
| 17 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 18 | REP_TAX_AUTHORITY_ID | — | — | — | — | — | — |
| 19 | TAX | — | — | — | — | — | — |
| 20 | TAX_ACCT_SRC_JURISDICT_ID | — | — | — | — | — | — |
| 21 | TAX_EXMPT_SRC_JURISDICT_ID | — | — | — | — | — | — |
| 22 | TAX_JURISDICTION_CODE | — | — | — | — | — | — |
| 23 | TAX_JURISDICTION_ID | — | — | — | — | — | — |
| 24 | TAX_REGIME_CODE | — | — | — | — | — | — |
| 25 | THRSHLD_SCHEDULE_GRP_LVL_FLAG | — | — | — | — | — | — |
| 26 | UNIQUENESS_VALIDATION_LEVEL | — | — | — | — | — | — |
| 27 | VALIDATION_LEVEL | — | — | — | — | — | — |
| 28 | VALIDATION_TYPE | — | — | — | — | — | — |
| 29 | WHT_BUCKET_LEVEL_FLAG | — | — | — | — | — | — |
| 30 | ZONE_GEOGRAPHY_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TAX_JURISDICTION_CODE | TaxJurisTaxJurisdictionCode | — |
| TAX_JURISDICTION_ID | TaxJurisTaxJurisdictionId | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | TaxJurisLastUpdateDate | ✅ |
| TAX_JURISDICTION_CODE | TaxJurisTaxJurisdictionCode | — |
| TAX_JURISDICTION_ID | TaxJurisTaxJurisdictionId | — |

### [[taxjurisdictionextractpvo|TaxJurisdictionExtractPVO]] (OTHER · BICC: 29/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_TAX_REGISTRATIONS_FLAG | TaxJurisdictionAllowTaxRegistrationsFlag | ✅ |
| ATTRIBUTE_CATEGORY | TaxJurisdictionAttributeCategory | — |
| COLL_TAX_AUTHORITY_ID | TaxJurisdictionCollTaxAuthorityId | ✅ |
| CREATED_BY | TaxJurisdictionCreatedBy | ✅ |
| CREATION_DATE | TaxJurisdictionCreationDate | ✅ |
| DEFAULT_FLG_EFFECTIVE_FROM | TaxJurisdictionDefaultFlgEffectiveFrom | ✅ |
| DEFAULT_FLG_EFFECTIVE_TO | TaxJurisdictionDefaultFlgEffectiveTo | ✅ |
| DEFAULT_JURISDICTION_FLAG | TaxJurisdictionDefaultJurisdictionFlag | ✅ |
| EFFECTIVE_FROM | TaxJurisdictionEffectiveFrom | ✅ |
| EFFECTIVE_TO | TaxJurisdictionEffectiveTo | ✅ |
| INNER_CITY_JURISDICTION_FLAG | TaxJurisdictionInnerCityJurisdictionFlag | ✅ |
| LAST_UPDATE_DATE | TaxJurisdictionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaxJurisdictionLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | TaxJurisdictionObjectVersionNumber | ✅ |
| PRECEDENCE_LEVEL | TaxJurisdictionPrecedenceLevel | ✅ |
| RECORD_TYPE_CODE | TaxJurisdictionRecordTypeCode | ✅ |
| REP_TAX_AUTHORITY_ID | TaxJurisdictionRepTaxAuthorityId | ✅ |
| TAX | TaxJurisdictionTax | ✅ |
| TAX_ACCT_SRC_JURISDICT_ID | TaxJurisdictionTaxAcctSrcJurisdictId | ✅ |
| TAX_EXMPT_SRC_JURISDICT_ID | TaxJurisdictionTaxExmptSrcJurisdictId | ✅ |
| TAX_JURISDICTION_CODE | TaxJurisdictionTaxJurisdictionCode | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTaxJurisdictionId | ✅ |
| TAX_REGIME_CODE | TaxJurisdictionTaxRegimeCode | ✅ |
| THRSHLD_SCHEDULE_GRP_LVL_FLAG | TaxJurisdictionThrshldScheduleGrpLvlFlag | ✅ |
| UNIQUENESS_VALIDATION_LEVEL | TaxJurisdictionUniquenessValidationLevel | ✅ |
| VALIDATION_LEVEL | TaxJurisdictionValidationLevel | ✅ |
| VALIDATION_TYPE | TaxJurisdictionValidationType | ✅ |
| WHT_BUCKET_LEVEL_FLAG | TaxJurisdictionWhtBucketLevelFlag | ✅ |
| ZONE_GEOGRAPHY_ID | TaxJurisdictionZoneGeographyId | ✅ |
