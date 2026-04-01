---
id: DOC-HCM-125
doc_type: system-doc
title: "FND_DF_CONTEXTS_VL — (título a preencher)"
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
  - FND_DF_CONTEXTS_VL
  - fnd_df_contexts_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DF_CONTEXTS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | APPLICATION_ID | — | — | — | — | — | — |
| 2 | CONTEXT_CODE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | DESCRIPTIVE_FLEXFIELD_CODE | — | — | — | — | — | — |
| 5 | NAME | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[flex_bi_allpayrollsddf_vi|FLEX_BI_AllPayrollsDDF_VI]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KEY_FLEX_CONTEXT_0 | — |
| CONTEXT_CODE | KEY_FLEX_CONTEXT_2 | — |
| DESCRIPTION | DESC_FLEX_CONTEXT_ | — |
| DESCRIPTIVE_FLEXFIELD_CODE | KEY_FLEX_CONTEXT_1 | — |
| NAME | NAME_FLEX_CONTEXT_ | — |

### [[flex_bi_passportdff_vi|FLEX_BI_PassportDFF_VI]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| APPLICATION_ID | KEY_FLEX_CONTEXT_0 | — |
| CONTEXT_CODE | KEY_FLEX_CONTEXT_2 | — |
| DESCRIPTION | DESC_FLEX_CONTEXT_ | — |
| DESCRIPTIVE_FLEXFIELD_CODE | KEY_FLEX_CONTEXT_1 | — |
| NAME | NAME_FLEX_CONTEXT_ | — |
