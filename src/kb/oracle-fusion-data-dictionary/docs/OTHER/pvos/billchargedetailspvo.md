---
id: DOC-OTHER-PVO-BillChargeDetailsPVO
doc_type: system-doc
title: "BillChargeDetailsPVO — PVO Cross-Module"
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
  - BillChargeDetailsPVO
  - billchargedetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillChargeDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Bill Charge Details. Acessa as tabelas: BEN_BILL_CHARGES, BEN_BILL_CHARGE_DETAILS, BEN_BILL_ENRT_RSLT (+3).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BillChargeDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 284 | 6 | 4 | 72 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[ben_bill_charges|BEN_BILL_CHARGES]] — 65 atributos (24 BICC)
- [[ben_bill_charge_details|BEN_BILL_CHARGE_DETAILS]] — 80 atributos (1 PKs, 27 BICC)
- [[ben_bill_enrt_rslt|BEN_BILL_ENRT_RSLT]] — 69 atributos (1 PKs, 2 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 6 atributos (1 BICC)
- [[ben_per_bill_info_f|BEN_PER_BILL_INFO_F]] — 61 atributos (16 BICC)
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (2 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[ben_bill_charges|BEN_BILL_CHARGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BchAttribute1 | BCH_ATTRIBUTE1 | — | — |
| 2 | BchAttribute10 | BCH_ATTRIBUTE10 | — | — |
| 3 | BchAttribute2 | BCH_ATTRIBUTE2 | — | — |
| 4 | BchAttribute3 | BCH_ATTRIBUTE3 | — | — |
| 5 | BchAttribute4 | BCH_ATTRIBUTE4 | — | — |
| 6 | BchAttribute5 | BCH_ATTRIBUTE5 | — | — |
| 7 | BchAttribute6 | BCH_ATTRIBUTE6 | — | — |
| 8 | BchAttribute7 | BCH_ATTRIBUTE7 | — | — |
| 9 | BchAttribute8 | BCH_ATTRIBUTE8 | — | — |
| 10 | BchAttribute9 | BCH_ATTRIBUTE9 | — | — |
| 11 | BchAttributeCategory | BCH_ATTRIBUTE_CATEGORY | — | — |
| 12 | BchAttributeDate1 | BCH_ATTRIBUTE_DATE1 | — | — |
| 13 | BchAttributeDate2 | BCH_ATTRIBUTE_DATE2 | — | — |
| 14 | BchAttributeDate3 | BCH_ATTRIBUTE_DATE3 | — | — |
| 15 | BchAttributeDate4 | BCH_ATTRIBUTE_DATE4 | — | — |
| 16 | BchAttributeDate5 | BCH_ATTRIBUTE_DATE5 | — | — |
| 17 | BchAttributeNumber1 | BCH_ATTRIBUTE_NUMBER1 | — | — |
| 18 | BchAttributeNumber2 | BCH_ATTRIBUTE_NUMBER2 | — | — |
| 19 | BchAttributeNumber3 | BCH_ATTRIBUTE_NUMBER3 | — | — |
| 20 | BchAttributeNumber4 | BCH_ATTRIBUTE_NUMBER4 | — | — |
| 21 | BchAttributeNumber5 | BCH_ATTRIBUTE_NUMBER5 | — | ✅ |
| 22 | BillCalId | BILL_CAL_ID | — | — |
| 23 | BillChargeId1 | BILL_CHARGE_ID | — | ✅ |
| 24 | BillGenerated | BILL_GENERATED | — | ✅ |
| 25 | BillGeneratedDate | BILL_GENERATED_DATE | — | ✅ |
| 26 | BillNum | BILL_NUM | — | ✅ |
| 27 | BillPeriod | BILL_PERIOD | — | ✅ |
| 28 | BillReason | BILL_REASON | — | ✅ |
| 29 | BillSource | BILL_SOURCE | — | ✅ |
| 30 | BillYear | BILL_YEAR | — | ✅ |
| 31 | BillingDate | BILLING_DATE | — | ✅ |
| 32 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 33 | Comments | COMMENTS | — | ✅ |
| 34 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 35 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 36 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 37 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 38 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 39 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 40 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 41 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 42 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 43 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 44 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 45 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 46 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 47 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 48 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 49 | CreatedBy1 | CREATED_BY | — | ✅ |
| 50 | CreationDate1 | CREATION_DATE | — | ✅ |
| 51 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 52 | CurrentBillAmt | CURRENT_BILL_AMT | — | ✅ |
| 53 | HoldBillFlag | HOLD_BILL_FLAG | — | ✅ |
| 54 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 55 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 57 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 58 | OtherAmtDue | OTHER_AMT_DUE | — | ✅ |
| 59 | PastAmtDue | PAST_AMT_DUE | — | ✅ |
| 60 | PerAcctNum | PER_ACCT_NUM | — | — |
| 61 | PerBillInfoId | PER_BILL_INFO_ID | — | — |
| 62 | PersonId | PERSON_ID | — | — |
| 63 | Status1 | STATUS | — | ✅ |
| 64 | TotalBillAmt | TOTAL_BILL_AMT | — | ✅ |
| 65 | TotalTaxAmt | TOTAL_TAX_AMT | — | ✅ |

### [[ben_bill_charge_details|BEN_BILL_CHARGE_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddFlatAmt | ADD_FLAT_AMT | — | ✅ |
| 2 | AdjAmt | ADJ_AMT | — | ✅ |
| 3 | AdjDate | ADJ_DATE | — | ✅ |
| 4 | AdjPercent | ADJ_PERCENT | — | ✅ |
| 5 | AllocSeqNum | ALLOC_SEQ_NUM | — | ✅ |
| 6 | AmtDue | AMT_DUE | — | ✅ |
| 7 | AmtPaid | AMT_PAID | — | ✅ |
| 8 | AnnRtVal | ANN_RT_VAL | — | ✅ |
| 9 | BcdAttribute1 | BCD_ATTRIBUTE1 | — | — |
| 10 | BcdAttribute10 | BCD_ATTRIBUTE10 | — | — |
| 11 | BcdAttribute2 | BCD_ATTRIBUTE2 | — | — |
| 12 | BcdAttribute3 | BCD_ATTRIBUTE3 | — | — |
| 13 | BcdAttribute4 | BCD_ATTRIBUTE4 | — | — |
| 14 | BcdAttribute5 | BCD_ATTRIBUTE5 | — | — |
| 15 | BcdAttribute6 | BCD_ATTRIBUTE6 | — | — |
| 16 | BcdAttribute7 | BCD_ATTRIBUTE7 | — | — |
| 17 | BcdAttribute8 | BCD_ATTRIBUTE8 | — | — |
| 18 | BcdAttribute9 | BCD_ATTRIBUTE9 | — | — |
| 19 | BcdAttributeCategory | BCD_ATTRIBUTE_CATEGORY | — | — |
| 20 | BcdAttributeDate1 | BCD_ATTRIBUTE_DATE1 | — | — |
| 21 | BcdAttributeDate2 | BCD_ATTRIBUTE_DATE2 | — | — |
| 22 | BcdAttributeDate3 | BCD_ATTRIBUTE_DATE3 | — | — |
| 23 | BcdAttributeDate4 | BCD_ATTRIBUTE_DATE4 | — | — |
| 24 | BcdAttributeDate5 | BCD_ATTRIBUTE_DATE5 | — | — |
| 25 | BcdAttributeNumber1 | BCD_ATTRIBUTE_NUMBER1 | — | — |
| 26 | BcdAttributeNumber2 | BCD_ATTRIBUTE_NUMBER2 | — | — |
| 27 | BcdAttributeNumber3 | BCD_ATTRIBUTE_NUMBER3 | — | — |
| 28 | BcdAttributeNumber4 | BCD_ATTRIBUTE_NUMBER4 | — | — |
| 29 | BcdAttributeNumber5 | BCD_ATTRIBUTE_NUMBER5 | — | — |
| 30 | BenefitRelationId | BENEFIT_RELATION_ID | — | — |
| 31 | BillAmt | BILL_AMT | — | ✅ |
| 32 | BillChargeDtlId | BILL_CHARGE_DTL_ID | 🔑 | ✅ |
| 33 | BillChargeId | BILL_CHARGE_ID | — | ✅ |
| 34 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 35 | CmcdRtFreq | CMCD_RT_FREQ | — | ✅ |
| 36 | CmcdRtVal | CMCD_RT_VAL | — | ✅ |
| 37 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 38 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 39 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 40 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 41 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 42 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 43 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 44 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 45 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 46 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 47 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 48 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 49 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 50 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 51 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 52 | CreatedBy | CREATED_BY | — | — |
| 53 | CreationDate | CREATION_DATE | — | — |
| 54 | CurrencyCd | CURRENCY_CD | — | — |
| 55 | DailyProtnFlag | DAILY_PROTN_FLAG | — | ✅ |
| 56 | DfndRtFreq | DFND_RT_FREQ | — | ✅ |
| 57 | DfndRtVal | DFND_RT_VAL | — | ✅ |
| 58 | HoldFlag | HOLD_FLAG | — | ✅ |
| 59 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 60 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 61 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 62 | LegalEntityId | LEGAL_ENTITY_ID | — | — |
| 63 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 64 | OiplId | OIPL_ID | — | — |
| 65 | OptId | OPT_ID | — | — |
| 66 | OriginalBillAmt | ORIGINAL_BILL_AMT | — | ✅ |
| 67 | OverrideDate | OVERRIDE_DATE | — | ✅ |
| 68 | OverrideReason | OVERRIDE_REASON | — | ✅ |
| 69 | PgmId | PGM_ID | — | — |
| 70 | PlId | PL_ID | — | — |
| 71 | PlTypId | PL_TYP_ID | — | — |
| 72 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | — |
| 73 | PrttRtValId | PRTT_RT_VAL_ID | — | — |
| 74 | PtipId | PTIP_ID | — | — |
| 75 | RateEndDt | RATE_END_DT | — | ✅ |
| 76 | RateStartDt | RATE_START_DT | — | ✅ |
| 77 | Status | STATUS | — | ✅ |
| 78 | TaxAmt | TAX_AMT | — | ✅ |
| 79 | TaxPercent | TAX_PERCENT | — | ✅ |
| 80 | TaxType | TAX_TYPE | — | ✅ |

### [[ben_bill_enrt_rslt|BEN_BILL_ENRT_RSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitRelationId2 | BENEFIT_RELATION_ID | — | — |
| 2 | BerAttribute1 | BER_ATTRIBUTE1 | — | — |
| 3 | BerAttribute10 | BER_ATTRIBUTE10 | — | — |
| 4 | BerAttribute2 | BER_ATTRIBUTE2 | — | — |
| 5 | BerAttribute3 | BER_ATTRIBUTE3 | — | — |
| 6 | BerAttribute4 | BER_ATTRIBUTE4 | — | — |
| 7 | BerAttribute5 | BER_ATTRIBUTE5 | — | — |
| 8 | BerAttribute6 | BER_ATTRIBUTE6 | — | — |
| 9 | BerAttribute7 | BER_ATTRIBUTE7 | — | — |
| 10 | BerAttribute8 | BER_ATTRIBUTE8 | — | — |
| 11 | BerAttribute9 | BER_ATTRIBUTE9 | — | — |
| 12 | BerAttributeCategory | BER_ATTRIBUTE_CATEGORY | — | — |
| 13 | BerAttributeDate1 | BER_ATTRIBUTE_DATE1 | — | — |
| 14 | BerAttributeDate2 | BER_ATTRIBUTE_DATE2 | — | — |
| 15 | BerAttributeDate3 | BER_ATTRIBUTE_DATE3 | — | — |
| 16 | BerAttributeDate4 | BER_ATTRIBUTE_DATE4 | — | — |
| 17 | BerAttributeDate5 | BER_ATTRIBUTE_DATE5 | — | — |
| 18 | BerAttributeNumber1 | BER_ATTRIBUTE_NUMBER1 | — | — |
| 19 | BerAttributeNumber2 | BER_ATTRIBUTE_NUMBER2 | — | — |
| 20 | BerAttributeNumber3 | BER_ATTRIBUTE_NUMBER3 | — | — |
| 21 | BerAttributeNumber4 | BER_ATTRIBUTE_NUMBER4 | — | — |
| 22 | BerAttributeNumber5 | BER_ATTRIBUTE_NUMBER5 | — | — |
| 23 | BillEndDate | BILL_END_DATE | — | — |
| 24 | BillEnrtRsltId | BILL_ENRT_RSLT_ID | 🔑 | ✅ |
| 25 | BillStartDate | BILL_START_DATE | — | — |
| 26 | BnftAmt | BNFT_AMT | — | — |
| 27 | BusinessGroupId4 | BUSINESS_GROUP_ID | — | — |
| 28 | ConfigChar13 | CONFIG_CHAR_1 | — | — |
| 29 | ConfigChar23 | CONFIG_CHAR_2 | — | — |
| 30 | ConfigChar33 | CONFIG_CHAR_3 | — | — |
| 31 | ConfigChar43 | CONFIG_CHAR_4 | — | — |
| 32 | ConfigChar53 | CONFIG_CHAR_5 | — | — |
| 33 | ConfigDate13 | CONFIG_DATE_1 | — | — |
| 34 | ConfigDate23 | CONFIG_DATE_2 | — | — |
| 35 | ConfigDate33 | CONFIG_DATE_3 | — | — |
| 36 | ConfigDate43 | CONFIG_DATE_4 | — | — |
| 37 | ConfigDate53 | CONFIG_DATE_5 | — | — |
| 38 | ConfigNum13 | CONFIG_NUM_1 | — | — |
| 39 | ConfigNum23 | CONFIG_NUM_2 | — | — |
| 40 | ConfigNum33 | CONFIG_NUM_3 | — | — |
| 41 | ConfigNum43 | CONFIG_NUM_4 | — | — |
| 42 | ConfigNum53 | CONFIG_NUM_5 | — | — |
| 43 | CreatedBy4 | CREATED_BY | — | — |
| 44 | CreationDate4 | CREATION_DATE | — | — |
| 45 | ElectionDate | ELECTION_DATE | — | — |
| 46 | EnrtCvgStrtDt | ENRT_CVG_STRT_DT | — | — |
| 47 | EnrtCvgThruDt | ENRT_CVG_THRU_DT | — | — |
| 48 | LastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 49 | LastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 50 | LastUpdatedBy4 | LAST_UPDATED_BY | — | — |
| 51 | LegalEntityId2 | LEGAL_ENTITY_ID | — | — |
| 52 | LerId | LER_ID | — | — |
| 53 | LerTypCd | LER_TYP_CD | — | — |
| 54 | ObjectVersionNumber4 | OBJECT_VERSION_NUMBER | — | — |
| 55 | OiplId1 | OIPL_ID | — | — |
| 56 | OptId1 | OPT_ID | — | — |
| 57 | OrgnlEnrtDt | ORGNL_ENRT_DT | — | — |
| 58 | OrgnlPrttEnrtRsltId | ORGNL_PRTT_ENRT_RSLT_ID | — | — |
| 59 | PerInLerId | PER_IN_LER_ID | — | — |
| 60 | PersonId3 | PERSON_ID | — | — |
| 61 | PgmId1 | PGM_ID | — | — |
| 62 | PlId1 | PL_ID | — | — |
| 63 | PlTypId1 | PL_TYP_ID | — | — |
| 64 | ProrateDays | PRORATE_DAYS | — | — |
| 65 | ProratePercent | PRORATE_PERCENT | — | — |
| 66 | ProrateType | PRORATE_TYPE | — | — |
| 67 | PtipId1 | PTIP_ID | — | — |
| 68 | SrcCd | SRC_CD | — | — |
| 69 | StopBillFlag1 | STOP_BILL_FLAG | — | — |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |
| 5 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 6 | PersonId4 | PERSON_ID | — | — |

### [[ben_per_bill_info_f|BEN_PER_BILL_INFO_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 2 | AddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 3 | AddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 4 | AddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 5 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 6 | City | CITY | — | ✅ |
| 7 | Comments1 | COMMENTS | — | ✅ |
| 8 | ConfigChar12 | CONFIG_CHAR_1 | — | — |
| 9 | ConfigChar22 | CONFIG_CHAR_2 | — | — |
| 10 | ConfigChar32 | CONFIG_CHAR_3 | — | — |
| 11 | ConfigChar42 | CONFIG_CHAR_4 | — | — |
| 12 | ConfigChar52 | CONFIG_CHAR_5 | — | — |
| 13 | ConfigDate12 | CONFIG_DATE_1 | — | — |
| 14 | ConfigDate22 | CONFIG_DATE_2 | — | — |
| 15 | ConfigDate32 | CONFIG_DATE_3 | — | — |
| 16 | ConfigDate42 | CONFIG_DATE_4 | — | — |
| 17 | ConfigDate52 | CONFIG_DATE_5 | — | — |
| 18 | ConfigNum12 | CONFIG_NUM_1 | — | — |
| 19 | ConfigNum22 | CONFIG_NUM_2 | — | — |
| 20 | ConfigNum32 | CONFIG_NUM_3 | — | — |
| 21 | ConfigNum42 | CONFIG_NUM_4 | — | — |
| 22 | ConfigNum52 | CONFIG_NUM_5 | — | — |
| 23 | Country | COUNTRY | — | ✅ |
| 24 | CreatedBy2 | CREATED_BY | — | — |
| 25 | CreationDate2 | CREATION_DATE | — | — |
| 26 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 27 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 28 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 30 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 31 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 32 | PbiAttribute1 | PBI_ATTRIBUTE1 | — | — |
| 33 | PbiAttribute10 | PBI_ATTRIBUTE10 | — | — |
| 34 | PbiAttribute2 | PBI_ATTRIBUTE2 | — | — |
| 35 | PbiAttribute3 | PBI_ATTRIBUTE3 | — | — |
| 36 | PbiAttribute4 | PBI_ATTRIBUTE4 | — | — |
| 37 | PbiAttribute5 | PBI_ATTRIBUTE5 | — | — |
| 38 | PbiAttribute6 | PBI_ATTRIBUTE6 | — | — |
| 39 | PbiAttribute7 | PBI_ATTRIBUTE7 | — | — |
| 40 | PbiAttribute8 | PBI_ATTRIBUTE8 | — | — |
| 41 | PbiAttribute9 | PBI_ATTRIBUTE9 | — | — |
| 42 | PbiAttributeCategory | PBI_ATTRIBUTE_CATEGORY | — | — |
| 43 | PbiAttributeDate1 | PBI_ATTRIBUTE_DATE1 | — | — |
| 44 | PbiAttributeDate2 | PBI_ATTRIBUTE_DATE2 | — | — |
| 45 | PbiAttributeDate3 | PBI_ATTRIBUTE_DATE3 | — | — |
| 46 | PbiAttributeDate4 | PBI_ATTRIBUTE_DATE4 | — | — |
| 47 | PbiAttributeDate5 | PBI_ATTRIBUTE_DATE5 | — | — |
| 48 | PbiAttributeNumber1 | PBI_ATTRIBUTE_NUMBER1 | — | — |
| 49 | PbiAttributeNumber2 | PBI_ATTRIBUTE_NUMBER2 | — | — |
| 50 | PbiAttributeNumber3 | PBI_ATTRIBUTE_NUMBER3 | — | — |
| 51 | PbiAttributeNumber4 | PBI_ATTRIBUTE_NUMBER4 | — | — |
| 52 | PbiAttributeNumber5 | PBI_ATTRIBUTE_NUMBER5 | — | — |
| 53 | PerAcctNum1 | PER_ACCT_NUM | — | ✅ |
| 54 | PerBillInfoId1 | PER_BILL_INFO_ID | — | — |
| 55 | PersonId1 | PERSON_ID | — | — |
| 56 | PrefCommMode | PREF_COMM_MODE | — | — |
| 57 | PrmryEmailId | PRMRY_EMAIL_ID | — | ✅ |
| 58 | PrmryMailAddressId | PRMRY_MAIL_ADDRESS_ID | — | ✅ |
| 59 | State | STATE | — | ✅ |
| 60 | StopBillFlag | STOP_BILL_FLAG | — | ✅ |
| 61 | ZipCode | ZIP_CODE | — | ✅ |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate1 | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate1 | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | PersonId2 | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
