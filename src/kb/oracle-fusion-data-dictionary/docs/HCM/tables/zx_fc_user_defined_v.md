---
id: DOC-HCM-888
doc_type: system-doc
title: "ZX_FC_USER_DEFINED_V — (título a preencher)"
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
  - ZX_FC_USER_DEFINED_V
  - zx_fc_user_defined_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_USER_DEFINED_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 2 | CLASSIFICATION_NAME | — | — | — | — | — | — |
| 3 | COUNTRY_CODE | — | — | — | — | — | — |
| 4 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 5 | EFFECTIVE_TO | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassPEOClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassPEOClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassPEOCountryCode1 | — |
| EFFECTIVE_FROM | UserDefinedFiscClassPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | UserDefinedFiscClassPEOEffectiveTo1 | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassPEOClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassPEOClassificationName | — |
| COUNTRY_CODE | UserDefinedFiscClassPEOCountryCode2 | — |
| EFFECTIVE_FROM | UserDefinedFiscClassPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | UserDefinedFiscClassPEOEffectiveTo1 | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassPEOClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassPEOClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassPEOCountryCode1 | — |
| EFFECTIVE_FROM | UserDefinedFiscClassPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | UserDefinedFiscClassPEOEffectiveTo1 | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassPEOClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassPEOClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassPEOCountryCode2 | — |
| EFFECTIVE_FROM | UserDefinedFiscClassPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | UserDefinedFiscClassPEOEffectiveTo1 | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassPEOClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassPEOClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassPEOCountryCode2 | — |
| EFFECTIVE_FROM | UserDefinedFiscClassPEOEffectiveFrom1 | — |
| EFFECTIVE_TO | UserDefinedFiscClassPEOEffectiveTo1 | — |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | ✅ |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | ✅ |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | ✅ |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassCountryCode | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassClassificationName | — |
| COUNTRY_CODE | UserDefinedFiscClassCountryCode | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UserDefinedFiscClassClassificationCode | — |
| CLASSIFICATION_NAME | UserDefinedFiscClassClassificationName | ✅ |
| COUNTRY_CODE | UserDefinedFiscClassCountryCode | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | ✅ |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | — |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | — |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | ✅ |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | ✅ |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | LineUsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_CODE | UsrDfndFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | LineUsrDfndFiscClsClassificationName | ✅ |
| CLASSIFICATION_NAME | UsrDfndFiscClsClassificationName | ✅ |
| COUNTRY_CODE | LineUsrDfndFiscClsCountryCode | — |
| COUNTRY_CODE | UsrDfndFiscClsCountryCode | — |
