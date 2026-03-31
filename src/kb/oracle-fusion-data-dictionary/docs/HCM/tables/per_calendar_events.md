---
id: DOC-HCM-637
doc_type: system-doc
title: "PER_CALENDAR_EVENTS — Eventos de Calendário"
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
  - workforce-management
  - calendario
  - calendar-events
aliases:
  - PER_CALENDAR_EVENTS
  - per_calendar_events
  - per-calendar-events
  - eventos-de-calendário
  - per-calendar-events
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_CALENDAR_EVENTS

## 📌 Visão Geral

Armazena os **eventos de calendário** utilizados pelo módulo HCM. Define feriados, datas comemorativas e eventos corporativos que impactam o calendário de trabalho.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de feriados** — cadastro de feriados nacionais, estaduais e municipais.
- **Calendário de trabalho** — base para cálculo de dias úteis.
- **Payroll** — determinação de dias trabalhados vs. feriados.
- **Planejamento** — eventos corporativos que impactam a operação.
- **Compliance** — registro de feriados obrigatórios por legislação.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CALENDAR_EVENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único do evento | — | 🟢 95% |
| 2 | EVENT_DATE | DATE | NOT NULL | Período | Data do evento | — | 🟢 90% |
| 3 | EVENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo de evento (HOLIDAY, CORPORATE, etc.) | — | 🟢 85% |
| 4 | LEGISLATION_CODE | VARCHAR2(30) | NULL | Classificação | Código da legislação aplicável | — | 🟢 85% |
| 5 | RECURRING_FLAG | VARCHAR2(1) | NULL | Configuração | Se é recorrente anualmente (Y/N) | — | 🟡 75% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de eventos de calendário.

### Tabelas-filha (FK de saída)
- [[per_calendar_events_tl]] — via `CALENDAR_EVENT_ID` (traduções do evento de calendário)

---

## 📎 Uso Típico

### Feriados de um ano
```sql
SELECT pce.EVENT_DATE, pce.EVENT_TYPE, pce.LEGISLATION_CODE
FROM   PER_CALENDAR_EVENTS pce
WHERE  pce.EVENT_TYPE = 'HOLIDAY'
  AND  EXTRACT(YEAR FROM pce.EVENT_DATE) = :p_year
ORDER BY pce.EVENT_DATE;
```

### Filtros comuns
- `EVENT_TYPE = 'HOLIDAY'` — Feriados
- `LEGISLATION_CODE = 'BR'` — Eventos para legislação brasileira
---

## 🔒 Observações

- Feriados impactam diretamente o cálculo de dias úteis e ausências.
- O `LEGISLATION_CODE` permite feriados específicos por país.
- Eventos recorrentes (`RECURRING_FLAG = 'Y'`) são repetidos automaticamente a cada ano.
---

## 📚 Referências

- [Oracle Docs — PER_CALENDAR_EVENTS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/percalendarevents.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
