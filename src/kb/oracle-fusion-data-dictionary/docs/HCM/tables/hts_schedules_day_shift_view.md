---
id: DOC-HCM-290
doc_type: system-doc
title: "HTS_SCHEDULES_DAY_SHIFT_VIEW — Turnos por Dia de Schedule (View)"
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
  - schedules
  - shifts
  - time-labor
aliases:
  - HTS_SCHEDULES_DAY_SHIFT_VIEW
  - hts_schedules_day_shift_view
  - hts-schedules-day-shift-view
  - schedules-day-shift-view
  - turnos-dia-schedule
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HTS_SCHEDULES_DAY_SHIFT_VIEW

## 📌 Visao Geral

View que expoe os **turnos por dia** dentro de cada schedule. Apresenta a configuracao de shifts (turnos) para cada dia da semana.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Scheduling:** Visualizar turnos por dia.
- **Time and Labor:** Validar configuracao de escalas.
- **Relatorios:** Analisar padroes de trabalho.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_ID | NUMBER(18) | NOT NULL | PK | Identificador do schedule | — | 🟡 80% |
| 2 | DAY_OF_WEEK | VARCHAR2(30) | NULL | Classificacao | Dia da semana | — | 🟡 80% |
| 3 | SHIFT_NAME | VARCHAR2(240) | NULL | Dados | Nome do turno | — | 🟡 80% |
| 4 | START_TIME | VARCHAR2(30) | NULL | Data | Hora de inicio do turno | — | 🟡 80% |
| 5 | END_TIME | VARCHAR2(30) | NULL | Data | Hora de fim do turno | — | 🟡 80% |
| 6 | DURATION_HOURS | NUMBER | NULL | Dados | Duracao em horas | — | 🟡 75% |
| 7 | SCHEDULE_DATE | DATE | NULL | Data | Data especifica do schedule | — | 🟡 75% |
| 8 | CREATION_DATE | TIMESTAMP | NULL | Auditoria | Data de criacao | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma FK de entrada identificada.

### Tabelas-filha (FK de saida)
- Nenhuma FK de saida identificada.

---

## 📎 Uso Tipico

### Turnos de um schedule
```sql
SELECT sds.DAY_OF_WEEK, sds.SHIFT_NAME,
       sds.START_TIME, sds.END_TIME
FROM   HTS_SCHEDULES_DAY_SHIFT_VIEW sds
WHERE  sds.SCHEDULE_ID = :p_schedule_id
ORDER BY sds.DAY_OF_WEEK;
```

---

## 🔒 Observacoes

- View somente leitura.
- Util para visualizar a configuracao de escalas de trabalho.

---

## 📚 Referencias

- [Oracle Docs — HTS_SCHEDULES_DAY_SHIFT_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/htsschedulesdayshiftview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM

---

## 🔗 PVOs Relacionados

### [[plannedscheduleshiftentrypvo|PlannedScheduleShiftEntryPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARENT_TM_REC_GRP_ID | ScheduleDayShift1PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift2PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift3PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOParentTmRecGrpVersion | — |
| SHIFT_DATE_FROM | ScheduleDayShift1PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift2PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift3PEOShiftDateFrom | — |
| SHIFT_DATE_TO | ScheduleDayShift1PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift2PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift3PEOShiftDateTo | — |
| SHIFT_ID | ScheduleDayShift1PEOShiftId1 | — |
| SHIFT_ID | ScheduleDayShift2PEOShiftId1 | — |
| SHIFT_ID | ScheduleDayShift3PEOShiftId1 | — |
| SHIFT_NAME | ScheduleDayShift1PEOShiftName1 | — |
| SHIFT_NAME | ScheduleDayShift2PEOShiftName1 | — |
| SHIFT_NAME | ScheduleDayShift3PEOShiftName1 | — |
| SHIFT_SEQUENCE | ScheduleDayShift1PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift2PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift3PEOShiftSequence | — |
| SHIFT_SHORT_NAME | ScheduleDayShift1PEOShiftShortName1 | — |
| SHIFT_SHORT_NAME | ScheduleDayShift2PEOShiftShortName1 | — |
| SHIFT_SHORT_NAME | ScheduleDayShift3PEOShiftShortName1 | — |
| SHIFT_START_TIME | ScheduleDayShift1PEOShiftStartTime | — |
| SHIFT_START_TIME | ScheduleDayShift2PEOShiftStartTime | — |
| SHIFT_START_TIME | ScheduleDayShift3PEOShiftStartTime | — |
| SHIFT_STOP_TIME | ScheduleDayShift1PEOShiftStopTime | — |
| SHIFT_STOP_TIME | ScheduleDayShift2PEOShiftStopTime | — |
| SHIFT_STOP_TIME | ScheduleDayShift3PEOShiftStopTime | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift1PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift2PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift3PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOShiftTmRecGrpVersion | — |
| SHIFT_TYPE_CODE | ScheduleDayShift1PEOShiftTypeCode1 | — |
| SHIFT_TYPE_CODE | ScheduleDayShift2PEOShiftTypeCode1 | — |
| SHIFT_TYPE_CODE | ScheduleDayShift3PEOShiftTypeCode1 | — |

### [[publishedscheduleshiftentrypvo|PublishedScheduleShiftEntryPVO]] (HCM · BICC: 15/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARENT_TM_REC_GRP_ID | ScheduleDayShift1PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift2PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift3PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOParentTmRecGrpVersion | — |
| SHIFT_DATE_FROM | ScheduleDayShift1PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift2PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift3PEOShiftDateFrom | — |
| SHIFT_DATE_TO | ScheduleDayShift1PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift2PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift3PEOShiftDateTo | — |
| SHIFT_ID | ScheduleDayShift1PEOShiftId1 | — |
| SHIFT_ID | ScheduleDayShift2PEOShiftId1 | — |
| SHIFT_ID | ScheduleDayShift3PEOShiftId1 | — |
| SHIFT_NAME | ScheduleDayShift1PEOShiftName1 | ✅ |
| SHIFT_NAME | ScheduleDayShift2PEOShiftName1 | ✅ |
| SHIFT_NAME | ScheduleDayShift3PEOShiftName1 | ✅ |
| SHIFT_SEQUENCE | ScheduleDayShift1PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift2PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift3PEOShiftSequence | — |
| SHIFT_SHORT_NAME | ScheduleDayShift1PEOShiftShortName1 | ✅ |
| SHIFT_SHORT_NAME | ScheduleDayShift2PEOShiftShortName1 | ✅ |
| SHIFT_SHORT_NAME | ScheduleDayShift3PEOShiftShortName1 | ✅ |
| SHIFT_START_TIME | ScheduleDayShift1PEOShiftStartTime | ✅ |
| SHIFT_START_TIME | ScheduleDayShift2PEOShiftStartTime | ✅ |
| SHIFT_START_TIME | ScheduleDayShift3PEOShiftStartTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift1PEOShiftStopTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift2PEOShiftStopTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift3PEOShiftStopTime | ✅ |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift1PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift2PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift3PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOShiftTmRecGrpVersion | — |
| SHIFT_TYPE_CODE | ScheduleDayShift1PEOShiftTypeCode1 | ✅ |
| SHIFT_TYPE_CODE | ScheduleDayShift2PEOShiftTypeCode1 | ✅ |
| SHIFT_TYPE_CODE | ScheduleDayShift3PEOShiftTypeCode1 | ✅ |

### [[scheduledaypvo|ScheduleDayPVO]] (HCM · BICC: 15/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARENT_TM_REC_GRP_ID | ScheduleDayShift1PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift2PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_ID | ScheduleDayShift3PEOParentTmRecGrpId | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOParentTmRecGrpVersion | — |
| PARENT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOParentTmRecGrpVersion | — |
| SHIFT_DATE_FROM | ScheduleDayShift1PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift2PEOShiftDateFrom | — |
| SHIFT_DATE_FROM | ScheduleDayShift3PEOShiftDateFrom | — |
| SHIFT_DATE_TO | ScheduleDayShift1PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift2PEOShiftDateTo | — |
| SHIFT_DATE_TO | ScheduleDayShift3PEOShiftDateTo | — |
| SHIFT_ID | ScheduleDayShift1PEOShiftId | — |
| SHIFT_ID | ScheduleDayShift2PEOShiftId | — |
| SHIFT_ID | ScheduleDayShift3PEOShiftId | — |
| SHIFT_NAME | ScheduleDayShift1PEOShiftName | ✅ |
| SHIFT_NAME | ScheduleDayShift2PEOShiftName | ✅ |
| SHIFT_NAME | ScheduleDayShift3PEOShiftName | ✅ |
| SHIFT_SEQUENCE | ScheduleDayShift1PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift2PEOShiftSequence | — |
| SHIFT_SEQUENCE | ScheduleDayShift3PEOShiftSequence | — |
| SHIFT_SHORT_NAME | ScheduleDayShift1PEOShiftShortName | ✅ |
| SHIFT_SHORT_NAME | ScheduleDayShift2PEOShiftShortName | ✅ |
| SHIFT_SHORT_NAME | ScheduleDayShift3PEOShiftShortName | ✅ |
| SHIFT_START_TIME | ScheduleDayShift1PEOShiftStartTime | ✅ |
| SHIFT_START_TIME | ScheduleDayShift2PEOShiftStartTime | ✅ |
| SHIFT_START_TIME | ScheduleDayShift3PEOShiftStartTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift1PEOShiftStopTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift2PEOShiftStopTime | ✅ |
| SHIFT_STOP_TIME | ScheduleDayShift3PEOShiftStopTime | ✅ |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift1PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift2PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_ID | ScheduleDayShift3PEOShiftTmRecGrpId | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift1PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift2PEOShiftTmRecGrpVersion | — |
| SHIFT_TM_REC_GRP_VERSION | ScheduleDayShift3PEOShiftTmRecGrpVersion | — |
| SHIFT_TYPE_CODE | ScheduleDayShift1PEOShiftTypeCode | ✅ |
| SHIFT_TYPE_CODE | ScheduleDayShift2PEOShiftTypeCode | ✅ |
| SHIFT_TYPE_CODE | ScheduleDayShift3PEOShiftTypeCode | ✅ |
