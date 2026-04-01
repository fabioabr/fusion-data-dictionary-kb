---
id: DOC-OTHER-PVO-GenealogyObjectExtractPVO
doc_type: system-doc
title: "GenealogyObjectExtractPVO — PVO Cross-Module"
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
  - GenealogyObjectExtractPVO
  - genealogyobjectextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyObjectExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Object Extract. Acessa as tabelas: CSE_GENEALOGY_OBJECTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.GenealogyObjectExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AnalyticsSyncFlag | ANALYTICS_SYNC_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | GenObjectId | GEN_OBJECT_ID | 🔑 | ✅ |
| 5 | ItemId | ITEM_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | LotNumber | LOT_NUMBER | — | ✅ |
| 10 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 12 | OriginationDocumentNumber | ORIGINATION_DOCUMENT_NUMBER | — | ✅ |
| 13 | OriginationDocumentType | ORIGINATION_DOCUMENT_TYPE | — | ✅ |
| 14 | OriginationQuantity | ORIGINATION_QUANTITY | — | ✅ |
| 15 | SerialNumber | SERIAL_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
