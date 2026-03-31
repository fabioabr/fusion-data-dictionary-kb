---
id: DOC-HCM-902
doc_type: system-doc
title: "ZX_REGIMES_TL — (título a preencher)"
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
  - ZX_REGIMES_TL
  - zx_regimes_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_REGIMES_TL

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
| 8 | TAX_REGIME_ID | — | — | — | — | — | — |
| 9 | TAX_REGIME_NAME | — | — | — | — | — | — |

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
| LANGUAGE | TaxRegimeTLLanguage | — |
| TAX_REGIME_ID | TaxRegimeTLTaxRegimeId | — |
| TAX_REGIME_NAME | TaxRegimeTaxRegimeName | ✅ |

### [[taxregimeextractpvo|TaxRegimeExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxRegimeTLCreatedBy1 | ✅ |
| CREATION_DATE | TaxRegimeTLCreationDate1 | ✅ |
| LANGUAGE | TaxRegimeTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxRegimeTLLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | TaxRegimeTLLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | TaxRegimeTLLastUpdatedBy1 | ✅ |
| SOURCE_LANG | TaxRegimeTLSourceLang | ✅ |
| TAX_REGIME_ID | TaxRegimeTLTaxRegimeId | ✅ |
| TAX_REGIME_NAME | TaxRegimeTLTaxRegimeName | ✅ |

### [[taxregimetlextractpvo|TaxRegimeTLExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxRegimeTLCreatedBy | ✅ |
| CREATION_DATE | TaxRegimeTLCreationDate | ✅ |
| LANGUAGE | TaxRegimeTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxRegimeTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxRegimeTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaxRegimeTLLastUpdatedBy | ✅ |
| SOURCE_LANG | TaxRegimeTLSourceLang | ✅ |
| TAX_REGIME_ID | TaxRegimeTLTaxRegimeId | ✅ |
| TAX_REGIME_NAME | TaxRegimeTLTaxRegimeName | ✅ |

### [[taxregimetranslationpvo|TaxRegimeTranslationPVO]] (AP · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxRegimeTLPEOCreatedBy | — |
| CREATION_DATE | TaxRegimeTLPEOCreationDate | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | TaxRegimeTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxRegimeTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxRegimeTLPEOLastUpdatedBy | — |
| SOURCE_LANG | TaxRegimeTLPEOSourceLang | — |
| TAX_REGIME_ID | TaxRegimeId | ✅ |
| TAX_REGIME_NAME | TaxRegimeTLPEOTaxRegimeName | ✅ |
