---
id: DOC-OTHER-PVO-ChangeAuditEntitiesExtractPVO
doc_type: system-doc
title: "ChangeAuditEntitiesExtractPVO — PVO Cross-Module"
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
  - ChangeAuditEntitiesExtractPVO
  - changeauditentitiesextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeAuditEntitiesExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Audit Entities Extract. Acessa as tabelas: EGO_CHANGE_AUDIT_ENTITIES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeAuditEntitiesExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 38 | 1 | 1 | 38 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_audit_entities|EGO_CHANGE_AUDIT_ENTITIES]] — 38 atributos (1 PKs, 38 BICC)

---

## ⚙️ Atributos

### [[ego_change_audit_entities|EGO_CHANGE_AUDIT_ENTITIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeAuditEntitiesPEOActionType | ACTION_TYPE | — | ✅ |
| 2 | ChangeAuditEntitiesPEOActionTypeValue | ACTION_TYPE_VALUE | — | ✅ |
| 3 | ChangeAuditEntitiesPEOAffectedObjName | AFFECTED_OBJ_NAME | — | ✅ |
| 4 | ChangeAuditEntitiesPEOAffectedObjPk1 | AFFECTED_OBJ_PK1 | — | ✅ |
| 5 | ChangeAuditEntitiesPEOAffectedObjPk2 | AFFECTED_OBJ_PK2 | — | ✅ |
| 6 | ChangeAuditEntitiesPEOAffectedObjPk3 | AFFECTED_OBJ_PK3 | — | ✅ |
| 7 | ChangeAuditEntitiesPEOAffectedObjPk4 | AFFECTED_OBJ_PK4 | — | ✅ |
| 8 | ChangeAuditEntitiesPEOAffectedObjPk5 | AFFECTED_OBJ_PK5 | — | ✅ |
| 9 | ChangeAuditEntitiesPEOAffectedObjSeq | AFFECTED_OBJ_SEQ | — | ✅ |
| 10 | ChangeAuditEntitiesPEOAuditEntityId | AUDIT_ENTITY_ID | 🔑 | ✅ |
| 11 | ChangeAuditEntitiesPEOAuditType | AUDIT_TYPE | — | ✅ |
| 12 | ChangeAuditEntitiesPEOAuthorDatetime | AUTHOR_DATETIME | — | ✅ |
| 13 | ChangeAuditEntitiesPEOAuthorId | AUTHOR_ID | — | ✅ |
| 14 | ChangeAuditEntitiesPEOAuthorName | AUTHOR_NAME | — | ✅ |
| 15 | ChangeAuditEntitiesPEOChangeId | CHANGE_ID | — | ✅ |
| 16 | ChangeAuditEntitiesPEOChangeLineId | CHANGE_LINE_ID | — | ✅ |
| 17 | ChangeAuditEntitiesPEOCoStatusCode | CO_STATUS_CODE | — | ✅ |
| 18 | ChangeAuditEntitiesPEOCoStatusValue | CO_STATUS_VALUE | — | ✅ |
| 19 | ChangeAuditEntitiesPEOComments | COMMENTS | — | ✅ |
| 20 | ChangeAuditEntitiesPEOCreatedBy | CREATED_BY | — | ✅ |
| 21 | ChangeAuditEntitiesPEOCreationDate | CREATION_DATE | — | ✅ |
| 22 | ChangeAuditEntitiesPEOEntityCode | ENTITY_CODE | — | ✅ |
| 23 | ChangeAuditEntitiesPEOEntityName | ENTITY_NAME | — | ✅ |
| 24 | ChangeAuditEntitiesPEOEntityType | ENTITY_TYPE | — | ✅ |
| 25 | ChangeAuditEntitiesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 26 | ChangeAuditEntitiesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 27 | ChangeAuditEntitiesPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 28 | ChangeAuditEntitiesPEOMigratedFlag | MIGRATED_FLAG | — | ✅ |
| 29 | ChangeAuditEntitiesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 30 | ChangeAuditEntitiesPEOPk1Value | PK1_VALUE | — | ✅ |
| 31 | ChangeAuditEntitiesPEOPk2Value | PK2_VALUE | — | ✅ |
| 32 | ChangeAuditEntitiesPEOPk3Value | PK3_VALUE | — | ✅ |
| 33 | ChangeAuditEntitiesPEOPk4Value | PK4_VALUE | — | ✅ |
| 34 | ChangeAuditEntitiesPEOPk5Value | PK5_VALUE | — | ✅ |
| 35 | ChangeAuditEntitiesPEOSubActionType | SUB_ACTION_TYPE | — | ✅ |
| 36 | ChangeAuditEntitiesPEOSubActionTypeValue | SUB_ACTION_TYPE_VALUE | — | ✅ |
| 37 | ChangeAuditEntitiesPEOSubEntityCode | SUB_ENTITY_CODE | — | ✅ |
| 38 | ChangeAuditEntitiesPEOSubEntityName | SUB_ENTITY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
