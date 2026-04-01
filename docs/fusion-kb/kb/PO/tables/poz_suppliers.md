---
id: DOC-PO-088
doc_type: system-doc
title: "POZ_SUPPLIERS — Cadastro Principal de Fornecedores"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - suppliers
  - fornecedores
  - cadastro-mestre
aliases:
  - POZ_SUPPLIERS
  - poz_suppliers
  - cadastro-fornecedores
  - supplier-master
  - fornecedores-fusion
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POZ_SUPPLIERS

## Visão Geral

Tabela **mestre de fornecedores** do Oracle Fusion Procurement. Armazena o cadastro principal de todos os fornecedores da organização, incluindo dados de identificação, classificação, status e vínculo com o Trading Community Architecture (TCA). É a tabela central do módulo de Supplier Management, referenciada por praticamente todas as transações de compras e contas a pagar.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cadastro mestre:** Registro centralizado de todos os fornecedores (nacionais e internacionais).
- **Pedidos de compra:** Referência obrigatória em todos os POs — identifica o fornecedor da transação.
- **Contas a pagar:** Vínculo com faturas (AP Invoices) para processamento de pagamentos.
- **Qualificação:** Base para processos de qualificação, homologação e avaliação de fornecedores.
- **Sourcing:** Identificação de fornecedores elegíveis para negociações e cotações.
- **Relatórios e analytics:** Dimensão principal em análises de gastos (Spend Analysis).
- **Integração TCA:** Ponte entre o cadastro de procurement e o Trading Community Architecture (HZ_PARTIES).

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VENDOR_ID | NUMBER(18) | NOT NULL | PK | Identificador único do fornecedor | — | 🟢 95% |
| 2 | VENDOR_NAME | VARCHAR2(360) | NOT NULL | Identificação | Razão social / nome do fornecedor | — | 🟢 95% |
| 3 | SEGMENT1 | VARCHAR2(30) | NOT NULL | Identificação | Número do fornecedor (código visível ao usuário) | — | 🟢 95% |
| 4 | VENDOR_TYPE_LOOKUP_CODE | VARCHAR2(30) | NULL | Classificação | Tipo do fornecedor: VENDOR, EMPLOYEE, TAX_AUTHORITY, etc. | — | 🟢 90% |
| 5 | PARTY_ID | NUMBER(18) | NOT NULL | FK | Identificador do party no TCA | [[hz_parties]] | 🟢 90% |
| 6 | ENABLED_FLAG | VARCHAR2(1) | NOT NULL | Status | Fornecedor ativo (Y/N) | — | 🟢 90% |
| 7 | START_DATE_ACTIVE | DATE | NULL | Vigência | Data de início de atividade do fornecedor | — | 🟢 85% |
| 8 | END_DATE_ACTIVE | DATE | NULL | Vigência | Data de encerramento de atividade | — | 🟢 85% |
| 9 | BUSINESS_RELATIONSHIP | VARCHAR2(30) | NULL | Classificação | Tipo de relacionamento: SPEND_AUTHORIZED, NOT_AUTHORIZED | — | 🟡 75% |
| 10 | TAX_ORGANIZATION_TYPE_CODE | VARCHAR2(30) | NULL | Fiscal | Tipo de organização fiscal | — | 🟡 70% |
| 11 | FEDERAL_REPORTABLE_FLAG | VARCHAR2(1) | NULL | Fiscal | Sujeito a reporte federal (Y/N) — contexto US | — | 🟡 70% |
| 12 | STANDARD_INDUSTRY_CLASS | VARCHAR2(25) | NULL | Classificação | Código SIC (Standard Industry Classification) | — | 🟡 70% |
| 13 | ONE_TIME_FLAG | VARCHAR2(1) | NULL | Classificação | Fornecedor de uso único (Y/N) | — | 🟡 75% |
| 14 | PARENT_VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor-pai (hierarquia de fornecedores) | [[poz_suppliers]] | 🟡 70% |
| 15 | CUSTOMER_NUM | VARCHAR2(25) | NULL | Referência cruzada | Número de cliente do fornecedor (reciprocidade) | — | 🟡 65% |
| 16 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 17 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 18 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 19 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 20 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |
| 21 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hz_parties]] — via `PARTY_ID` (entidade TCA — nome, endereço, CNPJ/CPF)
- [[poz_suppliers]] — via `PARENT_VENDOR_ID` (auto-referência para hierarquia)

### Tabelas-filha (FK de saída)

### Views

---

## Uso Típico

### Buscar fornecedor por número ou nome
```sql
SELECT s.VENDOR_ID, s.SEGMENT1 AS vendor_number,
       s.VENDOR_NAME, s.VENDOR_TYPE_LOOKUP_CODE,
       s.ENABLED_FLAG
FROM   POZ_SUPPLIERS s
WHERE  s.SEGMENT1 = :p_vendor_number
   OR  UPPER(s.VENDOR_NAME) LIKE UPPER(:p_search || '%');
```

### Fornecedores ativos com spend autorizado
```sql
SELECT s.VENDOR_ID, s.SEGMENT1, s.VENDOR_NAME,
       s.BUSINESS_RELATIONSHIP
FROM   POZ_SUPPLIERS s
WHERE  s.ENABLED_FLAG = 'Y'
  AND  s.BUSINESS_RELATIONSHIP = 'SPEND_AUTHORIZED'
  AND  (s.END_DATE_ACTIVE IS NULL OR s.END_DATE_ACTIVE > SYSDATE);
```

### Filtros comuns
- `ENABLED_FLAG = 'Y'` — Fornecedores ativos
- `VENDOR_TYPE_LOOKUP_CODE = 'VENDOR'` — Apenas fornecedores (excluindo funcionários, autoridades fiscais)
- `ONE_TIME_FLAG = 'N'` — Excluir fornecedores de uso único

---

## Observações

- Esta é a **tabela mais referenciada** do módulo Procurement — alterações no `VENDOR_ID` impactam praticamente todo o ecossistema de compras e pagamentos.
- O `PARTY_ID` vincula o fornecedor ao **TCA (Trading Community Architecture)**, onde ficam dados como CNPJ/CPF, endereço fiscal e informações de partido.
- O campo `BUSINESS_RELATIONSHIP` controla se o fornecedor está autorizado para gastos (`SPEND_AUTHORIZED`) ou apenas registrado.
- Dados sensíveis como CPF/CNPJ do representante legal ficam na tabela separada `POZ_SUPPLIERS_PII`.
- O `SEGMENT1` é o **número do fornecedor** visível ao usuário; pode ser sequencial ou seguir regra de numeração customizada.
- Fornecedores com `ONE_TIME_FLAG = 'Y'` são tipicamente usados para pagamentos pontuais e não participam de processos de sourcing.

---

## Referências

- [Oracle Docs — POZ_SUPPLIERS](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/pozsuppliers-25316.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement

---

## 🔗 PVOs Relacionados

### [[maintenanceworkorderpvo|MaintenanceWorkOrderPVO]] (OTHER · BICC: 15/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_TAX_CALC_FLAG | SupplierPEOAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierPEOAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierPEOAwtGroupId | ✅ |
| BANK_CHARGE_BEARER | SupplierPEOBankChargeBearer | — |
| BC_NOT_APPLICABLE_FLAG | SupplierPEOBcNotApplicableFlag | — |
| BUSINESS_RELATIONSHIP | SupplierPEOBusinessRelationship | — |
| CHANGE_REQ_NUMBER | SupplierPEOChangeReqNumber | — |
| CORPORATE_WEBSITE | SupplierPEOCorporateWebsite | — |
| CREATED_BY | SupplierPEOCreatedBy1 | — |
| CREATION_DATE | SupplierPEOCreationDate1 | ✅ |
| CREATION_SOURCE | SupplierPEOCreationSource | — |
| CUSTOMER_NUM | SupplierPEOCustomerNum | — |
| EMPLOYEE_ID | SupplierPEOEmployeeId | ✅ |
| ENABLED_FLAG | SupplierPEOEnabledFlag1 | — |
| END_DATE_ACTIVE | SupplierPEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierPEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | SupplierPEOGlobalAttribute110 | — |
| GLOBAL_ATTRIBUTE10 | SupplierPEOGlobalAttribute101 | — |
| GLOBAL_ATTRIBUTE11 | SupplierPEOGlobalAttribute111 | — |
| GLOBAL_ATTRIBUTE12 | SupplierPEOGlobalAttribute121 | — |
| GLOBAL_ATTRIBUTE13 | SupplierPEOGlobalAttribute131 | — |
| GLOBAL_ATTRIBUTE14 | SupplierPEOGlobalAttribute141 | — |
| GLOBAL_ATTRIBUTE15 | SupplierPEOGlobalAttribute151 | — |
| GLOBAL_ATTRIBUTE16 | SupplierPEOGlobalAttribute161 | — |
| GLOBAL_ATTRIBUTE17 | SupplierPEOGlobalAttribute171 | — |
| GLOBAL_ATTRIBUTE18 | SupplierPEOGlobalAttribute181 | — |
| GLOBAL_ATTRIBUTE19 | SupplierPEOGlobalAttribute191 | — |
| GLOBAL_ATTRIBUTE2 | SupplierPEOGlobalAttribute21 | — |
| GLOBAL_ATTRIBUTE20 | SupplierPEOGlobalAttribute201 | — |
| GLOBAL_ATTRIBUTE3 | SupplierPEOGlobalAttribute31 | — |
| GLOBAL_ATTRIBUTE4 | SupplierPEOGlobalAttribute41 | — |
| GLOBAL_ATTRIBUTE5 | SupplierPEOGlobalAttribute51 | — |
| GLOBAL_ATTRIBUTE6 | SupplierPEOGlobalAttribute61 | — |
| GLOBAL_ATTRIBUTE7 | SupplierPEOGlobalAttribute71 | — |
| GLOBAL_ATTRIBUTE8 | SupplierPEOGlobalAttribute81 | — |
| GLOBAL_ATTRIBUTE9 | SupplierPEOGlobalAttribute91 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierPEOGlobalAttributeCategory1 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierPEOGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierPEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierPEOGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierPEOGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierPEOGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierPEOGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierPEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierPEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierPEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierPEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierPEOGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierPEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierPEOGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierPEOGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierPEOGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierPEOGlobalAttributeNumber5 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierPEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierPEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierPEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierPEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierPEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierPEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierPEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierPEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierPEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierPEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierPEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierPEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierPEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierPEOGlobalAttributeTimestamp9 | — |
| INCOME_TAX_ID_FLAG | SupplierPEOIncomeTaxIdFlag | — |
| JOB_DEFINITION_NAME | SupplierPEOJobDefinitionName1 | — |
| JOB_DEFINITION_PACKAGE | SupplierPEOJobDefinitionPackage1 | — |
| LAST_UPDATE_DATE | SupplierPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | SupplierPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | SupplierPEOLastUpdatedBy1 | — |
| MIN_ORDER_AMOUNT | SupplierPEOMinOrderAmount | — |
| MINORITY_GROUP_LOOKUP_CODE | SupplierPEOMinorityGroupLookupCode | — |
| NAME_CONTROL | SupplierPEONameControl | — |
| NI_NUMBER | SupplierPEONiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierPEOObjectVersionNumber1 | — |
| OFFSET_TAX_FLAG | SupplierPEOOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierPEOOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierPEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierPEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierPEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | SupplierPEOParentVendorId | ✅ |
| PARTY_ID | SupplierPEOPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierPEOProgramApplicationId | ✅ |
| PROGRAM_ID | SupplierPEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SupplierPEOProgramUpdateDate | ✅ |
| REQUEST_ID | SupplierPEORequestId1 | ✅ |
| SEGMENT1 | SupplierPEOSegment11 | — |
| SET_OF_BOOKS_ID | SupplierPEOSetOfBooksId | ✅ |
| SMALL_BUSINESS_FLAG | SupplierPEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | SupplierPEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierPEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierPEOStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierPEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierPEOStateReportableFlag | — |
| SUMMARY_FLAG | SupplierPEOSummaryFlag1 | — |
| SUPPLIER_LOCKED_FLAG | SupplierPEOSupplierLockedFlag | — |
| TAX_REPORTING_NAME | SupplierPEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierPEOTaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | SupplierPEOTaxpayerCountry | — |
| TYPE_1099 | SupplierPEOType1099 | — |
| VAT_CODE | SupplierPEOVatCode | — |
| VAT_REGISTRATION_NUM | SupplierPEOVatRegistrationNum | — |
| VENDOR_ID | SupplierPEOVendorId1 | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierPEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierPEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierPEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | SupplierPEOWomenOwnedFlag | — |

### [[projectplanlinebudgetpvo|ProjectPlanLineBudgetPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEGMENT1 | SupplierForRbsElementVendorSegment1 | ✅ |
| TAX_REPORTING_NAME | SupplierForRbsElementVendorTaxReportingName | — |
| VENDOR_ID | SupplierForRbsElementVendorVendorId | — |

### [[projectplanlinedetailbudgetpvo|ProjectPlanLineDetailBudgetPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEGMENT1 | SupplierForRbsElementVendorSegment1 | ✅ |
| TAX_REPORTING_NAME | SupplierForRbsElementVendorTaxReportingName | — |
| VENDOR_ID | SupplierForRbsElementVendorVendorId | — |

### [[projectplanlineforecastpvo|ProjectPlanLineForecastPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEGMENT1 | SupplierForRbsElementVendorSegment1 | ✅ |
| TAX_REPORTING_NAME | SupplierForRbsElementVendorTaxReportingName | — |
| VENDOR_ID | SupplierForRbsElementVendorVendorId | — |

### [[projplanlinedetailforecastpvo|ProjPlanLineDetailForecastPVO]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| SEGMENT1 | SupplierForRbsElementVendorSegment1 | ✅ |
| TAX_REPORTING_NAME | SupplierForRbsElementVendorTaxReportingName | — |
| VENDOR_ID | SupplierForRbsElementVendorVendorId | — |

### [[supplieraddressbankaccountpvo|SupplierAddressBankAccountPVO]] (PO · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | — |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | — |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | — |
| CREATED_BY | SupplierCreatedBy | — |
| CREATION_DATE | SupplierCreationDate | — |
| CREATION_SOURCE | SupplierCreationSource | — |
| CUSTOMER_NUM | SupplierCustomerNum | — |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | — |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | — |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | — |
| NI_NUMBER | SupplierNiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | — |
| PARTY_ID | SupplierPartyId | — |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| REVIEW_TYPE | SupplierReviewType | — |
| SEGMENT1 | SupplierSegment1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | — |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | — |
| TYPE_1099 | SupplierType1099 | — |
| VAT_CODE | SupplierVatCode | — |
| VENDOR_ID | SupplierVendorId | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[supplierbankaccountpvo|SupplierBankAccountPVO]] (PO · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | — |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | — |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | — |
| CREATED_BY | SupplierCreatedBy | — |
| CREATION_DATE | SupplierCreationDate | — |
| CREATION_SOURCE | SupplierCreationSource | — |
| CUSTOMER_NUM | SupplierCustomerNum | — |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | — |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | — |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | — |
| NI_NUMBER | SupplierNiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | — |
| PARTY_ID | SupplierPartyId | — |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| REVIEW_TYPE | SupplierReviewType | — |
| SEGMENT1 | SupplierSegment1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | — |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | — |
| TYPE_1099 | SupplierType1099 | — |
| VAT_CODE | SupplierVatCode | — |
| VENDOR_ID | SupplierVendorId | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[supplierextractpvo|SupplierExtractPVO]] (PO · BICC: 35/136)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | AllowAwtFlag | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | ✅ |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| AWT_GROUP_ID | AwtGroupId | ✅ |
| BC_NOT_APPLICABLE_FLAG | BcNotApplicableFlag | ✅ |
| BUSINESS_RELATIONSHIP | BusinessRelationship | ✅ |
| CORPORATE_WEBSITE | CorporateWebsite | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_SOURCE | CreationSource | ✅ |
| CUSTOMER_NUM | CustomerNum | ✅ |
| END_DATE_ACTIVE | EndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | FederalReportableFlag | ✅ |
| GLOBAL_ATTRIBUTE1 | GlobalAttribute1 | — |
| GLOBAL_ATTRIBUTE10 | GlobalAttribute10 | — |
| GLOBAL_ATTRIBUTE11 | GlobalAttribute11 | — |
| GLOBAL_ATTRIBUTE12 | GlobalAttribute12 | — |
| GLOBAL_ATTRIBUTE13 | GlobalAttribute13 | — |
| GLOBAL_ATTRIBUTE14 | GlobalAttribute14 | — |
| GLOBAL_ATTRIBUTE15 | GlobalAttribute15 | — |
| GLOBAL_ATTRIBUTE16 | GlobalAttribute16 | — |
| GLOBAL_ATTRIBUTE17 | GlobalAttribute17 | — |
| GLOBAL_ATTRIBUTE18 | GlobalAttribute18 | — |
| GLOBAL_ATTRIBUTE19 | GlobalAttribute19 | — |
| GLOBAL_ATTRIBUTE2 | GlobalAttribute2 | — |
| GLOBAL_ATTRIBUTE20 | GlobalAttribute20 | — |
| GLOBAL_ATTRIBUTE3 | GlobalAttribute3 | — |
| GLOBAL_ATTRIBUTE4 | GlobalAttribute4 | — |
| GLOBAL_ATTRIBUTE5 | GlobalAttribute5 | — |
| GLOBAL_ATTRIBUTE6 | GlobalAttribute6 | — |
| GLOBAL_ATTRIBUTE7 | GlobalAttribute7 | — |
| GLOBAL_ATTRIBUTE8 | GlobalAttribute8 | — |
| GLOBAL_ATTRIBUTE9 | GlobalAttribute9 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | GlobalAttributeCategory | — |
| GLOBAL_ATTRIBUTE_DATE1 | GlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE10 | GlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | GlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | GlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | GlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | GlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_DATE6 | GlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | GlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | GlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | GlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | GlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | GlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | GlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | GlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | GlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | GlobalAttributeNumber5 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | GlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | GlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | GlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | GlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | GlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | GlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | GlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | GlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | GlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | GlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | GlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | GlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | GlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | GlobalAttributeTimestamp9 | — |
| INCOME_TAX_ID_FLAG | IncomeTaxIdFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME_CONTROL | NameControl | ✅ |
| NI_NUMBER_FLAG | NiNumberFlag | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| ONE_TIME_FLAG | OneTimeFlag | ✅ |
| ORGANIZATION_TYPE_LOOKUP_CODE | OrganizationTypeLookupCode | ✅ |
| PARENT_PARTY_ID | ParentPartyId | ✅ |
| PARENT_VENDOR_ID | ParentVendorId | ✅ |
| PARTY_ID | PartyId | ✅ |
| SEGMENT1 | Segment1 | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SpendAuthReviewStatus | ✅ |
| STANDARD_INDUSTRY_CLASS | StandardIndustryClass | ✅ |
| START_DATE_ACTIVE | StartDateActive | ✅ |
| STATE_REPORTABLE_FLAG | StateReportableFlag | ✅ |
| TAX_REPORTING_NAME | TaxReportingName | ✅ |
| TAX_VERIFICATION_DATE | TaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | TaxpayerCountry | ✅ |
| TYPE_1099 | Type1099 | ✅ |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | VendorTypeLookupCode | ✅ |

### [[supplierproductsservicespvo|SupplierProductsServicesPVO]] (PO · BICC: 2/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | — |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | — |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | — |
| CREATED_BY | SupplierCreatedBy | — |
| CREATION_DATE | SupplierCreationDate | — |
| CREATION_SOURCE | SupplierCreationSource | — |
| CUSTOMER_NUM | SupplierCustomerNum | — |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | — |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | — |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | — |
| NI_NUMBER | SupplierNiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | — |
| PARTY_ID | SupplierPartyId | — |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| REVIEW_TYPE | SupplierReviewType | — |
| SEGMENT1 | SupplierSegment1 | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | — |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | — |
| TYPE_1099 | SupplierType1099 | — |
| VAT_CODE | SupplierVatCode | — |
| VENDOR_ID | SupplierVendorId | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[supplierpvo|SupplierPVO]] (PO · BICC: 145/167)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | ✅ |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| ATTRIBUTE1 | SupplierAttribute1 | ✅ |
| ATTRIBUTE10 | SupplierAttribute10 | ✅ |
| ATTRIBUTE11 | SupplierAttribute11 | ✅ |
| ATTRIBUTE12 | SupplierAttribute12 | ✅ |
| ATTRIBUTE13 | SupplierAttribute13 | ✅ |
| ATTRIBUTE14 | SupplierAttribute14 | ✅ |
| ATTRIBUTE15 | SupplierAttribute15 | ✅ |
| ATTRIBUTE16 | SupplierAttribute16 | ✅ |
| ATTRIBUTE17 | SupplierAttribute17 | ✅ |
| ATTRIBUTE18 | SupplierAttribute18 | ✅ |
| ATTRIBUTE19 | SupplierAttribute19 | ✅ |
| ATTRIBUTE2 | SupplierAttribute2 | ✅ |
| ATTRIBUTE20 | SupplierAttribute20 | ✅ |
| ATTRIBUTE3 | SupplierAttribute3 | ✅ |
| ATTRIBUTE4 | SupplierAttribute4 | ✅ |
| ATTRIBUTE5 | SupplierAttribute5 | ✅ |
| ATTRIBUTE6 | SupplierAttribute6 | ✅ |
| ATTRIBUTE7 | SupplierAttribute7 | ✅ |
| ATTRIBUTE8 | SupplierAttribute8 | ✅ |
| ATTRIBUTE9 | SupplierAttribute9 | ✅ |
| ATTRIBUTE_CATEGORY | SupplierAttributeCategory | ✅ |
| ATTRIBUTE_DATE1 | SupplierAttributeDate1 | ✅ |
| ATTRIBUTE_DATE10 | SupplierAttributeDate10 | ✅ |
| ATTRIBUTE_DATE2 | SupplierAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | SupplierAttributeDate3 | ✅ |
| ATTRIBUTE_DATE4 | SupplierAttributeDate4 | ✅ |
| ATTRIBUTE_DATE5 | SupplierAttributeDate5 | ✅ |
| ATTRIBUTE_DATE6 | SupplierAttributeDate6 | ✅ |
| ATTRIBUTE_DATE7 | SupplierAttributeDate7 | ✅ |
| ATTRIBUTE_DATE8 | SupplierAttributeDate8 | ✅ |
| ATTRIBUTE_DATE9 | SupplierAttributeDate9 | ✅ |
| ATTRIBUTE_NUMBER1 | SupplierAttributeNumber1 | ✅ |
| ATTRIBUTE_NUMBER10 | SupplierAttributeNumber10 | ✅ |
| ATTRIBUTE_NUMBER2 | SupplierAttributeNumber2 | ✅ |
| ATTRIBUTE_NUMBER3 | SupplierAttributeNumber3 | ✅ |
| ATTRIBUTE_NUMBER4 | SupplierAttributeNumber4 | ✅ |
| ATTRIBUTE_NUMBER5 | SupplierAttributeNumber5 | ✅ |
| ATTRIBUTE_NUMBER6 | SupplierAttributeNumber6 | ✅ |
| ATTRIBUTE_NUMBER7 | SupplierAttributeNumber7 | ✅ |
| ATTRIBUTE_NUMBER8 | SupplierAttributeNumber8 | ✅ |
| ATTRIBUTE_NUMBER9 | SupplierAttributeNumber9 | ✅ |
| ATTRIBUTE_TIMESTAMP1 | SupplierAttributeTimestamp1 | ✅ |
| ATTRIBUTE_TIMESTAMP10 | SupplierAttributeTimestamp10 | ✅ |
| ATTRIBUTE_TIMESTAMP2 | SupplierAttributeTimestamp2 | ✅ |
| ATTRIBUTE_TIMESTAMP3 | SupplierAttributeTimestamp3 | ✅ |
| ATTRIBUTE_TIMESTAMP4 | SupplierAttributeTimestamp4 | ✅ |
| ATTRIBUTE_TIMESTAMP5 | SupplierAttributeTimestamp5 | ✅ |
| ATTRIBUTE_TIMESTAMP6 | SupplierAttributeTimestamp6 | ✅ |
| ATTRIBUTE_TIMESTAMP7 | SupplierAttributeTimestamp7 | ✅ |
| ATTRIBUTE_TIMESTAMP8 | SupplierAttributeTimestamp8 | ✅ |
| ATTRIBUTE_TIMESTAMP9 | SupplierAttributeTimestamp9 | ✅ |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | ✅ |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BC_NOT_APPLICABLE_FLAG | SupplierBcNotApplicableFlag | ✅ |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | ✅ |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | ✅ |
| CREATED_BY | SupplierCreatedBy | ✅ |
| CREATION_DATE | SupplierCreationDate | ✅ |
| CREATION_SOURCE | SupplierCreationSource | ✅ |
| CUSTOMER_NUM | SupplierCustomerNum | ✅ |
| DATAFOX_COMPANY_ID | DatafoxCompanyId | ✅ |
| DENIED_PARTY_FLAG | DeniedPartyFlag | — |
| DF_COMPANY_NAME | DfCompanyName | ✅ |
| DF_CORPORATE_WEBSITE | DfCorporateWebsite | ✅ |
| DF_INDUSTRY_CATEGORY_CODE | DfIndustryCategoryCode | ✅ |
| DF_INDUSTRY_SUB_CATEGORY_CODE | DfIndustrySubCategoryCode | ✅ |
| DF_LAST_SYNC_DATE | DfLastSyncDate | ✅ |
| DF_LEGAL_NAME | DfLegalName | ✅ |
| DF_NAICS_CODE | DfNaicsCode | ✅ |
| DF_SCORE | DfScore | ✅ |
| DF_TAXPAYER_COUNTRY | DfTaxpayerCountry | ✅ |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | ✅ |
| GLOBAL_ATTRIBUTE1 | SupplierGlobalAttribute1 | ✅ |
| GLOBAL_ATTRIBUTE10 | SupplierGlobalAttribute10 | ✅ |
| GLOBAL_ATTRIBUTE11 | SupplierGlobalAttribute11 | ✅ |
| GLOBAL_ATTRIBUTE12 | SupplierGlobalAttribute12 | ✅ |
| GLOBAL_ATTRIBUTE13 | SupplierGlobalAttribute13 | ✅ |
| GLOBAL_ATTRIBUTE14 | SupplierGlobalAttribute14 | ✅ |
| GLOBAL_ATTRIBUTE15 | SupplierGlobalAttribute15 | ✅ |
| GLOBAL_ATTRIBUTE16 | SupplierGlobalAttribute16 | ✅ |
| GLOBAL_ATTRIBUTE17 | SupplierGlobalAttribute17 | ✅ |
| GLOBAL_ATTRIBUTE18 | SupplierGlobalAttribute18 | ✅ |
| GLOBAL_ATTRIBUTE19 | SupplierGlobalAttribute19 | ✅ |
| GLOBAL_ATTRIBUTE2 | SupplierGlobalAttribute2 | ✅ |
| GLOBAL_ATTRIBUTE20 | SupplierGlobalAttribute20 | ✅ |
| GLOBAL_ATTRIBUTE3 | SupplierGlobalAttribute3 | ✅ |
| GLOBAL_ATTRIBUTE4 | SupplierGlobalAttribute4 | ✅ |
| GLOBAL_ATTRIBUTE5 | SupplierGlobalAttribute5 | ✅ |
| GLOBAL_ATTRIBUTE6 | SupplierGlobalAttribute6 | ✅ |
| GLOBAL_ATTRIBUTE7 | SupplierGlobalAttribute7 | ✅ |
| GLOBAL_ATTRIBUTE8 | SupplierGlobalAttribute8 | ✅ |
| GLOBAL_ATTRIBUTE9 | SupplierGlobalAttribute9 | ✅ |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierGlobalAttributeCategory | ✅ |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierGlobalAttributeDate1 | ✅ |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierGlobalAttributeDate10 | ✅ |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierGlobalAttributeDate2 | ✅ |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierGlobalAttributeDate3 | ✅ |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierGlobalAttributeDate4 | ✅ |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierGlobalAttributeDate5 | ✅ |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierGlobalAttributeDate6 | ✅ |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierGlobalAttributeDate7 | ✅ |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierGlobalAttributeDate8 | ✅ |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierGlobalAttributeDate9 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierGlobalAttributeNumber1 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierGlobalAttributeNumber10 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierGlobalAttributeNumber2 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierGlobalAttributeNumber3 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierGlobalAttributeNumber4 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierGlobalAttributeNumber5 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierGlobalAttributeNumber6 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierGlobalAttributeNumber7 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierGlobalAttributeNumber8 | ✅ |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierGlobalAttributeNumber9 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierGlobalAttributeTimestamp1 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierGlobalAttributeTimestamp10 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierGlobalAttributeTimestamp2 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierGlobalAttributeTimestamp3 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierGlobalAttributeTimestamp4 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierGlobalAttributeTimestamp5 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierGlobalAttributeTimestamp6 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierGlobalAttributeTimestamp7 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierGlobalAttributeTimestamp8 | ✅ |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierGlobalAttributeTimestamp9 | ✅ |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | ✅ |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | ✅ |
| NI_NUMBER_FLAG | SupplierNiNumberFlag | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OBN_MATCHED_STATUS | ObnMatchedStatus | ✅ |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | ✅ |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | ✅ |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | ✅ |
| PARTY_ID | SuppParentPartyId | — |
| PARTY_ID | SupplierPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| REVIEW_TYPE | SupplierReviewType | ✅ |
| SEGMENT1 | SuppParentSegment1 | ✅ |
| SEGMENT1 | SupplierSegment1 | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | ✅ |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | ✅ |
| START_DATE_ACTIVE | SupplierStartDateActive | ✅ |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | ✅ |
| TAX_REPORTING_NAME | SupplierTaxReportingName | ✅ |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | ✅ |
| TYPE_1099 | SupplierType1099 | ✅ |
| VAT_CODE | SupplierVatCode | ✅ |
| VENDOR_ID | SuppParentVendorId | — |
| VENDOR_ID | VendorId | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | ✅ |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[suppliersiteassignmentspvo|SupplierSiteAssignmentsPVO]] (PO · BICC: 49/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | ✅ |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | ✅ |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | ✅ |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | ✅ |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | ✅ |
| AWT_GROUP_ID | SupplierAwtGroupId | ✅ |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | ✅ |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | ✅ |
| CREATED_BY | SupplierCreatedBy | ✅ |
| CREATION_DATE | SupplierCreationDate | ✅ |
| CREATION_SOURCE | SupplierCreationSource | ✅ |
| CUSTOMER_NUM | SupplierCustomerNum | ✅ |
| EMPLOYEE_ID | SupplierEmployeeId | ✅ |
| END_DATE_ACTIVE | SupplierEndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | ✅ |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | ✅ |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | ✅ |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | ✅ |
| NAME_CONTROL | SupplierNameControl | ✅ |
| NI_NUMBER | SupplierNiNumber | ✅ |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | ✅ |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | ✅ |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | ✅ |
| ONE_TIME_FLAG | SupplierOneTimeFlag | ✅ |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | ✅ |
| PARENT_PARTY_ID | SupplierParentPartyId | ✅ |
| PARENT_VENDOR_ID | SupplierParentVendorId | ✅ |
| PARTY_ID | SupplierPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | ✅ |
| PROGRAM_ID | SupplierProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | ✅ |
| REQUEST_ID | SupplierRequestId | ✅ |
| REVIEW_TYPE | SupplierReviewType | ✅ |
| SEGMENT1 | SupplierSegment1 | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | ✅ |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | ✅ |
| START_DATE_ACTIVE | SupplierStartDateActive | ✅ |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | ✅ |
| TAX_REPORTING_NAME | SupplierTaxReportingName | ✅ |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | ✅ |
| TYPE_1099 | SupplierType1099 | ✅ |
| VAT_CODE | SupplierVatCode | ✅ |
| VENDOR_ID | SupplierVendorId | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | ✅ |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | ✅ |

### [[suppliersitebankaccountpvo|SupplierSiteBankAccountPVO]] (PO · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | — |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | — |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | — |
| CREATED_BY | SupplierCreatedBy | — |
| CREATION_DATE | SupplierCreationDate | — |
| CREATION_SOURCE | SupplierCreationSource | — |
| CUSTOMER_NUM | SupplierCustomerNum | — |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | — |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | — |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | — |
| NI_NUMBER | SupplierNiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | — |
| PARTY_ID | SupplierPartyId | — |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| REVIEW_TYPE | SupplierReviewType | — |
| SEGMENT1 | SupplierSegment1 | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | — |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | — |
| TYPE_1099 | SupplierType1099 | — |
| VAT_CODE | SupplierVatCode | — |
| VENDOR_ID | SupplierVendorId | — |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[suppliersitepvo|SupplierSitePVO]] (PO · BICC: 6/47)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_AWT_FLAG | SupplierAllowAwtFlag | ✅ |
| AMOUNT_INCLUDES_TAX_FLAG | SupplierAmountIncludesTaxFlag | — |
| AP_TAX_ROUNDING_RULE | SupplierApTaxRoundingRule | — |
| AUTO_TAX_CALC_FLAG | SupplierAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierAwtGroupId | — |
| BUSINESS_RELATIONSHIP | SupplierBusinessRelationship | — |
| CORPORATE_WEBSITE | SupplierCorporateWebsite | — |
| CREATED_BY | SupplierCreatedBy | — |
| CREATION_DATE | SupplierCreationDate | — |
| CUSTOMER_NUM | SupplierCustomerNum | — |
| EMPLOYEE_ID | SupplierEmployeeId | — |
| END_DATE_ACTIVE | SupplierEndDateActive | ✅ |
| FEDERAL_REPORTABLE_FLAG | SupplierFederalReportableFlag | — |
| INCOME_TAX_ID_FLAG | SupplierIncomeTaxIdFlag | — |
| LAST_UPDATE_DATE | SupplierLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | SupplierLastUpdateLogin | — |
| LAST_UPDATED_BY | SupplierLastUpdatedBy | — |
| MIN_ORDER_AMOUNT | SupplierMinOrderAmount | — |
| NAME_CONTROL | SupplierNameControl | — |
| NI_NUMBER | SupplierNiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierObjectVersionNumber | — |
| OFFSET_TAX_FLAG | SupplierOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierParentPartyId | — |
| PARENT_VENDOR_ID | SupplierParentVendorId | — |
| PARTY_ID | SupplierPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierProgramApplicationId | — |
| PROGRAM_ID | SupplierProgramId | — |
| PROGRAM_UPDATE_DATE | SupplierProgramUpdateDate | — |
| REQUEST_ID | SupplierRequestId | — |
| SEGMENT1 | SupplierSegment1 | ✅ |
| SPEND_AUTH_REVIEW_STATUS | SupplierSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierStateReportableFlag | — |
| TAX_REPORTING_NAME | SupplierTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierTaxVerificationDate | — |
| TAXPAYER_COUNTRY | SupplierTaxpayerCountry | — |
| TYPE_1099 | SupplierType1099 | — |
| VAT_CODE | SupplierVatCode | — |
| VENDOR_ID | SupplierVendorId | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierWithholdingStartDate | — |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierWithholdingStatusLookupCode | — |

### [[workorderpvo|WorkOrderPVO]] (OTHER · BICC: 15/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_TAX_CALC_FLAG | SupplierPEOAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierPEOAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierPEOAwtGroupId | ✅ |
| BANK_CHARGE_BEARER | SupplierPEOBankChargeBearer | — |
| BC_NOT_APPLICABLE_FLAG | SupplierPEOBcNotApplicableFlag | — |
| BUSINESS_RELATIONSHIP | SupplierPEOBusinessRelationship | — |
| CHANGE_REQ_NUMBER | SupplierPEOChangeReqNumber | — |
| CORPORATE_WEBSITE | SupplierPEOCorporateWebsite | — |
| CREATED_BY | SupplierPEOCreatedBy1 | — |
| CREATION_DATE | SupplierPEOCreationDate1 | ✅ |
| CREATION_SOURCE | SupplierPEOCreationSource | — |
| CUSTOMER_NUM | SupplierPEOCustomerNum | — |
| EMPLOYEE_ID | SupplierPEOEmployeeId | ✅ |
| ENABLED_FLAG | SupplierPEOEnabledFlag1 | — |
| END_DATE_ACTIVE | SupplierPEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierPEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | SupplierPEOGlobalAttribute110 | — |
| GLOBAL_ATTRIBUTE10 | SupplierPEOGlobalAttribute101 | — |
| GLOBAL_ATTRIBUTE11 | SupplierPEOGlobalAttribute111 | — |
| GLOBAL_ATTRIBUTE12 | SupplierPEOGlobalAttribute121 | — |
| GLOBAL_ATTRIBUTE13 | SupplierPEOGlobalAttribute131 | — |
| GLOBAL_ATTRIBUTE14 | SupplierPEOGlobalAttribute141 | — |
| GLOBAL_ATTRIBUTE15 | SupplierPEOGlobalAttribute151 | — |
| GLOBAL_ATTRIBUTE16 | SupplierPEOGlobalAttribute161 | — |
| GLOBAL_ATTRIBUTE17 | SupplierPEOGlobalAttribute171 | — |
| GLOBAL_ATTRIBUTE18 | SupplierPEOGlobalAttribute181 | — |
| GLOBAL_ATTRIBUTE19 | SupplierPEOGlobalAttribute191 | — |
| GLOBAL_ATTRIBUTE2 | SupplierPEOGlobalAttribute21 | — |
| GLOBAL_ATTRIBUTE20 | SupplierPEOGlobalAttribute201 | — |
| GLOBAL_ATTRIBUTE3 | SupplierPEOGlobalAttribute31 | — |
| GLOBAL_ATTRIBUTE4 | SupplierPEOGlobalAttribute41 | — |
| GLOBAL_ATTRIBUTE5 | SupplierPEOGlobalAttribute51 | — |
| GLOBAL_ATTRIBUTE6 | SupplierPEOGlobalAttribute61 | — |
| GLOBAL_ATTRIBUTE7 | SupplierPEOGlobalAttribute71 | — |
| GLOBAL_ATTRIBUTE8 | SupplierPEOGlobalAttribute81 | — |
| GLOBAL_ATTRIBUTE9 | SupplierPEOGlobalAttribute91 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierPEOGlobalAttributeCategory1 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierPEOGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierPEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierPEOGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierPEOGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierPEOGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierPEOGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierPEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierPEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierPEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierPEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierPEOGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierPEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierPEOGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierPEOGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierPEOGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierPEOGlobalAttributeNumber5 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierPEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierPEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierPEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierPEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierPEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierPEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierPEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierPEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierPEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierPEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierPEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierPEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierPEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierPEOGlobalAttributeTimestamp9 | — |
| INCOME_TAX_ID_FLAG | SupplierPEOIncomeTaxIdFlag | — |
| JOB_DEFINITION_NAME | SupplierPEOJobDefinitionName1 | — |
| JOB_DEFINITION_PACKAGE | SupplierPEOJobDefinitionPackage1 | — |
| LAST_UPDATE_DATE | SupplierPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | SupplierPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | SupplierPEOLastUpdatedBy1 | — |
| MIN_ORDER_AMOUNT | SupplierPEOMinOrderAmount | — |
| MINORITY_GROUP_LOOKUP_CODE | SupplierPEOMinorityGroupLookupCode | — |
| NAME_CONTROL | SupplierPEONameControl | — |
| NI_NUMBER | SupplierPEONiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierPEOObjectVersionNumber1 | — |
| OFFSET_TAX_FLAG | SupplierPEOOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierPEOOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierPEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierPEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierPEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | SupplierPEOParentVendorId | ✅ |
| PARTY_ID | SupplierPEOPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierPEOProgramApplicationId | ✅ |
| PROGRAM_ID | SupplierPEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SupplierPEOProgramUpdateDate | ✅ |
| REQUEST_ID | SupplierPEORequestId1 | ✅ |
| SEGMENT1 | SupplierPEOSegment11 | — |
| SET_OF_BOOKS_ID | SupplierPEOSetOfBooksId | ✅ |
| SMALL_BUSINESS_FLAG | SupplierPEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | SupplierPEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierPEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierPEOStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierPEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierPEOStateReportableFlag | — |
| SUMMARY_FLAG | SupplierPEOSummaryFlag1 | — |
| SUPPLIER_LOCKED_FLAG | SupplierPEOSupplierLockedFlag | — |
| TAX_REPORTING_NAME | SupplierPEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierPEOTaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | SupplierPEOTaxpayerCountry | — |
| TYPE_1099 | SupplierPEOType1099 | — |
| VAT_CODE | SupplierPEOVatCode | — |
| VAT_REGISTRATION_NUM | SupplierPEOVatRegistrationNum | — |
| VENDOR_ID | SupplierPEOVendorId1 | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierPEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierPEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierPEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | SupplierPEOWomenOwnedFlag | — |

### [[workorderrefpvo|WorkOrderRefPVO]] (OTHER · BICC: 15/110)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUTO_TAX_CALC_FLAG | SupplierPEOAutoTaxCalcFlag | — |
| AUTO_TAX_CALC_OVERRIDE | SupplierPEOAutoTaxCalcOverride | — |
| AWT_GROUP_ID | SupplierPEOAwtGroupId | ✅ |
| BANK_CHARGE_BEARER | SupplierPEOBankChargeBearer | — |
| BC_NOT_APPLICABLE_FLAG | SupplierPEOBcNotApplicableFlag | — |
| BUSINESS_RELATIONSHIP | SupplierPEOBusinessRelationship | — |
| CHANGE_REQ_NUMBER | SupplierPEOChangeReqNumber | — |
| CORPORATE_WEBSITE | SupplierPEOCorporateWebsite | — |
| CREATED_BY | SupplierPEOCreatedBy1 | — |
| CREATION_DATE | SupplierPEOCreationDate1 | ✅ |
| CREATION_SOURCE | SupplierPEOCreationSource | — |
| CUSTOMER_NUM | SupplierPEOCustomerNum | — |
| EMPLOYEE_ID | SupplierPEOEmployeeId | ✅ |
| ENABLED_FLAG | SupplierPEOEnabledFlag1 | — |
| END_DATE_ACTIVE | SupplierPEOEndDateActive | — |
| FEDERAL_REPORTABLE_FLAG | SupplierPEOFederalReportableFlag | — |
| GLOBAL_ATTRIBUTE1 | SupplierPEOGlobalAttribute110 | — |
| GLOBAL_ATTRIBUTE10 | SupplierPEOGlobalAttribute101 | — |
| GLOBAL_ATTRIBUTE11 | SupplierPEOGlobalAttribute111 | — |
| GLOBAL_ATTRIBUTE12 | SupplierPEOGlobalAttribute121 | — |
| GLOBAL_ATTRIBUTE13 | SupplierPEOGlobalAttribute131 | — |
| GLOBAL_ATTRIBUTE14 | SupplierPEOGlobalAttribute141 | — |
| GLOBAL_ATTRIBUTE15 | SupplierPEOGlobalAttribute151 | — |
| GLOBAL_ATTRIBUTE16 | SupplierPEOGlobalAttribute161 | — |
| GLOBAL_ATTRIBUTE17 | SupplierPEOGlobalAttribute171 | — |
| GLOBAL_ATTRIBUTE18 | SupplierPEOGlobalAttribute181 | — |
| GLOBAL_ATTRIBUTE19 | SupplierPEOGlobalAttribute191 | — |
| GLOBAL_ATTRIBUTE2 | SupplierPEOGlobalAttribute21 | — |
| GLOBAL_ATTRIBUTE20 | SupplierPEOGlobalAttribute201 | — |
| GLOBAL_ATTRIBUTE3 | SupplierPEOGlobalAttribute31 | — |
| GLOBAL_ATTRIBUTE4 | SupplierPEOGlobalAttribute41 | — |
| GLOBAL_ATTRIBUTE5 | SupplierPEOGlobalAttribute51 | — |
| GLOBAL_ATTRIBUTE6 | SupplierPEOGlobalAttribute61 | — |
| GLOBAL_ATTRIBUTE7 | SupplierPEOGlobalAttribute71 | — |
| GLOBAL_ATTRIBUTE8 | SupplierPEOGlobalAttribute81 | — |
| GLOBAL_ATTRIBUTE9 | SupplierPEOGlobalAttribute91 | — |
| GLOBAL_ATTRIBUTE_CATEGORY | SupplierPEOGlobalAttributeCategory1 | — |
| GLOBAL_ATTRIBUTE_DATE1 | SupplierPEOGlobalAttributeDate1 | — |
| GLOBAL_ATTRIBUTE_DATE10 | SupplierPEOGlobalAttributeDate10 | — |
| GLOBAL_ATTRIBUTE_DATE2 | SupplierPEOGlobalAttributeDate2 | — |
| GLOBAL_ATTRIBUTE_DATE3 | SupplierPEOGlobalAttributeDate3 | — |
| GLOBAL_ATTRIBUTE_DATE4 | SupplierPEOGlobalAttributeDate4 | — |
| GLOBAL_ATTRIBUTE_DATE5 | SupplierPEOGlobalAttributeDate5 | — |
| GLOBAL_ATTRIBUTE_DATE6 | SupplierPEOGlobalAttributeDate6 | — |
| GLOBAL_ATTRIBUTE_DATE7 | SupplierPEOGlobalAttributeDate7 | — |
| GLOBAL_ATTRIBUTE_DATE8 | SupplierPEOGlobalAttributeDate8 | — |
| GLOBAL_ATTRIBUTE_DATE9 | SupplierPEOGlobalAttributeDate9 | — |
| GLOBAL_ATTRIBUTE_NUMBER1 | SupplierPEOGlobalAttributeNumber1 | — |
| GLOBAL_ATTRIBUTE_NUMBER10 | SupplierPEOGlobalAttributeNumber10 | — |
| GLOBAL_ATTRIBUTE_NUMBER2 | SupplierPEOGlobalAttributeNumber2 | — |
| GLOBAL_ATTRIBUTE_NUMBER3 | SupplierPEOGlobalAttributeNumber3 | — |
| GLOBAL_ATTRIBUTE_NUMBER4 | SupplierPEOGlobalAttributeNumber4 | — |
| GLOBAL_ATTRIBUTE_NUMBER5 | SupplierPEOGlobalAttributeNumber5 | — |
| GLOBAL_ATTRIBUTE_NUMBER6 | SupplierPEOGlobalAttributeNumber6 | — |
| GLOBAL_ATTRIBUTE_NUMBER7 | SupplierPEOGlobalAttributeNumber7 | — |
| GLOBAL_ATTRIBUTE_NUMBER8 | SupplierPEOGlobalAttributeNumber8 | — |
| GLOBAL_ATTRIBUTE_NUMBER9 | SupplierPEOGlobalAttributeNumber9 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP1 | SupplierPEOGlobalAttributeTimestamp1 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP10 | SupplierPEOGlobalAttributeTimestamp10 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP2 | SupplierPEOGlobalAttributeTimestamp2 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP3 | SupplierPEOGlobalAttributeTimestamp3 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP4 | SupplierPEOGlobalAttributeTimestamp4 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP5 | SupplierPEOGlobalAttributeTimestamp5 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP6 | SupplierPEOGlobalAttributeTimestamp6 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP7 | SupplierPEOGlobalAttributeTimestamp7 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP8 | SupplierPEOGlobalAttributeTimestamp8 | — |
| GLOBAL_ATTRIBUTE_TIMESTAMP9 | SupplierPEOGlobalAttributeTimestamp9 | — |
| INCOME_TAX_ID_FLAG | SupplierPEOIncomeTaxIdFlag | — |
| JOB_DEFINITION_NAME | SupplierPEOJobDefinitionName1 | — |
| JOB_DEFINITION_PACKAGE | SupplierPEOJobDefinitionPackage1 | — |
| LAST_UPDATE_DATE | SupplierPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | SupplierPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | SupplierPEOLastUpdatedBy1 | — |
| MIN_ORDER_AMOUNT | SupplierPEOMinOrderAmount | ✅ |
| MINORITY_GROUP_LOOKUP_CODE | SupplierPEOMinorityGroupLookupCode | — |
| NAME_CONTROL | SupplierPEONameControl | — |
| NI_NUMBER | SupplierPEONiNumber | — |
| OBJECT_VERSION_NUMBER | SupplierPEOObjectVersionNumber1 | — |
| OFFSET_TAX_FLAG | SupplierPEOOffsetTaxFlag | — |
| OFFSET_VAT_CODE | SupplierPEOOffsetVatCode | — |
| ONE_TIME_FLAG | SupplierPEOOneTimeFlag | — |
| ORGANIZATION_TYPE_LOOKUP_CODE | SupplierPEOOrganizationTypeLookupCode | — |
| PARENT_PARTY_ID | SupplierPEOParentPartyId | ✅ |
| PARENT_VENDOR_ID | SupplierPEOParentVendorId | ✅ |
| PARTY_ID | SupplierPEOPartyId | ✅ |
| PROGRAM_APPLICATION_ID | SupplierPEOProgramApplicationId | ✅ |
| PROGRAM_ID | SupplierPEOProgramId | ✅ |
| PROGRAM_UPDATE_DATE | SupplierPEOProgramUpdateDate | — |
| REQUEST_ID | SupplierPEORequestId1 | ✅ |
| SEGMENT1 | SupplierPEOSegment11 | — |
| SET_OF_BOOKS_ID | SupplierPEOSetOfBooksId | ✅ |
| SMALL_BUSINESS_FLAG | SupplierPEOSmallBusinessFlag | — |
| SPEND_AUTH_JUSTIFICATION | SupplierPEOSpendAuthJustification | — |
| SPEND_AUTH_REVIEW_STATUS | SupplierPEOSpendAuthReviewStatus | — |
| STANDARD_INDUSTRY_CLASS | SupplierPEOStandardIndustryClass | — |
| START_DATE_ACTIVE | SupplierPEOStartDateActive | — |
| STATE_REPORTABLE_FLAG | SupplierPEOStateReportableFlag | — |
| SUMMARY_FLAG | SupplierPEOSummaryFlag1 | — |
| SUPPLIER_LOCKED_FLAG | SupplierPEOSupplierLockedFlag | — |
| TAX_REPORTING_NAME | SupplierPEOTaxReportingName | — |
| TAX_VERIFICATION_DATE | SupplierPEOTaxVerificationDate | ✅ |
| TAXPAYER_COUNTRY | SupplierPEOTaxpayerCountry | — |
| TYPE_1099 | SupplierPEOType1099 | — |
| VAT_CODE | SupplierPEOVatCode | — |
| VAT_REGISTRATION_NUM | SupplierPEOVatRegistrationNum | — |
| VENDOR_ID | SupplierPEOVendorId1 | ✅ |
| VENDOR_TYPE_LOOKUP_CODE | SupplierPEOVendorTypeLookupCode | — |
| WITHHOLDING_START_DATE | SupplierPEOWithholdingStartDate | ✅ |
| WITHHOLDING_STATUS_LOOKUP_CODE | SupplierPEOWithholdingStatusLookupCode | — |
| WOMEN_OWNED_FLAG | SupplierPEOWomenOwnedFlag | — |
