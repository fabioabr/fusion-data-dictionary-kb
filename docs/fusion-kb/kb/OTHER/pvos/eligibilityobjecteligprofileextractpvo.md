---
id: DOC-OTHER-PVO-EligibilityObjectEligProfileExtractPVO
doc_type: system-doc
title: "EligibilityObjectEligProfileExtractPVO — PVO Cross-Module"
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
  - EligibilityObjectEligProfileExtractPVO
  - eligibilityobjecteligprofileextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EligibilityObjectEligProfileExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Eligibility Object Elig Profile Extract. Acessa as tabelas: BEN_ELIG_OBJ_ELIG_PROFL_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.BenefitsBiccExtractAM.EligibilityObjectEligProfileExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_elig_obj_elig_profl_f|BEN_ELIG_OBJ_ELIG_PROFL_F]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[ben_elig_obj_elig_profl_f|BEN_ELIG_OBJ_ELIG_PROFL_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 5 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 6 | EligObjEligPrflId | ELIG_OBJ_ELIG_PRFL_ID | 🔑 | ✅ |
| 7 | EligObjId | ELIG_OBJ_ID | — | ✅ |
| 8 | EligPrflId | ELIG_PRFL_ID | — | ✅ |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | MndtryFlag | MNDTRY_FLAG | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
