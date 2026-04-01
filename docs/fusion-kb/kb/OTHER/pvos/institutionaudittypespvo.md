---
id: DOC-OTHER-PVO-InstitutionAuditTypesPVO
doc_type: system-doc
title: "InstitutionAuditTypesPVO — PVO Cross-Module"
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
  - InstitutionAuditTypesPVO
  - institutionaudittypespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionAuditTypesPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Audit Types. Acessa as tabelas: GMS_INSTN_AUDIT_TYPES.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionAuditTypesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 3 | 33% |

---

## 🔗 Tabelas Relacionadas

- [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]] — 9 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionAuditTypesPEOAuditType | AUDIT_TYPE | — | ✅ |
| 2 | InstitutionAuditTypesPEOCreatedBy | CREATED_BY | — | — |
| 3 | InstitutionAuditTypesPEOCreationDate | CREATION_DATE | — | — |
| 4 | InstitutionAuditTypesPEOInstitutionId | INSTITUTION_ID | — | — |
| 5 | InstitutionAuditTypesPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InstitutionAuditTypesPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InstitutionAuditTypesPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InstitutionAuditTypesPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InstnAuditTypeId | INSTN_AUDIT_TYPE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
