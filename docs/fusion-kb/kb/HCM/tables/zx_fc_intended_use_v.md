---
id: DOC-HCM-884
doc_type: system-doc
title: "ZX_FC_INTENDED_USE_V — (título a preencher)"
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
  - ZX_FC_INTENDED_USE_V
  - zx_fc_intended_use_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_INTENDED_USE_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_ID | — | — | — | — | — | — |
| 2 | CODE | — | — | — | — | — | — |
| 3 | COUNTRY_CODE | — | — | — | — | — | — |
| 4 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 5 | EFFECTIVE_TO | — | — | — | — | — | — |
| 6 | NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseLineIntendedClassificationId | — |
| NAME | LineIntendedUseLineIntendedUseName | — |

### [[fdinterfaceexceptionsp1|FDInterfaceExceptionsP1]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName | — |

### [[fiscaldocholdsp|FiscalDocHoldsP]] (OTHER · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName | ✅ |

### [[fiscaldocumentchargeassocp|FiscalDocumentChargeAssocP]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode1 | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName3 | — |

### [[fiscaldocumentlinesp|FiscalDocumentLinesP]] (OTHER · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName | ✅ |

### [[fiscaldocumentrcvchargeallocsp|FiscalDocumentRcvChargeAllocsP]] (OTHER · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode1 | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName1 | ✅ |

### [[fiscaldocumentschedulesp|FiscalDocumentSchedulesP]] (OTHER · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode1 | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName2 | ✅ |

### [[interfacefiscaldocumentp1|InterfaceFiscalDocumentP1]] (OTHER · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUsePEOClassificationId | — |
| CODE | LineIntendedUsePEOCode | — |
| COUNTRY_CODE | LineIntendedUsePEOCountryCode | — |
| EFFECTIVE_FROM | LineIntendedUsePEOEffectiveFrom | — |
| EFFECTIVE_TO | LineIntendedUsePEOEffectiveTo | — |
| NAME | LineIntendedUsePEOName | ✅ |

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | ✅ |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseClassificationId | — |
| NAME | LineIntendedUseName | ✅ |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseClassificationId | — |
| NAME | LineIntendedUseName | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseClassificationId | — |
| NAME | LineIntendedUseName | ✅ |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseLineIntendedClassificationId | — |
| NAME | LineIntendedUseLineIntendedUseName | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LineIntendedUseLineIntendedClassificationId | — |
| NAME | LineIntendedUseLineIntendedUseName | — |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | ✅ |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_ID | LnIntndUseClassificationId | — |
| CODE | LnIntndUseCode | — |
| COUNTRY_CODE | LnIntndUseCountryCode | — |
| NAME | LnIntndUseName | ✅ |
