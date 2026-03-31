---
id: DOC-HCM-662
doc_type: system-doc
title: "PER_GRADE_LADDERS_F — Escadas Salariais"
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
  - escadas-salariais
  - grade-ladders
aliases:
  - PER_GRADE_LADDERS_F
  - per_grade_ladders_f
  - per-grade-ladders-f
  - escadas-salariais
  - per-grade-ladders-f
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PER_GRADE_LADDERS_F

## 📌 Visão Geral

Armazena as **escadas (ladders) salariais** da organização, com vigência temporal. Uma escada define uma sequência ordenada de grades que representam uma trilha de carreira.

> [!note] Sufixo _F
> O sufixo `_F` indica tabela **date-effective** — cada registro possui `EFFECTIVE_START_DATE` e `EFFECTIVE_END_DATE` controlando a vigência temporal.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Trilhas de carreira** — define os caminhos de progressão salarial.
- **Planejamento de carreira** — visualização das possibilidades de evolução.
- **Políticas de remuneração** — estruturação da política de grades e faixas.
- **Relatórios de compensação** — análise da estrutura salarial por escada.
---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GRADE_LADDER_ID | NUMBER(18) | NOT NULL | PK | Identificador único da escada | — | 🟢 95% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Data de início da vigência do registro | — | 🟢 95% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Data de fim da vigência do registro | — | 🟢 95% |
| 4 | BUSINESS_GROUP_ID | NUMBER(18) | NOT NULL | FK | Grupo de negócio | — | 🟢 90% |
| 5 | ACTIVE_FLAG | VARCHAR2(1) | NULL | Status | Se está ativa (Y/N) | — | 🟢 85% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 10 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de versão otimista do registro | — | 🟢 90% |
---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- - Nenhuma FK direta — tabela raiz de escadas salariais.

### Tabelas-filha (FK de saída)
- [[per_grade_ladders_f_tl]] — via `GRADE_LADDER_ID` (traduções da escala de grades salariais)
- [[per_grades_in_ladders_f]] — via `GRADE_LADDER_ID` (grades na escada)

---

## 📎 Uso Típico

### Escadas salariais ativas
```sql
SELECT pgl.GRADE_LADDER_ID, pgl.ACTIVE_FLAG
FROM   PER_GRADE_LADDERS_F pgl
WHERE  pgl.ACTIVE_FLAG = 'Y'
  AND  SYSDATE BETWEEN pgl.EFFECTIVE_START_DATE AND pgl.EFFECTIVE_END_DATE;
```

### Filtros comuns
- `ACTIVE_FLAG = 'Y'` — Escadas ativas
---

## 🔒 Observações

- Tabela date-effective (_F) — sempre filtrar por vigência.
- Cada escada contém uma sequência ordenada de grades via PER_GRADES_IN_LADDERS_F.
- Escadas representam trilhas de carreira (ex.: Técnica, Gerencial, Especialista).
---

## 🔗 PVOs Relacionados

### [[globalpersonpvo|GlobalPersonPVO]] (HCM · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | GradeLadderPEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | GradeLadderPEOEffectiveStartDate | ✅ |
| GRADE_LADDER_ID | GradeLadderPEOGradeLadderId | ✅ |
| LAST_UPDATE_DATE | GradeLadderPEOLastUpdateDate | ✅ |

### [[globalpersonpvoviewall|GlobalPersonPVOViewAll]] (HCM · BICC: 2/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | GradeLadderPEOEffectiveEndDate | — |
| EFFECTIVE_START_DATE | GradeLadderPEOEffectiveStartDate | ✅ |
| GRADE_LADDER_ID | GradeLadderPEOGradeLadderId | — |
| LAST_UPDATE_DATE | GradeLadderPEOLastUpdateDate | ✅ |

### [[gradeladderpvo|GradeLadderPVO]] (GL · BICC: 20/109)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTION_OCCURRENCE_ID | ActionOccurrenceId | — |
| ACTIVE_STATUS | ActiveStatus | ✅ |
| ALLOW_PROG_OVERRIDE_FLAG | AllowProgOverrideFlag | — |
| ALLOW_SALARY_OVERRIDE_FLAG | AllowSalaryOverrideFlag | — |
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
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| AUTO_PROGRESSION_CODE | AutoProgressionCode | ✅ |
| AUTO_SAL_CHANGE_CODE | AutoSalChangeCode | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | — |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| EFFECTIVE_END_DATE | EffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| GRADE_LADDER_GRP_CODE | GradeLadderGrpCode | ✅ |
| GRADE_LADDER_ID | GradeLadderId | ✅ |
| GRADE_SET_ID | GradeSetId | — |
| GRADE_TYPE | GradeType | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LEGISLATIVE_DATA_GROUP_ID | LegislativeDataGroupId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PROG_ACTION_ID | ProgActionId | — |
| PROG_ACTION_OCCURRENCE_ID | ProgActionOccurrenceId | — |
| PROG_ACTION_REASON_ID | ProgActionReasonId | — |
| PROGRESSION_DATE_CODE | ProgressionDateCode | ✅ |
| PROGRESSION_DATE_RULE_ID | ProgressionDateRuleId | — |
| PROGRESSION_STYLE_CODE | ProgressionStyleCode | ✅ |
| RATE_CHANGE_DATE_CODE | RateChangeDateCode | ✅ |
| RATE_CHANGE_DATE_RULE_ID | RateChangeDateRuleId | — |
| RATE_SYNC_ACTION_ID | RateSyncActionId | — |
| RATE_SYNC_ACTION_REASON_ID | RateSyncActionReasonId | — |
| SALARY_ACTION_ID | SalaryActionId | — |
| SALARY_ACTION_OCCURRENCE_ID | SalaryActionOccurrenceId | — |
| SALARY_ACTION_REASON_ID | SalaryActionReasonId | — |
| SALARY_ADJUSTMENT_TYPE_CODE | SalaryAdjustmentTypeCode | ✅ |
| SALARY_CALC_METHOD_CODE | SalaryCalcMethodCode | ✅ |
| SALARY_CALC_RULE_ID | SalaryCalcRuleId | — |
| SALARY_CHANGE_DATE_CODE | SalaryChangeDateCode | ✅ |
| SALARY_CHANGE_DATE_RULE_ID | SalaryChangeDateRuleId | — |
| SALARY_ELEMENT_TYPE_ID | SalaryElementTypeId | — |
| SALARY_INPUT_VALUE_ID | SalaryInputValueId | — |
| SALARY_UPD_METHOD_CODE | SalaryUpdMethodCode | — |
| STEP_DETERMINATION_CODE | StepDeterminationCode | — |
| UPDATE_SALARY_FLAG | UpdateSalaryFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — PER_GRADE_LADDERS_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/pergradeladdersf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
