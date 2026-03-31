---
id: DOC-OTHER-PVO-ProcessClassTLExtractPVO
doc_type: system-doc
title: "ProcessClassTLExtractPVO — PVO Cross-Module"
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
  - ProcessClassTLExtractPVO
  - processclasstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProcessClassTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Process Class TLExtract. Acessa as tabelas: DOO_PROCESS_CLASSES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.ProcessClassTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[doo_process_classes_tl|DOO_PROCESS_CLASSES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Description | DESCRIPTION | — | ✅ |
| 4 | Language | LANGUAGE | 🔑 | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | OrchestrationApplicationId | ORCHESTRATION_APPLICATION_ID | — | ✅ |
| 10 | ProcessClassId | PROCESS_CLASS_ID | 🔑 | ✅ |
| 11 | ProcessClassName | PROCESS_CLASS_NAME | — | ✅ |
| 12 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
