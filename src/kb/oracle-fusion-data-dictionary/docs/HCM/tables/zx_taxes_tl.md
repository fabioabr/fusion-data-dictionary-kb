---
id: DOC-HCM-912
doc_type: system-doc
title: "ZX_TAXES_TL — (título a preencher)"
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
  - ZX_TAXES_TL
  - zx_taxes_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_TAXES_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | LANGUAGE | — | — | — | — | — | — |
| 4 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 5 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 6 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 7 | SOURCE_LANG | — | — | — | — | — | — |
| 8 | TAX_FULL_NAME | — | — | — | — | — | — |
| 9 | TAX_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | WhtTaxesTLLanguage | — |
| TAX_FULL_NAME | WhtTaxesTaxFullName | ✅ |
| TAX_ID | WhtTaxesTLTaxId | — |

### [[transactiontaxextractpvo|TransactionTaxExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TransactionTaxTLCreatedBy | ✅ |
| CREATION_DATE | TransactionTaxTLCreationDate | ✅ |
| LANGUAGE | TransactionTaxTLLanguage | ✅ |
| LAST_UPDATE_DATE | TransactionTaxTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTaxTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TransactionTaxTLLastUpdatedBy | ✅ |
| SOURCE_LANG | TransactionTaxTLSourceLang | ✅ |
| TAX_FULL_NAME | TransactionTaxTLTaxFullName | ✅ |
| TAX_ID | TransactionTaxTLTaxId | ✅ |

### [[transactiontaxtlextractpvo|TransactionTaxTLExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TransactionTaxTLCreatedBy | ✅ |
| CREATION_DATE | TransactionTaxTLCreationDate | ✅ |
| LANGUAGE | TransactionTaxTLLanguage | ✅ |
| LAST_UPDATE_DATE | TransactionTaxTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTaxTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TransactionTaxTLLastUpdatedBy | ✅ |
| SOURCE_LANG | TransactionTaxTLSourceLang | ✅ |
| TAX_FULL_NAME | TransactionTaxTLTaxFullName | ✅ |
| TAX_ID | TransactionTaxTLTaxId | ✅ |

### [[transactiontaxtranslationpvo|TransactionTaxTranslationPVO]] (AP · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TransactionTaxTLPEOCreatedBy | — |
| CREATION_DATE | TransactionTaxTLPEOCreationDate | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | TransactionTaxTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TransactionTaxTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TransactionTaxTLPEOLastUpdatedBy | — |
| SOURCE_LANG | TransactionTaxTLPEOSourceLang | — |
| TAX_FULL_NAME | TransactionTaxTLPEOTaxFullName | ✅ |
| TAX_ID | TaxId | ✅ |

### [[withholdingbucketpvo|WithholdingBucketPVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaxesTLLanguage | — |
| TAX_FULL_NAME | TaxesTaxFullName | ✅ |
| TAX_ID | TaxesTLTaxId | — |
