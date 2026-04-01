---
id: DOC-OTHER-PVO-ProcessStatusWH
doc_type: system-doc
title: "ProcessStatusWH — PVO Cross-Module"
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
  - ProcessStatusWH
  - processstatuswh
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessStatusWH

## 📌 Visão Geral

View Object para extração BICC de dados de Process Status WH. Acessa as tabelas: DOO_STATUSES_B.

**Caminho:** `FscmTopModelAM.DooTopAM.ProcessStatusWH`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 6 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[doo_statuses_b|DOO_STATUSES_B]] — 9 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[doo_statuses_b|DOO_STATUSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | SeededFlag | SEEDED_FLAG | — | — |
| 8 | StatusCode | STATUS_CODE | — | ✅ |
| 9 | StatusId | STATUS_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
