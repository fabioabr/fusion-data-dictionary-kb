---
id: DOC-OTHER-PVO-GroupsPVO
doc_type: system-doc
title: "GroupsPVO — PVO Cross-Module"
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
  - GroupsPVO
  - groupspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Groups. Acessa as tabelas: HWM_GRPS_B, HWM_GRPS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GroupsAM.GroupsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 35 | 2 | 2 | 35 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_grps_b|HWM_GRPS_B]] — 23 atributos (1 PKs, 23 BICC)
- [[hwm_grps_tl|HWM_GRPS_TL]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[hwm_grps_b|HWM_GRPS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupsPEOApplUsgCd | APPL_USG_CD | — | ✅ |
| 2 | GroupsPEOAppliesToCd | APPLIES_TO_CD | — | ✅ |
| 3 | GroupsPEOAssignmentToUseCd | ASSIGNMENT_TO_USE_CD | — | ✅ |
| 4 | GroupsPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | GroupsPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | GroupsPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 7 | GroupsPEOEvalStatusCd | EVAL_STATUS_CD | — | ✅ |
| 8 | GroupsPEOFreezeFlag | FREEZE_FLAG | — | ✅ |
| 9 | GroupsPEOGroupCode | GRP_CODE | — | ✅ |
| 10 | GroupsPEOGroupId | GRP_ID | 🔑 | ✅ |
| 11 | GroupsPEOLastRefreshDt | LAST_REFRESH_DT | — | ✅ |
| 12 | GroupsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | GroupsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | GroupsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | GroupsPEOMassEvalFlag | MASS_EVAL_FLAG | — | ✅ |
| 16 | GroupsPEOMemTypeCd | MEM_TYPE_CD | — | ✅ |
| 17 | GroupsPEOModuleId | MODULE_ID | — | ✅ |
| 18 | GroupsPEONextRefreshDt | NEXT_REFRESH_DT | — | ✅ |
| 19 | GroupsPEONumberDaysNext | NUM_DAYS_NEXT | — | ✅ |
| 20 | GroupsPEONumberDaysPrev | NUM_DAYS_PREV | — | ✅ |
| 21 | GroupsPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | GroupsPEOOnlineEvaluateFlag | ONLINE_EVAL_FLAG | — | ✅ |
| 23 | GroupsPEORunType | RUN_TYPE | — | ✅ |

### [[hwm_grps_tl|HWM_GRPS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GroupsTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | GroupsTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | GroupsTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | GroupsTranslationPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 5 | GroupsTranslationPEOGroupId | GRP_ID | — | ✅ |
| 6 | GroupsTranslationPEOGroupName | GROUP_NAME | — | ✅ |
| 7 | GroupsTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 8 | GroupsTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | GroupsTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | GroupsTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | GroupsTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | GroupsTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
