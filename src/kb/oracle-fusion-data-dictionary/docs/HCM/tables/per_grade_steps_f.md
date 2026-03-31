---
id: DOC-HCM-664
doc_type: system-doc
title: "PER_GRADE_STEPS_F — Steps de Grade Salarial"
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
  - steps
  - grade-steps
aliases:
  - PER_GRADE_STEPS_F
  - per_grade_steps_f
  - per-grade-steps-f
  - steps-de-grade-salarial
  - per-grade-steps-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADE_STEPS_F

## 📌 Visão Geral

Armazena os **steps (degraus)** dentro de cada grade salarial, com vigência temporal. Cada step representa um valor específico dentro da faixa salarial da grade.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Progressão intra-grade** — define os degraus salariais dentro de cada grade.
- **Remuneração** — cada step tem um valor monetário associado.
- **Políticas de merit increase** — progressão automática ou por mérito entre steps.
- **Equidade salarial** — transparência na política de remuneração por grade e step.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_STEP_ID | NUMBER(18) | NOT NULL | PK | Identificador único do step | — | 🟢 95% |
| 2 | GRADE_ID | NUMBER(18) | NOT NULL | FK | Grade salarial | PER_GRADES_F | 🟢 90% |
| 3 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 4 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 5 | STEP_VALUE | NUMBER | NULL | Dados | Valor monetário do step | — | 🟢 85% |
| 6 | SEQUENCE | NUMBER | NULL | Configuração | Ordem do step na grade | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_grades_f]] — via `GRADE_ID` (grade salarial do step)

### Tabelas-filha (FK de saída)
- [[per_grade_steps_f_tl]] — via `GRADE_STEP_ID` (traduções do step de grade salarial)
- [[per_assign_grade_steps_f]] — via `GRADE_STEP_ID` (assignments neste step)

---

## 📎 Uso Típico

### Steps de uma grade
```sql
SELECT pgs.GRADE_STEP_ID, pgs.STEP_VALUE, pgs.SEQUENCE
FROM   PER_GRADE_STEPS_F pgs
WHERE  pgs.GRADE_ID = :p_grade_id
  AND  SYSDATE BETWEEN pgs.EFFECTIVE_START_DATE AND pgs.EFFECTIVE_END_DATE
ORDER BY pgs.SEQUENCE;
```

### Filtros comuns
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Steps vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- A `SEQUENCE` define a ordem de progressão dentro da grade.
- O `STEP_VALUE` pode representar salário mensal, anual ou por hora, dependendo da configuração.
---

## 🔗 PVOs Relacionados

### [[gradesteppvo|GradeStepPVO]] (GL · BICC: 6/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | GradeStepPEOActionOccurrenceId | — |
| CREATED_BY | GradeStepPEOCreatedBy | ✅ |
| CREATION_DATE | GradeStepPEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_ID | GradeStepPEOGradeId | — |
| GRADE_STEP_ID | GradeStepId | ✅ |
| LAST_UPDATE_DATE | GradeStepPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradeStepPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradeStepPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GradeStepPEOObjectVersionNumber | — |
| PAY_SCALE_POINT_ID | GradeStepPEOPayScalePointId | — |
| SEQUENCE | GradeStepPEOSequence | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_GRADE_STEPS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradestepsf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
