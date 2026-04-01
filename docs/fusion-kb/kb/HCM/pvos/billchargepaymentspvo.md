---
id: DOC-HCM-PVO-BillChargePaymentsPVO
doc_type: system-doc
title: "BillChargePaymentsPVO — PVO Human Capital Management"
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
  - BillChargePaymentsPVO
  - billchargepaymentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillChargePaymentsPVO

## 📌 Visão Geral

Relaciona pagamentos a cobrancas de beneficios com ajustes, creditos e valores devidos. Suporta conciliacao financeira de billing de beneficios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BillChargePaymentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 177 | 5 | 1 | 35 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[ben_bill_charge_payments|BEN_BILL_CHARGE_PAYMENTS]] — 55 atributos (1 PKs, 9 BICC)
- [[ben_bill_payments|BEN_BILL_PAYMENTS]] — 61 atributos (19 BICC)
- [[ben_bill_per_credit|BEN_BILL_PER_CREDIT]] — 52 atributos (7 BICC)
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 6 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_bill_charge_payments|BEN_BILL_CHARGE_PAYMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AmtDue | AMT_DUE | — | ✅ |
| 2 | AmtPaid | AMT_PAID | — | ✅ |
| 3 | BcpAttribute1 | BCP_ATTRIBUTE1 | — | — |
| 4 | BcpAttribute10 | BCP_ATTRIBUTE10 | — | — |
| 5 | BcpAttribute2 | BCP_ATTRIBUTE2 | — | — |
| 6 | BcpAttribute3 | BCP_ATTRIBUTE3 | — | — |
| 7 | BcpAttribute4 | BCP_ATTRIBUTE4 | — | — |
| 8 | BcpAttribute5 | BCP_ATTRIBUTE5 | — | — |
| 9 | BcpAttribute6 | BCP_ATTRIBUTE6 | — | — |
| 10 | BcpAttribute7 | BCP_ATTRIBUTE7 | — | — |
| 11 | BcpAttribute8 | BCP_ATTRIBUTE8 | — | — |
| 12 | BcpAttribute9 | BCP_ATTRIBUTE9 | — | — |
| 13 | BcpAttributeCategory | BCP_ATTRIBUTE_CATEGORY | — | — |
| 14 | BcpAttributeDate1 | BCP_ATTRIBUTE_DATE1 | — | — |
| 15 | BcpAttributeDate2 | BCP_ATTRIBUTE_DATE2 | — | — |
| 16 | BcpAttributeDate3 | BCP_ATTRIBUTE_DATE3 | — | — |
| 17 | BcpAttributeDate4 | BCP_ATTRIBUTE_DATE4 | — | — |
| 18 | BcpAttributeDate5 | BCP_ATTRIBUTE_DATE5 | — | — |
| 19 | BcpAttributeNumber1 | BCP_ATTRIBUTE_NUMBER1 | — | — |
| 20 | BcpAttributeNumber2 | BCP_ATTRIBUTE_NUMBER2 | — | — |
| 21 | BcpAttributeNumber3 | BCP_ATTRIBUTE_NUMBER3 | — | — |
| 22 | BcpAttributeNumber4 | BCP_ATTRIBUTE_NUMBER4 | — | — |
| 23 | BcpAttributeNumber5 | BCP_ATTRIBUTE_NUMBER5 | — | — |
| 24 | BillCalId | BILL_CAL_ID | — | — |
| 25 | BillChargeDtlId | BILL_CHARGE_DTL_ID | — | ✅ |
| 26 | BillChargeId | BILL_CHARGE_ID | — | — |
| 27 | BillChargePaymentId | BILL_CHARGE_PAYMENT_ID | 🔑 | ✅ |
| 28 | BillNum | BILL_NUM | — | ✅ |
| 29 | BillPaymentId | BILL_PAYMENT_ID | — | ✅ |
| 30 | BillPeriod | BILL_PERIOD | — | ✅ |
| 31 | BillYear | BILL_YEAR | — | ✅ |
| 32 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 33 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 34 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 35 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 36 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 37 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 38 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 39 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 40 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 41 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 42 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 43 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 44 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 45 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 46 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 47 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 48 | CreatedBy | CREATED_BY | — | — |
| 49 | CreationDate | CREATION_DATE | — | — |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 54 | PerCreditId | PER_CREDIT_ID | — | — |
| 55 | PersonId | PERSON_ID | — | — |

### [[ben_bill_payments|BEN_BILL_PAYMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjAmt | ADJ_AMT | — | ✅ |
| 2 | AdjDate | ADJ_DATE | — | ✅ |
| 3 | AmtPaid1 | AMT_PAID | — | — |
| 4 | BillNum1 | BILL_NUM | — | — |
| 5 | BillPaymentId1 | BILL_PAYMENT_ID | — | — |
| 6 | BpyAttribute1 | BPY_ATTRIBUTE1 | — | — |
| 7 | BpyAttribute10 | BPY_ATTRIBUTE10 | — | — |
| 8 | BpyAttribute2 | BPY_ATTRIBUTE2 | — | — |
| 9 | BpyAttribute3 | BPY_ATTRIBUTE3 | — | — |
| 10 | BpyAttribute4 | BPY_ATTRIBUTE4 | — | — |
| 11 | BpyAttribute5 | BPY_ATTRIBUTE5 | — | — |
| 12 | BpyAttribute6 | BPY_ATTRIBUTE6 | — | — |
| 13 | BpyAttribute7 | BPY_ATTRIBUTE7 | — | — |
| 14 | BpyAttribute8 | BPY_ATTRIBUTE8 | — | — |
| 15 | BpyAttribute9 | BPY_ATTRIBUTE9 | — | — |
| 16 | BpyAttributeCategory | BPY_ATTRIBUTE_CATEGORY | — | — |
| 17 | BpyAttributeDate1 | BPY_ATTRIBUTE_DATE1 | — | — |
| 18 | BpyAttributeDate2 | BPY_ATTRIBUTE_DATE2 | — | — |
| 19 | BpyAttributeDate3 | BPY_ATTRIBUTE_DATE3 | — | — |
| 20 | BpyAttributeDate4 | BPY_ATTRIBUTE_DATE4 | — | — |
| 21 | BpyAttributeDate5 | BPY_ATTRIBUTE_DATE5 | — | — |
| 22 | BpyAttributeNumber1 | BPY_ATTRIBUTE_NUMBER1 | — | — |
| 23 | BpyAttributeNumber2 | BPY_ATTRIBUTE_NUMBER2 | — | — |
| 24 | BpyAttributeNumber3 | BPY_ATTRIBUTE_NUMBER3 | — | — |
| 25 | BpyAttributeNumber4 | BPY_ATTRIBUTE_NUMBER4 | — | — |
| 26 | BpyAttributeNumber5 | BPY_ATTRIBUTE_NUMBER5 | — | — |
| 27 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 28 | Comments | COMMENTS | — | ✅ |
| 29 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 30 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 31 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 32 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 33 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 34 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 35 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 36 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 37 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 38 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 39 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 40 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 41 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 42 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 43 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 44 | CreatedBy1 | CREATED_BY | — | ✅ |
| 45 | CreationDate1 | CREATION_DATE | — | ✅ |
| 46 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 47 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 48 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | ✅ |
| 49 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 50 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 51 | PaySeq | PAY_SEQ | — | ✅ |
| 52 | PayeeOrgDetails | PAYEE_ORG_DETAILS | — | ✅ |
| 53 | PayeeOrgName | PAYEE_ORG_NAME | — | ✅ |
| 54 | PayeeOrgNum | PAYEE_ORG_NUM | — | ✅ |
| 55 | PaymentDate | PAYMENT_DATE | — | ✅ |
| 56 | PaymentDocNum | PAYMENT_DOC_NUM | — | ✅ |
| 57 | PaymentEntryDate | PAYMENT_ENTRY_DATE | — | ✅ |
| 58 | PaymentMode | PAYMENT_MODE | — | ✅ |
| 59 | PaymentType | PAYMENT_TYPE | — | ✅ |
| 60 | PerAcctNum | PER_ACCT_NUM | — | ✅ |
| 61 | PersonId1 | PERSON_ID | — | — |

### [[ben_bill_per_credit|BEN_BILL_PER_CREDIT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillPaymentId2 | BILL_PAYMENT_ID | — | — |
| 2 | BillPerCreditId | BILL_PER_CREDIT_ID | — | — |
| 3 | BpcAttribute1 | BPC_ATTRIBUTE1 | — | — |
| 4 | BpcAttribute10 | BPC_ATTRIBUTE10 | — | — |
| 5 | BpcAttribute2 | BPC_ATTRIBUTE2 | — | — |
| 6 | BpcAttribute3 | BPC_ATTRIBUTE3 | — | — |
| 7 | BpcAttribute4 | BPC_ATTRIBUTE4 | — | — |
| 8 | BpcAttribute5 | BPC_ATTRIBUTE5 | — | — |
| 9 | BpcAttribute6 | BPC_ATTRIBUTE6 | — | — |
| 10 | BpcAttribute7 | BPC_ATTRIBUTE7 | — | — |
| 11 | BpcAttribute8 | BPC_ATTRIBUTE8 | — | — |
| 12 | BpcAttribute9 | BPC_ATTRIBUTE9 | — | — |
| 13 | BpcAttributeCategory | BPC_ATTRIBUTE_CATEGORY | — | — |
| 14 | BpcAttributeDate1 | BPC_ATTRIBUTE_DATE1 | — | — |
| 15 | BpcAttributeDate2 | BPC_ATTRIBUTE_DATE2 | — | — |
| 16 | BpcAttributeDate3 | BPC_ATTRIBUTE_DATE3 | — | — |
| 17 | BpcAttributeDate4 | BPC_ATTRIBUTE_DATE4 | — | — |
| 18 | BpcAttributeDate5 | BPC_ATTRIBUTE_DATE5 | — | — |
| 19 | BpcAttributeMumber1 | BPC_ATTRIBUTE_MUMBER1 | — | — |
| 20 | BpcAttributeMumber2 | BPC_ATTRIBUTE_MUMBER2 | — | — |
| 21 | BpcAttributeMumber3 | BPC_ATTRIBUTE_MUMBER3 | — | — |
| 22 | BpcAttributeMumber4 | BPC_ATTRIBUTE_MUMBER4 | — | — |
| 23 | BpcAttributeMumber5 | BPC_ATTRIBUTE_MUMBER5 | — | — |
| 24 | BusinessGroupId2 | BUSINESS_GROUP_ID | — | — |
| 25 | Comments1 | COMMENTS | — | ✅ |
| 26 | ConfigChar12 | CONFIG_CHAR_1 | — | — |
| 27 | ConfigChar22 | CONFIG_CHAR_2 | — | — |
| 28 | ConfigChar32 | CONFIG_CHAR_3 | — | — |
| 29 | ConfigChar42 | CONFIG_CHAR_4 | — | — |
| 30 | ConfigChar52 | CONFIG_CHAR_5 | — | — |
| 31 | ConfigDate12 | CONFIG_DATE_1 | — | — |
| 32 | ConfigDate22 | CONFIG_DATE_2 | — | — |
| 33 | ConfigDate32 | CONFIG_DATE_3 | — | — |
| 34 | ConfigDate42 | CONFIG_DATE_4 | — | — |
| 35 | ConfigDate52 | CONFIG_DATE_5 | — | — |
| 36 | ConfigNum12 | CONFIG_NUM_1 | — | — |
| 37 | ConfigNum22 | CONFIG_NUM_2 | — | — |
| 38 | ConfigNum32 | CONFIG_NUM_3 | — | — |
| 39 | ConfigNum42 | CONFIG_NUM_4 | — | — |
| 40 | ConfigNum52 | CONFIG_NUM_5 | — | — |
| 41 | CreatedBy2 | CREATED_BY | — | — |
| 42 | CreationDate2 | CREATION_DATE | — | — |
| 43 | CreditAmt | CREDIT_AMT | — | ✅ |
| 44 | CurrencyCode1 | CURRENCY_CODE | — | ✅ |
| 45 | DebitAmt | DEBIT_AMT | — | ✅ |
| 46 | LastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 47 | LastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 48 | LastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 49 | NoBillFlag | NO_BILL_FLAG | — | ✅ |
| 50 | ObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 51 | PersonId2 | PERSON_ID | — | — |
| 52 | RecordedDate | RECORDED_DATE | — | ✅ |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |
| 5 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 6 | PersonId4 | PERSON_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId3 | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
