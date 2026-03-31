---
id: DOC-OTHER-PVO-GenealogyObjectPVO
doc_type: system-doc
title: "GenealogyObjectPVO — PVO Cross-Module"
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
  - GenealogyObjectPVO
  - genealogyobjectpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GenealogyObjectPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Genealogy Object. Acessa as tabelas: CSE_GENEALOGY_OBJECTS.

**Caminho:** `FscmTopModelAM.ProductGenealogyAM.GenealogyObjectPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[cse_genealogy_objects|CSE_GENEALOGY_OBJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | GenObjectId | GEN_OBJECT_ID | 🔑 | ✅ |
| 4 | ItemId | ITEM_ID | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | LotNumber | LOT_NUMBER | — | ✅ |
| 9 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 10 | OriginationDate | ORIGINATION_DATE | — | ✅ |
| 11 | OriginationDocumentNumber | ORIGINATION_DOCUMENT_NUMBER | — | ✅ |
| 12 | OriginationDocumentType | ORIGINATION_DOCUMENT_TYPE | — | ✅ |
| 13 | OriginationQuantity | ORIGINATION_QUANTITY | — | ✅ |
| 14 | SerialNumber | SERIAL_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
