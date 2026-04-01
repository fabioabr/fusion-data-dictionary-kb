---
id: DOC-AP-PVO-TaxJurisdictionTranslationPVO
doc_type: system-doc
title: "TaxJurisdictionTranslationPVO — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TaxJurisdictionTranslationPVO
  - taxjurisdictiontranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TaxJurisdictionTranslationPVO

## 📌 Visão Geral

Extrai as traduções dos nomes de jurisdições fiscais para diferentes idiomas. Necessário para operações internacionais onde jurisdições tributárias precisam ser apresentadas no idioma local do usuário.

**Caminho:** `FscmTopModelAM.FinApInvTransactionsAM.TaxJurisdictionTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 2 | 4 | 44% |

---

## 🔗 Tabelas Relacionadas

- [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]] — 9 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[zx_jurisdictions_tl|ZX_JURISDICTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | TaxJurisdictionId | TAX_JURISDICTION_ID | 🔑 | ✅ |
| 3 | TaxJurisdictionTLPEOCreatedBy | CREATED_BY | — | — |
| 4 | TaxJurisdictionTLPEOCreationDate | CREATION_DATE | — | — |
| 5 | TaxJurisdictionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | TaxJurisdictionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | TaxJurisdictionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | TaxJurisdictionTLPEOSourceLang | SOURCE_LANG | — | — |
| 9 | TaxJurisdictionTLPEOTaxJurisdictionName | TAX_JURISDICTION_NAME | — | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
