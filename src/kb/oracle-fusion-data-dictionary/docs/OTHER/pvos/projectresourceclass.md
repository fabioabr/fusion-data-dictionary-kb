---
id: DOC-OTHER-PVO-ProjectResourceClass
doc_type: system-doc
title: "ProjectResourceClass — PVO Cross-Module"
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
  - ProjectResourceClass
  - projectresourceclass
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceClass

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Class. Acessa as tabelas: PJF_RESOURCE_CLASSES_B, PJF_RESOURCE_CLASSES_TL.

**Caminho:** `FscmTopModelAM.PjfResourcesAnalyticsAM.ProjectResourceClass`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 20 | 2 | 1 | 8 | 40% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_resource_classes_b|PJF_RESOURCE_CLASSES_B]] — 9 atributos (1 PKs, 7 BICC)
- [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]] — 11 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pjf_resource_classes_b|PJF_RESOURCE_CLASSES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResClassPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | ProjectResClassPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | ProjectResClassPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | ProjectResClassPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | ProjectResClassPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ProjectResClassPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProjectResClassPEOResourceClassCode | RESOURCE_CLASS_CODE | — | ✅ |
| 8 | ProjectResClassPEOResourceClassSeq | RESOURCE_CLASS_SEQ | — | ✅ |
| 9 | ResourceClassId | RESOURCE_CLASS_ID | 🔑 | ✅ |

### [[pjf_resource_classes_tl|PJF_RESOURCE_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ProjectResClassTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | ProjectResClassTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | ProjectResClassTLPEODescription | DESCRIPTION | — | — |
| 4 | ProjectResClassTLPEOLanguage | LANGUAGE | — | — |
| 5 | ProjectResClassTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ProjectResClassTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ProjectResClassTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ProjectResClassTLPEOName | NAME | — | — |
| 9 | ProjectResClassTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ProjectResClassTLPEOResourceClassId | RESOURCE_CLASS_ID | — | — |
| 11 | ProjectResClassTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
