---
id: DOC-HCM-377
doc_type: system-doc
title: "HWM_TM_HIS_ABS_ENTRY_V — View Histórica de Entradas de Ausência"
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
  - time-management
  - absence-entry
  - historico-ausencia
  - view
aliases:
  - HWM_TM_HIS_ABS_ENTRY_V
  - hwm_tm_his_abs_entry_v
  - hwm-tm-his-abs-entry-v
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HWM_TM_HIS_ABS_ENTRY_V

## 📌 Visão Geral

View que apresenta o **histórico de entradas de ausência** no módulo Time Management. Consolida informações de registros de ausência com detalhes temporais para consultas históricas.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto é uma **view** — consulta pré-definida sobre tabelas base, somente leitura.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Consulta histórica:** visualizar entradas de ausência já processadas ou encerradas.
- **Relatórios de absenteismo:** base para análises de tendências de ausência.
- **Auditoria:** rastreabilidade completa de entradas de ausência anteriores.
- **Integração com BI:** fonte para dashboards de gestão de pessoas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Identificador do colaborador | PER_ALL_PEOPLE_F | 🟡 70% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NULL | FK | Identificador da atribuição/cargo | PER_ALL_ASSIGNMENTS_M | 🟡 70% |
| 3 | ABSENCE_ENTRY_ID | NUMBER(18) | NOT NULL | PK | Identificador da entrada de ausência | — | 🟡 65% |
| 4 | ABSENCE_TYPE_ID | NUMBER(18) | NULL | FK | Tipo de ausência | ANC_ABSENCE_TYPES_F | 🟡 65% |
| 5 | START_DATE | DATE | NOT NULL | Período | Data de início da ausência | — | 🟡 70% |
| 6 | END_DATE | DATE | NULL | Período | Data de término da ausência | — | 🟡 70% |
| 7 | DURATION | NUMBER | NULL | Dados | Duração da ausência em dias/horas | — | 🟡 60% |
| 8 | STATUS | VARCHAR2(30) | NULL | Classificação | Status da entrada | — | 🟡 65% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (dados do colaborador)
- [[anc_absence_types_f]] — via `ABSENCE_TYPE_ID` (tipo de ausência)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha (view somente leitura).

---

## 📎 Uso Típico

### Histórico de ausências por colaborador
```sql
SELECT v.PERSON_ID, v.START_DATE, v.END_DATE,
       v.DURATION, v.STATUS
FROM   HWM_TM_HIS_ABS_ENTRY_V v
WHERE  v.PERSON_ID = :p_person_id
ORDER BY v.START_DATE DESC;
```

### Filtros comuns
- `PERSON_ID = :p_person_id — Filtrar por colaborador`
- `START_DATE BETWEEN :dt_ini AND :dt_fim — Filtrar por período`

---

## 🔒 Observações

- View somente leitura — não suporta DML.
- Consolida dados históricos; para entradas ativas, utilizar a tabela base.

---

## 📚 Referências

- [Oracle Docs — HWM_TM_HIS_ABS_ENTRY_V](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/hwmtmhisabsentryv.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
