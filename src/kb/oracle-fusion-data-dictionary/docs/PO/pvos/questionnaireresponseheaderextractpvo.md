---
id: DOC-PO-PVO-QuestionnaireResponseHeaderExtractPVO
doc_type: system-doc
title: "QuestionnaireResponseHeaderExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QuestionnaireResponseHeaderExtractPVO
  - questionnaireresponseheaderextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireResponseHeaderExtractPVO

## 📌 Visão Geral

Extrai os cabeçalhos de respostas a questionários para carga BICC, com data de submissão, respondente e status. Permite análise de taxa de resposta e tempo de preenchimento.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireResponseHeaderExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 37 | 1 | 1 | 37 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_resp_headers|POQ_QUESTNAIRE_RESP_HEADERS]] — 37 atributos (1 PKs, 37 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_resp_headers|POQ_QUESTNAIRE_RESP_HEADERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceDate | ACCEPTANCE_DATE | — | ✅ |
| 2 | AcceptanceNote | ACCEPTANCE_NOTE | — | ✅ |
| 3 | AcceptedBy | ACCEPTED_BY | — | ✅ |
| 4 | CanceledBy | CANCELED_BY | — | ✅ |
| 5 | CanceledDate | CANCELED_DATE | — | ✅ |
| 6 | CanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 7 | ChangeRequestId | CHANGE_REQUEST_ID | — | ✅ |
| 8 | CrOutcomeCode | CR_OUTCOME_CODE | — | ✅ |
| 9 | CreatedBy | CREATED_BY | — | ✅ |
| 10 | CreationDate | CREATION_DATE | — | ✅ |
| 11 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 12 | InitiativeSuppContactId | INITIATIVE_SUPP_CONTACT_ID | — | ✅ |
| 13 | InternalRespondentId | INTERNAL_RESPONDENT_ID | — | ✅ |
| 14 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 16 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | MergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 18 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 19 | PrcBuId | PRC_BU_ID | — | ✅ |
| 20 | QuestnaireId | QUESTNAIRE_ID | — | ✅ |
| 21 | QuestnaireRespHeaderId | QUESTNAIRE_RESP_HEADER_ID | 🔑 | ✅ |
| 22 | RecentNotificationFlag | RECENT_NOTIFICATION_FLAG | — | ✅ |
| 23 | RequestErrorReason | REQUEST_ERROR_REASON | — | ✅ |
| 24 | RequestId | REQUEST_ID | — | ✅ |
| 25 | ResponseStatus | RESPONSE_STATUS | — | ✅ |
| 26 | ReturnMessageContent | RETURN_MESSAGE_CONTENT | — | ✅ |
| 27 | ReturnedBy | RETURNED_BY | — | ✅ |
| 28 | ReturnedDate | RETURNED_DATE | — | ✅ |
| 29 | SubmissionDate | SUBMISSION_DATE | — | ✅ |
| 30 | SubmittedBy | SUBMITTED_BY | — | ✅ |
| 31 | SupplierContactPartyId | SUPPLIER_CONTACT_PARTY_ID | — | ✅ |
| 32 | SupplierId | SUPPLIER_ID | — | ✅ |
| 33 | SupplierRegId | SUPPLIER_REG_ID | — | ✅ |
| 34 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 35 | SurrogEnteredBy | SURROG_ENTERED_BY | — | ✅ |
| 36 | SurrogEntryDate | SURROG_ENTRY_DATE | — | ✅ |
| 37 | SurrogResponseFlag | SURROG_RESPONSE_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
