---
id: DOC-HCM-668
doc_type: system-doc
title: "PER_JOB_EVALUATIONS — Avaliações de Cargo"
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
  - compensation
  - avaliacoes
  - job-evaluations
aliases:
  - PER_JOB_EVALUATIONS
  - per_job_evaluations
  - per-job-evaluations
  - avaliações-de-cargo
  - per-job-evaluations
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_JOB_EVALUATIONS

## 📌 Visão Geral

Armazena as **avaliações de cargo (job evaluations)** realizadas sobre os cargos da organização. Define a pontuação e classificação de cada cargo segundo metodologia de avaliação utilizada.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Avaliação de cargos** — pontuação e classificação por metodologia (Hay, Mercer, etc.).
- **Estrutura de remuneração** — base para vinculação de grades salariais a cargos.
- **Equidade interna** — garantia de justiça na classificação de cargos.
- **Benchmark** — comparação com mercado baseada em avaliação padronizada.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | JOB_EVALUATION_ID | NUMBER(18) | NOT NULL | PK | Identificador único da avaliação | — | 🟢 90% |
| 2 | JOB_ID | NUMBER(18) | NOT NULL | FK | Cargo avaliado | PER_JOBS_F | 🟢 90% |
| 3 | EVALUATION_SYSTEM | VARCHAR2(30) | NULL | Classificação | Sistema de avaliação (HAY, MERCER, etc.) | — | 🟡 75% |
| 4 | TOTAL_POINTS | NUMBER | NULL | Dados | Pontuação total | — | 🟢 85% |
| 5 | EVALUATION_DATE | DATE | NULL | Período | Data da avaliação | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (cargo avaliado na avaliação de cargo)

### Tabelas-filha (FK de saída)
- - Nenhuma tabela-filha direta identificada.

---

## 📎 Uso Típico

### Avaliações de um cargo
```sql
SELECT pje.EVALUATION_SYSTEM, pje.TOTAL_POINTS, pje.EVALUATION_DATE
FROM   PER_JOB_EVALUATIONS pje
WHERE  pje.JOB_ID = :p_job_id
ORDER BY pje.EVALUATION_DATE DESC;
```

### Filtros comuns
- `EVALUATION_SYSTEM = 'HAY'` — Avaliações pelo sistema Hay
---

## 🔒 Observações

- A pontuação total é usada para classificar cargos e associá-los a grades salariais.
- O histórico de avaliações permite rastrear reclassificações ao longo do tempo.
- Integra-se com políticas de remuneração para garantir equidade interna.
---

## 🔗 PVOs Relacionados

### [[jobpvo|JobPVO]] (HCM · BICC: 13/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTABILITY | JobEvaluationPEOAccountability | ✅ |
| BUSINESS_GROUP_ID | JobEvaluationPEOBusinessGroupId | — |
| CREATED_BY | JobEvaluationPEOCreatedBy | ✅ |
| CREATION_DATE | JobEvaluationPEOCreationDate | ✅ |
| DATE_EVALUATED | JobEvaluationPEODateEvaluated | ✅ |
| EVALUATION_SYSTEM | JobEvaluationPEOEvaluationSystem | ✅ |
| JOB_EVALUATION_ID | JobEvaluationPEOJobEvaluationId | ✅ |
| JOB_ID | JobEvaluationPEOJobId | — |
| KNOWHOW | JobEvaluationPEOKnowhow | ✅ |
| LAST_UPDATE_DATE | JobEvaluationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobEvaluationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobEvaluationPEOLastUpdatedBy | ✅ |
| MEASURED_IN | JobEvaluationPEOMeasuredIn | ✅ |
| OBJECT_VERSION_NUMBER | JobEvaluationPEOObjectVersionNumber | — |
| OVERALL_SCORE | JobEvaluationPEOOverallScore | ✅ |
| POSITION_ID | JobEvaluationPEOPositionId | ✅ |
| PROBLEM_SOLVING | JobEvaluationPEOProblemSolving | ✅ |
| WORKING_CONDITIONS | JobEvaluationPEOWorkingConditions | — |

### [[jobpvoviewall|JobPVOViewAll]] (HCM · BICC: 1/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTABILITY | JobEvaluationPEOAccountability | — |
| BUSINESS_GROUP_ID | JobEvaluationPEOBusinessGroupId | — |
| CREATED_BY | JobEvaluationPEOCreatedBy | — |
| CREATION_DATE | JobEvaluationPEOCreationDate | — |
| DATE_EVALUATED | JobEvaluationPEODateEvaluated | — |
| EVALUATION_SYSTEM | JobEvaluationPEOEvaluationSystem | — |
| JOB_EVALUATION_ID | JobEvaluationPEOJobEvaluationId | — |
| JOB_ID | JobEvaluationPEOJobId | — |
| KNOWHOW | JobEvaluationPEOKnowhow | — |
| LAST_UPDATE_DATE | JobEvaluationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobEvaluationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobEvaluationPEOLastUpdatedBy | — |
| MEASURED_IN | JobEvaluationPEOMeasuredIn | — |
| OBJECT_VERSION_NUMBER | JobEvaluationPEOObjectVersionNumber | — |
| OVERALL_SCORE | JobEvaluationPEOOverallScore | — |
| POSITION_ID | JobEvaluationPEOPositionId | — |
| PROBLEM_SOLVING | JobEvaluationPEOProblemSolving | — |
| WORKING_CONDITIONS | JobEvaluationPEOWorkingConditions | — |

### [[positionpvo|PositionPVO]] (PO · BICC: 12/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTABILITY | JobEvaluationPEOAccountability | ✅ |
| BUSINESS_GROUP_ID | JobEvaluationPEOBusinessGroupId | — |
| CREATED_BY | JobEvaluationPEOCreatedBy | ✅ |
| CREATION_DATE | JobEvaluationPEOCreationDate | ✅ |
| DATE_EVALUATED | JobEvaluationPEODateEvaluated | ✅ |
| EVALUATION_SYSTEM | JobEvaluationPEOEvaluationSystem | ✅ |
| JOB_EVALUATION_ID | JobEvaluationPEOJobEvaluationId | ✅ |
| JOB_ID | JobEvaluationPEOJobId | — |
| KNOWHOW | JobEvaluationPEOKnowhow | ✅ |
| LAST_UPDATE_DATE | JobEvaluationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobEvaluationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobEvaluationPEOLastUpdatedBy | ✅ |
| MEASURED_IN | JobEvaluationPEOMeasuredIn | ✅ |
| OBJECT_VERSION_NUMBER | JobEvaluationPEOObjectVersionNumber | — |
| OVERALL_SCORE | JobEvaluationPEOOverallScore | ✅ |
| POSITION_ID | JobEvaluationPEOPositionId | — |
| PROBLEM_SOLVING | JobEvaluationPEOProblemSolving | ✅ |
| WORKING_CONDITIONS | JobEvaluationPEOWorkingConditions | — |

### [[positionpvoviewall|PositionPVOViewAll]] (PO · BICC: 12/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCOUNTABILITY | JobEvaluationPEOAccountability | ✅ |
| BUSINESS_GROUP_ID | JobEvaluationPEOBusinessGroupId | — |
| CREATED_BY | JobEvaluationPEOCreatedBy | ✅ |
| CREATION_DATE | JobEvaluationPEOCreationDate | ✅ |
| DATE_EVALUATED | JobEvaluationPEODateEvaluated | ✅ |
| EVALUATION_SYSTEM | JobEvaluationPEOEvaluationSystem | ✅ |
| JOB_EVALUATION_ID | JobEvaluationPEOJobEvaluationId | ✅ |
| JOB_ID | JobEvaluationPEOJobId | — |
| KNOWHOW | JobEvaluationPEOKnowhow | ✅ |
| LAST_UPDATE_DATE | JobEvaluationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | JobEvaluationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | JobEvaluationPEOLastUpdatedBy | ✅ |
| MEASURED_IN | JobEvaluationPEOMeasuredIn | ✅ |
| OBJECT_VERSION_NUMBER | JobEvaluationPEOObjectVersionNumber | — |
| OVERALL_SCORE | JobEvaluationPEOOverallScore | ✅ |
| POSITION_ID | JobEvaluationPEOPositionId | — |
| PROBLEM_SOLVING | JobEvaluationPEOProblemSolving | ✅ |
| WORKING_CONDITIONS | JobEvaluationPEOWorkingConditions | — |

---

## 📚 Referências

- [Oracle Docs — PER_JOB_EVALUATIONS](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/perjobevaluations.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
