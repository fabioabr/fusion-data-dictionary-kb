---
id: DOC-OTHER-PVO-WorkRequirementConditionEventPVO
doc_type: system-doc
title: "WorkRequirementConditionEventPVO — PVO Cross-Module"
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
  - WorkRequirementConditionEventPVO
  - workrequirementconditioneventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkRequirementConditionEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Requirement Condition Event. Acessa as tabelas: MNT_WR_CONDITION_EVENTS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.WorkRequirementConditionEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 1 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_wr_condition_events|MNT_WR_CONDITION_EVENTS]] — 13 atributos (1 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[mnt_wr_condition_events|MNT_WR_CONDITION_EVENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConditionEventCodeId | CONDITION_EVENT_CODE_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 5 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 11 | RequestId | REQUEST_ID | — | ✅ |
| 12 | RequirementConditionEventId | REQUIREMENT_CONDITION_EVENT_ID | 🔑 | ✅ |
| 13 | RequirementId | REQUIREMENT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
