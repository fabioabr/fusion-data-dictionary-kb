---
id: DOC-HCM-666
doc_type: system-doc
title: "PER_JOBS_F — Cargos (Jobs)"
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
  - cargos
  - jobs
aliases:
  - PER_JOBS_F
  - per_jobs_f
  - per-jobs-f
  - cargos-(jobs)
  - per-jobs-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOBS_F

## 📌 Visão Geral

Armazena a definição dos **cargos (jobs)** da organização, com vigência temporal. Um cargo define uma função genérica que pode ser atribuída a múltiplos colaboradores e posições.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de cargos** — define todos os cargos disponíveis na organização.
- **Classificação funcional** — agrupamento de funções para fins de remuneração e carreira.
- **Recrutamento** — base para descrição de vagas e requisitos.
- **Avaliação de cargo** — associação com avaliações de complexidade e valor.
- **Relatórios organizacionais** — análise da estrutura de cargos.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cargo | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | JOB_CODE | VARCHAR2(30) | NULL | Identificação | Código do cargo | — | 🟢 90% |
| 5 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 6 | JOB_FAMILY_ID | NUMBER(18) | NULL | FK | Família do cargo | PER_JOB_FAMILY_F | 🟢 85% |
| 7 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativo (Y/N) | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_job_family_f]] — via `JOB_FAMILY_ID` (família do cargo)

### Tabelas-filha (FK de saída)
- [[per_jobs_f_tl]] — via `JOB_ID` (traduÃ§Ãµes do cargo)
- [[per_job_evaluations]] — via `JOB_ID` (avaliações do cargo)
- [[per_job_extra_info_f]] — via `JOB_ID` (informações extras)
- [[per_job_leg_f]] — via `JOB_ID` (dados legislativos)
- [[per_all_assignments_m]] — via `JOB_ID` (assignments com este cargo)

---

## 📎 Uso Típico

### Cargos ativos
```sql
SELECT pjf.JOB_ID, pjf.JOB_CODE, pjf.ACTIVE_STATUS
FROM   PER_JOBS_F pjf
WHERE  pjf.ACTIVE_STATUS = 'Y'
  AND  SYSDATE BETWEEN pjf.EFFECTIVE_START_DATE AND pjf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Cargos ativos
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Cargos vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Job é genérico (ex.: 'Analista de Dados') — Position é específica (ex.: 'Analista de Dados - Squad Alpha').
- Cargos são agrupados em famílias (JOB_FAMILY) para fins de classificação e carreira.
- Fundamental para relatórios de headcount por cargo e análise de estrutura organizacional.
---

## 📚 Referências

- [Oracle Docs — PER_JOBS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
