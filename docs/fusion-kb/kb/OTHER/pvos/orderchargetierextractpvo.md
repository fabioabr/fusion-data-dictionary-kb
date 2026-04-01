---
id: DOC-OTHER-PVO-OrderChargeTierExtractPVO
doc_type: system-doc
title: "OrderChargeTierExtractPVO — PVO Cross-Module"
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
  - OrderChargeTierExtractPVO
  - orderchargetierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrderChargeTierExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Order Charge Tier Extract. Acessa as tabelas: DOO_ORDER_CHARGE_TIERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrderChargeTierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_order_charge_tiers|DOO_ORDER_CHARGE_TIERS]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[doo_order_charge_tiers|DOO_ORDER_CHARGE_TIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrderChargeTierAdjustmentAmount | ADJUSTMENT_AMOUNT | — | ✅ |
| 2 | OrderChargeTierAdjustmentBasisId | ADJUSTMENT_BASIS_ID | — | ✅ |
| 3 | OrderChargeTierAdjustmentTypeCode | ADJUSTMENT_TYPE_CODE | — | ✅ |
| 4 | OrderChargeTierApplicationMethodCode | APPLICATION_METHOD_CODE | — | ✅ |
| 5 | OrderChargeTierBlockSize | BLOCK_SIZE | — | ✅ |
| 6 | OrderChargeTierCreatedBy | CREATED_BY | — | ✅ |
| 7 | OrderChargeTierCreationDate | CREATION_DATE | — | ✅ |
| 8 | OrderChargeTierDeltaType | DELTA_TYPE | — | ✅ |
| 9 | OrderChargeTierId | ORDER_CHARGE_TIER_ID | 🔑 | ✅ |
| 10 | OrderChargeTierLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | OrderChargeTierLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | OrderChargeTierLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | OrderChargeTierModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 14 | OrderChargeTierObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | OrderChargeTierOrderChargeId | ORDER_CHARGE_ID | — | ✅ |
| 16 | OrderChargeTierPartialBlockAction | PARTIAL_BLOCK_ACTION | — | ✅ |
| 17 | OrderChargeTierReferenceOrderChargeTierId | REFERENCE_ORDER_CHARGE_TIER_ID | — | ✅ |
| 18 | OrderChargeTierSourceOrderChargeTierId | SOURCE_ORDER_CHARGE_TIER_ID | — | ✅ |
| 19 | OrderChargeTierTierFrom | TIER_FROM | — | ✅ |
| 20 | OrderChargeTierTierSequenceNumber | TIER_SEQUENCE_NUMBER | — | ✅ |
| 21 | OrderChargeTierTierTo | TIER_TO | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
