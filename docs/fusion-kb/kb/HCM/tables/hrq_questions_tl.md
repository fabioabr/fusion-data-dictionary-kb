---
id: DOC-HCM-197
doc_type: system-doc
title: "HRQ_QUESTIONS_TL — Traduções de Questões"
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
  - questionnaires
  - questions
  - translation
aliases:
  - HRQ_QUESTIONS_TL
  - hrq_questions_tl
  - traduções-de-questões
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QUESTIONS_TL

## 📌 Visão Geral

Tabela de **traduções** de questões de questionários (base). Padrão Oracle MLS.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Internacionalização:** Traduções em múltiplos idiomas.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTION_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador | [[hrq_questions_b]] | 🟢 95% |
| 2 | LANGUAGE | VARCHAR2(4) | NOT NULL | PK | Código do idioma | — | 🟢 100% |
| 3 | SOURCE_LANG | VARCHAR2(4) | NOT NULL | Controle | Idioma de origem | — | 🟢 100% |
| 4 | NAME | VARCHAR2(240) | NOT NULL | Tradução | Nome traduzido | — | 🟢 90% |
| 5 | DESCRIPTION | VARCHAR2(2000) | NULL | Tradução | Descrição traduzida | — | 🟡 80% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[hrq_questions_b]] — via `QUESTION_ID` (registro base do cadastro)

---

## 📎 Uso Típico

### Traduções
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRQ_QUESTIONS_TL tl
WHERE  tl.QUESTION_ID = :p_id AND tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `QUESTION_ID` + `LANGUAGE`.

---

## 🔗 PVOs Relacionados

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | — |
| CREATED_BY | QuestionnaireTranslationPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireTranslationPEOCreationDate | — |
| INSTRUCTIONS_TEXT | QuestionTranslationPEOInstructionsText | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireTranslationPEOObjectVersionNumber | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | — |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | — |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SOURCE_LANG | QuestionnaireTranslationPEOSourceLang | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 9/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireTranslationPEOCreationDate | ✅ |
| INSTRUCTIONS_TEXT | QuestionTranslationPEOInstructionsText | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | QuestionnaireTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireTranslationPEOLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireTranslationPEOObjectVersionNumber | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | ✅ |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | ✅ |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SOURCE_LANG | QuestionnaireTranslationPEOSourceLang | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | — |
| CREATED_BY | QuestionnaireTranslationPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireTranslationPEOCreationDate | — |
| INSTRUCTIONS_TEXT | QuestionTranslationPEOInstructionsText | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireTranslationPEOObjectVersionNumber | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | — |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | — |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SOURCE_LANG | QuestionnaireTranslationPEOSourceLang | — |

### [[questionnaireallquestionsp1|QuestionnaireAllQuestionsP1]] (HCM · BICC: 1/13)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | — |
| INSTRUCTIONS_TEXT | QuestionTranslationPEOInstructionsText | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | — |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | — |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SEED_DATA_SOURCE | QuestionTranslationPEOSeedDataSource | — |
| SOURCE_LANG | QuestionTranslationPEOSourceLang | — |

### [[questionnairequestionpvo|QuestionnaireQuestionPVO]] (HCM · BICC: 6/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireTranslationPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireTranslationPEOCreationDate | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | QuestionnaireTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireTranslationPEOObjectVersionNumber | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | ✅ |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | ✅ |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SOURCE_LANG | QuestionnaireTranslationPEOSourceLang | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | ConditionQuestionTLPEOBusinessGroupId | — |
| BUSINESS_GROUP_ID | QuestionTranslationPEOBusinessGroupId | — |
| CREATED_BY | QuestionnaireTranslationPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireTranslationPEOCreationDate | — |
| INSTRUCTIONS_TEXT | QuestionTranslationPEOInstructionsText | — |
| LANGUAGE | ConditionQuestionTLPEOLanguage | — |
| LANGUAGE | QuestionTranslationPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireTranslationPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireTranslationPEOLastUpdatedBy | — |
| OBJECT_VERSION_NUMBER | QuestionnaireTranslationPEOObjectVersionNumber | — |
| QSTN_VERSION_NUM | ConditionQuestionTLPEOQstnVersionNum | — |
| QSTN_VERSION_NUM | QuestionTranslationPEOQstnVersionNum | — |
| QUESTION_ID | ConditionQuestionTLPEOQuestionId | — |
| QUESTION_ID | QuestionTranslationPEOQuestionId | — |
| QUESTION_TEXT | ConditionQuestionTLPEOQuestionText | — |
| QUESTION_TEXT | QuestionTranslationPEOQuestionText | ✅ |
| SOURCE_LANG | QuestionnaireTranslationPEOSourceLang | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
