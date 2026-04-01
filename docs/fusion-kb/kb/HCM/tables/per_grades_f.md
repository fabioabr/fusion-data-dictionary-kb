---
id: DOC-HCM-659
doc_type: system-doc
title: "PER_GRADES_F — Grades Salariais"
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
  - grades
  - faixas-salariais
aliases:
  - PER_GRADES_F
  - per_grades_f
  - per-grades-f
  - grades-salariais
  - per-grades-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADES_F

## 📌 Visão Geral

Armazena as **grades (faixas) salariais** da organização, com vigência temporal. Define as faixas de remuneração associadas a cargos e posições.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estrutura de remuneração** — define as grades salariais da organização.
- **Equidade salarial** — garante consistência na remuneração por nível.
- **Progressão de carreira** — grades representam níveis na estrutura de carreira.
- **Orçamento** — base para planejamento de custos de pessoal.
- **Compliance** — transparência na política de remuneração.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da grade | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 5 | GRADE_CODE | VARCHAR2(30) | NULL | Identificação | Código da grade | — | 🟢 85% |
| 6 | ACTIVE_STATUS | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 11 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de grades salariais.

### Tabelas-filha (FK de saída)
- [[per_grades_f_tl]] — via `GRADE_ID` (traduções da grade salarial)
- [[per_grades_in_ladders_f]] — via `GRADE_ID` (grades em escadas salariais)
- [[per_grade_steps_f]] — via `GRADE_ID` (steps da grade salarial)
- [[per_all_assignments_m]] — via `GRADE_ID` (assignments nesta grade)

---

## 📎 Uso Típico

### Grades salariais ativas
```sql
SELECT pgf.GRADE_ID, pgf.GRADE_CODE, pgf.ACTIVE_STATUS
FROM   PER_GRADES_F pgf
WHERE  pgf.ACTIVE_STATUS = 'Y'
  AND  SYSDATE BETWEEN pgf.EFFECTIVE_START_DATE AND pgf.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_STATUS = 'Y'` — Grades ativas
- `SYSDATE BETWEEN EFFECTIVE_START_DATE AND EFFECTIVE_END_DATE` — Grades vigentes
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Grades são a base da estrutura de remuneração — cada assignment referencia uma grade.
- O código da grade tipicamente reflete o nível hierárquico (ex.: G01, G02, SENIOR, DIRECTOR).
---

## 🔗 PVOs Relacionados

### [[gradeextractpvo|GradeExtractPVO]] (HCM · BICC: 18/83)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | ✅ |
| ACTIVE_STATUS | ActiveStatus | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE21 | Attribute21 | — |
| ATTRIBUTE22 | Attribute22 | — |
| ATTRIBUTE23 | Attribute23 | — |
| ATTRIBUTE24 | Attribute24 | — |
| ATTRIBUTE25 | Attribute25 | — |
| ATTRIBUTE26 | Attribute26 | — |
| ATTRIBUTE27 | Attribute27 | — |
| ATTRIBUTE28 | Attribute28 | — |
| ATTRIBUTE29 | Attribute29 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE30 | Attribute30 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE11 | AttributeDate11 | — |
| ATTRIBUTE_DATE12 | AttributeDate12 | — |
| ATTRIBUTE_DATE13 | AttributeDate13 | — |
| ATTRIBUTE_DATE14 | AttributeDate14 | — |
| ATTRIBUTE_DATE15 | AttributeDate15 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | AttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | AttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | AttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | AttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | AttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | AttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | AttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | AttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | AttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | AttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CEILING_STEP_ID | CeilingStepId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_CODE | GradeCode | ✅ |
| GRADE_ID | GradeId | ✅ |
| GRADE_TYPE | GradeType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PAY_SCALE_ID | PayScaleId | ✅ |
| SET_ID | SetId | ✅ |
| STARTING_STEP | StartingStep | ✅ |

### [[gradepvo|GradePVO]] (GL · BICC: 18/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | GradePEOActionOccurrenceId | ✅ |
| ACTIVE_STATUS | GradePEOActiveStatus | ✅ |
| BUSINESS_GROUP_ID | GradePEOBusinessGroupId | ✅ |
| CEILING_STEP_ID | GradePEOCeilingStepId | ✅ |
| CREATED_BY | GradePEOCreatedBy | ✅ |
| CREATION_DATE | GradePEOCreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_CODE | GradePEOGradeCode | ✅ |
| GRADE_ID | GradeId | ✅ |
| GRADE_TYPE | GradePEOGradeType | ✅ |
| LAST_UPDATE_DATE | GradePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradePEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | GradePEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | GradePEOObjectVersionNumber | ✅ |
| PAY_SCALE_ID | GradePEOPayScaleId | ✅ |
| SET_ID | GradePEOSetId | ✅ |
| STARTING_STEP | GradePEOStartingStep | ✅ |

### [[graderefpvo|GradeRefPVO]] (GL · BICC: 7/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_STATUS | GradePEOActiveStatus | ✅ |
| BUSINESS_GROUP_ID | GradePEOBusinessGroupId | — |
| CREATED_BY | GradePEOCreatedBy | — |
| CREATION_DATE | GradePEOCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_CODE | GradePEOGradeCode | ✅ |
| GRADE_ID | GradeId | ✅ |
| LAST_UPDATE_DATE | GradePEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | GradePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GradePEOObjectVersionNumber | — |
| SET_ID | GradePEOSetId | ✅ |

### [[validgradespvo|ValidGradesPVO]] (GL)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | GradePEOActionOccurrenceId | — |
| ACTIVE_STATUS | GradePEOActiveStatus | — |
| ATTRIBUTE1 | GradePEOAttribute1 | — |
| ATTRIBUTE10 | GradePEOAttribute10 | — |
| ATTRIBUTE11 | GradePEOAttribute11 | — |
| ATTRIBUTE12 | GradePEOAttribute12 | — |
| ATTRIBUTE13 | GradePEOAttribute13 | — |
| ATTRIBUTE14 | GradePEOAttribute14 | — |
| ATTRIBUTE15 | GradePEOAttribute15 | — |
| ATTRIBUTE16 | GradePEOAttribute16 | — |
| ATTRIBUTE17 | GradePEOAttribute17 | — |
| ATTRIBUTE18 | GradePEOAttribute18 | — |
| ATTRIBUTE19 | GradePEOAttribute19 | — |
| ATTRIBUTE2 | GradePEOAttribute2 | — |
| ATTRIBUTE20 | GradePEOAttribute20 | — |
| ATTRIBUTE21 | GradePEOAttribute21 | — |
| ATTRIBUTE22 | GradePEOAttribute22 | — |
| ATTRIBUTE23 | GradePEOAttribute23 | — |
| ATTRIBUTE24 | GradePEOAttribute24 | — |
| ATTRIBUTE25 | GradePEOAttribute25 | — |
| ATTRIBUTE26 | GradePEOAttribute26 | — |
| ATTRIBUTE27 | GradePEOAttribute27 | — |
| ATTRIBUTE28 | GradePEOAttribute28 | — |
| ATTRIBUTE29 | GradePEOAttribute29 | — |
| ATTRIBUTE3 | GradePEOAttribute3 | — |
| ATTRIBUTE30 | GradePEOAttribute30 | — |
| ATTRIBUTE4 | GradePEOAttribute4 | — |
| ATTRIBUTE5 | GradePEOAttribute5 | — |
| ATTRIBUTE6 | GradePEOAttribute6 | — |
| ATTRIBUTE7 | GradePEOAttribute7 | — |
| ATTRIBUTE8 | GradePEOAttribute8 | — |
| ATTRIBUTE9 | GradePEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | GradePEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | GradePEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | GradePEOAttributeDate10 | — |
| ATTRIBUTE_DATE11 | GradePEOAttributeDate11 | — |
| ATTRIBUTE_DATE12 | GradePEOAttributeDate12 | — |
| ATTRIBUTE_DATE13 | GradePEOAttributeDate13 | — |
| ATTRIBUTE_DATE14 | GradePEOAttributeDate14 | — |
| ATTRIBUTE_DATE15 | GradePEOAttributeDate15 | — |
| ATTRIBUTE_DATE2 | GradePEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | GradePEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | GradePEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | GradePEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | GradePEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | GradePEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | GradePEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | GradePEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | GradePEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | GradePEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER11 | GradePEOAttributeNumber11 | — |
| ATTRIBUTE_NUMBER12 | GradePEOAttributeNumber12 | — |
| ATTRIBUTE_NUMBER13 | GradePEOAttributeNumber13 | — |
| ATTRIBUTE_NUMBER14 | GradePEOAttributeNumber14 | — |
| ATTRIBUTE_NUMBER15 | GradePEOAttributeNumber15 | — |
| ATTRIBUTE_NUMBER16 | GradePEOAttributeNumber16 | — |
| ATTRIBUTE_NUMBER17 | GradePEOAttributeNumber17 | — |
| ATTRIBUTE_NUMBER18 | GradePEOAttributeNumber18 | — |
| ATTRIBUTE_NUMBER19 | GradePEOAttributeNumber19 | — |
| ATTRIBUTE_NUMBER2 | GradePEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER20 | GradePEOAttributeNumber20 | — |
| ATTRIBUTE_NUMBER3 | GradePEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | GradePEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | GradePEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | GradePEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | GradePEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | GradePEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | GradePEOAttributeNumber9 | — |
| BUSINESS_GROUP_ID | GradePEOBusinessGroupId | — |
| CEILING_STEP_ID | GradePEOCeilingStepId | — |
| CREATED_BY | GradePEOCreatedBy | — |
| CREATION_DATE | GradePEOCreationDate | — |
| EFFECTIVE_END_DATE | GradePEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradePEOEffectiveStartDate | — |
| GRADE_CODE | GradePEOGradeCode | — |
| GRADE_ID | GradePEOGradeId | — |
| GRADE_TYPE | GradePEOGradeType | — |
| LAST_UPDATE_DATE | GradePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | GradePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | GradePEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | GradePEOObjectVersionNumber | — |
| PAY_SCALE_ID | GradePEOPayScaleId | — |
| SET_ID | GradePEOSetId | — |
| STARTING_STEP | GradePEOStartingStep | — |

---

## 📚 Referências

- [Oracle Docs — PER_GRADES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
