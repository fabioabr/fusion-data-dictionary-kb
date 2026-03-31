---
id: DOC-OTHER-PVO-SetIdSetsPVO
doc_type: system-doc
title: "SetIdSetsPVO — PVO Cross-Module"
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
  - SetIdSetsPVO
  - setidsetspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SetIdSetsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Set Id Sets. Acessa as tabelas: FND_SETID_SETS.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.SetIdSetsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets|FND_SETID_SETS]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets|FND_SETID_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | SetCode | SET_CODE | — | ✅ |
| 9 | SetId | SET_ID | 🔑 | ✅ |
| 10 | SetName | SET_NAME | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
