---
id: DOC-OTHER-PVO-GrantsPersonnelKeywordPVO
doc_type: system-doc
title: "GrantsPersonnelKeywordPVO — PVO Cross-Module"
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
  - GrantsPersonnelKeywordPVO
  - grantspersonnelkeywordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GrantsPersonnelKeywordPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Grants Personnel Keyword. Acessa as tabelas: GMS_PERSONNEL_KEYWORDS.

**Caminho:** `FscmTopModelAM.GmsSetupAM.GrantsPersonnelKeywordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[gms_personnel_keywords|GMS_PERSONNEL_KEYWORDS]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[gms_personnel_keywords|GMS_PERSONNEL_KEYWORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GrantsPersonnelKeywordsPEOCreatedBy | CREATED_BY | — | — |
| 2 | GrantsPersonnelKeywordsPEOCreationDate | CREATION_DATE | — | — |
| 3 | GrantsPersonnelKeywordsPEOId | ID | 🔑 | ✅ |
| 4 | GrantsPersonnelKeywordsPEOKeywordId | KEYWORD_ID | — | ✅ |
| 5 | GrantsPersonnelKeywordsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | GrantsPersonnelKeywordsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | GrantsPersonnelKeywordsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | GrantsPersonnelKeywordsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | GrantsPersonnelKeywordsPEOPersonId | PERSON_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
