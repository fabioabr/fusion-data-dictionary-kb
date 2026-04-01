---
id: DOC-OTHER-PVO-ProfileTypePVO
doc_type: system-doc
title: "ProfileTypePVO — PVO Cross-Module"
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
  - ProfileTypePVO
  - profiletypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileTypePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Profile Type. Acessa as tabelas: HRT_PROFILE_TYPES_B, HRT_PROFILE_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmProfileSetupAM.ProfileTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 3 | 18 | 82% |

---

## 🔗 Tabelas Relacionadas

- [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]] — 15 atributos (2 PKs, 12 BICC)
- [[hrt_profile_types_tl|HRT_PROFILE_TYPES_TL]] — 7 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hrt_profile_types_b|HRT_PROFILE_TYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | ProfileTypeBPEOBusinessGroupId | BUSINESS_GROUP_ID | 🔑 | ✅ |
| 8 | ProfileTypeBPEODateFrom | DATE_FROM | — | ✅ |
| 9 | ProfileTypeBPEODateTo | DATE_TO | — | ✅ |
| 10 | ProfileTypeBPEOModuleId | MODULE_ID | — | — |
| 11 | ProfileTypeBPEOPidApprovalFlag | PID_APPROVAL_FLAG | — | ✅ |
| 12 | ProfileTypeBPEOProfileStatusCode | PROFILE_STATUS_CODE | — | ✅ |
| 13 | ProfileTypeBPEOProfileTypeCode | PROFILE_TYPE_CODE | — | ✅ |
| 14 | ProfileTypeBPEOProfileTypeId | PROFILE_TYPE_ID | 🔑 | ✅ |
| 15 | ProfileTypeBPEOProfileUsageCode | PROFILE_USAGE_CODE | — | ✅ |

### [[hrt_profile_types_tl|HRT_PROFILE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ProfileTypeTranslationPEOBusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | ProfileTypeTranslationPEODescription | DESCRIPTION | — | ✅ |
| 4 | ProfileTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | ProfileTypeTranslationPEOProfileTypeId | PROFILE_TYPE_ID | — | ✅ |
| 6 | ProfileTypeTranslationPEOSummary | SUMMARY | — | ✅ |
| 7 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
