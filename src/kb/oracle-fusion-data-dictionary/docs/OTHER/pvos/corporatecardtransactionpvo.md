---
id: DOC-OTHER-PVO-CorporateCardTransactionPVO
doc_type: system-doc
title: "CorporateCardTransactionPVO — PVO Cross-Module"
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
  - CorporateCardTransactionPVO
  - corporatecardtransactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CorporateCardTransactionPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Corporate Card Transaction. Acessa as tabelas: EXM_CARDS, EXM_CREDIT_CARD_TRXNS, EXM_EXPENSES (+5).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.CorporateCardTransactionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 366 | 8 | 1 | 38 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[exm_cards|EXM_CARDS]] — 27 atributos
- [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]] — 146 atributos (1 PKs, 36 BICC)
- [[exm_expenses|EXM_EXPENSES]] — 90 atributos
- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 52 atributos
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 23 atributos (2 BICC)
- [[per_users|PER_USERS]] — 20 atributos

---

## ⚙️ Atributos

### [[exm_cards|EXM_CARDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardPEOAccountCategoryCode | ACCOUNT_CATEGORY_CODE | — | — |
| 2 | CardPEOAccountTypeCode | ACCOUNT_TYPE_CODE | — | — |
| 3 | CardPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 4 | CardPEOCardExpirationDate | CARD_EXPIRATION_DATE | — | — |
| 5 | CardPEOCardId | CARD_ID | — | — |
| 6 | CardPEOCardNumber | CARD_NUMBER | — | — |
| 7 | CardPEOCardPEOPersonId | PERSON_ID | — | — |
| 8 | CardPEOCardProgramId | CARD_PROGRAM_ID | — | — |
| 9 | CardPEOCardReferenceId | CARD_REFERENCE_ID | — | — |
| 10 | CardPEOCardStatusCode | CARD_STATUS_CODE | — | — |
| 11 | CardPEOCardmemberName | CARDMEMBER_NAME | — | — |
| 12 | CardPEOCompanyAccountId | COMPANY_ACCOUNT_ID | — | — |
| 13 | CardPEOCreatedBy | CREATED_BY | — | — |
| 14 | CardPEOCreationDate | CREATION_DATE | — | — |
| 15 | CardPEODescription | DESCRIPTION | — | — |
| 16 | CardPEOInactiveDate | INACTIVE_DATE | — | — |
| 17 | CardPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 18 | CardPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 19 | CardPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 20 | CardPEOLocationId | LOCATION_ID | — | — |
| 21 | CardPEOMaxPeriodAmount | MAX_PERIOD_AMOUNT | — | — |
| 22 | CardPEOMothersMaidenName | MOTHERS_MAIDEN_NAME | — | — |
| 23 | CardPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 24 | CardPEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 25 | CardPEOProgramName | PROGRAM_NAME | — | — |
| 26 | CardPEORequestId | REQUEST_ID | — | — |
| 27 | CardPEOTrxLimitAmount | TRX_LIMIT_AMOUNT | — | — |

### [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreditCardTrxAirAgencyNumber | AIR_AGENCY_NUMBER | — | — |
| 2 | CreditCardTrxAirArrivalCity | AIR_ARRIVAL_CITY | — | — |
| 3 | CreditCardTrxAirArrivalDate | AIR_ARRIVAL_DATE | — | — |
| 4 | CreditCardTrxAirBaseFareAmount | AIR_BASE_FARE_AMOUNT | — | — |
| 5 | CreditCardTrxAirCarrierAbbreviation | AIR_CARRIER_ABBREVIATION | — | — |
| 6 | CreditCardTrxAirCarrierCode | AIR_CARRIER_CODE | — | — |
| 7 | CreditCardTrxAirDepartureCity | AIR_DEPARTURE_CITY | — | — |
| 8 | CreditCardTrxAirDepartureDate | AIR_DEPARTURE_DATE | — | — |
| 9 | CreditCardTrxAirExchangedTicketNumber | AIR_EXCHANGED_TICKET_NUMBER | — | — |
| 10 | CreditCardTrxAirFareBasisCode | AIR_FARE_BASIS_CODE | — | — |
| 11 | CreditCardTrxAirIssuerCity | AIR_ISSUER_CITY | — | — |
| 12 | CreditCardTrxAirPassengerName | AIR_PASSENGER_NAME | — | — |
| 13 | CreditCardTrxAirRefundTicketNumber | AIR_REFUND_TICKET_NUMBER | — | — |
| 14 | CreditCardTrxAirRouting | AIR_ROUTING | — | — |
| 15 | CreditCardTrxAirServiceClass | AIR_SERVICE_CLASS | — | — |
| 16 | CreditCardTrxAirStopoverFlag | AIR_STOPOVER_FLAG | — | — |
| 17 | CreditCardTrxAirTicketIssuer | AIR_TICKET_ISSUER | — | — |
| 18 | CreditCardTrxAirTicketNumber | AIR_TICKET_NUMBER | — | — |
| 19 | CreditCardTrxAirTotalFeesAmount | AIR_TOTAL_FEES_AMOUNT | — | — |
| 20 | CreditCardTrxAtmCashAdvance | ATM_CASH_ADVANCE | — | — |
| 21 | CreditCardTrxAtmFeeAmount | ATM_FEE_AMOUNT | — | — |
| 22 | CreditCardTrxAtmId | ATM_ID | — | — |
| 23 | CreditCardTrxAtmNetworkId | ATM_NETWORK_ID | — | — |
| 24 | CreditCardTrxAtmTransactionDate | ATM_TRANSACTION_DATE | — | — |
| 25 | CreditCardTrxAtmType | ATM_TYPE | — | — |
| 26 | CreditCardTrxAudioVisualCharges | AUDIO_VISUAL_CHARGES | — | — |
| 27 | CreditCardTrxAuthTrxnNumber | AUTH_TRXN_NUMBER | — | — |
| 28 | CreditCardTrxBanquetCharges | BANQUET_CHARGES | — | — |
| 29 | CreditCardTrxBilledAmount | BILLED_AMOUNT | — | ✅ |
| 30 | CreditCardTrxBilledCurrencyCode | BILLED_CURRENCY_CODE | — | ✅ |
| 31 | CreditCardTrxBilledDate | BILLED_DATE | — | ✅ |
| 32 | CreditCardTrxBilledDecimal | BILLED_DECIMAL | — | — |
| 33 | CreditCardTrxBillingCntlAcctNumber | BILLING_CNTL_ACCT_NUMBER | — | — |
| 34 | CreditCardTrxCarClass | CAR_CLASS | — | — |
| 35 | CreditCardTrxCarDailyRate | CAR_DAILY_RATE | — | — |
| 36 | CreditCardTrxCarGasAmount | CAR_GAS_AMOUNT | — | — |
| 37 | CreditCardTrxCarInsuranceAmount | CAR_INSURANCE_AMOUNT | — | — |
| 38 | CreditCardTrxCarMileageAmount | CAR_MILEAGE_AMOUNT | — | — |
| 39 | CreditCardTrxCarRentalAgreementNumber | CAR_RENTAL_AGREEMENT_NUMBER | — | — |
| 40 | CreditCardTrxCarRentalDate | CAR_RENTAL_DATE | — | — |
| 41 | CreditCardTrxCarRentalDays | CAR_RENTAL_DAYS | — | — |
| 42 | CreditCardTrxCarRentalLocation | CAR_RENTAL_LOCATION | — | — |
| 43 | CreditCardTrxCarRentalState | CAR_RENTAL_STATE | — | — |
| 44 | CreditCardTrxCarRenterName | CAR_RENTER_NAME | — | — |
| 45 | CreditCardTrxCarReturnDate | CAR_RETURN_DATE | — | — |
| 46 | CreditCardTrxCarReturnLocation | CAR_RETURN_LOCATION | — | — |
| 47 | CreditCardTrxCarReturnState | CAR_RETURN_STATE | — | — |
| 48 | CreditCardTrxCarTotalMileage | CAR_TOTAL_MILEAGE | — | — |
| 49 | CreditCardTrxCardAcceptorId | CARD_ACCEPTOR_ID | — | — |
| 50 | CreditCardTrxCardId | CARD_ID | — | — |
| 51 | CreditCardTrxCardIssuerNumber | CARD_ISSUER_NUMBER | — | — |
| 52 | CreditCardTrxCardNumber | CARD_NUMBER | — | — |
| 53 | CreditCardTrxCardProgramId | CARD_PROGRAM_ID | — | — |
| 54 | CreditCardTrxCashAdvances | CASH_ADVANCES | — | — |
| 55 | CreditCardTrxCompanyAccountId | COMPANY_ACCOUNT_ID | — | — |
| 56 | CreditCardTrxCompanyNumber | COMPANY_NUMBER | — | — |
| 57 | CreditCardTrxConferenceRoomCharges | CONFERENCE_ROOM_CHARGES | — | — |
| 58 | CreditCardTrxCreatedBy | CREATED_BY | — | ✅ |
| 59 | CreditCardTrxCreationDate | CREATION_DATE | — | ✅ |
| 60 | CreditCardTrxCreditCardTrxnId | CREDIT_CARD_TRXN_ID | 🔑 | ✅ |
| 61 | CreditCardTrxCurrencyConversionExponent | CURRENCY_CONVERSION_EXPONENT | — | — |
| 62 | CreditCardTrxCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | ✅ |
| 63 | CreditCardTrxDebitFlag | DEBIT_FLAG | — | ✅ |
| 64 | CreditCardTrxDescription | DESCRIPTION | — | ✅ |
| 65 | CreditCardTrxDisputeDate | DISPUTE_DATE | — | — |
| 66 | CreditCardTrxEarlyDepartureCharges | EARLY_DEPARTURE_CHARGES | — | — |
| 67 | CreditCardTrxEmployeeNumber | EMPLOYEE_NUMBER | — | — |
| 68 | CreditCardTrxFinancialCategory | FINANCIAL_CATEGORY | — | — |
| 69 | CreditCardTrxFolioType | FOLIO_TYPE | — | — |
| 70 | CreditCardTrxHotelArrivalDate | HOTEL_ARRIVAL_DATE | — | — |
| 71 | CreditCardTrxHotelBarAmount | HOTEL_BAR_AMOUNT | — | — |
| 72 | CreditCardTrxHotelBusinessAmount | HOTEL_BUSINESS_AMOUNT | — | — |
| 73 | CreditCardTrxHotelCashDisbAmount | HOTEL_CASH_DISB_AMOUNT | — | — |
| 74 | CreditCardTrxHotelChargeDesc | HOTEL_CHARGE_DESC | — | — |
| 75 | CreditCardTrxHotelCity | HOTEL_CITY | — | — |
| 76 | CreditCardTrxHotelDepartDate | HOTEL_DEPART_DATE | — | — |
| 77 | CreditCardTrxHotelFolioNumber | HOTEL_FOLIO_NUMBER | — | — |
| 78 | CreditCardTrxHotelGiftShopAmount | HOTEL_GIFT_SHOP_AMOUNT | — | — |
| 79 | CreditCardTrxHotelGuestName | HOTEL_GUEST_NAME | — | — |
| 80 | CreditCardTrxHotelHealthAmount | HOTEL_HEALTH_AMOUNT | — | — |
| 81 | CreditCardTrxHotelLaundryAmount | HOTEL_LAUNDRY_AMOUNT | — | — |
| 82 | CreditCardTrxHotelMiscAmount | HOTEL_MISC_AMOUNT | — | — |
| 83 | CreditCardTrxHotelMovieAmount | HOTEL_MOVIE_AMOUNT | — | — |
| 84 | CreditCardTrxHotelNoShowFlag | HOTEL_NO_SHOW_FLAG | — | — |
| 85 | CreditCardTrxHotelParkingAmount | HOTEL_PARKING_AMOUNT | — | — |
| 86 | CreditCardTrxHotelRestaurantAmount | HOTEL_RESTAURANT_AMOUNT | — | — |
| 87 | CreditCardTrxHotelRoomAmount | HOTEL_ROOM_AMOUNT | — | — |
| 88 | CreditCardTrxHotelRoomRate | HOTEL_ROOM_RATE | — | — |
| 89 | CreditCardTrxHotelRoomServiceAmount | HOTEL_ROOM_SERVICE_AMOUNT | — | — |
| 90 | CreditCardTrxHotelRoomTax | HOTEL_ROOM_TAX | — | — |
| 91 | CreditCardTrxHotelRoomType | HOTEL_ROOM_TYPE | — | — |
| 92 | CreditCardTrxHotelState | HOTEL_STATE | — | — |
| 93 | CreditCardTrxHotelStayDuration | HOTEL_STAY_DURATION | — | — |
| 94 | CreditCardTrxHotelTelephoneAmount | HOTEL_TELEPHONE_AMOUNT | — | — |
| 95 | CreditCardTrxHotelTipAmount | HOTEL_TIP_AMOUNT | — | — |
| 96 | CreditCardTrxHotelTransportationAmount | HOTEL_TRANSPORTATION_AMOUNT | — | — |
| 97 | CreditCardTrxInterbankCardassocNumber | INTERBANK_CARDASSOC_NUMBER | — | — |
| 98 | CreditCardTrxInternetAccessCharges | INTERNET_ACCESS_CHARGES | — | — |
| 99 | CreditCardTrxLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 100 | CreditCardTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 101 | CreditCardTrxLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 102 | CreditCardTrxLocalTax | LOCAL_TAX | — | — |
| 103 | CreditCardTrxMarketCode | MARKET_CODE | — | — |
| 104 | CreditCardTrxMerchantActivity | MERCHANT_ACTIVITY | — | — |
| 105 | CreditCardTrxMerchantAddress1 | MERCHANT_ADDRESS1 | — | ✅ |
| 106 | CreditCardTrxMerchantAddress2 | MERCHANT_ADDRESS2 | — | ✅ |
| 107 | CreditCardTrxMerchantAddress3 | MERCHANT_ADDRESS3 | — | ✅ |
| 108 | CreditCardTrxMerchantAddress4 | MERCHANT_ADDRESS4 | — | ✅ |
| 109 | CreditCardTrxMerchantCategoryCode | MERCHANT_CATEGORY_CODE | — | ✅ |
| 110 | CreditCardTrxMerchantCity | MERCHANT_CITY | — | ✅ |
| 111 | CreditCardTrxMerchantCountry | MERCHANT_COUNTRY | — | ✅ |
| 112 | CreditCardTrxMerchantName1 | MERCHANT_NAME1 | — | ✅ |
| 113 | CreditCardTrxMerchantName2 | MERCHANT_NAME2 | — | ✅ |
| 114 | CreditCardTrxMerchantPostalCode | MERCHANT_POSTAL_CODE | — | ✅ |
| 115 | CreditCardTrxMerchantProvinceState | MERCHANT_PROVINCE_STATE | — | ✅ |
| 116 | CreditCardTrxMerchantReference | MERCHANT_REFERENCE | — | ✅ |
| 117 | CreditCardTrxMerchantTaxId | MERCHANT_TAX_ID | — | ✅ |
| 118 | CreditCardTrxMiniBarAmount | MINI_BAR_AMOUNT | — | — |
| 119 | CreditCardTrxMisIndustryCode | MIS_INDUSTRY_CODE | — | ✅ |
| 120 | CreditCardTrxNationalTax | NATIONAL_TAX | — | — |
| 121 | CreditCardTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | CreditCardTrxOtherTax | OTHER_TAX | — | — |
| 123 | CreditCardTrxPaymentDueFromCode | PAYMENT_DUE_FROM_CODE | — | — |
| 124 | CreditCardTrxPaymentFlag | PAYMENT_FLAG | — | ✅ |
| 125 | CreditCardTrxPostedAmount | POSTED_AMOUNT | — | ✅ |
| 126 | CreditCardTrxPostedCurrencyCode | POSTED_CURRENCY_CODE | — | ✅ |
| 127 | CreditCardTrxPostedDate | POSTED_DATE | — | ✅ |
| 128 | CreditCardTrxPostedDecimal | POSTED_DECIMAL | — | — |
| 129 | CreditCardTrxRecordType | RECORD_TYPE | — | — |
| 130 | CreditCardTrxReferenceNumber | REFERENCE_NUMBER | — | ✅ |
| 131 | CreditCardTrxReqCntlAcctNumber | REQ_CNTL_ACCT_NUMBER | — | — |
| 132 | CreditCardTrxRequestId | REQUEST_ID | — | — |
| 133 | CreditCardTrxRestaurantBeverageAmount | RESTAURANT_BEVERAGE_AMOUNT | — | — |
| 134 | CreditCardTrxRestaurantFoodAmount | RESTAURANT_FOOD_AMOUNT | — | — |
| 135 | CreditCardTrxRestaurantTipAmount | RESTAURANT_TIP_AMOUNT | — | — |
| 136 | CreditCardTrxReviewedFlag | REVIEWED_FLAG | — | — |
| 137 | CreditCardTrxSicCode | SIC_CODE | — | ✅ |
| 138 | CreditCardTrxTotalTax | TOTAL_TAX | — | — |
| 139 | CreditCardTrxTransactionAmount | TRANSACTION_AMOUNT | — | ✅ |
| 140 | CreditCardTrxTransactionDate | TRANSACTION_DATE | — | ✅ |
| 141 | CreditCardTrxTransactionStatus | TRANSACTION_STATUS | — | ✅ |
| 142 | CreditCardTrxTransactionType | TRANSACTION_TYPE | — | ✅ |
| 143 | CreditCardTrxTransportationCharges | TRANSPORTATION_CHARGES | — | — |
| 144 | CreditCardTrxTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 145 | CreditCardTrxTrxnDetailFlag | TRXN_DETAIL_FLAG | — | — |
| 146 | CreditCardTrxValidateCode | VALIDATE_CODE | — | ✅ |

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpensePEOAllocationReason | ALLOCATION_REASON | — | — |
| 2 | ExpensePEOAllocationSplitCode | ALLOCATION_SPLIT_CODE | — | — |
| 3 | ExpensePEOAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | ExpensePEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 5 | ExpensePEOAuditAdjustmentReason | AUDIT_ADJUSTMENT_REASON | — | — |
| 6 | ExpensePEOAuditAdjustmentReasonCode | AUDIT_ADJUSTMENT_REASON_CODE | — | — |
| 7 | ExpensePEOAvgMileageRate | AVG_MILEAGE_RATE | — | — |
| 8 | ExpensePEOAwtGroupId | AWT_GROUP_ID | — | — |
| 9 | ExpensePEOCardId | CARD_ID | — | — |
| 10 | ExpensePEOCcPrepaidInvoiceId | CC_PREPAID_INVOICE_ID | — | — |
| 11 | ExpensePEOCcPrepaidRequestId | CC_PREPAID_REQUEST_ID | — | — |
| 12 | ExpensePEOCheckoutDate | CHECKOUT_DATE | — | — |
| 13 | ExpensePEOCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 14 | ExpensePEOCreatedBy | CREATED_BY | — | — |
| 15 | ExpensePEOCreationDate | CREATION_DATE | — | — |
| 16 | ExpensePEOCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 17 | ExpensePEODailyDistance | DAILY_DISTANCE | — | — |
| 18 | ExpensePEODepartureLocationId | DEPARTURE_LOCATION_ID | — | — |
| 19 | ExpensePEODescription | DESCRIPTION | — | — |
| 20 | ExpensePEODestinationFrom | DESTINATION_FROM | — | — |
| 21 | ExpensePEODestinationTo | DESTINATION_TO | — | — |
| 22 | ExpensePEODistanceUnitCode | DISTANCE_UNIT_CODE | — | — |
| 23 | ExpensePEOEmpDefaultCostCenter | EMP_DEFAULT_COST_CENTER | — | — |
| 24 | ExpensePEOEndDate | END_DATE | — | — |
| 25 | ExpensePEOExchangeRate | EXCHANGE_RATE | — | — |
| 26 | ExpensePEOExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | — |
| 27 | ExpensePEOExpenseCreationMethodCode | EXPENSE_CREATION_METHOD_CODE | — | — |
| 28 | ExpensePEOExpenseId | EXPENSE_ID | — | — |
| 29 | ExpensePEOExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 30 | ExpensePEOExpenseSource | EXPENSE_SOURCE | — | — |
| 31 | ExpensePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 32 | ExpensePEOExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | — |
| 33 | ExpensePEOExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 34 | ExpensePEOFlightNumber | FLIGHT_NUMBER | — | — |
| 35 | ExpensePEOFuelType | FUEL_TYPE | — | — |
| 36 | ExpensePEOFuncCurrencyAmount | FUNC_CURRENCY_AMOUNT | — | — |
| 37 | ExpensePEOImgReceiptRequiredFlag | IMG_RECEIPT_REQUIRED_FLAG | — | — |
| 38 | ExpensePEOInactiveEmpProcessId | INACTIVE_EMP_PROCESS_ID | — | — |
| 39 | ExpensePEOItemizationParentExpenseId | ITEMIZATION_PARENT_EXPENSE_ID | — | — |
| 40 | ExpensePEOJustification | JUSTIFICATION | — | — |
| 41 | ExpensePEOJustificationRequiredFlag | JUSTIFICATION_REQUIRED_FLAG | — | — |
| 42 | ExpensePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 43 | ExpensePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 44 | ExpensePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 45 | ExpensePEOLicensePlateNumber | LICENSE_PLATE_NUMBER | — | — |
| 46 | ExpensePEOLocation | LOCATION | — | — |
| 47 | ExpensePEOLocationId | LOCATION_ID | — | — |
| 48 | ExpensePEOMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | — |
| 49 | ExpensePEOMerchantName | MERCHANT_NAME | — | — |
| 50 | ExpensePEOMerchantReference | MERCHANT_REFERENCE | — | — |
| 51 | ExpensePEOMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 52 | ExpensePEOMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 53 | ExpensePEOMileageRateAdjustedFlag | MILEAGE_RATE_ADJUSTED_FLAG | — | — |
| 54 | ExpensePEONumberOfAttendees | NUMBER_OF_ATTENDEES | — | — |
| 55 | ExpensePEONumberPeople | NUMBER_PEOPLE | — | — |
| 56 | ExpensePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 57 | ExpensePEOOrgId | ORG_ID | — | — |
| 58 | ExpensePEOOrigExchangeRate | ORIG_EXCHANGE_RATE | — | — |
| 59 | ExpensePEOOrigExpenseTypeId | ORIG_EXPENSE_TYPE_ID | — | — |
| 60 | ExpensePEOOrigReceiptAmount | ORIG_RECEIPT_AMOUNT | — | — |
| 61 | ExpensePEOOrigReimbursableAmount | ORIG_REIMBURSABLE_AMOUNT | — | — |
| 62 | ExpensePEOPassengerAmount | PASSENGER_AMOUNT | — | — |
| 63 | ExpensePEOPassengerRateType | PASSENGER_RATE_TYPE | — | — |
| 64 | ExpensePEOPersonId | PERSON_ID | — | — |
| 65 | ExpensePEOPersonalReceiptAmount | PERSONAL_RECEIPT_AMOUNT | — | — |
| 66 | ExpensePEOPolicyShortpayFlag | POLICY_SHORTPAY_FLAG | — | — |
| 67 | ExpensePEOPolicyViolatedFlag | POLICY_VIOLATED_FLAG | — | — |
| 68 | ExpensePEOPreparerId | PREPARER_ID | — | — |
| 69 | ExpensePEORangeHigh | RANGE_HIGH | — | — |
| 70 | ExpensePEORangeLow | RANGE_LOW | — | — |
| 71 | ExpensePEORatePerPassenger | RATE_PER_PASSENGER | — | — |
| 72 | ExpensePEOReceiptAmount | RECEIPT_AMOUNT | — | — |
| 73 | ExpensePEOReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | — |
| 74 | ExpensePEOReceiptMissingDecReqFlag | RECEIPT_MISSING_DEC_REQ_FLAG | — | — |
| 75 | ExpensePEOReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | — |
| 76 | ExpensePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 77 | ExpensePEOReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | — |
| 78 | ExpensePEOReimbursableAmount | REIMBURSABLE_AMOUNT | — | — |
| 79 | ExpensePEOReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 80 | ExpensePEOSequenceNum | SEQUENCE_NUM | — | — |
| 81 | ExpensePEOStartDate | START_DATE | — | — |
| 82 | ExpensePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |
| 83 | ExpensePEOTicketClassCode | TICKET_CLASS_CODE | — | — |
| 84 | ExpensePEOTicketNumber | TICKET_NUMBER | — | — |
| 85 | ExpensePEOTravelType | TRAVEL_TYPE | — | — |
| 86 | ExpensePEOTripDistance | TRIP_DISTANCE | — | — |
| 87 | ExpensePEOTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 88 | ExpensePEOUomDays | UOM_DAYS | — | — |
| 89 | ExpensePEOVehicleCategoryCode | VEHICLE_CATEGORY_CODE | — | — |
| 90 | ExpensePEOVehicleType | VEHICLE_TYPE | — | — |

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrApplyCashAdvFlag | APPLY_CASH_ADV_FLAG | — | — |
| 2 | ExpHdrAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | ExpHdrAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 4 | ExpHdrAuditCode | AUDIT_CODE | — | — |
| 5 | ExpHdrAuditPriorMgrStatusCode | AUDIT_PRIOR_MGR_STATUS_CODE | — | — |
| 6 | ExpHdrAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 7 | ExpHdrAwtGroupId1 | AWT_GROUP_ID | — | — |
| 8 | ExpHdrBothpayFlag | BOTHPAY_FLAG | — | — |
| 9 | ExpHdrCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | — |
| 10 | ExpHdrCreatedBy2 | CREATED_BY | — | — |
| 11 | ExpHdrCreationDate2 | CREATION_DATE | — | — |
| 12 | ExpHdrCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 13 | ExpHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 14 | ExpHdrExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 15 | ExpHdrExpenseReportDate | EXPENSE_REPORT_DATE | — | — |
| 16 | ExpHdrExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 17 | ExpHdrExpenseReportNum | EXPENSE_REPORT_NUM | — | — |
| 18 | ExpHdrExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 19 | ExpHdrExpenseStatusCode | EXPENSE_STATUS_CODE | — | — |
| 20 | ExpHdrExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 21 | ExpHdrExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 22 | ExpHdrExportRequestId | EXPORT_REQUEST_ID | — | — |
| 23 | ExpHdrFinalApprovalDate | FINAL_APPROVAL_DATE | — | — |
| 24 | ExpHdrHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 25 | ExpHdrImagedReceiptsReceivedDate | IMAGED_RECEIPTS_RECEIVED_DATE | — | — |
| 26 | ExpHdrImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | — |
| 27 | ExpHdrLastAuditBy | LAST_AUDIT_BY | — | — |
| 28 | ExpHdrLastUpdateDate2 | LAST_UPDATE_DATE | — | — |
| 29 | ExpHdrLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 30 | ExpHdrLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 31 | ExpHdrMissingImagesReason | MISSING_IMAGES_REASON | — | — |
| 32 | ExpHdrObjectVersionNumber3 | OBJECT_VERSION_NUMBER | — | — |
| 33 | ExpHdrOrgId | ORG_ID | — | — |
| 34 | ExpHdrOverdueRcptCorrelationId | OVERDUE_RCPT_CORRELATION_ID | — | — |
| 35 | ExpHdrOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 36 | ExpHdrParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 37 | ExpHdrPaymentHoldCorrelationId | PAYMENT_HOLD_CORRELATION_ID | — | — |
| 38 | ExpHdrPaymentMethodCode | PAYMENT_METHOD_CODE | — | — |
| 39 | ExpHdrPersonId | PERSON_ID | — | — |
| 40 | ExpHdrPreparerId1 | PREPARER_ID | — | — |
| 41 | ExpHdrPurpose | PURPOSE | — | — |
| 42 | ExpHdrReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 43 | ExpHdrReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | — |
| 44 | ExpHdrReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | — |
| 45 | ExpHdrReimbursementCurrencyCode1 | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 46 | ExpHdrReportCreationMethodCode | REPORT_CREATION_METHOD_CODE | — | — |
| 47 | ExpHdrReportSubmitDate | REPORT_SUBMIT_DATE | — | — |
| 48 | ExpHdrShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 49 | ExpHdrTripId | TRIP_ID | — | — |
| 50 | ExpHdrUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 51 | ExpHdrUnappliedCashAdvReason | UNAPPLIED_CASH_ADV_REASON | — | — |
| 52 | ExpHdrWorkflowCorrelationId | WORKFLOW_CORRELATION_ID | — | — |

### [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrganizationEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | OrganizationEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | OrganizationLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 4 | OrganizationOrganizationId | ORGANIZATION_ID | — | — |

### [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BUPrimaryLedgerId | ORG_INFORMATION3 | — | — |
| 2 | OrgInfoEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | OrgInfoEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | OrgInfoOrgInformationId | ORG_INFORMATION_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardPersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | CardPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | CardPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | CardPersonCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | CardPersonCreatedByPersonId | PERSON_ID | — | — |
| 6 | CardPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 7 | CardPersonUpdatedbyDisplayName | DISPLAY_NAME | — | — |
| 8 | CardPersonUpdatedbyEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 9 | CardPersonUpdatedbyEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 10 | CardPersonUpdatedbyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | CardPersonUpdatedbyPersonId | PERSON_ID | — | — |
| 12 | CardPersonUpdatedbyPersonNameId | PERSON_NAME_ID | — | — |
| 13 | TrnxPersonCreatedbyDisplayName | DISPLAY_NAME | — | ✅ |
| 14 | TrnxPersonCreatedbyEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 15 | TrnxPersonCreatedbyEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 16 | TrnxPersonCreatedbyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TrnxPersonCreatedbyPersonId | PERSON_ID | — | — |
| 18 | TrnxPersonCreatedbyPersonNameId | PERSON_NAME_ID | — | — |
| 19 | TrnxPersonUpdatedbyDisplayName | DISPLAY_NAME | — | ✅ |
| 20 | TrnxPersonUpdatedbyEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 21 | TrnxPersonUpdatedbyEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 22 | TrnxPersonUpdatedbyPersonId | PERSON_ID | — | — |
| 23 | TrnxPersonUpdatedbyPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CardCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | CardCreatedByPersonId | PERSON_ID | — | — |
| 3 | CardCreatedByUserGuid | USER_GUID | — | — |
| 4 | CardCreatedByUserId | USER_ID | — | — |
| 5 | CardCreatedByUsername | USERNAME | — | — |
| 6 | CardUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | CardUserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | CardUserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | CardUserUpdatedByUserId | USER_ID | — | — |
| 10 | CardUserUpdatedByUsername | USERNAME | — | — |
| 11 | TrnxCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | TrnxCreatedByPersonId | PERSON_ID | — | — |
| 13 | TrnxCreatedByUserGuid | USER_GUID | — | — |
| 14 | TrnxCreatedByUserId | USER_ID | — | — |
| 15 | TrnxCreatedByUsername | USERNAME | — | — |
| 16 | TrnxUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | TrnxUserUpdatedByPersonId | PERSON_ID | — | — |
| 18 | TrnxUserUpdatedByUserGuid | USER_GUID | — | — |
| 19 | TrnxUserUpdatedByUserId | USER_ID | — | — |
| 20 | TrnxUserUpdatedByUsername | USERNAME | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
