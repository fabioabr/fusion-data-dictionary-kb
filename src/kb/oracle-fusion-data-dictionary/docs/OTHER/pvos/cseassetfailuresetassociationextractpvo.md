---
id: DOC-OTHER-PVO-CseAssetFailureSetAssociationExtractPVO
doc_type: system-doc
title: "CseAssetFailureSetAssociationExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureSetAssociationExtractPVO
  - cseassetfailuresetassociationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureSetAssociationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Set Association Extract. Acessa as tabelas: CSE_FAILURE_SET_ASSOCIATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureSetAssociationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_set_associations|CSE_FAILURE_SET_ASSOCIATIONS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[cse_failure_set_associations|CSE_FAILURE_SET_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CaptureRequiredFlag | CAPTURE_REQUIRED_FLAG | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | DefaultFlag | DEFAULT_FLAG | — | ✅ |
| 6 | FailureSetId | FAILURE_SET_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectId | OBJECT_ID | — | ✅ |
| 11 | ObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | SetAssociationId | SET_ASSOCIATION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
