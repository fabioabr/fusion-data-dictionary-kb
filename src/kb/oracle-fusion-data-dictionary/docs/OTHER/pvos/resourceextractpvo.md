---
id: DOC-OTHER-PVO-ResourceExtractPVO
doc_type: system-doc
title: "ResourceExtractPVO — PVO Cross-Module"
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
  - ResourceExtractPVO
  - resourceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Extract. Acessa as tabelas: WIS_RESOURCES_B, WIS_RESOURCES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.ResourceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 68 | 2 | 3 | 68 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_resources_b|WIS_RESOURCES_B]] — 57 atributos (1 PKs, 57 BICC)
- [[wis_resources_tl|WIS_RESOURCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_resources_b|WIS_RESOURCES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttributeCategory | ATTRIBUTE_CATEGORY | — | ✅ |
| 2 | AttributeChar1 | ATTRIBUTE_CHAR1 | — | ✅ |
| 3 | AttributeChar10 | ATTRIBUTE_CHAR10 | — | ✅ |
| 4 | AttributeChar11 | ATTRIBUTE_CHAR11 | — | ✅ |
| 5 | AttributeChar12 | ATTRIBUTE_CHAR12 | — | ✅ |
| 6 | AttributeChar13 | ATTRIBUTE_CHAR13 | — | ✅ |
| 7 | AttributeChar14 | ATTRIBUTE_CHAR14 | — | ✅ |
| 8 | AttributeChar15 | ATTRIBUTE_CHAR15 | — | ✅ |
| 9 | AttributeChar16 | ATTRIBUTE_CHAR16 | — | ✅ |
| 10 | AttributeChar17 | ATTRIBUTE_CHAR17 | — | ✅ |
| 11 | AttributeChar18 | ATTRIBUTE_CHAR18 | — | ✅ |
| 12 | AttributeChar19 | ATTRIBUTE_CHAR19 | — | ✅ |
| 13 | AttributeChar2 | ATTRIBUTE_CHAR2 | — | ✅ |
| 14 | AttributeChar20 | ATTRIBUTE_CHAR20 | — | ✅ |
| 15 | AttributeChar3 | ATTRIBUTE_CHAR3 | — | ✅ |
| 16 | AttributeChar4 | ATTRIBUTE_CHAR4 | — | ✅ |
| 17 | AttributeChar5 | ATTRIBUTE_CHAR5 | — | ✅ |
| 18 | AttributeChar6 | ATTRIBUTE_CHAR6 | — | ✅ |
| 19 | AttributeChar7 | ATTRIBUTE_CHAR7 | — | ✅ |
| 20 | AttributeChar8 | ATTRIBUTE_CHAR8 | — | ✅ |
| 21 | AttributeChar9 | ATTRIBUTE_CHAR9 | — | ✅ |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | ✅ |
| 23 | AttributeDate2 | ATTRIBUTE_DATE2 | — | ✅ |
| 24 | AttributeDate3 | ATTRIBUTE_DATE3 | — | ✅ |
| 25 | AttributeDate4 | ATTRIBUTE_DATE4 | — | ✅ |
| 26 | AttributeDate5 | ATTRIBUTE_DATE5 | — | ✅ |
| 27 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | ✅ |
| 28 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | ✅ |
| 29 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | ✅ |
| 30 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | ✅ |
| 31 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | ✅ |
| 32 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | ✅ |
| 33 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | ✅ |
| 34 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | ✅ |
| 35 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | ✅ |
| 36 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | ✅ |
| 37 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | ✅ |
| 38 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | ✅ |
| 39 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | ✅ |
| 40 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | ✅ |
| 41 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | ✅ |
| 42 | AutoEquipmentFlag | AUTO_EQUIPMENT_FLAG | — | ✅ |
| 43 | CostedFlag | COSTED_FLAG | — | ✅ |
| 44 | CreatedBy | CREATED_BY | — | ✅ |
| 45 | CreationDate | CREATION_DATE | — | ✅ |
| 46 | InactiveDate | INACTIVE_DATE | — | ✅ |
| 47 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 48 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 49 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 50 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 51 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 52 | PjcExpenditureTypeId | PJC_EXPENDITURE_TYPE_ID | — | ✅ |
| 53 | ResourceClassCode | RESOURCE_CLASS_CODE | — | ✅ |
| 54 | ResourceCode | RESOURCE_CODE | — | ✅ |
| 55 | ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 56 | ResourceType | RESOURCE_TYPE | — | ✅ |
| 57 | UomCode | UOM_CODE | — | ✅ |

### [[wis_resources_tl|WIS_RESOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ResourceTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ResourceTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ResourceTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 4 | ResourceTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ResourceTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | ResourceTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ResourceTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ResourceTranslationPEOResourceDescription | RESOURCE_DESCRIPTION | — | ✅ |
| 9 | ResourceTranslationPEOResourceId | RESOURCE_ID | 🔑 | ✅ |
| 10 | ResourceTranslationPEOResourceName | RESOURCE_NAME | — | ✅ |
| 11 | ResourceTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
