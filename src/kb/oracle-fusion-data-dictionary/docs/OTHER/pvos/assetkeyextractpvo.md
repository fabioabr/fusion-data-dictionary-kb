---
id: DOC-OTHER-PVO-AssetKeyExtractPVO
doc_type: system-doc
title: "AssetKeyExtractPVO — PVO Cross-Module"
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
  - AssetKeyExtractPVO
  - assetkeyextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetKeyExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Key Extract. Acessa as tabelas: FA_ASSET_KEYWORDS.

**Caminho:** `FscmTopModelAM.FinExtractAM.FaBiccExtractAM.AssetKeyExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 1 | 2 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fa_asset_keywords|FA_ASSET_KEYWORDS]] — 22 atributos (2 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[fa_asset_keywords|FA_ASSET_KEYWORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetKeyCodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 2 | AssetKeyCreatedBy | CREATED_BY | — | ✅ |
| 3 | AssetKeyCreationDate | CREATION_DATE | — | ✅ |
| 4 | AssetKeyEnabledFlag | ENABLED_FLAG | — | ✅ |
| 5 | AssetKeyEndDateActive | END_DATE_ACTIVE | — | ✅ |
| 6 | AssetKeyLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | AssetKeyLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | AssetKeyLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | AssetKeyObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | AssetKeySegment1 | SEGMENT1 | — | ✅ |
| 11 | AssetKeySegment10 | SEGMENT10 | — | ✅ |
| 12 | AssetKeySegment2 | SEGMENT2 | — | ✅ |
| 13 | AssetKeySegment3 | SEGMENT3 | — | ✅ |
| 14 | AssetKeySegment4 | SEGMENT4 | — | ✅ |
| 15 | AssetKeySegment5 | SEGMENT5 | — | ✅ |
| 16 | AssetKeySegment6 | SEGMENT6 | — | ✅ |
| 17 | AssetKeySegment7 | SEGMENT7 | — | ✅ |
| 18 | AssetKeySegment8 | SEGMENT8 | — | ✅ |
| 19 | AssetKeySegment9 | SEGMENT9 | — | ✅ |
| 20 | AssetKeyStartDateActive | START_DATE_ACTIVE | — | ✅ |
| 21 | AssetKeyStructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | 🔑 | ✅ |
| 22 | AssetKeySummaryFlag | SUMMARY_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
