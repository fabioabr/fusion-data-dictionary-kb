---
id: DOC-PO-PVO-InitiativeSupplierExtractPVO
doc_type: system-doc
title: "InitiativeSupplierExtractPVO — PVO Purchasing"
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
  - InitiativeSupplierExtractPVO
  - initiativesupplierextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativeSupplierExtractPVO

## 📌 Visão Geral

Extrai os fornecedores vinculados a iniciativas de qualificação para carga BICC. Alimenta análises de cobertura e taxa de conclusão das campanhas de homologação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.InitiativeSupplierExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_initiative_suppliers|POQ_INITIATIVE_SUPPLIERS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[poq_initiative_suppliers|POQ_INITIATIVE_SUPPLIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | InitSupplierId | INIT_SUPPLIER_ID | 🔑 | ✅ |
| 4 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 5 | InternalResponderId | INTERNAL_RESPONDER_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | SendIntQnnaireFlag | SEND_INT_QNNAIRE_FLAG | — | ✅ |
| 11 | SendSuppQnnaireFlag | SEND_SUPP_QNNAIRE_FLAG | — | ✅ |
| 12 | SuppContactPartyId | SUPP_CONTACT_PARTY_ID | — | ✅ |
| 13 | SupplierId | SUPPLIER_ID | — | ✅ |
| 14 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
