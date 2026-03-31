---
id: DOC-OTHER-PVO-ChangeAuditRedlineAttrExtractPVO
doc_type: system-doc
title: "ChangeAuditRedlineAttrExtractPVO — PVO Cross-Module"
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
  - ChangeAuditRedlineAttrExtractPVO
  - changeauditredlineattrextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ChangeAuditRedlineAttrExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Change Audit Redline Attr Extract. Acessa as tabelas: EGO_CHANGE_AUDIT_REDLINE_ATTRS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.EgoBiccExtractAM.ChangeAuditRedlineAttrExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ego_change_audit_redline_attrs|EGO_CHANGE_AUDIT_REDLINE_ATTRS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[ego_change_audit_redline_attrs|EGO_CHANGE_AUDIT_REDLINE_ATTRS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChangeAuditRedlineAttrPEOAttrDisplayName | ATTR_DISPLAY_NAME | — | ✅ |
| 2 | ChangeAuditRedlineAttrPEOAttrName | ATTR_NAME | — | ✅ |
| 3 | ChangeAuditRedlineAttrPEOAttrNewCode | ATTR_NEW_CODE | — | ✅ |
| 4 | ChangeAuditRedlineAttrPEOAttrNewValue | ATTR_NEW_VALUE | — | ✅ |
| 5 | ChangeAuditRedlineAttrPEOAttrOldCode | ATTR_OLD_CODE | — | ✅ |
| 6 | ChangeAuditRedlineAttrPEOAttrOldValue | ATTR_OLD_VALUE | — | ✅ |
| 7 | ChangeAuditRedlineAttrPEOAuditEntityAttrId | AUDIT_ENTITY_ATTR_ID | 🔑 | ✅ |
| 8 | ChangeAuditRedlineAttrPEOAuditEntityId | AUDIT_ENTITY_ID | — | ✅ |
| 9 | ChangeAuditRedlineAttrPEOCreatedBy | CREATED_BY | — | ✅ |
| 10 | ChangeAuditRedlineAttrPEOCreationDate | CREATION_DATE | — | ✅ |
| 11 | ChangeAuditRedlineAttrPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | ChangeAuditRedlineAttrPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | ChangeAuditRedlineAttrPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | ChangeAuditRedlineAttrPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
