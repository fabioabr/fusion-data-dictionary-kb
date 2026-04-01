---
id: DOC-HCM-164
doc_type: system-doc
title: "HRD_PERSONAL_INTENTS — Intenções Pessoais de Desenvolvimento"
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
  - development
  - personal
  - intents
aliases:
  - HRD_PERSONAL_INTENTS
  - hrd_personal_intents
  - intenções-pessoais-de-desenvolvimento
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRD_PERSONAL_INTENTS

## 📌 Visão Geral

Armazena **intenções pessoais de desenvolvimento** de colaboradores. Aspirações de carreira, mobilidade, realocação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de carreira:** Aspirações declaradas.
- **Sucessão:** Informa planos de sucessão.
- **Mobilidade:** Disponibilidade para transferências.
- **Analytics:** Dashboards de talent management.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PERSONAL_INTENT_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 90% |
| 2 | PERSON_ID | NUMBER(18) | NOT NULL | FK | Colaborador | [[per_all_people_f]] | 🟢 90% |
| 3 | INTENT_TYPE | VARCHAR2(30) | NOT NULL | Classificação | Tipo (CAREER_MOVE, RELOCATION, RETIREMENT) | — | 🟡 75% |
| 4 | INTENT_VALUE | VARCHAR2(240) | NULL | Dados | Valor da intenção | — | 🟡 70% |
| 5 | EFFECTIVE_START_DATE | DATE | NULL | Data | Início da vigência | — | 🟡 75% |
| 6 | EFFECTIVE_END_DATE | DATE | NULL | Data | Fim da vigência | — | 🟡 75% |
| 7 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários | — | 🟡 65% |
| 8 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 9 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 10 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 11 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 12 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 13 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PERSON_ID` (colaborador da intencao pessoal de desenvolvimento)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Intenções pessoais ativas
```sql
SELECT pi.INTENT_TYPE, pi.INTENT_VALUE, pi.COMMENTS
FROM   HRD_PERSONAL_INTENTS pi
WHERE  pi.PERSON_ID = :p_person_id
  AND  SYSDATE BETWEEN NVL(pi.EFFECTIVE_START_DATE, SYSDATE) AND NVL(pi.EFFECTIVE_END_DATE, SYSDATE+1);
```

---

## 🔒 Observações

- Intenções são declarativas.
- Utilizado em Talent Review meetings.
- Integra-se com [[hrm_plans_v]].

---

## 🔗 PVOs Relacionados

### [[careerdevgoalpvo|CareerDevGoalPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[careerdevgoalpvoviewall|CareerDevGoalPVOViewAll]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[careerdevgoalversionpvo|CareerDevGoalVersionPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[careerdevgoalversionpvoviewall|CareerDevGoalVersionPVOViewAll]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[developmentgoalpvo|DevelopmentGoalPVO]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[developmentgoalpvoviewall|DevelopmentGoalPVOViewAll]] (HCM · BICC: 2/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[goalppvo1|GoalPPVO1]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[goalpvo_copy|GoalPVO_Copy]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[performancegoalpvo|PerformanceGoalPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[performancegoalpvoviewall|PerformanceGoalPVOViewAll]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[performancegoalversionpvo|PerformanceGoalVersionPVO]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[performancegoalversionpvoviewall|PerformanceGoalVersionPVOViewAll]] (HCM · BICC: 1/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

### [[personalgoalpvo|PersonalGoalPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| INTENT_NAME | IntentName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| PERSON_ID | PersonId1 | — |
| PERSONAL_INTENT_ID | PersonalIntentId | — |
| PRIVACY_FLAG | PrivacyFlag | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
