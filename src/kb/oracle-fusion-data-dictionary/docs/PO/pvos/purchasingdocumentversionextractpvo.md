---
id: DOC-PO-PVO-PurchasingDocumentVersionExtractPVO
doc_type: system-doc
title: "PurchasingDocumentVersionExtractPVO — PVO Purchasing"
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
  - PurchasingDocumentVersionExtractPVO
  - purchasingdocumentversionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PurchasingDocumentVersionExtractPVO

## 📌 Visão Geral

Extrai as versões históricas de documentos de compra para carga BICC, registrando alterações de preço, quantidade e condições. Suporta auditoria de mudanças e análise de renegociações.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoBiccExtractAM.PurchasingDocumentVersionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 45 | 1 | 1 | 45 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[po_versions|PO_VERSIONS]] — 45 atributos (1 PKs, 45 BICC)

---

## ⚙️ Atributos

### [[po_versions|PO_VERSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AcceptedDate | ACCEPTED_DATE | — | ✅ |
| 2 | ApprovedDate | APPROVED_DATE | — | ✅ |
| 3 | B2bMessageId | B2B_MESSAGE_ID | — | ✅ |
| 4 | BaseVersionId | BASE_VERSION_ID | — | ✅ |
| 5 | CancelBackingReqFlag | CANCEL_BACKING_REQ_FLAG | — | ✅ |
| 6 | CancelDocFlag | CANCEL_DOC_FLAG | — | ✅ |
| 7 | ChangeOrderDesc | CHANGE_ORDER_DESC | — | ✅ |
| 8 | ChangeOrderStatus | CHANGE_ORDER_STATUS | — | ✅ |
| 9 | ChangeOrderType | CHANGE_ORDER_TYPE | — | ✅ |
| 10 | CoCanceledByRole | CO_CANCELED_BY_ROLE | — | ✅ |
| 11 | CoCanceledByUserId | CO_CANCELED_BY_USER_ID | — | ✅ |
| 12 | CoCanceledFlag | CO_CANCELED_FLAG | — | ✅ |
| 13 | CoNum | CO_NUM | — | ✅ |
| 14 | CoSequence | CO_SEQUENCE | — | ✅ |
| 15 | CommunicatedDate | COMMUNICATED_DATE | — | ✅ |
| 16 | CommunicatedToSupplier | COMMUNICATED_TO_SUPPLIER | — | ✅ |
| 17 | CounterproposalFlag | COUNTERPROPOSAL_FLAG | — | ✅ |
| 18 | CreatedBy | CREATED_BY | — | ✅ |
| 19 | CreatedByProgramName | CREATED_BY_PROGRAM_NAME | — | ✅ |
| 20 | CreationDate | CREATION_DATE | — | ✅ |
| 21 | DocumentDate | DOCUMENT_DATE | — | ✅ |
| 22 | EsignEnvOwnerEmailId | ESIGN_ENV_OWNER_EMAIL_ID | — | ✅ |
| 23 | EsignEnvelopeId | ESIGN_ENVELOPE_ID | — | ✅ |
| 24 | EsignEnvelopeOwner | ESIGN_ENVELOPE_OWNER | — | ✅ |
| 25 | EsignEnvelopeStatus | ESIGN_ENVELOPE_STATUS | — | ✅ |
| 26 | ExternalSystemFlag | EXTERNAL_SYSTEM_FLAG | — | ✅ |
| 27 | FundsStatus | FUNDS_STATUS | — | ✅ |
| 28 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 29 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 30 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 31 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 32 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 33 | OnlineReportId | ONLINE_REPORT_ID | — | ✅ |
| 34 | OriginatorId | ORIGINATOR_ID | — | ✅ |
| 35 | OriginatorRole | ORIGINATOR_ROLE | — | ✅ |
| 36 | PendingResponseRole | PENDING_RESPONSE_ROLE | — | ✅ |
| 37 | PoHeaderId | PO_HEADER_ID | — | ✅ |
| 38 | ProcessedDate | PROCESSED_DATE | — | ✅ |
| 39 | RejectedFlag | REJECTED_FLAG | — | ✅ |
| 40 | RequestDate | REQUEST_DATE | — | ✅ |
| 41 | RequestId | REQUEST_ID | — | ✅ |
| 42 | RevisionNum | REVISION_NUM | — | ✅ |
| 43 | SubmittedDate | SUBMITTED_DATE | — | ✅ |
| 44 | VersionId | VERSION_ID | 🔑 | ✅ |
| 45 | WithdrawnFlag | WITHDRAWN_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
