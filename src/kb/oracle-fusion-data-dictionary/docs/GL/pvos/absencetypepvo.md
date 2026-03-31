---
id: DOC-GL-PVO-AbsenceTypePVO
doc_type: system-doc
title: "AbsenceTypePVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AbsenceTypePVO
  - absencetypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence Type. Acessa as tabelas: ANC_ABSENCE_TYPES_F, ANC_ABSENCE_TYPES_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsenceTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 53 | 2 | 5 | 43 | 81% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_types_f|ANC_ABSENCE_TYPES_F]] — 38 atributos (2 PKs, 32 BICC)
- [[anc_absence_types_f_tl|ANC_ABSENCE_TYPES_F_TL]] — 15 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[anc_absence_types_f|ANC_ABSENCE_TYPES_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceTypeId | ABSENCE_TYPE_ID | 🔑 | ✅ |
| 2 | AdminAllowUpdatesCd | ADMIN_ALLOW_UPDATES_CD | — | ✅ |
| 3 | AncAbsenceTypesFAltcd | ANC_ABSENCE_TYPES_F_ALTCD | — | — |
| 4 | ChildEventTypeCd | CHILD_EVENT_TYPE_CD | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DurationUomCd | DURATION_UOM_CD | — | ✅ |
| 8 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 9 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | EmpAllowUpdatesCd | EMP_ALLOW_UPDATES_CD | — | ✅ |
| 11 | EmpLockIfConfirmCd | EMP_LOCK_IF_CONFIRM_CD | — | ✅ |
| 12 | EnterpriseId | ENTERPRISE_ID | — | — |
| 13 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 14 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 16 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 17 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | — |
| 18 | LinkageDuration | LINKAGE_DURATION | — | ✅ |
| 19 | LinkageReasonCd | LINKAGE_REASON_CD | — | ✅ |
| 20 | LinkageRuleCd | LINKAGE_RULE_CD | — | ✅ |
| 21 | LinkageUomCd | LINKAGE_UOM_CD | — | ✅ |
| 22 | ManagementTypeCd | MANAGEMENT_TYPE_CD | — | ✅ |
| 23 | MapEventTypeCd | MAP_EVENT_TYPE_CD | — | ✅ |
| 24 | MaxDuration | MAX_DURATION | — | ✅ |
| 25 | MaxDurationRuleCd | MAX_DURATION_RULE_CD | — | ✅ |
| 26 | MgrAllowUpdatesCd | MGR_ALLOW_UPDATES_CD | — | ✅ |
| 27 | MgrLockIfConfirmCd | MGR_LOCK_IF_CONFIRM_CD | — | ✅ |
| 28 | MinDuration | MIN_DURATION | — | ✅ |
| 29 | MinDurationRuleCd | MIN_DURATION_RULE_CD | — | ✅ |
| 30 | ModuleId | MODULE_ID | — | — |
| 31 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 32 | PartialDay | PARTIAL_DAY | — | ✅ |
| 33 | PartialDayFormulaId | PARTIAL_DAY_FORMULA_ID | — | ✅ |
| 34 | PatternCD | PATTERN_CD | — | ✅ |
| 35 | SplCondition | SPL_CONDITION | — | ✅ |
| 36 | Status | STATUS | — | ✅ |
| 37 | TimecardAvailFlag | TIMECARD_AVAIL_FLAG | — | ✅ |
| 38 | TimekeeperAvailFlag | TIMEKEEPER_AVAIL_FLAG | — | ✅ |

### [[anc_absence_types_f_tl|ANC_ABSENCE_TYPES_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceTypeId1 | ABSENCE_TYPE_ID | 🔑 | ✅ |
| 2 | CreatedBy1 | CREATED_BY | — | ✅ |
| 3 | CreationDate1 | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 12 | ModuleId1 | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
