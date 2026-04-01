---
id: DOC-OTHER-PVO-ExternalIdentifierPVO
doc_type: system-doc
title: "ExternalIdentifierPVO — PVO Cross-Module"
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
  - ExternalIdentifierPVO
  - externalidentifierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ExternalIdentifierPVO

## 📌 Visão Geral

View Object para extração BICC de dados de External Identifier. Acessa as tabelas: PER_EXT_APP_IDENTIFIERS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.PersonAM.ExternalIdentifierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 13 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[per_ext_app_identifiers|PER_EXT_APP_IDENTIFIERS]] — 16 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[per_ext_app_identifiers|PER_EXT_APP_IDENTIFIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | ✅ |
| 2 | Comments | COMMENTS | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DateFrom | DATE_FROM | — | ✅ |
| 6 | DateTo | DATE_TO | — | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | — |
| 8 | ExtIdentifierId | EXT_IDENTIFIER_ID | 🔑 | ✅ |
| 9 | ExtIdentifierNumber | EXT_IDENTIFIER_NUMBER | — | ✅ |
| 10 | ExtIdentifierSeq | EXT_IDENTIFIER_SEQ | — | ✅ |
| 11 | ExtIdentifierType | EXT_IDENTIFIER_TYPE | — | ✅ |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PersonId | PERSON_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
