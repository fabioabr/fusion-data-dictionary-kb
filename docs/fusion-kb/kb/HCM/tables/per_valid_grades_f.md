---
id: DOC-HCM-720
doc_type: system-doc
title: "PER_VALID_GRADES_F — Grades Válidos por Cargo"
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
  - grades
  - cargos
  - remuneração
aliases:
  - PER_VALID_GRADES_F
  - per_valid_grades_f
  - per-valid-grades-f
  - grades-válidos-por-cargo
  - valid-grades
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PER_VALID_GRADES_F

## Visão Geral

Armazena a **associação entre cargos (jobs/positions) e grades válidos**, definindo quais níveis salariais/classificações são permitidos para cada cargo. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura salarial** — define quais grades/faixas são válidos para cada cargo.
- **Validação de atribuição** — impede atribuição de grades incompatíveis com o cargo.
- **Planejamento de carreira** — mostra os grades possíveis dentro de um cargo.
- **Compliance salarial** — garante aderência à política de remuneração.
- **Relatórios de remuneração** — suporta análises de equidade salarial.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | VALID_GRADE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da associação grade-cargo | — | 🟢 90% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 95% |
| 4 | JOB_ID | NUMBER(18) | NULL | FK | Cargo associado | PER_JOBS_F | 🟢 85% |
| 5 | POSITION_ID | NUMBER(18) | NULL | FK | Posição associada | HR_ALL_POSITIONS_F | 🟢 85% |
| 6 | GRADE_ID | NUMBER(18) | NOT NULL | FK | Grade válido para o cargo/posição | PER_GRADES_F | 🟢 90% |
| 7 | BUSINESS_GROUP_ID | NUMBER(18) | NULL | FK | Grupo de negócio | — | 🟢 85% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_jobs_f]] — via `JOB_ID` (cargo com grade salarial válida)
- [[hr_all_positions_f]] — via `POSITION_ID` (posição com grade salarial válida)
- [[per_grades_f]] — via `GRADE_ID` (grade salarial válida para cargo/posição)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Grades válidos para um cargo
```sql
SELECT vg.GRADE_ID, g.NAME AS grade_name
FROM   PER_VALID_GRADES_F vg
JOIN   PER_GRADES_F g ON vg.GRADE_ID = g.GRADE_ID
WHERE  vg.JOB_ID = :p_job_id
  AND  SYSDATE BETWEEN vg.EFFECTIVE_START_DATE AND vg.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `JOB_ID = :p_job_id` — Grades de um cargo específico
- `POSITION_ID = :p_position_id` — Grades de uma posição específica

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Um cargo pode ter múltiplos grades válidos simultaneamente.
- JOB_ID e POSITION_ID são mutuamente exclusivos na maioria dos cenários.
- Fundamental para validação de movimentações salariais.

---

## Referências

- [Oracle Docs — PER_VALID_GRADES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pervalidgradesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[validgradespvo|ValidGradesPVO]] (GL · BICC: 14/80)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ValidGradesPEOActionOccurrenceId | ✅ |
| ATTRIBUTE1 | ValidGradesPEOAttribute1 | — |
| ATTRIBUTE10 | ValidGradesPEOAttribute10 | — |
| ATTRIBUTE11 | ValidGradesPEOAttribute11 | — |
| ATTRIBUTE12 | ValidGradesPEOAttribute12 | — |
| ATTRIBUTE13 | ValidGradesPEOAttribute13 | — |
| ATTRIBUTE14 | ValidGradesPEOAttribute14 | — |
| ATTRIBUTE15 | ValidGradesPEOAttribute15 | — |
| ATTRIBUTE16 | ValidGradesPEOAttribute16 | — |
| ATTRIBUTE17 | ValidGradesPEOAttribute17 | — |
| ATTRIBUTE18 | ValidGradesPEOAttribute18 | — |
| ATTRIBUTE19 | ValidGradesPEOAttribute19 | — |
| ATTRIBUTE2 | ValidGradesPEOAttribute2 | — |
| ATTRIBUTE20 | ValidGradesPEOAttribute20 | — |
| ATTRIBUTE21 | ValidGradesPEOAttribute21 | — |
| ATTRIBUTE22 | ValidGradesPEOAttribute22 | — |
| ATTRIBUTE23 | ValidGradesPEOAttribute23 | — |
| ATTRIBUTE24 | ValidGradesPEOAttribute24 | — |
| ATTRIBUTE25 | ValidGradesPEOAttribute25 | — |
| ATTRIBUTE26 | ValidGradesPEOAttribute26 | — |
| ATTRIBUTE27 | ValidGradesPEOAttribute27 | — |
| ATTRIBUTE28 | ValidGradesPEOAttribute28 | — |
| ATTRIBUTE29 | ValidGradesPEOAttribute29 | — |
| ATTRIBUTE3 | ValidGradesPEOAttribute3 | — |
| ATTRIBUTE30 | ValidGradesPEOAttribute30 | — |
| ATTRIBUTE4 | ValidGradesPEOAttribute4 | — |
| ATTRIBUTE5 | ValidGradesPEOAttribute5 | — |
| ATTRIBUTE6 | ValidGradesPEOAttribute6 | — |
| ATTRIBUTE7 | ValidGradesPEOAttribute7 | — |
| ATTRIBUTE8 | ValidGradesPEOAttribute8 | — |
| ATTRIBUTE9 | ValidGradesPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | ValidGradesPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | ValidGradesPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | ValidGradesPEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | ValidGradesPEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | ValidGradesPEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | ValidGradesPEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | ValidGradesPEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | ValidGradesPEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | ValidGradesPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | ValidGradesPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | ValidGradesPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | ValidGradesPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | ValidGradesPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | ValidGradesPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | ValidGradesPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | ValidGradesPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | ValidGradesPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | ValidGradesPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | ValidGradesPEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | ValidGradesPEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | ValidGradesPEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | ValidGradesPEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | ValidGradesPEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | ValidGradesPEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | ValidGradesPEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | ValidGradesPEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | ValidGradesPEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | ValidGradesPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | ValidGradesPEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | ValidGradesPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | ValidGradesPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | ValidGradesPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | ValidGradesPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | ValidGradesPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | ValidGradesPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | ValidGradesPEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | ValidGradesPEOBusinessGroupId | ✅ |
| CREATED_BY | ValidGradesPEOCreatedBy | ✅ |
| CREATION_DATE | ValidGradesPEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | ValidGradesPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ValidGradesPEOEffectiveStartDate | ✅ |
| GRADE_ID | ValidGradesPEOGradeId | ✅ |
| JOB_ID | ValidGradesPEOJobId | ✅ |
| LAST_UPDATE_DATE | ValidGradesPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ValidGradesPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | ValidGradesPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ValidGradesPEOObjectVersionNumber | ✅ |
| POSITION_ID | ValidGradesPEOPositionId | ✅ |
| VALID_GRADE_ID | ValidGradesPEOValidGradeId | ✅ |
