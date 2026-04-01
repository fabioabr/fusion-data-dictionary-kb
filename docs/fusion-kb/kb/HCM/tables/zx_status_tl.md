---
id: DOC-HCM-910
doc_type: system-doc
title: "ZX_STATUS_TL — (título a preencher)"
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
  - ZX_STATUS_TL
  - zx_status_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_STATUS_TL

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
| 8 | TAX_STATUS_ID | — | — | — | — | — | — |
| 9 | TAX_STATUS_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaxStatusLanguage | — |
| TAX_STATUS_ID | TaxStatusTLTaxStatusId | — |
| TAX_STATUS_NAME | TaxStatusTaxStatusName | — |

### [[taxstatusextractpvo|TaxStatusExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxStatusTLCreatedBy1 | ✅ |
| CREATION_DATE | TaxStatusTLCreationDate1 | ✅ |
| LANGUAGE | TaxStatusTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxStatusTLLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | TaxStatusTLLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | TaxStatusTLLastUpdatedBy1 | ✅ |
| SOURCE_LANG | TaxStatusTLSourceLang | ✅ |
| TAX_STATUS_ID | TaxStatusTLTaxStatusId1 | ✅ |
| TAX_STATUS_NAME | TaxStatusTLTaxStatusName | ✅ |

### [[taxstatustlextractpvo|TaxStatusTLExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxStatusTLCreatedBy | ✅ |
| CREATION_DATE | TaxStatusTLCreationDate | ✅ |
| LANGUAGE | TaxStatusTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxStatusTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxStatusTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaxStatusTLLastUpdatedBy | ✅ |
| SOURCE_LANG | TaxStatusTLSourceLang | ✅ |
| TAX_STATUS_ID | TaxStatusTLTaxStatusId | ✅ |
| TAX_STATUS_NAME | TaxStatusTLTaxStatusName | ✅ |

### [[taxstatustranslationpvo|TaxStatusTranslationPVO]] (AP · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxStatusTLPEOCreatedBy | — |
| CREATION_DATE | TaxStatusTLPEOCreationDate | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | TaxStatusTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxStatusTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxStatusTLPEOLastUpdatedBy | — |
| SOURCE_LANG | TaxStatusTLPEOSourceLang | — |
| TAX_STATUS_ID | TaxStatusId | ✅ |
| TAX_STATUS_NAME | TaxStatusTLPEOTaxStatusName | ✅ |
