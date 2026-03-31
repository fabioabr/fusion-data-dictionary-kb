---
id: DOC-HCM-711
doc_type: system-doc
title: "PER_SCHEDULE_ASSIGNMENTS — Atribuições de Agenda/Escala"
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
  - agenda-trabalho
  - schedule
  - escala
  - horario-trabalho
aliases:
  - PER_SCHEDULE_ASSIGNMENTS
  - per_schedule_assignments
  - atribuicoes-agenda
  - escala-trabalho
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_SCHEDULE_ASSIGNMENTS

## Visão Geral

Armazena as **atribuições de agendas/escalas de trabalho** a recursos (pessoas, organizações ou posições). Define qual escala de trabalho está associada a cada entidade, controlando horários de trabalho, dias úteis e turnos.

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de jornada de trabalho** — vincular colaboradores a escalas de trabalho
- **Controle de ponto** — definir o horário esperado para cada colaborador
- **Cálculos de folha** — determinar horas regulares, extras e noturnas
- **Gestão de turnos** — associar escalas rotativas a equipes
- **Planejamento de capacidade** — calcular disponibilidade de recursos
- **Compliance trabalhista** — garantir conformidade com limites de jornada (CLT)

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_ASSIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atribuição | — | 🟡 80% |
| 2 | SCHEDULE_ID | NUMBER(18) | NOT NULL | FK | Referência à escala/agenda de trabalho | — | 🟡 80% |
| 3 | RESOURCE_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo de recurso (PERSON, ORGANIZATION, POSITION) | — | 🟡 75% |
| 4 | RESOURCE_ID | NUMBER(18) | NOT NULL | FK | Identificador do recurso | — | 🟡 75% |
| 5 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Vínculo do colaborador | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 6 | PRIMARY_FLAG | VARCHAR2(1) | NULL | Flag | Indica se é a agenda principal (Y/N) | — | 🟡 70% |
| 7 | EFFECTIVE_START_DATE | DATE | NULL | Vigência | Data de início da vigência | — | 🟡 80% |
| 8 | EFFECTIVE_END_DATE | DATE | NULL | Vigência | Data de fim da vigência | — | 🟡 80% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 13 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista | — | 🟢 90% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vínculo com agenda de trabalho atribuída)

### Tabelas-filha (FK de saída)
- [[per_schedule_exceptions]] — via `SCHEDULE_ASSIGNMENT_ID` (exceções na agenda de trabalho atribuída)
- [[per_resource_exceptions]] — via `SCHEDULE_ID` (exceções de recurso na agenda)

---

## Uso Típico

### Agenda de trabalho atual de um colaborador
```sql
SELECT sa.SCHEDULE_ID, sa.PRIMARY_FLAG
FROM   PER_SCHEDULE_ASSIGNMENTS sa
WHERE  sa.RESOURCE_ID = :p_person_id
  AND  sa.RESOURCE_TYPE = 'PERSON'
  AND  sa.PRIMARY_FLAG = 'Y'
  AND  SYSDATE BETWEEN sa.EFFECTIVE_START_DATE AND sa.EFFECTIVE_END_DATE;
```

---

## Observações

- `RESOURCE_TYPE` permite associar agendas a pessoas, organizações ou posições.
- Uma pessoa pode ter múltiplas agendas; `PRIMARY_FLAG = 'Y'` indica a principal.
- Exceções à agenda são registradas em `PER_SCHEDULE_EXCEPTIONS` e `PER_RESOURCE_EXCEPTIONS`.
- Fundamental para cálculos de jornada e compliance CLT.

---

## Referências

- [Oracle Docs — PER_SCHEDULE_ASSIGNMENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perscheduleassignments.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
