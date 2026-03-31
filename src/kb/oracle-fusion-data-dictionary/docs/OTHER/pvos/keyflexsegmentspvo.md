---
id: DOC-OTHER-PVO-KeyFlexSegmentsPVO
doc_type: system-doc
title: "KeyFlexSegmentsPVO — PVO Cross-Module"
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
  - KeyFlexSegmentsPVO
  - keyflexsegmentspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeyFlexSegmentsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Key Flex Segments. Acessa as tabelas: FND_KF_SEGMENTS_B, FND_KF_SEGMENTS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.KeyFlexSegmentsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 2 | 22 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_segments_b|FND_KF_SEGMENTS_B]] — 14 atributos (2 PKs, 14 BICC)
- [[fnd_kf_segments_tl|FND_KF_SEGMENTS_TL]] — 8 atributos (8 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_segments_b|FND_KF_SEGMENTS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ColumnName | COLUMN_NAME | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DefaultValueSetId | DEFAULT_VALUE_SET_ID | — | ✅ |
| 5 | DisplayWidth | DISPLAY_WIDTH | — | ✅ |
| 6 | EnabledFlag | ENABLED_FLAG | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RangeType | RANGE_TYPE | — | ✅ |
| 11 | SegmentCode | SEGMENT_CODE | 🔑 | ✅ |
| 12 | SegmentIdentifier | SEGMENT_IDENTIFIER | — | ✅ |
| 13 | SequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 14 | StructureId | STRUCTURE_ID | 🔑 | ✅ |

### [[fnd_kf_segments_tl|FND_KF_SEGMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Description | DESCRIPTION | — | ✅ |
| 2 | Language | LANGUAGE | — | ✅ |
| 3 | Name | NAME | — | ✅ |
| 4 | Prompt | PROMPT | — | ✅ |
| 5 | SegmentCode1 | SEGMENT_CODE | — | ✅ |
| 6 | ShortPrompt | SHORT_PROMPT | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |
| 8 | StructureId1 | STRUCTURE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
