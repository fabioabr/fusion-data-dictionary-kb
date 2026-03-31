---
id: DOC-OTHER-PVO-ExpensePVO
doc_type: system-doc
title: "ExpensePVO — PVO Cross-Module"
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
  - ExpensePVO
  - expensepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExpensePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Expense. Acessa as tabelas: EXM_CREDIT_CARD_TRXNS, EXM_EXPENSES, EXM_EXPENSE_DISTS (+10).

**Caminho:** `FscmTopModelAM.FinExmEntrySharedAM.ExpensePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 635 | 13 | 1 | 89 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]] — 146 atributos (2 BICC)
- [[exm_expenses|EXM_EXPENSES]] — 98 atributos (1 PKs, 47 BICC)
- [[exm_expense_dists|EXM_EXPENSE_DISTS]] — 75 atributos
- [[exm_expense_reports|EXM_EXPENSE_REPORTS]] — 112 atributos (25 BICC)
- [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]] — 21 atributos (2 BICC)
- [[exm_expense_types|EXM_EXPENSE_TYPES]] — 27 atributos (2 BICC)
- [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]] — 18 atributos (1 BICC)
- [[hr_all_organization_units_f|HR_ALL_ORGANIZATION_UNITS_F]] — 4 atributos
- [[hr_organization_information_f|HR_ORGANIZATION_INFORMATION_F]] — 4 atributos
- [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]] — 8 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 82 atributos (7 BICC)
- [[per_users|PER_USERS]] — 20 atributos
- [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]] — 20 atributos (2 BICC)

---

## ⚙️ Atributos

### [[exm_credit_card_trxns|EXM_CREDIT_CARD_TRXNS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpCreditCardTrxAirAgencyNumber | AIR_AGENCY_NUMBER | — | — |
| 2 | ExpCreditCardTrxAirArrivalCity | AIR_ARRIVAL_CITY | — | — |
| 3 | ExpCreditCardTrxAirArrivalDate | AIR_ARRIVAL_DATE | — | — |
| 4 | ExpCreditCardTrxAirBaseFareAmount | AIR_BASE_FARE_AMOUNT | — | — |
| 5 | ExpCreditCardTrxAirCarrierAbbreviation | AIR_CARRIER_ABBREVIATION | — | — |
| 6 | ExpCreditCardTrxAirCarrierCode | AIR_CARRIER_CODE | — | — |
| 7 | ExpCreditCardTrxAirDepartureCity | AIR_DEPARTURE_CITY | — | — |
| 8 | ExpCreditCardTrxAirDepartureDate | AIR_DEPARTURE_DATE | — | — |
| 9 | ExpCreditCardTrxAirExchangedTicketNumber | AIR_EXCHANGED_TICKET_NUMBER | — | — |
| 10 | ExpCreditCardTrxAirFareBasisCode | AIR_FARE_BASIS_CODE | — | — |
| 11 | ExpCreditCardTrxAirIssuerCity | AIR_ISSUER_CITY | — | — |
| 12 | ExpCreditCardTrxAirPassengerName | AIR_PASSENGER_NAME | — | — |
| 13 | ExpCreditCardTrxAirRefundTicketNumber | AIR_REFUND_TICKET_NUMBER | — | — |
| 14 | ExpCreditCardTrxAirRouting | AIR_ROUTING | — | — |
| 15 | ExpCreditCardTrxAirServiceClass | AIR_SERVICE_CLASS | — | — |
| 16 | ExpCreditCardTrxAirStopoverFlag | AIR_STOPOVER_FLAG | — | — |
| 17 | ExpCreditCardTrxAirTicketIssuer | AIR_TICKET_ISSUER | — | — |
| 18 | ExpCreditCardTrxAirTicketNumber | AIR_TICKET_NUMBER | — | — |
| 19 | ExpCreditCardTrxAirTotalFeesAmount | AIR_TOTAL_FEES_AMOUNT | — | — |
| 20 | ExpCreditCardTrxAtmCashAdvance | ATM_CASH_ADVANCE | — | — |
| 21 | ExpCreditCardTrxAtmFeeAmount | ATM_FEE_AMOUNT | — | — |
| 22 | ExpCreditCardTrxAtmId | ATM_ID | — | — |
| 23 | ExpCreditCardTrxAtmNetworkId | ATM_NETWORK_ID | — | — |
| 24 | ExpCreditCardTrxAtmTransactionDate | ATM_TRANSACTION_DATE | — | — |
| 25 | ExpCreditCardTrxAtmType | ATM_TYPE | — | — |
| 26 | ExpCreditCardTrxAudioVisualCharges | AUDIO_VISUAL_CHARGES | — | — |
| 27 | ExpCreditCardTrxAuthTrxnNumber | AUTH_TRXN_NUMBER | — | — |
| 28 | ExpCreditCardTrxBanquetCharges | BANQUET_CHARGES | — | — |
| 29 | ExpCreditCardTrxBilledAmount | BILLED_AMOUNT | — | — |
| 30 | ExpCreditCardTrxBilledCurrencyCode | BILLED_CURRENCY_CODE | — | — |
| 31 | ExpCreditCardTrxBilledDate | BILLED_DATE | — | — |
| 32 | ExpCreditCardTrxBilledDecimal | BILLED_DECIMAL | — | — |
| 33 | ExpCreditCardTrxBillingCntlAcctNumber | BILLING_CNTL_ACCT_NUMBER | — | — |
| 34 | ExpCreditCardTrxCarClass | CAR_CLASS | — | — |
| 35 | ExpCreditCardTrxCarDailyRate | CAR_DAILY_RATE | — | — |
| 36 | ExpCreditCardTrxCarGasAmount | CAR_GAS_AMOUNT | — | — |
| 37 | ExpCreditCardTrxCarInsuranceAmount | CAR_INSURANCE_AMOUNT | — | — |
| 38 | ExpCreditCardTrxCarMileageAmount | CAR_MILEAGE_AMOUNT | — | — |
| 39 | ExpCreditCardTrxCarRentalAgreementNumber | CAR_RENTAL_AGREEMENT_NUMBER | — | — |
| 40 | ExpCreditCardTrxCarRentalDate | CAR_RENTAL_DATE | — | — |
| 41 | ExpCreditCardTrxCarRentalDays | CAR_RENTAL_DAYS | — | — |
| 42 | ExpCreditCardTrxCarRentalLocation | CAR_RENTAL_LOCATION | — | — |
| 43 | ExpCreditCardTrxCarRentalState | CAR_RENTAL_STATE | — | — |
| 44 | ExpCreditCardTrxCarRenterName | CAR_RENTER_NAME | — | — |
| 45 | ExpCreditCardTrxCarReturnDate | CAR_RETURN_DATE | — | — |
| 46 | ExpCreditCardTrxCarReturnLocation | CAR_RETURN_LOCATION | — | — |
| 47 | ExpCreditCardTrxCarReturnState | CAR_RETURN_STATE | — | — |
| 48 | ExpCreditCardTrxCarTotalMileage | CAR_TOTAL_MILEAGE | — | — |
| 49 | ExpCreditCardTrxCardAcceptorId | CARD_ACCEPTOR_ID | — | — |
| 50 | ExpCreditCardTrxCardId | CARD_ID | — | — |
| 51 | ExpCreditCardTrxCardIssuerNumber | CARD_ISSUER_NUMBER | — | — |
| 52 | ExpCreditCardTrxCardNumber | CARD_NUMBER | — | — |
| 53 | ExpCreditCardTrxCardProgramId | CARD_PROGRAM_ID | — | — |
| 54 | ExpCreditCardTrxCashAdvances | CASH_ADVANCES | — | — |
| 55 | ExpCreditCardTrxCompanyAccountId | COMPANY_ACCOUNT_ID | — | — |
| 56 | ExpCreditCardTrxCompanyNumber | COMPANY_NUMBER | — | — |
| 57 | ExpCreditCardTrxConferenceRoomCharges | CONFERENCE_ROOM_CHARGES | — | — |
| 58 | ExpCreditCardTrxCreatedBy | CREATED_BY | — | — |
| 59 | ExpCreditCardTrxCreationDate | CREATION_DATE | — | — |
| 60 | ExpCreditCardTrxCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | — |
| 61 | ExpCreditCardTrxCurrencyConversionExponent | CURRENCY_CONVERSION_EXPONENT | — | — |
| 62 | ExpCreditCardTrxCurrencyConversionRate | CURRENCY_CONVERSION_RATE | — | — |
| 63 | ExpCreditCardTrxDebitFlag | DEBIT_FLAG | — | — |
| 64 | ExpCreditCardTrxDescription | DESCRIPTION | — | — |
| 65 | ExpCreditCardTrxDisputeDate | DISPUTE_DATE | — | — |
| 66 | ExpCreditCardTrxEarlyDepartureCharges | EARLY_DEPARTURE_CHARGES | — | — |
| 67 | ExpCreditCardTrxEmployeeNumber | EMPLOYEE_NUMBER | — | — |
| 68 | ExpCreditCardTrxFinancialCategory | FINANCIAL_CATEGORY | — | — |
| 69 | ExpCreditCardTrxFolioType | FOLIO_TYPE | — | — |
| 70 | ExpCreditCardTrxHotelArrivalDate | HOTEL_ARRIVAL_DATE | — | — |
| 71 | ExpCreditCardTrxHotelBarAmount | HOTEL_BAR_AMOUNT | — | — |
| 72 | ExpCreditCardTrxHotelBusinessAmount | HOTEL_BUSINESS_AMOUNT | — | — |
| 73 | ExpCreditCardTrxHotelCashDisbAmount | HOTEL_CASH_DISB_AMOUNT | — | — |
| 74 | ExpCreditCardTrxHotelChargeDesc | HOTEL_CHARGE_DESC | — | — |
| 75 | ExpCreditCardTrxHotelCity | HOTEL_CITY | — | — |
| 76 | ExpCreditCardTrxHotelDepartDate | HOTEL_DEPART_DATE | — | — |
| 77 | ExpCreditCardTrxHotelFolioNumber | HOTEL_FOLIO_NUMBER | — | — |
| 78 | ExpCreditCardTrxHotelGiftShopAmount | HOTEL_GIFT_SHOP_AMOUNT | — | — |
| 79 | ExpCreditCardTrxHotelGuestName | HOTEL_GUEST_NAME | — | — |
| 80 | ExpCreditCardTrxHotelHealthAmount | HOTEL_HEALTH_AMOUNT | — | — |
| 81 | ExpCreditCardTrxHotelLaundryAmount | HOTEL_LAUNDRY_AMOUNT | — | — |
| 82 | ExpCreditCardTrxHotelMiscAmount | HOTEL_MISC_AMOUNT | — | — |
| 83 | ExpCreditCardTrxHotelMovieAmount | HOTEL_MOVIE_AMOUNT | — | — |
| 84 | ExpCreditCardTrxHotelNoShowFlag | HOTEL_NO_SHOW_FLAG | — | — |
| 85 | ExpCreditCardTrxHotelParkingAmount | HOTEL_PARKING_AMOUNT | — | — |
| 86 | ExpCreditCardTrxHotelRestaurantAmount | HOTEL_RESTAURANT_AMOUNT | — | — |
| 87 | ExpCreditCardTrxHotelRoomAmount | HOTEL_ROOM_AMOUNT | — | — |
| 88 | ExpCreditCardTrxHotelRoomRate | HOTEL_ROOM_RATE | — | — |
| 89 | ExpCreditCardTrxHotelRoomServiceAmount | HOTEL_ROOM_SERVICE_AMOUNT | — | — |
| 90 | ExpCreditCardTrxHotelRoomTax | HOTEL_ROOM_TAX | — | — |
| 91 | ExpCreditCardTrxHotelRoomType | HOTEL_ROOM_TYPE | — | — |
| 92 | ExpCreditCardTrxHotelState | HOTEL_STATE | — | — |
| 93 | ExpCreditCardTrxHotelStayDuration | HOTEL_STAY_DURATION | — | — |
| 94 | ExpCreditCardTrxHotelTelephoneAmount | HOTEL_TELEPHONE_AMOUNT | — | — |
| 95 | ExpCreditCardTrxHotelTipAmount | HOTEL_TIP_AMOUNT | — | — |
| 96 | ExpCreditCardTrxHotelTransportationAmount | HOTEL_TRANSPORTATION_AMOUNT | — | — |
| 97 | ExpCreditCardTrxInterbankCardassocNumber | INTERBANK_CARDASSOC_NUMBER | — | — |
| 98 | ExpCreditCardTrxInternetAccessCharges | INTERNET_ACCESS_CHARGES | — | — |
| 99 | ExpCreditCardTrxLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 100 | ExpCreditCardTrxLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 101 | ExpCreditCardTrxLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 102 | ExpCreditCardTrxLocalTax | LOCAL_TAX | — | — |
| 103 | ExpCreditCardTrxMarketCode | MARKET_CODE | — | — |
| 104 | ExpCreditCardTrxMerchantActivity | MERCHANT_ACTIVITY | — | — |
| 105 | ExpCreditCardTrxMerchantAddress1 | MERCHANT_ADDRESS1 | — | — |
| 106 | ExpCreditCardTrxMerchantAddress2 | MERCHANT_ADDRESS2 | — | — |
| 107 | ExpCreditCardTrxMerchantAddress3 | MERCHANT_ADDRESS3 | — | — |
| 108 | ExpCreditCardTrxMerchantAddress4 | MERCHANT_ADDRESS4 | — | — |
| 109 | ExpCreditCardTrxMerchantCategoryCode | MERCHANT_CATEGORY_CODE | — | — |
| 110 | ExpCreditCardTrxMerchantCity | MERCHANT_CITY | — | — |
| 111 | ExpCreditCardTrxMerchantCountry | MERCHANT_COUNTRY | — | — |
| 112 | ExpCreditCardTrxMerchantName1 | MERCHANT_NAME1 | — | — |
| 113 | ExpCreditCardTrxMerchantName2 | MERCHANT_NAME2 | — | — |
| 114 | ExpCreditCardTrxMerchantPostalCode | MERCHANT_POSTAL_CODE | — | — |
| 115 | ExpCreditCardTrxMerchantProvinceState | MERCHANT_PROVINCE_STATE | — | — |
| 116 | ExpCreditCardTrxMerchantReference | MERCHANT_REFERENCE | — | — |
| 117 | ExpCreditCardTrxMerchantTaxId | MERCHANT_TAX_ID | — | — |
| 118 | ExpCreditCardTrxMiniBarAmount | MINI_BAR_AMOUNT | — | — |
| 119 | ExpCreditCardTrxMisIndustryCode | MIS_INDUSTRY_CODE | — | — |
| 120 | ExpCreditCardTrxNationalTax | NATIONAL_TAX | — | — |
| 121 | ExpCreditCardTrxObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 122 | ExpCreditCardTrxOtherTax | OTHER_TAX | — | — |
| 123 | ExpCreditCardTrxPaymentDueFromCode | PAYMENT_DUE_FROM_CODE | — | — |
| 124 | ExpCreditCardTrxPaymentFlag | PAYMENT_FLAG | — | — |
| 125 | ExpCreditCardTrxPostedAmount | POSTED_AMOUNT | — | — |
| 126 | ExpCreditCardTrxPostedCurrencyCode | POSTED_CURRENCY_CODE | — | — |
| 127 | ExpCreditCardTrxPostedDate | POSTED_DATE | — | — |
| 128 | ExpCreditCardTrxPostedDecimal | POSTED_DECIMAL | — | — |
| 129 | ExpCreditCardTrxRecordType | RECORD_TYPE | — | — |
| 130 | ExpCreditCardTrxReferenceNumber | REFERENCE_NUMBER | — | ✅ |
| 131 | ExpCreditCardTrxReqCntlAcctNumber | REQ_CNTL_ACCT_NUMBER | — | — |
| 132 | ExpCreditCardTrxRequestId | REQUEST_ID | — | — |
| 133 | ExpCreditCardTrxRestaurantBeverageAmount | RESTAURANT_BEVERAGE_AMOUNT | — | — |
| 134 | ExpCreditCardTrxRestaurantFoodAmount | RESTAURANT_FOOD_AMOUNT | — | — |
| 135 | ExpCreditCardTrxRestaurantTipAmount | RESTAURANT_TIP_AMOUNT | — | — |
| 136 | ExpCreditCardTrxReviewedFlag | REVIEWED_FLAG | — | — |
| 137 | ExpCreditCardTrxSicCode | SIC_CODE | — | — |
| 138 | ExpCreditCardTrxTotalTax | TOTAL_TAX | — | — |
| 139 | ExpCreditCardTrxTransactionAmount | TRANSACTION_AMOUNT | — | — |
| 140 | ExpCreditCardTrxTransactionDate | TRANSACTION_DATE | — | — |
| 141 | ExpCreditCardTrxTransactionStatus | TRANSACTION_STATUS | — | — |
| 142 | ExpCreditCardTrxTransactionType | TRANSACTION_TYPE | — | — |
| 143 | ExpCreditCardTrxTransportationCharges | TRANSPORTATION_CHARGES | — | — |
| 144 | ExpCreditCardTrxTrxnAvailableDate | TRXN_AVAILABLE_DATE | — | — |
| 145 | ExpCreditCardTrxTrxnDetailFlag | TRXN_DETAIL_FLAG | — | — |
| 146 | ExpCreditCardTrxValidateCode | VALIDATE_CODE | — | — |

### [[exm_expenses|EXM_EXPENSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpAllocationReason | ALLOCATION_REASON | — | — |
| 2 | ExpAllocationSplitCode | ALLOCATION_SPLIT_CODE | — | — |
| 3 | ExpAssignmentId | ASSIGNMENT_ID | — | — |
| 4 | ExpAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 5 | ExpAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 6 | ExpAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 7 | ExpAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 8 | ExpAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 9 | ExpAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 10 | ExpAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 11 | ExpAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 12 | ExpAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 13 | ExpAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 14 | ExpAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 15 | ExpAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 16 | ExpAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 17 | ExpAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 18 | ExpAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 19 | ExpAuditAdjustmentReason | AUDIT_ADJUSTMENT_REASON | — | — |
| 20 | ExpAuditAdjustmentReasonCode | AUDIT_ADJUSTMENT_REASON_CODE | — | — |
| 21 | ExpAvgMileageRate | AVG_MILEAGE_RATE | — | ✅ |
| 22 | ExpAwtGroupId | AWT_GROUP_ID | — | — |
| 23 | ExpCardId | CARD_ID | — | — |
| 24 | ExpCcPrepaidInvoiceId | CC_PREPAID_INVOICE_ID | — | — |
| 25 | ExpCheckoutDate | CHECKOUT_DATE | — | — |
| 26 | ExpCountryOfSupply | COUNTRY_OF_SUPPLY | — | — |
| 27 | ExpCreatedBy | CREATED_BY | — | ✅ |
| 28 | ExpCreationDate | CREATION_DATE | — | ✅ |
| 29 | ExpCreditCardTrxnId | CREDIT_CARD_TRXN_ID | — | ✅ |
| 30 | ExpDailyDistance | DAILY_DISTANCE | — | ✅ |
| 31 | ExpDepartureLocationId | DEPARTURE_LOCATION_ID | — | — |
| 32 | ExpDescription | DESCRIPTION | — | ✅ |
| 33 | ExpDestinationFrom | DESTINATION_FROM | — | ✅ |
| 34 | ExpDestinationTo | DESTINATION_TO | — | ✅ |
| 35 | ExpDistanceUnitCode | DISTANCE_UNIT_CODE | — | ✅ |
| 36 | ExpEmpDefaultCostCenter | EMP_DEFAULT_COST_CENTER | — | ✅ |
| 37 | ExpEndDate | END_DATE | — | ✅ |
| 38 | ExpExchangeRate | EXCHANGE_RATE | — | ✅ |
| 39 | ExpExpenseCategoryCode | EXPENSE_CATEGORY_CODE | — | ✅ |
| 40 | ExpExpenseReportId | EXPENSE_REPORT_ID | — | ✅ |
| 41 | ExpExpenseSource | EXPENSE_SOURCE | — | ✅ |
| 42 | ExpExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 43 | ExpExpenseTypeCategoryCode | EXPENSE_TYPE_CATEGORY_CODE | — | ✅ |
| 44 | ExpExpenseTypeId | EXPENSE_TYPE_ID | — | ✅ |
| 45 | ExpFlightNumber | FLIGHT_NUMBER | — | ✅ |
| 46 | ExpFuelType | FUEL_TYPE | — | ✅ |
| 47 | ExpFuncCurrencyAmount | FUNC_CURRENCY_AMOUNT | — | ✅ |
| 48 | ExpInactiveEmpProcessId | INACTIVE_EMP_PROCESS_ID | — | — |
| 49 | ExpItemizationParentExpenseId | ITEMIZATION_PARENT_EXPENSE_ID | — | ✅ |
| 50 | ExpJustification | JUSTIFICATION | — | ✅ |
| 51 | ExpJustificationRequiredFlag | JUSTIFICATION_REQUIRED_FLAG | — | — |
| 52 | ExpLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 53 | ExpLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 54 | ExpLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 55 | ExpLicensePlateNumber | LICENSE_PLATE_NUMBER | — | — |
| 56 | ExpLocation | LOCATION | — | ✅ |
| 57 | ExpLocationId | LOCATION_ID | — | ✅ |
| 58 | ExpMerchantDocumentNumber | MERCHANT_DOCUMENT_NUMBER | — | ✅ |
| 59 | ExpMerchantName | MERCHANT_NAME | — | ✅ |
| 60 | ExpMerchantReference | MERCHANT_REFERENCE | — | — |
| 61 | ExpMerchantTaxRegNumber | MERCHANT_TAX_REG_NUMBER | — | — |
| 62 | ExpMerchantTaxpayerId | MERCHANT_TAXPAYER_ID | — | — |
| 63 | ExpMileageRateAdjustedFlag | MILEAGE_RATE_ADJUSTED_FLAG | — | — |
| 64 | ExpNumberOfAttendees | NUMBER_OF_ATTENDEES | — | ✅ |
| 65 | ExpNumberPeople | NUMBER_PEOPLE | — | — |
| 66 | ExpObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 67 | ExpOrgId | ORG_ID | — | ✅ |
| 68 | ExpOrigReceiptAmount | ORIG_RECEIPT_AMOUNT | — | — |
| 69 | ExpOrigReimbursableAmount | ORIG_REIMBURSABLE_AMOUNT | — | ✅ |
| 70 | ExpPassengerAmount | PASSENGER_AMOUNT | — | ✅ |
| 71 | ExpPassengerRateType | PASSENGER_RATE_TYPE | — | — |
| 72 | ExpPersonId | PERSON_ID | — | ✅ |
| 73 | ExpPersonalReceiptAmount | PERSONAL_RECEIPT_AMOUNT | — | ✅ |
| 74 | ExpPolicyShortpayFlag | POLICY_SHORTPAY_FLAG | — | — |
| 75 | ExpPolicyViolatedFlag | POLICY_VIOLATED_FLAG | — | — |
| 76 | ExpPreparerId | PREPARER_ID | — | — |
| 77 | ExpRangeHigh | RANGE_HIGH | — | — |
| 78 | ExpRangeLow | RANGE_LOW | — | — |
| 79 | ExpRatePerPassenger | RATE_PER_PASSENGER | — | — |
| 80 | ExpReceiptAmount | RECEIPT_AMOUNT | — | ✅ |
| 81 | ExpReceiptCurrencyCode | RECEIPT_CURRENCY_CODE | — | ✅ |
| 82 | ExpReceiptMissingFlag | RECEIPT_MISSING_FLAG | — | — |
| 83 | ExpReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 84 | ExpReceiptVerifiedFlag | RECEIPT_VERIFIED_FLAG | — | — |
| 85 | ExpReimbursableAmount | REIMBURSABLE_AMOUNT | — | ✅ |
| 86 | ExpReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 87 | ExpSequenceNum | SEQUENCE_NUM | — | — |
| 88 | ExpStartDate | START_DATE | — | ✅ |
| 89 | ExpTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | ✅ |
| 90 | ExpTicketClassCode | TICKET_CLASS_CODE | — | ✅ |
| 91 | ExpTicketNumber | TICKET_NUMBER | — | ✅ |
| 92 | ExpTravelType | TRAVEL_TYPE | — | ✅ |
| 93 | ExpTripDistance | TRIP_DISTANCE | — | ✅ |
| 94 | ExpUomDays | UOM_DAYS | — | — |
| 95 | ExpVehicleCategoryCode | VEHICLE_CATEGORY_CODE | — | ✅ |
| 96 | ExpVehicleType | VEHICLE_TYPE | — | ✅ |
| 97 | ExpenseId | EXPENSE_ID | 🔑 | ✅ |
| 98 | FullExpExpenseCMC | EXPENSE_CREATION_METHOD_CODE | — | — |

### [[exm_expense_dists|EXM_EXPENSE_DISTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpDistCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 2 | ExpDistCostCenter | COST_CENTER | — | — |
| 3 | ExpDistCreatedBy | CREATED_BY | — | — |
| 4 | ExpDistExpenseDistId | EXPENSE_DIST_ID | — | — |
| 5 | ExpDistExpenseId | EXPENSE_ID | — | — |
| 6 | ExpDistExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 7 | ExpDistLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ExpDistLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ExpDistObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ExpDistOrgId | ORG_ID | — | — |
| 11 | ExpDistPjcBillableFlag | PJC_BILLABLE_FLAG | — | — |
| 12 | ExpDistPjcCapitalizableFlag | PJC_CAPITALIZABLE_FLAG | — | — |
| 13 | ExpDistPjcContextCategory | PJC_CONTEXT_CATEGORY | — | — |
| 14 | ExpDistPjcContractId | PJC_CONTRACT_ID | — | — |
| 15 | ExpDistPjcContractLineId | PJC_CONTRACT_LINE_ID | — | — |
| 16 | ExpDistPjcExpenditureItemDate | PJC_EXPENDITURE_ITEM_DATE | — | — |
| 17 | ExpDistPjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | — |
| 18 | ExpDistPjcFundingAllocationId | PJC_FUNDING_ALLOCATION_ID | — | — |
| 19 | ExpDistPjcOrganizationId | PJC_ORGANIZATION_ID | — | — |
| 20 | ExpDistPjcProjectId | PJC_PROJECT_ID | — | — |
| 21 | ExpDistPjcReservedAttribute1 | PJC_RESERVED_ATTRIBUTE1 | — | — |
| 22 | ExpDistPjcReservedAttribute10 | PJC_RESERVED_ATTRIBUTE10 | — | — |
| 23 | ExpDistPjcReservedAttribute2 | PJC_RESERVED_ATTRIBUTE2 | — | — |
| 24 | ExpDistPjcReservedAttribute3 | PJC_RESERVED_ATTRIBUTE3 | — | — |
| 25 | ExpDistPjcReservedAttribute4 | PJC_RESERVED_ATTRIBUTE4 | — | — |
| 26 | ExpDistPjcReservedAttribute5 | PJC_RESERVED_ATTRIBUTE5 | — | — |
| 27 | ExpDistPjcReservedAttribute6 | PJC_RESERVED_ATTRIBUTE6 | — | — |
| 28 | ExpDistPjcReservedAttribute7 | PJC_RESERVED_ATTRIBUTE7 | — | — |
| 29 | ExpDistPjcReservedAttribute8 | PJC_RESERVED_ATTRIBUTE8 | — | — |
| 30 | ExpDistPjcReservedAttribute9 | PJC_RESERVED_ATTRIBUTE9 | — | — |
| 31 | ExpDistPjcTaskId | PJC_TASK_ID | — | — |
| 32 | ExpDistPjcUserDefAttribute1 | PJC_USER_DEF_ATTRIBUTE1 | — | — |
| 33 | ExpDistPjcUserDefAttribute10 | PJC_USER_DEF_ATTRIBUTE10 | — | — |
| 34 | ExpDistPjcUserDefAttribute2 | PJC_USER_DEF_ATTRIBUTE2 | — | — |
| 35 | ExpDistPjcUserDefAttribute3 | PJC_USER_DEF_ATTRIBUTE3 | — | — |
| 36 | ExpDistPjcUserDefAttribute4 | PJC_USER_DEF_ATTRIBUTE4 | — | — |
| 37 | ExpDistPjcUserDefAttribute5 | PJC_USER_DEF_ATTRIBUTE5 | — | — |
| 38 | ExpDistPjcUserDefAttribute6 | PJC_USER_DEF_ATTRIBUTE6 | — | — |
| 39 | ExpDistPjcUserDefAttribute7 | PJC_USER_DEF_ATTRIBUTE7 | — | — |
| 40 | ExpDistPjcUserDefAttribute8 | PJC_USER_DEF_ATTRIBUTE8 | — | — |
| 41 | ExpDistPjcUserDefAttribute9 | PJC_USER_DEF_ATTRIBUTE9 | — | — |
| 42 | ExpDistPjcWorkTypeId | PJC_WORK_TYPE_ID | — | — |
| 43 | ExpDistPreparerModifiedFlag | PREPARER_MODIFIED_FLAG | — | — |
| 44 | ExpDistReimbursableAmount | REIMBURSABLE_AMOUNT | — | — |
| 45 | ExpDistSegment1 | SEGMENT1 | — | — |
| 46 | ExpDistSegment10 | SEGMENT10 | — | — |
| 47 | ExpDistSegment11 | SEGMENT11 | — | — |
| 48 | ExpDistSegment12 | SEGMENT12 | — | — |
| 49 | ExpDistSegment13 | SEGMENT13 | — | — |
| 50 | ExpDistSegment14 | SEGMENT14 | — | — |
| 51 | ExpDistSegment15 | SEGMENT15 | — | — |
| 52 | ExpDistSegment16 | SEGMENT16 | — | — |
| 53 | ExpDistSegment17 | SEGMENT17 | — | — |
| 54 | ExpDistSegment18 | SEGMENT18 | — | — |
| 55 | ExpDistSegment19 | SEGMENT19 | — | — |
| 56 | ExpDistSegment2 | SEGMENT2 | — | — |
| 57 | ExpDistSegment20 | SEGMENT20 | — | — |
| 58 | ExpDistSegment21 | SEGMENT21 | — | — |
| 59 | ExpDistSegment22 | SEGMENT22 | — | — |
| 60 | ExpDistSegment23 | SEGMENT23 | — | — |
| 61 | ExpDistSegment24 | SEGMENT24 | — | — |
| 62 | ExpDistSegment25 | SEGMENT25 | — | — |
| 63 | ExpDistSegment26 | SEGMENT26 | — | — |
| 64 | ExpDistSegment27 | SEGMENT27 | — | — |
| 65 | ExpDistSegment28 | SEGMENT28 | — | — |
| 66 | ExpDistSegment29 | SEGMENT29 | — | — |
| 67 | ExpDistSegment3 | SEGMENT3 | — | — |
| 68 | ExpDistSegment30 | SEGMENT30 | — | — |
| 69 | ExpDistSegment4 | SEGMENT4 | — | — |
| 70 | ExpDistSegment5 | SEGMENT5 | — | — |
| 71 | ExpDistSegment6 | SEGMENT6 | — | — |
| 72 | ExpDistSegment7 | SEGMENT7 | — | — |
| 73 | ExpDistSegment8 | SEGMENT8 | — | — |
| 74 | ExpDistSegment9 | SEGMENT9 | — | — |
| 75 | ExpDistSequenceNum | SEQUENCE_NUM | — | — |

### [[exm_expense_reports|EXM_EXPENSE_REPORTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | ExpHdrAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 3 | ExpHdrAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 4 | ExpHdrAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 5 | ExpHdrAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 6 | ExpHdrAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 7 | ExpHdrAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 8 | ExpHdrAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 9 | ExpHdrAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 10 | ExpHdrAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 11 | ExpHdrAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 12 | ExpHdrAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 13 | ExpHdrAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 14 | ExpHdrAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 15 | ExpHdrAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 16 | ExpHdrAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 17 | ExpHdrAuditCode | AUDIT_CODE | — | ✅ |
| 18 | ExpHdrAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | ✅ |
| 19 | ExpHdrAwtGroupId | AWT_GROUP_ID | — | — |
| 20 | ExpHdrBothpayFlag | BOTHPAY_FLAG | — | — |
| 21 | ExpHdrCashExpensePaidDate | CASH_EXPENSE_PAID_DATE | — | ✅ |
| 22 | ExpHdrCreatedBy | CREATED_BY | — | ✅ |
| 23 | ExpHdrCreationDate | CREATION_DATE | — | ✅ |
| 24 | ExpHdrCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 25 | ExpHdrExchangeRateType | EXCHANGE_RATE_TYPE | — | ✅ |
| 26 | ExpHdrExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 27 | ExpHdrExpenseReportDate | EXPENSE_REPORT_DATE | — | ✅ |
| 28 | ExpHdrExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 29 | ExpHdrExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 30 | ExpHdrExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 31 | ExpHdrExpenseStatusCode | EXPENSE_STATUS_CODE | — | ✅ |
| 32 | ExpHdrExpenseStatusDate | EXPENSE_STATUS_DATE | — | ✅ |
| 33 | ExpHdrExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 34 | ExpHdrExportRequestId | EXPORT_REQUEST_ID | — | — |
| 35 | ExpHdrFinalApprovalDate | FINAL_APPROVAL_DATE | — | ✅ |
| 36 | ExpHdrHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 37 | ExpHdrImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | ✅ |
| 38 | ExpHdrLastAuditBy | LAST_AUDIT_BY | — | — |
| 39 | ExpHdrLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 40 | ExpHdrLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 41 | ExpHdrLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 42 | ExpHdrObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 43 | ExpHdrOrgId | ORG_ID | — | — |
| 44 | ExpHdrOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 45 | ExpHdrParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | ✅ |
| 46 | ExpHdrPaymentMethodCode | PAYMENT_METHOD_CODE | — | ✅ |
| 47 | ExpHdrPersonId | PERSON_ID | — | — |
| 48 | ExpHdrPreparerId | PREPARER_ID | — | — |
| 49 | ExpHdrPrntAssignmentId | ASSIGNMENT_ID | — | — |
| 50 | ExpHdrPrntAttributeChar1 | ATTRIBUTE_CHAR1 | — | — |
| 51 | ExpHdrPrntAttributeChar10 | ATTRIBUTE_CHAR10 | — | — |
| 52 | ExpHdrPrntAttributeChar11 | ATTRIBUTE_CHAR11 | — | — |
| 53 | ExpHdrPrntAttributeChar12 | ATTRIBUTE_CHAR12 | — | — |
| 54 | ExpHdrPrntAttributeChar13 | ATTRIBUTE_CHAR13 | — | — |
| 55 | ExpHdrPrntAttributeChar14 | ATTRIBUTE_CHAR14 | — | — |
| 56 | ExpHdrPrntAttributeChar15 | ATTRIBUTE_CHAR15 | — | — |
| 57 | ExpHdrPrntAttributeChar2 | ATTRIBUTE_CHAR2 | — | — |
| 58 | ExpHdrPrntAttributeChar3 | ATTRIBUTE_CHAR3 | — | — |
| 59 | ExpHdrPrntAttributeChar4 | ATTRIBUTE_CHAR4 | — | — |
| 60 | ExpHdrPrntAttributeChar5 | ATTRIBUTE_CHAR5 | — | — |
| 61 | ExpHdrPrntAttributeChar6 | ATTRIBUTE_CHAR6 | — | — |
| 62 | ExpHdrPrntAttributeChar7 | ATTRIBUTE_CHAR7 | — | — |
| 63 | ExpHdrPrntAttributeChar8 | ATTRIBUTE_CHAR8 | — | — |
| 64 | ExpHdrPrntAttributeChar9 | ATTRIBUTE_CHAR9 | — | — |
| 65 | ExpHdrPrntAuditCode | AUDIT_CODE | — | — |
| 66 | ExpHdrPrntAuditReturnReasonCode | AUDIT_RETURN_REASON_CODE | — | — |
| 67 | ExpHdrPrntAwtGroupId | AWT_GROUP_ID | — | — |
| 68 | ExpHdrPrntBothpayFlag | BOTHPAY_FLAG | — | — |
| 69 | ExpHdrPrntCreatedBy | CREATED_BY | — | — |
| 70 | ExpHdrPrntCurrentApproverId | CURRENT_APPROVER_ID | — | — |
| 71 | ExpHdrPrntExchangeRateType | EXCHANGE_RATE_TYPE | — | — |
| 72 | ExpHdrPrntExpRepProcessingId | EXP_REP_PROCESSING_ID | — | — |
| 73 | ExpHdrPrntExpenseReportDate | EXPENSE_REPORT_DATE | — | — |
| 74 | ExpHdrPrntExpenseReportId | EXPENSE_REPORT_ID | — | — |
| 75 | ExpHdrPrntExpenseReportNum | EXPENSE_REPORT_NUM | — | ✅ |
| 76 | ExpHdrPrntExpenseReportTotal | EXPENSE_REPORT_TOTAL | — | — |
| 77 | ExpHdrPrntExpenseStatusCode | EXPENSE_STATUS_CODE | — | — |
| 78 | ExpHdrPrntExpenseStatusDate | EXPENSE_STATUS_DATE | — | — |
| 79 | ExpHdrPrntExportRejectCode | EXPORT_REJECT_CODE | — | — |
| 80 | ExpHdrPrntExportRequestId | EXPORT_REQUEST_ID | — | — |
| 81 | ExpHdrPrntHoldingExpenseReportId | HOLDING_EXPENSE_REPORT_ID | — | — |
| 82 | ExpHdrPrntImagedReceiptsStatusCode | IMAGED_RECEIPTS_STATUS_CODE | — | — |
| 83 | ExpHdrPrntLastAuditBy | LAST_AUDIT_BY | — | — |
| 84 | ExpHdrPrntLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 85 | ExpHdrPrntLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 86 | ExpHdrPrntLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 87 | ExpHdrPrntObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 88 | ExpHdrPrntOrgId | ORG_ID | — | — |
| 89 | ExpHdrPrntOverrideApproverId | OVERRIDE_APPROVER_ID | — | — |
| 90 | ExpHdrPrntParentExpenseReportId | PARENT_EXPENSE_REPORT_ID | — | — |
| 91 | ExpHdrPrntPersonId | PERSON_ID | — | — |
| 92 | ExpHdrPrntPreparerId | PREPARER_ID | — | — |
| 93 | ExpHdrPrntPurpose | PURPOSE | — | — |
| 94 | ExpHdrPrntReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | — |
| 95 | ExpHdrPrntReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | — |
| 96 | ExpHdrPrntReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | — |
| 97 | ExpHdrPrntReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | — |
| 98 | ExpHdrPrntReportSubmitDate | REPORT_SUBMIT_DATE | — | — |
| 99 | ExpHdrPrntShortpayTypeCode | SHORTPAY_TYPE_CODE | — | — |
| 100 | ExpHdrPrntTripId | TRIP_ID | — | — |
| 101 | ExpHdrPrntUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 102 | ExpHdrPurpose | PURPOSE | — | ✅ |
| 103 | ExpHdrReceiptsFilingNumber | RECEIPTS_FILING_NUMBER | — | ✅ |
| 104 | ExpHdrReceiptsReceivedDate | RECEIPTS_RECEIVED_DATE | — | ✅ |
| 105 | ExpHdrReceiptsStatusCode | RECEIPTS_STATUS_CODE | — | ✅ |
| 106 | ExpHdrReimbursementCurrencyCode | REIMBURSEMENT_CURRENCY_CODE | — | ✅ |
| 107 | ExpHdrReportSubmitDate | REPORT_SUBMIT_DATE | — | ✅ |
| 108 | ExpHdrShortpayTypeCode | SHORTPAY_TYPE_CODE | — | ✅ |
| 109 | ExpHdrTripId | TRIP_ID | — | — |
| 110 | ExpHdrUnappliedAdvancesJust | UNAPPLIED_ADVANCES_JUST | — | — |
| 111 | FullExpHdrPrntReportCMC | REPORT_CREATION_METHOD_CODE | — | — |
| 112 | FullExpHdrReportCMC | REPORT_CREATION_METHOD_CODE | — | — |

### [[exm_expense_templates|EXM_EXPENSE_TEMPLATES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTemplatePEOAllowRcptMissingFlag | ALLOW_RCPT_MISSING_FLAG | — | — |
| 2 | ExpenseTemplatePEOCashReceiptReqFlag | CASH_RECEIPT_REQ_FLAG | — | — |
| 3 | ExpenseTemplatePEOCashReceiptReqLimit | CASH_RECEIPT_REQ_LIMIT | — | — |
| 4 | ExpenseTemplatePEOCcReceiptReqFlag | CC_RECEIPT_REQ_FLAG | — | — |
| 5 | ExpenseTemplatePEOCcReceiptReqLimit | CC_RECEIPT_REQ_LIMIT | — | — |
| 6 | ExpenseTemplatePEOCreatedBy | CREATED_BY | — | — |
| 7 | ExpenseTemplatePEOCreationDate | CREATION_DATE | — | — |
| 8 | ExpenseTemplatePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTemplatePEODfltCcExpTypeId | DFLT_CC_EXP_TYPE_ID | — | — |
| 10 | ExpenseTemplatePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 11 | ExpenseTemplatePEOEnableCcMappingFlag | ENABLE_CC_MAPPING_FLAG | — | — |
| 12 | ExpenseTemplatePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTemplatePEOInactiveDate | INACTIVE_DATE | — | — |
| 14 | ExpenseTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | ExpenseTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | ExpenseTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 17 | ExpenseTemplatePEOName | NAME | — | ✅ |
| 18 | ExpenseTemplatePEONegativeRcptReqFlag | NEGATIVE_RCPT_REQ_FLAG | — | — |
| 19 | ExpenseTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | ExpenseTemplatePEOOrgId | ORG_ID | — | — |
| 21 | ExpenseTemplatePEOStartDate | START_DATE | — | — |

### [[exm_expense_types|EXM_EXPENSE_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpenseTypePEOCategoryCode | CATEGORY_CODE | — | — |
| 2 | ExpenseTypePEOCcReceiptRequiredFlag | CC_RECEIPT_REQUIRED_FLAG | — | — |
| 3 | ExpenseTypePEOCcReceiptThreshold | CC_RECEIPT_THRESHOLD | — | — |
| 4 | ExpenseTypePEOCodeCombinationId | CODE_COMBINATION_ID | — | — |
| 5 | ExpenseTypePEOCreatedBy | CREATED_BY | — | — |
| 6 | ExpenseTypePEOCreationDate | CREATION_DATE | — | — |
| 7 | ExpenseTypePEODefaultProjExpendType | DEFAULT_PROJ_EXPEND_TYPE | — | — |
| 8 | ExpenseTypePEODescription | DESCRIPTION | — | — |
| 9 | ExpenseTypePEODispRcptViolationFlag | DISP_RCPT_VIOLATION_FLAG | — | — |
| 10 | ExpenseTypePEOEnableProjectsFlag | ENABLE_PROJECTS_FLAG | — | — |
| 11 | ExpenseTypePEOEndDate | END_DATE | — | — |
| 12 | ExpenseTypePEOExpenseTemplateId | EXPENSE_TEMPLATE_ID | — | — |
| 13 | ExpenseTypePEOExpenseTypeId | EXPENSE_TYPE_ID | — | — |
| 14 | ExpenseTypePEOItemizationBehaviourCode | ITEMIZATION_BEHAVIOUR_CODE | — | — |
| 15 | ExpenseTypePEOItemizationOnlyFlag | ITEMIZATION_ONLY_FLAG | — | — |
| 16 | ExpenseTypePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | ExpenseTypePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | ExpenseTypePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | ExpenseTypePEOName | NAME | — | ✅ |
| 20 | ExpenseTypePEONegativeRcptReqCode | NEGATIVE_RCPT_REQ_CODE | — | — |
| 21 | ExpenseTypePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 22 | ExpenseTypePEOOrgId1 | ORG_ID | — | — |
| 23 | ExpenseTypePEORcptRequiredProjFlag | RCPT_REQUIRED_PROJ_FLAG | — | — |
| 24 | ExpenseTypePEOReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | — |
| 25 | ExpenseTypePEOReceiptThreshold | RECEIPT_THRESHOLD | — | — |
| 26 | ExpenseTypePEOStartDate | START_DATE | — | — |
| 27 | ExpenseTypePEOTaxClassificationCode | TAX_CLASSIFICATION_CODE | — | — |

### [[gl_daily_conversion_types|GL_DAILY_CONVERSION_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlDailyConversionTypesConversionType | CONVERSION_TYPE | — | — |
| 2 | GlDailyConversionTypesCreatedBy | CREATED_BY | — | — |
| 3 | GlDailyConversionTypesCreationDate | CREATION_DATE | — | — |
| 4 | GlDailyConversionTypesDescription | DESCRIPTION | — | — |
| 5 | GlDailyConversionTypesEnableCrossRateFlag | ENABLE_CROSS_RATE_FLAG | — | — |
| 6 | GlDailyConversionTypesEnforceInverseRateFlag | ENFORCE_INVERSE_RATE_FLAG | — | — |
| 7 | GlDailyConversionTypesFemEnabledFlag | FEM_ENABLED_FLAG | — | — |
| 8 | GlDailyConversionTypesFemRateTypeCode | FEM_RATE_TYPE_CODE | — | — |
| 9 | GlDailyConversionTypesFemScenario | FEM_SCENARIO | — | — |
| 10 | GlDailyConversionTypesFemTimeframe | FEM_TIMEFRAME | — | — |
| 11 | GlDailyConversionTypesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | GlDailyConversionTypesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | GlDailyConversionTypesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | GlDailyConversionTypesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 15 | GlDailyConversionTypesPivotCurrencyCode | PIVOT_CURRENCY_CODE | — | — |
| 16 | GlDailyConversionTypesSecurityFlag | SECURITY_FLAG | — | — |
| 17 | GlDailyConversionTypesUserConversionType | USER_CONVERSION_TYPE | — | — |
| 18 | GlDailyConversionTypesUserOverrideCrossRateFlag | USER_OVERRIDE_CROSS_RATE_FLAG | — | — |

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

### [[per_all_assignments_m|PER_ALL_ASSIGNMENTS_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentAssignmentId | ASSIGNMENT_ID | — | — |
| 2 | AssignmentEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | AssignmentEffectiveLatestChange | EFFECTIVE_LATEST_CHANGE | — | — |
| 4 | AssignmentEffectiveSequence | EFFECTIVE_SEQUENCE | — | — |
| 5 | AssignmentExpenseCheckAddress | EXPENSE_CHECK_ADDRESS | — | ✅ |
| 6 | AssignmentLegalEntityId | LEGAL_ENTITY_ID | — | — |
| 7 | AssignmentPersonId | PERSON_ID | — | — |
| 8 | ExpAssignmentEffectiveStartDate | EFFECTIVE_START_DATE | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 2 | ExpHdrPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | ExpHdrPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | ExpHdrPersonUpdatedByPersonId | PERSON_ID | — | — |
| 5 | ExpHdrPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | ExpHdrPreparerNameDisplayName | DISPLAY_NAME | — | ✅ |
| 7 | ExpHdrPreparerNameEffEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | ExpHdrPreparerNameEffStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | ExpHdrPreparerNamePersonNameId | PERSON_NAME_ID | — | — |
| 10 | ExpPersonUpdatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 11 | ExpPersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 12 | ExpPersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 13 | ExpPersonUpdatedByPersonId | PERSON_ID | — | — |
| 14 | ExpPersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |
| 15 | ExpPersoncreatedByPersonId | PERSON_ID | — | — |
| 16 | ExpenHdrPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 17 | ExpenHdrPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 18 | ExpenHdrPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 19 | ExpenHdrPersonCreatedByPersonId | PERSON_ID | — | — |
| 20 | ExpenHdrPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 21 | ExpenPersonCreatedByDisplayName | DISPLAY_NAME | — | ✅ |
| 22 | ExpenPersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 23 | ExpenPersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 24 | ExpenPersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 25 | PersonNamePEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 26 | PersonNamePEOCreatedBy1 | CREATED_BY | — | — |
| 27 | PersonNamePEOCreationDate1 | CREATION_DATE | — | — |
| 28 | PersonNamePEODisplayName | DISPLAY_NAME | — | ✅ |
| 29 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 30 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 31 | PersonNamePEOFirstName | FIRST_NAME | — | — |
| 32 | PersonNamePEOFullName | FULL_NAME | — | — |
| 33 | PersonNamePEOHonors | HONORS | — | — |
| 34 | PersonNamePEOKnownAs | KNOWN_AS | — | — |
| 35 | PersonNamePEOLastName | LAST_NAME | — | — |
| 36 | PersonNamePEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 37 | PersonNamePEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 38 | PersonNamePEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 39 | PersonNamePEOLegislationCode | LEGISLATION_CODE | — | — |
| 40 | PersonNamePEOListName | LIST_NAME | — | — |
| 41 | PersonNamePEOMiddleNames | MIDDLE_NAMES | — | — |
| 42 | PersonNamePEOMilitaryRank | MILITARY_RANK | — | — |
| 43 | PersonNamePEONamInformation1 | NAM_INFORMATION1 | — | — |
| 44 | PersonNamePEONamInformation10 | NAM_INFORMATION10 | — | — |
| 45 | PersonNamePEONamInformation11 | NAM_INFORMATION11 | — | — |
| 46 | PersonNamePEONamInformation12 | NAM_INFORMATION12 | — | — |
| 47 | PersonNamePEONamInformation13 | NAM_INFORMATION13 | — | — |
| 48 | PersonNamePEONamInformation14 | NAM_INFORMATION14 | — | — |
| 49 | PersonNamePEONamInformation15 | NAM_INFORMATION15 | — | — |
| 50 | PersonNamePEONamInformation16 | NAM_INFORMATION16 | — | — |
| 51 | PersonNamePEONamInformation17 | NAM_INFORMATION17 | — | — |
| 52 | PersonNamePEONamInformation18 | NAM_INFORMATION18 | — | — |
| 53 | PersonNamePEONamInformation19 | NAM_INFORMATION19 | — | — |
| 54 | PersonNamePEONamInformation2 | NAM_INFORMATION2 | — | — |
| 55 | PersonNamePEONamInformation20 | NAM_INFORMATION20 | — | — |
| 56 | PersonNamePEONamInformation21 | NAM_INFORMATION21 | — | — |
| 57 | PersonNamePEONamInformation22 | NAM_INFORMATION22 | — | — |
| 58 | PersonNamePEONamInformation23 | NAM_INFORMATION23 | — | — |
| 59 | PersonNamePEONamInformation24 | NAM_INFORMATION24 | — | — |
| 60 | PersonNamePEONamInformation25 | NAM_INFORMATION25 | — | — |
| 61 | PersonNamePEONamInformation26 | NAM_INFORMATION26 | — | — |
| 62 | PersonNamePEONamInformation27 | NAM_INFORMATION27 | — | — |
| 63 | PersonNamePEONamInformation28 | NAM_INFORMATION28 | — | — |
| 64 | PersonNamePEONamInformation29 | NAM_INFORMATION29 | — | — |
| 65 | PersonNamePEONamInformation3 | NAM_INFORMATION3 | — | — |
| 66 | PersonNamePEONamInformation30 | NAM_INFORMATION30 | — | — |
| 67 | PersonNamePEONamInformation4 | NAM_INFORMATION4 | — | — |
| 68 | PersonNamePEONamInformation5 | NAM_INFORMATION5 | — | — |
| 69 | PersonNamePEONamInformation6 | NAM_INFORMATION6 | — | — |
| 70 | PersonNamePEONamInformation7 | NAM_INFORMATION7 | — | — |
| 71 | PersonNamePEONamInformation8 | NAM_INFORMATION8 | — | — |
| 72 | PersonNamePEONamInformation9 | NAM_INFORMATION9 | — | — |
| 73 | PersonNamePEONamInformationCategory | NAM_INFORMATION_CATEGORY | — | — |
| 74 | PersonNamePEONameType | NAME_TYPE | — | — |
| 75 | PersonNamePEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 76 | PersonNamePEOOrderName | ORDER_NAME | — | — |
| 77 | PersonNamePEOPersonId1 | PERSON_ID | — | — |
| 78 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |
| 79 | PersonNamePEOPreNameAdjunct | PRE_NAME_ADJUNCT | — | — |
| 80 | PersonNamePEOPreviousLastName | PREVIOUS_LAST_NAME | — | — |
| 81 | PersonNamePEOSuffix | SUFFIX | — | — |
| 82 | PersonNamePEOTitle | TITLE | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ExpHdrUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | ExpHdrUserUpdatedByPersonId | PERSON_ID | — | — |
| 3 | ExpHdrUserUpdatedByUserGuid | USER_GUID | — | — |
| 4 | ExpHdrUserUpdatedByUserId | USER_ID | — | — |
| 5 | ExpHdrUserUpdatedByUsername | USERNAME | — | — |
| 6 | ExpUserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ExpUserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | ExpUserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | ExpUserUpdatedByUserId | USER_ID | — | — |
| 10 | ExpUserUpdatedByUsername | USERNAME | — | — |
| 11 | ExpenCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ExpenCreatedByPersonId | PERSON_ID | — | — |
| 13 | ExpenCreatedByUserGuid | USER_GUID | — | — |
| 14 | ExpenCreatedByUserId | USER_ID | — | — |
| 15 | ExpenCreatedByUsername | USERNAME | — | — |
| 16 | ExpenHdrCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | ExpenHdrCreatedByPersonId | PERSON_ID | — | — |
| 18 | ExpenHdrCreatedByUserGuid | USER_GUID | — | — |
| 19 | ExpenHdrCreatedByUserId | USER_ID | — | — |
| 20 | ExpenHdrCreatedByUsername | USERNAME | — | — |

### [[zx_wht_tax_classification_v|ZX_WHT_TAX_CLASSIFICATION_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | WithholdingTaxGroupExpCreatedBy | CREATED_BY | — | — |
| 2 | WithholdingTaxGroupExpCreationDate | CREATION_DATE | — | — |
| 3 | WithholdingTaxGroupExpDescription | DESCRIPTION | — | — |
| 4 | WithholdingTaxGroupExpGroupId | GROUP_ID | — | — |
| 5 | WithholdingTaxGroupExpInactiveDate | INACTIVE_DATE | — | — |
| 6 | WithholdingTaxGroupExpLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | WithholdingTaxGroupExpLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | WithholdingTaxGroupExpLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | WithholdingTaxGroupExpName | NAME | — | — |
| 10 | WithholdingTaxGroupExpObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | WithholdingTaxGroupExpRptCreatedBy | CREATED_BY | — | — |
| 12 | WithholdingTaxGroupExpRptCreationDate | CREATION_DATE | — | — |
| 13 | WithholdingTaxGroupExpRptDescription | DESCRIPTION | — | — |
| 14 | WithholdingTaxGroupExpRptGroupId | GROUP_ID | — | — |
| 15 | WithholdingTaxGroupExpRptInactiveDate | INACTIVE_DATE | — | — |
| 16 | WithholdingTaxGroupExpRptLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 17 | WithholdingTaxGroupExpRptLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 18 | WithholdingTaxGroupExpRptLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 19 | WithholdingTaxGroupExpRptName | NAME | — | — |
| 20 | WithholdingTaxGroupExpRptObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
