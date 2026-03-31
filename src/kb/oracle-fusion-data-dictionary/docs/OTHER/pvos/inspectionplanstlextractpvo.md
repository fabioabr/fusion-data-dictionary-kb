---
id: DOC-OTHER-PVO-InspectionPlansTLExtractPVO
doc_type: system-doc
title: "InspectionPlansTLExtractPVO — PVO Cross-Module"
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
  - InspectionPlansTLExtractPVO
  - inspectionplanstlextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InspectionPlansTLExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inspection Plans TLExtract. Acessa as tabelas: QA_INSPECTION_PLANS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.QaBiccExtractAM.InspectionPlansTLExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[qa_inspection_plans_tl|QA_INSPECTION_PLANS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InspectionPlansTLRptPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | InspectionPlansTLRptPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | InspectionPlansTLRptPEODescription | DESCRIPTION | — | ✅ |
| 4 | InspectionPlansTLRptPEOInspectionPlanId | INSPECTION_PLAN_ID | 🔑 | ✅ |
| 5 | InspectionPlansTLRptPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | InspectionPlansTLRptPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InspectionPlansTLRptPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InspectionPlansTLRptPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InspectionPlansTLRptPEOName | NAME | — | ✅ |
| 10 | InspectionPlansTLRptPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
