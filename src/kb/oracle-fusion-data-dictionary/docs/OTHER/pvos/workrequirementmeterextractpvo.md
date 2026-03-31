---
id: DOC-OTHER-PVO-WorkRequirementMeterExtractPVO
doc_type: system-doc
title: "WorkRequirementMeterExtractPVO — PVO Cross-Module"
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
  - WorkRequirementMeterExtractPVO
  - workrequirementmeterextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkRequirementMeterExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Requirement Meter Extract. Acessa as tabelas: MNT_WR_METERS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.WorkRequirementMeterExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_wr_meters|MNT_WR_METERS]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[mnt_wr_meters|MNT_WR_METERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseInterval | BASE_INTERVAL | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | MeterDefinitionId | METER_DEFINITION_ID | — | ✅ |
| 10 | MeterId | METER_ID | — | ✅ |
| 11 | NextForecastDueByCode | NEXT_FORECAST_DUE_BY_CODE | — | ✅ |
| 12 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 14 | RequestId | REQUEST_ID | — | ✅ |
| 15 | RequirementId | REQUIREMENT_ID | — | ✅ |
| 16 | RequirementMeterId | REQUIREMENT_METER_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
