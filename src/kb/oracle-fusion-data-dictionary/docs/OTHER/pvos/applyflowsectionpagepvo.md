---
id: DOC-OTHER-PVO-ApplyFlowSectionPagePVO
doc_type: system-doc
title: "ApplyFlowSectionPagePVO — PVO Cross-Module"
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
  - ApplyFlowSectionPagePVO
  - applyflowsectionpagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplyFlowSectionPagePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Apply Flow Section Page. Acessa as tabelas: IRC_AF_PAGES_B, IRC_AF_PAGES_TL, IRC_AF_SECTIONS_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.ApplyFlowSectionPagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 4 | 1 | 5 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[irc_af_pages_b|IRC_AF_PAGES_B]] — 7 atributos (1 BICC)
- [[irc_af_pages_tl|IRC_AF_PAGES_TL]] — 4 atributos
- [[irc_af_sections_b|IRC_AF_SECTIONS_B]] — 9 atributos (1 PKs, 3 BICC)
- [[irc_af_sections_tl|IRC_AF_SECTIONS_TL]] — 4 atributos (1 BICC)

---

## ⚙️ Atributos

### [[irc_af_pages_b|IRC_AF_PAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowPageBPEOCreatedBy | CREATED_BY | — | — |
| 2 | ApplyFlowPageBPEOCreationDate | CREATION_DATE | — | — |
| 3 | ApplyFlowPageBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ApplyFlowPageBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | ApplyFlowPageBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ApplyFlowPageBPEOPageSeqNum | PAGE_SEQ_NUM | — | — |
| 7 | PageId | PAGE_ID | — | — |

### [[irc_af_pages_tl|IRC_AF_PAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AFPageTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | AFPageTranslationPEOPageId | PAGE_ID | — | — |
| 3 | AFPageTranslationPEOPageName | PAGE_NAME | — | — |
| 4 | AFPageTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[irc_af_sections_b|IRC_AF_SECTIONS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AfVersionId | AF_VERSION_ID | — | — |
| 2 | CreatedBy | CREATED_BY | — | — |
| 3 | CreationDate | CREATION_DATE | — | — |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SectionId | SECTION_ID | 🔑 | ✅ |
| 9 | SectionSeqNum | SECTION_SEQ_NUM | — | ✅ |

### [[irc_af_sections_tl|IRC_AF_SECTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AFSectionTranslationPEOLanguage | LANGUAGE | — | — |
| 2 | AFSectionTranslationPEOSectionId | SECTION_ID | — | — |
| 3 | AFSectionTranslationPEOSectionName | SECTION_NAME | — | ✅ |
| 4 | AFSectionTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
