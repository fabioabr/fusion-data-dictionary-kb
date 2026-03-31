---
id: DOC-PO-PVO-SupplierRelationshipPVO
doc_type: system-doc
title: "SupplierRelationshipPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - SupplierRelationshipPVO
  - supplierrelationshippvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierRelationshipPVO

## 📌 Visão Geral

Extrai os tipos de relacionamento entre fornecedores e a organização (spend authorized, supplier, prospective). Permite classificação e segmentação da base por natureza do relacionamento.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierRelationshipPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 2 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poz_supp_relationship_vl|POZ_SUPP_RELATIONSHIP_VL]] — 8 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[poz_supp_relationship_vl|POZ_SUPP_RELATIONSHIP_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 3 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PartyId | PARTY_ID | 🔑 | ✅ |
| 5 | PartyUsageCode | PARTY_USAGE_CODE | 🔑 | ✅ |
| 6 | PartyUsageName | PARTY_USAGE_NAME | — | ✅ |
| 7 | PartyUsageType | PARTY_USAGE_TYPE | — | ✅ |
| 8 | StatusFlag | STATUS_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
