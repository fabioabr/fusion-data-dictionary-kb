---
id: DOC-HCM-518
doc_type: system-doc
title: "IBY_PAYMENT_CODES_VL — (título a preencher)"
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
  - IBY_PAYMENT_CODES_VL
  - iby_payment_codes_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_PAYMENT_CODES_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | END_DATE | — | — | — | — | — | — |
| 5 | FORMAT_VALUE | — | — | — | — | — | — |
| 6 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 7 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 8 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 9 | MEANING | — | — | — | — | — | — |
| 10 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 11 | PAYMENT_CODE | — | — | — | — | — | — |
| 12 | PAYMENT_CODE_TYPE | — | — | — | — | — | — |
| 13 | SEEDED_FLAG | — | — | — | — | — | — |
| 14 | START_DATE | — | — | — | — | — | — |
| 15 | TERRITORY_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[expensedistributionpvo|ExpenseDistributionPVO]] (OTHER · BICC: 2/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PayDelcodeCreatedBy | — |
| CREATED_BY | PayReacodeCreatedBy | — |
| CREATION_DATE | PayDelcodeCreationDate | — |
| CREATION_DATE | PayReacodeCreationDate | — |
| DESCRIPTION | PayDelcodeDescription | — |
| DESCRIPTION | PayReacodeDescription | — |
| END_DATE | PayDelcodeEndDate | — |
| END_DATE | PayReacodeEndDate | — |
| FORMAT_VALUE | PayDelcodeFormatValue | — |
| FORMAT_VALUE | PayReacodeFormatValue | — |
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PayDelcodeLastUpdateLogin | — |
| LAST_UPDATE_LOGIN | PayReacodeLastUpdateLogin | — |
| LAST_UPDATED_BY | PayDelcodeLastUpdatedBy | — |
| LAST_UPDATED_BY | PayReacodeLastUpdatedBy | — |
| MEANING | PayDelcodeMeaning | — |
| MEANING | PayReacodeMeaning | — |
| OBJECT_VERSION_NUMBER | PayDelcodeObjectVersionNumber | — |
| OBJECT_VERSION_NUMBER | PayReacodeObjectVersionNumber | — |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |
| SEEDED_FLAG | PayDelcodeSeededFlag | — |
| SEEDED_FLAG | PayReacodeSeededFlag | — |
| START_DATE | PayDelcodeStartDate | — |
| START_DATE | PayReacodeStartDate | — |
| TERRITORY_CODE | PayDelcodeTerritoryCode | — |
| TERRITORY_CODE | PayReacodeTerritoryCode | — |

### [[invoiceheaderholdspvo|InvoiceHeaderHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | — |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | — |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | — |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | — |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[invoiceholdpvo|InvoiceHoldPVO]] (AP · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | ✅ |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[invoiceholdpvoactiveholds|InvoiceHoldPVOActiveHolds]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | — |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | — |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[invoicelineholdspvo|InvoiceLineHoldsPVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | — |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | — |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[invoicepaymentschedulepvo|InvoicePaymentSchedulePVO]] (AP · BICC: 6/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | ✅ |
| MEANING | PayDelcodeMeaning | ✅ |
| MEANING | PayReacodeMeaning | ✅ |
| PAYMENT_CODE | PayDelcodePaymentCode | ✅ |
| PAYMENT_CODE | PayReacodePaymentCode | ✅ |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[paymentcodes|PaymentCodes]] (AR · BICC: 4/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | PaymentCodesCreatedBy | — |
| CREATION_DATE | PaymentCodesCreationDate | — |
| DESCRIPTION | PaymentCodesDescription | — |
| END_DATE | PaymentCodesEndDate | — |
| FORMAT_VALUE | PaymentCodesFormatValue | — |
| LAST_UPDATE_DATE | PaymentCodesLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PaymentCodesLastUpdateLogin | — |
| LAST_UPDATED_BY | PaymentCodesLastUpdatedBy | — |
| MEANING | PaymentCodesMeaning | ✅ |
| OBJECT_VERSION_NUMBER | PaymentCodesObjectVersionNumber | — |
| PAYMENT_CODE | PaymentCode | ✅ |
| PAYMENT_CODE_TYPE | PaymentCodeType | ✅ |
| SEEDED_FLAG | PaymentCodesSeededFlag | — |
| START_DATE | PaymentCodesStartDate | — |
| TERRITORY_CODE | PaymentCodesTerritoryCode | — |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | ✅ |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |

### [[prepaymentappliationdistributionpvo|PrepaymentAppliationDistributionPVO]] (AP · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDelcodeLastUpdateDate | ✅ |
| LAST_UPDATE_DATE | PayReacodeLastUpdateDate | ✅ |
| PAYMENT_CODE | PayDelcodePaymentCode | — |
| PAYMENT_CODE | PayReacodePaymentCode | — |
| PAYMENT_CODE_TYPE | PayDelcodePaymentCodeType | — |
| PAYMENT_CODE_TYPE | PayReacodePaymentCodeType | — |
