---
id: DOC-OTHER-PVO-InvoiceFormatExtractPVO
doc_type: system-doc
title: "InvoiceFormatExtractPVO — PVO Cross-Module"
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
  - InvoiceFormatExtractPVO
  - invoiceformatextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvoiceFormatExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Invoice Format Extract. Acessa as tabelas: PJB_INVOICE_FORMATS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjbBiccExtractAM.InvoiceFormatExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjb_invoice_formats|PJB_INVOICE_FORMATS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[pjb_invoice_formats|PJB_INVOICE_FORMATS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvoiceFormatPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InvoiceFormatPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InvoiceFormatPEOCustomerInvoiceFlag | CUSTOMER_INVOICE_FLAG | — | ✅ |
| 4 | InvoiceFormatPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | InvoiceFormatPEOFixedFormatFlag | FIXED_FORMAT_FLAG | — | ✅ |
| 6 | InvoiceFormatPEOInternalInvoiceFlag | INTERNAL_INVOICE_FLAG | — | ✅ |
| 7 | InvoiceFormatPEOInvoiceFormatId | INVOICE_FORMAT_ID | 🔑 | ✅ |
| 8 | InvoiceFormatPEOInvoiceFormatType | INVOICE_FORMAT_TYPE | — | ✅ |
| 9 | InvoiceFormatPEOInvoiceGroupId | INVOICE_GROUP_ID | — | ✅ |
| 10 | InvoiceFormatPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | InvoiceFormatPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | InvoiceFormatPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | InvoiceFormatPEOName | NAME | — | ✅ |
| 14 | InvoiceFormatPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | InvoiceFormatPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
