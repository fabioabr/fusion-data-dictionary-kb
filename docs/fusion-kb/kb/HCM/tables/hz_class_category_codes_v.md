---
id: DOC-HCM-484
doc_type: system-doc
title: "HZ_CLASS_CATEGORY_CODES_V — (título a preencher)"
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
  - HZ_CLASS_CATEGORY_CODES_V
  - hz_class_category_codes_v
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_CLASS_CATEGORY_CODES_V

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CLASS_CATEGORY | — | — | — | — | — | — |
| 2 | CLASS_CODE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | MEANING | — | — | — | — | — | — |
| 7 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 8 | VIEW_APPLICATION_ID | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[sitetaxclassification|SiteTaxClassification]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASS_CATEGORY | ClassCatCodeClassCategory | — |
| CLASS_CODE | ClassCatCodeClassCode | — |
| DESCRIPTION | ClassCatCodeDescription | — |
| END_DATE_ACTIVE | ClassCatCodeEndDateActive | — |
| LAST_UPDATED_BY | ClassCatCodeLastUpdatedBy | — |
| MEANING | ClassCatCodeMeaning | ✅ |
| START_DATE_ACTIVE | ClassCatCodeStartDateActive | — |
| VIEW_APPLICATION_ID | ClassCatCodeViewApplicationId | — |

### [[taxclassification|TaxClassification]] (AR · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CLASS_CATEGORY | ClassCatCodeClassCategory | — |
| CLASS_CODE | ClassCatCodeClassCode | — |
| DESCRIPTION | ClassCatCodeDescription | — |
| END_DATE_ACTIVE | ClassCatCodeEndDateActive | — |
| LAST_UPDATED_BY | ClassCatCodeLastUpdatedBy | — |
| MEANING | ClassCatCodeMeaning | ✅ |
| START_DATE_ACTIVE | ClassCatCodeStartDateActive | — |
| VIEW_APPLICATION_ID | ClassCatCodeViewApplicationId | — |
