---
id: DOC-HCM-883
doc_type: system-doc
title: "ZX_FC_DOCUMENT_FISCAL_V — (título a preencher)"
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
  - ZX_FC_DOCUMENT_FISCAL_V
  - zx_fc_document_fiscal_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_FC_DOCUMENT_FISCAL_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 2 | CLASSIFICATION_ID | — | — | — | — | — | — |
| 3 | CLASSIFICATION_NAME | — | — | — | — | — | — |
| 4 | CONCAT_CLASSIF_CODE | — | — | — | — | — | — |
| 5 | CONCAT_CLASSIF_NAME | — | — | — | — | — | — |
| 6 | COUNTRY_CODE | — | — | — | — | — | — |
| 7 | EFFECTIVE_FROM | — | — | — | — | — | — |
| 8 | EFFECTIVE_TO | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[agreementheaderpvo|AgreementHeaderPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | — |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[agreementlinepvo|AgreementLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | — |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | — |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | — |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | ✅ |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | ✅ |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | — |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[standardheaderpvo|StandardHeaderPVO]] (PO · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | ✅ |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[standardlinepvo|StandardLinePVO]] (PO · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | ✅ |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | DocFisClassificationClassificationCode | — |
| CLASSIFICATION_ID | DocFisClassificationClassificationId | — |
| CLASSIFICATION_NAME | DocFisClassificationClassificationName | — |
| CONCAT_CLASSIF_CODE | DocFisClassificationConcatClassifCode | — |
| CONCAT_CLASSIF_NAME | DocFisClassificationConcatClassifName | ✅ |
| COUNTRY_CODE | DocFisClassificationCountryCode | — |
| EFFECTIVE_FROM | DocFisClassificationEffectiveFrom | — |
| EFFECTIVE_TO | DocFisClassificationEffectiveTo | — |
