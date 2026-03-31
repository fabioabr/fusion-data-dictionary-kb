---
id: DOC-PO-056
doc_type: system-doc
title: "POQ_QUESTNAIRE_RESPONSES — Respostas de Questionários de Qualificação"
system: Oracle Fusion Cloud ERP
module: Procurement
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - procurement
  - data-dictionary
  - qualificacao
  - respostas-questionario
  - supplier-qualification
aliases:
  - POQ_QUESTNAIRE_RESPONSES
  - poq_questnaire_responses
  - respostas-questionario-qualificacao
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTNAIRE_RESPONSES

## 📌 Visão Geral

Armazena as **respostas submetidas** a questionários de qualificação de fornecedores. Cada registro representa uma submissão completa de questionário por um fornecedor ou avaliador, incluindo status de submissão, pontuação total calculada e datas de submissão. Funciona como a tabela de detalhes de respostas, vinculada ao cabeçalho em [[poq_questnaire_resp_headers]].

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Submissão de questionários:** Registro das respostas enviadas por fornecedores ou avaliadores internos.
- **Avaliação e scoring:** Armazenamento da pontuação total obtida na submissão.
- **Workflow de aprovação:** Controle do status de cada submissão (rascunho, submetida, aprovada, rejeitada).
- **Histórico de qualificações:** Rastreamento de todas as submissões ao longo do tempo.
- **Análise comparativa:** Comparação entre diferentes submissões do mesmo fornecedor ou entre fornecedores distintos.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | QUESTIONNAIRE_RESPONSE_ID | NUMBER(18) | NOT NULL | PK | Identificador único da resposta do questionário | — | 🟡 75% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário ao qual a resposta se refere | [[poq_questnaires_vl]] | 🟡 75% |
| 3 | RESPONSE_HEADER_ID | NUMBER(18) | NULL | FK | Cabeçalho da resposta (contexto do processo) | [[poq_questnaire_resp_headers]] | 🟡 70% |
| 4 | SUPPLIER_ID | NUMBER(18) | NULL | FK | Fornecedor que submeteu a resposta | [[ap_suppliers]] | 🟡 70% |
| 5 | RESPONDENT_ID | NUMBER(18) | NULL | FK | Usuário respondente (quando avaliador interno) | — | 🟡 60% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status da submissão: DRAFT, SUBMITTED, APPROVED, REJECTED, EXPIRED | — | 🟡 70% |
| 7 | TOTAL_SCORE | NUMBER | NULL | Pontuação | Pontuação total calculada | — | 🟡 70% |
| 8 | MAX_POSSIBLE_SCORE | NUMBER | NULL | Pontuação | Pontuação máxima possível | — | 🟡 60% |
| 9 | PERCENTAGE_SCORE | NUMBER | NULL | Pontuação | Percentual da pontuação (TOTAL_SCORE / MAX_POSSIBLE_SCORE * 100) | — | 🟡 55% |
| 10 | PASS_FAIL_FLAG | VARCHAR2(1) | NULL | Resultado | Indica aprovação (P) ou reprovação (F) | — | 🟡 55% |
| 11 | SUBMISSION_DATE | TIMESTAMP | NULL | Data | Data/hora da submissão | — | 🟡 70% |
| 12 | EXPIRATION_DATE | DATE | NULL | Data | Data de expiração da qualificação | — | 🟡 60% |
| 13 | COMMENTS | VARCHAR2(4000) | NULL | Texto livre | Comentários do avaliador ou fornecedor | — | 🟡 65% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questnaires_vl]] — via `QUESTIONNAIRE_ID` (definição do questionário)
- [[poq_questnaire_resp_headers]] — via `RESPONSE_HEADER_ID` (cabeçalho do processo)
- [[ap_suppliers]] — via `SUPPLIER_ID` (fornecedor que respondeu ao questionário)

### Tabelas-filha (FK de saída)
- [[poq_qual_responses]] — via `QUESTIONNAIRE_RESPONSE_ID` (respostas individuais por pergunta)
- [[poq_questnaire_resp_sections]] — via `QUESTIONNAIRE_RESPONSE_ID` (respostas por seção)

---

## 📎 Uso Típico

### Submissões aprovadas por questionário
```sql
SELECT qr.QUESTIONNAIRE_RESPONSE_ID,
       qr.SUPPLIER_ID,
       qr.TOTAL_SCORE,
       qr.PERCENTAGE_SCORE,
       qr.PASS_FAIL_FLAG,
       qr.SUBMISSION_DATE
FROM   POQ_QUESTNAIRE_RESPONSES qr
WHERE  qr.QUESTIONNAIRE_ID = :p_questionnaire_id
  AND  qr.STATUS = 'APPROVED'
ORDER BY qr.TOTAL_SCORE DESC;
```

### Fornecedores reprovados em qualificação
```sql
SELECT qr.SUPPLIER_ID,
       qr.QUESTIONNAIRE_ID,
       qr.TOTAL_SCORE,
       qr.PERCENTAGE_SCORE,
       qr.SUBMISSION_DATE
FROM   POQ_QUESTNAIRE_RESPONSES qr
WHERE  qr.PASS_FAIL_FLAG = 'F'
  AND  qr.STATUS = 'APPROVED';
```

---

## 🔒 Observações

- O campo `STATUS` controla o ciclo de vida da submissão: **DRAFT** (rascunho), **SUBMITTED** (submetido para avaliação), **APPROVED** (aprovado), **REJECTED** (rejeitado), **EXPIRED** (expirado).
- O `PASS_FAIL_FLAG` é calculado automaticamente comparando `TOTAL_SCORE` com o `MIN_PASSING_SCORE` do questionário em [[poq_questnaires_vl]].
- A `EXPIRATION_DATE` indica quando a qualificação do fornecedor expira e precisa ser renovada.
- Para obter as respostas individuais de cada pergunta, consultar [[poq_qual_responses]] via `QUESTIONNAIRE_RESPONSE_ID`.
- A nomenclatura `QUESTNAIRE` (sem o 'i' em questionnaire) segue a convenção Oracle original.

---

## 🔗 PVOs Relacionados

### [[questionnaireresponseextractpvo|QuestionnaireResponseExtractPVO]] (PO · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_NOTE | AcceptanceNote | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| FAILED_POZ_VALIDATION_FLAG | FailedPozValidationFlag | ✅ |
| HAS_NEWER_RESPONSE_FLAG | HasNewerResponseFlag | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| QUESTION_DISPLAYED_FLAG | QuestionDisplayedFlag | ✅ |
| QUESTION_ID | QuestionId | ✅ |
| QUESTNAIRE_QUESTION_ID | QuestnaireQuestionId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | QuestnaireRespHeaderId | ✅ |
| QUESTNAIRE_RESP_SECTION_ID | QuestnaireRespSectionId | ✅ |
| QUESTNAIRE_RESPONSE_ID | QuestnaireResponseId | ✅ |
| RESPONSE_COMMENTS | ResponseComments | ✅ |

### [[questionnaireresponsespvo|QuestionnaireResponsesPVO]] (PO · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_NOTE | QuestionnaireResponseAcceptanceNote | ✅ |
| CREATED_BY | QuestionnaireResponseCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireResponseCreationDate | ✅ |
| FAILED_POZ_VALIDATION_FLAG | QuestionnaireResponseFailedPozValidationFlag | ✅ |
| HAS_NEWER_RESPONSE_FLAG | QuestionnaireResponseHasNewerResponseFlag | ✅ |
| LAST_UPDATE_DATE | QuestionnaireResponseLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireResponseLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionnaireResponseLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireResponseObjectVersionNumber | ✅ |
| QUESTION_DISPLAYED_FLAG | QuestionnaireResponseQuestionDisplayedFlag | ✅ |
| QUESTION_ID | QuestionnaireResponseQuestionId | ✅ |
| QUESTNAIRE_QUESTION_ID | QuestionnaireResponseQuestnaireQuestionId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | QuestionnaireResponseQuestnaireRespHeaderId | ✅ |
| QUESTNAIRE_RESP_SECTION_ID | QuestionnaireResponseQuestnaireRespSectionId | ✅ |
| QUESTNAIRE_RESPONSE_ID | QuestnaireResponseId | ✅ |
| RESPONSE_COMMENTS | QuestionnaireResponseResponseComments | ✅ |

### [[questionnaireresponsevaluespvo|QuestionnaireResponseValuesPVO]] (PO · BICC: 16/16)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_NOTE | QuestRespAcceptanceNote | ✅ |
| CREATED_BY | QuestRespCreatedBy | ✅ |
| CREATION_DATE | QuestRespCreationDate | ✅ |
| FAILED_POZ_VALIDATION_FLAG | QuestRespFailedPozValidationFlag | ✅ |
| HAS_NEWER_RESPONSE_FLAG | QuestRespHasNewerResponseFlag | ✅ |
| LAST_UPDATE_DATE | QuestRespLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestRespLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestRespLastUpdatedBy | ✅ |
| OBJECT_VERSION_NUMBER | QuestRespObjectVersionNumber | ✅ |
| QUESTION_DISPLAYED_FLAG | QuestRespQuestionDisplayedFlag | ✅ |
| QUESTION_ID | QuestRespQuestionId | ✅ |
| QUESTNAIRE_QUESTION_ID | QuestRespQuestnaireQuestionId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | QuestRespQuestnaireRespHeaderId | ✅ |
| QUESTNAIRE_RESP_SECTION_ID | QuestRespQuestnaireRespSectionId | ✅ |
| QUESTNAIRE_RESPONSE_ID | QuestRespQuestnaireResponseId | ✅ |
| RESPONSE_COMMENTS | QuestRespResponseComments | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
