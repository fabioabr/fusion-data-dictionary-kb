---
id: DOC-HCM-PVO-OrgUnitClassificationPVO
doc_type: system-doc
title: "OrgUnitClassificationPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - OrgUnitClassificationPVO
  - orgunitclassificationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OrgUnitClassificationPVO

## 📌 Visão Geral

Extrai classificações de unidades organizacionais (department, legal entity, business unit) com vigência. Define a tipologia funcional de cada organização no Oracle Fusion HCM.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.OrganizationAM.OrgUnitClassificationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 4 | 3 | 20 | 83% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_setid_sets_vl|FND_SETID_SETS_VL]] — 4 atributos (4 BICC)
- [[hr_org_classifications|HR_ORG_CLASSIFICATIONS]] — 1 atributos
- [[hr_org_classifications_tl|HR_ORG_CLASSIFICATIONS_TL]] — 3 atributos
- [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]] — 16 atributos (3 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[fnd_setid_sets_vl|FND_SETID_SETS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SetIdSetPEODescription | DESCRIPTION | — | ✅ |
| 2 | SetIdSetPEOSetCode | SET_CODE | — | ✅ |
| 3 | SetIdSetPEOSetId | SET_ID | — | ✅ |
| 4 | SetIdSetPEOSetName | SET_NAME | — | ✅ |

### [[hr_org_classifications|HR_ORG_CLASSIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgClassificationPEOClassificationCode | CLASSIFICATION_CODE | — | — |

### [[hr_org_classifications_tl|HR_ORG_CLASSIFICATIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgClassificationTLPEOClassificationCode | CLASSIFICATION_CODE | — | — |
| 2 | OrgClassificationTLPEOClassificationName | CLASSIFICATION_NAME | — | — |
| 3 | OrgClassificationTLPEOLanguage | LANGUAGE | — | — |

### [[hr_org_unit_classifications_f|HR_ORG_UNIT_CLASSIFICATIONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 2 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 3 | OrgUnitClassificationId | ORG_UNIT_CLASSIFICATION_ID | 🔑 | ✅ |
| 4 | OrgUnitClassificationPEOActionOccurrenceId | ACTION_OCCURRENCE_ID | — | ✅ |
| 5 | OrgUnitClassificationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 6 | OrgUnitClassificationPEOClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 7 | OrgUnitClassificationPEOCreatedBy | CREATED_BY | — | ✅ |
| 8 | OrgUnitClassificationPEOCreationDate | CREATION_DATE | — | ✅ |
| 9 | OrgUnitClassificationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | OrgUnitClassificationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | OrgUnitClassificationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | OrgUnitClassificationPEOLegislationCode | LEGISLATION_CODE | — | ✅ |
| 13 | OrgUnitClassificationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | OrgUnitClassificationPEOOrganizationId | ORGANIZATION_ID | — | ✅ |
| 15 | OrgUnitClassificationPEOSetId | SET_ID | — | ✅ |
| 16 | OrgUnitClassificationPEOStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
