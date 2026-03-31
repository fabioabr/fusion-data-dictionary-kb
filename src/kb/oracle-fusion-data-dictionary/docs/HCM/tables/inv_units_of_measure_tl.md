---
id: DOC-HCM-528
doc_type: system-doc
title: "INV_UNITS_OF_MEASURE_TL — (título a preencher)"
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
  - INV_UNITS_OF_MEASURE_TL
  - inv_units_of_measure_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# INV_UNITS_OF_MEASURE_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | LANGUAGE | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 8 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 9 | SOURCE_LANG | — | — | — | — | — | — |
| 10 | UNIT_OF_MEASURE | — | — | — | — | — | — |
| 11 | UNIT_OF_MEASURE_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | ✅ |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[invunitsofmeasuretranslationpvo|InvUnitsOfMeasureTranslationPVO]] (OTHER · BICC: 11/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| UNIT_OF_MEASURE | UnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | UnitOfMeasureId | ✅ |

### [[invuompvo|InvUomPVO]] (OTHER · BICC: 6/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | InvUomTLPEOCreatedBy | — |
| CREATION_DATE | InvUomTLPEOCreationDate | — |
| DESCRIPTION | InvUomTLPEODescription | ✅ |
| LANGUAGE | InvUomTLPEOLanguage | ✅ |
| LAST_UPDATE_DATE | InvUomTLPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvUomTLPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvUomTLPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | InvUomTLPEOObjectVersionNumber | — |
| SOURCE_LANG | InvUomTLPEOSourceLang | ✅ |
| UNIT_OF_MEASURE | InvUomTLPEOUnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | InvUomTLPEOUnitOfMeasureId | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | ✅ |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | — |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | — |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | — |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | — |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | — |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | — |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | ✅ |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | UomDescription | ✅ |
| LANGUAGE | UomTLLanguage | — |
| UNIT_OF_MEASURE | UomUnitOfMeasure | ✅ |
| UNIT_OF_MEASURE_ID | UomTLUnitOfMeasureId | — |
