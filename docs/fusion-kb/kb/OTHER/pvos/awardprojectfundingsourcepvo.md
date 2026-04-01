---
id: DOC-OTHER-PVO-AwardProjectFundingSourcePVO
doc_type: system-doc
title: "AwardProjectFundingSourcePVO — PVO Cross-Module"
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
  - AwardProjectFundingSourcePVO
  - awardprojectfundingsourcepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardProjectFundingSourcePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Project Funding Source. Acessa as tabelas: GMS_AWD_PRJ_FND_SOURCES.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardProjectFundingSourcePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 2 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[gms_awd_prj_fnd_sources|GMS_AWD_PRJ_FND_SOURCES]] — 12 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[gms_awd_prj_fnd_sources|GMS_AWD_PRJ_FND_SOURCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectFundingSourcePEOAwardFundingSourceId | AWARD_FUNDING_SOURCE_ID | — | — |
| 2 | AwardProjectFundingSourcePEOAwardId | AWARD_ID | — | — |
| 3 | AwardProjectFundingSourcePEOAwdProjLinkageId | AWD_PROJ_LINKAGE_ID | — | — |
| 4 | AwardProjectFundingSourcePEOCreatedBy | CREATED_BY | — | — |
| 5 | AwardProjectFundingSourcePEOCreationDate | CREATION_DATE | — | — |
| 6 | AwardProjectFundingSourcePEOFundingSourceId | FUNDING_SOURCE_ID | — | — |
| 7 | AwardProjectFundingSourcePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardProjectFundingSourcePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 9 | AwardProjectFundingSourcePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 10 | AwardProjectFundingSourcePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | AwardProjectFundingSourcePEOProjectId | PROJECT_ID | — | — |
| 12 | AwdPrjFundSourceId | AWD_PRJ_FUND_SOURCE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
