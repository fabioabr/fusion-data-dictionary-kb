---
id: DOC-HCM-652
doc_type: system-doc
title: "JTF_RS_REP_MANAGERS — (título a preencher)"
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
  - JTF_RS_REP_MANAGERS
  - jtf_rs_rep_managers
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# JTF_RS_REP_MANAGERS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DENORM_MGR_ID | — | — | — | — | — | — |
| 2 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 3 | GROUP_ID | — | — | — | — | — | — |
| 4 | PARENT_RESOURCE_ID | — | — | — | — | — | — |
| 5 | START_DATE_ACTIVE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[resourcepartnerpvo|ResourcePartnerPVO]] (OTHER · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DENORM_MGR_ID | DenormMgrId | — |
| END_DATE_ACTIVE | RptgMgrEndDateActive | — |
| GROUP_ID | PrimaryOrg | ✅ |
| PARENT_RESOURCE_ID | ParentResourceId | — |
| START_DATE_ACTIVE | RptgMgrStartDateActive | — |
