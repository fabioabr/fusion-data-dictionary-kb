---
id: DOC-OTHER-PVO-WorkCenterResourceExceptionDetailsExtractPVO
doc_type: system-doc
title: "WorkCenterResourceExceptionDetailsExtractPVO — PVO Cross-Module"
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
  - WorkCenterResourceExceptionDetailsExtractPVO
  - workcenterresourceexceptiondetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterResourceExceptionDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center Resource Exception Details Extract. Acessa as tabelas: RCS_WC_RESOURCE_EXC_DETAILS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.WorkCenterResourceExceptionDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_wc_resource_exc_details|RCS_WC_RESOURCE_EXC_DETAILS]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[rcs_wc_resource_exc_details|RCS_WC_RESOURCE_EXC_DETAILS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | ExcUnitsAvailable | EXC_UNITS_AVAILABLE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ResourceId | RESOURCE_ID | — | ✅ |
| 9 | WcId | WC_ID | — | ✅ |
| 10 | WcResExcDetailId | WC_RES_EXC_DETAIL_ID | 🔑 | ✅ |
| 11 | WcResourceExcId | WC_RESOURCE_EXC_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
