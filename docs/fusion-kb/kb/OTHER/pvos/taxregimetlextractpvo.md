---
id: DOC-OTHER-PVO-TaxRegimeTLExtractPVO
doc_type: system-doc
title: "TaxRegimeTLExtractPVO — PVO Cross-Module"
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
  - TaxRegimeTLExtractPVO
  - taxregimetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxRegimeTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Regime TLExtract. Acessa as tabelas: ZX_REGIMES_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxRegimeTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_regimes_tl|ZX_REGIMES_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[zx_regimes_tl|ZX_REGIMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxRegimeTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaxRegimeTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaxRegimeTLLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | TaxRegimeTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxRegimeTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxRegimeTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxRegimeTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxRegimeTLTaxRegimeId | TAX_REGIME_ID | 🔑 | ✅ |
| 9 | TaxRegimeTLTaxRegimeName | TAX_REGIME_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
