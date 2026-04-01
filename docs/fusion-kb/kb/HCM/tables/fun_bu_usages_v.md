---
id: DOC-HCM-151
doc_type: system-doc
title: "FUN_BU_USAGES_V — (título a preencher)"
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
  - FUN_BU_USAGES_V
  - fun_bu_usages_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FUN_BU_USAGES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BUSINESS_UNIT_ID | — | — | — | — | — | — |
| 2 | BU_NAME | — | — | — | — | — | — |
| 3 | CONFIGURATION_STATUS | — | — | — | — | — | — |
| 4 | MODULE_ID | — | — | — | — | — | — |
| 5 | MODULE_KEY | — | — | — | — | — | — |
| 6 | MODULE_NAME | — | — | — | — | — | — |
| 7 | SHORT_CODE | — | — | — | — | — | — |
| 8 | STATUS | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[allbuyerpvo|AllBuyerPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | — |
| BUSINESS_UNIT_ID | BusinessUnitUsageBusinessUnitId | — |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | — |
| MODULE_ID | BusinessUnitUsageModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | — |
| MODULE_NAME | BusinessUnitUsageModuleName | — |
| SHORT_CODE | BusinessUnitUsageShortCode | — |
| STATUS | BusinessUnitUsageStatus | — |

### [[billingandrevenuebuusagepvo|BillingAndRevenueBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[businessunitusagepvo|BusinessUnitUsagePVO]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | — |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | — |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | — |
| MODULE_NAME | BusinessUnitUsageModuleName | — |
| SHORT_CODE | BusinessUnitUsageShortCode | — |
| STATUS | BusinessUnitUsageStatus | — |

### [[collectionbuusagepvo|CollectionBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[customercontractbuusagepvo|CustomerContractBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[customerpaymentsbuusagepvo|CustomerPaymentsBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[expensebuusagepvo|ExpenseBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[incentivecompensationbuusagepvo|IncentiveCompensationBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[materialmanagementbuusagepvo|MaterialManagementBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[payablesinvoicingbuusagepvo|PayablesInvoicingBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[payablespaymentsbuusagepvo|PayablesPaymentsBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[procurementbuusagepvo|ProcurementBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[procurementcontractbuusagepvo|ProcurementContractBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[projectaccountingbuusagepvo|ProjectAccountingBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[receivingbuusagepvo|ReceivingBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[requisitionbuusagepvo|RequisitionBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |

### [[salesbuusagepvo|SalesBUUsagePVO]] (OTHER · BICC: 7/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BU_NAME | BusinessUnitUsageName | ✅ |
| BUSINESS_UNIT_ID | BusinessUnitId | ✅ |
| CONFIGURATION_STATUS | BusinessUnitUsageConfigurationStatus | ✅ |
| MODULE_ID | ModuleId | — |
| MODULE_KEY | BusinessUnitUsageModuleKey | ✅ |
| MODULE_NAME | BusinessUnitUsageModuleName | ✅ |
| SHORT_CODE | BusinessUnitUsageShortCode | ✅ |
| STATUS | BusinessUnitUsageStatus | ✅ |
