---
id: DOC-HCM-411
doc_type: system-doc
title: "HXT_SCH_PROF_DEFAULT_VIEW — View Padrao de Perfis de Agenda"
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
  - schedule-profile
  - perfil-agenda
  - view
aliases:
  - HXT_SCH_PROF_DEFAULT_VIEW
  - hxt_sch_prof_default_view
  - hxt-sch-prof-default-view
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HXT_SCH_PROF_DEFAULT_VIEW

## 📌 Visao Geral

View que apresenta os **perfis padrao de agenda** (schedule profiles) no modulo Time & Labor (HXT). Define templates de horario de trabalho reutilizaveis.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Templates de agenda:** define perfis reutilizaveis de horario de trabalho.
- **Padronizacao:** permite atribuir o mesmo perfil de horario a multiplos colaboradores.
- **Configuracao centralizada:** gerencia agendas de forma centralizada.

---

## ⚙️ Colunas Principais

> [!tip] Confianca
> Escala de 0% a 100% — grau de certeza da descricao gerada por IA com base na documentacao oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentacao oficial Oracle; nome, tipo e descricao confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrao Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existencia ou tipo incertos; pode nao existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SCHEDULE_PROFILE_ID | NUMBER(18) | NOT NULL | PK | Identificador do perfil | — | 🟡 65% |
| 2 | PROFILE_NAME | VARCHAR2(240) | NULL | Identificacao | Nome do perfil de agenda | — | 🟡 60% |
| 3 | SCHEDULE_TYPE | VARCHAR2(30) | NULL | Classificacao | Tipo de agenda | — | 🟡 55% |
| 4 | HOURS_PER_DAY | NUMBER | NULL | Dados | Horas padrao por dia | — | 🟡 55% |
| 5 | DAYS_PER_WEEK | NUMBER | NULL | Dados | Dias por semana | — | 🟡 55% |
| 6 | START_TIME | VARCHAR2(8) | NULL | Dados | Horario de inicio padrao | — | 🟡 50% |
| 7 | END_TIME | VARCHAR2(8) | NULL | Dados | Horario de termino padrao | — | 🟡 50% |
| 8 | ENABLED_FLAG | VARCHAR2(1) | NULL | Controle | Indicador ativo/inativo | — | 🟡 60% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- Nenhuma tabela-pai documentada neste release.

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Perfis de agenda ativos
```sql
SELECT v.SCHEDULE_PROFILE_ID, v.PROFILE_NAME,
       v.HOURS_PER_DAY, v.DAYS_PER_WEEK
FROM   HXT_SCH_PROF_DEFAULT_VIEW v
WHERE  v.ENABLED_FLAG = 'Y';
```

### Filtros comuns
- `ENABLED_FLAG = 'Y' — Perfis ativos`
- `SCHEDULE_TYPE = :p_type — Por tipo de agenda`

---

## 🔒 Observacoes

- View somente leitura.
- Define templates padrao de jornada de trabalho.
- Perfis podem ser associados a organizacoes ou atribuicoes individuais.

---

## 📚 Referencias

- [Oracle Docs — HXT_SCH_PROF_DEFAULT_VIEW](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hxtschprofdefaultview.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
