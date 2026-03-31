---
id: DOC-HCM-195
doc_type: system-doc
title: "HRQ_QUESTIONNAIRES_TL — Traduções de Questionários"
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
  - translation
aliases:
  - HRQ_QUESTIONNAIRES_TL
  - hrq_questionnaires_tl
  - traduções-de-questionários
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QUESTIONNAIRES_TL

## 📌 Visão Geral

Tabela de **traduções** de questionários (base). Padrão Oracle MLS.

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
| 1 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | PK/FK | Identificador | [[hrq_questionnaires_b]] | 🟢 95% |
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
- [[hrq_questionnaires_b]] — via `QUESTIONNAIRE_ID` (registro base do cadastro)

---

## 📎 Uso Típico

### Traduções
```sql
SELECT tl.NAME, tl.DESCRIPTION
FROM   HRQ_QUESTIONNAIRES_TL tl
WHERE  tl.QUESTIONNAIRE_ID = :p_id AND tl.LANGUAGE = USERENV('LANG');
```

---

## 🔒 Observações

- Chave primária composta: `QUESTIONNAIRE_ID` + `LANGUAGE`.

---

## 🔗 PVOs Relacionados

### [[allocatedchecklisttaskspvo|AllocatedChecklistTasksPVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTranslationPEOBusinessGroupId | — |
| LANGUAGE | QuestionnaireTranslationPEOLanguage | — |
| NAME | QuestionnaireTranslationPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTranslationPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTranslationPEOQuestionnaireId | — |

### [[checklisttasktemplatepvo|ChecklistTaskTemplatePVO]] (HCM · BICC: 1/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTranslationPEOBusinessGroupId | — |
| LANGUAGE | QuestionnaireTranslationPEOLanguage | — |
| NAME | QuestionnaireTranslationPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTranslationPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTranslationPEOQuestionnaireId | — |

### [[feedbackdetailspvo|FeedbackDetailsPVO]] (HCM · BICC: 7/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy5 | — |
| CREATION_DATE | CreationDate5 | — |
| DESCRIPTION | Description | ✅ |
| INTRO_TEXT | IntroText | ✅ |
| KEYWORDS | Keywords | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate5 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin5 | — |
| LAST_UPDATED_BY | LastUpdatedBy5 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber4 | — |
| QSTNR_VERSION_NUM | QstnrVersionNum3 | — |
| QUESTIONNAIRE_ID | QuestionnaireId3 | — |
| SOURCE_LANG | SourceLang | ✅ |

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTLPEOBusinessGroupId | — |
| INTRO_TEXT | QuestionnaireTLPEOIntroText | — |
| LANGUAGE | QuestionnaireTLPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTLPEOLastUpdateDate | — |
| NAME | QuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | QuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTLPEOQuestionnaireId | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 1/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTLPEOBusinessGroupId | — |
| INTRO_TEXT | QuestionnaireTLPEOIntroText | — |
| LANGUAGE | QuestionnaireTLPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTLPEOLastUpdateDate | — |
| NAME | QuestionnaireTLPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTLPEOQuestionnaireId | — |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTLPEOBusinessGroupId | — |
| INTRO_TEXT | QuestionnaireTLPEOIntroText | — |
| LANGUAGE | QuestionnaireTLPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTLPEOLastUpdateDate | — |
| NAME | QuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | QuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTLPEOQuestionnaireId | — |

### [[participantquestionnairequestionresponselistpvo|ParticipantQuestionnaireQuestionResponseListPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireTLPEOBusinessGroupId | — |
| LANGUAGE | AdditionalQuestionnaireTLPEOLanguage | — |
| NAME | AdditionalQuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireTLPEOQuestionnaireId | — |

### [[questionanswerpvo|QuestionAnswerPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireTLPEOBusinessGroupId | — |
| LANGUAGE | AdditionalQuestionnaireTLPEOLanguage | — |
| NAME | AdditionalQuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireTLPEOQuestionnaireId | — |

### [[questionnairepvo|QuestionnairePVO]] (HCM · BICC: 2/15)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | BusinessGroupId1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DESCRIPTION | Description | — |
| INTRO_TEXT | IntroText | — |
| KEYWORDS | Keywords | — |
| LANGUAGE | Language1 | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber1 | — |
| QSTNR_VERSION_NUM | QstnrVersionNum1 | — |
| QUESTIONNAIRE_ID | QuestionnaireId1 | — |
| SOURCE_LANG | SourceLang | — |

### [[questionnairequestionresponselistpvo|QuestionnaireQuestionResponseListPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | AdditionalQuestionnaireTLPEOBusinessGroupId | — |
| LANGUAGE | AdditionalQuestionnaireTLPEOLanguage | — |
| NAME | AdditionalQuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | AdditionalQuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | AdditionalQuestionnaireTLPEOQuestionnaireId | — |

### [[requisitionqstnrexternalviewallpvo|RequisitionQstnrExternalViewAllPVO]] (PO · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTranslationPEOBusinessGroupId | — |
| DESCRIPTION | QuestionnaireTranslationPEODescription | ✅ |
| INTRO_TEXT | QuestionnaireTranslationPEOIntroText | — |
| LANGUAGE | QuestionnaireTranslationPEOLanguage | — |
| NAME | QuestionnaireTranslationPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTranslationPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTranslationPEOQuestionnaireId | — |

### [[requisitionqstnrinternalviewallpvo|RequisitionQstnrInternalViewAllPVO]] (PO · BICC: 2/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTranslationPEOBusinessGroupId | — |
| DESCRIPTION | QuestionnaireTranslationPEODescription | ✅ |
| INTRO_TEXT | QuestionnaireTranslationPEOIntroText | — |
| LANGUAGE | QuestionnaireTranslationPEOLanguage | — |
| NAME | QuestionnaireTranslationPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTranslationPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTranslationPEOQuestionnaireId | — |

### [[requisitionqstnrinterviewviewallpvo|RequisitionQstnrInterviewViewAllPVO]] (PO · BICC: 3/7)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTranslationPEOBusinessGroupId | — |
| DESCRIPTION | QuestionnaireTranslationPEODescription | ✅ |
| INTRO_TEXT | QuestionnaireTranslationPEOIntroText | ✅ |
| LANGUAGE | QuestionnaireTranslationPEOLanguage | — |
| NAME | QuestionnaireTranslationPEOName | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireTranslationPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTranslationPEOQuestionnaireId | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BUSINESS_GROUP_ID | QuestionnaireTLPEOBusinessGroupId | — |
| INTRO_TEXT | QuestionnaireTLPEOIntroText | — |
| LANGUAGE | QuestionnaireTLPEOLanguage | — |
| LAST_UPDATE_DATE | QuestionnaireTLPEOLastUpdateDate | — |
| NAME | QuestionnaireTLPEOName | — |
| QSTNR_VERSION_NUM | QuestionnaireTLPEOQstnrVersionNum | — |
| QUESTIONNAIRE_ID | QuestionnaireTLPEOQuestionnaireId | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
