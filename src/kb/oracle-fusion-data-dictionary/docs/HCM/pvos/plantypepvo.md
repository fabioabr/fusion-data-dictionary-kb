---
id: DOC-HCM-PVO-PlanTypePVO
doc_type: system-doc
title: "PlanTypePVO — PVO Human Capital Management"
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
  - PlanTypePVO
  - plantypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PlanTypePVO

## 📌 Visão Geral

Extrai os tipos de plano de benefícios (médico, dental, vida, etc.) com vigência e nome da operadora. Dimensão de referência para categorização dos programas de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.PlanTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 1 | 3 | 21 | 36% |

---

## 🔗 Tabelas Relacionadas

- [[ben_pl_typ_f|BEN_PL_TYP_F]] — 59 atributos (3 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[ben_pl_typ_f|BEN_PL_TYP_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AdminCategoryCd | ADMIN_CATEGORY_CD | — | — |
| 2 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 3 | CarrierPlanTypeName | CARRIER_PLAN_TYPE_NAME | — | ✅ |
| 4 | CompTypCd | COMP_TYP_CD | — | — |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | GlobalFlag | GLOBAL_FLAG | — | ✅ |
| 10 | IvrIdent | IVR_IDENT | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 15 | LegislationSubgroup | LEGISLATION_SUBGROUP | — | ✅ |
| 16 | MnEnrlRqdNum | MN_ENRL_RQD_NUM | — | ✅ |
| 17 | MxEnrlAlwdNum | MX_ENRL_ALWD_NUM | — | ✅ |
| 18 | Name | NAME | — | ✅ |
| 19 | NoMnEnrlNumDfndFlag | NO_MN_ENRL_NUM_DFND_FLAG | — | ✅ |
| 20 | NoMxEnrlNumDfndFlag | NO_MX_ENRL_NUM_DFND_FLAG | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 22 | OptDsplyFmtCd | OPT_DSPLY_FMT_CD | — | — |
| 23 | OptTypCd | OPT_TYP_CD | — | ✅ |
| 24 | PlTypId | PL_TYP_ID | 🔑 | ✅ |
| 25 | PlTypStatCd | PL_TYP_STAT_CD | — | ✅ |
| 26 | PtpAttribute1 | PTP_ATTRIBUTE1 | — | — |
| 27 | PtpAttribute10 | PTP_ATTRIBUTE10 | — | — |
| 28 | PtpAttribute11 | PTP_ATTRIBUTE11 | — | — |
| 29 | PtpAttribute12 | PTP_ATTRIBUTE12 | — | — |
| 30 | PtpAttribute13 | PTP_ATTRIBUTE13 | — | — |
| 31 | PtpAttribute14 | PTP_ATTRIBUTE14 | — | — |
| 32 | PtpAttribute15 | PTP_ATTRIBUTE15 | — | — |
| 33 | PtpAttribute16 | PTP_ATTRIBUTE16 | — | — |
| 34 | PtpAttribute17 | PTP_ATTRIBUTE17 | — | — |
| 35 | PtpAttribute18 | PTP_ATTRIBUTE18 | — | — |
| 36 | PtpAttribute19 | PTP_ATTRIBUTE19 | — | — |
| 37 | PtpAttribute2 | PTP_ATTRIBUTE2 | — | — |
| 38 | PtpAttribute20 | PTP_ATTRIBUTE20 | — | — |
| 39 | PtpAttribute21 | PTP_ATTRIBUTE21 | — | — |
| 40 | PtpAttribute22 | PTP_ATTRIBUTE22 | — | — |
| 41 | PtpAttribute23 | PTP_ATTRIBUTE23 | — | — |
| 42 | PtpAttribute24 | PTP_ATTRIBUTE24 | — | — |
| 43 | PtpAttribute25 | PTP_ATTRIBUTE25 | — | — |
| 44 | PtpAttribute26 | PTP_ATTRIBUTE26 | — | — |
| 45 | PtpAttribute27 | PTP_ATTRIBUTE27 | — | — |
| 46 | PtpAttribute28 | PTP_ATTRIBUTE28 | — | — |
| 47 | PtpAttribute29 | PTP_ATTRIBUTE29 | — | — |
| 48 | PtpAttribute3 | PTP_ATTRIBUTE3 | — | — |
| 49 | PtpAttribute30 | PTP_ATTRIBUTE30 | — | — |
| 50 | PtpAttribute4 | PTP_ATTRIBUTE4 | — | — |
| 51 | PtpAttribute5 | PTP_ATTRIBUTE5 | — | — |
| 52 | PtpAttribute6 | PTP_ATTRIBUTE6 | — | — |
| 53 | PtpAttribute7 | PTP_ATTRIBUTE7 | — | — |
| 54 | PtpAttribute8 | PTP_ATTRIBUTE8 | — | — |
| 55 | PtpAttribute9 | PTP_ATTRIBUTE9 | — | — |
| 56 | PtpAttributeCategory | PTP_ATTRIBUTE_CATEGORY | — | ✅ |
| 57 | ShortCode | SHORT_CODE | — | — |
| 58 | ShortName | SHORT_NAME | — | — |
| 59 | SsCategoryCd | SS_CATEGORY_CD | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
