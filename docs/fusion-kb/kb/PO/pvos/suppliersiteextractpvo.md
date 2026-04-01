---
id: DOC-PO-PVO-SupplierSiteExtractPVO
doc_type: system-doc
title: "SupplierSiteExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierSiteExtractPVO
  - suppliersiteextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierSiteExtractPVO

## 📌 Visão Geral

Extrai os sites (estabelecimentos) dos fornecedores para carga BICC, com endereço, dados fiscais, condições de pagamento e status. Alimenta análises de locais de fornecimento.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PozBiccExtractAM.SupplierSiteExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 209 | 1 | 1 | 107 | 51% |

---

## 🔗 Tabelas Relacionadas

- [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]] — 209 atributos (1 PKs, 107 BICC)

---

## ⚙️ Atributos

### [[poz_supplier_sites_all_m|POZ_SUPPLIER_SITES_ALL_M]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgingOnsetPoint | AGING_ONSET_POINT | — | ✅ |
| 2 | AgingPeriodDays | AGING_PERIOD_DAYS | — | ✅ |
| 3 | AllowSubstituteReceiptsFlag | ALLOW_SUBSTITUTE_RECEIPTS_FLAG | — | ✅ |
| 4 | AllowUnorderedReceiptsFlag | ALLOW_UNORDERED_RECEIPTS_FLAG | — | ✅ |
| 5 | AlwaysTakeDiscFlag | ALWAYS_TAKE_DISC_FLAG | — | ✅ |
| 6 | AmountIncludesTaxFlag | AMOUNT_INCLUDES_TAX_FLAG | — | ✅ |
| 7 | ApTaxRoundingRule | AP_TAX_ROUNDING_RULE | — | ✅ |
| 8 | AreaCode | AREA_CODE | — | ✅ |
| 9 | AttentionArFlag | ATTENTION_AR_FLAG | — | ✅ |
| 10 | Attribute1 | ATTRIBUTE1 | — | — |
| 11 | Attribute10 | ATTRIBUTE10 | — | — |
| 12 | Attribute11 | ATTRIBUTE11 | — | — |
| 13 | Attribute12 | ATTRIBUTE12 | — | — |
| 14 | Attribute13 | ATTRIBUTE13 | — | — |
| 15 | Attribute14 | ATTRIBUTE14 | — | — |
| 16 | Attribute15 | ATTRIBUTE15 | — | — |
| 17 | Attribute16 | ATTRIBUTE16 | — | — |
| 18 | Attribute17 | ATTRIBUTE17 | — | — |
| 19 | Attribute18 | ATTRIBUTE18 | — | — |
| 20 | Attribute19 | ATTRIBUTE19 | — | — |
| 21 | Attribute2 | ATTRIBUTE2 | — | — |
| 22 | Attribute20 | ATTRIBUTE20 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute4 | ATTRIBUTE4 | — | — |
| 25 | Attribute5 | ATTRIBUTE5 | — | — |
| 26 | Attribute6 | ATTRIBUTE6 | — | — |
| 27 | Attribute7 | ATTRIBUTE7 | — | — |
| 28 | Attribute8 | ATTRIBUTE8 | — | — |
| 29 | Attribute9 | ATTRIBUTE9 | — | — |
| 30 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 31 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 32 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 33 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 34 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 35 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 36 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 37 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 38 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 39 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 40 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 41 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 42 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 43 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 44 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 45 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 46 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 47 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 48 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 49 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 50 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 51 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 52 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 53 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 54 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 55 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 56 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 57 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 58 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 59 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 60 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 61 | AutoCalculateInterestFlag | AUTO_CALCULATE_INTEREST_FLAG | — | ✅ |
| 62 | AutoTaxCalcFlag | AUTO_TAX_CALC_FLAG | — | ✅ |
| 63 | AutoTaxCalcOverride | AUTO_TAX_CALC_OVERRIDE | — | ✅ |
| 64 | B2bCommMethodCode | B2B_COMM_METHOD_CODE | — | ✅ |
| 65 | B2bSiteCode | B2B_SITE_CODE | — | ✅ |
| 66 | BankChargeBearer | BANK_CHARGE_BEARER | — | ✅ |
| 67 | BankChargeDeductionType | BANK_CHARGE_DEDUCTION_TYPE | — | ✅ |
| 68 | BuyerManagedTransportFlag | BUYER_MANAGED_TRANSPORT_FLAG | — | ✅ |
| 69 | CarrierId | CARRIER_ID | — | ✅ |
| 70 | ConsumptionAdviceFrequency | CONSUMPTION_ADVICE_FREQUENCY | — | ✅ |
| 71 | ConsumptionAdviceSummary | CONSUMPTION_ADVICE_SUMMARY | — | ✅ |
| 72 | CountryOfOriginCode | COUNTRY_OF_ORIGIN_CODE | — | ✅ |
| 73 | CreateDebitMemoFlag | CREATE_DEBIT_MEMO_FLAG | — | ✅ |
| 74 | CreatedBy | CREATED_BY | — | ✅ |
| 75 | CreationDate | CREATION_DATE | — | ✅ |
| 76 | CustomerNum | CUSTOMER_NUM | — | ✅ |
| 77 | DaysEarlyReceiptAllowed | DAYS_EARLY_RECEIPT_ALLOWED | — | ✅ |
| 78 | DaysLateReceiptAllowed | DAYS_LATE_RECEIPT_ALLOWED | — | ✅ |
| 79 | DefaultPaySiteId | DEFAULT_PAY_SITE_ID | — | ✅ |
| 80 | EceTpLocationCode | ECE_TP_LOCATION_CODE | — | ✅ |
| 81 | EmailAddress | EMAIL_ADDRESS | — | ✅ |
| 82 | EnforceShipToLocationCode | ENFORCE_SHIP_TO_LOCATION_CODE | — | ✅ |
| 83 | ExcludeFreightFromDiscount | EXCLUDE_FREIGHT_FROM_DISCOUNT | — | ✅ |
| 84 | ExcludeTaxFromDiscount | EXCLUDE_TAX_FROM_DISCOUNT | — | ✅ |
| 85 | Fax | FAX | — | ✅ |
| 86 | FaxAreaCode | FAX_AREA_CODE | — | ✅ |
| 87 | FaxCountryCode | FAX_COUNTRY_CODE | — | ✅ |
| 88 | FobLookupCode | FOB_LOOKUP_CODE | — | ✅ |
| 89 | FreightTermsLookupCode | FREIGHT_TERMS_LOOKUP_CODE | — | ✅ |
| 90 | GaplessInvNumFlag | GAPLESS_INV_NUM_FLAG | — | ✅ |
| 91 | GlobalAttribute1 | GLOBAL_ATTRIBUTE1 | — | — |
| 92 | GlobalAttribute10 | GLOBAL_ATTRIBUTE10 | — | — |
| 93 | GlobalAttribute11 | GLOBAL_ATTRIBUTE11 | — | — |
| 94 | GlobalAttribute12 | GLOBAL_ATTRIBUTE12 | — | — |
| 95 | GlobalAttribute13 | GLOBAL_ATTRIBUTE13 | — | — |
| 96 | GlobalAttribute14 | GLOBAL_ATTRIBUTE14 | — | — |
| 97 | GlobalAttribute15 | GLOBAL_ATTRIBUTE15 | — | — |
| 98 | GlobalAttribute16 | GLOBAL_ATTRIBUTE16 | — | — |
| 99 | GlobalAttribute17 | GLOBAL_ATTRIBUTE17 | — | — |
| 100 | GlobalAttribute18 | GLOBAL_ATTRIBUTE18 | — | — |
| 101 | GlobalAttribute19 | GLOBAL_ATTRIBUTE19 | — | — |
| 102 | GlobalAttribute2 | GLOBAL_ATTRIBUTE2 | — | — |
| 103 | GlobalAttribute20 | GLOBAL_ATTRIBUTE20 | — | — |
| 104 | GlobalAttribute3 | GLOBAL_ATTRIBUTE3 | — | — |
| 105 | GlobalAttribute4 | GLOBAL_ATTRIBUTE4 | — | — |
| 106 | GlobalAttribute5 | GLOBAL_ATTRIBUTE5 | — | — |
| 107 | GlobalAttribute6 | GLOBAL_ATTRIBUTE6 | — | — |
| 108 | GlobalAttribute7 | GLOBAL_ATTRIBUTE7 | — | — |
| 109 | GlobalAttribute8 | GLOBAL_ATTRIBUTE8 | — | — |
| 110 | GlobalAttribute9 | GLOBAL_ATTRIBUTE9 | — | — |
| 111 | GlobalAttributeCategory | GLOBAL_ATTRIBUTE_CATEGORY | — | — |
| 112 | GlobalAttributeDate1 | GLOBAL_ATTRIBUTE_DATE1 | — | — |
| 113 | GlobalAttributeDate10 | GLOBAL_ATTRIBUTE_DATE10 | — | — |
| 114 | GlobalAttributeDate2 | GLOBAL_ATTRIBUTE_DATE2 | — | — |
| 115 | GlobalAttributeDate3 | GLOBAL_ATTRIBUTE_DATE3 | — | — |
| 116 | GlobalAttributeDate4 | GLOBAL_ATTRIBUTE_DATE4 | — | — |
| 117 | GlobalAttributeDate5 | GLOBAL_ATTRIBUTE_DATE5 | — | — |
| 118 | GlobalAttributeDate6 | GLOBAL_ATTRIBUTE_DATE6 | — | — |
| 119 | GlobalAttributeDate7 | GLOBAL_ATTRIBUTE_DATE7 | — | — |
| 120 | GlobalAttributeDate8 | GLOBAL_ATTRIBUTE_DATE8 | — | — |
| 121 | GlobalAttributeDate9 | GLOBAL_ATTRIBUTE_DATE9 | — | — |
| 122 | GlobalAttributeNumber1 | GLOBAL_ATTRIBUTE_NUMBER1 | — | — |
| 123 | GlobalAttributeNumber10 | GLOBAL_ATTRIBUTE_NUMBER10 | — | — |
| 124 | GlobalAttributeNumber2 | GLOBAL_ATTRIBUTE_NUMBER2 | — | — |
| 125 | GlobalAttributeNumber3 | GLOBAL_ATTRIBUTE_NUMBER3 | — | — |
| 126 | GlobalAttributeNumber4 | GLOBAL_ATTRIBUTE_NUMBER4 | — | — |
| 127 | GlobalAttributeNumber5 | GLOBAL_ATTRIBUTE_NUMBER5 | — | — |
| 128 | GlobalAttributeNumber6 | GLOBAL_ATTRIBUTE_NUMBER6 | — | — |
| 129 | GlobalAttributeNumber7 | GLOBAL_ATTRIBUTE_NUMBER7 | — | — |
| 130 | GlobalAttributeNumber8 | GLOBAL_ATTRIBUTE_NUMBER8 | — | — |
| 131 | GlobalAttributeNumber9 | GLOBAL_ATTRIBUTE_NUMBER9 | — | — |
| 132 | GlobalAttributeTimestamp1 | GLOBAL_ATTRIBUTE_TIMESTAMP1 | — | — |
| 133 | GlobalAttributeTimestamp10 | GLOBAL_ATTRIBUTE_TIMESTAMP10 | — | — |
| 134 | GlobalAttributeTimestamp2 | GLOBAL_ATTRIBUTE_TIMESTAMP2 | — | — |
| 135 | GlobalAttributeTimestamp3 | GLOBAL_ATTRIBUTE_TIMESTAMP3 | — | — |
| 136 | GlobalAttributeTimestamp4 | GLOBAL_ATTRIBUTE_TIMESTAMP4 | — | — |
| 137 | GlobalAttributeTimestamp5 | GLOBAL_ATTRIBUTE_TIMESTAMP5 | — | — |
| 138 | GlobalAttributeTimestamp6 | GLOBAL_ATTRIBUTE_TIMESTAMP6 | — | — |
| 139 | GlobalAttributeTimestamp7 | GLOBAL_ATTRIBUTE_TIMESTAMP7 | — | — |
| 140 | GlobalAttributeTimestamp8 | GLOBAL_ATTRIBUTE_TIMESTAMP8 | — | — |
| 141 | GlobalAttributeTimestamp9 | GLOBAL_ATTRIBUTE_TIMESTAMP9 | — | — |
| 142 | HoldAllPaymentsFlag | HOLD_ALL_PAYMENTS_FLAG | — | ✅ |
| 143 | HoldBy | HOLD_BY | — | ✅ |
| 144 | HoldDate | HOLD_DATE | — | ✅ |
| 145 | HoldFlag | HOLD_FLAG | — | ✅ |
| 146 | HoldFuturePaymentsFlag | HOLD_FUTURE_PAYMENTS_FLAG | — | ✅ |
| 147 | HoldReason | HOLD_REASON | — | ✅ |
| 148 | HoldUnmatchedInvoicesFlag | HOLD_UNMATCHED_INVOICES_FLAG | — | ✅ |
| 149 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 150 | InspectionRequiredFlag | INSPECTION_REQUIRED_FLAG | — | ✅ |
| 151 | InvoiceAmountLimit | INVOICE_AMOUNT_LIMIT | — | ✅ |
| 152 | InvoiceChannel | INVOICE_CHANNEL | — | ✅ |
| 153 | InvoiceCurrencyCode | INVOICE_CURRENCY_CODE | — | ✅ |
| 154 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 155 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 156 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 157 | LocationId | LOCATION_ID | — | ✅ |
| 158 | MatchOption | MATCH_OPTION | — | ✅ |
| 159 | ModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 160 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 161 | OffsetTaxFlag | OFFSET_TAX_FLAG | — | ✅ |
| 162 | OffsetVatCode | OFFSET_VAT_CODE | — | ✅ |
| 163 | PartySiteId | PARTY_SITE_ID | — | ✅ |
| 164 | PayDateBasisLookupCode | PAY_DATE_BASIS_LOOKUP_CODE | — | ✅ |
| 165 | PayGroupLookupCode | PAY_GROUP_LOOKUP_CODE | — | ✅ |
| 166 | PayOnCode | PAY_ON_CODE | — | ✅ |
| 167 | PayOnReceiptSummaryCode | PAY_ON_RECEIPT_SUMMARY_CODE | — | ✅ |
| 168 | PayOnUseFlag | PAY_ON_USE_FLAG | — | ✅ |
| 169 | PaySiteFlag | PAY_SITE_FLAG | — | ✅ |
| 170 | PaymentCurrencyCode | PAYMENT_CURRENCY_CODE | — | ✅ |
| 171 | PaymentHoldDate | PAYMENT_HOLD_DATE | — | ✅ |
| 172 | PaymentPriority | PAYMENT_PRIORITY | — | ✅ |
| 173 | PcardSiteFlag | PCARD_SITE_FLAG | — | ✅ |
| 174 | Phone | PHONE | — | ✅ |
| 175 | PhoneCountryCode | PHONE_COUNTRY_CODE | — | ✅ |
| 176 | PhoneExtension | PHONE_EXTENSION | — | ✅ |
| 177 | PoAckReqdCode | PO_ACK_REQD_CODE | — | ✅ |
| 178 | PoAckReqdDays | PO_ACK_REQD_DAYS | — | ✅ |
| 179 | PrcBuId | PRC_BU_ID | — | ✅ |
| 180 | PrimaryPaySiteFlag | PRIMARY_PAY_SITE_FLAG | — | ✅ |
| 181 | PurchasingHoldReason | PURCHASING_HOLD_REASON | — | ✅ |
| 182 | PurchasingSiteFlag | PURCHASING_SITE_FLAG | — | ✅ |
| 183 | QtyRcvExceptionCode | QTY_RCV_EXCEPTION_CODE | — | ✅ |
| 184 | QtyRcvTolerance | QTY_RCV_TOLERANCE | — | ✅ |
| 185 | ReceiptDaysExceptionCode | RECEIPT_DAYS_EXCEPTION_CODE | — | ✅ |
| 186 | ReceiptRequiredFlag | RECEIPT_REQUIRED_FLAG | — | ✅ |
| 187 | ReceivingRoutingId | RECEIVING_ROUTING_ID | — | ✅ |
| 188 | RetainageRate | RETAINAGE_RATE | — | ✅ |
| 189 | RfqOnlySiteFlag | RFQ_ONLY_SITE_FLAG | — | ✅ |
| 190 | SellingCompanyIdentifier | SELLING_COMPANY_IDENTIFIER | — | ✅ |
| 191 | ServiceLevel | SERVICE_LEVEL | — | ✅ |
| 192 | ServicesToleranceId | SERVICES_TOLERANCE_ID | — | ✅ |
| 193 | ShipViaLookupCode | SHIP_VIA_LOOKUP_CODE | — | ✅ |
| 194 | ShippingControl | SHIPPING_CONTROL | — | ✅ |
| 195 | ShippingNetworkLocation | SHIPPING_NETWORK_LOCATION | — | ✅ |
| 196 | SupplierNotifMethod | SUPPLIER_NOTIF_METHOD | — | ✅ |
| 197 | TaxCountryCode | TAX_COUNTRY_CODE | — | ✅ |
| 198 | TaxReportingSiteFlag | TAX_REPORTING_SITE_FLAG | — | ✅ |
| 199 | Telex | TELEX | — | ✅ |
| 200 | TermsDateBasis | TERMS_DATE_BASIS | — | ✅ |
| 201 | TermsId | TERMS_ID | — | ✅ |
| 202 | ToleranceId | TOLERANCE_ID | — | ✅ |
| 203 | TpHeaderId | TP_HEADER_ID | — | ✅ |
| 204 | VatCode | VAT_CODE | — | ✅ |
| 205 | VatRegistrationNum | VAT_REGISTRATION_NUM | — | ✅ |
| 206 | VendorId | VENDOR_ID | — | ✅ |
| 207 | VendorSiteCode | VENDOR_SITE_CODE | — | ✅ |
| 208 | VendorSiteCodeAlt | VENDOR_SITE_CODE_ALT | — | ✅ |
| 209 | VendorSiteId | VENDOR_SITE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
