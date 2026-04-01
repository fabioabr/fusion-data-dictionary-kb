---
id: DOC-OTHER-PVO-AssetKeyPVO
doc_type: system-doc
title: "AssetKeyPVO — PVO Cross-Module"
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
  - AssetKeyPVO
  - assetkeypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssetKeyPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Asset Key. Acessa as tabelas: FA_ASSET_KEYWORDS.

**Caminho:** `FscmTopModelAM.FinFaTrackDescDetailsAM.AssetKeyPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 2 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[fa_asset_keywords|FA_ASSET_KEYWORDS]] — 12 atributos (2 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[fa_asset_keywords|FA_ASSET_KEYWORDS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CodeCombinationId | CODE_COMBINATION_ID | 🔑 | ✅ |
| 2 | Segment1 | SEGMENT1 | — | — |
| 3 | Segment10 | SEGMENT10 | — | — |
| 4 | Segment2 | SEGMENT2 | — | — |
| 5 | Segment3 | SEGMENT3 | — | — |
| 6 | Segment4 | SEGMENT4 | — | — |
| 7 | Segment5 | SEGMENT5 | — | — |
| 8 | Segment6 | SEGMENT6 | — | — |
| 9 | Segment7 | SEGMENT7 | — | — |
| 10 | Segment8 | SEGMENT8 | — | — |
| 11 | Segment9 | SEGMENT9 | — | — |
| 12 | StructureInstanceNumber | STRUCTURE_INSTANCE_NUMBER | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
