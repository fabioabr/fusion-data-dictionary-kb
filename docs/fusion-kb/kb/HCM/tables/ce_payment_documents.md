---
id: DOC-HCM-069
doc_type: system-doc
title: "CE_PAYMENT_DOCUMENTS — (título a preencher)"
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
  - CE_PAYMENT_DOCUMENTS
  - ce_payment_documents
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# CE_PAYMENT_DOCUMENTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 2 | PAYMENT_DOCUMENT_ID | — | — | — | — | — | — |
| 3 | PAYMENT_DOCUMENT_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[disbursementheaderpvo|DisbursementHeaderPVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDocLastUpdateDate | ✅ |
| PAYMENT_DOCUMENT_ID | PayDocPaymentDocumentId | — |
| PAYMENT_DOCUMENT_NAME | PayDocPaymentDocumentName | ✅ |

### [[paiddisbursementschedulepvo|PaidDisbursementSchedulePVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDocLastUpdateDate | ✅ |
| PAYMENT_DOCUMENT_ID | PayDocPaymentDocumentId | — |
| PAYMENT_DOCUMENT_NAME | PayDocPaymentDocumentName | ✅ |

### [[paymenthistorydistributionpvo|PaymentHistoryDistributionPVO]] (AP · BICC: 2/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LAST_UPDATE_DATE | PayDocLastUpdateDate | ✅ |
| PAYMENT_DOCUMENT_ID | PayDocPaymentDocumentId | — |
| PAYMENT_DOCUMENT_NAME | PayDocPaymentDocumentName | ✅ |
