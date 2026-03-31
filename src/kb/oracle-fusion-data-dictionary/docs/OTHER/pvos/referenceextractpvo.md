---
id: DOC-OTHER-PVO-ReferenceExtractPVO
doc_type: system-doc
title: "ReferenceExtractPVO — PVO Cross-Module"
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
  - ReferenceExtractPVO
  - referenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReferenceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Reference Extract. Acessa as tabelas: GMS_REFERENCES_B, GMS_REFERENCES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.ReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_references_b|GMS_REFERENCES_B]] — 9 atributos (1 PKs, 9 BICC)
- [[gms_references_tl|GMS_REFERENCES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[gms_references_b|GMS_REFERENCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceBaseCreatedBy | CREATED_BY | — | ✅ |
| 2 | ReferenceBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | ReferenceBaseEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 4 | ReferenceBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ReferenceBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ReferenceBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ReferenceBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ReferenceBaseReferenceId | REFERENCE_ID | 🔑 | ✅ |
| 9 | ReferenceBaseStartDateActive | START_DATE_ACTIVE | — | ✅ |

### [[gms_references_tl|GMS_REFERENCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ReferenceTransLangCreatedBy | CREATED_BY | — | ✅ |
| 2 | ReferenceTransLangCreationDate | CREATION_DATE | — | ✅ |
| 3 | ReferenceTransLangDescription | DESCRIPTION | — | ✅ |
| 4 | ReferenceTransLangLanguage | LANGUAGE | — | ✅ |
| 5 | ReferenceTransLangLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ReferenceTransLangLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ReferenceTransLangLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ReferenceTransLangObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | ReferenceTransLangReferenceId | REFERENCE_ID | — | ✅ |
| 10 | ReferenceTransLangReferenceName | REFERENCE_NAME | — | ✅ |
| 11 | ReferenceTransLangSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
