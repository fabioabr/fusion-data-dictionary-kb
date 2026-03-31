---
id: DOC-GL-PVO-PersonAbsCertificationsPVO
doc_type: system-doc
title: "PersonAbsCertificationsPVO — PVO General Ledger"
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
  - PersonAbsCertificationsPVO
  - personabscertificationspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PersonAbsCertificationsPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Person Abs Certifications. Acessa as tabelas: ANC_ABSENCE_PLANS_F_TL, ANC_ABS_CERTIFICATIONS_F_TL, ANC_PER_ABS_CERTS.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.PersonAbsCertificationsPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 3 | 1 | 31 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]] — 5 atributos (2 BICC)
- [[anc_abs_certifications_f_tl|ANC_ABS_CERTIFICATIONS_F_TL]] — 15 atributos (4 BICC)
- [[anc_per_abs_certs|ANC_PER_ABS_CERTS]] — 35 atributos (1 PKs, 25 BICC)

---

## ⚙️ Atributos

### [[anc_absence_plans_f_tl|ANC_ABSENCE_PLANS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsencePlanId | ABSENCE_PLAN_ID | — | — |
| 2 | AbsenceTargetPlanName | NAME | — | ✅ |
| 3 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | — |
| 4 | EffectiveStartDate1 | EFFECTIVE_START_DATE | — | ✅ |
| 5 | Language1 | LANGUAGE | — | — |

### [[anc_abs_certifications_f_tl|ANC_ABS_CERTIFICATIONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCertificationDesc | ABSENCE_CERTIFICATION_DESC | — | ✅ |
| 2 | AbsenceCertificationId1 | ABSENCE_CERTIFICATION_ID | — | — |
| 3 | CreatedBy1 | CREATED_BY | — | — |
| 4 | CreationDate1 | CREATION_DATE | — | — |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | — | — |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 12 | ModuleId | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | — |

### [[anc_per_abs_certs|ANC_PER_ABS_CERTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCertificationId | ABSENCE_CERTIFICATION_ID | — | — |
| 2 | AcceptedBy | ACCEPTED_BY | — | ✅ |
| 3 | AcceptedDate | ACCEPTED_DATE | — | ✅ |
| 4 | AcceptedYn | ACCEPTED_YN | — | ✅ |
| 5 | CertCreationDate | CERT_CREATION_DATE | — | ✅ |
| 6 | Comments | COMMENTS | — | ✅ |
| 7 | CompleteYn | COMPLETE_YN | — | ✅ |
| 8 | CompletedDate | COMPLETED_DATE | — | ✅ |
| 9 | ConfirmRsnCd | CONFIRM_RSN_CD | — | ✅ |
| 10 | CreatedBy | CREATED_BY | — | — |
| 11 | CreationDate | CREATION_DATE | — | — |
| 12 | CtfnCreationMode | CTFN_CREATION_MODE | — | ✅ |
| 13 | EnterpriseId | ENTERPRISE_ID | — | — |
| 14 | EvidenceSource | EVIDENCE_SOURCE | — | — |
| 15 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 16 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 17 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 18 | LateReason | LATE_REASON | — | ✅ |
| 19 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | PerAbsenceEntryId | PER_ABSENCE_ENTRY_ID | — | — |
| 21 | PerCertId | PER_CERT_ID | 🔑 | ✅ |
| 22 | PersonAbsCertificationsPEOCaseId | CASE_ID | — | — |
| 23 | ReceivedDate | RECEIVED_DATE | — | ✅ |
| 24 | ReceivedLateYn | RECEIVED_LATE_YN | — | ✅ |
| 25 | ReceivedYn | RECEIVED_YN | — | ✅ |
| 26 | RequiredByDate | REQUIRED_BY_DATE | — | ✅ |
| 27 | RevPayEndDt | REV_PAY_END_DT | — | ✅ |
| 28 | RevPayPct | REV_PAY_PCT | — | ✅ |
| 29 | RevPayStartDt | REV_PAY_START_DT | — | ✅ |
| 30 | Status | STATUS | — | ✅ |
| 31 | TargetPlanId | TARGET_PLAN_ID | — | ✅ |
| 32 | ValidUptoDate | VALID_UPTO_DATE | — | ✅ |
| 33 | VoidRsnCd | VOID_RSN_CD | — | ✅ |
| 34 | VoidYn | VOID_YN | — | ✅ |
| 35 | VoidedDate | VOIDED_DATE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
