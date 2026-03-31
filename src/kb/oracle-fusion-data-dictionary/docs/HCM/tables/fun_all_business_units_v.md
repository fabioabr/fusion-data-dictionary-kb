---
id: DOC-HCM-147
doc_type: system-doc
title: "FUN_ALL_BUSINESS_UNITS_V — (título a preencher)"
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
  - FUN_ALL_BUSINESS_UNITS_V
  - fun_all_business_units_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_ALL_BUSINESS_UNITS_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_GROUP_ID | — | — | — | — | — | — |
| 2 | BU_ID | — | — | — | — | — | — |
| 3 | BU_NAME | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATION_DATE | — | — | — | — | — | — |
| 6 | DATE_FROM | — | — | — | — | — | — |
| 7 | DATE_TO | — | — | — | — | — | — |
| 8 | DEFAULT_CURRENCY_CODE | — | — | — | — | — | — |
| 9 | DEFAULT_SET_ID | — | — | — | — | — | — |
| 10 | ENABLED_FOR_HR_FLAG | — | — | — | — | — | — |
| 11 | FIN_BUSINESS_UNIT_ID | — | — | — | — | — | — |
| 12 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 13 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 14 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 15 | LEGAL_ENTITY_ID | — | — | — | — | — | — |
| 16 | LOCATION_ID | — | — | — | — | — | — |
| 17 | MANAGER_ID | — | — | — | — | — | — |
| 18 | PRIMARY_LEDGER_ID | — | — | — | — | — | — |
| 19 | PROFIT_CENTER_FLAG | — | — | — | — | — | — |
| 20 | SHORT_CODE | — | — | — | — | — | — |
| 21 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[agreementheaderpvo|AgreementHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| STATUS | BillToBUStatus | — |

### [[agreementlinepvo|AgreementLinePVO]] (PO · BICC: 2/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | — |
| BU_NAME | FromContractHeaderPrcBuName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 2/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | — |
| BU_NAME | FromContractHeaderPrcBuName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[attainment|Attainment]] (OTHER · BICC: 8/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
| SHORT_CODE | ShortCode | ✅ |
| STATUS | BusinessUnitPEOStatus | — |

### [[awardednegotiationresponselinepvo|AwardedNegotiationResponseLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |

### [[billingandrevenuebuusagepvo|BillingAndRevenueBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[billingplan|BillingPlan]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | ✅ |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[businessunitusagepvo|BusinessUnitUsagePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | — |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| DATE_FROM | BusinessUnitDateFrom | — |
| DATE_TO | BusinessUnitDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| MANAGER_ID | BusinessUnitManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitShortCode | — |
| STATUS | BusinessUnitStatus | — |

### [[cmrallperiodclosetxnspvo|CmrAllPeriodCloseTxnsPVO]] (AR · BICC: 20/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | ✅ |
| CREATED_BY | BusinessUnitPEOCreatedBy | ✅ |
| CREATION_DATE | BusinessUnitPEOCreationDate | ✅ |
| DATE_FROM | BusinessUnitPEODateFrom | ✅ |
| DATE_TO | BusinessUnitPEODateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitPEOLocationId | ✅ |
| MANAGER_ID | BusinessUnitPEOManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitPEOShortCode | ✅ |
| STATUS | BusinessUnitPEOStatus | ✅ |

### [[collectionbuusagepvo|CollectionBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[compplan|CompPlan]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[compplansecured|CompPlanSecured]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[contactuseraccountdataaccessdetails|ContactUserAccountDataAccessDetails]] (PO · BICC: 2/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | PrcBUBusinessUnitId | — |
| BU_NAME | PrcBUName | ✅ |
| BUSINESS_GROUP_ID | PrcBUEnterpriseId | — |
| CREATED_BY | PrcBUCreatedBy | — |
| CREATION_DATE | PrcBUCreationDate | — |
| DATE_FROM | PrcBUDateFrom | — |
| DATE_TO | PrcBUDateTo | — |
| DEFAULT_CURRENCY_CODE | PrcBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | PrcBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | PrcBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | PrcBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | PrcBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrcBULastUpdateLogin | — |
| LAST_UPDATED_BY | PrcBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | PrcBULegalEntityId | — |
| LOCATION_ID | PrcBULocationId | — |
| MANAGER_ID | PrcBUManagerId | — |
| PRIMARY_LEDGER_ID | PrcBUPrimaryLedgerId | — |
| SHORT_CODE | PrcBUShortCode | — |
| STATUS | PrcBUStatus | — |

### [[contractheadercurrentp|ContractHeaderCurrentP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOId | — |
| BU_NAME | HdrBUPEOBUName | — |

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | HdrBusinessUnitId | — |
| BU_NAME | HdrBusinessUnitPEOName | — |
| PRIMARY_LEDGER_ID | HdrBusinessUnitPEOLedgerId | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | HdrBusinessUnitId | — |
| BU_NAME | HdrBusinessUnitPEOName | — |
| PRIMARY_LEDGER_ID | HdrBusinessUnitPEOLedgerId | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | HdrBusinessUnitId | — |
| BU_NAME | HdrBusinessUnitPEOName | — |
| PRIMARY_LEDGER_ID | HdrBusinessUnitPEOLedgerId | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | HdrBusinessUnitId | — |
| BU_NAME | HdrBusinessUnitPEOName | — |
| PRIMARY_LEDGER_ID | HdrBusinessUnitPEOLedgerId | — |

### [[contractheaderp|ContractHeaderP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOId | — |
| BU_NAME | HdrBUPEOBUName | — |

### [[contractheaderrefp|ContractHeaderRefP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOId | — |
| BU_NAME | HdrBUPEOBUName | — |

### [[contractpartyp|ContractPartyP]] (OTHER · BICC: 4/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | Name | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | — |
| CREATED_BY | BusinessUnitCreatedBy | — |
| CREATION_DATE | BusinessUnitCreationDate | — |
| DATE_FROM | BusinessUnitDateFrom | — |
| DATE_TO | BusinessUnitDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | — |
| LOCATION_ID | BusinessUnitLocationId | — |
| MANAGER_ID | BusinessUnitManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitProfitCenterFlag | — |
| SHORT_CODE | ShortCode | ✅ |
| STATUS | BusinessUnitStatus | — |

### [[credit|Credit]] (OTHER · BICC: 8/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
| SHORT_CODE | ShortCode | ✅ |

### [[credittype|CreditType]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[crosschargedistributionp1|CrossChargeDistributionP1]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | ✅ |

### [[customercontractbuusagepvo|CustomerContractBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[customerpaymentsbuusagepvo|CustomerPaymentsBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[dispute|Dispute]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[earning|Earning]] (OTHER · BICC: 9/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
| SHORT_CODE | ShortCode | ✅ |
| STATUS | Status | ✅ |

### [[eligiblecategorypvo|EligibleCategoryPVO]] (OTHER · BICC: 3/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | — |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ID | ManagerId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
| SHORT_CODE | ShortCode | ✅ |
| STATUS | Status | ✅ |

### [[expenditureitempvo|ExpenditureItemPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | RecvrBusinessUnitPEOBusinessUnitId | — |
| BU_NAME | RecvrBusinessUnitPEOName | — |

### [[expenditureitemrefpvo|ExpenditureItemRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | RecvrBusinessUnitPEOBusinessUnitId | — |
| BU_NAME | RecvrBusinessUnitPEOName | — |

### [[expensebuusagepvo|ExpenseBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[fdinterfaceexceptionsp1|FDInterfaceExceptionsP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy5 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate5 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate5 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin5 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy5 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldoceventlogp1|FiscalDocEventLogP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy4 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate4 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin4 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy4 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocheadersp|FiscalDocHeadersP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName1 | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy3 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate3 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate3 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin3 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy3 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocreferenceattrp1|FiscalDocReferenceAttrP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy4 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate4 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin4 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy4 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName1 | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy8 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate8 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate8 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin8 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy8 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | HdrBusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | HdrBusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | HdrBusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy7 | — |
| CREATED_BY | HdrBusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate7 | — |
| CREATION_DATE | HdrBusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | HdrBusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | HdrBusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | HdrBusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | HdrBusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | HdrBusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | HdrBusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate7 | — |
| LAST_UPDATE_DATE | HdrBusinessUnitPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin7 | — |
| LAST_UPDATE_LOGIN | HdrBusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy7 | — |
| LAST_UPDATED_BY | HdrBusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | HdrBusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | HdrBusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | HdrBusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | HdrBusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| PROFIT_CENTER_FLAG | HdrBusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | HdrBusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | HdrBusinessUnitPEOStatus | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy15 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate15 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate15 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin15 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy15 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId1 | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[formula|Formula]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[fulfillline|FulfillLine]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[fulfilllinedetail|FulfillLineDetail]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[fulfilllinedetailinvoice|FulfillLineDetailInvoice]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[fulfilllinedetailreceiving|FulfillLineDetailReceiving]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[fulfilllinedetailshipping|FulfillLineDetailShipping]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[fulfilllinedetailtransportationplanning|FulfillLineDetailTransportationPlanning]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[fulfilllineref|FulfillLineRef]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[header|Header]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[holdinstance|HoldInstance]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| BUSINESS_GROUP_ID | BUEnterpriseId | — |
| CREATED_BY | BUCreatedBy | — |
| CREATION_DATE | BUCreationDate | — |
| DATE_FROM | BUDateFrom | — |
| DATE_TO | BUDateTo | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BULastUpdateLogin | — |
| LAST_UPDATED_BY | BULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BULegalEntityId | — |
| LOCATION_ID | BULocationId | — |
| MANAGER_ID | BUManagerId | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BUProfitCenterFlag | — |
| SHORT_CODE | BUShortCode | — |
| STATUS | BUStatus | — |

### [[incentivecompensationbuusagepvo|IncentiveCompensationBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[interfacefiscaldocumentp1|InterfaceFiscalDocumentP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName1 | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy10 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate10 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate10 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin10 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy10 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[inventorylocatorpvo|InventoryLocatorPVO]] (OTHER · BICC: 2/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventorylocatorrefpvo|InventoryLocatorRefPVO]] (OTHER · BICC: 3/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparameterscyclecountvcpvo|InventoryOrgParametersCycleCountVCPVO]] (OTHER · BICC: 2/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparametersinvtransvcpvo|InventoryOrgParametersInvTransVCPVO]] (OTHER · BICC: 2/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparametersonhandqtyvcpvo|InventoryOrgParametersOnhandQtyVCPVO]] (OTHER · BICC: 2/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparametersrcvreceiptdatavcpvo|InventoryOrgParametersRcvReceiptDataVCPVO]] (OTHER · BICC: 2/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparametersrefpvo|InventoryOrgParametersRefPVO]] (OTHER · BICC: 3/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventoryorgparametersshipmentdatavcpvo|InventoryOrgParametersShipmentDataVCPVO]] (OTHER · BICC: 2/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | ✅ |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventorysubinventorypvo|InventorySubinventoryPVO]] (OTHER · BICC: 3/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventorysubinventoryrefpvo|InventorySubinventoryRefPVO]] (OTHER · BICC: 3/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_ID | MasterOrgBUBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BU_NAME | MasterOrgBUName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| BUSINESS_GROUP_ID | MasterOrgBUEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATED_BY | MasterOrgBUCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| CREATION_DATE | MasterOrgBUCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_FROM | MasterOrgBUDateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DATE_TO | MasterOrgBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | MasterOrgBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| DEFAULT_SET_ID | MasterOrgBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | MasterOrgBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | MasterOrgBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | MasterOrgBULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | MasterOrgBULastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LAST_UPDATED_BY | MasterOrgBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LEGAL_ENTITY_ID | MasterOrgBULegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| LOCATION_ID | MasterOrgBULocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| MANAGER_ID | MasterOrgBUManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | MasterOrgBUPrimaryLedgerId | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| SHORT_CODE | MasterOrgBUShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |
| STATUS | MasterOrgBUStatus | — |

### [[inventorysupplypvo|InventorySupplyPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |

### [[inventorytransactiondetailpvo|InventoryTransactionDetailPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |

### [[landedcostpvo|LandedCostPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[legaldocumentassocp1|LegalDocumentAssocP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy4 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate4 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate4 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin4 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy4 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[line|Line]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[lotserial|LotSerial]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |

### [[manualpriceadjustment|ManualPriceAdjustment]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[materialmanagementbuusagepvo|MaterialManagementBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[moacbusinessunitp1|MoacBusinessUnitP1]] (PO · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | ✅ |
| BU_NAME | Name | ✅ |
| SHORT_CODE | ShortCode | — |

### [[negotiationresponsepurchaseorderlinepvo|NegotiationResponsePurchaseOrderLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |

### [[negotiationspvo|NegotiationsPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBuId | — |
| BU_NAME | BusinessUnitBuName | — |

### [[onholdprocessinstance|OnHoldProcessInstance]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |

### [[orchestrationgroup|OrchestrationGroup]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[orchestrationprimaryroutepvo|OrchestrationPrimaryRoutePVO]] (OTHER · BICC: 8/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOFtrBuyingBuId | ✅ |
| BU_ID | BusinessUnitPEOFtrSellingBuId | ✅ |
| BU_ID | BusinessUnitPEOPtrBuyingBuId | ✅ |
| BU_ID | BusinessUnitPEOPtrSellingBuId | ✅ |
| BU_NAME | BusinessUnitPEOFtrBuyingBuName | ✅ |
| BU_NAME | BusinessUnitPEOFtrSellingBuName | ✅ |
| BU_NAME | BusinessUnitPEOPtrBuyingBuName | ✅ |
| BU_NAME | BusinessUnitPEOPtrSellingBuName | ✅ |

### [[orderchargecomponent|OrderChargeComponent]] (OTHER · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | ✅ |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotal|OrderTotal]] (OTHER · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |
| BU_NAME | BUName | ✅ |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | ✅ |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotaldiscount|OrderTotalDiscount]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotalforcredit|OrderTotalForCredit]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotallistprice|OrderTotalListPrice]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotalnetprice|OrderTotalNetPrice]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotalpaynow|OrderTotalPayNow]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotalshipcharge|OrderTotalShipCharge]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[ordertotaltax|OrderTotalTax]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |

### [[participantpay|ParticipantPay]] (HCM · BICC: 3/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ID | ManagerId | ✅ |

### [[participantpvo|ParticipantPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[participantsecuredpvo|ParticipantSecuredPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[payablesinvoicingbuusagepvo|PayablesInvoicingBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[payablespaymentsbuusagepvo|PayablesPaymentsBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[paymentbatch|PaymentBatch]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[paymentplan|PaymentPlan]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[plancomponent|PlanComponent]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[plancomponentsecured|PlanComponentSecured]] (HCM · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[priceadjustment|PriceAdjustment]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |

### [[processinstance|ProcessInstance]] (OTHER · BICC: 1/1)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | ✅ |

### [[procurementbuusagepvo|ProcurementBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[procurementcontractbuusagepvo|ProcurementContractBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[projectaccountingbuusagepvo|ProjectAccountingBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[projectassetlinedetailpvo|ProjectAssetLineDetailPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | ExpProjectBusinessUnitPEOBusinessUnitId | — |

### [[projectassetlinepvo|ProjectAssetLinePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |

### [[projectassetpvo|ProjectAssetPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitID | — |

### [[projectcostdistributionpvo|ProjectCostDistributionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | RecvrBusinessUnitPEOBusinessUnitId | — |
| BU_NAME | RecvrBusinessUnitPEOName | — |

### [[projectunprocessedcosttransactionpvo|ProjectUnprocessedCostTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | RecvrBusinessUnitPEOBusinessUnitId | — |
| BU_NAME | RecvrBusinessUnitPEOName | — |

### [[purchasingagreementbuaccesspvo|PurchasingAgreementBuAccessPVO]] (PO · BICC: 18/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | AgreementBuAccessBilltoBuBusinessUnitId | ✅ |
| BU_ID | AgreementBuAccessReqBuBusinessUnitId | ✅ |
| BU_NAME | AgreementBuAccessBilltoBuName | ✅ |
| BU_NAME | AgreementBuAccessReqBuName | ✅ |
| BUSINESS_GROUP_ID | AgreementBuAccessBilltoBuEnterpriseId | — |
| BUSINESS_GROUP_ID | AgreementBuAccessReqBuEnterpriseId | — |
| CREATED_BY | AgreementBuAccessBilltoBuCreatedBy | ✅ |
| CREATED_BY | AgreementBuAccessReqBuCreatedBy | ✅ |
| CREATION_DATE | AgreementBuAccessBilltoBuCreationDate | ✅ |
| CREATION_DATE | AgreementBuAccessReqBuCreationDate | ✅ |
| DATE_FROM | AgreementBuAccessBilltoBuDateFrom | ✅ |
| DATE_FROM | AgreementBuAccessReqBuDateFrom | ✅ |
| DATE_TO | AgreementBuAccessBilltoBuDateTo | ✅ |
| DATE_TO | AgreementBuAccessReqBuDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | AgreementBuAccessBilltoBuDefaultCurrencyCode | ✅ |
| DEFAULT_CURRENCY_CODE | AgreementBuAccessReqBuDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | AgreementBuAccessBilltoBuDefaultSetId | — |
| DEFAULT_SET_ID | AgreementBuAccessReqBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | AgreementBuAccessBilltoBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | AgreementBuAccessReqBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | AgreementBuAccessBilltoBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | AgreementBuAccessReqBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | AgreementBuAccessBilltoBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | AgreementBuAccessReqBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AgreementBuAccessBilltoBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | AgreementBuAccessReqBuLastUpdateLogin | — |
| LAST_UPDATED_BY | AgreementBuAccessBilltoBuLastUpdatedBy | — |
| LAST_UPDATED_BY | AgreementBuAccessReqBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | AgreementBuAccessBilltoBuLegalEntityId | — |
| LEGAL_ENTITY_ID | AgreementBuAccessReqBuLegalEntityId | — |
| LOCATION_ID | AgreementBuAccessBilltoBuLocationId | — |
| LOCATION_ID | AgreementBuAccessReqBuLocationId | — |
| MANAGER_ID | AgreementBuAccessBilltoBuManagerId | — |
| MANAGER_ID | AgreementBuAccessReqBuManagerId | — |
| PRIMARY_LEDGER_ID | AgreementBuAccessBilltoBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | AgreementBuAccessReqBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | AgreementBuAccessBilltoBuProfitCenterFlag | — |
| SHORT_CODE | AgreementBuAccessBilltoBuShortCode | — |
| SHORT_CODE | AgreementBuAccessReqBuShortCode | — |
| STATUS | AgreementBuAccessBilltoBuStatus | ✅ |
| STATUS | AgreementBuAccessReqBuStatus | ✅ |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO · BICC: 2/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | — |
| BU_NAME | FromContractHeaderPrcBuName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[ratetable|RateTable]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |

### [[receiptaccountingpvo|ReceiptAccountingPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBusinessUnitPEOBusinessUnitId | — |
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BillToBusinessUnitPEOName | — |
| BU_NAME | BusinessUnitPEOName | — |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBusinessUnitPEOBusinessUnitId3 | — |
| BU_ID | BusinessUnitPEOBusinessUnitId2 | — |
| BU_NAME | BillToBusinessUnitPEOName1 | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BillToBusinessUnitPEOEnterpriseId1 | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BillToBusinessUnitPEOCreatedBy25 | — |
| CREATED_BY | BusinessUnitPEOCreatedBy23 | — |
| CREATION_DATE | BillToBusinessUnitPEOCreationDate25 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate23 | — |
| DATE_FROM | BillToBusinessUnitPEODateFrom1 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BillToBusinessUnitPEODateTo1 | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBusinessUnitPEODefaultCurrencyCode1 | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBusinessUnitPEODefaultSetId1 | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBusinessUnitPEOEnabledForHrFlag1 | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBusinessUnitPEOFinancialsBusinessUnitId1 | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBusinessUnitPEOLastUpdateDate25 | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate23 | — |
| LAST_UPDATE_LOGIN | BillToBusinessUnitPEOLastUpdateLogin25 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin23 | — |
| LAST_UPDATED_BY | BillToBusinessUnitPEOLastUpdatedBy25 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy23 | — |
| LEGAL_ENTITY_ID | BillToBusinessUnitPEOLegalEntityId4 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId3 | — |
| LOCATION_ID | BillToBusinessUnitPEOLocationId3 | — |
| LOCATION_ID | BusinessUnitPEOLocationId2 | — |
| MANAGER_ID | BillToBusinessUnitPEOManagerId3 | — |
| MANAGER_ID | BusinessUnitPEOManagerId2 | — |
| PRIMARY_LEDGER_ID | BillToBusinessUnitPEOPrimaryLedgerId2 | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId1 | — |
| PROFIT_CENTER_FLAG | BillToBusinessUnitPEOProfitCenterFlag1 | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BillToBusinessUnitPEOShortCode1 | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BillToBusinessUnitPEOStatus1 | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR · BICC: 2/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBusinessUnitPEOBusinessUnitId3 | — |
| BU_ID | BusinessUnitPEOBusinessUnitId2 | — |
| BU_NAME | BillToBusinessUnitPEOName1 | — |
| BU_NAME | BusinessUnitPEOName | — |
| BUSINESS_GROUP_ID | BillToBusinessUnitPEOEnterpriseId1 | — |
| BUSINESS_GROUP_ID | BusinessUnitPEOEnterpriseId | — |
| CREATED_BY | BillToBusinessUnitPEOCreatedBy25 | — |
| CREATED_BY | BusinessUnitPEOCreatedBy23 | — |
| CREATION_DATE | BillToBusinessUnitPEOCreationDate25 | — |
| CREATION_DATE | BusinessUnitPEOCreationDate23 | — |
| DATE_FROM | BillToBusinessUnitPEODateFrom1 | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BillToBusinessUnitPEODateTo1 | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBusinessUnitPEODefaultCurrencyCode1 | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBusinessUnitPEODefaultSetId1 | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBusinessUnitPEOEnabledForHrFlag1 | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBusinessUnitPEOFinancialsBusinessUnitId1 | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBusinessUnitPEOLastUpdateDate25 | ✅ |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate23 | ✅ |
| LAST_UPDATE_LOGIN | BillToBusinessUnitPEOLastUpdateLogin25 | — |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin23 | — |
| LAST_UPDATED_BY | BillToBusinessUnitPEOLastUpdatedBy25 | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy23 | — |
| LEGAL_ENTITY_ID | BillToBusinessUnitPEOLegalEntityId4 | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId3 | — |
| LOCATION_ID | BillToBusinessUnitPEOLocationId3 | — |
| LOCATION_ID | BusinessUnitPEOLocationId2 | — |
| MANAGER_ID | BillToBusinessUnitPEOManagerId3 | — |
| MANAGER_ID | BusinessUnitPEOManagerId2 | — |
| PRIMARY_LEDGER_ID | BillToBusinessUnitPEOPrimaryLedgerId2 | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId1 | — |
| PROFIT_CENTER_FLAG | BillToBusinessUnitPEOProfitCenterFlag1 | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BillToBusinessUnitPEOShortCode1 | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BillToBusinessUnitPEOStatus1 | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[receivingbuusagepvo|ReceivingBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[requisitionbuusagepvo|RequisitionBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | — |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | — |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ID | ManagerId | — |
| PRIMARY_LEDGER_ID | ReqBUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | ProfitCenterFlag | — |
| SHORT_CODE | ShortCode | — |
| STATUS | Status | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 2/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | — |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ID | ManagerId | — |
| PRIMARY_LEDGER_ID | ReqBUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | ProfitCenterFlag | — |
| SHORT_CODE | ShortCode | — |
| STATUS | Status | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | Name | — |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | — |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | — |
| MANAGER_ID | ManagerId | — |
| PRIMARY_LEDGER_ID | ReqBUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | ProfitCenterFlag | — |
| SHORT_CODE | ShortCode | — |
| STATUS | Status | — |

### [[revenuedistributionpvo|RevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | — |

### [[salesbuusagepvo|SalesBUUsagePVO]] (OTHER · BICC: 15/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | ✅ |
| BU_NAME | BusinessUnitName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitEnterpriseId | ✅ |
| DATE_FROM | BusinessUnitDateFrom | ✅ |
| DATE_TO | BusinessUnitDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BusinessUnitDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BusinessUnitDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BusinessUnitEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BusinessUnitFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BusinessUnitLastUpdateDate | — |
| LEGAL_ENTITY_ID | BusinessUnitLegalEntityId | ✅ |
| LOCATION_ID | BusinessUnitLocationId | ✅ |
| MANAGER_ID | BusinessUnitManagerId | ✅ |
| PRIMARY_LEDGER_ID | BusinessUnitPrimaryLedgerId | ✅ |
| SHORT_CODE | BusinessUnitShortCode | ✅ |
| STATUS | BusinessUnitStatus | ✅ |

### [[sponsoragreementspvo|SponsorAgreementsPVO]] (OTHER · BICC: 2/21)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitPEOBusinessUnitPEOBuId | — |
| BU_NAME | BusinessUnitPEOBuName | ✅ |
| BUSINESS_GROUP_ID | BusinessUnitPEOBusinessGroupId | — |
| CREATED_BY | BusinessUnitPEOCreatedBy | — |
| CREATION_DATE | BusinessUnitPEOCreationDate | — |
| DATE_FROM | BusinessUnitPEODateFrom | — |
| DATE_TO | BusinessUnitPEODateTo | — |
| DEFAULT_CURRENCY_CODE | BusinessUnitPEODefaultCurrencyCode | — |
| DEFAULT_SET_ID | BusinessUnitPEODefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BusinessUnitPEOEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BusinessUnitPEOFinBusinessUnitId | — |
| LAST_UPDATE_DATE | BusinessUnitPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BusinessUnitPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | BusinessUnitPEOLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BusinessUnitPEOLegalEntityId | — |
| LOCATION_ID | BusinessUnitPEOLocationId | — |
| MANAGER_ID | BusinessUnitPEOManagerId | — |
| PRIMARY_LEDGER_ID | BusinessUnitPEOPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BusinessUnitPEOProfitCenterFlag | — |
| SHORT_CODE | BusinessUnitPEOShortCode | — |
| STATUS | BusinessUnitPEOStatus | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | — |
| BU_NAME | FromContractHeaderPrcBuName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | — |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[standardheaderpvo|StandardHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| STATUS | BillToBUStatus | — |

### [[standardlinepvo|StandardLinePVO]] (PO · BICC: 4/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | ✅ |
| BU_NAME | FromContractHeaderPrcBuName | ✅ |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO · BICC: 2/61)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBUBusinessUnitId | — |
| BU_ID | FromBlanketHeaderPrcBuBusinessUnitId | — |
| BU_ID | FromContractHeaderPrcBuBusinessUnitId | — |
| BU_NAME | BillToBUName | — |
| BU_NAME | FromBlanketHeaderPrcBuName | ✅ |
| BU_NAME | FromContractHeaderPrcBuName | ✅ |
| BUSINESS_GROUP_ID | BillToBUEnterpriseId | — |
| BUSINESS_GROUP_ID | FromBlanketHeaderPrcBuEnterpriseId | — |
| BUSINESS_GROUP_ID | FromContractHeaderPrcBuEnterpriseId | — |
| CREATED_BY | BillToBUCreatedBy | — |
| CREATED_BY | FromBlanketHeaderPrcBuCreatedBy | — |
| CREATED_BY | FromContractHeaderPrcBuCreatedBy | — |
| CREATION_DATE | BillToBUCreationDate | — |
| CREATION_DATE | FromBlanketHeaderPrcBuCreationDate | — |
| CREATION_DATE | FromContractHeaderPrcBuCreationDate | — |
| DATE_FROM | BillToBUDateFrom | — |
| DATE_FROM | FromBlanketHeaderPrcBuDateFrom | — |
| DATE_FROM | FromContractHeaderPrcBuDateFrom | — |
| DATE_TO | BillToBUDateTo | — |
| DATE_TO | FromBlanketHeaderPrcBuDateTo | — |
| DATE_TO | FromContractHeaderPrcBuDateTo | — |
| DEFAULT_CURRENCY_CODE | BillToBUDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromBlanketHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_CURRENCY_CODE | FromContractHeaderPrcBuDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BillToBUDefaultSetId | — |
| DEFAULT_SET_ID | FromBlanketHeaderPrcBuDefaultSetId | — |
| DEFAULT_SET_ID | FromContractHeaderPrcBuDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BillToBUEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromBlanketHeaderPrcBuEnabledForHrFlag | — |
| ENABLED_FOR_HR_FLAG | FromContractHeaderPrcBuEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BillToBUFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromBlanketHeaderPrcBuFinancialsBusinessUnitId | — |
| FIN_BUSINESS_UNIT_ID | FromContractHeaderPrcBuFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BillToBULastUpdateDate | — |
| LAST_UPDATE_DATE | FromBlanketHeaderPrcBuLastUpdateDate | — |
| LAST_UPDATE_DATE | FromContractHeaderPrcBuLastUpdateDate | — |
| LAST_UPDATE_LOGIN | BillToBULastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromBlanketHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | FromContractHeaderPrcBuLastUpdateLogin | — |
| LAST_UPDATED_BY | BillToBULastUpdatedBy | — |
| LAST_UPDATED_BY | FromBlanketHeaderPrcBuLastUpdatedBy | — |
| LAST_UPDATED_BY | FromContractHeaderPrcBuLastUpdatedBy | — |
| LEGAL_ENTITY_ID | BillToBULegalEntityId | — |
| LEGAL_ENTITY_ID | FromBlanketHeaderPrcBuLegalEntityId | — |
| LEGAL_ENTITY_ID | FromContractHeaderPrcBuLegalEntityId | — |
| LOCATION_ID | BillToBULocationId | — |
| LOCATION_ID | FromBlanketHeaderPrcBuLocationId | — |
| LOCATION_ID | FromContractHeaderPrcBuLocationId | — |
| MANAGER_ID | BillToBUManagerId | — |
| MANAGER_ID | FromBlanketHeaderPrcBuManagerId | — |
| MANAGER_ID | FromContractHeaderPrcBuManagerId | — |
| PRIMARY_LEDGER_ID | BillToBUPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromBlanketHeaderPrcBuPrimaryLedgerId | — |
| PRIMARY_LEDGER_ID | FromContractHeaderPrcBuPrimaryLedgerId | — |
| PROFIT_CENTER_FLAG | BillToBUProfitCenterFlag | — |
| SHORT_CODE | BillToBUShortCode | — |
| SHORT_CODE | FromBlanketHeaderPrcBuShortCode | — |
| SHORT_CODE | FromContractHeaderPrcBuShortCode | — |
| STATUS | BillToBUStatus | — |
| STATUS | FromBlanketHeaderPrcBuStatus | — |
| STATUS | FromContractHeaderPrcBuStatus | — |

### [[stepinstance|StepInstance]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[stepinstancedetail|StepInstanceDetail]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[supplierregistrationmappingpvo|SupplierRegistrationMappingPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | ✅ |

### [[suppliersiteassignmentspvo|SupplierSiteAssignmentsPVO]] (PO · BICC: 40/40)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BillToBuBusinessUnitId | ✅ |
| BU_ID | ClientBuBusinessUnitId | ✅ |
| BU_NAME | BillToBuName | ✅ |
| BU_NAME | ClientBuName | ✅ |
| BUSINESS_GROUP_ID | BillToBuEnterpriseId | ✅ |
| BUSINESS_GROUP_ID | ClientBuEnterpriseId | ✅ |
| CREATED_BY | BillToBuCreatedBy | ✅ |
| CREATED_BY | ClientBuCreatedBy | ✅ |
| CREATION_DATE | BillToBuCreationDate | ✅ |
| CREATION_DATE | ClientBuCreationDate | ✅ |
| DATE_FROM | BillToBuDateFrom | ✅ |
| DATE_FROM | ClientBuDateFrom | ✅ |
| DATE_TO | BillToBuDateTo | ✅ |
| DATE_TO | ClientBuDateTo | ✅ |
| DEFAULT_CURRENCY_CODE | BillToBuDefaultCurrencyCode | ✅ |
| DEFAULT_CURRENCY_CODE | ClientBuDefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | BillToBuDefaultSetId | ✅ |
| DEFAULT_SET_ID | ClientBuDefaultSetId | ✅ |
| ENABLED_FOR_HR_FLAG | BillToBuEnabledForHrFlag | ✅ |
| ENABLED_FOR_HR_FLAG | ClientBuEnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | BillToBuFinancialsBusinessUnitId | ✅ |
| FIN_BUSINESS_UNIT_ID | ClientBuFinancialsBusinessUnitId | ✅ |
| LAST_UPDATE_DATE | BillToBuLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | ClientBuLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BillToBuLastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN | ClientBuLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | BillToBuLastUpdatedBy | ✅ |
| LAST_UPDATED_BY | ClientBuLastUpdatedBy | ✅ |
| LEGAL_ENTITY_ID | BillToBuLegalEntityId | ✅ |
| LEGAL_ENTITY_ID | ClientBuLegalEntityId | ✅ |
| LOCATION_ID | BillToBuLocationId | ✅ |
| LOCATION_ID | ClientBuLocationId | ✅ |
| MANAGER_ID | BillToBuManagerId | ✅ |
| MANAGER_ID | ClientBuManagerId | ✅ |
| PRIMARY_LEDGER_ID | BillToBuPrimaryLedgerId | ✅ |
| PRIMARY_LEDGER_ID | ClientBuPrimaryLedgerId | ✅ |
| SHORT_CODE | BillToBuShortCode | ✅ |
| SHORT_CODE | ClientBuShortCode | ✅ |
| STATUS | BillToBuStatus | ✅ |
| STATUS | ClientBuStatus | ✅ |

### [[suppliersitepvo|SupplierSitePVO]] (PO · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BUName | ✅ |
| BUSINESS_GROUP_ID | BUEnterpriseId | — |
| CREATED_BY | BUCreatedBy | — |
| CREATION_DATE | BUCreationDate | — |
| DATE_FROM | BUDateFrom | — |
| DATE_TO | BUDateTo | — |
| DEFAULT_CURRENCY_CODE | BUDefaultCurrencyCode | — |
| DEFAULT_SET_ID | BUDefaultSetId | — |
| ENABLED_FOR_HR_FLAG | BUEnabledForHrFlag | — |
| FIN_BUSINESS_UNIT_ID | BUFinancialsBusinessUnitId | — |
| LAST_UPDATE_DATE | BULastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | BULastUpdateLogin | — |
| LAST_UPDATED_BY | BULastUpdatedBy | — |
| LEGAL_ENTITY_ID | BULegalEntityId | — |
| LOCATION_ID | BULocationId | — |
| MANAGER_ID | BUManagerId | — |
| PRIMARY_LEDGER_ID | BUPrimaryLedgerId | — |
| SHORT_CODE | BUShortCode | ✅ |
| STATUS | BUStatus | — |

### [[supplierspendauthorizationrequestspvo|SupplierSpendAuthorizationRequestsPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |
| BU_NAME | BUName | ✅ |

### [[supplierthirdpartypaymentpvo|SupplierThirdPartyPaymentPVO]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitBusinessUnitId | — |
| BU_NAME | BusinessUnitName | ✅ |

### [[taskinstance|TaskInstance]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BUBusinessUnitId | — |

### [[transaction|Transaction]] (OTHER · BICC: 9/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| BU_NAME | BusinessUnitPEOName | ✅ |
| BUSINESS_GROUP_ID | EnterpriseId | — |
| DATE_FROM | DateFrom | ✅ |
| DATE_TO | DateTo | ✅ |
| DEFAULT_CURRENCY_CODE | DefaultCurrencyCode | ✅ |
| DEFAULT_SET_ID | DefaultSetId | — |
| ENABLED_FOR_HR_FLAG | EnabledForHrFlag | ✅ |
| FIN_BUSINESS_UNIT_ID | FinancialsBusinessUnitId | — |
| LEGAL_ENTITY_ID | LegalEntityId | — |
| LOCATION_ID | LocationId | ✅ |
| MANAGER_ID | ManagerId | ✅ |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
| SHORT_CODE | ShortCode | ✅ |
| STATUS | Status | ✅ |

### [[unlockednegotiationresponselinepvo|UnlockedNegotiationResponseLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_ID | BusinessUnitId | — |
| PRIMARY_LEDGER_ID | PrimaryLedgerId | — |
