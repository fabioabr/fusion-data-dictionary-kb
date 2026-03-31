---
id: DOC-OTHER-PVO-OrchestrationGroupExtractPVO
doc_type: system-doc
title: "OrchestrationGroupExtractPVO — PVO Cross-Module"
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
  - OrchestrationGroupExtractPVO
  - orchestrationgroupextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrchestrationGroupExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Orchestration Group Extract. Acessa as tabelas: DOO_ORCHESTRATION_GROUPS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.DooBiccExtractAM.OrchestrationGroupExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 1 | 1 | 25 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]] — 25 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[doo_orchestration_groups|DOO_ORCHESTRATION_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrchestrationGroupCreatedBy | CREATED_BY | — | ✅ |
| 2 | OrchestrationGroupCreationDate | CREATION_DATE | — | ✅ |
| 3 | OrchestrationGroupDeltaType | DELTA_TYPE | — | ✅ |
| 4 | OrchestrationGroupDooProcessId | DOO_PROCESS_ID | — | ✅ |
| 5 | OrchestrationGroupDooProcessInstanceId | DOO_PROCESS_INSTANCE_ID | — | ✅ |
| 6 | OrchestrationGroupDooProcessVersion | DOO_PROCESS_VERSION | — | ✅ |
| 7 | OrchestrationGroupFulfillmentLineId | FULFILLMENT_LINE_ID | — | ✅ |
| 8 | OrchestrationGroupGroupCreatedBy | GROUP_CREATED_BY | — | ✅ |
| 9 | OrchestrationGroupGroupId | GROUP_ID | — | ✅ |
| 10 | OrchestrationGroupGroupSeqId | GROUP_SEQ_ID | 🔑 | ✅ |
| 11 | OrchestrationGroupGroupSetName | GROUP_SET_NAME | — | ✅ |
| 12 | OrchestrationGroupGroupSetType | GROUP_SET_TYPE | — | ✅ |
| 13 | OrchestrationGroupHeaderId | HEADER_ID | — | ✅ |
| 14 | OrchestrationGroupIsGroupEditable | IS_GROUP_EDITABLE | — | ✅ |
| 15 | OrchestrationGroupLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | OrchestrationGroupLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 17 | OrchestrationGroupLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 18 | OrchestrationGroupLineId | LINE_ID | — | ✅ |
| 19 | OrchestrationGroupObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 20 | OrchestrationGroupOrgId | ORG_ID | — | ✅ |
| 21 | OrchestrationGroupParentGroupId | PARENT_GROUP_ID | — | ✅ |
| 22 | OrchestrationGroupReferenceGroupId | REFERENCE_GROUP_ID | — | ✅ |
| 23 | OrchestrationGroupRootParentGroupId | ROOT_PARENT_GROUP_ID | — | ✅ |
| 24 | OrchestrationGroupSplitGroupFromId | SPLIT_GROUP_FROM_ID | — | ✅ |
| 25 | OrchestrationGroupStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
