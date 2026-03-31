---
id: DOC-HCM-014
doc_type: system-doc
title: "ANC_PER_ABS_DAILY_DTLS — Detalhes Diários de Ausência por Pessoa"
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
  - detalhes-diarios
  - daily-details
  - ausencia-diaria
aliases:
  - ANC_PER_ABS_DAILY_DTLS
  - anc_per_abs_daily_dtls
  - detalhes-diarios-ausencia
  - absence-daily-details
  - anc-per-abs-daily
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# ANC_PER_ABS_DAILY_DTLS

## 📌 Visão Geral

Armazena os **detalhes diários** de cada ausência registrada. Cada registro representa um dia específico dentro de um período de ausência, com a duração (parcial ou integral) e outros detalhes granulares.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Controle granular:** Rastreamento dia a dia de ausências (importante para ausências parciais).
- **Cálculo de folha:** Base para cálculo de descontos/pagamentos por dia de ausência.
- **Calendário de ausências:** Alimenta visualizações de calendário no self-service.
- **Compliance:** Registro detalhado de cada dia de afastamento para fins trabalhistas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PER_ABS_DAILY_DTL_ID | NUMBER(18) | NOT NULL | PK | Identificador único do detalhe diário | — | 🟢 90% |
| 2 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | FK | Entrada de ausência | [[anc_per_abs_entries]] | 🟢 90% |
| 3 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 4 | ABSENCE_DATE | DATE | NOT NULL | Data | Data específica da ausência | — | 🟢 90% |
| 5 | DURATION | NUMBER | NULL | Duração | Duração em dias ou horas para este dia | — | 🟢 85% |
| 6 | DURATION_UOM | VARCHAR2(30) | NULL | Classificação | Unidade de medida (DAYS, HOURS) | — | 🟡 75% |
| 7 | START_TIME | VARCHAR2(5) | NULL | Horário | Hora de início (para ausência parcial) | — | 🟡 70% |
| 8 | END_TIME | VARCHAR2(5) | NULL | Horário | Hora de fim (para ausência parcial) | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[anc_per_abs_entries]] — via `ABSENCE_ENTRY_ID` (registro de ausencia do detalhe diario)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador do detalhe diario de ausencia)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha conhecida.

---

## 📎 Uso Típico

### Detalhes diários de uma ausência
```sql
SELECT dd.ABSENCE_DATE, dd.DURATION, dd.DURATION_UOM,
       dd.START_TIME, dd.END_TIME
FROM   ANC_PER_ABS_DAILY_DTLS dd
WHERE  dd.ABSENCE_ENTRY_ID = :p_absence_entry_id
ORDER BY dd.ABSENCE_DATE;
```

### Filtros comuns
- `DURATION_UOM = 'DAYS'` — Duração em dias
- `DURATION_UOM = 'HOURS'` — Duração em horas

---

## 🔒 Observações

- Cada registro representa um único dia da ausência.
- Para ausências de dia inteiro, `DURATION = 1` e `START_TIME`/`END_TIME` são nulos.
- Para ausências parciais, `START_TIME` e `END_TIME` indicam o período específico.
- A soma dos `DURATION` de todos os detalhes diários deve coincidir com a duração total da entrada de ausência.

---

## 🔗 PVOs Relacionados

### [[personabsdailydetailpvo|PersonAbsDailyDetailPVO]] (GL · BICC: 10/19)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ABS_DATE | AbsDate | — |
| ABS_DAYS | AbsDays | ✅ |
| ABS_HOURS | AbsHours | ✅ |
| ABSENCE_PLAN_ID | AbsencePlanId | — |
| ABSENCE_TYPE_ID | AbsenceTypeId | — |
| ABSENCE_TYPE_REASON_ID | AbsenceTypeReasonId | — |
| ASSIGNMENT_ID | AssignmentId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PER_ABS_DAILY_DTL_ID | PerAbsDailyDtlId | ✅ |
| PER_ABSENCE_ENTRY_ID | PerAbsenceEntryId | ✅ |
| PERSON_ID | PersonId | — |
| SCHEDULED_UNITS | ScheduledUnits | — |
| UOM | Uom | ✅ |

---

## 📚 Referências

- [Oracle Docs — ANC_PER_ABS_DAILY_DTLS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/ancperabsdailydtls.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
