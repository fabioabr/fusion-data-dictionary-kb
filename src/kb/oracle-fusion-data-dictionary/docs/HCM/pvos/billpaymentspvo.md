---
id: DOC-HCM-PVO-BillPaymentsPVO
doc_type: system-doc
title: "BillPaymentsPVO — PVO Human Capital Management"
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
  - BillPaymentsPVO
  - billpaymentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BillPaymentsPVO

## 📌 Visão Geral

Disponibiliza pagamentos de billing de beneficios com ajustes e creditos. Suporta gestao de recebimentos e conciliacao de pagamentos de planos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BillPaymentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 122 | 4 | 1 | 22 | 18% |

---

## 🔗 Tabelas Relacionadas

- [[ben_bill_payments|BEN_BILL_PAYMENTS]] — 61 atributos (1 PKs, 22 BICC)
- [[ben_bill_per_credit|BEN_BILL_PER_CREDIT]] — 52 atributos
- [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]] — 6 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos

---

## ⚙️ Atributos

### [[ben_bill_payments|BEN_BILL_PAYMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdjAmt | ADJ_AMT | — | ✅ |
| 2 | AdjDate | ADJ_DATE | — | ✅ |
| 3 | AmtPaid | AMT_PAID | — | ✅ |
| 4 | BillNum | BILL_NUM | — | ✅ |
| 5 | BillPaymentId | BILL_PAYMENT_ID | 🔑 | ✅ |
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
| 27 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 28 | Comments | COMMENTS | — | ✅ |
| 29 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 30 | ConfigChar2 | CONFIG_CHAR_2 | — | — |
| 31 | ConfigChar3 | CONFIG_CHAR_3 | — | — |
| 32 | ConfigChar4 | CONFIG_CHAR_4 | — | — |
| 33 | ConfigChar5 | CONFIG_CHAR_5 | — | — |
| 34 | ConfigDate1 | CONFIG_DATE_1 | — | — |
| 35 | ConfigDate2 | CONFIG_DATE_2 | — | — |
| 36 | ConfigDate3 | CONFIG_DATE_3 | — | — |
| 37 | ConfigDate4 | CONFIG_DATE_4 | — | — |
| 38 | ConfigDate5 | CONFIG_DATE_5 | — | — |
| 39 | ConfigNum1 | CONFIG_NUM_1 | — | — |
| 40 | ConfigNum2 | CONFIG_NUM_2 | — | — |
| 41 | ConfigNum3 | CONFIG_NUM_3 | — | — |
| 42 | ConfigNum4 | CONFIG_NUM_4 | — | — |
| 43 | ConfigNum5 | CONFIG_NUM_5 | — | — |
| 44 | CreatedBy | CREATED_BY | — | ✅ |
| 45 | CreationDate | CREATION_DATE | — | ✅ |
| 46 | CurrencyCode | CURRENCY_CODE | — | ✅ |
| 47 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 49 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
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
| 61 | PersonId | PERSON_ID | — | — |

### [[ben_bill_per_credit|BEN_BILL_PER_CREDIT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BillPaymentId1 | BILL_PAYMENT_ID | — | — |
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
| 24 | BusinessGroupId1 | BUSINESS_GROUP_ID | — | — |
| 25 | Comments1 | COMMENTS | — | — |
| 26 | ConfigChar11 | CONFIG_CHAR_1 | — | — |
| 27 | ConfigChar21 | CONFIG_CHAR_2 | — | — |
| 28 | ConfigChar31 | CONFIG_CHAR_3 | — | — |
| 29 | ConfigChar41 | CONFIG_CHAR_4 | — | — |
| 30 | ConfigChar51 | CONFIG_CHAR_5 | — | — |
| 31 | ConfigDate11 | CONFIG_DATE_1 | — | — |
| 32 | ConfigDate21 | CONFIG_DATE_2 | — | — |
| 33 | ConfigDate31 | CONFIG_DATE_3 | — | — |
| 34 | ConfigDate41 | CONFIG_DATE_4 | — | — |
| 35 | ConfigDate51 | CONFIG_DATE_5 | — | — |
| 36 | ConfigNum11 | CONFIG_NUM_1 | — | — |
| 37 | ConfigNum21 | CONFIG_NUM_2 | — | — |
| 38 | ConfigNum31 | CONFIG_NUM_3 | — | — |
| 39 | ConfigNum41 | CONFIG_NUM_4 | — | — |
| 40 | ConfigNum51 | CONFIG_NUM_5 | — | — |
| 41 | CreatedBy1 | CREATED_BY | — | — |
| 42 | CreationDate1 | CREATION_DATE | — | — |
| 43 | CreditAmt | CREDIT_AMT | — | — |
| 44 | CurrencyCode1 | CURRENCY_CODE | — | — |
| 45 | DebitAmt | DEBIT_AMT | — | — |
| 46 | LastUpdateDate1 | LAST_UPDATE_DATE | — | — |
| 47 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 48 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 49 | NoBillFlag | NO_BILL_FLAG | — | — |
| 50 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 51 | PersonId1 | PERSON_ID | — | — |
| 52 | RecordedDate | RECORDED_DATE | — | — |

### [[ben_per_benefit_group_f|BEN_PER_BENEFIT_GROUP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BenefitGroupId | BENEFIT_GROUP_ID | — | — |
| 2 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 3 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | — |
| 4 | LeBenefitGroupId | LE_BENEFIT_GROUP_ID | — | — |
| 5 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 6 | PersonId3 | PERSON_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 3 | PersonId2 | PERSON_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
