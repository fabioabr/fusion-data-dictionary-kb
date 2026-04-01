---
id: DOC-OTHER-PVO-TaxJurisdictionTLExtractPVO
doc_type: system-doc
title: "TaxJurisdictionTLExtractPVO — PVO Cross-Module"
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
  - TaxJurisdictionTLExtractPVO
  - taxjurisdictiontlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxJurisdictionTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Tax Jurisdiction TLExtract. Acessa as tabelas: ZX_JURISDICTIONS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ZxBiccExtractAM.TaxJurisdictionTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]] — 9 atributos (2 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | TaxJurisdictionTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | TaxJurisdictionTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | TaxJurisdictionTLLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | TaxJurisdictionTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | TaxJurisdictionTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | TaxJurisdictionTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | TaxJurisdictionTLSourceLang | SOURCE_LANG | — | ✅ |
| 8 | TaxJurisdictionTLTaxJurisdictionId | TAX_JURISDICTION_ID | 🔑 | ✅ |
| 9 | TaxJurisdictionTLTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
