---
id: DOC-HCM-516
doc_type: system-doc
title: "IBY_FNDCPT_TX_EXTENSIONS — (título a preencher)"
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
  - IBY_FNDCPT_TX_EXTENSIONS
  - iby_fndcpt_tx_extensions
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# IBY_FNDCPT_TX_EXTENSIONS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ADDITIONAL_INFO | — | — | — | — | — | — |
| 2 | ENCRYPTED | — | — | — | — | — | — |
| 3 | INSTRUMENT_SECURITY_CODE | — | — | — | — | — | — |
| 4 | INSTR_SEC_CODE_LENGTH | — | — | — | — | — | — |
| 5 | PAYMENT_CHANNEL_CODE | — | — | — | — | — | — |
| 6 | PAYMENT_SYSTEM_ORDER_NUMBER | — | — | — | — | — | — |
| 7 | PO_LINE_NUMBER | — | — | — | — | — | — |
| 8 | PO_NUMBER | — | — | — | — | — | — |
| 9 | TRXN_EXTENSION_ID | — | — | — | — | — | — |
| 10 | TRXN_REF_NUMBER1 | — | — | — | — | — | — |
| 11 | TRXN_REF_NUMBER2 | — | — | — | — | — | — |
| 12 | VOICE_AUTHORIZATION_CODE | — | — | — | — | — | — |
| 13 | VOICE_AUTHORIZATION_DATE | — | — | — | — | — | — |
| 14 | VOICE_AUTHORIZATION_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ADDITIONAL_INFO | TrxExtnLineAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| ENCRYPTED | TrxExtnLineEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnLineInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnLineInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnLinePaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnLinePaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_LINE_NUMBER | TrxExtnLinePoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| PO_NUMBER | TrxExtnLinePoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_EXTENSION_ID | TrxExtnLineTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER1 | TrxExtnLineTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| TRXN_REF_NUMBER2 | TrxExtnLineTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnLineVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnLineVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnLineVoiceAuthorizationFlag | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnAdditionalInfo | — |
| ENCRYPTED | TrxExtnEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnPoLineNumber | — |
| PO_NUMBER | TrxExtnPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnVoiceAuthorizationFlag | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PAYMENT_SYSTEM_ORDER_NUMBER | RcptPmtTrxnExtPaymentSystemOrderNumber | — |
| PO_LINE_NUMBER | RcptPmtTrxnExtPoLineNumber | — |
| PO_NUMBER | RcptPmtTrxnExtPoNumber | — |
| TRXN_EXTENSION_ID | RcptPmtTrxnExtTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | RcptPmtTrxnExtTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | RcptPmtTrxnExtTrxnRefNumber2 | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PAYMENT_SYSTEM_ORDER_NUMBER | RcptPmtTrxnExtPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | RcptPmtTrxnExtPoLineNumber | — |
| PO_NUMBER | RcptPmtTrxnExtPoNumber | — |
| TRXN_EXTENSION_ID | RcptPmtTrxnExtTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | RcptPmtTrxnExtTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | RcptPmtTrxnExtTrxnRefNumber2 | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnAdditionalInfo | — |
| ENCRYPTED | TrxExtnEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnPoLineNumber | — |
| PO_NUMBER | TrxExtnPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnVoiceAuthorizationFlag | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnAdditionalInfo | — |
| ENCRYPTED | TrxExtnEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnPoLineNumber | — |
| PO_NUMBER | TrxExtnPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnVoiceAuthorizationFlag | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | — |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | — |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ADDITIONAL_INFO | TrxExtnLineAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| ENCRYPTED | TrxExtnLineEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnLineInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnLineInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnLinePaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnLinePaymentSystemOrderNumber | — |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_LINE_NUMBER | TrxExtnLinePoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| PO_NUMBER | TrxExtnLinePoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_EXTENSION_ID | TrxExtnLineTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER1 | TrxExtnLineTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| TRXN_REF_NUMBER2 | TrxExtnLineTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnLineVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnLineVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnLineVoiceAuthorizationFlag | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ADDITIONAL_INFO | TrxExtnLineAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| ENCRYPTED | TrxExtnLineEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnLineInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnLineInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnLinePaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnLinePaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_LINE_NUMBER | TrxExtnLinePoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| PO_NUMBER | TrxExtnLinePoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_EXTENSION_ID | TrxExtnLineTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER1 | TrxExtnLineTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| TRXN_REF_NUMBER2 | TrxExtnLineTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnLineVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnLineVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnLineVoiceAuthorizationFlag | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ADDITIONAL_INFO | TrxExtnHdrAdditionalInfo | — |
| ADDITIONAL_INFO | TrxExtnLineAdditionalInfo | — |
| ENCRYPTED | TrxExtnHdrEncrypted | — |
| ENCRYPTED | TrxExtnLineEncrypted | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnHdrInstrSecCodeLength | — |
| INSTR_SEC_CODE_LENGTH | TrxExtnLineInstrSecCodeLength | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnHdrInstrumentSecurityCode | — |
| INSTRUMENT_SECURITY_CODE | TrxExtnLineInstrumentSecurityCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnHdrPaymentChannelCode | — |
| PAYMENT_CHANNEL_CODE | TrxExtnLinePaymentChannelCode | — |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnHdrPaymentSystemOrderNumber | ✅ |
| PAYMENT_SYSTEM_ORDER_NUMBER | TrxExtnLinePaymentSystemOrderNumber | ✅ |
| PO_LINE_NUMBER | TrxExtnHdrPoLineNumber | — |
| PO_LINE_NUMBER | TrxExtnLinePoLineNumber | — |
| PO_NUMBER | TrxExtnHdrPoNumber | — |
| PO_NUMBER | TrxExtnLinePoNumber | — |
| TRXN_EXTENSION_ID | TrxExtnHdrTrxnExtensionId | — |
| TRXN_EXTENSION_ID | TrxExtnLineTrxnExtensionId | — |
| TRXN_REF_NUMBER1 | TrxExtnHdrTrxnRefNumber1 | — |
| TRXN_REF_NUMBER1 | TrxExtnLineTrxnRefNumber1 | — |
| TRXN_REF_NUMBER2 | TrxExtnHdrTrxnRefNumber2 | — |
| TRXN_REF_NUMBER2 | TrxExtnLineTrxnRefNumber2 | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnHdrVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_CODE | TrxExtnLineVoiceAuthorizationCode | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnHdrVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_DATE | TrxExtnLineVoiceAuthorizationDate | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnHdrVoiceAuthorizationFlag | — |
| VOICE_AUTHORIZATION_FLAG | TrxExtnLineVoiceAuthorizationFlag | — |
