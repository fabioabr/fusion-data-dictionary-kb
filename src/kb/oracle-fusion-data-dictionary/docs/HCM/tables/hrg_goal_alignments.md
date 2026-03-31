---
id: DOC-HCM-167
doc_type: system-doc
title: "HRG_GOAL_ALIGNMENTS — Alinhamentos de Objetivos"
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
  - goals
  - alignments
aliases:
  - HRG_GOAL_ALIGNMENTS
  - hrg_goal_alignments
  - alinhamentos-de-objetivos
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRG_GOAL_ALIGNMENTS

## 📌 Visão Geral

Armazena **alinhamentos entre objetivos**. Cascata de metas organizacionais para individuais.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Cascata de metas:** Objetivos individuais vinculados a organizacionais.
- **Alinhamento estratégico:** Conexão com estratégia.
- **Visibilidade cross-funcional:** Dependências entre áreas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | GOAL_ALIGNMENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo filho | [[hrg_goals]] | 🟢 90% |
| 3 | ALIGNED_GOAL_ID | NUMBER(18) | NOT NULL | FK | Objetivo pai | [[hrg_goals]] | 🟢 85% |
| 4 | ALIGNMENT_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo (ORGANIZATION, TEAM, INDIVIDUAL) | — | 🟡 70% |
| 5 | ALIGNMENT_WEIGHT | NUMBER | NULL | Métrica | Peso da contribuição | — | 🟡 65% |
| 6 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 7 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 8 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 9 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 10 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrg_goals]] — via `GOAL_ID` (meta filha no alinhamento de metas)
- [[hrg_goals]] — via `ALIGNED_GOAL_ID` (pai)

---

## 📎 Uso Típico

### Cascata de alinhamento
```sql
SELECT child.GOAL_NAME, parent.GOAL_NAME AS org_goal
FROM   HRG_GOAL_ALIGNMENTS a
JOIN   HRG_GOALS child ON child.GOAL_ID = a.GOAL_ID
JOIN   HRG_GOALS parent ON parent.GOAL_ID = a.ALIGNED_GOAL_ID
WHERE  a.ALIGNED_GOAL_ID = :p_org_goal_id;
```

---

## 🔒 Observações

- Árvore hierárquica de objetivos.
- Um objetivo pode alinhar-se a múltiplos pais.

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[goalalignmentextractpvo|GoalAlignmentExtractPVO]] (HCM · BICC: 10/10)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | AlignedGoalId | ✅ |
| BUSINESS_GROUP_ID | BusinessGroupId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| GOAL_ALIGNMENT_ID | GoalAlignmentId | ✅ |
| GOAL_ID | GoalId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM · BICC: 1/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALIGNED_GOAL_ID | GoalAlignmentPEOAlignedGoalId | — |
| GOAL_ALIGNMENT_ID | GoalAlignmentPEOGoalAlignmentId | — |
| GOAL_ID | GoalAlignmentPEOGoalId1 | — |
| LAST_UPDATE_DATE | GoalAlignmentPEOLastUpdateDate | ✅ |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
