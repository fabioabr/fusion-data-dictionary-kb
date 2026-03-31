---
id: DOC-HCM-709
doc_type: system-doc
title: "PER_RESOURCE_EXCEPTIONS — Exceções de Recursos/Agenda"
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
  - excecoes-recursos
  - resource-exceptions
  - agenda
  - horario-trabalho
aliases:
  - PER_RESOURCE_EXCEPTIONS
  - per_resource_exceptions
  - excecoes-recursos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_RESOURCE_EXCEPTIONS

## Visão Geral

Armazena as **exceções de recursos/agenda** no sistema. Define períodos onde um recurso (pessoa ou equipamento) está indisponível ou tem horário diferenciado em relação ao padrão, como feriados, manutenção programada ou ausências planejadas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de feriados** — registrar exceções ao calendário padrão de trabalho
- **Planejamento de capacidade** — considerar indisponibilidades na alocação de recursos
- **Cálculos de folha** — identificar dias não-úteis para cálculos de horas trabalhadas
- **Agendamento de projetos** — ajustar cronogramas conforme exceções
- **Gestão de turnos** — exceções a escalas de trabalho regulares

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESOURCE_EXCEPTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da exceção | — | 🟡 75% |
| 2 | RESOURCE_ID | NUMBER(18) | NULL | FK | Recurso associado (pessoa ou equipamento) | — | 🟡 70% |
| 3 | EXCEPTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de exceção (HOLIDAY, UNAVAILABLE, OVERRIDE) | — | 🟡 70% |
| 4 | EXCEPTION_DATE | DATE | NOT NULL | Data | Data da exceção | — | 🟡 75% |
| 5 | START_TIME | TIMESTAMP | NULL | Horário | Hora de início (para exceções parciais) | — | 🟡 65% |
| 6 | END_TIME | TIMESTAMP | NULL | Horário | Hora de fim (para exceções parciais) | — | 🟡 65% |
| 7 | SCHEDULE_ID | NUMBER(18) | NULL | FK | Agenda/escala associada | PER_SCHEDULE_ASSIGNMENTS | 🟡 65% |
| 8 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descrição da exceção | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_schedule_assignments]] — via `SCHEDULE_ID` (agenda de trabalho da exceção de recurso)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Exceções (feriados) em um período
```sql
SELECT re.EXCEPTION_DATE, re.EXCEPTION_TYPE, re.DESCRIPTION
FROM   PER_RESOURCE_EXCEPTIONS re
WHERE  re.EXCEPTION_TYPE = 'HOLIDAY'
  AND  re.EXCEPTION_DATE BETWEEN :p_start_date AND :p_end_date;
```

---

## Observações

- Exceções podem ser de dia inteiro ou parciais (com `START_TIME`/`END_TIME`).
- Utilizada em conjunto com `PER_SCHEDULE_ASSIGNMENTS` e `PER_SCHEDULE_EXCEPTIONS`.
- Feriados nacionais e regionais são registrados como exceções.

---

## Referências

- [Oracle Docs — PER_RESOURCE_EXCEPTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perresourceexceptions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[scheduleexceptionpvo|ScheduleExceptionPVO]] (GL · BICC: 4/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| AVAILABILITY_CODE | ResourceExceptionPEOAvailabilityCode | — |
| CREATED_BY | ResourceExceptionPEOCreatedBy | — |
| CREATION_DATE | ResourceExceptionPEOCreationDate | — |
| END_DATE_TIME | ResourceExceptionPEOEndDateTime | ✅ |
| ENTERPRISE_ID | ResourceExceptionPEOEnterpriseId | — |
| EXCEPTION_ID | ResourceExceptionPEOExceptionId | — |
| EXCEPTION_NAME | ResourceExceptionPEOExceptionName | ✅ |
| LAST_UPDATE_DATE | ResourceExceptionPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ResourceExceptionPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ResourceExceptionPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | ResourceExceptionPEOObjectVersionNumber | — |
| START_DATE_TIME | ResourceExceptionPEOStartDateTime | ✅ |
