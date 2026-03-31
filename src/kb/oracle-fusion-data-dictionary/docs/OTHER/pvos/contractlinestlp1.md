---
id: DOC-OTHER-PVO-ContractLinesTLP1
doc_type: system-doc
title: "ContractLinesTLP1 — PVO Cross-Module"
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
  - ContractLinesTLP1
  - contractlinestlp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractLinesTLP1

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Lines TLP1. Acessa as tabelas: OKC_K_LINES_TL.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractLinesTLP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 3 | 11 | 61% |

---

## 🔗 Tabelas Relacionadas

- [[okc_k_lines_tl|OKC_K_LINES_TL]] — 18 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[okc_k_lines_tl|OKC_K_LINES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Cognomen | COGNOMEN | — | — |
| 2 | Comments | COMMENTS | — | — |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Id | ID | 🔑 | ✅ |
| 6 | ItemDescription | ITEM_DESCRIPTION | — | ✅ |
| 7 | ItemName | ITEM_NAME | — | ✅ |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | LineDescription | LINE_DESCRIPTION | — | — |
| 13 | LineName | LINE_NAME | — | — |
| 14 | LineReference | LINE_REFERENCE | — | — |
| 15 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |
| 16 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 17 | SourceLang | SOURCE_LANG | — | ✅ |
| 18 | VersionType | VERSION_TYPE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
