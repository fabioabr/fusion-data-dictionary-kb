---
id: DOC-OTHER-PVO-ProjectResourceClassExtractPVO
doc_type: system-doc
title: "ProjectResourceClassExtractPVO — PVO Cross-Module"
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
  - ProjectResourceClassExtractPVO
  - projectresourceclassextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceClassExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Class Extract. Acessa as tabelas: PJF_RESOURCE_CLASSES_B, PJF_RESOURCE_CLASSES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceClassExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 20 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_resource_classes_b|PJF_RESOURCE_CLASSES_B]] — 9 atributos (1 PKs, 9 BICC)
- [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_resource_classes_b|PJF_RESOURCE_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceClassBaseCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceClassBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceClassBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProjectResourceClassBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | ProjectResourceClassBaseLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ProjectResourceClassBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProjectResourceClassBaseResourceClassCode | RESOURCE_CLASS_CODE | — | ✅ |
| 8 | ProjectResourceClassBaseResourceClassId | RESOURCE_CLASS_ID | 🔑 | ✅ |
| 9 | ProjectResourceClassBaseResourceClassSeq | RESOURCE_CLASS_SEQ | — | ✅ |

### [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResourceClassTLCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResourceClassTLCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResourceClassTLDescription | DESCRIPTION | — | ✅ |
| 4 | ProjectResourceClassTLLanguage | LANGUAGE | — | ✅ |
| 5 | ProjectResourceClassTLLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResourceClassTLLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | ProjectResourceClassTLLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ProjectResourceClassTLName | NAME | — | ✅ |
| 9 | ProjectResourceClassTLObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ProjectResourceClassTLResourceClassId | RESOURCE_CLASS_ID | — | ✅ |
| 11 | ProjectResourceClassTLSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
