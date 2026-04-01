---
id: DOC-HCM-PVO-KeyFlexSegmentLabelsVLPVO
doc_type: system-doc
title: "KeyFlexSegmentLabelsVLPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - KeyFlexSegmentLabelsVLPVO
  - keyflexsegmentlabelsvlpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# KeyFlexSegmentLabelsVLPVO

## 📌 Visão Geral

Disponibiliza rótulos de segmentos de key flexfields com mapeamento BI. Utilizado para configuração de campos chave em relatórios analíticos.

**Caminho:** `FscmTopModelAM.AnalyticsServiceAM.KeyFlexSegmentLabelsVLPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_kf_segment_labels_vl|FND_KF_SEGMENT_LABELS_VL]] — 14 atributos (3 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fnd_kf_segment_labels_vl|FND_KF_SEGMENT_LABELS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | BiObjectName | BI_OBJECT_NAME | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | GlobalFlag | GLOBAL_FLAG | — | ✅ |
| 7 | KeyFlexfieldCode | KEY_FLEXFIELD_CODE | 🔑 | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | Name | NAME | — | ✅ |
| 12 | RequiredFlag | REQUIRED_FLAG | — | ✅ |
| 13 | SegmentLabelCode | SEGMENT_LABEL_CODE | 🔑 | ✅ |
| 14 | UniqueFlag | UNIQUE_FLAG | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
