---
id: DOC-OTHER-PVO-LotSerialExtractPVO
doc_type: system-doc
title: "LotSerialExtractPVO — PVO Cross-Module"
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
  - LotSerialExtractPVO
  - lotserialextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LotSerialExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Lot Serial Extract. Acessa as tabelas: DOO_LOT_SERIAL_NUMBERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.LotSerialExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_lot_serial_numbers|DOO_LOT_SERIAL_NUMBERS]] — 20 atributos (1 PKs, 20 BICC)

---

## ⚙️ Atributos

### [[doo_lot_serial_numbers|DOO_LOT_SERIAL_NUMBERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | LotSerialCreatedBy | CREATED_BY | — | ✅ |
| 2 | LotSerialCreationDate | CREATION_DATE | — | ✅ |
| 3 | LotSerialDeltaType | DELTA_TYPE | — | ✅ |
| 4 | LotSerialFulfillLineId | FULFILL_LINE_ID | — | ✅ |
| 5 | LotSerialId | LOT_SERIAL_ID | 🔑 | ✅ |
| 6 | LotSerialItemRevisionNumber | ITEM_REVISION_NUMBER | — | ✅ |
| 7 | LotSerialItemSerialNumberFrom | ITEM_SERIAL_NUMBER_FROM | — | ✅ |
| 8 | LotSerialItemSerialNumberTo | ITEM_SERIAL_NUMBER_TO | — | ✅ |
| 9 | LotSerialLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LotSerialLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LotSerialLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | LotSerialLineId | LINE_ID | — | ✅ |
| 13 | LotSerialLocatorId | LOCATOR_ID | — | ✅ |
| 14 | LotSerialLotNumber | LOT_NUMBER | — | ✅ |
| 15 | LotSerialModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 16 | LotSerialObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | LotSerialOrigSysLotserialRef | ORIG_SYS_LOTSERIAL_REF | — | ✅ |
| 18 | LotSerialQuantity | QUANTITY | — | ✅ |
| 19 | LotSerialReferenceLotSerialId | REFERENCE_LOT_SERIAL_ID | — | ✅ |
| 20 | LotSerialSecondaryQuantity | SECONDARY_QUANTITY | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
