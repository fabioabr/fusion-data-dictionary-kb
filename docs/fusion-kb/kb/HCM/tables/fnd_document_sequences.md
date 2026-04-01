---
id: DOC-HCM-129
doc_type: system-doc
title: "FND_DOCUMENT_SEQUENCES — (título a preencher)"
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
  - FND_DOCUMENT_SEQUENCES
  - fnd_document_sequences
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DOCUMENT_SEQUENCES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | AUDIT_TABLE_NAME | — | — | — | — | — | — |
| 2 | DB_SEQUENCE_NAME | — | — | — | — | — | — |
| 3 | DOC_SEQUENCE_ID | — | — | — | — | — | — |
| 4 | NAME | — | — | — | — | — | — |
| 5 | TABLE_NAME | — | — | — | — | — | — |
| 6 | TYPE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[adjustmentdistributionpvo|AdjustmentDistributionPVO]] (AR · BICC: 2/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| DOC_SEQUENCE_ID | TrxDocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| NAME | DocSeqName | ✅ |
| NAME | TrxDocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |
| TABLE_NAME | DocSeqTableName | — |

### [[adjustmentpvo|AdjustmentPVO]] (AR · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| DOC_SEQUENCE_ID | TrxDocSeqHdrDocSequenceId | — |
| NAME | DocSeqName | ✅ |
| NAME | TrxDocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqTableName | — |

### [[completedtrxrevadjdistributionpvo|CompletedTrxRevAdjDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[completedtrxrevenuedistributionpvo|CompletedTrxRevenueDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[creditmemoapplicationdistributionpvo|CreditMemoApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| NAME | DocSeqName | — |
| TABLE_NAME | DocSeqHdrTableName | — |
| TABLE_NAME | DocSeqTableName | — |

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |

### [[headersalescreditpvo|HeaderSalesCreditPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[invoiceheaderpvo|InvoiceHeaderPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |

### [[journalentrylinepvo|JournalEntryLinePVO]] (GL · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| NAME | DocSeqName | ✅ |
| TABLE_NAME | DocSeqTableName | — |

### [[journalheaderpvo|JournalHeaderPVO]] (GL · BICC: 3/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DB_SEQUENCE_NAME | DocSequenceDbSequenceName | ✅ |
| DB_SEQUENCE_NAME | LocalDocSequenceDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| DOC_SEQUENCE_ID | LocalDocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |
| NAME | LocalDocSequenceName | ✅ |
| TYPE | DocSequenceType | — |
| TYPE | LocalDocSequenceType | — |

### [[journallinepvo|JournalLinePVO]] (GL · BICC: 3/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DB_SEQUENCE_NAME | DocSequenceDbSequenceName | ✅ |
| DB_SEQUENCE_NAME | LocalDocSequenceDbSequenceName | — |
| DB_SEQUENCE_NAME | SlaDocSequenceDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| DOC_SEQUENCE_ID | LocalDocSequenceDocSequenceId | — |
| DOC_SEQUENCE_ID | SlaDocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |
| NAME | LocalDocSequenceName | ✅ |
| NAME | SlaDocSequenceName | — |
| TYPE | DocSequenceType | — |
| TYPE | LocalDocSequenceType | — |
| TYPE | SlaDocSequenceType | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[miscreceiptdistributionpvo|MiscReceiptDistributionPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| NAME | DocSeqName | ✅ |
| TABLE_NAME | DocSeqTableName | — |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DOC_SEQUENCE_ID | DocSequenceDocSequenceId | — |
| NAME | DocSequenceName | ✅ |

### [[paymentschedulepvo|PaymentSchedulePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[receiptapplicationdistributionpvo|ReceiptApplicationDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| NAME | DocSeqName | — |
| TABLE_NAME | DocSeqHdrTableName | — |
| TABLE_NAME | DocSeqTableName | — |

### [[receiptapplicationdistributionvc|ReceiptApplicationDistributionVC]] (AR · BICC: 1/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| NAME | DocSeqName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |
| TABLE_NAME | DocSeqTableName | — |

### [[receiptapplicationpvo|ReceiptApplicationPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| NAME | DocSeqName | ✅ |
| TABLE_NAME | DocSeqTableName | — |

### [[receiptheaderpvo|ReceiptHeaderPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| NAME | DocSeqName | ✅ |
| TABLE_NAME | DocSeqTableName | — |

### [[salesinvoicecustomertrxlinesalescreditpvo|SalesInvoiceCustomerTrxLineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[salesinvoicecustomertrxlinespvo|SalesInvoiceCustomerTrxLinesPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[subledgerjournaldistributionpvo|SubledgerJournalDistributionPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqDocSequenceId | — |
| NAME | DocSeqName | — |
| TABLE_NAME | DocSeqTableName | — |

### [[transactionheaderbillsreceivablepvo|TransactionHeaderBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionheadernovcpvo|TransactionHeaderNoVCPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionheaderpvo|TransactionHeaderPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | — |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AUDIT_TABLE_NAME | DocSeqHdrAuditTableName | — |
| DB_SEQUENCE_NAME | DocSeqHdrDbSequenceName | — |
| DOC_SEQUENCE_ID | DocSeqHdrDocSequenceId | — |
| NAME | DocSeqHdrName | ✅ |
| TABLE_NAME | DocSeqHdrTableName | — |
