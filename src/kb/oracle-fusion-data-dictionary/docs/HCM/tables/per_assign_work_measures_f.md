---
id: DOC-HCM-636
doc_type: system-doc
title: "PER_ASSIGN_WORK_MEASURES_F — Medidas de Trabalho por Assignment"
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
  - fte
  - work-measures
aliases:
  - PER_ASSIGN_WORK_MEASURES_F
  - per_assign_work_measures_f
  - per-assign-work-measures-f
  - medidas-de-trabalho-por-assignment
  - per-assign-work-meas
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_ASSIGN_WORK_MEASURES_F

## 📌 Visão Geral

Armazena as **medidas de trabalho** associadas a assignments, com vigência temporal. Define parâmetros como FTE (Full-Time Equivalent), jornada de trabalho, headcount e outras métricas de workforce.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **FTE** — define o equivalente de tempo integral do colaborador.
- **Jornada de trabalho** — horas semanais/mensais contratadas.
- **Headcount** — peso do colaborador para contagem de quadro.
- **Relatórios de workforce** — métricas precisas para planejamento.
- **Compliance trabalhista** — registro de jornada contratual.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ASSIGN_WORK_MEASURE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da medida | — | 🟢 90% |
| 2 | ASSIGNMENT_ID | NUMBER(18) | NOT NULL | FK | Assignment associado | PER_ALL_ASSIGNMENTS_M | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | UNIT | VARCHAR2(30) | NOT NULL | Classificação | Unidade de medida (FTE, HEADCOUNT, HOURS) | — | 🟢 85% |
| 6 | VALUE | NUMBER | NOT NULL | Dados | Valor da medida | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_assignments_m]] — via `ASSIGNMENT_ID` (vÃ­nculo da medida de trabalho)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### FTE atual de um assignment
```sql
SELECT pawm.UNIT, pawm.VALUE
FROM   PER_ASSIGN_WORK_MEASURES_F pawm
WHERE  pawm.ASSIGNMENT_ID = :p_assignment_id
  AND  pawm.UNIT = 'FTE'
  AND  SYSDATE BETWEEN pawm.EFFECTIVE_START_DATE AND pawm.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `UNIT = 'FTE'` — Full-Time Equivalent
- `UNIT = 'HEADCOUNT'` — Peso de headcount
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- O FTE=1.0 indica jornada integral; 0.5 indica meio período.
- O HEADCOUNT normalmente é 1 para cada assignment ativo.
- Fundamental para relatórios de planejamento de workforce.
---

## 📚 Referências

- [Oracle Docs — PER_ASSIGN_WORK_MEASURES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perassignworkmeasuresf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
