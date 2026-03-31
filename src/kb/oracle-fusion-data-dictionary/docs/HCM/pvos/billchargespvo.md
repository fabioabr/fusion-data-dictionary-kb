---
id: DOC-HCM-PVO-BillChargesPVO
doc_type: system-doc
title: "BillChargesPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - BillChargesPVO
  - billchargespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillChargesPVO

## 📌 Visão Geral

Extrai cobrancas de beneficios com grupos e informacoes de billing por pessoa. Base para faturamento e controle de custos de planos de beneficios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BillChargesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 135 | 4 | 3 | 42 | 31% |

---

## 🔗 Tabelas Relacionadas

- [[ben_bill_charges|BEN_BILL_CHARGES]] — 65 atributos (1 PKs, 24 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 6 atributos (1 BICC)
- [[ben_per_bill_info_f|BEN_PER_BILL_INFO_F]] — 61 atributos (15 BICC)
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
| 21 | BchAttributeNumber5 | BCH_ATTRIBUTE_NUMBER5 | — | — |
| 22 | BillCalId | BILL_CAL_ID | — | — |
| 23 | BillChargeId | BILL_CHARGE_ID | 🔑 | ✅ |
| 24 | BillGenerated | BILL_GENERATED | — | ✅ |
| 25 | BillGeneratedDate | BILL_GENERATED_DATE | — | ✅ |
| 26 | BillNum | BILL_NUM | — | ✅ |
| 27 | BillPeriod | BILL_PERIOD | — | ✅ |
| 28 | BillReason | BILL_REASON | — | ✅ |
| 29 | BillSource | BILL_SOURCE | — | ✅ |
| 30 | BillYear | BILL_YEAR | — | ✅ |
| 31 | BillingDate | BILLING_DATE | — | ✅ |
| 32 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 33 | Comments | COMMENTS | — | ✅ |
| 34 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 35 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 36 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 37 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 38 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 39 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 40 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 41 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 42 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 43 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 44 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 45 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 46 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 47 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 48 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 49 | CreatedBy | CREATED_BY | — | ✅ |
| 50 | CreationDate | CREATION_DATE | — | ✅ |
| 51 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 52 | CurrentBillAmt | CURRENT_BILL_AMT | — | ✅ |
| 53 | HoldBillFlag | HOLD_BILL_FLAG | — | ✅ |
| 54 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 55 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 56 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 57 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 58 | OtherAmtDue | OTHER_AMT_DUE | — | ✅ |
| 59 | PastAmtDue | PAST_AMT_DUE | — | ✅ |
| 60 | PerAcctNum | PER_ACCT_NUM | — | ✅ |
| 61 | PerBillInfoId | PER_BILL_INFO_ID | — | — |
| 62 | PersonId | PERSON_ID | — | — |
| 63 | Status | STATUS | — | ✅ |
| 64 | TotalBillAmt | TOTAL_BILL_AMT | — | ✅ |
| 65 | TotalTaxAmt | TOTAL_TAX_AMT | — | ✅ |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate2 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate2 | EFFECTIVE_START_DATE | — | ✅ |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |
| 5 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 6 | PersonId3 | PERSON_ID | — | — |

### [[ben_per_bill_info_f|BEN_PER_BILL_INFO_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AddressLine1 | ADDRESS_LINE1 | — | ✅ |
| 2 | AddressLine2 | ADDRESS_LINE2 | — | ✅ |
| 3 | AddressLine3 | ADDRESS_LINE3 | — | ✅ |
| 4 | AddressLine4 | ADDRESS_LINE4 | — | ✅ |
| 5 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 6 | City | CITY | — | ✅ |
| 7 | Comments1 | COMMENTS | — | ✅ |
| 8 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 9 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 10 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 11 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 12 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 13 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 14 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 15 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 16 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 17 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 18 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 19 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 20 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 21 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 22 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 23 | Country | COUNTRY | — | ✅ |
| 24 | CreatedBy1 | CREATED_BY | — | — |
| 25 | CreationDate1 | CREATION_DATE | — | — |
| 26 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 27 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 28 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 30 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 31 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
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
| 53 | PerAcctNum1 | PER_ACCT_NUM | — | — |
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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
