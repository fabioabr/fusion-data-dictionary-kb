---
id: DOC-OTHER-PVO-HoldCodeTLExtractPVO
doc_type: system-doc
title: "HoldCodeTLExtractPVO — PVO Cross-Module"
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
  - HoldCodeTLExtractPVO
  - holdcodetlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# HoldCodeTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Hold Code TLExtract. Acessa as tabelas: DOO_HOLD_CODES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.HoldCodeTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_hold_codes_tl|DOO_HOLD_CODES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[doo_hold_codes_tl|DOO_HOLD_CODES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | HoldCodeId | HOLD_CODE_ID | 🔑 | ✅ |
| 4 | HoldDescription | HOLD_DESCRIPTION | — | ✅ |
| 5 | HoldName | HOLD_NAME | — | ✅ |
| 6 | Language | LANGUAGE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
