---
id: DOC-OTHER-PVO-ItemRevision
doc_type: system-doc
title: "ItemRevision — PVO Cross-Module"
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
  - ItemRevision
  - itemrevision
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ItemRevision

## 📌 Visão Geral

View Object para extração BICC de dados de Item Revision. Acessa as tabelas: EGP_ITEM_REVISIONS_B_V, EGP_ITEM_REVISIONS_TL_V.

**Caminho:** `FscmTopModelAM.EgpItemsPublicModelAM.ItemRevision`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 33 | 2 | 2 | 15 | 45% |

---

## 🔗 Tabelas Relacionadas

- [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]] — 23 atributos (1 PKs, 12 BICC)
- [[egp_item_revisions_tl_v|EGP_ITEM_REVISIONS_TL_V]] — 10 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[egp_item_revisions_b_v|EGP_ITEM_REVISIONS_B_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRevisionBasePEOChangeLineId | CHANGE_LINE_ID | — | — |
| 2 | ItemRevisionBasePEOCreatedBy | CREATED_BY | — | — |
| 3 | ItemRevisionBasePEOCreationDate | CREATION_DATE | — | — |
| 4 | ItemRevisionBasePEOCurrentPhaseId | CURRENT_PHASE_ID | — | — |
| 5 | ItemRevisionBasePEODescription | DESCRIPTION | — | ✅ |
| 6 | ItemRevisionBasePEOEcnInitiationDate | ECN_INITIATION_DATE | — | ✅ |
| 7 | ItemRevisionBasePEOEffectivityDate | EFFECTIVITY_DATE | — | ✅ |
| 8 | ItemRevisionBasePEOEndEffectivityDate | END_EFFECTIVITY_DATE | — | ✅ |
| 9 | ItemRevisionBasePEOImplementationDate | IMPLEMENTATION_DATE | — | ✅ |
| 10 | ItemRevisionBasePEOInventoryItemId | INVENTORY_ITEM_ID | — | — |
| 11 | ItemRevisionBasePEOJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 12 | ItemRevisionBasePEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 13 | ItemRevisionBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | ItemRevisionBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ItemRevisionBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ItemRevisionBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 17 | ItemRevisionBasePEOOrganizationId | ORGANIZATION_ID | — | — |
| 18 | ItemRevisionBasePEOProgramAppName | PROGRAM_APP_NAME | — | — |
| 19 | ItemRevisionBasePEOProgramName | PROGRAM_NAME | — | — |
| 20 | ItemRevisionBasePEORequestId | REQUEST_ID | — | — |
| 21 | ItemRevisionBasePEORevision | REVISION | — | ✅ |
| 22 | ItemRevisionBasePEORevisionReason | REVISION_REASON | — | ✅ |
| 23 | RevisionId | REVISION_ID | 🔑 | ✅ |

### [[egp_item_revisions_tl_v|EGP_ITEM_REVISIONS_TL_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ItemRevisionTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | ItemRevisionTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | ItemRevisionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ItemRevisionTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | ItemRevisionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ItemRevisionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ItemRevisionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ItemRevisionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | ItemRevisionTranslationPEORevisionId | REVISION_ID | — | — |
| 10 | ItemRevisionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
