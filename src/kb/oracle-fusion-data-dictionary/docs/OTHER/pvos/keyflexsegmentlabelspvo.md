---
id: DOC-OTHER-PVO-KeyFlexSegmentLabelsPVO
doc_type: system-doc
title: "KeyFlexSegmentLabelsPVO — PVO Cross-Module"
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
  - KeyFlexSegmentLabelsPVO
  - keyflexsegmentlabelspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeyFlexSegmentLabelsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Key Flex Segment Labels. Acessa as tabelas: FND_KF_SEGMENT_LABELS_B, FND_KF_SEGMENT_LABELS_TL.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.KeyFlexSegmentLabelsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 2 | 3 | 19 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_segment_labels_b|FND_KF_SEGMENT_LABELS_B]] — 12 atributos (3 PKs, 12 BICC)
- [[fnd_kf_segment_labels_tl|FND_KF_SEGMENT_LABELS_TL]] — 7 atributos (7 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_segment_labels_b|FND_KF_SEGMENT_LABELS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | BiObjectName | BI_OBJECT_NAME | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | GlobalFlag | GLOBAL_FLAG | — | ✅ |
| 6 | KeyFlexfieldCode | KEY_FLEXFIELD_CODE | 🔑 | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | RequiredFlag | REQUIRED_FLAG | — | ✅ |
| 11 | SegmentLabelCode | SEGMENT_LABEL_CODE | 🔑 | ✅ |
| 12 | UniqueFlag | UNIQUE_FLAG | — | ✅ |

### [[fnd_kf_segment_labels_tl|FND_KF_SEGMENT_LABELS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId1 | APPLICATION_ID | — | ✅ |
| 2 | Description | DESCRIPTION | — | ✅ |
| 3 | KeyFlexfieldCode1 | KEY_FLEXFIELD_CODE | — | ✅ |
| 4 | Language | LANGUAGE | — | ✅ |
| 5 | Name | NAME | — | ✅ |
| 6 | SegmentLabelCode1 | SEGMENT_LABEL_CODE | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
