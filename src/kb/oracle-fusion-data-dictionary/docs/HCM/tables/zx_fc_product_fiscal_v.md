---
id: DOC-HCM-886
doc_type: system-doc
title: "ZX_FC_PRODUCT_FISCAL_V — (título a preencher)"
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
  - ZX_FC_PRODUCT_FISCAL_V
  - zx_fc_product_fiscal_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_PRODUCT_FISCAL_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CATEGORY_ID | — | — | — | — | — | — |
| 2 | CATEGORY_SET_ID | — | — | — | — | — | — |
| 3 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 4 | CLASSIFICATION_NAME | — | — | — | — | — | — |
| 5 | COUNTRY_CODE | — | — | — | — | — | — |
| 6 | EFFECTIVE_TO | — | — | — | — | — | — |
| 7 | STRUCTURE_ID | — | — | — | — | — | — |
| 8 | STRUCTURE_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[fdinterfaceexceptionsp1|FDInterfaceExceptionsP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsPE1CategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsPE1CategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsPE1ClassificationCode1 | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsPE1ClassificationName1 | — |
| COUNTRY_CODE | ProductFiscClassificationsPE1CountryCode2 | — |
| EFFECTIVE_TO | ProductFiscClassificationsPE1EffectiveTo2 | — |
| STRUCTURE_ID | ProductFiscClassificationsPE1StructureId | — |
| STRUCTURE_NAME | ProductFiscClassificationsPE1StructureName | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificatnsPEOCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificatnsPEOCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificatnsPEOClassificationCode2 | — |
| CLASSIFICATION_NAME | ProductFiscClassificatnsPEOClassificationName2 | ✅ |
| COUNTRY_CODE | ProductFiscClassificatnsPEOCountryCode3 | — |
| EFFECTIVE_TO | ProductFiscClassificatnsPEOEffectiveTo3 | — |
| STRUCTURE_ID | ProductFiscClassificatnsPEOStructureId | — |
| STRUCTURE_NAME | ProductFiscClassificatnsPEOStructureName | — |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificatnsPEOCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificatnsPEOCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificatnsPEOClassificationCode2 | — |
| CLASSIFICATION_NAME | ProductFiscClassificatnsPEOClassificationName2 | — |
| COUNTRY_CODE | ProductFiscClassificatnsPEOCountryCode4 | — |
| EFFECTIVE_TO | ProductFiscClassificatnsPEOEffectiveTo3 | — |
| STRUCTURE_ID | ProductFiscClassificatnsPEOStructureId | — |
| STRUCTURE_NAME | ProductFiscClassificatnsPEOStructureName | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificatnsPEOCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificatnsPEOCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificatnsPEOClassificationCode2 | — |
| CLASSIFICATION_NAME | ProductFiscClassificatnsPEOClassificationName2 | ✅ |
| COUNTRY_CODE | ProductFiscClassificatnsPEOCountryCode3 | — |
| EFFECTIVE_TO | ProductFiscClassificatnsPEOEffectiveTo3 | — |
| STRUCTURE_ID | ProductFiscClassificatnsPEOStructureId | — |
| STRUCTURE_NAME | ProductFiscClassificatnsPEOStructureName | — |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsPE1CategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsPE1CategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsPE1ClassificationCode2 | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsPE1ClassificationName2 | ✅ |
| COUNTRY_CODE | ProductFiscClassificationsPE1CountryCode4 | — |
| EFFECTIVE_TO | ProductFiscClassificationsPE1EffectiveTo3 | — |
| STRUCTURE_ID | ProductFiscClassificationsPE1StructureId | — |
| STRUCTURE_NAME | ProductFiscClassificationsPE1StructureName | — |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsPE1CategoryId2 | — |
| CATEGORY_SET_ID | ProductFiscClassificationsPE1CategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsPE1ClassificationCode2 | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsPE1ClassificationName2 | ✅ |
| COUNTRY_CODE | ProductFiscClassificationsPE1CountryCode4 | — |
| EFFECTIVE_TO | ProductFiscClassificationsPE1EffectiveTo3 | — |
| STRUCTURE_ID | ProductFiscClassificationsPE1StructureId | — |
| STRUCTURE_NAME | ProductFiscClassificationsPE1StructureName | — |

### [[interfacefiscaldocumentp1|InterfaceFiscalDocumentP1]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsPE1CategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsPE1CategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsPE1ClassificationCode1 | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsPE1ClassificationName1 | ✅ |
| COUNTRY_CODE | ProductFiscClassificationsPE1CountryCode2 | — |
| EFFECTIVE_TO | ProductFiscClassificationsPE1EffectiveTo2 | — |
| STRUCTURE_ID | ProductFiscClassificationsPE1StructureId | — |
| STRUCTURE_NAME | ProductFiscClassificationsPE1StructureName | — |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | ✅ |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsClassificationCode | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsClassificationName | ✅ |
| COUNTRY_CODE | ProductFiscClassificationsCountryCode | — |
| STRUCTURE_ID | ProductFiscClassificationsStructureId | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsClassificationCode | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsClassificationName | — |
| COUNTRY_CODE | ProductFiscClassificationsCountryCode | — |
| STRUCTURE_ID | ProductFiscClassificationsStructureId | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProductFiscClassificationsCategoryId | — |
| CATEGORY_SET_ID | ProductFiscClassificationsCategorySetId | — |
| CLASSIFICATION_CODE | ProductFiscClassificationsClassificationCode | — |
| CLASSIFICATION_NAME | ProductFiscClassificationsClassificationName | ✅ |
| COUNTRY_CODE | ProductFiscClassificationsCountryCode | — |
| STRUCTURE_ID | ProductFiscClassificationsStructureId | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | — |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | — |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | — |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | ✅ |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CATEGORY_ID | ProdFiscClsCategoryId | — |
| CATEGORY_SET_ID | ProdFiscClsCategorySetId | — |
| CLASSIFICATION_CODE | ProdFiscClsClassificationCode | — |
| CLASSIFICATION_NAME | ProdFiscClsClassificationName | ✅ |
| COUNTRY_CODE | ProdFiscClsCountryCode | — |
| EFFECTIVE_TO | ProdFiscClsEffectiveTo | — |
| STRUCTURE_ID | ProdFiscClsStructureId | — |
| STRUCTURE_NAME | ProdFiscClsStructureName | — |
