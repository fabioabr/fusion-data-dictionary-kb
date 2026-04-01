---
id: DOC-OTHER-PVO-RequirementLineItemsPVO
doc_type: system-doc
title: "RequirementLineItemsPVO — PVO Cross-Module"
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
  - RequirementLineItemsPVO
  - requirementlineitemspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementLineItemsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Requirement Line Items. Acessa as tabelas: ACN_REQUIREMENT_LINE_ITEM, ACN_REQUIREMENT_VL, ACN_REQ_VERSION_VL.

**Caminho:** `FscmTopModelAM.RequirementsAnalyticsAM.RequirementLineItemsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 3 | 1 | 43 | 96% |

---

## 🔗 Tabelas Relacionadas

- [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]] — 20 atributos (1 PKs, 20 BICC)
- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 11 atributos (11 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 14 atributos (12 BICC)

---

## ⚙️ Atributos

### [[acn_requirement_line_item|ACN_REQUIREMENT_LINE_ITEM]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementLineItemsBaseLineItemId | BASE_LINE_ITEM_ID | — | ✅ |
| 2 | RequirementLineItemsContent | CONTENT | — | ✅ |
| 3 | RequirementLineItemsCreatedBy | CREATED_BY | — | ✅ |
| 4 | RequirementLineItemsCreationDate | CREATION_DATE | — | ✅ |
| 5 | RequirementLineItemsDescription | DESCRIPTION | — | ✅ |
| 6 | RequirementLineItemsEstimates | ESTIMATES | — | ✅ |
| 7 | RequirementLineItemsFulfilled | FULFILLED | — | ✅ |
| 8 | RequirementLineItemsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | RequirementLineItemsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | RequirementLineItemsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | RequirementLineItemsName | NAME | — | ✅ |
| 12 | RequirementLineItemsObjectId | OBJECT_ID | — | ✅ |
| 13 | RequirementLineItemsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | RequirementLineItemsParentLineItemId | PARENT_LINE_ITEM_ID | — | ✅ |
| 15 | RequirementLineItemsPriority | PRIORITY | — | ✅ |
| 16 | RequirementLineItemsRequirementLineItemId | REQUIREMENT_LINE_ITEM_ID | 🔑 | ✅ |
| 17 | RequirementLineItemsRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 18 | RequirementLineItemsScope | SCOPE | — | ✅ |
| 19 | RequirementLineItemsSectionCode | SECTION_CODE | — | ✅ |
| 20 | SectionNumber | SECTION_NUMBER | — | ✅ |

### [[acn_requirement_vl|ACN_REQUIREMENT_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RequirementCreatedBy | CREATED_BY | — | ✅ |
| 3 | RequirementCreationDate | CREATION_DATE | — | ✅ |
| 4 | RequirementId | REQUIREMENT_ID | — | ✅ |
| 5 | RequirementLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RequirementLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RequirementLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RequirementLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 9 | RequirementName | NAME | — | ✅ |
| 10 | RequirementObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | Type | TYPE | — | ✅ |

### [[acn_req_version_vl|ACN_REQ_VERSION_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementVersionCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementVersionCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementVersionDescription | DESCRIPTION | — | — |
| 4 | RequirementVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RequirementVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RequirementVersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RequirementVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | RequirementVersionProduct | PRODUCT | — | ✅ |
| 9 | RequirementVersionRequirementId | REQUIREMENT_ID | — | ✅ |
| 10 | RequirementVersionRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 11 | RequirementVersionStatus | STATUS | — | ✅ |
| 12 | RequirementVersionStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 13 | RequirementVersionTotalEstimates | TOTAL_ESTIMATES | — | ✅ |
| 14 | RequirementVersionVersionNumber | VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
