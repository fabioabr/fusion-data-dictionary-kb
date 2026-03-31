---
id: DOC-OTHER-PVO-MntRequirementWorkDefinitionExtractPVO
doc_type: system-doc
title: "MntRequirementWorkDefinitionExtractPVO — PVO Cross-Module"
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
  - MntRequirementWorkDefinitionExtractPVO
  - mntrequirementworkdefinitionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntRequirementWorkDefinitionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Requirement Work Definition Extract. Acessa as tabelas: MNT_WR_WORK_DEFINITIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntRequirementWorkDefinitionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_wr_work_definitions|MNT_WR_WORK_DEFINITIONS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[mnt_wr_work_definitions|MNT_WR_WORK_DEFINITIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DueAtCycleInterval | DUE_AT_CYCLE_INTERVAL | — | ✅ |
| 4 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | RepeatsInCycleFlag | REPEATS_IN_CYCLE_FLAG | — | ✅ |
| 12 | RequestId | REQUEST_ID | — | ✅ |
| 13 | RequirementId | REQUIREMENT_ID | — | ✅ |
| 14 | RequirementWdId | REQUIREMENT_WD_ID | 🔑 | ✅ |
| 15 | WorkDefinitionId | WORK_DEFINITION_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
