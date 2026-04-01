---
id: DOC-PO-144
doc_type: system-doc
title: "PO_VERSIONS_INIT_SEQUENCE_V — Sequencia Inicial de Versoes de PO (View)"
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
  - versionamento
  - change-tracking
  - versoes
aliases:
  - PO_VERSIONS_INIT_SEQUENCE_V
  - po_versions_init_sequence_v
  - po-versions-init-sequence-v
  - po-versions
  - sequencia-inicial-de-versoes-de-po-
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_VERSIONS_INIT_SEQUENCE_V

## 📌 Visão Geral

View com a **sequencia inicial de versoes** de documentos de compras. Identifica a versao baseline.

> [!note] Sufixo _V
> O sufixo `_V` indica que este objeto e uma **view**, projetada para simplificar consultas.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Baseline:** Versao inicial de cada PO.
- **Auditoria:** Referencia para comparacao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | FK | Cabecalho | [[po_headers_all]] | 🟡 80% |
| 2 | INIT_VERSION_NUM | NUMBER | NULL | Identificacao | Versao inicial | — | 🟡 75% |
| 3 | INIT_CREATION_DATE | TIMESTAMP | NULL | Data | Data da versao inicial | — | 🟡 75% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (PO da sequência inicial de versões)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versao inicial
```sql
SELECT PO_HEADER_ID, INIT_VERSION_NUM, INIT_CREATION_DATE
FROM   PO_VERSIONS_INIT_SEQUENCE_V
WHERE  PO_HEADER_ID = :p_po_header_id;
```

---

## 🔒 Observações

- View derivada de `PO_VERSIONS`.
- Util para identificar a baseline.

---

## 🔗 PVOs Relacionados

### [[agreementheaderpvo|AgreementHeaderPVO]] (PO · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchaseOrderVersionAcceptedDate | — |
| APPROVED_DATE | PurchaseOrderVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchaseOrderVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchaseOrderVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchaseOrderVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchaseOrderVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchaseOrderVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchaseOrderVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchaseOrderVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchaseOrderVersionCoCanceledFlag | — |
| CO_NUM | PurchaseOrderVersionCoNum | — |
| CO_SEQUENCE | PurchaseOrderVersionCoSequence | — |
| COMMUNICATED_DATE | PurchaseOrderVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchaseOrderVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchaseOrderVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchaseOrderVersionCreatedByProgramName | — |
| CREATION_DATE | PurchaseOrderVersionCreationDate | — |
| DOCUMENT_DATE | PurchaseOrderVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchaseOrderVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchaseOrderVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchaseOrderVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchaseOrderVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchaseOrderVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchaseOrderVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchaseOrderVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchaseOrderVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchaseOrderVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchaseOrderVersionPoHeaderId | — |
| PROCESSED_DATE | PurchaseOrderVersionProcessedDate | — |
| PROGRAM_APP_NAME | PurchaseOrderVersionProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderVersionProgramName | — |
| REJECTED_FLAG | PurchaseOrderVersionRejectedFlag | — |
| REQUEST_DATE | PurchaseOrderVersionRequestDate | — |
| REQUEST_ID | PurchaseOrderVersionRequestId | — |
| REVISION_NUM | PurchaseOrderVersionRevisionNum | — |
| SUBMITTED_DATE | PurchaseOrderVersionSubmittedDate | — |
| VERSION_ID | PurchaseOrderVersionVersionId | — |
| WITHDRAWN_FLAG | PurchaseOrderVersionWithdrawnFlag | — |

### [[agreementlinepvo|AgreementLinePVO]] (PO · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | — |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | — |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | — |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[agreementpricebreakpvo|AgreementPriceBreakPVO]] (PO · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | — |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | — |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | — |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[maintenancewoprocurementpopvo|MaintenanceWOProcurementPOPVO]] (OTHER · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PrcDocumentVersionInitSeqPEOAcceptedDate | — |
| APPROVED_DATE | PrcDocumentVersionInitSeqPEOApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PrcDocumentVersionInitSeqPEOCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PrcDocumentVersionInitSeqPEOCancelDocFlag | — |
| CHANGE_ORDER_DESC | PrcDocumentVersionInitSeqPEOChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PrcDocumentVersionInitSeqPEOChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PrcDocumentVersionInitSeqPEOChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PrcDocumentVersionInitSeqPEOCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PrcDocumentVersionInitSeqPEOCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PrcDocumentVersionInitSeqPEOCoCanceledFlag | — |
| CO_NUM | PrcDocumentVersionInitSeqPEOCoNum | — |
| CO_SEQUENCE | PrcDocumentVersionInitSeqPEOCoSequence | — |
| COMMUNICATED_DATE | PrcDocumentVersionInitSeqPEOCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PrcDocumentVersionInitSeqPEOCommunicatedToSupplier | — |
| CREATED_BY | PrcDocumentVersionInitSeqPEOCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PrcDocumentVersionInitSeqPEOCreatedByProgramName | — |
| CREATION_DATE | PrcDocumentVersionInitSeqPEOCreationDate | — |
| DOCUMENT_DATE | PrcDocumentVersionInitSeqPEODocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PrcDocumentVersionInitSeqPEOExternalSystemFlag | — |
| FUNDS_STATUS | PrcDocumentVersionInitSeqPEOFundsStatus | — |
| JOB_DEFINITION_NAME | PrcDocumentVersionInitSeqPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PrcDocumentVersionInitSeqPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PrcDocumentVersionInitSeqPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrcDocumentVersionInitSeqPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PrcDocumentVersionInitSeqPEOLastUpdatedBy | — |
| MODIFIED_FLAG | PrcDocumentVersionInitSeqPEOModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PrcDocumentVersionInitSeqPEOObjectVersionNumber | — |
| ONLINE_REPORT_ID | PrcDocumentVersionInitSeqPEOOnlineReportId | — |
| ORIGINATOR_ID | PrcDocumentVersionInitSeqPEOOriginatorId | — |
| ORIGINATOR_ROLE | PrcDocumentVersionInitSeqPEOOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PrcDocumentVersionInitSeqPEOPendingResponseRole | — |
| PO_HEADER_ID | PrcDocumentVersionInitSeqPEOPoHeaderId | — |
| PROCESSED_DATE | PrcDocumentVersionInitSeqPEOProcessedDate | — |
| PROGRAM_APP_NAME | PrcDocumentVersionInitSeqPEOProgramAppName | — |
| PROGRAM_NAME | PrcDocumentVersionInitSeqPEOProgramName | — |
| REJECTED_FLAG | PrcDocumentVersionInitSeqPEORejectedFlag | — |
| REQUEST_DATE | PrcDocumentVersionInitSeqPEORequestDate | — |
| REQUEST_ID | PrcDocumentVersionInitSeqPEORequestId | — |
| REVISION_NUM | PrcDocumentVersionInitSeqPEORevisionNum | — |
| SUBMITTED_DATE | PrcDocumentVersionInitSeqPEOSubmittedDate | — |
| VERSION_ID | PrcDocumentVersionInitSeqPEOVersionId | — |
| WITHDRAWN_FLAG | PrcDocumentVersionInitSeqPEOWithdrawnFlag | — |

### [[maintenancewoprocurementreceiptpvo|MaintenanceWOProcurementReceiptPVO]] (OTHER · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PrcDocumentVersionInitSeqPEOAcceptedDate | — |
| APPROVED_DATE | PrcDocumentVersionInitSeqPEOApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PrcDocumentVersionInitSeqPEOCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PrcDocumentVersionInitSeqPEOCancelDocFlag | — |
| CHANGE_ORDER_DESC | PrcDocumentVersionInitSeqPEOChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PrcDocumentVersionInitSeqPEOChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PrcDocumentVersionInitSeqPEOChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PrcDocumentVersionInitSeqPEOCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PrcDocumentVersionInitSeqPEOCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PrcDocumentVersionInitSeqPEOCoCanceledFlag | — |
| CO_NUM | PrcDocumentVersionInitSeqPEOCoNum | — |
| CO_SEQUENCE | PrcDocumentVersionInitSeqPEOCoSequence | — |
| COMMUNICATED_DATE | PrcDocumentVersionInitSeqPEOCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PrcDocumentVersionInitSeqPEOCommunicatedToSupplier | — |
| CREATED_BY | PrcDocumentVersionInitSeqPEOCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PrcDocumentVersionInitSeqPEOCreatedByProgramName | — |
| CREATION_DATE | PrcDocumentVersionInitSeqPEOCreationDate | — |
| DOCUMENT_DATE | PrcDocumentVersionInitSeqPEODocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PrcDocumentVersionInitSeqPEOExternalSystemFlag | — |
| FUNDS_STATUS | PrcDocumentVersionInitSeqPEOFundsStatus | — |
| JOB_DEFINITION_NAME | PrcDocumentVersionInitSeqPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PrcDocumentVersionInitSeqPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PrcDocumentVersionInitSeqPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrcDocumentVersionInitSeqPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PrcDocumentVersionInitSeqPEOLastUpdatedBy | — |
| MODIFIED_FLAG | PrcDocumentVersionInitSeqPEOModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PrcDocumentVersionInitSeqPEOObjectVersionNumber | — |
| ONLINE_REPORT_ID | PrcDocumentVersionInitSeqPEOOnlineReportId | — |
| ORIGINATOR_ID | PrcDocumentVersionInitSeqPEOOriginatorId | — |
| ORIGINATOR_ROLE | PrcDocumentVersionInitSeqPEOOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PrcDocumentVersionInitSeqPEOPendingResponseRole | — |
| PO_HEADER_ID | PrcDocumentVersionInitSeqPEOPoHeaderId | — |
| PROCESSED_DATE | PrcDocumentVersionInitSeqPEOProcessedDate | — |
| PROGRAM_APP_NAME | PrcDocumentVersionInitSeqPEOProgramAppName | — |
| PROGRAM_NAME | PrcDocumentVersionInitSeqPEOProgramName | — |
| REJECTED_FLAG | PrcDocumentVersionInitSeqPEORejectedFlag | — |
| REQUEST_DATE | PrcDocumentVersionInitSeqPEORequestDate | — |
| REQUEST_ID | PrcDocumentVersionInitSeqPEORequestId | — |
| REVISION_NUM | PrcDocumentVersionInitSeqPEORevisionNum | — |
| SUBMITTED_DATE | PrcDocumentVersionInitSeqPEOSubmittedDate | — |
| VERSION_ID | PrcDocumentVersionInitSeqPEOVersionId | — |
| WITHDRAWN_FLAG | PrcDocumentVersionInitSeqPEOWithdrawnFlag | — |

### [[purchasingdocumentlinepvo|PurchasingDocumentLinePVO]] (PO · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | — |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | — |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | — |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[receivingreceiptp2ptransactionpvo|ReceivingReceiptP2PTransactionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PoVersionInitSequencePEOAcceptedDate | — |
| APPROVED_DATE | PoVersionInitSequencePEOApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PoVersionInitSequencePEOCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PoVersionInitSequencePEOCancelDocFlag | — |
| CHANGE_ORDER_DESC | PoVersionInitSequencePEOChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PoVersionInitSequencePEOChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PoVersionInitSequencePEOChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PoVersionInitSequencePEOCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PoVersionInitSequencePEOCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PoVersionInitSequencePEOCoCanceledFlag | — |
| CO_NUM | PoVersionInitSequencePEOCoNum | — |
| CO_SEQUENCE | PoVersionInitSequencePEOCoSequence | — |
| COMMUNICATED_DATE | PoVersionInitSequencePEOCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PoVersionInitSequencePEOCommunicatedToSupplier | — |
| CREATED_BY | PoVersionInitSequencePEOCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PoVersionInitSequencePEOCreatedByProgramName | — |
| CREATION_DATE | PoVersionInitSequencePEOCreationDate | — |
| DOCUMENT_DATE | PoVersionInitSequencePEODocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PoVersionInitSequencePEOExternalSystemFlag | — |
| FUNDS_STATUS | PoVersionInitSequencePEOFundsStatus | — |
| JOB_DEFINITION_NAME | PoVersionInitSequencePEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PoVersionInitSequencePEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PoVersionInitSequencePEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PoVersionInitSequencePEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PoVersionInitSequencePEOLastUpdatedBy | — |
| MODIFIED_FLAG | PoVersionInitSequencePEOModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PoVersionInitSequencePEOObjectVersionNumber | — |
| ONLINE_REPORT_ID | PoVersionInitSequencePEOOnlineReportId | — |
| ORIGINATOR_ID | PoVersionInitSequencePEOOriginatorId | — |
| ORIGINATOR_ROLE | PoVersionInitSequencePEOOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PoVersionInitSequencePEOPendingResponseRole | — |
| PO_HEADER_ID | PoVersionInitSequencePEOPoHeaderId | — |
| PROCESSED_DATE | PoVersionInitSequencePEOProcessedDate | — |
| PROGRAM_APP_NAME | PoVersionInitSequencePEOProgramAppName | — |
| PROGRAM_NAME | PoVersionInitSequencePEOProgramName | — |
| REJECTED_FLAG | PoVersionInitSequencePEORejectedFlag | — |
| REQUEST_DATE | PoVersionInitSequencePEORequestDate | — |
| REQUEST_ID | PoVersionInitSequencePEORequestId | — |
| REVISION_NUM | PoVersionInitSequencePEORevisionNum | — |
| SUBMITTED_DATE | PoVersionInitSequencePEOSubmittedDate | — |
| VERSION_ID | PoVersionInitSequencePEOVersionId | — |
| WITHDRAWN_FLAG | PoVersionInitSequencePEOWithdrawnFlag | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 5/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | ✅ |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | ✅ |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | ✅ |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | — |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 2/41)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | — |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 6/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | ✅ |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | ✅ |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | ✅ |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | ✅ |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO · BICC: 6/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | ✅ |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | ✅ |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | ✅ |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | ✅ |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[standardheaderpvo|StandardHeaderPVO]] (PO · BICC: 5/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchaseOrderVersionAcceptedDate | — |
| APPROVED_DATE | PurchaseOrderVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchaseOrderVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchaseOrderVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchaseOrderVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchaseOrderVersionChangeOrderStatus | ✅ |
| CHANGE_ORDER_TYPE | PurchaseOrderVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchaseOrderVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchaseOrderVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchaseOrderVersionCoCanceledFlag | — |
| CO_NUM | PurchaseOrderVersionCoNum | — |
| CO_SEQUENCE | PurchaseOrderVersionCoSequence | — |
| COMMUNICATED_DATE | PurchaseOrderVersionCommunicatedDate | ✅ |
| COMMUNICATED_TO_SUPPLIER | PurchaseOrderVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchaseOrderVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchaseOrderVersionCreatedByProgramName | — |
| CREATION_DATE | PurchaseOrderVersionCreationDate | — |
| DOCUMENT_DATE | PurchaseOrderVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchaseOrderVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchaseOrderVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchaseOrderVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchaseOrderVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchaseOrderVersionLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PurchaseOrderVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchaseOrderVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchaseOrderVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchaseOrderVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchaseOrderVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchaseOrderVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchaseOrderVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchaseOrderVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchaseOrderVersionPoHeaderId | — |
| PROCESSED_DATE | PurchaseOrderVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchaseOrderVersionProgramAppName | — |
| PROGRAM_NAME | PurchaseOrderVersionProgramName | — |
| REJECTED_FLAG | PurchaseOrderVersionRejectedFlag | — |
| REQUEST_DATE | PurchaseOrderVersionRequestDate | — |
| REQUEST_ID | PurchaseOrderVersionRequestId | — |
| REVISION_NUM | PurchaseOrderVersionRevisionNum | — |
| SUBMITTED_DATE | PurchaseOrderVersionSubmittedDate | ✅ |
| VERSION_ID | PurchaseOrderVersionVersionId | — |
| WITHDRAWN_FLAG | PurchaseOrderVersionWithdrawnFlag | — |

### [[standardlinepvo|StandardLinePVO]] (PO · BICC: 4/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | — |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | ✅ |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | ✅ |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | ✅ |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[standardshipmentpvo|StandardShipmentPVO]] (PO · BICC: 7/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PurchasingDocumentVersionAcceptedDate | ✅ |
| APPROVED_DATE | PurchasingDocumentVersionApprovedDate | ✅ |
| CANCEL_BACKING_REQ_FLAG | PurchasingDocumentVersionCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PurchasingDocumentVersionCancelDocFlag | — |
| CHANGE_ORDER_DESC | PurchasingDocumentVersionChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PurchasingDocumentVersionChangeOrderStatus | ✅ |
| CHANGE_ORDER_TYPE | PurchasingDocumentVersionChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PurchasingDocumentVersionCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PurchasingDocumentVersionCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PurchasingDocumentVersionCoCanceledFlag | — |
| CO_NUM | PurchasingDocumentVersionCoNum | — |
| CO_SEQUENCE | PurchasingDocumentVersionCoSequence | — |
| COMMUNICATED_DATE | PurchasingDocumentVersionCommunicatedDate | ✅ |
| COMMUNICATED_TO_SUPPLIER | PurchasingDocumentVersionCommunicatedToSupplier | — |
| CREATED_BY | PurchasingDocumentVersionCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PurchasingDocumentVersionCreatedByProgramName | — |
| CREATION_DATE | PurchasingDocumentVersionCreationDate | — |
| DOCUMENT_DATE | PurchasingDocumentVersionDocumentDate | ✅ |
| EXTERNAL_SYSTEM_FLAG | PurchasingDocumentVersionExternalSystemFlag | — |
| FUNDS_STATUS | PurchasingDocumentVersionFundsStatus | — |
| JOB_DEFINITION_NAME | PurchasingDocumentVersionJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PurchasingDocumentVersionJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PurchasingDocumentVersionLastUpdateDate | — |
| LAST_UPDATE_LOGIN | PurchasingDocumentVersionLastUpdateLogin | — |
| LAST_UPDATED_BY | PurchasingDocumentVersionLastUpdatedBy | — |
| MODIFIED_FLAG | PurchasingDocumentVersionModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PurchasingDocumentVersionObjectVersionNumber | — |
| ONLINE_REPORT_ID | PurchasingDocumentVersionOnlineReportId | — |
| ORIGINATOR_ID | PurchasingDocumentVersionOriginatorId | — |
| ORIGINATOR_ROLE | PurchasingDocumentVersionOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PurchasingDocumentVersionPendingResponseRole | — |
| PO_HEADER_ID | PurchasingDocumentVersionPoHeaderId | — |
| PROCESSED_DATE | PurchasingDocumentVersionProcessedDate | ✅ |
| PROGRAM_APP_NAME | PurchasingDocumentVersionProgramAppName | — |
| PROGRAM_NAME | PurchasingDocumentVersionProgramName | — |
| REJECTED_FLAG | PurchasingDocumentVersionRejectedFlag | — |
| REQUEST_DATE | PurchasingDocumentVersionRequestDate | — |
| REQUEST_ID | PurchasingDocumentVersionRequestId | — |
| REVISION_NUM | PurchasingDocumentVersionRevisionNum | — |
| SUBMITTED_DATE | PurchasingDocumentVersionSubmittedDate | ✅ |
| VERSION_ID | PurchasingDocumentVersionVersionId | — |
| WITHDRAWN_FLAG | PurchasingDocumentVersionWithdrawnFlag | — |

### [[woprocurementpopvo|WOProcurementPOPVO]] (OTHER · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PrcDocumentVersionInitSeqPEOAcceptedDate | — |
| APPROVED_DATE | PrcDocumentVersionInitSeqPEOApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PrcDocumentVersionInitSeqPEOCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PrcDocumentVersionInitSeqPEOCancelDocFlag | — |
| CHANGE_ORDER_DESC | PrcDocumentVersionInitSeqPEOChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PrcDocumentVersionInitSeqPEOChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PrcDocumentVersionInitSeqPEOChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PrcDocumentVersionInitSeqPEOCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PrcDocumentVersionInitSeqPEOCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PrcDocumentVersionInitSeqPEOCoCanceledFlag | — |
| CO_NUM | PrcDocumentVersionInitSeqPEOCoNum | — |
| CO_SEQUENCE | PrcDocumentVersionInitSeqPEOCoSequence | — |
| COMMUNICATED_DATE | PrcDocumentVersionInitSeqPEOCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PrcDocumentVersionInitSeqPEOCommunicatedToSupplier | — |
| CREATED_BY | PrcDocumentVersionInitSeqPEOCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PrcDocumentVersionInitSeqPEOCreatedByProgramName | — |
| CREATION_DATE | PrcDocumentVersionInitSeqPEOCreationDate | — |
| DOCUMENT_DATE | PrcDocumentVersionInitSeqPEODocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PrcDocumentVersionInitSeqPEOExternalSystemFlag | — |
| FUNDS_STATUS | PrcDocumentVersionInitSeqPEOFundsStatus | — |
| JOB_DEFINITION_NAME | PrcDocumentVersionInitSeqPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PrcDocumentVersionInitSeqPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PrcDocumentVersionInitSeqPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrcDocumentVersionInitSeqPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PrcDocumentVersionInitSeqPEOLastUpdatedBy | — |
| MODIFIED_FLAG | PrcDocumentVersionInitSeqPEOModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PrcDocumentVersionInitSeqPEOObjectVersionNumber | — |
| ONLINE_REPORT_ID | PrcDocumentVersionInitSeqPEOOnlineReportId | — |
| ORIGINATOR_ID | PrcDocumentVersionInitSeqPEOOriginatorId | — |
| ORIGINATOR_ROLE | PrcDocumentVersionInitSeqPEOOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PrcDocumentVersionInitSeqPEOPendingResponseRole | — |
| PO_HEADER_ID | PrcDocumentVersionInitSeqPEOPoHeaderId | — |
| PROCESSED_DATE | PrcDocumentVersionInitSeqPEOProcessedDate | — |
| PROGRAM_APP_NAME | PrcDocumentVersionInitSeqPEOProgramAppName | — |
| PROGRAM_NAME | PrcDocumentVersionInitSeqPEOProgramName | — |
| REJECTED_FLAG | PrcDocumentVersionInitSeqPEORejectedFlag | — |
| REQUEST_DATE | PrcDocumentVersionInitSeqPEORequestDate | — |
| REQUEST_ID | PrcDocumentVersionInitSeqPEORequestId | — |
| REVISION_NUM | PrcDocumentVersionInitSeqPEORevisionNum | — |
| SUBMITTED_DATE | PrcDocumentVersionInitSeqPEOSubmittedDate | — |
| VERSION_ID | PrcDocumentVersionInitSeqPEOVersionId | — |
| WITHDRAWN_FLAG | PrcDocumentVersionInitSeqPEOWithdrawnFlag | — |

### [[woprocurementreceiptpvo|WOProcurementReceiptPVO]] (OTHER · BICC: 1/42)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTED_DATE | PrcDocumentVersionInitSeqPEOAcceptedDate | — |
| APPROVED_DATE | PrcDocumentVersionInitSeqPEOApprovedDate | — |
| CANCEL_BACKING_REQ_FLAG | PrcDocumentVersionInitSeqPEOCancelBackingReqFlag | — |
| CANCEL_DOC_FLAG | PrcDocumentVersionInitSeqPEOCancelDocFlag | — |
| CHANGE_ORDER_DESC | PrcDocumentVersionInitSeqPEOChangeOrderDesc | — |
| CHANGE_ORDER_STATUS | PrcDocumentVersionInitSeqPEOChangeOrderStatus | — |
| CHANGE_ORDER_TYPE | PrcDocumentVersionInitSeqPEOChangeOrderType | — |
| CO_CANCELED_BY_ROLE | PrcDocumentVersionInitSeqPEOCoCanceledByRole | — |
| CO_CANCELED_BY_USER_ID | PrcDocumentVersionInitSeqPEOCoCanceledByUserId | — |
| CO_CANCELED_FLAG | PrcDocumentVersionInitSeqPEOCoCanceledFlag | — |
| CO_NUM | PrcDocumentVersionInitSeqPEOCoNum | — |
| CO_SEQUENCE | PrcDocumentVersionInitSeqPEOCoSequence | — |
| COMMUNICATED_DATE | PrcDocumentVersionInitSeqPEOCommunicatedDate | — |
| COMMUNICATED_TO_SUPPLIER | PrcDocumentVersionInitSeqPEOCommunicatedToSupplier | — |
| CREATED_BY | PrcDocumentVersionInitSeqPEOCreatedBy | — |
| CREATED_BY_PROGRAM_NAME | PrcDocumentVersionInitSeqPEOCreatedByProgramName | — |
| CREATION_DATE | PrcDocumentVersionInitSeqPEOCreationDate | — |
| DOCUMENT_DATE | PrcDocumentVersionInitSeqPEODocumentDate | — |
| EXTERNAL_SYSTEM_FLAG | PrcDocumentVersionInitSeqPEOExternalSystemFlag | — |
| FUNDS_STATUS | PrcDocumentVersionInitSeqPEOFundsStatus | — |
| JOB_DEFINITION_NAME | PrcDocumentVersionInitSeqPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | PrcDocumentVersionInitSeqPEOJobDefinitionPackage | — |
| LAST_UPDATE_DATE | PrcDocumentVersionInitSeqPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PrcDocumentVersionInitSeqPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | PrcDocumentVersionInitSeqPEOLastUpdatedBy | — |
| MODIFIED_FLAG | PrcDocumentVersionInitSeqPEOModifiedFlag | — |
| OBJECT_VERSION_NUMBER | PrcDocumentVersionInitSeqPEOObjectVersionNumber | — |
| ONLINE_REPORT_ID | PrcDocumentVersionInitSeqPEOOnlineReportId | — |
| ORIGINATOR_ID | PrcDocumentVersionInitSeqPEOOriginatorId | — |
| ORIGINATOR_ROLE | PrcDocumentVersionInitSeqPEOOriginatorRole | — |
| PENDING_RESPONSE_ROLE | PrcDocumentVersionInitSeqPEOPendingResponseRole | — |
| PO_HEADER_ID | PrcDocumentVersionInitSeqPEOPoHeaderId | — |
| PROCESSED_DATE | PrcDocumentVersionInitSeqPEOProcessedDate | — |
| PROGRAM_APP_NAME | PrcDocumentVersionInitSeqPEOProgramAppName | — |
| PROGRAM_NAME | PrcDocumentVersionInitSeqPEOProgramName | — |
| REJECTED_FLAG | PrcDocumentVersionInitSeqPEORejectedFlag | — |
| REQUEST_DATE | PrcDocumentVersionInitSeqPEORequestDate | — |
| REQUEST_ID | PrcDocumentVersionInitSeqPEORequestId | — |
| REVISION_NUM | PrcDocumentVersionInitSeqPEORevisionNum | — |
| SUBMITTED_DATE | PrcDocumentVersionInitSeqPEOSubmittedDate | — |
| VERSION_ID | PrcDocumentVersionInitSeqPEOVersionId | — |
| WITHDRAWN_FLAG | PrcDocumentVersionInitSeqPEOWithdrawnFlag | — |

---

## 📚 Referências

- [Oracle Docs — PO_VERSIONS_INIT_SEQUENCE_V](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
