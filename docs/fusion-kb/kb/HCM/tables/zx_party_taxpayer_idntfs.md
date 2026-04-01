---
id: DOC-HCM-895
doc_type: system-doc
title: "ZX_PARTY_TAXPAYER_IDNTFS — (título a preencher)"
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
  - ZX_PARTY_TAXPAYER_IDNTFS
  - zx_party_taxpayer_idntfs
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_PARTY_TAXPAYER_IDNTFS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COUNTRY_CODE | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 5 | EFFECTIVE_TO | — | — | — | — | — | — |
| 6 | ENTITY_ID | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 11 | PARTY_TAXPAYER_IDNTFS_ID | — | — | — | — | — | — |
| 12 | RECORD_TYPE_CODE | — | — | — | — | — | — |
| 13 | REPORTING_TYPE_CODE | — | — | — | — | — | — |
| 14 | TAX_PAYER_NUMBER | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxvalidation|SiteTaxValidation]] (AR · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | PartyTaxpayerIdentCountryCode | — |
| CREATED_BY | PartyTaxpayerIdentCreatedBy | — |
| CREATION_DATE | PartyTaxpayerIdentCreationDate | — |
| EFFECTIVE_FROM | PartyTaxpayerIdentEffectiveFrom | ✅ |
| EFFECTIVE_TO | PartyTaxpayerIdentEffectiveTo | ✅ |
| ENTITY_ID | PartyTaxpayerIdentEntityId | — |
| LAST_UPDATE_DATE | PartyTaxpayerIdentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxpayerIdentLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxpayerIdentLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartyTaxpayerIdentObjectVersionNumber | — |
| PARTY_TAXPAYER_IDNTFS_ID | PartyTaxpayerIdntfsId | — |
| RECORD_TYPE_CODE | PartyTaxpayerIdentRecordTypeCode | — |
| REPORTING_TYPE_CODE | PartyTaxpayerIdentReportingTypeCode | ✅ |
| TAX_PAYER_NUMBER | PartyTaxpayerIdentTaxPayerNumber | ✅ |

### [[taxvalidation|TaxValidation]] (AR · BICC: 5/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COUNTRY_CODE | PartyTaxpayerIdentCountryCode | — |
| CREATED_BY | PartyTaxpayerIdentCreatedBy | — |
| CREATION_DATE | PartyTaxpayerIdentCreationDate | — |
| EFFECTIVE_FROM | PartyTaxpayerIdentEffectiveFrom | ✅ |
| EFFECTIVE_TO | PartyTaxpayerIdentEffectiveTo | ✅ |
| ENTITY_ID | PartyTaxpayerIdentEntityId | — |
| LAST_UPDATE_DATE | PartyTaxpayerIdentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyTaxpayerIdentLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyTaxpayerIdentLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartyTaxpayerIdentObjectVersionNumber | — |
| PARTY_TAXPAYER_IDNTFS_ID | PartyTaxpayerIdntfsId | — |
| RECORD_TYPE_CODE | PartyTaxpayerIdentRecordTypeCode | — |
| REPORTING_TYPE_CODE | PartyTaxpayerIdentReportingTypeCode | ✅ |
| TAX_PAYER_NUMBER | PartyTaxpayerIdentTaxPayerNumber | ✅ |
