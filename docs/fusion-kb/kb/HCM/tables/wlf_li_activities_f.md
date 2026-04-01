---
id: DOC-HCM-737
doc_type: system-doc
title: "WLF_LI_ACTIVITIES_F — Atividades de Itens de Aprendizado"
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
  - learning
  - workforce-learning
  - atividades-aprendizado
aliases:
  - WLF_LI_ACTIVITIES_F
  - wlf_li_activities_f
  - wlf-li-activities-f
  - atividades-itens-aprendizado
  - li-activities
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-26
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# WLF_LI_ACTIVITIES_F

## Visão Geral

Armazena as **atividades** que compõem um item de aprendizado, detalhando as tarefas ou módulos que o participante deve completar. Tabela date-effective (_F).

---

## Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação de cursos** — define as atividades/módulos que compõem um treinamento.
- **Tracking de progresso** — base para acompanhamento de conclusão por atividade.
- **Sequenciamento** — define a ordem de execução das atividades.
- **Avaliação granular** — permite avaliar desempenho por atividade individual.

---

## Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | LI_ACTIVITY_ID | NUMBER(18) | NOT NULL | PK | Identificador único da atividade | — | 🟡 80% |
| 2 | EFFECTIVE_START_DATE | DATE | NOT NULL | Vigência | Início da validade do registro | — | 🟢 90% |
| 3 | EFFECTIVE_END_DATE | DATE | NOT NULL | Vigência | Fim da validade do registro | — | 🟢 90% |
| 4 | LEARNING_ITEM_ID | NUMBER(18) | NOT NULL | FK | Item de aprendizado pai | WLF_LEARNING_ITEMS_F | 🟢 85% |
| 5 | ACTIVITY_TYPE | VARCHAR2(30) | NULL | Classificação | Tipo da atividade (quiz, video, assignment) | — | 🟡 75% |
| 6 | SEQUENCE | NUMBER(9) | NULL | Controle | Ordem da atividade no item | — | 🟡 75% |
| 7 | MANDATORY_FLAG | VARCHAR2(1) | NULL | Regra | Indica se a atividade é obrigatória (Y/N) | — | 🟡 70% |
| 8 | DURATION_MINUTES | NUMBER(10) | NULL | Dados | Duração estimada em minutos | — | 🟡 70% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |

---

## Relacionamentos

### Tabelas-pai (FK de entrada)
- [[wlf_learning_items_f]] — via `LEARNING_ITEM_ID` (item de aprendizado)

### Tabelas-filha (FK de saída)
- Nenhuma tabela-filha identificada.

---

## Uso Típico

### Atividades de um item de aprendizado
```sql
SELECT la.ACTIVITY_TYPE, la.SEQUENCE, la.MANDATORY_FLAG, la.DURATION_MINUTES
FROM   WLF_LI_ACTIVITIES_F la
WHERE  la.LEARNING_ITEM_ID = :p_learning_item_id
  AND  SYSDATE BETWEEN la.EFFECTIVE_START_DATE AND la.EFFECTIVE_END_DATE
ORDER BY la.SEQUENCE;
```

### Filtros comuns
- `LEARNING_ITEM_ID = :p_item_id` — Atividades de um item específico
- `MANDATORY_FLAG = 'Y'` — Apenas atividades obrigatórias

---

## Observações

- Tabela date-effective (_F) — registros possuem vigência temporal.
- Faz parte do módulo Workforce Learning (prefixo WLF_).
- Granularidade abaixo do item de aprendizado (LI = Learning Item).

---

## Referências

- [Oracle Docs — WLF_LI_ACTIVITIES_F](https://docs.oracle.com/en/cloud/saas/human-resources/25a/oedmf/wlfliactivitiesf.html)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM

---

## 🔗 PVOs Relacionados

### [[activitiespvo|ActivitiesPVO]] (HCM · BICC: 13/76)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACT_ATTRIBUTE1 | ActivitiesDEOActAttribute1 | — |
| ACT_ATTRIBUTE10 | ActivitiesDEOActAttribute10 | — |
| ACT_ATTRIBUTE11 | ActivitiesDEOActAttribute11 | — |
| ACT_ATTRIBUTE12 | ActivitiesDEOActAttribute12 | — |
| ACT_ATTRIBUTE13 | ActivitiesDEOActAttribute13 | — |
| ACT_ATTRIBUTE14 | ActivitiesDEOActAttribute14 | — |
| ACT_ATTRIBUTE15 | ActivitiesDEOActAttribute15 | — |
| ACT_ATTRIBUTE16 | ActivitiesDEOActAttribute16 | — |
| ACT_ATTRIBUTE17 | ActivitiesDEOActAttribute17 | — |
| ACT_ATTRIBUTE18 | ActivitiesDEOActAttribute18 | — |
| ACT_ATTRIBUTE19 | ActivitiesDEOActAttribute19 | — |
| ACT_ATTRIBUTE2 | ActivitiesDEOActAttribute2 | — |
| ACT_ATTRIBUTE20 | ActivitiesDEOActAttribute20 | — |
| ACT_ATTRIBUTE3 | ActivitiesDEOActAttribute3 | — |
| ACT_ATTRIBUTE4 | ActivitiesDEOActAttribute4 | — |
| ACT_ATTRIBUTE5 | ActivitiesDEOActAttribute5 | — |
| ACT_ATTRIBUTE6 | ActivitiesDEOActAttribute6 | — |
| ACT_ATTRIBUTE7 | ActivitiesDEOActAttribute7 | — |
| ACT_ATTRIBUTE8 | ActivitiesDEOActAttribute8 | — |
| ACT_ATTRIBUTE9 | ActivitiesDEOActAttribute9 | — |
| ACT_ATTRIBUTE_CATEGORY | ActivitiesDEOActAttributeCategory | — |
| ACT_ATTRIBUTE_DATE1 | ActivitiesDEOActAttributeDate1 | — |
| ACT_ATTRIBUTE_DATE10 | ActivitiesDEOActAttributeDate10 | — |
| ACT_ATTRIBUTE_DATE11 | ActivitiesDEOActAttributeDate11 | — |
| ACT_ATTRIBUTE_DATE12 | ActivitiesDEOActAttributeDate12 | — |
| ACT_ATTRIBUTE_DATE13 | ActivitiesDEOActAttributeDate13 | — |
| ACT_ATTRIBUTE_DATE14 | ActivitiesDEOActAttributeDate14 | — |
| ACT_ATTRIBUTE_DATE15 | ActivitiesDEOActAttributeDate15 | — |
| ACT_ATTRIBUTE_DATE2 | ActivitiesDEOActAttributeDate2 | — |
| ACT_ATTRIBUTE_DATE3 | ActivitiesDEOActAttributeDate3 | — |
| ACT_ATTRIBUTE_DATE4 | ActivitiesDEOActAttributeDate4 | — |
| ACT_ATTRIBUTE_DATE5 | ActivitiesDEOActAttributeDate5 | — |
| ACT_ATTRIBUTE_DATE6 | ActivitiesDEOActAttributeDate6 | — |
| ACT_ATTRIBUTE_DATE7 | ActivitiesDEOActAttributeDate7 | — |
| ACT_ATTRIBUTE_DATE8 | ActivitiesDEOActAttributeDate8 | — |
| ACT_ATTRIBUTE_DATE9 | ActivitiesDEOActAttributeDate9 | — |
| ACT_ATTRIBUTE_NUMBER1 | ActivitiesDEOActAttributeNumber1 | — |
| ACT_ATTRIBUTE_NUMBER10 | ActivitiesDEOActAttributeNumber10 | — |
| ACT_ATTRIBUTE_NUMBER11 | ActivitiesDEOActAttributeNumber11 | — |
| ACT_ATTRIBUTE_NUMBER12 | ActivitiesDEOActAttributeNumber12 | — |
| ACT_ATTRIBUTE_NUMBER13 | ActivitiesDEOActAttributeNumber13 | — |
| ACT_ATTRIBUTE_NUMBER14 | ActivitiesDEOActAttributeNumber14 | — |
| ACT_ATTRIBUTE_NUMBER15 | ActivitiesDEOActAttributeNumber15 | — |
| ACT_ATTRIBUTE_NUMBER16 | ActivitiesDEOActAttributeNumber16 | — |
| ACT_ATTRIBUTE_NUMBER17 | ActivitiesDEOActAttributeNumber17 | — |
| ACT_ATTRIBUTE_NUMBER18 | ActivitiesDEOActAttributeNumber18 | — |
| ACT_ATTRIBUTE_NUMBER19 | ActivitiesDEOActAttributeNumber19 | — |
| ACT_ATTRIBUTE_NUMBER2 | ActivitiesDEOActAttributeNumber2 | — |
| ACT_ATTRIBUTE_NUMBER20 | ActivitiesDEOActAttributeNumber20 | — |
| ACT_ATTRIBUTE_NUMBER3 | ActivitiesDEOActAttributeNumber3 | — |
| ACT_ATTRIBUTE_NUMBER4 | ActivitiesDEOActAttributeNumber4 | — |
| ACT_ATTRIBUTE_NUMBER5 | ActivitiesDEOActAttributeNumber5 | — |
| ACT_ATTRIBUTE_NUMBER6 | ActivitiesDEOActAttributeNumber6 | — |
| ACT_ATTRIBUTE_NUMBER7 | ActivitiesDEOActAttributeNumber7 | — |
| ACT_ATTRIBUTE_NUMBER8 | ActivitiesDEOActAttributeNumber8 | — |
| ACT_ATTRIBUTE_NUMBER9 | ActivitiesDEOActAttributeNumber9 | — |
| ACTIVITY_ID | ActivitiesDEOActivityId | ✅ |
| ACTIVITY_TYPE | ActivitiesDEOActivityType | ✅ |
| COMPLETION_TYPE | ActivitiesDEOCompletionType | ✅ |
| CONTENT_TYPE | ActivitiesDEOContentType | ✅ |
| CREATED_BY | ActivitiesDEOCreatedBy | — |
| CREATION_DATE | ActivitiesDEOCreationDate | — |
| DUE_DATE | ActivitiesDEODueDate | ✅ |
| EFFECTIVE_END_DATE | ActivitiesDEOEffectiveEndDate | ✅ |
| EFFECTIVE_START_DATE | ActivitiesDEOEffectiveStartDate | ✅ |
| ENTERPRISE_ID | ActivitiesDEOEnterpriseId | — |
| LAST_UPDATE_DATE | ActivitiesDEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ActivitiesDEOLastUpdateLogin | — |
| LAST_UPDATED_BY | ActivitiesDEOLastUpdatedBy | — |
| LEARNING_ITEM_ID | ActivitiesDEOLearningItemId | ✅ |
| OBJECT_VERSION_NUMBER | ActivitiesDEOObjectVersionNumber | — |
| PARENT_LEARNING_ITEM_ID | ActivitiesDEOParentLearningItemId | — |
| RELATED_CONTENT_ID | ActivitiesDEORelatedContentId | ✅ |
| SELF_COMPLETE_FLAG | ActivitiesDEOSelfCompleteFlag | ✅ |
| TIME_ZONE | ActivitiesDEOTimeZone | ✅ |
| VIRTUAL_CLASSROOM_URL | ActivitiesDEOVirtualClassroomUrl | ✅ |
