---
id: DOC-HCM-712
doc_type: system-doc
title: "PER_SCHEDULE_EXCEPTIONS — Exceções de Agenda/Escala"
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
  - excecoes-agenda
  - schedule-exceptions
  - horario-trabalho
  - feriado
aliases:
  - PER_SCHEDULE_EXCEPTIONS
  - per_schedule_exceptions
  - excecoes-agenda
  - excecoes-escala
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_SCHEDULE_EXCEPTIONS

## Visão Geral

Armazena as **exceções específicas de agenda/escala** de trabalho. Define alterações pontuais ao padrão de uma escala, como feriados, compensações, dias especiais e alterações de turno para datas específicas.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de feriados na escala** — marcar dias não-úteis em escalas específicas
- **Compensação de jornada** — registrar dias compensados (banco de horas)
- **Alterações de turno** — modificar horário pontualmente para uma data
- **Cálculos de folha** — ajustar horas trabalhadas conforme exceções
- **Planejamento de capacidade** — considerar exceções na disponibilidade

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_EXCEPTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da exceção | — | 🟡 80% |
| 2 | SCHEDULE_ID | NUMBER(18) | NOT NULL | FK | Referência à escala de trabalho | — | 🟡 80% |
| 3 | EXCEPTION_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de exceção (HOLIDAY, COMP_DAY, OVERRIDE) | — | 🟡 75% |
| 4 | EXCEPTION_DATE | DATE | NOT NULL | Data | Data da exceção | — | 🟡 80% |
| 5 | START_TIME | TIMESTAMP | NULL | Horário | Hora de início (exceções parciais) | — | 🟡 65% |
| 6 | END_TIME | TIMESTAMP | NULL | Horário | Hora de fim (exceções parciais) | — | 🟡 65% |
| 7 | HOURS | NUMBER | NULL | Horário | Horas da exceção (para override de jornada) | — | 🟡 65% |
| 8 | SCHEDULE_ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuição de agenda associada | PER_SCHEDULE_ASSIGNMENTS | 🟡 70% |
| 9 | DESCRIPTION | VARCHAR2(240) | NULL | Descritivo | Descrição da exceção | — | 🟡 65% |
| 10 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 11 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 12 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 13 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 14 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_schedule_assignments]] — via `SCHEDULE_ASSIGNMENT_ID` (agenda de trabalho da exceção)

### Tabelas-filha (FK de saída)
- Nenhuma relação direta identificada.

---

## Uso Típico

### Feriados em uma escala no mês corrente
```sql
SELECT se.EXCEPTION_DATE, se.EXCEPTION_TYPE, se.DESCRIPTION
FROM   PER_SCHEDULE_EXCEPTIONS se
WHERE  se.SCHEDULE_ID = :p_schedule_id
  AND  se.EXCEPTION_TYPE = 'HOLIDAY'
  AND  se.EXCEPTION_DATE BETWEEN TRUNC(SYSDATE, 'MM') AND LAST_DAY(SYSDATE);
```

---

## Observações

- Exceções sobrepõem o padrão da escala para datas específicas.
- `EXCEPTION_TYPE = 'HOLIDAY'` marca feriados; `OVERRIDE` altera horários.
- Trabalha em conjunto com `PER_SCHEDULE_ASSIGNMENTS` e `PER_RESOURCE_EXCEPTIONS`.
- Exceções parciais usam `START_TIME`/`END_TIME` para definir o período alterado.

---

## Referências

- [Oracle Docs — PER_SCHEDULE_EXCEPTIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perscheduleexceptions.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
