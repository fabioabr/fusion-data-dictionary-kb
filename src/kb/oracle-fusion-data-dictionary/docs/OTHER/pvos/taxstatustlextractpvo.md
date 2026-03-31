---
id: DOC-OTHER-PVO-TaxStatusTLExtractPVO
doc_type: system-doc
title: "TaxStatusTLExtractPVO — PVO Cross-Module"
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
  - TaxStatusTLExtractPVO
  - taxstatustlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxStatusTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Status TLExtract. Acessa as tabelas: ZX_STATUS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxStatusTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_status_tl|ZX_STATUS_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[zx_status_tl|ZX_STATUS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxStatusTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaxStatusTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaxStatusTLLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | TaxStatusTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxStatusTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxStatusTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxStatusTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxStatusTLTaxStatusId | TAX_STATUS_ID | 🔑 | ✅ |
| 9 | TaxStatusTLTaxStatusName | TAX_STATUS_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
