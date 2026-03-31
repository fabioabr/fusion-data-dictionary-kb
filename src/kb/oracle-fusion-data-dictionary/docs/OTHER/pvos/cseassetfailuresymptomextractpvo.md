---
id: DOC-OTHER-PVO-CseAssetFailureSymptomExtractPVO
doc_type: system-doc
title: "CseAssetFailureSymptomExtractPVO — PVO Cross-Module"
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
  - CseAssetFailureSymptomExtractPVO
  - cseassetfailuresymptomextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CseAssetFailureSymptomExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cse Asset Failure Symptom Extract. Acessa as tabelas: CSE_FAILURE_SYMPTOMS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.CseAssetFailureSymptomExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_failure_symptoms|CSE_FAILURE_SYMPTOMS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[cse_failure_symptoms|CSE_FAILURE_SYMPTOMS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CaptureObjectId | CAPTURE_OBJECT_ID | — | ✅ |
| 2 | CaptureObjectType | CAPTURE_OBJECT_TYPE | — | ✅ |
| 3 | Comments | COMMENTS | — | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | DiagnosticCodeId | DIAGNOSTIC_CODE_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | SymptomId | SYMPTOM_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
