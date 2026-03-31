---
id: DOC-HCM-189
doc_type: system-doc
title: "HRQ_QSTNR_SECTIONS_B — Seções de Questionários (Base)"
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
  - sections
aliases:
  - HRQ_QSTNR_SECTIONS_B
  - hrq_qstnr_sections_b
  - seções-de-questionários-base
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# HRQ_QSTNR_SECTIONS_B

## 📌 Visão Geral

Tabela base das **seções de questionários** HCM. Organiza questões em grupos lógicos.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Estruturação:** Seções lógicas.
- **Organização:** Agrupamento temático de questões.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle.
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle.
> - 🔴 **0–50%** — Existência ou tipo incertos; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | SECTION_ID | NUMBER(18) | NOT NULL | PK | Identificador único | — | 🟢 95% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário | [[hrq_questionnaires_b]] | 🟢 90% |
| 3 | SECTION_CODE | VARCHAR2(30) | NULL | Identificação | Código da seção | — | 🟡 75% |
| 4 | DISPLAY_SEQUENCE | NUMBER | NULL | Ordenação | Ordem de exibição | — | 🟡 75% |
| 5 | OBJECT_VERSION_NUMBER | NUMBER(9) | NOT NULL | Controle | Controle de concorrência | — | 🟢 95% |
| 6 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 100% |
| 7 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 100% |
| 8 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 100% |
| 9 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 100% |
| 10 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai
- [[hrq_questionnaires_b]] — via `QUESTIONNAIRE_ID` (questionario da secao)

### Tabelas relacionadas

---

## 📎 Uso Típico

### Seções de um questionário
```sql
SELECT s.SECTION_ID, s.SECTION_CODE, s.DISPLAY_SEQUENCE
FROM   HRQ_QSTNR_SECTIONS_B s
WHERE  s.QUESTIONNAIRE_ID = :p_id
ORDER BY s.DISPLAY_SEQUENCE;
```

---

## 🔒 Observações

- Tabela base (sufixo `_B`) — traduções em [[hrq_qstnr_sections_tl]].

---

## 🔗 PVOs Relacionados

### [[managerquestionnairequestionpvo|ManagerQuestionnaireQuestionPVO]] (HCM · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireSectionBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireSectionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireSectionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireSectionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireSectionBPEOLastUpdatedBy | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | — |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| OBJECT_VERSION_NUMBER | QuestionnaireSectionBPEOObjectVersionNumber | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | — |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | — |

### [[participantquestionnairequestionpvo|ParticipantQuestionnaireQuestionPVO]] (HCM · BICC: 5/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireSectionBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireSectionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireSectionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireSectionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireSectionBPEOLastUpdatedBy | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | — |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| OBJECT_VERSION_NUMBER | QuestionnaireSectionBPEOObjectVersionNumber | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | ✅ |

### [[participantquestionnairequestionpvoforpotentialassessement|ParticipantQuestionnaireQuestionPVOForPotentialAssessement]] (HCM · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireSectionBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireSectionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireSectionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireSectionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireSectionBPEOLastUpdatedBy | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | — |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| OBJECT_VERSION_NUMBER | QuestionnaireSectionBPEOObjectVersionNumber | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | — |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | — |

### [[questionnaireallquestionsp1|QuestionnaireAllQuestionsP1]] (HCM · BICC: 3/11)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | ✅ |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | — |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | ✅ |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | ✅ |

### [[questionnairequestionpvo|QuestionnaireQuestionPVO]] (HCM · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireSectionBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireSectionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireSectionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireSectionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireSectionBPEOLastUpdatedBy | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | — |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| OBJECT_VERSION_NUMBER | QuestionnaireSectionBPEOObjectVersionNumber | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | — |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | — |

### [[workerquestionnairequestionpvo|WorkerQuestionnaireQuestionPVO]] (HCM · BICC: 3/17)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_ADHOC | QuestionnaireSectionBPEOAllowAdhoc | — |
| BUSINESS_GROUP_ID | QuestionnaireSectionBPEOBusinessGroupId | ✅ |
| CREATED_BY | QuestionnaireSectionBPEOCreatedBy | — |
| CREATION_DATE | QuestionnaireSectionBPEOCreationDate | — |
| LAST_UPDATE_DATE | QuestionnaireSectionBPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireSectionBPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | QuestionnaireSectionBPEOLastUpdatedBy | — |
| MANDATORY | QuestionnaireSectionBPEOMandatory | — |
| MODULE_ID | QuestionnaireSectionBPEOModuleId | — |
| NEW_PAGE | QuestionnaireSectionBPEONewPage | — |
| OBJECT_VERSION_NUMBER | QuestionnaireSectionBPEOObjectVersionNumber | — |
| QSTNR_SECTION_ID | QuestionnaireSectionBPEOQstnrSectionId | ✅ |
| QSTNR_VERSION_NUM | QuestionnaireSectionBPEOQstnrVersionNum | — |
| QUESTION_ORDER | QuestionnaireSectionBPEOQuestionOrder | — |
| QUESTIONNAIRE_ID | QuestionnaireSectionBPEOQuestionnaireId | — |
| RESPONSE_ORDER | QuestionnaireSectionBPEOResponseOrder | — |
| SECTION_SEQ_NUM | QuestionnaireSectionBPEOSectionSeqNum | — |

---

## 📚 Referências

- [Oracle Fusion HCM Tables and Views](https://docs.oracle.com/en/cloud/saas/human-resources/25a/)
- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
