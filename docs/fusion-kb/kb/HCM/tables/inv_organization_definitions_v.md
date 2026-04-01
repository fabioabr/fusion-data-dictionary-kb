---
id: DOC-HCM-525
doc_type: system-doc
title: "INV_ORGANIZATION_DEFINITIONS_V — (título a preencher)"
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
  - INV_ORGANIZATION_DEFINITIONS_V
  - inv_organization_definitions_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# INV_ORGANIZATION_DEFINITIONS_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_GROUP_ID | — | — | — | — | — | — |
| 2 | BUSINESS_UNIT_ID | — | — | — | — | — | — |
| 3 | BUSINESS_UNIT_NAME | — | — | — | — | — | — |
| 4 | CHART_OF_ACCOUNTS_ID | — | — | — | — | — | — |
| 5 | CURRENCY_CODE | — | — | — | — | — | — |
| 6 | DISABLE_DATE | — | — | — | — | — | — |
| 7 | DISTRIBUTED_ORGANIZATION_FLAG | — | — | — | — | — | — |
| 8 | INVENTORY_ENABLED_FLAG | — | — | — | — | — | — |
| 9 | INVENTORY_FLAG | — | — | — | — | — | — |
| 10 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 11 | LEGAL_ENTITY | — | — | — | — | — | — |
| 12 | LOCATION_ID | — | — | — | — | — | — |
| 13 | MANUAL_RECEIPT_EXP_AT_DEST | — | — | — | — | — | — |
| 14 | MASTER_ORGANIZATION_ID | — | — | — | — | — | — |
| 15 | ORGANIZATION_CODE | — | — | — | — | — | — |
| 16 | ORGANIZATION_ID | — | — | — | — | — | — |
| 17 | ORGANIZATION_NAME | — | — | — | — | — | — |
| 18 | ORGANIZATION_TYPE | — | — | — | — | — | — |
| 19 | PERIOD_SET_NAME | — | — | — | — | — | — |
| 20 | PROFIT_CENTER_BU_ID | — | — | — | — | — | — |
| 21 | SET_OF_BOOKS_ID | — | — | — | — | — | — |
| 22 | USER_DEFINITION_ENABLE_DATE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |

### [[carrierservicepvo|CarrierServicePVO]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPEOOrganizationCode | ✅ |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPEOOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPEOOrganizationName | ✅ |

### [[contractheadercurrentp|ContractHeaderCurrentP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_CODE | ContractLineShipInvOrgPEOOrganizationCode | — |
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_ID | ContractLineShipInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | — |
| ORGANIZATION_NAME | ContractLineShipInvOrgPEOOrganizationName | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_CODE | ContractLineShipInvOrgPEOOrganizationCode | — |
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_ID | ContractLineShipInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | — |
| ORGANIZATION_NAME | ContractLineShipInvOrgPEOOrganizationName | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_CODE | ContractLineShipInvOrgPEOOrganizationCode | — |
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_ID | ContractLineShipInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | ✅ |
| ORGANIZATION_NAME | ContractLineShipInvOrgPEOOrganizationName | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_CODE | ContractLineShipInvOrgPEOOrganizationCode | — |
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_ID | ContractLineShipInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | ✅ |
| ORGANIZATION_NAME | ContractLineShipInvOrgPEOOrganizationName | — |

### [[contractheaderp|ContractHeaderP]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | ✅ |

### [[contractheaderrefp|ContractHeaderRefP]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ORGANIZATION_ID | ContractHeaderInvOrgPEOOrganizationId | — |
| ORGANIZATION_NAME | ContractHeaderInvOrgPEOOrganizationName | ✅ |

### [[draftpurchaseorderdistributionpvo|DraftPurchaseOrderDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |

### [[draftpurchaseorderdistributionrefpvo|DraftPurchaseOrderDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |

### [[draftpurchasingdocumentlinelocationpvo|DraftPurchasingDocumentLineLocationPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |

### [[hrlocationsbasepvo|HRLocationsBasePVO]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | InventoryOrganizationPEOLastUpdateDate | — |
| ORGANIZATION_ID | InventoryOrganizationPEOOrganizationId | — |
| ORGANIZATION_NAME | InventoryOrganizationPEOOrganizationName | ✅ |

### [[hrlocationsbasepvoviewall|HRLocationsBasePVOViewAll]] (HCM · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | InventoryOrganizationPEOLastUpdateDate | — |
| ORGANIZATION_ID | InventoryOrganizationPEOOrganizationId | — |
| ORGANIZATION_NAME | InventoryOrganizationPEOOrganizationName | ✅ |

### [[hrlocationspvo|HRLocationsPVO]] (HCM · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | InventoryOrganizationPEOLastUpdateDate | — |
| ORGANIZATION_ID | InventoryOrganizationPEOOrganizationId | ✅ |
| ORGANIZATION_NAME | InventoryOrganizationPEOOrganizationName | ✅ |

### [[hrlocationspvoviewall|HRLocationsPVOViewAll]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | InventoryOrganizationPEOLastUpdateDate | — |
| ORGANIZATION_ID | InventoryOrganizationPEOOrganizationId | — |
| ORGANIZATION_NAME | InventoryOrganizationPEOOrganizationName | — |

### [[inventorylocatorpvo|InventoryLocatorPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventorylocatorrefpvo|InventoryLocatorRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparameterscyclecountvcpvo|InventoryOrgParametersCycleCountVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparametersinvtransvcpvo|InventoryOrgParametersInvTransVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparametersonhandqtyvcpvo|InventoryOrgParametersOnhandQtyVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparametersrcvreceiptdatavcpvo|InventoryOrgParametersRcvReceiptDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparametersrefpvo|InventoryOrgParametersRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventoryorgparametersshipmentdatavcpvo|InventoryOrgParametersShipmentDataVCPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventorysubinventorypvo|InventorySubinventoryPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[inventorysubinventoryrefpvo|InventorySubinventoryRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | OrgOrganizationDefinitionsPBusinessGroupId | — |
| BUSINESS_UNIT_ID | OrgOrganizationDefinitionsPBusinessUnitId | — |
| BUSINESS_UNIT_NAME | OrgOrganizationDefinitionsPBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | OrgOrganizationDefinitionsPChartOfAccountsId | — |
| CURRENCY_CODE | OrgOrganizationDefinitionsPCurrencyCode | — |
| DISABLE_DATE | OrgOrganizationDefinitionsPDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | OrgOrganizationDefinitionsPDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | OrgOrganizationDefinitionsPInventoryEnabledFlag | — |
| INVENTORY_FLAG | OrgOrganizationDefinitionsPInventoryFlag | — |
| LEGAL_ENTITY | OrgOrganizationDefinitionsPLegalEntity | — |
| LOCATION_ID | OrgOrganizationDefinitionsPLocationId | — |
| MASTER_ORGANIZATION_ID | OrgOrganizationDefinitionsPMasterOrganizationId | — |
| ORGANIZATION_CODE | OrgOrganizationDefinitionsPOrganizationCode | — |
| ORGANIZATION_ID | OrgOrganizationDefinitionsPOrganizationId | — |
| ORGANIZATION_NAME | OrgOrganizationDefinitionsPOrganizationName | — |
| ORGANIZATION_TYPE | OrgOrganizationDefinitionsPOrganizationType | — |
| PERIOD_SET_NAME | OrgOrganizationDefinitionsPPeriodSetName | — |
| SET_OF_BOOKS_ID | OrgOrganizationDefinitionsPSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | OrgOrganizationDefinitionsPUserDefinitionEnableDate | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | InvOrgDefinitionBusinessGroupId | — |
| BUSINESS_UNIT_ID | InvOrgDefinitionBusinessUnitId | — |
| BUSINESS_UNIT_NAME | InvOrgDefinitionBusinessUnitName | — |
| CHART_OF_ACCOUNTS_ID | InvOrgDefinitionChartOfAccountsId | — |
| CURRENCY_CODE | InvOrgDefinitionCurrencyCode | — |
| DISABLE_DATE | InvOrgDefinitionDisableDate | — |
| DISTRIBUTED_ORGANIZATION_FLAG | InvOrgDefinitionDistributedOrganizationFlag | — |
| INVENTORY_ENABLED_FLAG | InvOrgDefinitionInventoryEnabledFlag | — |
| INVENTORY_FLAG | InvOrgDefinitionInventoryFlag | — |
| LEGAL_ENTITY | InvOrgDefinitionLegalEntity | — |
| LOCATION_ID | InvOrgDefinitionLocationId | — |
| MANUAL_RECEIPT_EXP_AT_DEST | InvOrgDefinitionManualReceiptExpAtDest | — |
| MASTER_ORGANIZATION_ID | InvOrgDefinitionMasterOrganizationId | — |
| ORGANIZATION_CODE | InvOrgDefinitionOrganizationCode | — |
| ORGANIZATION_ID | InvOrgDefinitionOrganizationId | — |
| ORGANIZATION_NAME | InvOrgDefinitionOrganizationName | — |
| ORGANIZATION_TYPE | InvOrgDefinitionOrganizationType | — |
| PERIOD_SET_NAME | InvOrgDefinitionPeriodSetName | — |
| PROFIT_CENTER_BU_ID | InvOrgDefinitionProfitCenterBuId | — |
| SET_OF_BOOKS_ID | InvOrgDefinitionSetOfBooksId | — |
| USER_DEFINITION_ENABLE_DATE | InvOrgDefinitionUserDefinitionEnableDate | — |
