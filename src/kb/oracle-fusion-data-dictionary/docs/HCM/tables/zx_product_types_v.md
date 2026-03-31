---
id: DOC-HCM-897
doc_type: system-doc
title: "ZX_PRODUCT_TYPES_V — (título a preencher)"
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
  - ZX_PRODUCT_TYPES_V
  - zx_product_types_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_PRODUCT_TYPES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASSIFICATION_CODE | — | — | — | — | — | — |
| 2 | CLASSIFICATION_NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[linesalescreditpvo|LineSalesCreditPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | ✅ |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductTypesClassificationCode | — |
| CLASSIFICATION_NAME | ProductTypesClassificationName | ✅ |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductTypesClassificationCode | — |
| CLASSIFICATION_NAME | ProductTypesClassificationName | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProductTypesClassificationCode | — |
| CLASSIFICATION_NAME | ProductTypesClassificationName | ✅ |

### [[transactionhistorydistributionpvo|TransactionHistoryDistributionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | — |

### [[transactionhistorypvo|TransactionHistoryPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | — |

### [[transactionlinebillsreceivablepvo|TransactionLineBillsReceivablePVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | — |

### [[transactionlinedistributionpvo|TransactionLineDistributionPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | ✅ |

### [[transactionlinepvo|TransactionLinePVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASSIFICATION_CODE | ProdTypeClassificationCode | — |
| CLASSIFICATION_NAME | ProdTypeClassificationName | ✅ |
