---
id: DOC-HCM-891
doc_type: system-doc
title: "ZX_JURISDICTIONS_TL — (título a preencher)"
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
  - ZX_JURISDICTIONS_TL
  - zx_jurisdictions_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_JURISDICTIONS_TL

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
| 8 | TAX_JURISDICTION_ID | — | — | — | — | — | — |
| 9 | TAX_JURISDICTION_NAME | — | — | — | — | — | — |

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
| LANGUAGE | TaxJurisTLLanguage | — |
| TAX_JURISDICTION_ID | TaxJurisTLTaxJurisdictionId | — |
| TAX_JURISDICTION_NAME | TaxJurisTaxJurisdictionName | ✅ |

### [[taxjurisdictionextractpvo|TaxJurisdictionExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxJurisdictionTLCreatedBy1 | ✅ |
| CREATION_DATE | TaxJurisdictionTLCreationDate1 | ✅ |
| LANGUAGE | TaxJurisdictionTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxJurisdictionTLLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionTLLastUpdateLogin1 | ✅ |
| LAST_UPDATED_BY | TaxJurisdictionTLLastUpdatedBy1 | ✅ |
| SOURCE_LANG | TaxJurisdictionTLSourceLang | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTLTaxJurisdictionId | ✅ |
| TAX_JURISDICTION_NAME | TaxJurisdictionTLTaxJurisdictionName | ✅ |

### [[taxjurisdictiontlextractpvo|TaxJurisdictionTLExtractPVO]] (OTHER · BICC: 9/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxJurisdictionTLCreatedBy | ✅ |
| CREATION_DATE | TaxJurisdictionTLCreationDate | ✅ |
| LANGUAGE | TaxJurisdictionTLLanguage | ✅ |
| LAST_UPDATE_DATE | TaxJurisdictionTLLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionTLLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaxJurisdictionTLLastUpdatedBy | ✅ |
| SOURCE_LANG | TaxJurisdictionTLSourceLang | ✅ |
| TAX_JURISDICTION_ID | TaxJurisdictionTLTaxJurisdictionId | ✅ |
| TAX_JURISDICTION_NAME | TaxJurisdictionTLTaxJurisdictionName | ✅ |

### [[taxjurisdictiontranslationpvo|TaxJurisdictionTranslationPVO]] (AP · BICC: 4/9)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaxJurisdictionTLPEOCreatedBy | — |
| CREATION_DATE | TaxJurisdictionTLPEOCreationDate | — |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | TaxJurisdictionTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaxJurisdictionTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | TaxJurisdictionTLPEOLastUpdatedBy | — |
| SOURCE_LANG | TaxJurisdictionTLPEOSourceLang | — |
| TAX_JURISDICTION_ID | TaxJurisdictionId | ✅ |
| TAX_JURISDICTION_NAME | TaxJurisdictionTLPEOTaxJurisdictionName | ✅ |
