---
id: DOC-HCM-PVO-BenefitEmployeeHabitsPVO
doc_type: system-doc
title: "BenefitEmployeeHabitsPVO — PVO Human Capital Management"
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
  - BenefitEmployeeHabitsPVO
  - benefitemployeehabitspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BenefitEmployeeHabitsPVO

## 📌 Visão Geral

Extrai habitos e coberturas de saude de colaboradores com vigencia e coordenacao medica. Suporta underwriting e gestao de planos de saude.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.BenefitEmployeeHabitsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 4 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[ben_per_le_habits_cov_f|BEN_PER_LE_HABITS_COV_F]] — 30 atributos (4 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[ben_per_le_habits_cov_f|BEN_PER_LE_HABITS_COV_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BusinessGroupId | BUSINESS_GROUP_ID | — | ✅ |
| 2 | CoordMedCvgEndDt | COORD_MED_CVG_END_DT | — | ✅ |
| 3 | CoordMedCvgStrtDt | COORD_MED_CVG_STRT_DT | — | ✅ |
| 4 | CoordMedExtEr | COORD_MED_EXT_ER | — | ✅ |
| 5 | CoordMedInsrCrrIdent | COORD_MED_INSR_CRR_IDENT | — | ✅ |
| 6 | CoordMedInsrCrrNam | COORD_MED_INSR_CRR_NAM | — | ✅ |
| 7 | CoordMedPlName | COORD_MED_PL_NAME | — | ✅ |
| 8 | CoordMedPlnNo | COORD_MED_PLN_NO | — | ✅ |
| 9 | CoordNoCvgFlag | COORD_NO_CVG_FLAG | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | ✅ |
| 11 | CreationDate | CREATION_DATE | — | ✅ |
| 12 | CvrdInAnthrPl | CVRD_IN_ANTHR_PL | — | ✅ |
| 13 | DisabilityStatus | DISABILITY_STATUS | — | ✅ |
| 14 | DpdntAdoptionDate | DPDNT_ADOPTION_DATE | — | ✅ |
| 15 | DpdntVlntrySvceFlag | DPDNT_VLNTRY_SVCE_FLAG | — | ✅ |
| 16 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 17 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | LeHabitsCovId | LE_HABITS_COV_ID | 🔑 | ✅ |
| 22 | LegalEntityId | LEGAL_ENTITY_ID | 🔑 | ✅ |
| 23 | LegislativeDataGroupId | LEGISLATIVE_DATA_GROUP_ID | — | ✅ |
| 24 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 25 | OnMilitaryService | ON_MILITARY_SERVICE | — | ✅ |
| 26 | PersonId | PERSON_ID | — | ✅ |
| 27 | ReceiptOfDeathCertDate | RECEIPT_OF_DEATH_CERT_DATE | — | ✅ |
| 28 | RegisteredDisabledFlag | REGISTERED_DISABLED_FLAG | — | ✅ |
| 29 | StudentStatus | STUDENT_STATUS | — | ✅ |
| 30 | TobaccoTypeUsage | TOBACCO_TYPE_USAGE | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
