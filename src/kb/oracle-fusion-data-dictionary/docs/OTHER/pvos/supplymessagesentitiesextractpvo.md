---
id: DOC-OTHER-PVO-SupplyMessagesEntitiesExtractPVO
doc_type: system-doc
title: "SupplyMessagesEntitiesExtractPVO — PVO Cross-Module"
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
  - SupplyMessagesEntitiesExtractPVO
  - supplymessagesentitiesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplyMessagesEntitiesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Supply Messages Entities Extract. Acessa as tabelas: DOS_MESSAGE_ENTITIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DosBiccExtractAM.SupplyMessagesEntitiesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[dos_message_entities|DOS_MESSAGE_ENTITIES]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[dos_message_entities|DOS_MESSAGE_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DosMessageEntitiesPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | DosMessageEntitiesPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | DosMessageEntitiesPEOEntityId | ENTITY_ID | — | ✅ |
| 4 | DosMessageEntitiesPEOEntityType | ENTITY_TYPE | — | ✅ |
| 5 | DosMessageEntitiesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | DosMessageEntitiesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | DosMessageEntitiesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | DosMessageEntitiesPEOMessageEntityId | MESSAGE_ENTITY_ID | 🔑 | ✅ |
| 9 | DosMessageEntitiesPEOMessageId | MESSAGE_ID | — | ✅ |
| 10 | DosMessageEntitiesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
