---
id: DOC-OTHER-PVO-AwardKeywordExtractPVO
doc_type: system-doc
title: "AwardKeywordExtractPVO — PVO Cross-Module"
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
  - AwardKeywordExtractPVO
  - awardkeywordextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AwardKeywordExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Award Keyword Extract. Acessa as tabelas: GMS_AWARD_KEYWORDS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.AwardKeywordExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 1 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_award_keywords|GMS_AWARD_KEYWORDS]] — 10 atributos (1 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[gms_award_keywords|GMS_AWARD_KEYWORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AwardKeywordPEOAwardId | AWARD_ID | — | ✅ |
| 2 | AwardKeywordPEOAwdProjectLnkId | AWD_PROJECT_LNK_ID | — | ✅ |
| 3 | AwardKeywordPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | AwardKeywordPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | AwardKeywordPEOId | ID | 🔑 | ✅ |
| 6 | AwardKeywordPEOKeyword | KEYWORD | — | ✅ |
| 7 | AwardKeywordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | AwardKeywordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | AwardKeywordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | AwardKeywordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
