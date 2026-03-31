---
id: DOC-HCM-202
doc_type: system-doc
title: "HRR_DASHBOARDS — Dashboards de Talent Review"
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
  - dashboards
aliases:
  - HRR_DASHBOARDS
  - hrr_dashboards
  - dashboards-de-talent-review
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRR_DASHBOARDS

## 📌 Visão Geral

Armazena **dashboards** de Talent Review. Configurados para reuniões de revisão de talentos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Configuração:** Dashboards de talent review.
- **Visualização:** Análise de pool de talentos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | DASHBOARD_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | DASHBOARD_NAME | VARCHAR2(240) | NOT NULL | Identificação | Nome do dashboard | — | 🟡 80% |
| 3 | TEMPLATE_ID | NUMBER(18) | NULL | FK | Template | [[hrr_dashboard_tmpls_b]] | 🟡 80% |
| 4 | OWNER_PERSON_ID | NUMBER(18) | NULL | FK | Owner | [[per_all_people_f]] | 🟡 75% |
| 5 | STATUS_CODE | VARCHAR2(30) | NULL | Classificação | Status | — | 🟡 70% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 11 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrr_dashboard_tmpls_b]] — via `TEMPLATE_ID` (template do dashboard de talent review)

### Tabelas-filha

---

## 📎 Uso Típico

### Dashboards ativos
```sql
SELECT d.DASHBOARD_ID, d.DASHBOARD_NAME, d.STATUS_CODE
FROM   HRR_DASHBOARDS d
WHERE  d.STATUS_CODE = 'ACTIVE';
```

---

## 🔒 Observações

- Dashboards configuram a visualização de Talent Review.

---

## 🔗 PVOs Relacionados

### [[competenciescalbratingpvo|CompetenciesCalbRatingPVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[competenciescalbratingpvo_viewall|CompetenciesCalbRatingPVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[dashboardpvo|DashboardPVO]] (HCM · BICC: 25/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | AgeGroupValue | ✅ |
| ASSIGNMENT_ID | AssignmentId | ✅ |
| BU_LEADER_DIRECT_ID | BuLeaderDirectId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DASHBOARD_ID | DashboardId | ✅ |
| IMPACT_LOSS_CALB_RT_LVL_ID | ImpactLossCalbRtLvlId | ✅ |
| IMPACT_LOSS_RT_LVL_ID | ImpactLossRtLvlId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MEETING_ID | MeetingId | ✅ |
| MOBILITY_CALIB_VALUE | MobilityCalibValue | ✅ |
| MOBILITY_VALUE | MobilityValue | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PERF_CALIB_RT_LVL_ID | PerfCalibRtLvlId | ✅ |
| PERF_RT_LVL_ID | PerfRtLvlId | ✅ |
| PERSON_ID | PersonId | ✅ |
| POT_CALIB_RT_LVL_ID | PotCalibRtLvlId | ✅ |
| POT_RT_LVL_ID | PotRtLvlId | ✅ |
| RISK_LOSS_CALIB_RT_LVL_ID | RiskLossCalibRtLvlId | ✅ |
| RISK_LOSS_RT_LVL_ID | RiskLossRtLvlId | ✅ |
| TALENT_SCOR_CALB_RT_LVL_ID | TalentScorCalbRtLvlId | ✅ |
| TALENT_SCORE_RT_LVL_ID | TalentScoreRtLvlId | ✅ |

### [[goalscalibratingpvo|GoalsCalibRatingPVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[goalscalibratingpvo_viewall|GoalsCalibRatingPVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[impactoflosscalibratingpvo|ImpactOfLossCalibRatingPVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[impactoflosscalibratingpvo_viewall|ImpactOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[meetingnotepvo|MeetingNotePVO]] (HCM · BICC: 5/25)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | AgeGroupValue | — |
| ASSIGNMENT_ID | AssignmentId | — |
| BU_LEADER_DIRECT_ID | BuLeaderDirectId | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DASHBOARD_ID | DashboardId | ✅ |
| IMPACT_LOSS_CALB_RT_LVL_ID | ImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | ImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MEETING_ID | MeetingId | ✅ |
| MOBILITY_CALIB_VALUE | MobilityCalibValue | — |
| MOBILITY_VALUE | MobilityValue | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PERF_CALIB_RT_LVL_ID | PerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | PerfRtLvlId | — |
| PERSON_ID | PersonId | ✅ |
| POT_CALIB_RT_LVL_ID | PotCalibRtLvlId | — |
| POT_RT_LVL_ID | PotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | RiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | RiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | TalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | TalentScoreRtLvlId | — |

### [[performancecalibratedratingvo|PerformanceCalibratedRatingVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[performancecalibratedratingvo_viewall|PerformanceCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[potentialcalibratedratingvo|PotentialCalibratedRatingVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[potentialcalibratedratingvo_viewall|PotentialCalibratedRatingVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[riskoflosscalibratingpvo|RiskOfLossCalibRatingPVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[riskoflosscalibratingpvo_viewall|RiskOfLossCalibRatingPVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[talentscorecalibratingpvo|TalentScoreCalibRatingPVO]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

### [[talentscorecalibratingpvo_viewall|TalentScoreCalibRatingPVO_ViewAll]] (HCM · BICC: 2/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AGE_GROUP_VALUE | DashboardPEOAgeGroupValue | — |
| ASSIGNMENT_ID | DashboardPEOAssignmentId | — |
| BU_LEADER_DIRECT_ID | DashboardPEOBuLeaderDirectId | — |
| BUSINESS_GROUP_ID | DashboardPEOBusinessGroupId1 | — |
| CREATED_BY | DashboardPEOCreatedBy1 | — |
| CREATION_DATE | DashboardPEOCreationDate1 | — |
| DASHBOARD_ID | DashboardPEODashboardId | ✅ |
| EXTN_METRIC_CALIB_VALUE1 | DashboardPEOExtnMetricCalibValue1 | — |
| EXTN_METRIC_CALIB_VALUE2 | DashboardPEOExtnMetricCalibValue2 | — |
| EXTN_METRIC_VALUE1 | DashboardPEOExtnMetricValue1 | — |
| EXTN_METRIC_VALUE2 | DashboardPEOExtnMetricValue2 | — |
| IMPACT_LOSS_CALB_RT_LVL_ID | DashboardPEOImpactLossCalbRtLvlId | — |
| IMPACT_LOSS_RT_LVL_ID | DashboardPEOImpactLossRtLvlId | — |
| LAST_UPDATE_DATE | DashboardPEOLastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | DashboardPEOLastUpdateLogin1 | — |
| LAST_UPDATED_BY | DashboardPEOLastUpdatedBy1 | — |
| MEETING_ID | DashboardPEOMeetingId | — |
| MOBILITY_CALIB_VALUE | DashboardPEOMobilityCalibValue | — |
| MOBILITY_VALUE | DashboardPEOMobilityValue | — |
| OBJECT_VERSION_NUMBER | DashboardPEOObjectVersionNumber1 | — |
| PERF_CALIB_RT_LVL_ID | DashboardPEOPerfCalibRtLvlId | — |
| PERF_RT_LVL_ID | DashboardPEOPerfRtLvlId | — |
| PERSON_ID | DashboardPEOPersonId1 | — |
| POT_CALIB_RT_LVL_ID | DashboardPEOPotCalibRtLvlId | — |
| POT_RT_LVL_ID | DashboardPEOPotRtLvlId | — |
| RISK_LOSS_CALIB_RT_LVL_ID | DashboardPEORiskLossCalibRtLvlId | — |
| RISK_LOSS_RT_LVL_ID | DashboardPEORiskLossRtLvlId | — |
| TALENT_SCOR_CALB_RT_LVL_ID | DashboardPEOTalentScorCalbRtLvlId | — |
| TALENT_SCORE_RT_LVL_ID | DashboardPEOTalentScoreRtLvlId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
