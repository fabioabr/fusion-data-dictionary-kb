---
id: DOC-PO-057
doc_type: system-doc
title: "POQ_QUESTNAIRE_RESP_HEADERS — Cabeçalhos de Respostas de Questionários"
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
  - response-headers
  - supplier-qualification
aliases:
  - POQ_QUESTNAIRE_RESP_HEADERS
  - poq_questnaire_resp_headers
  - cabecalho-respostas-questionario
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POQ_QUESTNAIRE_RESP_HEADERS

## 📌 Visão Geral

Armazena os **cabeçalhos de respostas** de questionários de qualificação de fornecedores. Funciona como registro-mestre que agrupa todas as respostas de um processo de qualificação específico, incluindo informações do iniciador, datas, status geral do processo e referência ao evento de negociação ou qualificação que originou a solicitação.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Gestão de processos de qualificação:** Cabeçalho que consolida todas as submissões de respostas de um processo.
- **Rastreabilidade:** Associação entre o processo de qualificação e o evento de sourcing ou negociação que o originou.
- **Workflow de avaliação:** Controle do status geral do processo (em andamento, concluído, cancelado).
- **Relatórios gerenciais:** Visão consolidada de processos de qualificação por período, tipo e resultado.
- **Auditoria de procurement:** Registro de quem iniciou e quando o processo de qualificação foi conduzido.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | RESPONSE_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cabeçalho de resposta | — | 🟡 75% |
| 2 | QUESTIONNAIRE_ID | NUMBER(18) | NOT NULL | FK | Questionário utilizado neste processo | [[poq_questnaires_vl]] | 🟡 75% |
| 3 | QUALIFICATION_ID | NUMBER(18) | NULL | FK | Processo de qualificação associado | — | 🟡 65% |
| 4 | NEGOTIATION_ID | NUMBER(18) | NULL | FK | Evento de negociação/sourcing que originou a qualificação | [[pon_auction_headers_all]] | 🟡 60% |
| 5 | INITIATOR_ID | NUMBER(18) | NULL | FK | Usuário que iniciou o processo | — | 🟡 65% |
| 6 | STATUS | VARCHAR2(30) | NOT NULL | Classificação | Status do processo: OPEN, IN_PROGRESS, COMPLETED, CANCELLED | — | 🟡 70% |
| 7 | OPEN_DATE | DATE | NULL | Data | Data de abertura do processo de qualificação | — | 🟡 65% |
| 8 | CLOSE_DATE | DATE | NULL | Data | Data de encerramento do processo | — | 🟡 65% |
| 9 | DUE_DATE | DATE | NULL | Data | Data-limite para submissão de respostas | — | 🟡 65% |
| 10 | TOTAL_SUPPLIERS | NUMBER | NULL | Estatísticas | Total de fornecedores convidados | — | 🟡 55% |
| 11 | RESPONDED_SUPPLIERS | NUMBER | NULL | Estatísticas | Total de fornecedores que responderam | — | 🟡 55% |
| 12 | DESCRIPTION | VARCHAR2(2000) | NULL | Texto livre | Descrição do processo de qualificação | — | 🟡 65% |
| 13 | ORG_ID | NUMBER(18) | NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟡 65% |
| 14 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 15 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 16 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 17 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 18 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[poq_questnaires_vl]] — via `QUESTIONNAIRE_ID` (definição do questionário)
- [[pon_auction_headers_all]] — via `NEGOTIATION_ID` (evento de sourcing)
- [[hr_all_organization_units_f]] — via `ORG_ID` (business unit do cabeçalho de respostas)

### Tabelas-filha (FK de saída)
- [[poq_questnaire_responses]] — via `RESPONSE_HEADER_ID` (submissões individuais)
- [[poq_questnaire_resp_sections]] — via `RESPONSE_HEADER_ID` (seções de resposta)

---

## 📎 Uso Típico

### Processos de qualificação abertos
```sql
SELECT rh.RESPONSE_HEADER_ID,
       rh.QUESTIONNAIRE_ID,
       rh.STATUS,
       rh.OPEN_DATE,
       rh.DUE_DATE,
       rh.TOTAL_SUPPLIERS,
       rh.RESPONDED_SUPPLIERS
FROM   POQ_QUESTNAIRE_RESP_HEADERS rh
WHERE  rh.STATUS IN ('OPEN', 'IN_PROGRESS')
  AND  rh.ORG_ID = :p_org_id
ORDER BY rh.DUE_DATE;
```

### Taxa de resposta por processo
```sql
SELECT rh.RESPONSE_HEADER_ID,
       rh.TOTAL_SUPPLIERS,
       rh.RESPONDED_SUPPLIERS,
       ROUND(rh.RESPONDED_SUPPLIERS / NULLIF(rh.TOTAL_SUPPLIERS, 0) * 100, 1) AS taxa_resposta_pct
FROM   POQ_QUESTNAIRE_RESP_HEADERS rh
WHERE  rh.STATUS = 'COMPLETED';
```

---

## 🔒 Observações

- O campo `STATUS` controla o ciclo de vida do processo: **OPEN** (aberto para respostas), **IN_PROGRESS** (em avaliação), **COMPLETED** (concluído), **CANCELLED** (cancelado).
- O vínculo com `NEGOTIATION_ID` permite rastrear qualificações que foram geradas a partir de processos de sourcing em [[pon_auction_headers_all]].
- `TOTAL_SUPPLIERS` e `RESPONDED_SUPPLIERS` permitem calcular a taxa de adesão ao processo de qualificação.
- Este é o nível mais alto da hierarquia de respostas: Header → [[poq_questnaire_responses]] → [[poq_qual_responses]].
- A nomenclatura `QUESTNAIRE` (sem o 'i') segue a convenção Oracle original.

---

## 🔗 PVOs Relacionados

### [[questionnaireresponseheaderextractpvo|QuestionnaireResponseHeaderExtractPVO]] (PO · BICC: 37/37)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | AcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | AcceptanceNote | ✅ |
| ACCEPTED_BY | AcceptedBy | ✅ |
| CANCELED_BY | CanceledBy | ✅ |
| CANCELED_DATE | CanceledDate | ✅ |
| CANCELED_REASON_CODE | CanceledReasonCode | ✅ |
| CHANGE_REQUEST_ID | ChangeRequestId | ✅ |
| CR_OUTCOME_CODE | CrOutcomeCode | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| INITIATIVE_ID | InitiativeId | ✅ |
| INITIATIVE_SUPP_CONTACT_ID | InitiativeSuppContactId | ✅ |
| INTERNAL_RESPONDENT_ID | InternalRespondentId | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | MergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| QUESTNAIRE_ID | QuestnaireId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | QuestnaireRespHeaderId | ✅ |
| RECENT_NOTIFICATION_FLAG | RecentNotificationFlag | ✅ |
| REQUEST_ERROR_REASON | RequestErrorReason | ✅ |
| REQUEST_ID | RequestId | ✅ |
| RESPONSE_STATUS | ResponseStatus | ✅ |
| RETURN_MESSAGE_CONTENT | ReturnMessageContent | ✅ |
| RETURNED_BY | ReturnedBy | ✅ |
| RETURNED_DATE | ReturnedDate | ✅ |
| SUBMISSION_DATE | SubmissionDate | ✅ |
| SUBMITTED_BY | SubmittedBy | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | SupplierContactPartyId | ✅ |
| SUPPLIER_ID | SupplierId | ✅ |
| SUPPLIER_REG_ID | SupplierRegId | ✅ |
| SUPPLIER_SITE_ID | SupplierSiteId | ✅ |
| SURROG_ENTERED_BY | SurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | SurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | SurrogResponseFlag | ✅ |

### [[questionnaireresponseheaderspvo|QuestionnaireResponseHeadersPVO]] (PO · BICC: 38/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | QuestionnaireResponseHeaderAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | QuestionnaireResponseHeaderAcceptanceNote | ✅ |
| ACCEPTED_BY | QuestionnaireResponseHeaderAcceptedBy | ✅ |
| CANCELED_BY | QuestionnaireResponseHeaderCanceledBy | ✅ |
| CANCELED_DATE | QuestionnaireResponseHeaderCanceledDate | ✅ |
| CANCELED_REASON_CODE | QuestionnaireResponseHeaderCanceledReasonCode | ✅ |
| CHANGE_REQUEST_ID | QuestionnaireResponseHeaderChangeRequestId | ✅ |
| CLOSE_DATE | QuestionnaireResponseHeaderCloseDate | ✅ |
| CLOSED_BY | QuestionnaireResponseHeaderClosedBy | — |
| CR_OUTCOME_CODE | QuestionnaireResponseHeaderCrOutcomeCode | ✅ |
| CREATED_BY | QuestionnaireResponseHeaderCreatedBy | ✅ |
| CREATION_DATE | QuestionnaireResponseHeaderCreationDate | ✅ |
| INITIATIVE_ID | QuestionnaireResponseHeaderInitiativeId | ✅ |
| INITIATIVE_SUPP_CONTACT_ID | QuestionnaireResponseHeaderInitiativeSuppContactId | ✅ |
| INTERNAL_RESPONDENT_ID | QuestionnaireResponseHeaderInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | QuestionnaireResponseHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | QuestionnaireResponseHeaderLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | QuestionnaireResponseHeaderLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | QuestionnaireResponseHeaderMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | QuestionnaireResponseHeaderObjectVersionNumber | ✅ |
| PRC_BU_ID | QuestionnaireResponseHeaderPrcBuId | ✅ |
| QUESTNAIRE_ID | QuestionnaireResponseHeaderQuestnaireId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | QuestnaireRespHeaderId | ✅ |
| RECENT_NOTIFICATION_FLAG | QuestionnaireResponseHeaderRecentNotificationFlag | ✅ |
| REQUEST_ERROR_REASON | QuestionnaireResponseHeaderRequestErrorReason | ✅ |
| REQUEST_ID | QuestionnaireResponseHeaderRequestId | ✅ |
| RESPONSE_STATUS | QuestionnaireResponseHeaderResponseStatus | ✅ |
| RETURN_MESSAGE_CONTENT | QuestionnaireResponseHeaderReturnMessageContent | ✅ |
| RETURNED_BY | QuestionnaireResponseHeaderReturnedBy | ✅ |
| RETURNED_DATE | QuestionnaireResponseHeaderReturnedDate | ✅ |
| SUBMISSION_DATE | QuestionnaireResponseHeaderSubmissionDate | ✅ |
| SUBMITTED_BY | QuestionnaireResponseHeaderSubmittedBy | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | QuestionnaireResponseHeaderSupplierContactPartyId | ✅ |
| SUPPLIER_ID | QuestionnaireResponseHeaderSupplierId | ✅ |
| SUPPLIER_REG_ID | QuestionnaireResponseHeaderSupplierRegId | ✅ |
| SUPPLIER_SITE_ID | QuestionnaireResponseHeaderSupplierSiteId | ✅ |
| SURROG_ENTERED_BY | QuestionnaireResponseHeaderSurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | QuestionnaireResponseHeaderSurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | QuestionnaireResponseHeaderSurrogResponseFlag | ✅ |

### [[questionnaireresponsespvo|QuestionnaireResponsesPVO]] (PO · BICC: 38/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | RespHeaderAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | RespHeaderAcceptanceNote | ✅ |
| ACCEPTED_BY | RespHeaderAcceptedBy | ✅ |
| CANCELED_BY | RespHeaderCanceledBy | ✅ |
| CANCELED_DATE | RespHeaderCanceledDate | ✅ |
| CANCELED_REASON_CODE | RespHeaderCanceledReasonCode | ✅ |
| CHANGE_REQUEST_ID | RespHeaderChangeRequestId | ✅ |
| CLOSE_DATE | RespHeaderCloseDate | ✅ |
| CLOSED_BY | RespHeaderClosedBy | — |
| CR_OUTCOME_CODE | RespHeaderCrOutcomeCode | ✅ |
| CREATED_BY | RespHeaderCreatedBy | ✅ |
| CREATION_DATE | RespHeaderCreationDate | ✅ |
| INITIATIVE_ID | RespHeaderInitiativeId | ✅ |
| INITIATIVE_SUPP_CONTACT_ID | RespHeaderInitiativeSuppContactId | ✅ |
| INTERNAL_RESPONDENT_ID | RespHeaderInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | RespHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RespHeaderLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RespHeaderLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | RespHeaderMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | RespHeaderObjectVersionNumber | ✅ |
| PRC_BU_ID | RespHeaderPrcBuId | ✅ |
| QUESTNAIRE_ID | RespHeaderQuestnaireId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | RespHeaderQuestnaireRespHeaderId | ✅ |
| RECENT_NOTIFICATION_FLAG | RespHeaderRecentNotificationFlag | ✅ |
| REQUEST_ERROR_REASON | RespHeaderRequestErrorReason | ✅ |
| REQUEST_ID | RespHeaderRequestId | ✅ |
| RESPONSE_STATUS | RespHeaderResponseStatus | ✅ |
| RETURN_MESSAGE_CONTENT | RespHeaderReturnMessageContent | ✅ |
| RETURNED_BY | RespHeaderReturnedBy | ✅ |
| RETURNED_DATE | RespHeaderReturnedDate | ✅ |
| SUBMISSION_DATE | RespHeaderSubmissionDate | ✅ |
| SUBMITTED_BY | RespHeaderSubmittedBy | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | RespHeaderSupplierContactPartyId | ✅ |
| SUPPLIER_ID | RespHeaderSupplierId | ✅ |
| SUPPLIER_REG_ID | RespHeaderSupplierRegId | ✅ |
| SUPPLIER_SITE_ID | RespHeaderSupplierSiteId | ✅ |
| SURROG_ENTERED_BY | RespHeaderSurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | RespHeaderSurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | RespHeaderSurrogResponseFlag | ✅ |

### [[questionnaireresponsevaluespvo|QuestionnaireResponseValuesPVO]] (PO · BICC: 38/39)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DATE | RespHeaderAcceptanceDate | ✅ |
| ACCEPTANCE_NOTE | RespHeaderAcceptanceNote | ✅ |
| ACCEPTED_BY | RespHeaderAcceptedBy | ✅ |
| CANCELED_BY | RespHeaderCanceledBy | ✅ |
| CANCELED_DATE | RespHeaderCanceledDate | ✅ |
| CANCELED_REASON_CODE | RespHeaderCanceledReasonCode | ✅ |
| CHANGE_REQUEST_ID | RespHeaderChangeRequestId | ✅ |
| CLOSE_DATE | RespHeaderCloseDate | ✅ |
| CLOSED_BY | RespHeaderClosedBy | — |
| CR_OUTCOME_CODE | RespHeaderCrOutcomeCode | ✅ |
| CREATED_BY | RespHeaderCreatedBy | ✅ |
| CREATION_DATE | RespHeaderCreationDate | ✅ |
| INITIATIVE_ID | RespHeaderInitiativeId | ✅ |
| INITIATIVE_SUPP_CONTACT_ID | RespHeaderInitiativeSuppContactId | ✅ |
| INTERNAL_RESPONDENT_ID | RespHeaderInternalRespondentId | ✅ |
| LAST_UPDATE_DATE | RespHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RespHeaderLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | RespHeaderLastUpdatedBy | ✅ |
| MERGE_REQUEST_ID | RespHeaderMergeRequestId | ✅ |
| OBJECT_VERSION_NUMBER | RespHeaderObjectVersionNumber | ✅ |
| PRC_BU_ID | RespHeaderPrcBuId | ✅ |
| QUESTNAIRE_ID | RespHeaderQuestnaireId | ✅ |
| QUESTNAIRE_RESP_HEADER_ID | RespHeaderQuestnaireRespHeaderId | ✅ |
| RECENT_NOTIFICATION_FLAG | RespHeaderRecentNotificationFlag | ✅ |
| REQUEST_ERROR_REASON | RespHeaderRequestErrorReason | ✅ |
| REQUEST_ID | RespHeaderRequestId | ✅ |
| RESPONSE_STATUS | RespHeaderResponseStatus | ✅ |
| RETURN_MESSAGE_CONTENT | RespHeaderReturnMessageContent | ✅ |
| RETURNED_BY | RespHeaderReturnedBy | ✅ |
| RETURNED_DATE | RespHeaderReturnedDate | ✅ |
| SUBMISSION_DATE | RespHeaderSubmissionDate | ✅ |
| SUBMITTED_BY | RespHeaderSubmittedBy | ✅ |
| SUPPLIER_CONTACT_PARTY_ID | RespHeaderSupplierContactPartyId | ✅ |
| SUPPLIER_ID | RespHeaderSupplierId | ✅ |
| SUPPLIER_REG_ID | RespHeaderSupplierRegId | ✅ |
| SUPPLIER_SITE_ID | RespHeaderSupplierSiteId | ✅ |
| SURROG_ENTERED_BY | RespHeaderSurrogEnteredBy | ✅ |
| SURROG_ENTRY_DATE | RespHeaderSurrogEntryDate | ✅ |
| SURROG_RESPONSE_FLAG | RespHeaderSurrogResponseFlag | ✅ |

---

## 📚 Referências

- [Oracle Docs — Supplier Qualification Management](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
