---
id: DOC-OTHER-PVO-ApplyFlowPageBlockPVO
doc_type: system-doc
title: "ApplyFlowPageBlockPVO — PVO Cross-Module"
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
  - ApplyFlowPageBlockPVO
  - applyflowpageblockpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApplyFlowPageBlockPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Apply Flow Page Block. Acessa as tabelas: IRC_AF_BLOCKS_B, IRC_AF_BLOCKS_TL, IRC_AF_PAGE_BLOCKS_B (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingSetupAM.ApplyFlowPageBlockPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 4 | 1 | 9 | 24% |

---

## 🔗 Tabelas Relacionadas

- [[irc_af_blocks_b|IRC_AF_BLOCKS_B]] — 11 atributos (2 BICC)
- [[irc_af_blocks_tl|IRC_AF_BLOCKS_TL]] — 5 atributos (1 BICC)
- [[irc_af_page_blocks_b|IRC_AF_PAGE_BLOCKS_B]] — 11 atributos (1 PKs, 3 BICC)
- [[irc_af_page_blocks_tl|IRC_AF_PAGE_BLOCKS_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_af_blocks_b|IRC_AF_BLOCKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowBlockBPEOCreatedBy | CREATED_BY | — | — |
| 2 | ApplyFlowBlockBPEOCreationDate | CREATION_DATE | — | — |
| 3 | ApplyFlowBlockBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ApplyFlowBlockBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | ApplyFlowBlockBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | ApplyFlowBlockBPEOProfileContentTypeId | PROFILE_CONTENT_TYPE_ID | — | — |
| 7 | ApplyFlowBlockBPEOSeedDataSource | SEED_DATA_SOURCE | — | — |
| 8 | BlockCode | BLOCK_CODE | — | — |
| 9 | BlockId | BLOCK_ID | — | ✅ |
| 10 | BlockTypeCode | BLOCK_TYPE_CODE | — | — |
| 11 | BlockUsageCode | BLOCK_USAGE_CODE | — | — |

### [[irc_af_blocks_tl|IRC_AF_BLOCKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AFBlockTranslationPEOBlockId | BLOCK_ID | — | — |
| 2 | AFBlockTranslationPEOBlockInstructions | BLOCK_INSTRUCTIONS | — | — |
| 3 | AFBlockTranslationPEOBlockName | BLOCK_NAME | — | ✅ |
| 4 | AFBlockTranslationPEOBlockTitle | BLOCK_TITLE | — | — |
| 5 | AFBlockTranslationPEOLanguage | LANGUAGE | — | — |

### [[irc_af_page_blocks_b|IRC_AF_PAGE_BLOCKS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplyFlowPageBlockBPEOBlockId | BLOCK_ID | — | — |
| 2 | ApplyFlowPageBlockBPEOPageId | PAGE_ID | — | — |
| 3 | CreatedBy | CREATED_BY | — | — |
| 4 | CreationDate | CREATION_DATE | — | — |
| 5 | HideInMobileFlag | HIDE_IN_MOBILE_FLAG | — | — |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | PageBlockId | PAGE_BLOCK_ID | 🔑 | ✅ |
| 11 | PageBlockSeqNum | PAGE_BLOCK_SEQ_NUM | — | ✅ |

### [[irc_af_page_blocks_tl|IRC_AF_PAGE_BLOCKS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AFPageBlockTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | AFPageBlockTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | AFPageBlockTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | AFPageBlockTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | AFPageBlockTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | AFPageBlockTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | AFPageBlockTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | AFPageBlockTranslationPEOPageBlockId | PAGE_BLOCK_ID | — | — |
| 9 | AFPageBlockTranslationPEOPageBlockInstructions | PAGE_BLOCK_INSTRUCTIONS | — | ✅ |
| 10 | AFPageBlockTranslationPEOPageBlockTitle | PAGE_BLOCK_TITLE | — | ✅ |
| 11 | AFPageBlockTranslationPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
