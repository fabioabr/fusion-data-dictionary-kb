---
id: DOC-OTHER-PVO-LifeEventPVO
doc_type: system-doc
title: "LifeEventPVO — PVO Cross-Module"
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
  - LifeEventPVO
  - lifeeventpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LifeEventPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Life Event. Acessa as tabelas: BEN_LER_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.LifeEventPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 66 | 1 | 3 | 11 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[ben_ler_f|BEN_LER_F]] — 66 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[ben_ler_f|BEN_LER_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 2 | CkRltdPerEligFlag | CK_RLTD_PER_ELIG_FLAG | — | — |
| 3 | CmAplyFlag | CM_APLY_FLAG | — | — |
| 4 | ConfigChar1 | CONFIG_CHAR_1 | — | — |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DescTxt | DESC_TXT | — | ✅ |
| 8 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 9 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 10 | GlobalFlag | GLOBAL_FLAG | — | — |
| 11 | InstructionText | INSTRUCTION_TEXT | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | LerAttribute1 | LER_ATTRIBUTE1 | — | — |
| 16 | LerAttribute10 | LER_ATTRIBUTE10 | — | — |
| 17 | LerAttribute11 | LER_ATTRIBUTE11 | — | — |
| 18 | LerAttribute12 | LER_ATTRIBUTE12 | — | — |
| 19 | LerAttribute13 | LER_ATTRIBUTE13 | — | — |
| 20 | LerAttribute14 | LER_ATTRIBUTE14 | — | — |
| 21 | LerAttribute15 | LER_ATTRIBUTE15 | — | — |
| 22 | LerAttribute16 | LER_ATTRIBUTE16 | — | — |
| 23 | LerAttribute17 | LER_ATTRIBUTE17 | — | — |
| 24 | LerAttribute18 | LER_ATTRIBUTE18 | — | — |
| 25 | LerAttribute19 | LER_ATTRIBUTE19 | — | — |
| 26 | LerAttribute2 | LER_ATTRIBUTE2 | — | — |
| 27 | LerAttribute20 | LER_ATTRIBUTE20 | — | — |
| 28 | LerAttribute21 | LER_ATTRIBUTE21 | — | — |
| 29 | LerAttribute22 | LER_ATTRIBUTE22 | — | — |
| 30 | LerAttribute23 | LER_ATTRIBUTE23 | — | — |
| 31 | LerAttribute24 | LER_ATTRIBUTE24 | — | — |
| 32 | LerAttribute25 | LER_ATTRIBUTE25 | — | — |
| 33 | LerAttribute26 | LER_ATTRIBUTE26 | — | — |
| 34 | LerAttribute27 | LER_ATTRIBUTE27 | — | — |
| 35 | LerAttribute28 | LER_ATTRIBUTE28 | — | — |
| 36 | LerAttribute29 | LER_ATTRIBUTE29 | — | — |
| 37 | LerAttribute3 | LER_ATTRIBUTE3 | — | — |
| 38 | LerAttribute30 | LER_ATTRIBUTE30 | — | — |
| 39 | LerAttribute4 | LER_ATTRIBUTE4 | — | — |
| 40 | LerAttribute5 | LER_ATTRIBUTE5 | — | — |
| 41 | LerAttribute6 | LER_ATTRIBUTE6 | — | — |
| 42 | LerAttribute7 | LER_ATTRIBUTE7 | — | — |
| 43 | LerAttribute8 | LER_ATTRIBUTE8 | — | — |
| 44 | LerAttribute9 | LER_ATTRIBUTE9 | — | — |
| 45 | LerAttributeCategory | LER_ATTRIBUTE_CATEGORY | — | — |
| 46 | LerEvalRl | LER_EVAL_RL | — | — |
| 47 | LerId | LER_ID | 🔑 | ✅ |
| 48 | LerStatCd | LER_STAT_CD | — | — |
| 49 | LfEvtOperCd | LF_EVT_OPER_CD | — | — |
| 50 | Name | NAME | — | ✅ |
| 51 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 52 | OcrdDtDetCd | OCRD_DT_DET_CD | — | — |
| 53 | OvridgLeFlag | OVRIDG_LE_FLAG | — | ✅ |
| 54 | ProdCd | PROD_CD | — | — |
| 55 | PtnlLerTrtmtCd | PTNL_LER_TRTMT_CD | — | — |
| 56 | QualgEvtFlag | QUALG_EVT_FLAG | — | — |
| 57 | SelfAssignedEventFlag | SELF_ASSIGNED_EVENT_FLAG | — | — |
| 58 | ShortCode | SHORT_CODE | — | — |
| 59 | ShortName | SHORT_NAME | — | — |
| 60 | SlctblSlfSvcCd | SLCTBL_SLF_SVC_CD | — | — |
| 61 | TmlnsDysNum | TMLNS_DYS_NUM | — | — |
| 62 | TmlnsEvalCd | TMLNS_EVAL_CD | — | — |
| 63 | TmlnsPerdCd | TMLNS_PERD_CD | — | — |
| 64 | TmlnsPerdRl | TMLNS_PERD_RL | — | — |
| 65 | TypCd | TYP_CD | — | — |
| 66 | WhnToPrcsCd | WHN_TO_PRCS_CD | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
