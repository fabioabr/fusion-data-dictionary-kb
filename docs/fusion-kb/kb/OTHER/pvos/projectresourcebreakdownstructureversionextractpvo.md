---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureVersionExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureVersionExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureVersionExtractPVO
  - projectresourcebreakdownstructureversionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureVersionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Version Extract. Acessa as tabelas: PJF_RBS_VERSIONS_B, PJF_RBS_VERSIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureVersionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 27 | 2 | 1 | 27 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_versions_b|PJF_RBS_VERSIONS_B]] — 15 atributos (1 PKs, 15 BICC)
- [[pjf_rbs_versions_tl|PJF_RBS_VERSIONS_TL]] — 12 atributos (12 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_versions_b|PJF_RBS_VERSIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSVersionPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSVersionPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSVersionPEOCurrentReportingFlag | CURRENT_REPORTING_FLAG | — | ✅ |
| 4 | PRBSVersionPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 5 | PRBSVersionPEOJobSetId | JOB_SET_ID | — | ✅ |
| 6 | PRBSVersionPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PRBSVersionPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PRBSVersionPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PRBSVersionPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PRBSVersionPEORbsHeaderId | RBS_HEADER_ID | — | ✅ |
| 11 | PRBSVersionPEORbsVersionId | RBS_VERSION_ID | 🔑 | ✅ |
| 12 | PRBSVersionPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 13 | PRBSVersionPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 14 | PRBSVersionPEOStatusCode | STATUS_CODE | — | ✅ |
| 15 | PRBSVersionPEOVersionNumber | VERSION_NUMBER | — | ✅ |

### [[pjf_rbs_versions_tl|PJF_RBS_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSVersionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSVersionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSVersionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | PRBSVersionTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 5 | PRBSVersionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PRBSVersionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PRBSVersionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PRBSVersionTranslationPEOName | NAME | — | ✅ |
| 9 | PRBSVersionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PRBSVersionTranslationPEORbsVersionId | RBS_VERSION_ID | — | ✅ |
| 11 | PRBSVersionTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | PRBSVersionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
