---
id: DOC-OTHER-PVO-RequirementsPVO
doc_type: system-doc
title: "RequirementsPVO — PVO Cross-Module"
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
  - RequirementsPVO
  - requirementspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RequirementsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Requirements. Acessa as tabelas: ACN_REQUIREMENT_B, ACN_REQUIREMENT_TL, ACN_REQ_VERSION_B (+1).

**Caminho:** `FscmTopModelAM.RequirementsAnalyticsAM.RequirementsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 42 | 4 | 2 | 40 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[acn_requirement_b|ACN_REQUIREMENT_B]] — 10 atributos (1 PKs, 10 BICC)
- [[acn_requirement_tl|ACN_REQUIREMENT_TL]] — 10 atributos (10 BICC)
- [[acn_req_version_b|ACN_REQ_VERSION_B]] — 12 atributos (1 PKs, 11 BICC)
- [[acn_req_version_tl|ACN_REQ_VERSION_TL]] — 10 atributos (9 BICC)

---

## ⚙️ Atributos

### [[acn_requirement_b|ACN_REQUIREMENT_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementBaseAllowAccesstoEveryone | ALLOW_ACCESSTO_EVERYONE | — | ✅ |
| 2 | RequirementBaseCreatedBy | CREATED_BY | — | ✅ |
| 3 | RequirementBaseCreationDate | CREATION_DATE | — | ✅ |
| 4 | RequirementBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RequirementBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RequirementBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RequirementBaseLatestVersionId | LATEST_VERSION_ID | — | ✅ |
| 8 | RequirementBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequirementBaseRequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 10 | Type | TYPE | — | ✅ |

### [[acn_requirement_tl|ACN_REQUIREMENT_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementTranslationCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementTranslationCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementTranslationLanguage | LANGUAGE | — | ✅ |
| 4 | RequirementTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | RequirementTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | RequirementTranslationLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | RequirementTranslationName | NAME | — | ✅ |
| 8 | RequirementTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequirementTranslationRequirementId | REQUIREMENT_ID | — | ✅ |
| 10 | RequirementTranslationSourceLang | SOURCE_LANG | — | ✅ |

### [[acn_req_version_b|ACN_REQ_VERSION_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementVersionCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementVersionCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementVersionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | RequirementVersionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | RequirementVersionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | RequirementVersionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | RequirementVersionProduct | PRODUCT | — | ✅ |
| 8 | RequirementVersionRequirementId | REQUIREMENT_ID | — | ✅ |
| 9 | RequirementVersionRequirementVersionId | REQUIREMENT_VERSION_ID | 🔑 | ✅ |
| 10 | RequirementVersionStatus | STATUS | — | ✅ |
| 11 | RequirementVersionStructureUpdateDate | STRUCTURE_UPDATE_DATE | — | — |
| 12 | RequirementVersionVersionNumber | VERSION_NUMBER | — | ✅ |

### [[acn_req_version_tl|ACN_REQ_VERSION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RequirementVersionTranslatioCreatedBy | CREATED_BY | — | ✅ |
| 2 | RequirementVersionTranslatioCreationDate | CREATION_DATE | — | ✅ |
| 3 | RequirementVersionTranslatioDescription | DESCRIPTION | — | — |
| 4 | RequirementVersionTranslatioLanguage | LANGUAGE | — | ✅ |
| 5 | RequirementVersionTranslatioLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | RequirementVersionTranslatioLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | RequirementVersionTranslatioLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | RequirementVersionTranslatioObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | RequirementVersionTranslatioRequirementVersionId | REQUIREMENT_VERSION_ID | — | ✅ |
| 10 | RequirementVersionTranslatioSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
