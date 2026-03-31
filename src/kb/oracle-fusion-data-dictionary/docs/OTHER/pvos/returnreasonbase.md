---
id: DOC-OTHER-PVO-ReturnReasonBase
doc_type: system-doc
title: "ReturnReasonBase — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ReturnReasonBase
  - returnreasonbase
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReturnReasonBase

## 📌 Visão Geral

View Object para extração BICC de dados de Return Reason Base. Acessa as tabelas: MSC_SR_LOOKUP_VALUES_B.

**Caminho:** `FscmTopModelAM.DooTopAM.ReturnReasonBase`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 7 | 64% |

---

## 🔗 Tabelas Relacionadas

- [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]] — 11 atributos (2 PKs, 7 BICC)

---

## ⚙️ Atributos

### [[msc_sr_lookup_values_b|MSC_SR_LOOKUP_VALUES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 4 | EndDateActive | END_DATE_ACTIVE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LookupCode | LOOKUP_CODE | 🔑 | ✅ |
| 9 | LookupType | LOOKUP_TYPE | 🔑 | ✅ |
| 10 | RefreshNumber | REFRESH_NUMBER | — | — |
| 11 | StartDateActive | START_DATE_ACTIVE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
