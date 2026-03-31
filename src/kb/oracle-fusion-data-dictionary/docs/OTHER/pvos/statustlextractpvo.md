---
id: DOC-OTHER-PVO-StatusTLExtractPVO
doc_type: system-doc
title: "StatusTLExtractPVO — PVO Cross-Module"
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
  - StatusTLExtractPVO
  - statustlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# StatusTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Status TLExtract. Acessa as tabelas: DOO_STATUSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.StatusTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_statuses_tl|DOO_STATUSES_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[doo_statuses_tl|DOO_STATUSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DisplayName | DISPLAY_NAME | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | SourceLang | SOURCE_LANG | — | ✅ |
| 10 | StatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
