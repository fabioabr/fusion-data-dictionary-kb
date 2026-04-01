---
id: DOC-HCM-PVO-QualifiersPVO
doc_type: system-doc
title: "QualifiersPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QualifiersPVO
  - qualifierspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualifiersPVO

## 📌 Visão Geral

Disponibiliza qualificadores de perfil com traduções, utilizados na biblioteca de conteúdo. Define critérios de classificação para competências e habilidades no Talent Profile.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.QualifiersPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 28 | 2 | 2 | 20 | 71% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_qualifiers_b|HRT_QUALIFIERS_B]] — 17 atributos (2 PKs, 17 BICC)
- [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[hrt_qualifiers_b|HRT_QUALIFIERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifiersBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 2 | QualifiersBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | QualifiersBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | QualifiersBPEOEmpDefFlag | EMP_DEF_FLAG | — | ✅ |
| 5 | QualifiersBPEOEmpViewFlag | EMP_VIEW_FLAG | — | ✅ |
| 6 | QualifiersBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualifiersBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | QualifiersBPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | QualifiersBPEOMgrDefFlag | MGR_DEF_FLAG | — | ✅ |
| 10 | QualifiersBPEOMgrViewFlag | MGR_VIEW_FLAG | — | ✅ |
| 11 | QualifiersBPEOModuleId | MODULE_ID | — | ✅ |
| 12 | QualifiersBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | QualifiersBPEOQualifierCode | QUALIFIER_CODE | — | ✅ |
| 14 | QualifiersBPEOQualifierId | QUALIFIER_ID | 🔑 | ✅ |
| 15 | QualifiersBPEOQualifierSeqNumber | QUALIFIER_SEQ_NUMBER | — | ✅ |
| 16 | QualifiersBPEOQualifierSetId | QUALIFIER_SET_ID | — | ✅ |
| 17 | QualifiersBPEOSearchFlag | SEARCH_FLAG | — | ✅ |

### [[hrt_qualifiers_tl|HRT_QUALIFIERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | QualifiersTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | QualifiersTranslationPEOCreatedBy | CREATED_BY | — | — |
| 3 | QualifiersTranslationPEOCreationDate | CREATION_DATE | — | — |
| 4 | QualifiersTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | QualifiersTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | QualifiersTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | QualifiersTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | QualifiersTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | QualifiersTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | QualifiersTranslationPEOQualifierId | QUALIFIER_ID | — | — |
| 11 | SourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
