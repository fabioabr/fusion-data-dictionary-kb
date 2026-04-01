---
id: DOC-PO-PVO-RepositoryResponseExtractPVO
doc_type: system-doc
title: "RepositoryResponseExtractPVO — PVO Purchasing"
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
  - RepositoryResponseExtractPVO
  - repositoryresponseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RepositoryResponseExtractPVO

## 📌 Visão Geral

Extrai respostas do repositório central de qualificação para carga BICC, com dados históricos de fornecedores armazenados para reutilização em novos processos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.RepositoryResponseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 30 | 1 | 1 | 30 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_response_repository|POQ_RESPONSE_REPOSITORY]] — 30 atributos (1 PKs, 30 BICC)

---

## ⚙️ Atributos

### [[poq_response_repository|POQ_RESPONSE_REPOSITORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptanceDate | ACCEPTANCE_DATE | — | ✅ |
| 2 | AcceptanceNote | ACCEPTANCE_NOTE | — | ✅ |
| 3 | AcceptedBy | ACCEPTED_BY | — | ✅ |
| 4 | BatchId | BATCH_ID | — | ✅ |
| 5 | CreatedBy | CREATED_BY | — | ✅ |
| 6 | CreationDate | CREATION_DATE | — | ✅ |
| 7 | DataSourceId | DATA_SOURCE_ID | — | ✅ |
| 8 | DataSourceType | DATA_SOURCE_TYPE | — | ✅ |
| 9 | FirstSubmissionDate | FIRST_SUBMISSION_DATE | — | ✅ |
| 10 | InternalRespondentId | INTERNAL_RESPONDENT_ID | — | ✅ |
| 11 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | MergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | OriginalQuestionId | ORIGINAL_QUESTION_ID | — | ✅ |
| 17 | QuestionId | QUESTION_ID | — | ✅ |
| 18 | RequestId | REQUEST_ID | — | ✅ |
| 19 | ResponderType | RESPONDER_TYPE | — | ✅ |
| 20 | ResponseArchiveDate | RESPONSE_ARCHIVE_DATE | — | ✅ |
| 21 | ResponseComments | RESPONSE_COMMENTS | — | ✅ |
| 22 | ResponseRepositoryId | RESPONSE_REPOSITORY_ID | 🔑 | ✅ |
| 23 | ResponseStatus | RESPONSE_STATUS | — | ✅ |
| 24 | ResponseSubmissionDate | RESPONSE_SUBMISSION_DATE | — | ✅ |
| 25 | SupplierContactPartyId | SUPPLIER_CONTACT_PARTY_ID | — | ✅ |
| 26 | SupplierId | SUPPLIER_ID | — | ✅ |
| 27 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |
| 28 | SurrogEnteredBy | SURROG_ENTERED_BY | — | ✅ |
| 29 | SurrogEntryDate | SURROG_ENTRY_DATE | — | ✅ |
| 30 | SurrogResponseFlag | SURROG_RESPONSE_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
