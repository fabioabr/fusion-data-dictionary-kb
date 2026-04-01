---
id: DOC-OTHER-PVO-PaymentTermTLExtractPVO
doc_type: system-doc
title: "PaymentTermTLExtractPVO — PVO Cross-Module"
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
  - PaymentTermTLExtractPVO
  - paymenttermtlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PaymentTermTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Payment Term TLExtract. Acessa as tabelas: RA_TERMS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.PaymentTermTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ra_terms_tl|RA_TERMS_TL]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ra_terms_tl|RA_TERMS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaTermTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | RaTermTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | RaTermTLDescription | DESCRIPTION | — | ✅ |
| 4 | RaTermTLLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | RaTermTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RaTermTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RaTermTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RaTermTLName | NAME | — | ✅ |
| 9 | RaTermTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RaTermTLSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | RaTermTLSetId | SET_ID | — | ✅ |
| 12 | RaTermTLSourceLang | SOURCE_LANG | — | ✅ |
| 13 | RaTermTLTermId | TERM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
