---
id: DOC-HCM-889
doc_type: system-doc
title: "ZX_INPUT_CLASSIFICATIONS_V — (título a preencher)"
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
  - ZX_INPUT_CLASSIFICATIONS_V
  - zx_input_classifications_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_INPUT_CLASSIFICATIONS_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LOOKUP_CODE | — | — | — | — | — | — |
| 2 | MEANING | — | — | — | — | — | — |
| 3 | SET_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LOOKUP_CODE | InputTaxClassificationsLookupCode | — |
| MEANING | InputTaxClassificationsMeaning | — |
| SET_ID | InputTaxClassificationsSetId | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LOOKUP_CODE | InputTaxClassificationsLookupCode | — |
| MEANING | InputTaxClassificationsMeaning | — |
| SET_ID | InputTaxClassificationsSetId | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LOOKUP_CODE | InputTaxClassificationsLookupCode | — |
| MEANING | InputTaxClassificationsMeaning | — |
| SET_ID | InputTaxClassificationsSetId | — |
