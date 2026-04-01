---
id: DOC-PO-130
doc_type: system-doc
title: "PO_HEADERS_ARCHIVE_ALL — Arquivo de Cabecalhos de PO (Versionamento)"
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
  - purchase-orders
  - po-transactions
  - compras
aliases:
  - PO_HEADERS_ARCHIVE_ALL
  - po_headers_archive_all
  - po-headers-archive-all
  - po-headers
  - arquivo-de-cabecalhos-de-po-(versio
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# PO_HEADERS_ARCHIVE_ALL

## 📌 Visão Geral

Armazena **versoes arquivadas dos cabecalhos de PO**. Cada revisao gera copia do cabecalho anterior para rastreabilidade.

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `ORG_ID` e necessario para consultas por organizacao especifica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Versionamento:** Historico de alteracoes de cabecalho.
- **Auditoria:** Comparacao entre versoes.
- **Compliance:** Evidencia de alteracoes.
- **Rollback:** Referencia para reversao.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descricao | FK | Confianca |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | PO_HEADER_ID | NUMBER(18) | NOT NULL | PK | ID do cabecalho | [[po_headers_all]] | 🟢 100% |
| 2 | REVISION_NUM | NUMBER | NOT NULL | PK | Revisao arquivada | — | 🟢 100% |
| 3 | SEGMENT1 | VARCHAR2(20) | NOT NULL | Identificacao | Numero do PO | — | 🟢 100% |
| 4 | VENDOR_ID | NUMBER(18) | NULL | FK | Fornecedor | [[poz_suppliers]] | 🟢 100% |
| 5 | AUTHORIZATION_STATUS | VARCHAR2(25) | NULL | Status | Status na revisao | — | 🟢 100% |
| 6 | APPROVED_DATE | DATE | NULL | Data | Data de aprovacao | — | 🟢 95% |
| 7 | ORG_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit | [[hr_all_organization_units_f]] | 🟢 100% |
| 8 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuario criador | — | 🟢 100% |
| 9 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data de criacao | — | 🟢 100% |
| 10 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Ultimo alterador | — | 🟢 100% |
| 11 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Ultima alteracao | — | 🟢 100% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[po_headers_all]] — via `PO_HEADER_ID` (pedido de compra original do registro arquivado)
- [[poz_suppliers]] — via `VENDOR_ID` (fornecedor do PO na versão arquivada)

### Tabelas-filha (FK de saída)
- Nenhuma FK de saida identificada

---

## 📎 Uso Típico

### Versoes de um PO
```sql
SELECT REVISION_NUM, AUTHORIZATION_STATUS, APPROVED_DATE
FROM   PO_HEADERS_ARCHIVE_ALL
WHERE  PO_HEADER_ID = :p_po_header_id
ORDER BY REVISION_NUM;
```

---

## 🔒 Observações

- PK composta: `PO_HEADER_ID` + `REVISION_NUM`.
- Estrutura espelha `PO_HEADERS_ALL`.
- Cada revisao gera novo registro.

---

## 🔗 PVOs Relacionados

### [[purchasingdocumentversionpvo|PurchasingDocumentVersionPVO]] (PO · BICC: 16/108)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACCEPTANCE_DUE_DATE | ArchivedPOHeaderAcceptanceDueDate | — |
| ACCEPTANCE_REQUIRED_FLAG | ArchivedPOHeaderAcceptanceRequiredFlag | — |
| AGENT_ID | ArchivedPOHeaderAgentId | — |
| AGING_ONSET_POINT | ArchivedPOHeaderAgingOnsetPoint | ✅ |
| AGING_PERIOD_DAYS | ArchivedPOHeaderAgingPeriodDays | ✅ |
| AMOUNT_LIMIT | ArchivedPOHeaderAmountLimit | — |
| AUTO_SOURCING_FLAG | ArchivedPOHeaderAutoSourcingFlag | — |
| BILL_TO_LOCATION_ID | ArchivedPOHeaderBillToLocationId | — |
| BILLING_CYCLE_CLOSING_DATE | ArchivedPOHeaderBillingCycleClosingDate | ✅ |
| BILLTO_BU_ID | ArchivedPOHeaderBilltoBuId | ✅ |
| BLANKET_TOTAL_AMOUNT | ArchivedPOHeaderBlanketTotalAmount | — |
| BUYER_MANAGED_TRANSPORT_FLAG | ArchivedPOHeaderBuyerManagedTransportFlag | — |
| CANCEL_FLAG | ArchivedPOHeaderCancelFlag | — |
| CARRIER_ID | ArchivedPOHeaderCarrierId | — |
| CBC_ACCOUNTING_DATE | ArchivedPOHeaderCbcAccountingDate | — |
| CHANGE_REQUESTED_BY | ArchivedPOHeaderChangeRequestedBy | — |
| CHANGE_SUMMARY | ArchivedPOHeaderChangeSummary | — |
| COMMENTS | ArchivedPOHeaderComments | ✅ |
| CONFIRMING_ORDER_FLAG | ArchivedPOHeaderConfirmingOrderFlag | — |
| CONSIGNED_CONSUMPTION_FLAG | ArchivedPOHeaderConsignedConsumptionFlag | — |
| CONSUME_REQ_DEMAND_FLAG | ArchivedPOHeaderConsumeReqDemandFlag | — |
| CONSUMPTION_ADVICE_FREQUENCY | ArchivedPOHeaderConsumptionAdviceFrequency | ✅ |
| CONSUMPTION_ADVICE_SUMMARY | ArchivedPOHeaderConsumptionAdviceSummary | ✅ |
| CONTERMS_ARTICLES_UPD_DATE | ArchivedPOHeaderContermsArticlesUpdDate | — |
| CONTERMS_DELIV_UPD_DATE | ArchivedPOHeaderContermsDelivUpdDate | — |
| CONTERMS_EXIST_FLAG | ArchivedPOHeaderContermsExistFlag | — |
| CPA_REFERENCE | ArchivedPOHeaderCpaReference | — |
| CREATED_BY | ArchivedPOHeaderCreatedBy | — |
| CREATED_LANGUAGE | ArchivedPOHeaderCreatedLanguage | — |
| CREATION_DATE | ArchivedPOHeaderCreationDate | — |
| CURRENCY_CODE | ArchivedPOHeaderCurrencyCode | — |
| DEFAULT_CONSIGNMENT_LINE_FLAG | ArchivedPOHeaderDefaultConsignmentLineFlag | ✅ |
| DEFAULT_TAXATION_COUNTRY | ArchivedPOHeaderDefaultTaxationCountry | — |
| DOCUMENT_CREATION_METHOD | ArchivedPOHeaderDocumentCreationMethod | — |
| EMAIL_ADDRESS | ArchivedPOHeaderEmailAddress | — |
| ENABLED_FLAG | ArchivedPOHeaderEnabledFlag | — |
| ENCUMBRANCE_REQUIRED_FLAG | ArchivedPOHeaderEncumbranceRequiredFlag | — |
| END_DATE | ArchivedPOHeaderEndDate | — |
| ENTITY_CO_DISPOSITION | ArchivedPOHeaderEntityCoDisposition | — |
| FAX | ArchivedPOHeaderFax | — |
| FIRM_DATE | ArchivedPOHeaderFirmDate | — |
| FIRM_STATUS_LOOKUP_CODE | ArchivedPOHeaderFirmStatusLookupCode | — |
| FOB_LOOKUP_CODE | ArchivedPOHeaderFobLookupCode | — |
| FREIGHT_TERMS_LOOKUP_CODE | ArchivedPOHeaderFreightTermsLookupCode | — |
| FROM_CO_SEQ | ArchivedPOHeaderFromCoSeq | ✅ |
| FROM_HEADER_ID | ArchivedPOHeaderFromHeaderId | — |
| FROM_TYPE_LOOKUP_CODE | ArchivedPOHeaderFromTypeLookupCode | — |
| GENERATE_ORDERS_AUTOMATIC | ArchivedPOHeaderGenerateOrdersAutomatic | — |
| GOVERNMENT_CONTEXT | ArchivedPOHeaderGovernmentContext | — |
| GROUP_REQUISITION_LINES | ArchivedPOHeaderGroupRequisitionLines | — |
| GROUP_REQUISITIONS | ArchivedPOHeaderGroupRequisitions | — |
| INTERFACE_SOURCE_CODE | ArchivedPOHeaderInterfaceSourceCode | — |
| JOB_DEFINITION_NAME | ArchivedPOHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | ArchivedPOHeaderJobDefinitionPackage | — |
| LAST_UPDATE_DATE | ArchivedPOHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | ArchivedPOHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | ArchivedPOHeaderLastUpdatedBy | — |
| MIN_RELEASE_AMOUNT | ArchivedPOHeaderMinReleaseAmount | — |
| MODE_OF_TRANSPORT | ArchivedPOHeaderModeOfTransport | ✅ |
| NOTE_TO_AUTHORIZER | ArchivedPOHeaderNoteToAuthorizer | — |
| NOTE_TO_RECEIVER | ArchivedPOHeaderNoteToReceiver | — |
| NOTE_TO_VENDOR | ArchivedPOHeaderNoteToVendor | — |
| OBJECT_VERSION_NUMBER | ArchivedPOHeaderObjectVersionNumber | — |
| ORCHESTRATION_ORDER_FLAG | ArchivedPOHeaderOrchestrationOrderFlag | ✅ |
| PAY_ON_CODE | ArchivedPOHeaderPayOnCode | — |
| PAY_ON_USE_FLAG | ArchivedPOHeaderPayOnUseFlag | ✅ |
| PCARD_ID | ArchivedPOHeaderPcardId | — |
| PENDING_SIGNATURE_FLAG | ArchivedPOHeaderPendingSignatureFlag | — |
| PO_HEADER_ID | ArchivedPOHeaderPoHeaderId | ✅ |
| PRC_BU_ID | ArchivedPOHeaderPrcBuId | — |
| PRICE_UPDATE_TOLERANCE | ArchivedPOHeaderPriceUpdateTolerance | — |
| PROGRAM_APP_NAME | ArchivedPOHeaderProgramAppName | — |
| PROGRAM_NAME | ArchivedPOHeaderProgramName | — |
| RATE | ArchivedPOHeaderRate | — |
| RATE_DATE | ArchivedPOHeaderRateDate | — |
| RATE_TYPE | ArchivedPOHeaderRateType | — |
| REFERENCE_NUM | ArchivedPOHeaderReferenceNum | — |
| REQ_BU_ID | ArchivedPOHeaderReqBuId | — |
| REQUEST_ID | ArchivedPOHeaderRequestId | — |
| RETRO_PRICE_APPLY_UPDATES_FLAG | ArchivedPOHeaderRetroPriceApplyUpdatesFlag | — |
| RETRO_PRICE_COMM_UPDATES_FLAG | ArchivedPOHeaderRetroPriceCommUpdatesFlag | — |
| SEGMENT1 | ArchivedPOHeaderSegment1 | — |
| SEGMENT2 | ArchivedPOHeaderSegment2 | — |
| SEGMENT3 | ArchivedPOHeaderSegment3 | — |
| SEGMENT4 | ArchivedPOHeaderSegment4 | — |
| SEGMENT5 | ArchivedPOHeaderSegment5 | — |
| SERVICE_LEVEL | ArchivedPOHeaderServiceLevel | ✅ |
| SHIP_TO_LOCATION_ID | ArchivedPOHeaderShipToLocationId | — |
| SHIPPING_CONTROL | ArchivedPOHeaderShippingControl | — |
| SOLDTO_LE_ID | ArchivedPOHeaderSoldtoLeId | ✅ |
| START_DATE | ArchivedPOHeaderStartDate | — |
| STYLE_ID | ArchivedPOHeaderStyleId | — |
| SUBMIT_APPROVAL_AUTOMATIC | ArchivedPOHeaderSubmitApprovalAutomatic | — |
| SUBMIT_DATE | ArchivedPOHeaderSubmitDate | — |
| SUMMARY_FLAG | ArchivedPOHeaderSummaryFlag | — |
| SUPPLIER_NOTIF_METHOD | ArchivedPOHeaderSupplierNotifMethod | — |
| TAX_DOCUMENT_SUBTYPE | ArchivedPOHeaderTaxDocumentSubtype | — |
| TERMS_ID | ArchivedPOHeaderTermsId | — |
| TO_CO_SEQ | ArchivedPOHeaderToCoSeq | — |
| TYPE_LOOKUP_CODE | ArchivedPOHeaderTypeLookupCode | — |
| UPDATE_SOURCING_RULES_FLAG | ArchivedPOHeaderUpdateSourcingRulesFlag | — |
| USE_NEED_BY_DATE | ArchivedPOHeaderUseNeedByDate | — |
| USE_SHIP_TO | ArchivedPOHeaderUseShipTo | — |
| VENDOR_CONTACT_ID | ArchivedPOHeaderVendorContactId | — |
| VENDOR_ID | ArchivedPOHeaderVendorId | — |
| VENDOR_ORDER_NUM | ArchivedPOHeaderVendorOrderNum | — |
| VENDOR_SITE_ID | ArchivedPOHeaderVendorSiteId | — |
| XML_FLAG | ArchivedPOHeaderXmlFlag | — |

---

## 📚 Referências

- [Oracle Docs — PO_HEADERS_ARCHIVE_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/)
- [[po-module-data-dictionary]] — Dossiê do módulo PO/Procurement
