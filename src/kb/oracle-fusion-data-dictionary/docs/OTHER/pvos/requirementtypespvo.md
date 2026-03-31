---
id: DOC-OTHER-PVO-RequirementTypesPVO
doc_type: system-doc
title: "RequirementTypesPVO — PVO Cross-Module"
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
  - RequirementTypesPVO
  - requirementtypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Requirement Types. Acessa as tabelas: ACA_CS_CLASS_VL.

**Caminho:** `FscmTopModelAM.RequirementsAnalyticsAM.RequirementTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 1 | 1 | 19 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[aca_cs_class_vl|ACA_CS_CLASS_VL]] — 20 atributos (1 PKs, 19 BICC)

---

## ⚙️ Atributos

### [[aca_cs_class_vl|ACA_CS_CLASS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementTypeBipTemplate | BIP_TEMPLATE | — | ✅ |
| 2 | RequirementTypeClassCode | CLASS_CODE | — | ✅ |
| 3 | RequirementTypeClassFamilyCode | CLASS_FAMILY_CODE | — | ✅ |
| 4 | RequirementTypeClassId | CLASS_ID | 🔑 | ✅ |
| 5 | RequirementTypeClassName | CLASS_NAME | — | ✅ |
| 6 | RequirementTypeClassPolicy | CLASS_POLICY | — | ✅ |
| 7 | RequirementTypeClassSubFamilyCode | CLASS_SUB_FAMILY_CODE | — | ✅ |
| 8 | RequirementTypeCreatedBy | CREATED_BY | — | ✅ |
| 9 | RequirementTypeCreationDate | CREATION_DATE | — | ✅ |
| 10 | RequirementTypeDeletedFlag | DELETED_FLAG | — | ✅ |
| 11 | RequirementTypeDescription | DESCRIPTION | — | — |
| 12 | RequirementTypeDisableDate | DISABLE_DATE | — | ✅ |
| 13 | RequirementTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | RequirementTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 15 | RequirementTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | RequirementTypeObjectCreationAllowedFlag | OBJECT_CREATION_ALLOWED_FLAG | — | ✅ |
| 17 | RequirementTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 18 | RequirementTypeParentClassId | PARENT_CLASS_ID | — | ✅ |
| 19 | RequirementTypeProductOwned | PRODUCT_OWNED | — | ✅ |
| 20 | TrackHistoryFlag | TRACK_HISTORY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
