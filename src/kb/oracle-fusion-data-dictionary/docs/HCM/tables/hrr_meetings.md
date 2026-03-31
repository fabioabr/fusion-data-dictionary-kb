---
id: DOC-HCM-205
doc_type: system-doc
title: "HRR_MEETINGS — Reuniões de Talent Review"
system: Oracle Fusion Cloud HCM
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
  - talent-review
  - meetings
aliases:
  - HRR_MEETINGS
  - hrr_meetings
  - reuniões-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_MEETINGS

## 📌 Visão Geral

Armazena **reuniões de Talent Review**. Sessões agendadas de revisão de talentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Agendamento:** Reuniões de Talent Review.
- **Registro:** Sessões de revisão.
- **Integração:** Com dashboards e conteúdo.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | MEETING_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | MEETING_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome | — | 🟢 85% |
| 3 | DASHBOARD_ID | NUMBER(18) | NULL | FK | Dashboard | [[hrr_dashboards]] | 🟡 80% |
| 4 | MEETING_DATE | DATE | NULL | Data | Data da reunião | — | 🟡 80% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status (SCHEDULED, IN_PROGRESS, COMPLETED) | — | 🟡 75% |
| 6 | ORGANIZER_ID | NUMBER(18) | NULL | FK | Organizador | [[per_all_people_f]] | 🟡 75% |
| 7 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 12 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboards]] — via `DASHBOARD_ID` (dashboard da reuniao de talent review)

### Tabelas-filha

---

## 📎 Uso Típico

### Reuniões agendadas
```sql
SELECT m.MEETING_ID, m.MEETING_NAME, m.MEETING_DATE, m.STATUS_CODE
FROM   HRR_MEETINGS m
WHERE  m.STATUS_CODE = 'SCHEDULED'
ORDER BY m.MEETING_DATE;
```

---

## 🔒 Observações

- Tabela central de Talent Review meetings.
- Ciclo: SCHEDULED -> IN_PROGRESS -> COMPLETED.

---

## 🔗 PVOs Relacionados

### [[boxlabellookuppvo|BoxLabelLookupPVO]] (HCM · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DASHBOARD_TMPL_ID | DashboardTmplId | — |
| DATA_SUBMIT_DATE | DataSubmitDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MEETING_DATE | MeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingFacilitatorNotes | — |
| MEETING_ID | MeetingId | ✅ |
| MEETING_INSTRUCTIONS | MeetingInstructions | — |
| MEETING_LEADER_ID | MeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingStatusCode | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingTitle | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREF_REVIEW_QUALIFIER_ID | PrefReviewQualifierId | — |

### [[competenciescalbratingpvo|CompetenciesCalbRatingPVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[competenciescalbratingpvo_viewall|CompetenciesCalbRatingPVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[goalscalibratingpvo|GoalsCalibRatingPVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[goalscalibratingpvo_viewall|GoalsCalibRatingPVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[impactoflosscalibratingpvo|ImpactOfLossCalibRatingPVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[impactoflosscalibratingpvo_viewall|ImpactOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[meetingfactpvo|MeetingFactPVO]] (HCM · BICC: 3/22)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DASHBOARD_TMPL_ID | DashboardTmplId | — |
| DATA_SUBMIT_DATE | DataSubmitDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MEETING_DATE | MeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingFacilitatorNotes | — |
| MEETING_ID | MeetingId | ✅ |
| MEETING_INSTRUCTIONS | MeetingInstructions | — |
| MEETING_LEADER_ID | MeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingTitle | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREF_REVIEW_QUALIFIER_ID | PrefReviewQualifierId | — |
| QUESTIONNAIRE_ID | QuestionnaireId | — |

### [[meetingpvo|MeetingPVO]] (HCM · BICC: 21/23)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DASHBOARD_TMPL_ID | DashboardTmplId | ✅ |
| DATA_SUBMIT_DATE | DataSubmitDate | ✅ |
| DATA_VALIDITY_CODE | DataValidityCode | — |
| INCLUDE_MATRIX_MGMT | IncludeMatrixMgmt | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MEETING_DATE | MeetingDate | ✅ |
| MEETING_FACILITATOR_NOTES | MeetingFacilitatorNotes | ✅ |
| MEETING_ID | MeetingId | ✅ |
| MEETING_INSTRUCTIONS | MeetingInstructions | ✅ |
| MEETING_LEADER_ID | MeetingLeaderId | ✅ |
| MEETING_ORGANIZATION_ID | MeetingOrganizationId | ✅ |
| MEETING_PURPOSE | MeetingPurpose | ✅ |
| MEETING_STATUS_CODE | MeetingStatusCode | ✅ |
| MEETING_SUBMISSION_DATE | MeetingSubmissionDate | ✅ |
| MEETING_SUBMIT_STATUS_CODE | MeetingSubmitStatusCode | ✅ |
| MEETING_TITLE | MeetingTitle | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PREF_REVIEW_QUALIFIER_ID | PrefReviewQualifierId | — |

### [[nboxdimensionpvo|NBoxDimensionPVO]] (HCM · BICC: 3/87)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId | — |
| CREATED_BY | MeetingPEOCreatedBy | — |
| CREATION_DATE | MeetingPEOCreationDate | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | ✅ |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[nboxlabelpvo|NBoxLabelPVO]] (HCM · BICC: 3/20)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DASHBOARD_TMPL_ID | DashboardTmplId | — |
| DATA_SUBMIT_DATE | DataSubmitDate | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MEETING_DATE | MeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingFacilitatorNotes | — |
| MEETING_ID | MeetingId | ✅ |
| MEETING_INSTRUCTIONS | MeetingInstructions | — |
| MEETING_LEADER_ID | MeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingStatusCode | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingTitle | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PREF_REVIEW_QUALIFIER_ID | PrefReviewQualifierId | — |

### [[performancecalibratedratingvo|PerformanceCalibratedRatingVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[performancecalibratedratingvo_viewall|PerformanceCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[potentialcalibratedratingvo|PotentialCalibratedRatingVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[potentialcalibratedratingvo_viewall|PotentialCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[riskoflosscalibratingpvo|RiskOfLossCalibRatingPVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[riskoflosscalibratingpvo_viewall|RiskOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[talentscoreboxlabellookuppvo|TalentScoreBoxLabelLookupPVO]] (HCM · BICC: 2/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| MEETING_ID | MeetingId | ✅ |

### [[talentscorecalibratingpvo|TalentScoreCalibRatingPVO]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

### [[talentscorecalibratingpvo_viewall|TalentScoreCalibRatingPVO_ViewAll]] (HCM · BICC: 2/88)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ATTRIBUTE1 | MeetingPEOAttribute1 | — |
| ATTRIBUTE10 | MeetingPEOAttribute10 | — |
| ATTRIBUTE11 | MeetingPEOAttribute11 | — |
| ATTRIBUTE12 | MeetingPEOAttribute12 | — |
| ATTRIBUTE13 | MeetingPEOAttribute13 | — |
| ATTRIBUTE14 | MeetingPEOAttribute14 | — |
| ATTRIBUTE15 | MeetingPEOAttribute15 | — |
| ATTRIBUTE16 | MeetingPEOAttribute16 | — |
| ATTRIBUTE17 | MeetingPEOAttribute17 | — |
| ATTRIBUTE18 | MeetingPEOAttribute18 | — |
| ATTRIBUTE19 | MeetingPEOAttribute19 | — |
| ATTRIBUTE2 | MeetingPEOAttribute2 | — |
| ATTRIBUTE20 | MeetingPEOAttribute20 | — |
| ATTRIBUTE21 | MeetingPEOAttribute21 | — |
| ATTRIBUTE22 | MeetingPEOAttribute22 | — |
| ATTRIBUTE23 | MeetingPEOAttribute23 | — |
| ATTRIBUTE24 | MeetingPEOAttribute24 | — |
| ATTRIBUTE25 | MeetingPEOAttribute25 | — |
| ATTRIBUTE26 | MeetingPEOAttribute26 | — |
| ATTRIBUTE27 | MeetingPEOAttribute27 | — |
| ATTRIBUTE28 | MeetingPEOAttribute28 | — |
| ATTRIBUTE29 | MeetingPEOAttribute29 | — |
| ATTRIBUTE3 | MeetingPEOAttribute3 | — |
| ATTRIBUTE30 | MeetingPEOAttribute30 | — |
| ATTRIBUTE4 | MeetingPEOAttribute4 | — |
| ATTRIBUTE5 | MeetingPEOAttribute5 | — |
| ATTRIBUTE6 | MeetingPEOAttribute6 | — |
| ATTRIBUTE7 | MeetingPEOAttribute7 | — |
| ATTRIBUTE8 | MeetingPEOAttribute8 | — |
| ATTRIBUTE9 | MeetingPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | MeetingPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | MeetingPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | MeetingPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | MeetingPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | MeetingPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | MeetingPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | MeetingPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | MeetingPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | MeetingPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | MeetingPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | MeetingPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | MeetingPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | MeetingPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | MeetingPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | MeetingPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | MeetingPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | MeetingPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | MeetingPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | MeetingPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | MeetingPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | MeetingPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | MeetingPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | MeetingPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | MeetingPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | MeetingPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | MeetingPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | MeetingPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | MeetingPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | MeetingPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | MeetingPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | MeetingPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | MeetingPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | MeetingPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | MeetingPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | MeetingPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | MeetingPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | MeetingPEOBusinessGroupId2 | — |
| CREATED_BY | MeetingPEOCreatedBy2 | — |
| CREATION_DATE | MeetingPEOCreationDate2 | — |
| DASHBOARD_TMPL_ID | MeetingPEODashboardTmplId | — |
| DATA_SUBMIT_DATE | MeetingPEODataSubmitDate | — |
| DATA_VALIDITY_CODE | MeetingPEODataValidityCode | — |
| LAST_UPDATE_DATE | MeetingPEOLastUpdateDate2 | ✅ |
| LAST_UPDATE_LOGIN | MeetingPEOLastUpdateLogin2 | — |
| LAST_UPDATED_BY | MeetingPEOLastUpdatedBy2 | — |
| MEETING_DATE | MeetingPEOMeetingDate | — |
| MEETING_FACILITATOR_NOTES | MeetingPEOMeetingFacilitatorNotes | — |
| MEETING_ID | MeetingPEOMeetingId1 | ✅ |
| MEETING_INSTRUCTIONS | MeetingPEOMeetingInstructions | — |
| MEETING_LEADER_ID | MeetingPEOMeetingLeaderId | — |
| MEETING_ORGANIZATION_ID | MeetingPEOMeetingOrganizationId | — |
| MEETING_PURPOSE | MeetingPEOMeetingPurpose | — |
| MEETING_STATUS_CODE | MeetingPEOMeetingStatusCode | — |
| MEETING_SUBMISSION_DATE | MeetingPEOMeetingSubmissionDate | — |
| MEETING_SUBMIT_STATUS_CODE | MeetingPEOMeetingSubmitStatusCode | — |
| MEETING_TITLE | MeetingPEOMeetingTitle | — |
| OBJECT_VERSION_NUMBER | MeetingPEOObjectVersionNumber2 | — |
| PREF_REVIEW_QUALIFIER_ID | MeetingPEOPrefReviewQualifierId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
