---
id: DOC-OTHER-PVO-ImportBatchChange
doc_type: system-doc
title: "ImportBatchChange — PVO Cross-Module"
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
  - ImportBatchChange
  - importbatchchange
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ImportBatchChange

## 📌 Visão Geral

View Object para extração BICC de dados de Import Batch Change. Acessa as tabelas: EGI_IMPORT_BATCH_CHANGES.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.ImportBatchChange`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 4 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[egi_import_batch_changes|EGI_IMPORT_BATCH_CHANGES]] — 8 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[egi_import_batch_changes|EGI_IMPORT_BATCH_CHANGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BatchId | BATCH_ID | 🔑 | ✅ |
| 2 | ChangeId | CHANGE_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
