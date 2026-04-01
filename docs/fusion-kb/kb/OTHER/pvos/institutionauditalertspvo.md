---
id: DOC-OTHER-PVO-InstitutionAuditAlertsPVO
doc_type: system-doc
title: "InstitutionAuditAlertsPVO — PVO Cross-Module"
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
  - InstitutionAuditAlertsPVO
  - institutionauditalertspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionAuditAlertsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Audit Alerts. Acessa as tabelas: GMS_INSTN_AUDIT_ALERTS_VL, GMS_INSTN_AUDIT_DETAILS_VL, GMS_INSTN_AUDIT_TYPES (+2).

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionAuditAlertsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 5 | 1 | 7 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[gms_instn_audit_alerts_vl|GMS_INSTN_AUDIT_ALERTS_VL]] — 11 atributos (1 PKs, 4 BICC)
- [[gms_instn_audit_details_vl|GMS_INSTN_AUDIT_DETAILS_VL]] — 2 atributos
- [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]] — 2 atributos
- [[per_all_people_f|PER_ALL_PEOPLE_F]] — 3 atributos (1 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[gms_instn_audit_alerts_vl|GMS_INSTN_AUDIT_ALERTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionAuditAlertsPEOAlertNumber | ALERT_NUMBER | — | ✅ |
| 2 | InstitutionAuditAlertsPEOCreatedBy | CREATED_BY | — | — |
| 3 | InstitutionAuditAlertsPEOCreationDate | CREATION_DATE | — | — |
| 4 | InstitutionAuditAlertsPEODescription | DESCRIPTION | — | ✅ |
| 5 | InstitutionAuditAlertsPEOInstnAuditDetailId | INSTN_AUDIT_DETAIL_ID | — | — |
| 6 | InstitutionAuditAlertsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InstitutionAuditAlertsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InstitutionAuditAlertsPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InstitutionAuditAlertsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InstitutionAuditAlertsPEOResolutionOfficialId | RESOLUTION_OFFICIAL_ID | — | — |
| 11 | InstnAuditAlertId | INSTN_AUDIT_ALERT_ID | 🔑 | ✅ |

### [[gms_instn_audit_details_vl|GMS_INSTN_AUDIT_DETAILS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionAuditDetailsPEOInstnAuditDetailId | INSTN_AUDIT_DETAIL_ID | — | — |
| 2 | InstitutionAuditDetailsPEOInstnAuditTypeId | INSTN_AUDIT_TYPE_ID | — | — |

### [[gms_instn_audit_types|GMS_INSTN_AUDIT_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionAuditTypesPEOInstitutionId | INSTITUTION_ID | — | — |
| 2 | InstitutionAuditTypesPEOInstnAuditTypeId | INSTN_AUDIT_TYPE_ID | — | — |

### [[per_all_people_f|PER_ALL_PEOPLE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonDPEOPersonId | PERSON_ID | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuditResolutionOfficialName | DISPLAY_NAME | — | ✅ |
| 2 | PersonNameDPEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonNameDPEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 4 | PersonNameDPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 5 | PersonNameDPEOPersonId | PERSON_ID | — | — |
| 6 | PersonNameDPEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
