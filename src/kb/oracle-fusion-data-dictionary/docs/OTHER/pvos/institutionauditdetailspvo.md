---
id: DOC-OTHER-PVO-InstitutionAuditDetailsPVO
doc_type: system-doc
title: "InstitutionAuditDetailsPVO — PVO Cross-Module"
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
  - InstitutionAuditDetailsPVO
  - institutionauditdetailspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionAuditDetailsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Audit Details. Acessa as tabelas: GMS_INSTN_AUDIT_DETAILS_VL, GMS_INSTN_AUDIT_TYPES, HZ_PARTIES.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionAuditDetailsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 3 | 1 | 9 | 47% |

---

## 🔗 Tabelas Relacionadas

- [[gms_instn_audit_details_vl|GMS_INSTN_AUDIT_DETAILS_VL]] — 15 atributos (1 PKs, 8 BICC)
- [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]] — 2 atributos
- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)

---

## ⚙️ Atributos

### [[gms_instn_audit_details_vl|GMS_INSTN_AUDIT_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Auditor | AUDITOR | — | ✅ |
| 2 | InstitutionAuditDetailsPEOCreatedBy | CREATED_BY | — | — |
| 3 | InstitutionAuditDetailsPEOCreationDate | CREATION_DATE | — | — |
| 4 | InstitutionAuditDetailsPEOEndDate | END_DATE | — | ✅ |
| 5 | InstitutionAuditDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InstitutionAuditDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InstitutionAuditDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InstitutionAuditDetailsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | InstitutionAuditDetailsPEOProgramCoverage | PROGRAM_COVERAGE | — | ✅ |
| 10 | InstitutionAuditDetailsPEOReportDate | REPORT_DATE | — | ✅ |
| 11 | InstitutionAuditDetailsPEOStartDate | START_DATE | — | ✅ |
| 12 | InstnAuditDetailId | INSTN_AUDIT_DETAIL_ID | 🔑 | ✅ |
| 13 | InstnAuditTypeId | INSTN_AUDIT_TYPE_ID | — | — |
| 14 | ReportNumber | REPORT_NUMBER | — | ✅ |
| 15 | SponsorId | SPONSOR_ID | — | — |

### [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionAuditTypesPEOInstitutionId | INSTITUTION_ID | — | — |
| 2 | InstitutionAuditTypesPEOInstnAuditTypeId | INSTN_AUDIT_TYPE_ID | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | — |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
