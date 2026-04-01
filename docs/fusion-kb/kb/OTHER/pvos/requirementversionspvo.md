---
id: DOC-OTHER-PVO-RequirementVersionsPVO
doc_type: system-doc
title: "RequirementVersionsPVO — PVO Cross-Module"
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
  - RequirementVersionsPVO
  - requirementversionspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementVersionsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Requirement Versions. Acessa as tabelas: ACN_REQUIREMENT_VL, ACN_REQ_VERSION_VL.

**Caminho:** `FscmTopModelAM.RequirementsAnalyticsAM.RequirementVersionsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 2 | 1 | 23 | 92% |

---

## 🔗 Tabelas Relacionadas

- [[acn_requirement_vl|ACN_REQUIREMENT_VL]] — 11 atributos (11 BICC)
- [[acn_req_version_vl|ACN_REQ_VERSION_VL]] — 14 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

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
| 1 | RequirementVersionProduct | PRODUCT | — | ✅ |
| 2 | RequirementVersionStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 3 | RequirementVersionsCreatedBy | CREATED_BY | — | ✅ |
| 4 | RequirementVersionsCreationDate | CREATION_DATE | — | ✅ |
| 5 | RequirementVersionsDescription | DESCRIPTION | — | — |
| 6 | RequirementVersionsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | RequirementVersionsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | RequirementVersionsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | RequirementVersionsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | RequirementVersionsRequirementId | REQUIREMENT_ID | — | ✅ |
| 11 | RequirementVersionsRequirementVersionId | REQUIREMENT_VERSION_ID | 🔑 | ✅ |
| 12 | RequirementVersionsStatus | STATUS | — | ✅ |
| 13 | RequirementVersionsVersionNumber | VERSION_NUMBER | — | ✅ |
| 14 | TotalEstimates | TOTAL_ESTIMATES | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
