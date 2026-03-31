---
id: DOC-AP-033
doc_type: system-doc
title: "EXM_EXPENSES — Linhas de Despesa de Relatórios de Despesa"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - accounts-payable
  - data-dictionary
  - despesas
  - expenses
  - expense-management
aliases:
  - EXM_EXPENSES
  - exm_expenses
  - linhas-despesa-exm
  - exm-expenses
  - expense-lines
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# EXM_EXPENSES

## 📌 Visão Geral

Armazena as **linhas individuais de despesa** dentro de relatórios de despesa (Expense Reports) no módulo de Expense Management do Oracle Fusion. Cada registro representa um item de gasto — viagem, hospedagem, alimentação, combustível, etc. — com valor, data, tipo de despesa, justificativa e referências a projeto/tarefa quando aplicável.

> [!note] Expense Management
> O módulo EXM (Expense Management) faz parte do Accounts Payable, gerenciando o ciclo de vida de despesas de funcionários: criação → aprovação → reembolso.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de despesas:** Detalhamento de cada item de gasto dentro de um relatório de despesa.
- **Categorização de gastos:** Classificação por tipo de despesa (viagem, alimentação, hospedagem, etc.).
- **Alocação a projetos:** Vinculação de despesas a projetos e tarefas para capitalização ou custeio.
- **Validação de políticas:** Verificação de limites por tipo de despesa e categoria.
- **Geração de fatura de reembolso:** Base para criação da invoice de reembolso em [[ap_invoices_all]].
- **Auditoria e compliance:** Rastreamento de recibos, justificativas e comprovantes por linha.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | EXPENSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da linha de despesa | — | 🟢 95% |
| 2 | EXPENSE_REPORT_ID | NUMBER(18) | NOT NULL | FK | Relatório de despesa ao qual pertence | [[exm_expense_reports]] | 🟢 95% |
| 3 | EXPENSE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo/categoria da despesa | [[exm_expense_types]] | 🟢 95% |
| 4 | EXPENSE_TEMPLATE_ID | NUMBER(18) | NULL | FK | Template de despesa utilizado | [[exm_expense_templates]] | 🟡 75% |
| 5 | DESCRIPTION | VARCHAR2(240) | NULL | Texto livre | Descrição/justificativa da despesa | — | 🟢 90% |
| 6 | START_DATE | DATE | NOT NULL | Data | Data de início da despesa (ou data do gasto) | — | 🟢 95% |
| 7 | END_DATE | DATE | NULL | Data | Data de término (para despesas multi-dia como hospedagem) | — | 🟢 90% |
| 8 | RECEIPT_AMOUNT | NUMBER | NULL | Financeiro | Valor do recibo na moeda do recibo | — | 🟢 90% |
| 9 | RECEIPT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda do recibo | — | 🟢 90% |
| 10 | REIMBURSABLE_AMOUNT | NUMBER | NULL | Financeiro | Valor reembolsável na moeda de reembolso | — | 🟢 90% |
| 11 | REIMBURSEMENT_CURRENCY_CODE | VARCHAR2(15) | NULL | Moeda | Moeda de reembolso | — | 🟢 85% |
| 12 | EXCHANGE_RATE | NUMBER | NULL | Moeda | Taxa de câmbio do recibo para moeda de reembolso | — | 🟢 85% |
| 13 | LOCATION | VARCHAR2(240) | NULL | Localização | Local onde a despesa ocorreu (cidade, país) | — | 🟢 85% |
| 14 | MERCHANT_NAME | VARCHAR2(240) | NULL | Fornecedor | Nome do estabelecimento/fornecedor | — | 🟢 85% |
| 15 | RECEIPT_REQUIRED_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante é obrigatório (Y/N) | — | 🟡 80% |
| 16 | RECEIPT_MISSING_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se comprovante está ausente (Y/N) | — | 🟡 75% |
| 17 | JUSTIFICATION | VARCHAR2(2000) | NULL | Texto livre | Justificativa detalhada para a despesa | — | 🟡 75% |
| 18 | PROJECT_ID | NUMBER(18) | NULL | FK | Projeto associado à despesa | [[pjf_projects_all_b]] | 🟢 85% |
| 19 | TASK_ID | NUMBER(18) | NULL | FK | Tarefa do projeto | [[pjf_proj_elements_b]] | 🟢 85% |
| 20 | EXPENDITURE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de gasto para contabilidade de projetos | [[pjf_exp_types_tl]] | 🟡 75% |
| 21 | ITEMIZATION_PARENT_ID | NUMBER(18) | NULL | Referência | ID da despesa-pai (para linhas itemizadas/detalhadas) | — | 🟡 70% |
| 22 | NUMBER_OF_DAYS | NUMBER | NULL | Quantidade | Número de dias (para per diem) | — | 🟡 75% |
| 23 | DAILY_AMOUNT | NUMBER | NULL | Financeiro | Valor diário (per diem) | — | 🟡 75% |
| 24 | PERSONAL_FLAG | VARCHAR2(1) | NULL | Classificação | Indica se a despesa é pessoal/não reembolsável (Y/N) | — | 🟡 70% |
| 25 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit (multi-org) | [[hr_all_organization_units_f]] | 🟢 95% |
| 26 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 27 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 28 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 29 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 30 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[exm_expense_reports]] — via `EXPENSE_REPORT_ID` (relatório de despesa)
- [[exm_expense_types]] — via `EXPENSE_TYPE_ID` (tipo de despesa)
- [[exm_expense_templates]] — via `EXPENSE_TEMPLATE_ID` (template utilizado)
- [[pjf_projects_all_b]] — via `PROJECT_ID` (projeto associado)
- [[pjf_proj_elements_b]] — via `TASK_ID` (tarefa do projeto)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit da linha de despesa)

### Tabelas-filha (FK de saída)
- [[exm_expense_dists]] — via `EXPENSE_ID` (distribuições contábeis da despesa)

---

## 📎 Uso Típico

### Despesas de um relatório com tipo e valor
```sql
SELECT e.EXPENSE_ID, e.START_DATE, et.EXPENSE_TYPE_NAME,
       e.RECEIPT_AMOUNT, e.RECEIPT_CURRENCY_CODE,
       e.REIMBURSABLE_AMOUNT, e.MERCHANT_NAME
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.EXPENSE_REPORT_ID = :p_report_id
ORDER BY e.START_DATE;
```

### Total de despesas por tipo em um período
```sql
SELECT et.EXPENSE_TYPE_NAME,
       SUM(e.REIMBURSABLE_AMOUNT) AS total_reembolsavel,
       COUNT(*) AS qtd_itens
FROM   EXM_EXPENSES e
JOIN   EXM_EXPENSE_TYPES et ON et.EXPENSE_TYPE_ID = e.EXPENSE_TYPE_ID
WHERE  e.START_DATE BETWEEN :start_date AND :end_date
  AND  e.ORG_ID = :p_org_id
GROUP BY et.EXPENSE_TYPE_NAME
ORDER BY total_reembolsavel DESC;
```

### Filtros comuns
- `PERSONAL_FLAG = 'N'` — Despesas corporativas (reembolsáveis)
- `RECEIPT_MISSING_FLAG = 'Y'` — Despesas sem comprovante
- `PROJECT_ID IS NOT NULL` — Despesas alocadas a projetos

---

## 🔒 Observações

- Cada linha de despesa pode ser **itemizada** (detalhada em sub-linhas) usando `ITEMIZATION_PARENT_ID` para vincular sub-itens ao item principal.
- O campo `PERSONAL_FLAG = 'Y'` indica despesas pessoais incluídas no relatório para transparência, mas que **não serão reembolsadas**.
- `RECEIPT_AMOUNT` é na moeda do recibo (local), enquanto `REIMBURSABLE_AMOUNT` é na moeda de reembolso do funcionário.
- Despesas de **per diem** utilizam `NUMBER_OF_DAYS` × `DAILY_AMOUNT` para cálculo automático.
- A tabela [[exm_expense_dists]] contém as distribuições contábeis (rateio por CCID, projeto, etc.) para cada linha.

---

## 🔗 PVOs Relacionados

### [[corporatecardtransactionpvo|CorporateCardTransactionPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpensePEOAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpensePEOAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpensePEOAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpensePEOAttributeCategory | — |
| AUDIT_ADJUSTMENT_REASON | ExpensePEOAuditAdjustmentReason | — |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpensePEOAuditAdjustmentReasonCode | — |
| AVG_MILEAGE_RATE | ExpensePEOAvgMileageRate | — |
| AWT_GROUP_ID | ExpensePEOAwtGroupId | — |
| CARD_ID | ExpensePEOCardId | — |
| CC_PREPAID_INVOICE_ID | ExpensePEOCcPrepaidInvoiceId | — |
| CC_PREPAID_REQUEST_ID | ExpensePEOCcPrepaidRequestId | — |
| CHECKOUT_DATE | ExpensePEOCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpensePEOCountryOfSupply | — |
| CREATED_BY | ExpensePEOCreatedBy | — |
| CREATION_DATE | ExpensePEOCreationDate | — |
| CREDIT_CARD_TRXN_ID | ExpensePEOCreditCardTrxnId | — |
| DAILY_DISTANCE | ExpensePEODailyDistance | — |
| DEPARTURE_LOCATION_ID | ExpensePEODepartureLocationId | — |
| DESCRIPTION | ExpensePEODescription | — |
| DESTINATION_FROM | ExpensePEODestinationFrom | — |
| DESTINATION_TO | ExpensePEODestinationTo | — |
| DISTANCE_UNIT_CODE | ExpensePEODistanceUnitCode | — |
| EMP_DEFAULT_COST_CENTER | ExpensePEOEmpDefaultCostCenter | — |
| END_DATE | ExpensePEOEndDate | — |
| EXCHANGE_RATE | ExpensePEOExchangeRate | — |
| EXPENSE_CATEGORY_CODE | ExpensePEOExpenseCategoryCode | — |
| EXPENSE_CREATION_METHOD_CODE | ExpensePEOExpenseCreationMethodCode | — |
| EXPENSE_ID | ExpensePEOExpenseId | — |
| EXPENSE_REPORT_ID | ExpensePEOExpenseReportId | — |
| EXPENSE_SOURCE | ExpensePEOExpenseSource | — |
| EXPENSE_TEMPLATE_ID | ExpensePEOExpenseTemplateId | — |
| EXPENSE_TYPE_CATEGORY_CODE | ExpensePEOExpenseTypeCategoryCode | — |
| EXPENSE_TYPE_ID | ExpensePEOExpenseTypeId | — |
| FLIGHT_NUMBER | ExpensePEOFlightNumber | — |
| FUEL_TYPE | ExpensePEOFuelType | — |
| FUNC_CURRENCY_AMOUNT | ExpensePEOFuncCurrencyAmount | — |
| IMG_RECEIPT_REQUIRED_FLAG | ExpensePEOImgReceiptRequiredFlag | — |
| INACTIVE_EMP_PROCESS_ID | ExpensePEOInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpensePEOItemizationParentExpenseId | — |
| JUSTIFICATION | ExpensePEOJustification | — |
| JUSTIFICATION_REQUIRED_FLAG | ExpensePEOJustificationRequiredFlag | — |
| LAST_UPDATE_DATE | ExpensePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | ExpensePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpensePEOLastUpdatedBy | — |
| LICENSE_PLATE_NUMBER | ExpensePEOLicensePlateNumber | — |
| LOCATION | ExpensePEOLocation | — |
| LOCATION_ID | ExpensePEOLocationId | — |
| MERCHANT_DOCUMENT_NUMBER | ExpensePEOMerchantDocumentNumber | — |
| MERCHANT_NAME | ExpensePEOMerchantName | — |
| MERCHANT_REFERENCE | ExpensePEOMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpensePEOMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpensePEOMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpensePEOMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpensePEONumberOfAttendees | — |
| NUMBER_PEOPLE | ExpensePEONumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpensePEOObjectVersionNumber | — |
| ORG_ID | ExpensePEOOrgId | — |
| ORIG_EXCHANGE_RATE | ExpensePEOOrigExchangeRate | — |
| ORIG_EXPENSE_TYPE_ID | ExpensePEOOrigExpenseTypeId | — |
| ORIG_RECEIPT_AMOUNT | ExpensePEOOrigReceiptAmount | — |
| ORIG_REIMBURSABLE_AMOUNT | ExpensePEOOrigReimbursableAmount | — |
| PASSENGER_AMOUNT | ExpensePEOPassengerAmount | — |
| PASSENGER_RATE_TYPE | ExpensePEOPassengerRateType | — |
| PERSON_ID | ExpensePEOPersonId | — |
| PERSONAL_RECEIPT_AMOUNT | ExpensePEOPersonalReceiptAmount | — |
| POLICY_SHORTPAY_FLAG | ExpensePEOPolicyShortpayFlag | — |
| POLICY_VIOLATED_FLAG | ExpensePEOPolicyViolatedFlag | — |
| PREPARER_ID | ExpensePEOPreparerId | — |
| RANGE_HIGH | ExpensePEORangeHigh | — |
| RANGE_LOW | ExpensePEORangeLow | — |
| RATE_PER_PASSENGER | ExpensePEORatePerPassenger | — |
| RECEIPT_AMOUNT | ExpensePEOReceiptAmount | — |
| RECEIPT_CURRENCY_CODE | ExpensePEOReceiptCurrencyCode | — |
| RECEIPT_MISSING_DEC_REQ_FLAG | ExpensePEOReceiptMissingDecReqFlag | — |
| RECEIPT_MISSING_FLAG | ExpensePEOReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpensePEOReceiptRequiredFlag | — |
| RECEIPT_VERIFIED_FLAG | ExpensePEOReceiptVerifiedFlag | — |
| REIMBURSABLE_AMOUNT | ExpensePEOReimbursableAmount | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpensePEOReimbursementCurrencyCode | — |
| SEQUENCE_NUM | ExpensePEOSequenceNum | — |
| START_DATE | ExpensePEOStartDate | — |
| TAX_CLASSIFICATION_CODE | ExpensePEOTaxClassificationCode | — |
| TICKET_CLASS_CODE | ExpensePEOTicketClassCode | — |
| TICKET_NUMBER | ExpensePEOTicketNumber | — |
| TRAVEL_TYPE | ExpensePEOTravelType | — |
| TRIP_DISTANCE | ExpensePEOTripDistance | — |
| TRXN_AVAILABLE_DATE | ExpensePEOTrxnAvailableDate | — |
| UOM_DAYS | ExpensePEOUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpensePEOVehicleCategoryCode | — |
| VEHICLE_TYPE | ExpensePEOVehicleType | — |

### [[expenseattendeedetailspvo|ExpenseAttendeeDetailsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EXPENSE_ID | ExpExpenseId | — |

### [[expenseattendeepvo|ExpenseAttendeePVO]] (OTHER · BICC: 39/90)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpAttributeCategory1 | — |
| AUDIT_ADJUSTMENT_REASON | ExpAuditAdjustmentReason | — |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpAuditAdjustmentReasonCode | ✅ |
| AVG_MILEAGE_RATE | ExpAvgMileageRate | ✅ |
| AWT_GROUP_ID | ExpAwtGroupId | — |
| CARD_ID | ExpCardId | — |
| CC_PREPAID_INVOICE_ID | ExpCcPrepaidInvoiceId | — |
| CC_PREPAID_REQUEST_ID | ExpCcPrepaidRequestId | — |
| CHECKOUT_DATE | ExpCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpCountryOfSupply | — |
| CREATED_BY | ExpCreatedBy | ✅ |
| CREATION_DATE | ExpCreationDate | ✅ |
| CREDIT_CARD_TRXN_ID | ExpCreditCardTrxnId | — |
| DAILY_DISTANCE | ExpDailyDistance | ✅ |
| DEPARTURE_LOCATION_ID | ExpDepartureLocationId | — |
| DESCRIPTION | ExpDescription | ✅ |
| DESTINATION_FROM | ExpDestinationFrom | ✅ |
| DESTINATION_TO | ExpDestinationTo | ✅ |
| DISTANCE_UNIT_CODE | ExpDistanceUnitCode | ✅ |
| EMP_DEFAULT_COST_CENTER | ExpEmpDefaultCostCenter | — |
| END_DATE | ExpEndDate | ✅ |
| EXCHANGE_RATE | ExpExchangeRate | — |
| EXPENSE_CATEGORY_CODE | ExpExpenseCategoryCode | ✅ |
| EXPENSE_CREATION_METHOD_CODE | FullExpExpenseCMC | — |
| EXPENSE_ID | ExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpExpenseReportId | ✅ |
| EXPENSE_SOURCE | ExpExpenseSource | ✅ |
| EXPENSE_TEMPLATE_ID | ExpExpenseTemplateId | — |
| EXPENSE_TYPE_CATEGORY_CODE | ExpExpenseTypeCategoryCode | ✅ |
| EXPENSE_TYPE_ID | ExpExpenseTypeId | — |
| FLIGHT_NUMBER | ExpFlightNumber | ✅ |
| FUEL_TYPE | ExpFuelType | ✅ |
| FUNC_CURRENCY_AMOUNT | ExpFuncCurrencyAmount | — |
| IMG_RECEIPT_REQUIRED_FLAG | ExpImgReceiptRequiredFlag | — |
| INACTIVE_EMP_PROCESS_ID | ExpInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpItemizationParentExpenseId | — |
| JUSTIFICATION | ExpJustification | ✅ |
| JUSTIFICATION_REQUIRED_FLAG | ExpJustificationRequiredFlag | ✅ |
| LAST_UPDATE_DATE | ExpLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpLastUpdatedBy | ✅ |
| LICENSE_PLATE_NUMBER | ExpLicensePlateNumber | — |
| LOCATION | ExpLocation | ✅ |
| LOCATION_ID | ExpLocationId | — |
| MERCHANT_DOCUMENT_NUMBER | ExpMerchantDocumentNumber | ✅ |
| MERCHANT_NAME | ExpMerchantName | ✅ |
| MERCHANT_REFERENCE | ExpMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpNumberOfAttendees | ✅ |
| NUMBER_PEOPLE | ExpNumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpObjectVersionNumber | — |
| ORG_ID | ExpOrgId | — |
| ORIG_EXCHANGE_RATE | ExpOrigExchangeRate | — |
| ORIG_EXPENSE_TYPE_ID | ExpOrigExpenseTypeId | — |
| ORIG_RECEIPT_AMOUNT | ExpOrigReceiptAmount | — |
| ORIG_REIMBURSABLE_AMOUNT | ExpOrigReimbursableAmount | — |
| PASSENGER_AMOUNT | ExpPassengerAmount | — |
| PASSENGER_RATE_TYPE | ExpPassengerRateType | — |
| PERSON_ID | ExpPersonId | — |
| PERSONAL_RECEIPT_AMOUNT | ExpPersonalReceiptAmount | — |
| POLICY_SHORTPAY_FLAG | ExpPolicyShortpayFlag | ✅ |
| POLICY_VIOLATED_FLAG | ExpPolicyViolatedFlag | ✅ |
| PREPARER_ID | ExpPreparerId | — |
| RANGE_HIGH | ExpRangeHigh | — |
| RANGE_LOW | ExpRangeLow | — |
| RATE_PER_PASSENGER | ExpRatePerPassenger | — |
| RECEIPT_AMOUNT | ExpReceiptAmount | — |
| RECEIPT_CURRENCY_CODE | ExpReceiptCurrencyCode | ✅ |
| RECEIPT_MISSING_DEC_REQ_FLAG | ExpReceiptMissingDecReqFlag | — |
| RECEIPT_MISSING_FLAG | ExpReceiptMissingFlag | ✅ |
| RECEIPT_REQUIRED_FLAG | ExpReceiptRequiredFlag | ✅ |
| RECEIPT_VERIFIED_FLAG | ExpReceiptVerifiedFlag | ✅ |
| REIMBURSABLE_AMOUNT | ExpReimbursableAmount | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpReimbursementCurrencyCode | — |
| SEQUENCE_NUM | ExpSequenceNum | — |
| START_DATE | ExpStartDate | ✅ |
| TAX_CLASSIFICATION_CODE | ExpTaxClassificationCode | ✅ |
| TICKET_CLASS_CODE | ExpTicketClassCode | ✅ |
| TICKET_NUMBER | ExpTicketNumber | ✅ |
| TRAVEL_TYPE | ExpTravelType | ✅ |
| TRIP_DISTANCE | ExpTripDistance | ✅ |
| TRXN_AVAILABLE_DATE | ExpTrxnAvailableDate | — |
| UOM_DAYS | ExpUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpVehicleCategoryCode | ✅ |
| VEHICLE_TYPE | ExpVehicleType | ✅ |

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 50/96)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpAssignmentId | — |
| ATTRIBUTE_CHAR1 | ExpAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpAttributeChar9 | — |
| AUDIT_ADJUSTMENT_REASON | ExpAuditAdjustmentReason | — |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpAuditAdjustmentReasonCode | ✅ |
| AVG_MILEAGE_RATE | ExpAvgMileageRate | ✅ |
| AWT_GROUP_ID | ExpAwtGroupId | — |
| CARD_ID | ExpCardId | — |
| CC_PREPAID_INVOICE_ID | ExpCcPrepaidInvoiceId | — |
| CHECKOUT_DATE | ExpCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpCountryOfSupply | — |
| CREATED_BY | ExpCreatedBy | ✅ |
| CREATION_DATE | ExpCreationDate | ✅ |
| CREDIT_CARD_TRXN_ID | ExpCreditCardTrxnId | — |
| DAILY_DISTANCE | ExpDailyDistance | ✅ |
| DEPARTURE_LOCATION_ID | ExpDepartureLocationId | — |
| DESCRIPTION | ExpDescription | ✅ |
| DESTINATION_FROM | ExpDestinationFrom | ✅ |
| DESTINATION_TO | ExpDestinationTo | ✅ |
| DISTANCE_UNIT_CODE | ExpDistanceUnitCode | ✅ |
| EMP_DEFAULT_COST_CENTER | ExpEmpDefaultCostCenter | ✅ |
| END_DATE | ExpEndDate | ✅ |
| EXCHANGE_RATE | ExpExchangeRate | ✅ |
| EXPENSE_CATEGORY_CODE | ExpExpenseCategoryCode | ✅ |
| EXPENSE_CREATION_METHOD_CODE | FullExpExpenseCMC | — |
| EXPENSE_ID | ExpExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpExpenseReportId | ✅ |
| EXPENSE_SOURCE | ExpExpenseSource | ✅ |
| EXPENSE_TEMPLATE_ID | ExpExpenseTemplateId | — |
| EXPENSE_TYPE_CATEGORY_CODE | ExpExpenseTypeCategoryCode | ✅ |
| EXPENSE_TYPE_ID | ExpExpenseTypeId | ✅ |
| FLIGHT_NUMBER | ExpFlightNumber | ✅ |
| FUEL_TYPE | ExpFuelType | ✅ |
| FUNC_CURRENCY_AMOUNT | ExpFuncCurrencyAmount | ✅ |
| INACTIVE_EMP_PROCESS_ID | ExpInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpItemizationParentExpenseId | ✅ |
| JUSTIFICATION | ExpJustification | ✅ |
| JUSTIFICATION_REQUIRED_FLAG | ExpJustificationRequiredFlag | ✅ |
| LAST_UPDATE_DATE | ExpLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpLastUpdatedBy | ✅ |
| LICENSE_PLATE_NUMBER | ExpLicensePlateNumber | — |
| LOCATION | ExpLocation | ✅ |
| LOCATION_ID | ExpLocationId | ✅ |
| MERCHANT_DOCUMENT_NUMBER | ExpMerchantDocumentNumber | ✅ |
| MERCHANT_NAME | ExpMerchantName | ✅ |
| MERCHANT_REFERENCE | ExpMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpNumberOfAttendees | ✅ |
| NUMBER_PEOPLE | ExpNumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpObjectVersionNumber | — |
| ORG_ID | ExpOrgId | ✅ |
| ORIG_REIMBURSABLE_AMOUNT | ExpOrigReimbursableAmount | ✅ |
| PASSENGER_AMOUNT | ExpPassengerAmount | — |
| PASSENGER_RATE_TYPE | ExpPassengerRateType | — |
| PERSON_ID | ExpPersonId | — |
| POLICY_SHORTPAY_FLAG | ExpPolicyShortpayFlag | ✅ |
| POLICY_VIOLATED_FLAG | ExpPolicyViolatedFlag | ✅ |
| PREPARER_ID | ExpPreparerId | — |
| RANGE_HIGH | ExpRangeHigh | — |
| RANGE_LOW | ExpRangeLow | — |
| RATE_PER_PASSENGER | ExpRatePerPassenger | — |
| RECEIPT_AMOUNT | ExpReceiptAmount | — |
| RECEIPT_CURRENCY_CODE | ExpReceiptCurrencyCode | ✅ |
| RECEIPT_MISSING_FLAG | ExpReceiptMissingFlag | ✅ |
| RECEIPT_REQUIRED_FLAG | ExpReceiptRequiredFlag | ✅ |
| RECEIPT_VERIFIED_FLAG | ExpReceiptVerifiedFlag | ✅ |
| REIMBURSABLE_AMOUNT | ExpReimbursableAmount | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpReimbursementCurrencyCode | ✅ |
| SEQUENCE_NUM | ExpSequenceNum | ✅ |
| START_DATE | ExpStartDate | ✅ |
| TAX_CLASSIFICATION_CODE | ExpTaxClassificationCode | ✅ |
| TICKET_CLASS_CODE | ExpTicketClassCode | ✅ |
| TICKET_NUMBER | ExpTicketNumber | ✅ |
| TRAVEL_TYPE | ExpTravelType | ✅ |
| TRIP_DISTANCE | ExpTripDistance | ✅ |
| UOM_DAYS | ExpUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpVehicleCategoryCode | ✅ |
| VEHICLE_TYPE | ExpVehicleType | ✅ |

### [[expenseextractpvo|ExpenseExtractPVO]] (OTHER · BICC: 39/117)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpenseAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpenseAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpenseAssignmentId | ✅ |
| ATTRIBUTE_CATEGORY | ExpenseAttributeCategory | — |
| ATTRIBUTE_CHAR1 | ExpenseAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpenseAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpenseAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpenseAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpenseAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpenseAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpenseAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpenseAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpenseAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpenseAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpenseAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpenseAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpenseAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpenseAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpenseAttributeChar9 | — |
| ATTRIBUTE_DATE1 | ExpenseAttributeDate1 | — |
| ATTRIBUTE_DATE2 | ExpenseAttributeDate2 | ✅ |
| ATTRIBUTE_DATE3 | ExpenseAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ExpenseAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ExpenseAttributeDate5 | — |
| ATTRIBUTE_DATETIME1 | ExpenseAttributeDatetime1 | — |
| ATTRIBUTE_DATETIME2 | ExpenseAttributeDatetime2 | — |
| ATTRIBUTE_NUMBER1 | ExpenseAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | ExpenseAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | ExpenseAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ExpenseAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ExpenseAttributeNumber5 | — |
| AUDIT_ADJUSTMENT_REASON | ExpenseAuditAdjustmentReason | ✅ |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpenseAuditAdjustmentReasonCode | ✅ |
| AVG_MILEAGE_RATE | ExpenseAvgMileageRate | — |
| AWT_GROUP_ID | ExpenseAwtGroupId | — |
| CARD_ID | ExpenseCardId | ✅ |
| CC_PREPAID_INVOICE_ID | ExpenseCcPrepaidInvoiceId | — |
| CC_PREPAID_REQUEST_ID | ExpenseCcPrepaidRequestId | — |
| CHECKOUT_DATE | ExpenseCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpenseCountryOfSupply | — |
| CREATED_BY | ExpenseCreatedBy | — |
| CREATION_DATE | ExpenseCreationDate | ✅ |
| CREDIT_CARD_TRXN_ID | ExpenseCreditCardTrxnId | ✅ |
| DAILY_DISTANCE | ExpenseDailyDistance | — |
| DEPARTURE_LOCATION_ID | ExpenseDepartureLocationId | — |
| DESCRIPTION | ExpenseDescription | ✅ |
| DESTINATION_FROM | ExpenseDestinationFrom | — |
| DESTINATION_TO | ExpenseDestinationTo | — |
| DISTANCE_UNIT_CODE | ExpenseDistanceUnitCode | — |
| EMP_DEFAULT_COST_CENTER | ExpenseEmpDefaultCostCenter | ✅ |
| END_DATE | ExpenseEndDate | ✅ |
| EXCHANGE_RATE | ExpenseExchangeRate | ✅ |
| EXPENSE_CATEGORY_CODE | ExpenseCategoryCode | — |
| EXPENSE_CREATION_METHOD_CODE | ExpenseCreationMethodCode | — |
| EXPENSE_ID | ExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpenseReportId | ✅ |
| EXPENSE_SOURCE | ExpenseSource | ✅ |
| EXPENSE_TEMPLATE_ID | ExpenseTemplateId | ✅ |
| EXPENSE_TYPE_CATEGORY_CODE | ExpenseTypeCategoryCode | ✅ |
| EXPENSE_TYPE_ID | ExpenseTypeId | ✅ |
| FLIGHT_NUMBER | ExpenseFlightNumber | — |
| FUEL_TYPE | ExpenseFuelType | — |
| FUNC_CURRENCY_AMOUNT | ExpenseFuncCurrencyAmount | ✅ |
| IMG_RECEIPT_REQUIRED_FLAG | ExpenseImgReceiptRequiredFlag | — |
| INACTIVE_EMP_PROCESS_ID | ExpenseInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpenseItemizationParentExpenseId | ✅ |
| JUSTIFICATION | ExpenseJustification | ✅ |
| JUSTIFICATION_REQUIRED_FLAG | ExpenseJustificationRequiredFlag | ✅ |
| LAST_UPDATE_DATE | ExpenseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpenseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ExpenseLastUpdatedBy | — |
| LICENSE_PLATE_NUMBER | ExpenseLicensePlateNumber | — |
| LOCATION | ExpenseLocation | ✅ |
| LOCATION_ID | ExpenseLocationId | ✅ |
| MERCHANT_DOCUMENT_NUMBER | ExpenseMerchantDocumentNumber | — |
| MERCHANT_NAME | ExpenseMerchantName | — |
| MERCHANT_REFERENCE | ExpenseMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpenseMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpenseMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpenseMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpenseNumberOfAttendees | — |
| NUMBER_PEOPLE | ExpenseNumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpenseObjectVersionNumber | — |
| ORG_ID | ExpenseOrgId | ✅ |
| ORIG_EXCHANGE_RATE | ExpenseOrigExchangeRate | — |
| ORIG_EXPENSE_TYPE_ID | ExpenseOrigExpenseTypeId | — |
| ORIG_RECEIPT_AMOUNT | ExpenseOrigReceiptAmount | — |
| ORIG_REIMBURSABLE_AMOUNT | ExpenseOrigReimbursableAmount | ✅ |
| PASSENGER_AMOUNT | ExpensePassengerAmount | — |
| PASSENGER_RATE_TYPE | ExpensePassengerRateType | — |
| PERSON_ID | ExpensePersonId | ✅ |
| PERSONAL_RECEIPT_AMOUNT | ExpensePersonalReceiptAmount | ✅ |
| POLICY_SHORTPAY_FLAG | ExpensePolicyShortpayFlag | — |
| POLICY_VIOLATED_FLAG | ExpensePolicyViolatedFlag | — |
| PREPARER_ID | ExpensePreparerId | ✅ |
| RANGE_HIGH | ExpenseRangeHigh | — |
| RANGE_LOW | ExpenseRangeLow | — |
| RATE_PER_PASSENGER | ExpenseRatePerPassenger | — |
| RECEIPT_AMOUNT | ExpenseReceiptAmount | ✅ |
| RECEIPT_CURRENCY_CODE | ExpenseReceiptCurrencyCode | ✅ |
| RECEIPT_MISSING_DEC_REQ_FLAG | ExpenseReceiptMissingDecReqFlag | — |
| RECEIPT_MISSING_FLAG | ExpenseReceiptMissingFlag | ✅ |
| RECEIPT_REQUIRED_FLAG | ExpenseReceiptRequiredFlag | ✅ |
| RECEIPT_VERIFIED_FLAG | ExpenseReceiptVerifiedFlag | ✅ |
| REIMBURSABLE_AMOUNT | ExpenseReimbursableAmount | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpenseReimbursementCurrencyCode | ✅ |
| SEQUENCE_NUM | ExpenseSequenceNum | — |
| START_DATE | ExpenseStartDate | ✅ |
| TAX_CLASSIFICATION_CODE | ExpenseTaxClassificationCode | ✅ |
| TICKET_CLASS_CODE | ExpenseTicketClassCode | — |
| TICKET_NUMBER | ExpenseTicketNumber | — |
| TRAVEL_TYPE | ExpenseTravelType | — |
| TRIP_DISTANCE | ExpenseTripDistance | — |
| TRXN_AVAILABLE_DATE | ExpenseTrxnAvailableDate | — |
| UOM_DAYS | ExpenseUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpenseVehicleCategoryCode | — |
| VEHICLE_TYPE | ExpenseVehicleType | — |

### [[expensepvo|ExpensePVO]] (OTHER · BICC: 47/98)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpAssignmentId | — |
| ATTRIBUTE_CHAR1 | ExpAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpAttributeChar9 | — |
| AUDIT_ADJUSTMENT_REASON | ExpAuditAdjustmentReason | — |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpAuditAdjustmentReasonCode | — |
| AVG_MILEAGE_RATE | ExpAvgMileageRate | ✅ |
| AWT_GROUP_ID | ExpAwtGroupId | — |
| CARD_ID | ExpCardId | — |
| CC_PREPAID_INVOICE_ID | ExpCcPrepaidInvoiceId | — |
| CHECKOUT_DATE | ExpCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpCountryOfSupply | — |
| CREATED_BY | ExpCreatedBy | ✅ |
| CREATION_DATE | ExpCreationDate | ✅ |
| CREDIT_CARD_TRXN_ID | ExpCreditCardTrxnId | ✅ |
| DAILY_DISTANCE | ExpDailyDistance | ✅ |
| DEPARTURE_LOCATION_ID | ExpDepartureLocationId | — |
| DESCRIPTION | ExpDescription | ✅ |
| DESTINATION_FROM | ExpDestinationFrom | ✅ |
| DESTINATION_TO | ExpDestinationTo | ✅ |
| DISTANCE_UNIT_CODE | ExpDistanceUnitCode | ✅ |
| EMP_DEFAULT_COST_CENTER | ExpEmpDefaultCostCenter | ✅ |
| END_DATE | ExpEndDate | ✅ |
| EXCHANGE_RATE | ExpExchangeRate | ✅ |
| EXPENSE_CATEGORY_CODE | ExpExpenseCategoryCode | ✅ |
| EXPENSE_CREATION_METHOD_CODE | FullExpExpenseCMC | — |
| EXPENSE_ID | ExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpExpenseReportId | ✅ |
| EXPENSE_SOURCE | ExpExpenseSource | ✅ |
| EXPENSE_TEMPLATE_ID | ExpExpenseTemplateId | — |
| EXPENSE_TYPE_CATEGORY_CODE | ExpExpenseTypeCategoryCode | ✅ |
| EXPENSE_TYPE_ID | ExpExpenseTypeId | ✅ |
| FLIGHT_NUMBER | ExpFlightNumber | ✅ |
| FUEL_TYPE | ExpFuelType | ✅ |
| FUNC_CURRENCY_AMOUNT | ExpFuncCurrencyAmount | ✅ |
| INACTIVE_EMP_PROCESS_ID | ExpInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpItemizationParentExpenseId | ✅ |
| JUSTIFICATION | ExpJustification | ✅ |
| JUSTIFICATION_REQUIRED_FLAG | ExpJustificationRequiredFlag | — |
| LAST_UPDATE_DATE | ExpLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpLastUpdatedBy | ✅ |
| LICENSE_PLATE_NUMBER | ExpLicensePlateNumber | — |
| LOCATION | ExpLocation | ✅ |
| LOCATION_ID | ExpLocationId | ✅ |
| MERCHANT_DOCUMENT_NUMBER | ExpMerchantDocumentNumber | ✅ |
| MERCHANT_NAME | ExpMerchantName | ✅ |
| MERCHANT_REFERENCE | ExpMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpNumberOfAttendees | ✅ |
| NUMBER_PEOPLE | ExpNumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpObjectVersionNumber | — |
| ORG_ID | ExpOrgId | ✅ |
| ORIG_RECEIPT_AMOUNT | ExpOrigReceiptAmount | — |
| ORIG_REIMBURSABLE_AMOUNT | ExpOrigReimbursableAmount | ✅ |
| PASSENGER_AMOUNT | ExpPassengerAmount | ✅ |
| PASSENGER_RATE_TYPE | ExpPassengerRateType | — |
| PERSON_ID | ExpPersonId | ✅ |
| PERSONAL_RECEIPT_AMOUNT | ExpPersonalReceiptAmount | ✅ |
| POLICY_SHORTPAY_FLAG | ExpPolicyShortpayFlag | — |
| POLICY_VIOLATED_FLAG | ExpPolicyViolatedFlag | — |
| PREPARER_ID | ExpPreparerId | — |
| RANGE_HIGH | ExpRangeHigh | — |
| RANGE_LOW | ExpRangeLow | — |
| RATE_PER_PASSENGER | ExpRatePerPassenger | — |
| RECEIPT_AMOUNT | ExpReceiptAmount | ✅ |
| RECEIPT_CURRENCY_CODE | ExpReceiptCurrencyCode | ✅ |
| RECEIPT_MISSING_FLAG | ExpReceiptMissingFlag | — |
| RECEIPT_REQUIRED_FLAG | ExpReceiptRequiredFlag | — |
| RECEIPT_VERIFIED_FLAG | ExpReceiptVerifiedFlag | — |
| REIMBURSABLE_AMOUNT | ExpReimbursableAmount | ✅ |
| REIMBURSEMENT_CURRENCY_CODE | ExpReimbursementCurrencyCode | ✅ |
| SEQUENCE_NUM | ExpSequenceNum | — |
| START_DATE | ExpStartDate | ✅ |
| TAX_CLASSIFICATION_CODE | ExpTaxClassificationCode | ✅ |
| TICKET_CLASS_CODE | ExpTicketClassCode | ✅ |
| TICKET_NUMBER | ExpTicketNumber | ✅ |
| TRAVEL_TYPE | ExpTravelType | ✅ |
| TRIP_DISTANCE | ExpTripDistance | ✅ |
| UOM_DAYS | ExpUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpVehicleCategoryCode | ✅ |
| VEHICLE_TYPE | ExpVehicleType | ✅ |

### [[expenseviolationpvo|ExpenseViolationPVO]] (OTHER · BICC: 39/117)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOCATION_REASON | ExpAllocationReason | — |
| ALLOCATION_SPLIT_CODE | ExpAllocationSplitCode | — |
| ASSIGNMENT_ID | ExpAssignmentId | — |
| ATTRIBUTE_CATEGORY | ExpAttributeCategory | — |
| ATTRIBUTE_CHAR1 | ExpAttributeChar1 | — |
| ATTRIBUTE_CHAR10 | ExpAttributeChar10 | — |
| ATTRIBUTE_CHAR11 | ExpAttributeChar11 | — |
| ATTRIBUTE_CHAR12 | ExpAttributeChar12 | — |
| ATTRIBUTE_CHAR13 | ExpAttributeChar13 | — |
| ATTRIBUTE_CHAR14 | ExpAttributeChar14 | — |
| ATTRIBUTE_CHAR15 | ExpAttributeChar15 | — |
| ATTRIBUTE_CHAR2 | ExpAttributeChar2 | — |
| ATTRIBUTE_CHAR3 | ExpAttributeChar3 | — |
| ATTRIBUTE_CHAR4 | ExpAttributeChar4 | — |
| ATTRIBUTE_CHAR5 | ExpAttributeChar5 | — |
| ATTRIBUTE_CHAR6 | ExpAttributeChar6 | — |
| ATTRIBUTE_CHAR7 | ExpAttributeChar7 | — |
| ATTRIBUTE_CHAR8 | ExpAttributeChar8 | — |
| ATTRIBUTE_CHAR9 | ExpAttributeChar9 | — |
| ATTRIBUTE_DATE1 | ExpAttributeDate1 | — |
| ATTRIBUTE_DATE2 | ExpAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ExpAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ExpAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ExpAttributeDate5 | — |
| ATTRIBUTE_DATETIME1 | ExpAttributeDatetime1 | — |
| ATTRIBUTE_DATETIME2 | ExpAttributeDatetime2 | — |
| ATTRIBUTE_NUMBER1 | ExpAttributeNumber1 | — |
| ATTRIBUTE_NUMBER2 | ExpAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | ExpAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ExpAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ExpAttributeNumber5 | — |
| AUDIT_ADJUSTMENT_REASON | ExpAuditAdjustmentReason | — |
| AUDIT_ADJUSTMENT_REASON_CODE | ExpAuditAdjustmentReasonCode | ✅ |
| AVG_MILEAGE_RATE | ExpAvgMileageRate | ✅ |
| AWT_GROUP_ID | ExpAwtGroupId | — |
| CARD_ID | ExpCardId | — |
| CC_PREPAID_INVOICE_ID | ExpCcPrepaidInvoiceId | — |
| CC_PREPAID_REQUEST_ID | ExpCcPrepaidRequestId | — |
| CHECKOUT_DATE | ExpCheckoutDate | — |
| COUNTRY_OF_SUPPLY | ExpCountryOfSupply | — |
| CREATED_BY | ExpCreatedBy | ✅ |
| CREATION_DATE | ExpCreationDate | ✅ |
| CREDIT_CARD_TRXN_ID | ExpCreditCardTrxnId | — |
| DAILY_DISTANCE | ExpDailyDistance | ✅ |
| DEPARTURE_LOCATION_ID | ExpDepartureLocationId | — |
| DESCRIPTION | ExpDescription | ✅ |
| DESTINATION_FROM | ExpDestinationFrom | ✅ |
| DESTINATION_TO | ExpDestinationTo | ✅ |
| DISTANCE_UNIT_CODE | ExpDistanceUnitCode | ✅ |
| EMP_DEFAULT_COST_CENTER | ExpEmpDefaultCostCenter | — |
| END_DATE | ExpEndDate | ✅ |
| EXCHANGE_RATE | ExpExchangeRate | — |
| EXPENSE_CATEGORY_CODE | ExpExpenseCategoryCode | ✅ |
| EXPENSE_CREATION_METHOD_CODE | FullExpExpenseCMC | — |
| EXPENSE_ID | ExpExpenseId | ✅ |
| EXPENSE_REPORT_ID | ExpExpenseReportId | ✅ |
| EXPENSE_SOURCE | ExpExpenseSource | ✅ |
| EXPENSE_TEMPLATE_ID | ExpExpenseTemplateId | — |
| EXPENSE_TYPE_CATEGORY_CODE | ExpExpenseTypeCategoryCode | ✅ |
| EXPENSE_TYPE_ID | ExpExpenseTypeId | — |
| FLIGHT_NUMBER | ExpFlightNumber | ✅ |
| FUEL_TYPE | ExpFuelType | ✅ |
| FUNC_CURRENCY_AMOUNT | ExpFuncCurrencyAmount | — |
| IMG_RECEIPT_REQUIRED_FLAG | ExpImgReceiptRequiredFlag | — |
| INACTIVE_EMP_PROCESS_ID | ExpInactiveEmpProcessId | — |
| ITEMIZATION_PARENT_EXPENSE_ID | ExpItemizationParentExpenseId | — |
| JUSTIFICATION | ExpJustification | ✅ |
| JUSTIFICATION_REQUIRED_FLAG | ExpJustificationRequiredFlag | ✅ |
| LAST_UPDATE_DATE | ExpLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ExpLastUpdateLogin | — |
| LAST_UPDATED_BY | ExpLastUpdatedBy | ✅ |
| LICENSE_PLATE_NUMBER | ExpLicensePlateNumber | — |
| LOCATION | ExpLocation | ✅ |
| LOCATION_ID | ExpLocationId | — |
| MERCHANT_DOCUMENT_NUMBER | ExpMerchantDocumentNumber | ✅ |
| MERCHANT_NAME | ExpMerchantName | ✅ |
| MERCHANT_REFERENCE | ExpMerchantReference | — |
| MERCHANT_TAX_REG_NUMBER | ExpMerchantTaxRegNumber | — |
| MERCHANT_TAXPAYER_ID | ExpMerchantTaxpayerId | — |
| MILEAGE_RATE_ADJUSTED_FLAG | ExpMileageRateAdjustedFlag | — |
| NUMBER_OF_ATTENDEES | ExpNumberOfAttendees | ✅ |
| NUMBER_PEOPLE | ExpNumberPeople | — |
| OBJECT_VERSION_NUMBER | ExpObjectVersionNumber | — |
| ORG_ID | ExpOrgId | — |
| ORIG_EXCHANGE_RATE | ExpOrigExchangeRate | — |
| ORIG_EXPENSE_TYPE_ID | ExpOrigExpenseTypeId | — |
| ORIG_RECEIPT_AMOUNT | ExpOrigReceiptAmount | — |
| ORIG_REIMBURSABLE_AMOUNT | ExpOrigReimbursableAmount | — |
| PASSENGER_AMOUNT | ExpPassengerAmount | — |
| PASSENGER_RATE_TYPE | ExpPassengerRateType | — |
| PERSON_ID | ExpPersonId | — |
| PERSONAL_RECEIPT_AMOUNT | ExpPersonalReceiptAmount | — |
| POLICY_SHORTPAY_FLAG | ExpPolicyShortpayFlag | ✅ |
| POLICY_VIOLATED_FLAG | ExpPolicyViolatedFlag | ✅ |
| PREPARER_ID | ExpPreparerId | — |
| RANGE_HIGH | ExpRangeHigh | — |
| RANGE_LOW | ExpRangeLow | — |
| RATE_PER_PASSENGER | ExpRatePerPassenger | — |
| RECEIPT_AMOUNT | ExpReceiptAmount | — |
| RECEIPT_CURRENCY_CODE | ExpReceiptCurrencyCode | ✅ |
| RECEIPT_MISSING_DEC_REQ_FLAG | ExpReceiptMissingDecReqFlag | — |
| RECEIPT_MISSING_FLAG | ExpReceiptMissingFlag | ✅ |
| RECEIPT_REQUIRED_FLAG | ExpReceiptRequiredFlag | ✅ |
| RECEIPT_VERIFIED_FLAG | ExpReceiptVerifiedFlag | ✅ |
| REIMBURSABLE_AMOUNT | ExpReimbursableAmount | — |
| REIMBURSEMENT_CURRENCY_CODE | ExpReimbursementCurrencyCode | — |
| SEQUENCE_NUM | ExpSequenceNum | — |
| START_DATE | ExpStartDate | ✅ |
| TAX_CLASSIFICATION_CODE | ExpTaxClassificationCode | ✅ |
| TICKET_CLASS_CODE | ExpTicketClassCode | ✅ |
| TICKET_NUMBER | ExpTicketNumber | ✅ |
| TRAVEL_TYPE | ExpTravelType | ✅ |
| TRIP_DISTANCE | ExpTripDistance | ✅ |
| TRXN_AVAILABLE_DATE | ExpTrxnAvailableDate | — |
| UOM_DAYS | ExpUomDays | — |
| VEHICLE_CATEGORY_CODE | ExpVehicleCategoryCode | ✅ |
| VEHICLE_TYPE | ExpVehicleType | ✅ |

---

## 📚 Referências

- [Oracle Docs — EXM_EXPENSES](https://docs.oracle.com/en/cloud/saas/financials/25a/oedmf/exmexpenses.html)
- [[ap-module-data-dictionary]] — Dossiê do módulo AP
