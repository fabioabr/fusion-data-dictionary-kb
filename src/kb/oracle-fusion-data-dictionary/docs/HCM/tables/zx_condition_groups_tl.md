---
id: DOC-HCM-877
doc_type: system-doc
title: "ZX_CONDITION_GROUPS_TL — (título a preencher)"
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
  - ZX_CONDITION_GROUPS_TL
  - zx_condition_groups_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# ZX_CONDITION_GROUPS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CONDITION_GROUP_ID | — | — | — | — | — | — |
| 2 | CONDITION_GROUP_NAME | — | — | — | — | — | — |
| 3 | LANGUAGE | — | — | — | — | — | — |

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
| CONDITION_GROUP_ID | AwtTaxGroupLineTLConditionGroupId | — |
| CONDITION_GROUP_NAME | AwtTaxGroupLineConditionGroupName | ✅ |
| LANGUAGE | AwtTaxGroupLineTLLanguage | — |
