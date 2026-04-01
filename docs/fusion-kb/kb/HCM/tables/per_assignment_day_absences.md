---
id: DOC-HCM-630
doc_type: system-doc
title: "PER_ASSIGNMENT_DAY_ABSENCES — Detalhamento Diário de Ausências"
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
  - absence-management
  - ausencias-diarias
  - day-absences
aliases:
  - PER_ASSIGNMENT_DAY_ABSENCES
  - per_assignment_day_absences
  - per-assignment-day-absences
  - detalhamento-diário-de-ausências
  - per-assignment-day-a
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGNMENT_DAY_ABSENCES

## 📌 Visão Geral

Armazena o **detalhamento diário** das ausências por assignment. Cada registro representa um dia individual dentro de um período de ausência, permitindo cálculos granulares.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Granularidade diária** — decompõe períodos de ausência em registros por dia.
- **Cálculo de payroll** — base precisa para descontos e pagamentos diários.
- **Calendário** — integração com calendário de trabalho para identificar dias úteis.
- **Relatórios** — análise de padrões de ausência por dia da semana.
- **Compliance** — registros detalhados para auditoria.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_DAY_ABSENCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro diário | — | 🟢 90% |
| 2 | ABSENCE_ATTENDANCE_ID | NUMBER(18) | NOT NULL | FK | Ausência associada | PER_ABSENCE_ATTENDANCES | 🟢 90% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 90% |
| 4 | ABSENCE_DATE | DATE | NOT NULL | Período | Data da ausência | — | 🟢 95% |
| 5 | ABSENCE_DURATION | NUMBER | NULL | Cálculo | Duração da ausência neste dia (horas ou fração) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_absence_attendances]] — via `ABSENCE_ATTENDANCE_ID` (ausência detalhada por dia)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo do dia de ausência)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Dias de ausência em um período
```sql
SELECT pada.ABSENCE_DATE, pada.ABSENCE_DURATION
FROM   PER_ASSIGNMENT_DAY_ABSENCES pada
WHERE  pada.ABSENCE_ATTENDANCE_ID = :p_absence_id
ORDER BY pada.ABSENCE_DATE;
```

### Filtros comuns
- `ABSENCE_DATE BETWEEN :p_start AND :p_end` — Dias em um período
---

## 🔒 Observações

- Cada registro representa um dia individual — útil para ausências que abrangem múltiplos dias.
- A `ABSENCE_DURATION` pode ser fracionária para ausências parciais (meio dia).
- Integra-se com o calendário de trabalho para ignorar feriados e finais de semana.
---

## 🔗 PVOs Relacionados

### [[absenceeventfactpvo|AbsenceEventFactPVO]] (HCM · BICC: 3/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABSENCE_ATTENDANCE_ID | AbsenseDailyBreakUpPEOAbsenceAttendanceId | ✅ |
| ABSENCE_DATE | AbsenseDailyBreakUpPEOAbsenceDate | — |
| ABSENCE_DURATION_DAYS | AbsenseDailyBreakUpPEOAbsenceDurationDays | — |
| ABSENCE_DURATION_HOURS | AbsenseDailyBreakUpPEOAbsenceDurationHours | — |
| ASG_ABSENCE_RECORDING_ID | AbsenseDailyBreakUpPEOAsgAbsenceRecordingId | — |
| ASSIGNMENT_DAY_ABSENCE_ID | AssignmentDayAbsenceId | ✅ |
| ASSIGNMENT_ID | AbsenseDailyBreakUpPEOAssignmentId | — |
| CALENDAR_EVENT_DURATION | AbsenseDailyBreakUpPEOCalendarEventDuration | — |
| CREATED_BY | AbsenseDailyBreakUpPEOCreatedBy | — |
| CREATION_DATE | AbsenseDailyBreakUpPEOCreationDate | — |
| DAY_TYPE | AbsenseDailyBreakUpPEODayType | — |
| LAST_UPDATE_DATE | AbsenseDailyBreakUpPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AbsenseDailyBreakUpPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AbsenseDailyBreakUpPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AbsenseDailyBreakUpPEOObjectVersionNumber | — |
| PERSON_ID | AbsenseDailyBreakUpPEOPersonId | — |
| SCHEDULE_WORK_DURATION | AbsenseDailyBreakUpPEOScheduleWorkDuration | — |
| WORK_SCHEDULE_UNIT | AbsenseDailyBreakUpPEOWorkScheduleUnit | — |

---

## 📚 Referências

- [Oracle Docs — PER_ASSIGNMENT_DAY_ABSENCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignmentdayabsences.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
