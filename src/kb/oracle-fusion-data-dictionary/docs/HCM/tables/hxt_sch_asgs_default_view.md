---
id: DOC-HCM-410
doc_type: system-doc
title: "HXT_SCH_ASGS_DEFAULT_VIEW — View Padrao de Agendas por Atribuicao"
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
  - schedule
  - agenda-padrao
  - view
aliases:
  - HXT_SCH_ASGS_DEFAULT_VIEW
  - hxt_sch_asgs_default_view
  - hxt-sch-asgs-default-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SCH_ASGS_DEFAULT_VIEW

## 📌 Visao Geral

View que apresenta as **agendas padrao (schedules) por atribuicao** no modulo Time & Labor (HXT). Associa colaboradores a suas agendas de trabalho configuradas.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Agenda padrao:** identifica a agenda de trabalho atribuida a cada colaborador.
- **Calculo de horas:** base para determinar horas regulares vs. extras.
- **Configuracao de jornada:** define o padrao de horario de trabalho.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 65% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | PER_ALL_PEOPLE_F | 🟡 65% |
| 3 | SCHEDULE_ID | NUMBER(18) | NULL | FK | Agenda de trabalho | — | 🟡 60% |
| 4 | SCHEDULE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome da agenda | — | 🟡 55% |
| 5 | EFFECTIVE_START_DATE | DATE | NULL | Vigencia | Inicio da vigencia | — | 🟡 60% |
| 6 | EFFECTIVE_END_DATE | DATE | NULL | Vigencia | Fim da vigencia | — | 🟡 60% |
| 7 | SCHEDULE_SOURCE | VARCHAR2(30) | NULL | Classificacao | Fonte da agenda | — | 🟡 55% |
| 8 | HOURS_PER_DAY | NUMBER | NULL | Dados | Horas por dia | — | 🟡 50% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo da escala de trabalho padrao)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa da escala de trabalho padrao)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Agenda padrao por colaborador
```sql
SELECT v.PERSON_ID, v.SCHEDULE_NAME, v.HOURS_PER_DAY,
       v.EFFECTIVE_START_DATE, v.EFFECTIVE_END_DATE
FROM   HXT_SCH_ASGS_DEFAULT_VIEW v
WHERE  v.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN v.EFFECTIVE_START_DATE AND v.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE — Vigente`

---

## 🔒 Observacoes

- View somente leitura.
- Retorna a agenda padrao configurada para cada atribuicao.
- Essencial para calculo de horas regulares e extras.

---

## 📚 Referencias

- [Oracle Docs — HXT_SCH_ASGS_DEFAULT_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtschasgsdefaultview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
