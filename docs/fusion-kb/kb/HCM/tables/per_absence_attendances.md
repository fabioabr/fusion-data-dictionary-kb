---
id: DOC-HCM-602
doc_type: system-doc
title: "PER_ABSENCE_ATTENDANCES — Registros de Ausências e Presenças"
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
  - ausencias
  - absence-attendances
aliases:
  - PER_ABSENCE_ATTENDANCES
  - per_absence_attendances
  - per-absence-attendances
  - registros-de-ausências-e-presenças
  - per-absence-attendan
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ABSENCE_ATTENDANCES

## 📌 Visão Geral

Armazena os **registros individuais de ausências e presenças** dos colaboradores. Cada registro representa um evento de ausência com datas, tipo, motivo e duração.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Registro de ausências** — captura cada ocorrência de ausência (férias, doença, licenças).
- **Controle de duração** — armazena data início/fim e duração calculada em dias/horas.
- **Integração com payroll** — alimenta o processamento de folha para cálculos.
- **Relatórios de absenteísmo** — base para indicadores de RH e compliance.
- **Workflow de aprovação** — suporte ao fluxo de solicitação e aprovação.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ABSENCE_ATTENDANCE_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro de ausência | — | 🟢 95% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟢 95% |
| 3 | ABSENCE_ATTENDANCE_TYPE_ID | NUMBER(18) | NOT NULL | FK | Tipo de ausência | PER_ABSENCE_ATTENDANCE_TYPES_B | 🟢 90% |
| 4 | DATE_START | DATE | NOT NULL | Período | Data de início da ausência | — | 🟢 95% |
| 5 | DATE_END | DATE | NULL | Período | Data de fim da ausência | — | 🟢 95% |
| 6 | ABSENCE_DAYS | NUMBER | NULL | Cálculo | Duração da ausência em dias | — | 🟢 85% |
| 7 | ABSENCE_HOURS | NUMBER | NULL | Cálculo | Duração da ausência em horas | — | 🟢 85% |
| 8 | ABS_ATTENDANCE_REASON_ID | NUMBER(18) | NULL | FK | Motivo da ausência | PER_ABS_ATTENDANCE_REASONS | 🟢 85% |
| 9 | APPROVAL_STATUS | VARCHAR2(30) | NULL | Status | Status de aprovação (PENDING, APPROVED, REJECTED) | — | 🟡 75% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador associado)
- [[per_absence_attendance_types_b]] — via `ABSENCE_ATTENDANCE_TYPE_ID` (tipo de ausência)
- [[per_abs_attendance_reasons]] — via `ABS_ATTENDANCE_REASON_ID` (motivo da ausência)

### Tabelas-filha (FK de saída)
- [[per_assignment_day_absences]] — via `ABSENCE_ATTENDANCE_ID` (detalhamento diário)
- [[per_asg_absence_recording]] — via `ABSENCE_ATTENDANCE_ID` (registro por assignment)

---

## 📎 Uso Típico

### Ausências de um colaborador em período
```sql
SELECT paa.ABSENCE_ATTENDANCE_ID, paa.DATE_START, paa.DATE_END,
       paa.ABSENCE_DAYS, paa.APPROVAL_STATUS
FROM   PER_ABSENCE_ATTENDANCES paa
WHERE  paa.PERSON_ID = :p_person_id
  AND  paa.DATE_START BETWEEN :p_start_date AND :p_end_date;
```

### Filtros comuns
- `APPROVAL_STATUS = 'APPROVED'` — Ausências aprovadas
- `DATE_START >= TRUNC(SYSDATE, 'YEAR')` — Ausências do ano corrente
---

## 🔒 Observações

- Cada registro representa uma ocorrência única de ausência para um colaborador.
- A duração pode ser em dias ou horas dependendo da configuração do tipo de ausência.
- O campo `APPROVAL_STATUS` controla o workflow — apenas ausências aprovadas impactam o payroll.
- Registros podem ser criados via self-service pelo colaborador ou pelo gestor.
---

## 🔗 PVOs Relacionados

### [[absenceeventspvo|AbsenceEventsPVO]] (HCM · BICC: 1/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_ATTENDANCE_REASON_ID | AbsencePEOAbsAttendanceReasonId | — |
| ABS_INFORMATION_CATEGORY | AbsencePEOAbsInformationCategory | — |
| ABSENCE_ATTENDANCE_ID | AbsencePEOAbsenceAttendanceId | — |
| ABSENCE_ATTENDANCE_TYPE_ID | AbsencePEOAbsenceAttendanceTypeId | — |
| ABSENCE_CASE_ID | AbsencePEOAbsenceCaseId | — |
| BATCH_ID | AbsencePEOBatchId | — |
| BUSINESS_GROUP_ID | AbsencePEOBusinessGroupId | — |
| CREATED_BY | AbsencePEOCreatedBy | — |
| CREATION_DATE | AbsencePEOCreationDate | — |
| DATE_END | AbsencePEODateEnd | — |
| DATE_NOTIFICATION | AbsencePEODateNotification | — |
| DATE_PROJECTED_END | AbsencePEODateProjectedEnd | — |
| DATE_PROJECTED_START | AbsencePEODateProjectedStart | — |
| DATE_START | AbsencePEODateStart | — |
| LAST_UPDATE_DATE | AbsencePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AbsencePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AbsencePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AbsencePEOObjectVersionNumber | — |
| PERIOD_OF_INCAPACITY_ID | AbsencePEOPeriodOfIncapacityId | — |
| PERSON_ID | AbsencePEOPersonId | — |
| TIME_END | AbsencePEOTimeEnd | — |
| TIME_PROJECTED_END | AbsencePEOTimeProjectedEnd | — |
| TIME_PROJECTED_START | AbsencePEOTimeProjectedStart | — |
| TIME_START | AbsencePEOTimeStart | — |

### [[absencepvo|AbsencePVO]] (HCM · BICC: 2/24)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_ATTENDANCE_REASON_ID | AbsencePEOAbsAttendanceReasonId | — |
| ABS_INFORMATION_CATEGORY | AbsencePEOAbsInformationCategory | — |
| ABSENCE_ATTENDANCE_ID | AbsenceAttendanceId | ✅ |
| ABSENCE_ATTENDANCE_TYPE_ID | AbsencePEOAbsenceAttendanceTypeId | — |
| ABSENCE_CASE_ID | AbsencePEOAbsenceCaseId | — |
| BATCH_ID | AbsencePEOBatchId | — |
| BUSINESS_GROUP_ID | AbsencePEOBusinessGroupId | — |
| CREATED_BY | AbsencePEOCreatedBy | — |
| CREATION_DATE | AbsencePEOCreationDate | — |
| DATE_END | AbsencePEODateEnd | — |
| DATE_NOTIFICATION | AbsencePEODateNotification | — |
| DATE_PROJECTED_END | AbsencePEODateProjectedEnd | — |
| DATE_PROJECTED_START | AbsencePEODateProjectedStart | — |
| DATE_START | AbsencePEODateStart | — |
| LAST_UPDATE_DATE | AbsencePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | AbsencePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | AbsencePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | AbsencePEOObjectVersionNumber | — |
| PERIOD_OF_INCAPACITY_ID | AbsencePEOPeriodOfIncapacityId | — |
| PERSON_ID | AbsencePEOPersonId | — |
| TIME_END | AbsencePEOTimeEnd | — |
| TIME_PROJECTED_END | AbsencePEOTimeProjectedEnd | — |
| TIME_PROJECTED_START | AbsencePEOTimeProjectedStart | — |
| TIME_START | AbsencePEOTimeStart | — |

---

## 📚 Referências

- [Oracle Docs — PER_ABSENCE_ATTENDANCES](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perabsenceattendances.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
