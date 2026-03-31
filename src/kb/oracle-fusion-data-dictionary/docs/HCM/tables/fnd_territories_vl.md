---
id: DOC-HCM-141
doc_type: system-doc
title: "FND_TERRITORIES_VL — (título a preencher)"
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
  - FND_TERRITORIES_VL
  - fnd_territories_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_TERRITORIES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDRESS_STYLE | — | — | — | — | — | — |
| 2 | ADDRESS_VALIDATION | — | — | — | — | — | — |
| 3 | ALTERNATE_TERRITORY_CODE | — | — | — | — | — | — |
| 4 | BANK_INFO_STYLE | — | — | — | — | — | — |
| 5 | BANK_INFO_VALIDATION | — | — | — | — | — | — |
| 6 | CREATED_BY | — | — | — | — | — | — |
| 7 | CREATION_DATE | — | — | — | — | — | — |
| 8 | CURRENCY_CODE | — | — | — | — | — | — |
| 9 | DESCRIPTION | — | — | — | — | — | — |
| 10 | ENABLED_FLAG | — | — | — | — | — | — |
| 11 | EU_CODE | — | — | — | — | — | — |
| 12 | ISO_NUMERIC_CODE | — | — | — | — | — | — |
| 13 | ISO_TERRITORY_CODE | — | — | — | — | — | — |
| 14 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 15 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 16 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 17 | NLS_TERRITORY | — | — | — | — | — | — |
| 18 | OBSOLETE_FLAG | — | — | — | — | — | — |
| 19 | TERRITORY_CODE | — | — | — | — | — | — |
| 20 | TERRITORY_SHORT_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TERRITORY_CODE | TerritoryPEOTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryPEOTerritoryShortName | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TERRITORY_CODE | TerritoryPEOTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryPEOTerritoryShortName | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TERRITORY_CODE | TerritoryPEOTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryPEOTerritoryShortName | — |

### [[supplieraddresspvo|SupplierAddressPVO]] (PO · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_STYLE | TerritoryAddressStyle | — |
| ADDRESS_VALIDATION | TerritoryAddressValidation | — |
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| BANK_INFO_STYLE | TerritoryBankInfoStyle | — |
| BANK_INFO_VALIDATION | TerritoryBankInfoValidation | — |
| CREATED_BY | TerritoryCreatedBy | — |
| CREATION_DATE | TerritoryCreationDate | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| ENABLED_FLAG | TerritoryEnabledFlag | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| LAST_UPDATE_DATE | TerritoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TerritoryLastUpdateLogin | — |
| LAST_UPDATED_BY | TerritoryLastUpdatedBy | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| OBSOLETE_FLAG | TerritoryObsoleteFlag | — |
| TERRITORY_CODE | TerritoryTerritoryCode | ✅ |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[supplierregistrationaddressrequestpvo|SupplierRegistrationAddressRequestPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[supplierregistrationmappingpvo|SupplierRegistrationMappingPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[suppliersitepvo|SupplierSitePVO]] (PO · BICC: 1/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDRESS_STYLE | TerritoryAddressStyle | — |
| ADDRESS_VALIDATION | TerritoryAddressValidation | — |
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| BANK_INFO_STYLE | TerritoryBankInfoStyle | — |
| BANK_INFO_VALIDATION | TerritoryBankInfoValidation | — |
| CREATED_BY | TerritoryCreatedBy | — |
| CREATION_DATE | TerritoryCreationDate | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| ENABLED_FLAG | TerritoryEnabledFlag | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| LAST_UPDATE_DATE | TerritoryLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TerritoryLastUpdateLogin | — |
| LAST_UPDATED_BY | TerritoryLastUpdatedBy | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| OBSOLETE_FLAG | TerritoryObsoleteFlag | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryShortName | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALTERNATE_TERRITORY_CODE | TerritoryAlternateTerritoryCode | — |
| CURRENCY_CODE | TerritoryCurrencyCode | — |
| DESCRIPTION | TerritoryDescription | — |
| EU_CODE | TerritoryEuCode | — |
| ISO_NUMERIC_CODE | TerritoryIsoNumericCode | — |
| ISO_TERRITORY_CODE | TerritoryIsoTerritoryCode | — |
| NLS_TERRITORY | TerritoryNlsTerritory | — |
| TERRITORY_CODE | TerritoryTerritoryCode | — |
| TERRITORY_SHORT_NAME | TerritoryTerritoryShortName | ✅ |
