---
id: DOC-OTHER-PVO-AwardKeywordPVO
doc_type: system-doc
title: "AwardKeywordPVO — PVO Cross-Module"
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
  - AwardKeywordPVO
  - awardkeywordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardKeywordPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Keyword. Acessa as tabelas: GMS_AWARD_KEYWORDS, GMS_AWARD_PROJECTS, GMS_KEYWORDS_VL.

**Caminho:** `FscmTopModelAM.GmsAwardAM.AwardKeywordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 3 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_keywords|GMS_AWARD_KEYWORDS]] — 10 atributos (1 PKs, 10 BICC)
- [[gms_award_projects|GMS_AWARD_PROJECTS]] — 2 atributos (2 BICC)
- [[gms_keywords_vl|GMS_KEYWORDS_VL]] — 5 atributos (5 BICC)

---

## ⚙️ Atributos

### [[gms_award_keywords|GMS_AWARD_KEYWORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardKeywordPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardKeywordPEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardKeywordPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardKeywordPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardKeywordPEOKeyword | KEYWORD | — | ✅ |
| 6 | AwardKeywordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AwardKeywordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AwardKeywordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AwardKeywordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | Id | ID | 🔑 | ✅ |

### [[gms_award_projects|GMS_AWARD_PROJECTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardProjectPEOId | ID | — | ✅ |
| 2 | AwardProjectPEOProjectId | PROJECT_ID | — | ✅ |

### [[gms_keywords_vl|GMS_KEYWORDS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | KeywordPEODescription | DESCRIPTION | — | ✅ |
| 2 | KeywordPEOEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 3 | KeywordPEOKeywordId | KEYWORD_ID | — | ✅ |
| 4 | KeywordPEOKeywordName | KEYWORD_NAME | — | ✅ |
| 5 | KeywordPEOStartDateActive | START_DATE_ACTIVE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
