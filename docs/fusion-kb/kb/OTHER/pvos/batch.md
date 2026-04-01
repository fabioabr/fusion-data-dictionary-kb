---
id: DOC-OTHER-PVO-Batch
doc_type: system-doc
title: "Batch — PVO Cross-Module"
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
  - Batch
  - batch
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# Batch

## 📌 Visão Geral

View Object para extração BICC de dados de Batch. Acessa as tabelas: EGI_IMPORT_BATCHES_B.

**Caminho:** `FscmTopModelAM.EgiBatchesPublicModelAnalyticsAM.Batch`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 8 | 57% |

---

## 🔗 Tabelas Relacionadas

- [[egi_import_batches_b|EGI_IMPORT_BATCHES_B]] — 14 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[egi_import_batches_b|EGI_IMPORT_BATCHES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssigneeId | ASSIGNEE_ID | — | ✅ |
| 2 | BatchId | BATCH_ID | 🔑 | ✅ |
| 3 | BatchStatus | BATCH_STATUS | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | InternalFlag | INTERNAL_FLAG | — | — |
| 7 | LastImportRequestId | LAST_IMPORT_REQUEST_ID | — | — |
| 8 | LastMatchRequestId | LAST_MATCH_REQUEST_ID | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | OrganizationId | ORGANIZATION_ID | — | — |
| 14 | SourceSystemId | SOURCE_SYSTEM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
