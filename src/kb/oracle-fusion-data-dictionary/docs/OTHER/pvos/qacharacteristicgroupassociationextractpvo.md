---
id: DOC-OTHER-PVO-QaCharacteristicGroupAssociationExtractPVO
doc_type: system-doc
title: "QaCharacteristicGroupAssociationExtractPVO — PVO Cross-Module"
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
  - QaCharacteristicGroupAssociationExtractPVO
  - qacharacteristicgroupassociationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QaCharacteristicGroupAssociationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Qa Characteristic Group Association Extract. Acessa as tabelas: QA_CS_GROUP_ASSOCIATIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.QaCharacteristicGroupAssociationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_cs_group_associations|QA_CS_GROUP_ASSOCIATIONS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[qa_cs_group_associations|QA_CS_GROUP_ASSOCIATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QaCSGroupAssociationsPEOCharacteristicId | CHARACTERISTIC_ID | — | ✅ |
| 2 | QaCSGroupAssociationsPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QaCSGroupAssociationsPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QaCSGroupAssociationsPEOCsGroupAssociationId | CS_GROUP_ASSOCIATION_ID | 🔑 | ✅ |
| 5 | QaCSGroupAssociationsPEOCsGroupId | CS_GROUP_ID | — | ✅ |
| 6 | QaCSGroupAssociationsPEOEnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | QaCSGroupAssociationsPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 8 | QaCSGroupAssociationsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | QaCSGroupAssociationsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | QaCSGroupAssociationsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | QaCSGroupAssociationsPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
