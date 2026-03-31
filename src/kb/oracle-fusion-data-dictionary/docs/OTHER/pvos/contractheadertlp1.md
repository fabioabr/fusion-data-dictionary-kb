---
id: DOC-OTHER-PVO-ContractHeaderTLP1
doc_type: system-doc
title: "ContractHeaderTLP1 — PVO Cross-Module"
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
  - ContractHeaderTLP1
  - contractheadertlp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractHeaderTLP1

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Header TLP1. Acessa as tabelas: OKC_K_HEADERS_TL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractHeaderTLP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 11 | 79% |

---

## 🔗 Tabelas Relacionadas

- [[okc_k_headers_tl|OKC_K_HEADERS_TL]] — 14 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[okc_k_headers_tl|OKC_K_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Cognomen | COGNOMEN | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | — |
| 5 | Id | ID | 🔑 | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ShortDescription | SHORT_DESCRIPTION | — | ✅ |
| 13 | SourceLang | SOURCE_LANG | — | ✅ |
| 14 | VersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
