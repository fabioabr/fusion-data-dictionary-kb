---
id: DOC-HCM-504
doc_type: system-doc
title: "HZ_PARTY_SITE_USES — (título a preencher)"
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
  - HZ_PARTY_SITE_USES
  - hz_party_site_uses
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_PARTY_SITE_USES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ATTRIBUTE1 | — | — | — | — | — | — |
| 2 | ATTRIBUTE10 | — | — | — | — | — | — |
| 3 | ATTRIBUTE11 | — | — | — | — | — | — |
| 4 | ATTRIBUTE12 | — | — | — | — | — | — |
| 5 | ATTRIBUTE13 | — | — | — | — | — | — |
| 6 | ATTRIBUTE14 | — | — | — | — | — | — |
| 7 | ATTRIBUTE15 | — | — | — | — | — | — |
| 8 | ATTRIBUTE16 | — | — | — | — | — | — |
| 9 | ATTRIBUTE17 | — | — | — | — | — | — |
| 10 | ATTRIBUTE18 | — | — | — | — | — | — |
| 11 | ATTRIBUTE19 | — | — | — | — | — | — |
| 12 | ATTRIBUTE2 | — | — | — | — | — | — |
| 13 | ATTRIBUTE20 | — | — | — | — | — | — |
| 14 | ATTRIBUTE21 | — | — | — | — | — | — |
| 15 | ATTRIBUTE22 | — | — | — | — | — | — |
| 16 | ATTRIBUTE23 | — | — | — | — | — | — |
| 17 | ATTRIBUTE24 | — | — | — | — | — | — |
| 18 | ATTRIBUTE25 | — | — | — | — | — | — |
| 19 | ATTRIBUTE26 | — | — | — | — | — | — |
| 20 | ATTRIBUTE27 | — | — | — | — | — | — |
| 21 | ATTRIBUTE28 | — | — | — | — | — | — |
| 22 | ATTRIBUTE29 | — | — | — | — | — | — |
| 23 | ATTRIBUTE3 | — | — | — | — | — | — |
| 24 | ATTRIBUTE30 | — | — | — | — | — | — |
| 25 | ATTRIBUTE4 | — | — | — | — | — | — |
| 26 | ATTRIBUTE5 | — | — | — | — | — | — |
| 27 | ATTRIBUTE6 | — | — | — | — | — | — |
| 28 | ATTRIBUTE7 | — | — | — | — | — | — |
| 29 | ATTRIBUTE8 | — | — | — | — | — | — |
| 30 | ATTRIBUTE9 | — | — | — | — | — | — |
| 31 | ATTRIBUTE_CATEGORY | — | — | — | — | — | — |
| 32 | BEGIN_DATE | — | — | — | — | — | — |
| 33 | COMMENTS | — | — | — | — | — | — |
| 34 | CREATED_BY | — | — | — | — | — | — |
| 35 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 36 | CREATION_DATE | — | — | — | — | — | — |
| 37 | END_DATE | — | — | — | — | — | — |
| 38 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 39 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 40 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 41 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 42 | PARTY_SITE_ID | — | — | — | — | — | — |
| 43 | PARTY_SITE_USE_ID | — | — | — | — | — | — |
| 44 | PRIMARY_PER_TYPE | — | — | — | — | — | — |
| 45 | SITE_USE_TYPE | — | — | — | — | — | — |
| 46 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountcreditcard|AccountCreditCard]] (AR · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BEGIN_DATE | PartySiteUseBeginDate | — |
| COMMENTS | PartySiteUseComments | — |
| CREATED_BY | PartySiteUseCreatedBy | — |
| CREATED_BY_MODULE | PartySiteUseCreatedByModule | — |
| CREATION_DATE | PartySiteUseCreationDate | — |
| END_DATE | PartySiteUseEndDate | — |
| LAST_UPDATE_DATE | PartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartySiteUseLastUpdateLogin | — |
| LAST_UPDATED_BY | PartySiteUseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartySiteUseObjectVersionNumber | — |
| PARTY_SITE_ID | PartySiteUsePartySiteId | — |
| PARTY_SITE_USE_ID | PartySiteUsePartySiteUseId | — |
| PRIMARY_PER_TYPE | PartySiteUsePrimaryPerType | — |
| SITE_USE_TYPE | PartySiteUseSiteUseType | — |
| STATUS | PartySiteUseStatus | — |

### [[addresspvo|AddressPVO]] (OTHER · BICC: 2/46)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | PartySiteUsePEOAttribute1 | — |
| ATTRIBUTE10 | PartySiteUsePEOAttribute10 | — |
| ATTRIBUTE11 | PartySiteUsePEOAttribute11 | — |
| ATTRIBUTE12 | PartySiteUsePEOAttribute12 | — |
| ATTRIBUTE13 | PartySiteUsePEOAttribute13 | — |
| ATTRIBUTE14 | PartySiteUsePEOAttribute14 | — |
| ATTRIBUTE15 | PartySiteUsePEOAttribute15 | — |
| ATTRIBUTE16 | PartySiteUsePEOAttribute16 | — |
| ATTRIBUTE17 | PartySiteUsePEOAttribute17 | — |
| ATTRIBUTE18 | PartySiteUsePEOAttribute18 | — |
| ATTRIBUTE19 | PartySiteUsePEOAttribute19 | — |
| ATTRIBUTE2 | PartySiteUsePEOAttribute2 | — |
| ATTRIBUTE20 | PartySiteUsePEOAttribute20 | — |
| ATTRIBUTE21 | PartySiteUsePEOAttribute21 | — |
| ATTRIBUTE22 | PartySiteUsePEOAttribute22 | — |
| ATTRIBUTE23 | PartySiteUsePEOAttribute23 | — |
| ATTRIBUTE24 | PartySiteUsePEOAttribute24 | — |
| ATTRIBUTE25 | PartySiteUsePEOAttribute25 | — |
| ATTRIBUTE26 | PartySiteUsePEOAttribute26 | — |
| ATTRIBUTE27 | PartySiteUsePEOAttribute27 | — |
| ATTRIBUTE28 | PartySiteUsePEOAttribute28 | — |
| ATTRIBUTE29 | PartySiteUsePEOAttribute29 | — |
| ATTRIBUTE3 | PartySiteUsePEOAttribute3 | — |
| ATTRIBUTE30 | PartySiteUsePEOAttribute30 | — |
| ATTRIBUTE4 | PartySiteUsePEOAttribute4 | — |
| ATTRIBUTE5 | PartySiteUsePEOAttribute5 | — |
| ATTRIBUTE6 | PartySiteUsePEOAttribute6 | — |
| ATTRIBUTE7 | PartySiteUsePEOAttribute7 | — |
| ATTRIBUTE8 | PartySiteUsePEOAttribute8 | — |
| ATTRIBUTE9 | PartySiteUsePEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | PartySiteUsePEOAttributeCategory | — |
| BEGIN_DATE | PartySiteUsePEOBeginDate | — |
| COMMENTS | PartySiteUsePEOComments | — |
| CREATED_BY | PartySiteUsePEOCreatedBy | — |
| CREATED_BY_MODULE | PartySiteUsePEOCreatedByModule | — |
| CREATION_DATE | PartySiteUsePEOCreationDate | — |
| END_DATE | PartySiteUsePEOEndDate | — |
| LAST_UPDATE_DATE | PartySiteUsePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PartySiteUsePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PartySiteUsePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartySiteUsePEOObjectVersionNumber | — |
| PARTY_SITE_ID | PartySiteUsePEOPartySiteId | — |
| PARTY_SITE_USE_ID | PartySiteUsePEOPartySiteUseId | ✅ |
| PRIMARY_PER_TYPE | PartySiteUsePEOPrimaryPerType | — |
| SITE_USE_TYPE | PartySiteUsePEOSiteUseType | ✅ |
| STATUS | PartySiteUsePEOStatus | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[sitecreditcard|SiteCreditCard]] (AR · BICC: 1/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BEGIN_DATE | PartySiteUseBeginDate | — |
| COMMENTS | PartySiteUseComments | — |
| CREATED_BY | PartySiteUseCreatedBy | — |
| CREATED_BY_MODULE | PartySiteUseCreatedByModule | — |
| CREATION_DATE | PartySiteUseCreationDate | — |
| END_DATE | PartySiteUseEndDate | — |
| LAST_UPDATE_DATE | PartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartySiteUseLastUpdateLogin | — |
| LAST_UPDATED_BY | PartySiteUseLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | PartySiteUseObjectVersionNumber | — |
| PARTY_SITE_ID | PartySiteUsePartySiteId | — |
| PARTY_SITE_USE_ID | PartySiteUsePartySiteUseId | — |
| PRIMARY_PER_TYPE | PartySiteUsePrimaryPerType | — |
| SITE_USE_TYPE | PartySiteUseSiteUseType | — |
| STATUS | PartySiteUseStatus | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | ShipToPartySiteUseLastUpdateDate | ✅ |
| LAST_UPDATED_BY | ShipToPartySiteUseLastUpdatedBy | — |
| PARTY_SITE_USE_ID | ShipToPartySiteUsePartySiteUseId | — |
