---
id: DOC-OTHER-PVO-MeterApplicabilityExtractPVO
doc_type: system-doc
title: "MeterApplicabilityExtractPVO — PVO Cross-Module"
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
  - MeterApplicabilityExtractPVO
  - meterapplicabilityextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MeterApplicabilityExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Meter Applicability Extract. Acessa as tabelas: CSE_METER_APPLICABILITY.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.MeterApplicabilityExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_meter_applicability|CSE_METER_APPLICABILITY]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[cse_meter_applicability|CSE_METER_APPLICABILITY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | ActiveStartDate | ACTIVE_START_DATE | — | ✅ |
| 3 | ApplicabilityId | APPLICABILITY_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | ✅ |
| 5 | CreationDate | CREATION_DATE | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | MeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 12 | ObjectId | OBJECT_ID | — | ✅ |
| 13 | ObjectTypeCode | OBJECT_TYPE_CODE | — | ✅ |
| 14 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 15 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 16 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
