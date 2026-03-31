---
id: DOC-HCM-672
doc_type: system-doc
title: "PER_JOB_LEG_F — Dados Legislativos de Cargo"
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
  - legislacao
  - cbo
  - job-legislation
aliases:
  - PER_JOB_LEG_F
  - per_job_leg_f
  - per-job-leg-f
  - dados-legislativos-de-cargo
  - per-job-leg-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOB_LEG_F

## 📌 Visão Geral

Armazena **dados legislativos** (legais) associados aos cargos, com vigência temporal. Contém informações específicas da legislação trabalhista de cada país, como classificações oficiais de ocupação.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Compliance** — dados de classificação oficial do cargo por legislação.
- **CBO** — Classificação Brasileira de Ocupações (no Brasil).
- **Relatórios legais** — dados para declarações obrigatórias (RAIS, eSocial).
- **Requisitos regulatórios** — informações exigidas pela legislação trabalhista de cada país.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_LEG_ID | NUMBER(18) | NOT NULL | PK | Identificador único do registro legislativo | — | 🟢 90% |
| 2 | JOB_ID | NUMBER(18) | NOT NULL | FK | Cargo associado | PER_JOBS_F | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | LEGISLATION_CODE | VARCHAR2(30) | NOT NULL | Classificação | Código da legislação | — | 🟢 90% |
| 6 | JOB_LEG_ATTRIBUTE1 | VARCHAR2(150) | NULL | Dados | Atributo legislativo 1 (ex.: CBO) | — | 🟢 85% |
| 7 | JOB_LEG_ATTRIBUTE2 | VARCHAR2(150) | NULL | Dados | Atributo legislativo 2 | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 12 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (cargo com informações legislativas)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Dados legislativos de um cargo
```sql
SELECT pjl.LEGISLATION_CODE, pjl.JOB_LEG_ATTRIBUTE1 AS CBO_CODE
FROM   PER_JOB_LEG_F pjl
WHERE  pjl.JOB_ID = :p_job_id
  AND  pjl.LEGISLATION_CODE = 'BR'
  AND  SYSDATE BETWEEN pjl.EFFECTIVE_START_DATE AND pjl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `LEGISLATION_CODE = 'BR'` — Dados para legislação brasileira
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- No Brasil, o atributo legislativo principal é o código CBO (Classificação Brasileira de Ocupações).
- Fundamental para integração com eSocial e declarações trabalhistas obrigatórias.
- Os campos JOB_LEG_ATTRIBUTE1..N são flexíveis — significado varia por legislação.
---

## 📚 Referências

- [Oracle Docs — PER_JOB_LEG_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjoblegf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
