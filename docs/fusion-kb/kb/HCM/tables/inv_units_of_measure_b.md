---
id: DOC-HCM-527
doc_type: system-doc
title: "INV_UNITS_OF_MEASURE_B — (título a preencher)"
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
  - INV_UNITS_OF_MEASURE_B
  - inv_units_of_measure_b
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# INV_UNITS_OF_MEASURE_B

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ATTRIBUTE1 | — | — | — | — | — | — |
| 2 | ATTRIBUTE10 | — | — | — | — | — | — |
| 3 | ATTRIBUTE11 | — | — | — | — | — | — |
| 4 | ATTRIBUTE12 | — | — | — | — | — | — |
| 5 | ATTRIBUTE13 | — | — | — | — | — | — |
| 6 | ATTRIBUTE14 | — | — | — | — | — | — |
| 7 | ATTRIBUTE15 | — | — | — | — | — | — |
| 8 | ATTRIBUTE2 | — | — | — | — | — | — |
| 9 | ATTRIBUTE3 | — | — | — | — | — | — |
| 10 | ATTRIBUTE4 | — | — | — | — | — | — |
| 11 | ATTRIBUTE5 | — | — | — | — | — | — |
| 12 | ATTRIBUTE6 | — | — | — | — | — | — |
| 13 | ATTRIBUTE7 | — | — | — | — | — | — |
| 14 | ATTRIBUTE8 | — | — | — | — | — | — |
| 15 | ATTRIBUTE9 | — | — | — | — | — | — |
| 16 | ATTRIBUTE_CATEGORY | — | — | — | — | — | — |
| 17 | BASE_UOM_FLAG | — | — | — | — | — | — |
| 18 | CREATED_BY | — | — | — | — | — | — |
| 19 | CREATION_DATE | — | — | — | — | — | — |
| 20 | DISABLE_DATE | — | — | — | — | — | — |
| 21 | JOB_DEFINITION_NAME | — | — | — | — | — | — |
| 22 | JOB_DEFINITION_PACKAGE | — | — | — | — | — | — |
| 23 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 24 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 25 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 26 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 27 | REQUEST_ID | — | — | — | — | — | — |
| 28 | STANDARD_PACK_FLAG | — | — | — | — | — | — |
| 29 | UNIT_OF_MEASURE_ID | — | — | — | — | — | — |
| 30 | UOM_CLASS | — | — | — | — | — | — |
| 31 | UOM_CODE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | ✅ |

### [[invunitsofmeasurepvo|InvUnitsOfMeasurePVO]] (OTHER · BICC: 14/30)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| BASE_UOM_FLAG | BaseUomFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DISABLE_DATE | DisableDate | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| REQUEST_ID | RequestId | ✅ |
| UNIT_OF_MEASURE_ID | UnitOfMeasureId | ✅ |
| UOM_CLASS | UomClass | ✅ |
| UOM_CODE | UomCode | ✅ |

### [[invuompvo|InvUomPVO]] (OTHER · BICC: 5/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_UOM_FLAG | InvUomBPEOBaseUomFlag | ✅ |
| CREATED_BY | InvUomBPEOCreatedBy | — |
| CREATION_DATE | InvUomBPEOCreationDate | — |
| DISABLE_DATE | InvUomBPEODisableDate | — |
| JOB_DEFINITION_NAME | InvUomBPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | InvUomBPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | InvUomBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | InvUomBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | InvUomBPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | InvUomBPEOObjectVersionNumber | — |
| REQUEST_ID | InvUomBPEORequestId | — |
| STANDARD_PACK_FLAG | InvUomBPEOStandardPackFlag | — |
| UNIT_OF_MEASURE_ID | UnitOfMeasureId | ✅ |
| UOM_CLASS | InvUomBPEOUomClass | ✅ |
| UOM_CODE | InvUomBPEOUomCode | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| OBJECT_VERSION_NUMBER | UomObjectVersionNumber2 | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| OBJECT_VERSION_NUMBER | UomObjectVersionNumber2 | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| JOB_DEFINITION_NAME | UomJobDefinitionName | — |
| UNIT_OF_MEASURE_ID | UomUnitOfMeasureId | — |
| UOM_CODE | UomUomCode | — |
