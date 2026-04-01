---
id: DOC-HCM-411
doc_type: system-doc
title: "HXT_SCH_PROF_DEFAULT_VIEW — View Padrao de Perfis de Agenda"
system: Oracle Fusion Cloud HCM
module: Human Capital Management
domain: Tecnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - time-labor
  - hxt
  - schedule-profile
  - perfil-agenda
  - view
aliases:
  - HXT_SCH_PROF_DEFAULT_VIEW
  - hxt_sch_prof_default_view
  - hxt-sch-prof-default-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SCH_PROF_DEFAULT_VIEW

## 📌 Visao Geral

View que apresenta os **perfis padrao de agenda** (schedule profiles) no modulo Time & Labor (HXT). Define templates de horario de trabalho reutilizaveis.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Templates de agenda:** define perfis reutilizaveis de horario de trabalho.
- **Padronizacao:** permite atribuir o mesmo perfil de horario a multiplos colaboradores.
- **Configuracao centralizada:** gerencia agendas de forma centralizada.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador do perfil | — | 🟡 65% |
| 2 | PROFILE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome do perfil de agenda | — | 🟡 60% |
| 3 | SCHEDULE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de agenda | — | 🟡 55% |
| 4 | HOURS_PER_DAY | NUMBER | NULL | Dados | Horas padrao por dia | — | 🟡 55% |
| 5 | DAYS_PER_WEEK | NUMBER | NULL | Dados | Dias por semana | — | 🟡 55% |
| 6 | START_TIME | VARCHAR2(8) | NULL | Dados | Horario de inicio padrao | — | 🟡 50% |
| 7 | END_TIME | VARCHAR2(8) | NULL | Dados | Horario de termino padrao | — | 🟡 50% |
| 8 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Perfis de agenda ativos
```sql
SELECT v.SCHEDULE_PROFILE_ID, v.PROFILE_NAME,
       v.HOURS_PER_DAY, v.DAYS_PER_WEEK
FROM   HXT_SCH_PROF_DEFAULT_VIEW v
WHERE  v.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Perfis ativos`
- `SCHEDULE_TYPE = :p_type — Por tipo de agenda`

---

## 🔒 Observacoes

- View somente leitura.
- Define templates padrao de jornada de trabalho.
- Perfis podem ser associados a organizacoes ou atribuicoes individuais.

---

## 📚 Referencias

- [Oracle Docs — HXT_SCH_PROF_DEFAULT_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtschprofdefaultview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[plannedscheduleshiftentrypvo|PlannedScheduleShiftEntryPVO]] (HCM · BICC: 5/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGN_TO | SetupProfileAsgAssignTo | — |
| CREATION_DATE1 | SetupOptionCreationDate | — |
| EFFECTIVE_END_DATE | SetupOptionEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | SetupOptionEffectiveStartDate | ✅ |
| GRP_INCL_MEMBER_ID | GrpInclMemberId | — |
| INCL_MEMBER_ID | InclMemberId | — |
| PRODUCT_AREA | ProductArea | — |
| SETUP_OPTION_VAL_ID | SetupOptionValId | ✅ |
| SETUP_PROFILE_ASG_ID | SetupProfileAsgId | ✅ |
| SETUP_PROFILE_ID | SetupProfileId | ✅ |

### [[publishedscheduleshiftentrypvo|PublishedScheduleShiftEntryPVO]] (HCM · BICC: 5/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ASSIGN_TO | SetupProfileAsgAssignTo | — |
| CREATION_DATE1 | SetupOptionCreationDate | — |
| EFFECTIVE_END_DATE | SetupOptionEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | SetupOptionEffectiveStartDate | ✅ |
| GRP_INCL_MEMBER_ID | GrpInclMemberId | — |
| INCL_MEMBER_ID | InclMemberId | — |
| PRODUCT_AREA | ProductArea | — |
| SETUP_OPTION_VAL_ID | SetupOptionValId | ✅ |
| SETUP_PROFILE_ASG_ID | SetupProfileAsgId | ✅ |
| SETUP_PROFILE_ID | SetupProfileId | ✅ |

### [[scheduledaypvo|ScheduleDayPVO]] (HCM · BICC: 1/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATION_DATE1 | BISchedulerProfileOptionPEOCreationDate1 | — |
| EFFECTIVE_END_DATE | BISchedulerProfileOptionPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | BISchedulerProfileOptionPEOEffectiveStartDate | ✅ |
| INCL_MEMBER_ID | BISchedulerProfileOptionPEOInclMemberId | — |
| SETUP_OPTION_VAL_ID | BISchedulerProfileOptionPEOSetupOptionValId | — |
| SETUP_PROFILE_ASG_ID | BISchedulerProfileOptionPEOSetupProfileAsgId | — |

### [[schedulerprofileoptionpvo|SchedulerProfileOptionPVO]] (GL · BICC: 18/32)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATED_BY1 | CreatedBy1 | — |
| CREATION_DATE | CreationDate | ✅ |
| CREATION_DATE1 | CreationDate1 | — |
| DATE_FROM | DateFrom | — |
| DATE_TO | DateTo | — |
| DESCRIPTION | Description | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| FIRST_DAY_OF_WEEK | FirstDayOfWeek | — |
| GROUP_MANAGER_ID | GroupManagerId | ✅ |
| GRP_ID | GrpId | — |
| GRP_INCL_MEMBER_ID | GrpInclMemberId | — |
| INCL_MEMBER_ID | InclMemberId | — |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_DATE1 | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATE_LOGIN1 | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LAST_UPDATED_BY1 | LastUpdatedBy1 | — |
| NAME | Name | ✅ |
| OVER_STAFF_THRESHOLD | OverStaffThreshold | ✅ |
| PRECEDENCE | Precedence | — |
| PRODUCT_AREA | ProductArea | — |
| SCHEDULING_GROUP_ID | SchedulingGroupId | — |
| SETUP_OPTION_VAL_CD | SetupOptionValCd | ✅ |
| SETUP_OPTION_VAL_ID | SetupOptionValId | ✅ |
| SETUP_PROFILE_ASG_ID | SetupProfileAsgId | ✅ |
| SETUP_PROFILE_CD | SetupProfileCd | ✅ |
| SETUP_PROFILE_ID | SetupProfileId | ✅ |
| TYPE | Type | — |
| UNDER_STAFF_THRESHOLD | UnderStaffThreshold | ✅ |
