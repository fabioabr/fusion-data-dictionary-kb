---
id: DOC-OTHER-PVO-GroupInclObjectsPVO
doc_type: system-doc
title: "GroupInclObjectsPVO — PVO Cross-Module"
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
  - GroupInclObjectsPVO
  - groupinclobjectspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupInclObjectsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Incl Objects. Acessa as tabelas: FND_VS_VALUE_SETS, HWM_GRPS_VL, HWM_GRP_INCL_OBJECTS_V (+1).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupInclObjectsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 4 | 1 | 14 | 67% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_vs_value_sets|FND_VS_VALUE_SETS]] — 3 atributos (1 BICC)
- [[hwm_grps_vl|HWM_GRPS_VL]] — 2 atributos (1 BICC)
- [[hwm_grp_incl_objects_v|HWM_GRP_INCL_OBJECTS_V]] — 11 atributos (1 PKs, 10 BICC)
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 5 atributos (2 BICC)

---

## ⚙️ Atributos

### [[fnd_vs_value_sets|FND_VS_VALUE_SETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ValueSetsBPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 2 | ValueSetsBPEOValueSetCode | VALUE_SET_CODE | — | ✅ |
| 3 | ValueSetsBPEOValueSetId | VALUE_SET_ID | — | — |

### [[hwm_grps_vl|HWM_GRPS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupsVLPEOGroupName | GROUP_NAME | — | ✅ |
| 2 | GroupsVLPEOGrpId | GRP_ID | — | — |

### [[hwm_grp_incl_objects_v|HWM_GRP_INCL_OBJECTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupInclObjectsPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GroupInclObjectsPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GroupInclObjectsPEOGrpId | GRP_ID | — | — |
| 4 | GroupInclObjectsPEOGrpInclObjectId | GRP_INCL_OBJECT_ID | 🔑 | ✅ |
| 5 | GroupInclObjectsPEOInclFlag | INCL_FLAG | — | ✅ |
| 6 | GroupInclObjectsPEOInclObjectId | INCL_OBJECT_ID | — | ✅ |
| 7 | GroupInclObjectsPEOInclObjectTypeCode | INCL_OBJECT_TYPE_CODE | — | ✅ |
| 8 | GroupInclObjectsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GroupInclObjectsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | GroupInclObjectsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | GroupInclObjectsPEOOrderNum | ORDER_NUM | — | ✅ |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 2 | PersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 3 | PersonNamePEOFullName | FULL_NAME | — | ✅ |
| 4 | PersonNamePEOPersonId | PERSON_ID | — | — |
| 5 | PersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
