---
id: DOC-OTHER-PVO-ResourceAvailabilityDetailsExtractPVO
doc_type: system-doc
title: "ResourceAvailabilityDetailsExtractPVO — PVO Cross-Module"
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
  - ResourceAvailabilityDetailsExtractPVO
  - resourceavailabilitydetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceAvailabilityDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Availability Details Extract. Acessa as tabelas: RCS_RESOURCE_AVL_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ResourceAvailabilityDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_resource_avl_dtls|RCS_RESOURCE_AVL_DTLS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[rcs_resource_avl_dtls|RCS_RESOURCE_AVL_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AvailableUnits | AVAILABLE_UNITS | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EndDateTime | END_DATE_TIME | — | ✅ |
| 5 | ExceptionId | EXCEPTION_ID | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MfgOrgIdentifier | MFG_ORG_IDENTIFIER | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | ResourceScheduleId | RESOURCE_SCHEDULE_ID | 🔑 | ✅ |
| 12 | ScheduleDetailId | SCHEDULE_DETAIL_ID | — | ✅ |
| 13 | ScheduleId | SCHEDULE_ID | — | ✅ |
| 14 | ShiftId | SHIFT_ID | — | ✅ |
| 15 | StartDateTime | START_DATE_TIME | — | ✅ |
| 16 | WcResourceIdentifier | WC_RESOURCE_IDENTIFIER | — | ✅ |
| 17 | WorkCenterId | WORK_CENTER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
