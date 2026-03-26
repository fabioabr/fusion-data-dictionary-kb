---
id: DOC-HCM-409
doc_type: system-doc
title: "HWM_TM_SUBMITTED_TS_V — View de Time Sheets Submetidos"
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
  - time-management
  - submitted-timesheet
  - folha-ponto-submetida
  - view
aliases:
  - HWM_TM_SUBMITTED_TS_V
  - hwm_tm_submitted_ts_v
  - hwm-tm-submitted-ts-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_SUBMITTED_TS_V

## 📌 Visao Geral

View que apresenta os **time sheets (folhas de ponto) submetidos** no modulo Time Management. Consolida informacoes de time cards que ja foram submetidos para aprovacao.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Acompanhamento de submissoes:** visualizar time sheets ja submetidos.
- **Workflow de aprovacao:** base para processos de aprovacao de ponto.
- **Relatorios:** analise de time sheets pendentes de aprovacao.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 2 | TIMESHEET_ID | NUMBER(18) | NOT NULL | PK | Identificador do time sheet | — | 🟡 65% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | PERIOD_START_DATE | DATE | NOT NULL | Periodo | Inicio do periodo | — | 🟡 65% |
| 5 | PERIOD_END_DATE | DATE | NOT NULL | Periodo | Fim do periodo | — | 🟡 65% |
| 6 | SUBMISSION_DATE | TIMESTAMP | NULL | Periodo | Data/hora da submissao | — | 🟡 60% |
| 7 | TOTAL_HOURS | NUMBER | NULL | Dados | Total de horas no time sheet | — | 🟡 60% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do time sheet | — | 🟡 65% |
| 9 | APPROVER_ID | NUMBER(18) | NULL | FK | Aprovador designado | PER_ALL_PEOPLE_F | 🟡 55% |
| 10 | APPROVAL_DATE | TIMESTAMP | NULL | Periodo | Data da aprovacao | — | 🟡 55% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do timesheet submetido)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do timesheet submetido)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Time sheets submetidos pendentes de aprovacao
```sql
SELECT v.PERSON_ID, v.PERIOD_START_DATE, v.PERIOD_END_DATE,
       v.TOTAL_HOURS, v.STATUS
FROM   HWM_TM_SUBMITTED_TS_V v
WHERE  v.STATUS = 'SUBMITTED'
  AND  v.APPROVER_ID = :p_approver_id;
```

### Filtros comuns
- `STATUS = 'SUBMITTED' — Pendentes de aprovacao`
- `APPROVER_ID = :p_approver — Por aprovador`
- `PERIOD_START_DATE >= :dt_ini — Periodo`

---

## 🔒 Observacoes

- View somente leitura — nao suporta DML.
- Utilizada para workflow de aprovacao de time sheets.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_SUBMITTED_TS_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmsubmittedtsv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
