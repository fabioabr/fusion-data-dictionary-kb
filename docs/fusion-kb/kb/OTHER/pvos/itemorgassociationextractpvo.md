---
id: DOC-OTHER-PVO-ItemOrgAssociationExtractPVO
doc_type: system-doc
title: "ItemOrgAssociationExtractPVO — PVO Cross-Module"
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
  - ItemOrgAssociationExtractPVO
  - itemorgassociationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemOrgAssociationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Item Org Association Extract. Acessa as tabelas: EGP_ITEM_ORG_ASSOCIATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgpBiccExtractAM.ItemOrgAssociationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_org_associations|EGP_ITEM_ORG_ASSOCIATIONS]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[egp_item_org_associations|EGP_ITEM_ORG_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemOrgAssociationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ItemOrgAssociationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ItemOrgAssociationPEOInventoryItemId | INVENTORY_ITEM_ID | 🔑 | ✅ |
| 4 | ItemOrgAssociationPEOInventoryOrganizationId | INVENTORY_ORGANIZATION_ID | — | ✅ |
| 5 | ItemOrgAssociationPEOItemDefinitionOrgId | ITEM_DEFINITION_ORG_ID | — | ✅ |
| 6 | ItemOrgAssociationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | ItemOrgAssociationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | ItemOrgAssociationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ItemOrgAssociationPEOOrganizationId | ORGANIZATION_ID | 🔑 | ✅ |
| 10 | ItemOrgAssociationPEOPublicFlag | PUBLIC_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
