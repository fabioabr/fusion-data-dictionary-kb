---
id: DOC-HCM-PVO-PersonEnrollmentActionPVO
doc_type: system-doc
title: "PersonEnrollmentActionPVO — PVO Human Capital Management"
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
  - PersonEnrollmentActionPVO
  - personenrollmentactionpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonEnrollmentActionPVO

## 📌 Visão Geral

Extrai as ações de inscrição em planos de benefícios dos colaboradores, incluindo tipo de ação, nível e data de conclusão. Suporta auditoria do ciclo de enrollment de benefícios.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmBenefitsAM.PersonEnrollmentActionPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 98 | 2 | 1 | 12 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[ben_prtt_enrt_actn|BEN_PRTT_ENRT_ACTN]] — 91 atributos (1 PKs, 12 BICC)
- [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]] — 7 atributos

---

## ⚙️ Atributos

### [[ben_prtt_enrt_actn|BEN_PRTT_ENRT_ACTN]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActnTypId | ACTN_TYP_ID | — | ✅ |
| 2 | ActnTypLvlCd | ACTN_TYP_LVL_CD | — | ✅ |
| 3 | BusinessGroupId | BUSINESS_GROUP_ID | — | — |
| 4 | CmpltdDt | CMPLTD_DT | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DueDt | DUE_DT | — | ✅ |
| 8 | EligCvrdDpntId | ELIG_CVRD_DPNT_ID | — | — |
| 9 | EndedPerInLerId | ENDED_PER_IN_LER_ID | — | — |
| 10 | JobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 11 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 12 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 13 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 14 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 16 | PeaAttribute1 | PEA_ATTRIBUTE1 | — | — |
| 17 | PeaAttribute10 | PEA_ATTRIBUTE10 | — | — |
| 18 | PeaAttribute11 | PEA_ATTRIBUTE11 | — | — |
| 19 | PeaAttribute12 | PEA_ATTRIBUTE12 | — | — |
| 20 | PeaAttribute13 | PEA_ATTRIBUTE13 | — | — |
| 21 | PeaAttribute14 | PEA_ATTRIBUTE14 | — | — |
| 22 | PeaAttribute15 | PEA_ATTRIBUTE15 | — | — |
| 23 | PeaAttribute16 | PEA_ATTRIBUTE16 | — | — |
| 24 | PeaAttribute17 | PEA_ATTRIBUTE17 | — | — |
| 25 | PeaAttribute18 | PEA_ATTRIBUTE18 | — | — |
| 26 | PeaAttribute19 | PEA_ATTRIBUTE19 | — | — |
| 27 | PeaAttribute2 | PEA_ATTRIBUTE2 | — | — |
| 28 | PeaAttribute20 | PEA_ATTRIBUTE20 | — | — |
| 29 | PeaAttribute21 | PEA_ATTRIBUTE21 | — | — |
| 30 | PeaAttribute22 | PEA_ATTRIBUTE22 | — | — |
| 31 | PeaAttribute23 | PEA_ATTRIBUTE23 | — | — |
| 32 | PeaAttribute24 | PEA_ATTRIBUTE24 | — | — |
| 33 | PeaAttribute25 | PEA_ATTRIBUTE25 | — | — |
| 34 | PeaAttribute26 | PEA_ATTRIBUTE26 | — | — |
| 35 | PeaAttribute27 | PEA_ATTRIBUTE27 | — | — |
| 36 | PeaAttribute28 | PEA_ATTRIBUTE28 | — | — |
| 37 | PeaAttribute29 | PEA_ATTRIBUTE29 | — | — |
| 38 | PeaAttribute3 | PEA_ATTRIBUTE3 | — | — |
| 39 | PeaAttribute30 | PEA_ATTRIBUTE30 | — | — |
| 40 | PeaAttribute4 | PEA_ATTRIBUTE4 | — | — |
| 41 | PeaAttribute5 | PEA_ATTRIBUTE5 | — | — |
| 42 | PeaAttribute6 | PEA_ATTRIBUTE6 | — | — |
| 43 | PeaAttribute7 | PEA_ATTRIBUTE7 | — | — |
| 44 | PeaAttribute8 | PEA_ATTRIBUTE8 | — | — |
| 45 | PeaAttribute9 | PEA_ATTRIBUTE9 | — | — |
| 46 | PeaAttributeCategory | PEA_ATTRIBUTE_CATEGORY | — | — |
| 47 | PeaAttributeDate1 | PEA_ATTRIBUTE_DATE1 | — | — |
| 48 | PeaAttributeDate10 | PEA_ATTRIBUTE_DATE10 | — | — |
| 49 | PeaAttributeDate11 | PEA_ATTRIBUTE_DATE11 | — | — |
| 50 | PeaAttributeDate12 | PEA_ATTRIBUTE_DATE12 | — | — |
| 51 | PeaAttributeDate13 | PEA_ATTRIBUTE_DATE13 | — | — |
| 52 | PeaAttributeDate14 | PEA_ATTRIBUTE_DATE14 | — | — |
| 53 | PeaAttributeDate15 | PEA_ATTRIBUTE_DATE15 | — | — |
| 54 | PeaAttributeDate2 | PEA_ATTRIBUTE_DATE2 | — | — |
| 55 | PeaAttributeDate3 | PEA_ATTRIBUTE_DATE3 | — | — |
| 56 | PeaAttributeDate4 | PEA_ATTRIBUTE_DATE4 | — | — |
| 57 | PeaAttributeDate5 | PEA_ATTRIBUTE_DATE5 | — | — |
| 58 | PeaAttributeDate6 | PEA_ATTRIBUTE_DATE6 | — | — |
| 59 | PeaAttributeDate7 | PEA_ATTRIBUTE_DATE7 | — | — |
| 60 | PeaAttributeDate8 | PEA_ATTRIBUTE_DATE8 | — | — |
| 61 | PeaAttributeDate9 | PEA_ATTRIBUTE_DATE9 | — | — |
| 62 | PeaAttributeNumber1 | PEA_ATTRIBUTE_NUMBER1 | — | — |
| 63 | PeaAttributeNumber10 | PEA_ATTRIBUTE_NUMBER10 | — | — |
| 64 | PeaAttributeNumber11 | PEA_ATTRIBUTE_NUMBER11 | — | — |
| 65 | PeaAttributeNumber12 | PEA_ATTRIBUTE_NUMBER12 | — | — |
| 66 | PeaAttributeNumber13 | PEA_ATTRIBUTE_NUMBER13 | — | — |
| 67 | PeaAttributeNumber14 | PEA_ATTRIBUTE_NUMBER14 | — | — |
| 68 | PeaAttributeNumber15 | PEA_ATTRIBUTE_NUMBER15 | — | — |
| 69 | PeaAttributeNumber16 | PEA_ATTRIBUTE_NUMBER16 | — | — |
| 70 | PeaAttributeNumber17 | PEA_ATTRIBUTE_NUMBER17 | — | — |
| 71 | PeaAttributeNumber18 | PEA_ATTRIBUTE_NUMBER18 | — | — |
| 72 | PeaAttributeNumber19 | PEA_ATTRIBUTE_NUMBER19 | — | — |
| 73 | PeaAttributeNumber2 | PEA_ATTRIBUTE_NUMBER2 | — | — |
| 74 | PeaAttributeNumber20 | PEA_ATTRIBUTE_NUMBER20 | — | — |
| 75 | PeaAttributeNumber3 | PEA_ATTRIBUTE_NUMBER3 | — | — |
| 76 | PeaAttributeNumber4 | PEA_ATTRIBUTE_NUMBER4 | — | — |
| 77 | PeaAttributeNumber5 | PEA_ATTRIBUTE_NUMBER5 | — | — |
| 78 | PeaAttributeNumber6 | PEA_ATTRIBUTE_NUMBER6 | — | — |
| 79 | PeaAttributeNumber7 | PEA_ATTRIBUTE_NUMBER7 | — | — |
| 80 | PeaAttributeNumber8 | PEA_ATTRIBUTE_NUMBER8 | — | — |
| 81 | PeaAttributeNumber9 | PEA_ATTRIBUTE_NUMBER9 | — | — |
| 82 | PerInLerId | PER_IN_LER_ID | — | — |
| 83 | PlBnfId | PL_BNF_ID | — | — |
| 84 | ProgramAppName | PROGRAM_APP_NAME | — | — |
| 85 | ProgramName | PROGRAM_NAME | — | — |
| 86 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 87 | PrttEnrtActnId | PRTT_ENRT_ACTN_ID | 🔑 | ✅ |
| 88 | PrttEnrtRsltId | PRTT_ENRT_RSLT_ID | — | — |
| 89 | RequestId | REQUEST_ID | — | — |
| 90 | RqdFlag | RQD_FLAG | — | ✅ |
| 91 | SspndFlag | SSPND_FLAG | — | ✅ |

### [[ben_prtt_enrt_rslt|BEN_PRTT_ENRT_RSLT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentId | ASSIGNMENT_ID | — | — |
| 2 | OiplId | OIPL_ID | — | — |
| 3 | OptId | OPT_ID | — | — |
| 4 | PersonId | PERSON_ID | — | — |
| 5 | PgmId | PGM_ID | — | — |
| 6 | PlId | PL_ID | — | — |
| 7 | PrttEnrtRsltId1 | PRTT_ENRT_RSLT_ID | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
