---
id: DOC-HCM-404
doc_type: system-doc
title: "HWM_TM_RPT_ENTRY_V — View de Entradas Reportadas de Tempo"
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
  - reported-entry
  - entradas-reportadas
  - view
aliases:
  - HWM_TM_RPT_ENTRY_V
  - hwm_tm_rpt_entry_v
  - hwm-tm-rpt-entry-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_RPT_ENTRY_V

## 📌 Visao Geral

View que apresenta as **entradas reportadas de tempo** (reported time entries) no modulo Time Management. Consolida entradas que foram submetidas para processamento.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view** — consulta pre-definida sobre tabelas base, somente leitura.

---

## 🧠 Proposito de Negocio

Esta tabela e utilizada nos seguintes processos:

- **Consulta de entradas reportadas:** visualizar time entries submetidas ao payroll.
- **Reconciliacao:** verificar entradas reportadas vs. folha processada.
- **Relatorios:** base para analise de horas reportadas por periodo.

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
| 2 | RPT_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador da entrada reportada | — | 🟡 65% |
| 3 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Atribuicao | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 4 | ENTRY_DATE | DATE | NOT NULL | Periodo | Data da entrada | — | 🟡 70% |
| 5 | MEASURE | NUMBER | NULL | Dados | Quantidade reportada | — | 🟡 60% |
| 6 | ELEMENT_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de elemento de pagamento | — | 🟡 55% |
| 7 | STATUS | VARCHAR2(30) | NULL | Classificacao | Status do reporte | — | 🟡 65% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario que criou | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criacao | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (pessoa do lancamento de reporte de tempo)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vinculo do lancamento de reporte de tempo)

### Tabelas-filha (FK de saida)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Tipico

### Entradas reportadas por colaborador e periodo
```sql
SELECT v.PERSON_ID, v.ENTRY_DATE, v.MEASURE, v.STATUS
FROM   HWM_TM_RPT_ENTRY_V v
WHERE  v.PERSON_ID = :p_person_id
  AND  v.ENTRY_DATE BETWEEN :dt_ini AND :dt_fim;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Por colaborador`
- `ENTRY_DATE BETWEEN :dt_ini AND :dt_fim — Periodo`

---

## 🔒 Observacoes

- View somente leitura — nao suporta DML.
- Foco em entradas ja reportadas ao payroll.

---

## 📚 Referencias

- [Oracle Docs — HWM_TM_RPT_ENTRY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmrptentryv.html)
- [[hcm-module-data-dictionary]] — Dossie do modulo HCM
