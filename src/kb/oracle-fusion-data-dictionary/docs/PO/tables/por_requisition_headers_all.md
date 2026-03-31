---
id: DOC-PO-065
doc_type: system-doc
title: "POR_REQUISITION_HEADERS_ALL — Cabeçalhos de Requisições de Compra"
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
  - requisicoes
  - cabecalho
  - purchase-requisition
aliases:
  - POR_REQUISITION_HEADERS_ALL
  - por_requisition_headers_all
  - cabecalho-requisicoes
  - requisicao-compra-header
source_format: markdown
conversion_pipeline: manual-v1
conversion_quality: 100
qa_score: 0
qa_date: 2026-03-25
qa_status: not_reviewed
created_at: 2026-03-25
updated_at: 2026-03-25
---

# POR_REQUISITION_HEADERS_ALL

## 📌 Visão Geral

Armazena os **cabeçalhos de requisições de compra** do módulo Procurement. Cada registro representa uma requisição de compra com informações de identificação, solicitante, status de aprovação, tipo e datas. É a tabela-mãe das linhas de requisição (`POR_REQUISITION_LINES_ALL`) e das distribuições (`POR_REQ_DISTRIBUTIONS_ALL`).

> [!note] Sufixo _ALL
> O sufixo `_ALL` indica que a tabela armazena dados de **todas as business units** (multi-org). O filtro por `REQ_BU_ID` é necessário para consultas por organização específica.

---

## 🧠 Propósito de Negócio

Esta tabela é utilizada nos seguintes processos:

- **Criação de requisições:** Registro do pedido de compra pelo requisitante (self-service ou profissional).
- **Workflow de aprovação:** Controle do ciclo de aprovação da requisição (draft → submitted → approved → ordered).
- **Conversão para PO:** Base para criação automática ou manual de Purchase Orders.
- **Acompanhamento:** Rastreamento do ciclo de vida da requisição até o atendimento completo.
- **Relatórios gerenciais:** Análises de volume, valor e tempo de ciclo de requisições.
- **Auditoria:** Registro completo de quem requisitou, quando e por que.

---

## ⚙️ Colunas Principais

> [!tip] Confiança
> Escala de 0% a 100% — grau de certeza da descrição gerada por IA com base na documentação oficial Oracle (OEDMF/BICC Release 13/25A).
> - 🟢 **81–100%** — Coluna presente na documentação oficial Oracle; nome, tipo e descrição confirmados.
> - 🟡 **51–80%** — Coluna inferida por naming convention ou padrão Oracle; tipo exato pode variar.
> - 🔴 **0–50%** — Existência ou tipo incertos; pode não existir no release atual; validar no ambiente.

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | REQUISITION_HEADER_ID | NUMBER(18) | NOT NULL | PK | Identificador único do cabeçalho da requisição | — | 🟢 100% |
| 2 | REQUISITION_NUMBER | VARCHAR2(20) | NOT NULL | Identificação | Número visível da requisição | — | 🟢 100% |
| 3 | DESCRIPTION | VARCHAR2(240) | NULL | Descrição | Descrição/justificativa da requisição | — | 🟢 95% |
| 4 | AUTHORIZATION_STATUS | VARCHAR2(25) | NOT NULL | Status | Status de aprovação: INCOMPLETE, IN PROCESS, PRE-APPROVED, APPROVED, REJECTED, CANCELLED, WITHDRAWN | — | 🟢 100% |
| 5 | TYPE_LOOKUP_CODE | VARCHAR2(25) | NOT NULL | Classificação | Tipo da requisição: PURCHASE, INTERNAL | — | 🟢 95% |
| 6 | PREPARER_ID | NUMBER(18) | NOT NULL | FK | Preparador da requisição (pessoa que digitou) | [[per_all_people_f]] | 🟢 95% |
| 7 | REQUISITION_DATE | DATE | NOT NULL | Data | Data da requisição | — | 🟢 100% |
| 8 | REQ_BU_ID | NUMBER(18) | NOT NULL | Multi-Org | Business unit da requisição | [[hr_all_organization_units_f]] | 🟢 95% |
| 9 | FUNDS_STATUS | VARCHAR2(25) | NULL | Controle | Status de reserva de fundos (budgetary control) | — | 🟡 80% |
| 10 | DOCUMENT_STATUS | VARCHAR2(25) | NULL | Status | Status do documento no ciclo de vida | — | 🟢 90% |
| 11 | EMERGENCY_PO_NUM | VARCHAR2(20) | NULL | Referência | Número da PO de emergência associada | — | 🟡 75% |
| 12 | INTERFACE_SOURCE_CODE | VARCHAR2(25) | NULL | Integração | Código da origem (se criada via interface) | — | 🟢 90% |
| 13 | APPROVED_DATE | DATE | NULL | Data | Data de aprovação final | — | 🟡 80% |
| 14 | DOC_SEQUENCE_VALUE | NUMBER(15) | NULL | Identificação | Número de sequência de documento legal | — | 🟢 90% |
| 15 | CREATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Usuário que criou o registro | — | 🟢 95% |
| 16 | CREATION_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora de criação | — | 🟢 95% |
| 17 | LAST_UPDATED_BY | VARCHAR2(64) | NOT NULL | Auditoria | Último usuário que alterou | — | 🟢 95% |
| 18 | LAST_UPDATE_DATE | TIMESTAMP | NOT NULL | Auditoria | Data/hora da última alteração | — | 🟢 95% |
| 19 | LAST_UPDATE_LOGIN | VARCHAR2(32) | NULL | Auditoria | Login da última sessão | — | 🟢 95% |
| 20 | ATTRIBUTE1–15 | VARCHAR2(150) | NULL | DFF | Atributos descritivos customizáveis por implementação | — | 🟢 90% |
| 21 | ATTRIBUTE_CATEGORY | VARCHAR2(30) | NULL | DFF | Contexto do Descriptive Flexfield | — | 🟢 90% |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)
- [[per_all_people_f]] — via `PREPARER_ID` (preparador da requisição)
- [[hr_all_organization_units_f]] — via `REQ_BU_ID` (business unit da requisição de compra)

### Tabelas-filha (FK de saída)
- [[por_requisition_lines_all]] — via `REQUISITION_HEADER_ID` (linhas da requisição)
- [[por_req_distributions_all]] — via `REQUISITION_HEADER_ID` (distribuições contábeis, indiretamente via linhas)
- [[por_line_locations_sum_v]] — via `REQUISITION_HEADER_ID` (locais de entrega sumarizados)

---

## 📎 Uso Típico

### Requisições aprovadas por período
```sql
SELECT rh.REQUISITION_NUMBER,
       rh.DESCRIPTION,
       rh.REQUISITION_DATE,
       rh.AUTHORIZATION_STATUS,
       rh.APPROVED_DATE
FROM   POR_REQUISITION_HEADERS_ALL rh
WHERE  rh.AUTHORIZATION_STATUS = 'APPROVED'
  AND  rh.REQUISITION_DATE BETWEEN :start_date AND :end_date
  AND  rh.REQ_BU_ID = :p_bu_id;
```

### Contagem de requisições por status
```sql
SELECT rh.AUTHORIZATION_STATUS,
       COUNT(*) AS qtd
FROM   POR_REQUISITION_HEADERS_ALL rh
WHERE  rh.REQ_BU_ID = :p_bu_id
GROUP BY rh.AUTHORIZATION_STATUS;
```

### Filtros comuns
- `AUTHORIZATION_STATUS = 'APPROVED'` — Requisições aprovadas
- `AUTHORIZATION_STATUS = 'IN PROCESS'` — Em processo de aprovação
- `TYPE_LOOKUP_CODE = 'PURCHASE'` — Requisições de compra (não internas)

---

## 🔒 Observações

- O `AUTHORIZATION_STATUS` controla todo o ciclo de vida: **INCOMPLETE** → **IN PROCESS** → **PRE-APPROVED** → **APPROVED** → (convertida em PO).
- `TYPE_LOOKUP_CODE = 'PURCHASE'` são requisições externas; `INTERNAL` são transferências entre organizações.
- O campo `PREPARER_ID` referencia quem digitou a requisição, que pode ser diferente do requisitante (requester) nas linhas.
- Requisições canceladas mantêm `AUTHORIZATION_STATUS = 'CANCELLED'` para histórico.
- O `FUNDS_STATUS` é populado apenas quando budgetary control está habilitado na business unit.

---

## 🔗 PVOs Relacionados

### [[inventorysupplypvo|InventorySupplyPVO]] (OTHER · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | — |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEORequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId1 | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[maintenancewooperationspvo|MaintenanceWOOperationsPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |

### [[maintenancewoprocurementpopvo|MaintenanceWOProcurementPOPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[maintenancewoprocurementreceiptpvo|MaintenanceWOProcurementReceiptPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[maintenancewoprocurementreqpvo|MaintenanceWOProcurementReqPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[purchaseorderhistorypvo|PurchaseOrderHistoryPVO]] (PO · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | — |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | — |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | — |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | — |

### [[receiptaccountingpvo|ReceiptAccountingPVO]] (AR · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |

### [[receiptaccountingtxnp1|ReceiptAccountingTxnP1]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate1 | — |
| ATTRIBUTE1 | RequisitionHeaderPEOAttribute160 | — |
| ATTRIBUTE10 | RequisitionHeaderPEOAttribute1012 | — |
| ATTRIBUTE11 | RequisitionHeaderPEOAttribute1116 | — |
| ATTRIBUTE12 | RequisitionHeaderPEOAttribute1214 | — |
| ATTRIBUTE13 | RequisitionHeaderPEOAttribute1312 | — |
| ATTRIBUTE14 | RequisitionHeaderPEOAttribute1412 | — |
| ATTRIBUTE15 | RequisitionHeaderPEOAttribute1512 | — |
| ATTRIBUTE16 | RequisitionHeaderPEOAttribute169 | — |
| ATTRIBUTE17 | RequisitionHeaderPEOAttribute179 | — |
| ATTRIBUTE18 | RequisitionHeaderPEOAttribute189 | — |
| ATTRIBUTE19 | RequisitionHeaderPEOAttribute199 | — |
| ATTRIBUTE2 | RequisitionHeaderPEOAttribute214 | — |
| ATTRIBUTE20 | RequisitionHeaderPEOAttribute209 | — |
| ATTRIBUTE3 | RequisitionHeaderPEOAttribute313 | — |
| ATTRIBUTE4 | RequisitionHeaderPEOAttribute413 | — |
| ATTRIBUTE5 | RequisitionHeaderPEOAttribute512 | — |
| ATTRIBUTE6 | RequisitionHeaderPEOAttribute612 | — |
| ATTRIBUTE7 | RequisitionHeaderPEOAttribute712 | — |
| ATTRIBUTE8 | RequisitionHeaderPEOAttribute812 | — |
| ATTRIBUTE9 | RequisitionHeaderPEOAttribute912 | — |
| ATTRIBUTE_CATEGORY | RequisitionHeaderPEOAttributeCategory12 | — |
| ATTRIBUTE_DATE1 | RequisitionHeaderPEOAttributeDate114 | — |
| ATTRIBUTE_DATE10 | RequisitionHeaderPEOAttributeDate106 | — |
| ATTRIBUTE_DATE2 | RequisitionHeaderPEOAttributeDate212 | — |
| ATTRIBUTE_DATE3 | RequisitionHeaderPEOAttributeDate312 | — |
| ATTRIBUTE_DATE4 | RequisitionHeaderPEOAttributeDate412 | — |
| ATTRIBUTE_DATE5 | RequisitionHeaderPEOAttributeDate512 | — |
| ATTRIBUTE_DATE6 | RequisitionHeaderPEOAttributeDate66 | — |
| ATTRIBUTE_DATE7 | RequisitionHeaderPEOAttributeDate76 | — |
| ATTRIBUTE_DATE8 | RequisitionHeaderPEOAttributeDate86 | — |
| ATTRIBUTE_DATE9 | RequisitionHeaderPEOAttributeDate96 | — |
| ATTRIBUTE_NUMBER1 | RequisitionHeaderPEOAttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | RequisitionHeaderPEOAttributeNumber109 | — |
| ATTRIBUTE_NUMBER2 | RequisitionHeaderPEOAttributeNumber212 | — |
| ATTRIBUTE_NUMBER3 | RequisitionHeaderPEOAttributeNumber312 | — |
| ATTRIBUTE_NUMBER4 | RequisitionHeaderPEOAttributeNumber412 | — |
| ATTRIBUTE_NUMBER5 | RequisitionHeaderPEOAttributeNumber512 | — |
| ATTRIBUTE_NUMBER6 | RequisitionHeaderPEOAttributeNumber69 | — |
| ATTRIBUTE_NUMBER7 | RequisitionHeaderPEOAttributeNumber79 | — |
| ATTRIBUTE_NUMBER8 | RequisitionHeaderPEOAttributeNumber89 | — |
| ATTRIBUTE_NUMBER9 | RequisitionHeaderPEOAttributeNumber99 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionHeaderPEOAttributeTimestamp17 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionHeaderPEOAttributeTimestamp104 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionHeaderPEOAttributeTimestamp27 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionHeaderPEOAttributeTimestamp37 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionHeaderPEOAttributeTimestamp47 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionHeaderPEOAttributeTimestamp57 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionHeaderPEOAttributeTimestamp64 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionHeaderPEOAttributeTimestamp74 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionHeaderPEOAttributeTimestamp84 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionHeaderPEOAttributeTimestamp94 | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag1 | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy18 | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate18 | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry3 | — |
| DESCRIPTION | RequisitionHeaderPEODescription4 | — |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus1 | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType1 | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus7 | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode2 | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId1 | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName10 | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage10 | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification2 | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate18 | — |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin18 | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy18 | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber15 | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId1 | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId4 | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId4 | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId13 | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId1 | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[receiptaccountingtxnrefpvo|ReceiptAccountingTxnRefPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate1 | — |
| ATTRIBUTE1 | RequisitionHeaderPEOAttribute160 | — |
| ATTRIBUTE10 | RequisitionHeaderPEOAttribute1012 | — |
| ATTRIBUTE11 | RequisitionHeaderPEOAttribute1116 | — |
| ATTRIBUTE12 | RequisitionHeaderPEOAttribute1214 | — |
| ATTRIBUTE13 | RequisitionHeaderPEOAttribute1312 | — |
| ATTRIBUTE14 | RequisitionHeaderPEOAttribute1412 | — |
| ATTRIBUTE15 | RequisitionHeaderPEOAttribute1512 | — |
| ATTRIBUTE16 | RequisitionHeaderPEOAttribute169 | — |
| ATTRIBUTE17 | RequisitionHeaderPEOAttribute179 | — |
| ATTRIBUTE18 | RequisitionHeaderPEOAttribute189 | — |
| ATTRIBUTE19 | RequisitionHeaderPEOAttribute199 | — |
| ATTRIBUTE2 | RequisitionHeaderPEOAttribute214 | — |
| ATTRIBUTE20 | RequisitionHeaderPEOAttribute209 | — |
| ATTRIBUTE3 | RequisitionHeaderPEOAttribute313 | — |
| ATTRIBUTE4 | RequisitionHeaderPEOAttribute413 | — |
| ATTRIBUTE5 | RequisitionHeaderPEOAttribute512 | — |
| ATTRIBUTE6 | RequisitionHeaderPEOAttribute612 | — |
| ATTRIBUTE7 | RequisitionHeaderPEOAttribute712 | — |
| ATTRIBUTE8 | RequisitionHeaderPEOAttribute812 | — |
| ATTRIBUTE9 | RequisitionHeaderPEOAttribute912 | — |
| ATTRIBUTE_CATEGORY | RequisitionHeaderPEOAttributeCategory12 | — |
| ATTRIBUTE_DATE1 | RequisitionHeaderPEOAttributeDate114 | — |
| ATTRIBUTE_DATE10 | RequisitionHeaderPEOAttributeDate106 | — |
| ATTRIBUTE_DATE2 | RequisitionHeaderPEOAttributeDate212 | — |
| ATTRIBUTE_DATE3 | RequisitionHeaderPEOAttributeDate312 | — |
| ATTRIBUTE_DATE4 | RequisitionHeaderPEOAttributeDate412 | — |
| ATTRIBUTE_DATE5 | RequisitionHeaderPEOAttributeDate512 | — |
| ATTRIBUTE_DATE6 | RequisitionHeaderPEOAttributeDate66 | — |
| ATTRIBUTE_DATE7 | RequisitionHeaderPEOAttributeDate76 | — |
| ATTRIBUTE_DATE8 | RequisitionHeaderPEOAttributeDate86 | — |
| ATTRIBUTE_DATE9 | RequisitionHeaderPEOAttributeDate96 | — |
| ATTRIBUTE_NUMBER1 | RequisitionHeaderPEOAttributeNumber114 | — |
| ATTRIBUTE_NUMBER10 | RequisitionHeaderPEOAttributeNumber109 | — |
| ATTRIBUTE_NUMBER2 | RequisitionHeaderPEOAttributeNumber212 | — |
| ATTRIBUTE_NUMBER3 | RequisitionHeaderPEOAttributeNumber312 | — |
| ATTRIBUTE_NUMBER4 | RequisitionHeaderPEOAttributeNumber412 | — |
| ATTRIBUTE_NUMBER5 | RequisitionHeaderPEOAttributeNumber512 | — |
| ATTRIBUTE_NUMBER6 | RequisitionHeaderPEOAttributeNumber69 | — |
| ATTRIBUTE_NUMBER7 | RequisitionHeaderPEOAttributeNumber79 | — |
| ATTRIBUTE_NUMBER8 | RequisitionHeaderPEOAttributeNumber89 | — |
| ATTRIBUTE_NUMBER9 | RequisitionHeaderPEOAttributeNumber99 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionHeaderPEOAttributeTimestamp17 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionHeaderPEOAttributeTimestamp104 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionHeaderPEOAttributeTimestamp27 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionHeaderPEOAttributeTimestamp37 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionHeaderPEOAttributeTimestamp47 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionHeaderPEOAttributeTimestamp57 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionHeaderPEOAttributeTimestamp64 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionHeaderPEOAttributeTimestamp74 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionHeaderPEOAttributeTimestamp84 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionHeaderPEOAttributeTimestamp94 | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag1 | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy18 | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate18 | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry3 | — |
| DESCRIPTION | RequisitionHeaderPEODescription4 | — |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus1 | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType1 | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus7 | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode2 | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId1 | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName10 | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage10 | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification2 | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate18 | — |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin18 | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy18 | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber15 | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId1 | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId4 | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId4 | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId13 | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId1 | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[receivingreceiptp2ptransactionpvo|ReceivingReceiptP2PTransactionPVO]] (AR)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | — |
| ATTRIBUTE1 | RequisitionHeaderPEOAttribute1 | — |
| ATTRIBUTE10 | RequisitionHeaderPEOAttribute10 | — |
| ATTRIBUTE11 | RequisitionHeaderPEOAttribute11 | — |
| ATTRIBUTE12 | RequisitionHeaderPEOAttribute12 | — |
| ATTRIBUTE13 | RequisitionHeaderPEOAttribute13 | — |
| ATTRIBUTE14 | RequisitionHeaderPEOAttribute14 | — |
| ATTRIBUTE15 | RequisitionHeaderPEOAttribute15 | — |
| ATTRIBUTE16 | RequisitionHeaderPEOAttribute16 | — |
| ATTRIBUTE17 | RequisitionHeaderPEOAttribute17 | — |
| ATTRIBUTE18 | RequisitionHeaderPEOAttribute18 | — |
| ATTRIBUTE19 | RequisitionHeaderPEOAttribute19 | — |
| ATTRIBUTE2 | RequisitionHeaderPEOAttribute2 | — |
| ATTRIBUTE20 | RequisitionHeaderPEOAttribute20 | — |
| ATTRIBUTE3 | RequisitionHeaderPEOAttribute3 | — |
| ATTRIBUTE4 | RequisitionHeaderPEOAttribute4 | — |
| ATTRIBUTE5 | RequisitionHeaderPEOAttribute5 | — |
| ATTRIBUTE6 | RequisitionHeaderPEOAttribute6 | — |
| ATTRIBUTE7 | RequisitionHeaderPEOAttribute7 | — |
| ATTRIBUTE8 | RequisitionHeaderPEOAttribute8 | — |
| ATTRIBUTE9 | RequisitionHeaderPEOAttribute9 | — |
| ATTRIBUTE_CATEGORY | RequisitionHeaderPEOAttributeCategory | — |
| ATTRIBUTE_DATE1 | RequisitionHeaderPEOAttributeDate1 | — |
| ATTRIBUTE_DATE10 | RequisitionHeaderPEOAttributeDate10 | — |
| ATTRIBUTE_DATE2 | RequisitionHeaderPEOAttributeDate2 | — |
| ATTRIBUTE_DATE3 | RequisitionHeaderPEOAttributeDate3 | — |
| ATTRIBUTE_DATE4 | RequisitionHeaderPEOAttributeDate4 | — |
| ATTRIBUTE_DATE5 | RequisitionHeaderPEOAttributeDate5 | — |
| ATTRIBUTE_DATE6 | RequisitionHeaderPEOAttributeDate6 | — |
| ATTRIBUTE_DATE7 | RequisitionHeaderPEOAttributeDate7 | — |
| ATTRIBUTE_DATE8 | RequisitionHeaderPEOAttributeDate8 | — |
| ATTRIBUTE_DATE9 | RequisitionHeaderPEOAttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | RequisitionHeaderPEOAttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | RequisitionHeaderPEOAttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | RequisitionHeaderPEOAttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | RequisitionHeaderPEOAttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | RequisitionHeaderPEOAttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | RequisitionHeaderPEOAttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | RequisitionHeaderPEOAttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | RequisitionHeaderPEOAttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | RequisitionHeaderPEOAttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | RequisitionHeaderPEOAttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | RequisitionHeaderPEOAttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | RequisitionHeaderPEOAttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | RequisitionHeaderPEOAttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | RequisitionHeaderPEOAttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | RequisitionHeaderPEOAttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | RequisitionHeaderPEOAttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | RequisitionHeaderPEOAttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | RequisitionHeaderPEOAttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | RequisitionHeaderPEOAttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | RequisitionHeaderPEOAttributeTimestamp9 | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | — |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[requisitionactionhistorypvo|RequisitionActionHistoryPVO]] (PO · BICC: 1/27)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | — |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | — |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | — |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | — |

### [[requisitiondistributionp1|RequisitionDistributionP1]] (PO · BICC: 16/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderBudgetControlEnabledFlag | ✅ |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | ✅ |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | ✅ |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | ✅ |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | ✅ |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderExternallyManagedFlag | ✅ |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderFundsChkFailWarnFlag | — |
| FUNDS_STATUS | RequisitionHeaderFundsStatus | ✅ |
| HAS_ACTION_REQUIRED_LINES | RequisitionHeaderHasActionRequiredLines | — |
| HAS_CANCELED_LINES | RequisitionHeaderHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderHasWithdrawnLines | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | ✅ |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderInternalTransferReqFlag | ✅ |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| LIFECYCLE_STATUS | RequisitionHeaderLifeCycleStatus | — |
| LINE_GROUP | RequisitionHeaderLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | ✅ |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | ✅ |

### [[requisitiondistributionrefpvo|RequisitionDistributionRefPVO]] (PO · BICC: 9/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | ✅ |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderFundsChkFailWarnFlag | — |
| FUNDS_STATUS | RequisitionHeaderFundsStatus | ✅ |
| HAS_ACTION_REQUIRED_LINES | RequisitionHeaderHasActionRequiredLines | — |
| HAS_CANCELED_LINES | RequisitionHeaderHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderHasWithdrawnLines | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | ✅ |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderInternalTransferReqFlag | ✅ |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| LIFECYCLE_STATUS | RequisitionHeaderLifeCycleStatus | — |
| LINE_GROUP | RequisitionHeaderLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | — |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | — |

### [[requisitionheaderextractpvo|RequisitionHeaderExtractPVO]] (PO · BICC: 48/105)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | ActiveRequisitionFlag | ✅ |
| APPROVAL_INSTANCE_ID | ApprovalInstanceId | ✅ |
| APPROVED_DATE | ApprovedDate | ✅ |
| ATTRIBUTE1 | Attribute1 | — |
| ATTRIBUTE10 | Attribute10 | — |
| ATTRIBUTE11 | Attribute11 | — |
| ATTRIBUTE12 | Attribute12 | — |
| ATTRIBUTE13 | Attribute13 | — |
| ATTRIBUTE14 | Attribute14 | — |
| ATTRIBUTE15 | Attribute15 | — |
| ATTRIBUTE16 | Attribute16 | — |
| ATTRIBUTE17 | Attribute17 | — |
| ATTRIBUTE18 | Attribute18 | — |
| ATTRIBUTE19 | Attribute19 | — |
| ATTRIBUTE2 | Attribute2 | — |
| ATTRIBUTE20 | Attribute20 | — |
| ATTRIBUTE3 | Attribute3 | — |
| ATTRIBUTE4 | Attribute4 | — |
| ATTRIBUTE5 | Attribute5 | — |
| ATTRIBUTE6 | Attribute6 | — |
| ATTRIBUTE7 | Attribute7 | — |
| ATTRIBUTE8 | Attribute8 | — |
| ATTRIBUTE9 | Attribute9 | — |
| ATTRIBUTE_CATEGORY | AttributeCategory | — |
| ATTRIBUTE_DATE1 | AttributeDate1 | — |
| ATTRIBUTE_DATE10 | AttributeDate10 | — |
| ATTRIBUTE_DATE2 | AttributeDate2 | — |
| ATTRIBUTE_DATE3 | AttributeDate3 | — |
| ATTRIBUTE_DATE4 | AttributeDate4 | — |
| ATTRIBUTE_DATE5 | AttributeDate5 | — |
| ATTRIBUTE_DATE6 | AttributeDate6 | — |
| ATTRIBUTE_DATE7 | AttributeDate7 | — |
| ATTRIBUTE_DATE8 | AttributeDate8 | — |
| ATTRIBUTE_DATE9 | AttributeDate9 | — |
| ATTRIBUTE_NUMBER1 | AttributeNumber1 | — |
| ATTRIBUTE_NUMBER10 | AttributeNumber10 | — |
| ATTRIBUTE_NUMBER2 | AttributeNumber2 | — |
| ATTRIBUTE_NUMBER3 | AttributeNumber3 | — |
| ATTRIBUTE_NUMBER4 | AttributeNumber4 | — |
| ATTRIBUTE_NUMBER5 | AttributeNumber5 | — |
| ATTRIBUTE_NUMBER6 | AttributeNumber6 | — |
| ATTRIBUTE_NUMBER7 | AttributeNumber7 | — |
| ATTRIBUTE_NUMBER8 | AttributeNumber8 | — |
| ATTRIBUTE_NUMBER9 | AttributeNumber9 | — |
| ATTRIBUTE_TIMESTAMP1 | AttributeTimestamp1 | — |
| ATTRIBUTE_TIMESTAMP10 | AttributeTimestamp10 | — |
| ATTRIBUTE_TIMESTAMP2 | AttributeTimestamp2 | — |
| ATTRIBUTE_TIMESTAMP3 | AttributeTimestamp3 | — |
| ATTRIBUTE_TIMESTAMP4 | AttributeTimestamp4 | — |
| ATTRIBUTE_TIMESTAMP5 | AttributeTimestamp5 | — |
| ATTRIBUTE_TIMESTAMP6 | AttributeTimestamp6 | — |
| ATTRIBUTE_TIMESTAMP7 | AttributeTimestamp7 | — |
| ATTRIBUTE_TIMESTAMP8 | AttributeTimestamp8 | — |
| ATTRIBUTE_TIMESTAMP9 | AttributeTimestamp9 | — |
| BUDGET_CONTROL_ENABLED_FLAG | BudgetControlEnabledFlag | ✅ |
| CHANGE_PENDING_FLAG | ChangePendingFlag | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DEFAULT_TAXATION_COUNTRY | DefaultTaxationCountry | ✅ |
| DESCRIPTION | Description | ✅ |
| DOCUMENT_STATUS | DocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | DocumentSubType | ✅ |
| EMERGENCY_PO_NUMBER | EmergencyPoNumber | ✅ |
| EMERGENCY_REQ_FLAG | EmergencyReqFlag | ✅ |
| EXTERNALLY_MANAGED_FLAG | ExternallyManagedFlag | ✅ |
| FUNDS_CHK_FAIL_WARN_FLAG | FundsChkFailWarnFlag | ✅ |
| FUNDS_OVERRIDE_APPROVER_ID | FundsOverrideApproverId | ✅ |
| FUNDS_STATUS | FundsStatus | ✅ |
| HAS_ACTION_REQUIRED_LINES | HasActionRequiredLinesFlag | ✅ |
| HAS_CANCELED_LINES | HasCanceledLines | — |
| HAS_INCOMPLETE_LINES | HasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | HasPendingApprLines | — |
| HAS_REJECTED_LINES | HasRejectedLines | — |
| HAS_RETURNED_LINES | HasReturnedLines | — |
| HAS_WITHDRAWN_LINES | HasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | InsufficientFundsFlag | ✅ |
| INTERFACE_SOURCE_CODE | InterfaceSourceCode | ✅ |
| INTERFACE_SOURCE_LINE_ID | InterfaceSourceLineId | ✅ |
| INTERNAL_TRANSFER_REQ_FLAG | InternalTransferReqFlag | ✅ |
| JOB_DEFINITION_NAME | JobDefinitionName | ✅ |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | ✅ |
| JUSTIFICATION | Justification | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| LIFECYCLE_STATUS | LifecycleStatus | ✅ |
| LINE_GROUP | LineGroup | ✅ |
| LOCKED_BY_BUYER_FLAG | LockedByBuyerFlag | ✅ |
| MODIFYING_APPROVER_ID | ModifyingApproverId | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | ✅ |
| OVERRIDING_APPROVER_ID | OverridingApproverId | ✅ |
| PCARD_ID | PcardId | ✅ |
| PRC_BU_ID | PrcBuId | ✅ |
| PREPARER_ID | PreparerId | ✅ |
| PROCESS_STATUS | ProcessStatus | ✅ |
| REJECT_REASON | RejectReason | ✅ |
| REJECTED_BY_APPROVER_ID | RejectedByApproverId | ✅ |
| REQ_BU_ID | ReqBuId | ✅ |
| REQ_IMPORT_APPROVER_ID | ReqImportApproverId | ✅ |
| REQUEST_ID | RequestId | ✅ |
| REQUISITION_HEADER_ID | RequisitionHeaderId | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| SOLDTO_LE_ID | SoldtoLeId | ✅ |
| SUBMISSION_DATE | SubmissionDate | ✅ |
| TAX_USER_OVERRIDE_HDR_FLAG | TaxUserOverrideHdrFlag | ✅ |

### [[requisitionheaderp1|RequisitionHeaderP1]] (PO · BICC: 6/29)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | ActiveRequisitionFlag | — |
| APPROVED_DATE | ApprovedDate | — |
| BUDGET_CONTROL_ENABLED_FLAG | BudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | ChangePendingFlag | — |
| CREATED_BY | CreatedBy | — |
| CREATION_DATE | CreationDate | — |
| DESCRIPTION | Description | ✅ |
| DOCUMENT_STATUS | DocumentStatus | ✅ |
| EMERGENCY_PO_NUMBER | EmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | EmergencyReqFlag | — |
| INTERFACE_SOURCE_CODE | InterfaceSourceCode | ✅ |
| INTERFACE_SOURCE_LINE_ID | InterfaceSourceLineId | — |
| JOB_DEFINITION_NAME | JobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | JobDefinitionPackage | — |
| JUSTIFICATION | Justification | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | — |
| MODIFYING_APPROVER_ID | ModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PCARD_ID | PcardId | — |
| PRC_BU_ID | PrcBuId | — |
| PREPARER_ID | PreparerId | — |
| REQ_BU_ID | ReqBuId | — |
| REQUEST_ID | RequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderId | ✅ |
| REQUISITION_NUMBER | RequisitionNumber | ✅ |
| SOLDTO_LE_ID | SoldtoLeId | — |
| SUBMISSION_DATE | SubmissionDate | — |

### [[requisitionlinep1|RequisitionLineP1]] (PO · BICC: 18/43)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderBudgetControlEnabledFlag | ✅ |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | ✅ |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | ✅ |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | ✅ |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | ✅ |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderExternallyManagedFlag | ✅ |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderFundsChkFailWarnFlag | ✅ |
| FUNDS_STATUS | RequisitionHeaderFundsStatus | ✅ |
| HAS_ACTION_REQUIRED_LINES | RequisitionHeaderHasActionRequiredLines | — |
| HAS_CANCELED_LINES | RequisitionHeaderHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderHasWithdrawnLines | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | ✅ |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderInternalTransferRequisitionFlag | ✅ |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| LIFECYCLE_STATUS | RequisitionHeaderLifeCycleStatus | — |
| LINE_GROUP | RequisitionHeaderLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | ✅ |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | ✅ |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | ✅ |

### [[standarddistributionpvo|StandardDistributionPVO]] (PO · BICC: 2/28)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderActiveRequisitionFlag | — |
| APPROVED_DATE | RequisitionHeaderApprovedDate | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderCreatedBy | — |
| CREATION_DATE | RequisitionHeaderCreationDate | — |
| DESCRIPTION | RequisitionHeaderDescription | — |
| DOCUMENT_STATUS | RequisitionHeaderDocumentStatus | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | ExternallyManagedFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderInterfaceSourceLineId | — |
| JOB_DEFINITION_NAME | RequisitionHeaderJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderLastUpdatedBy | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderObjectVersionNumber | — |
| PCARD_ID | RequisitionHeaderPcardId | — |
| PRC_BU_ID | RequisitionHeaderPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPreparerId | — |
| REQ_BU_ID | RequisitionHeaderReqBuId | — |
| REQUEST_ID | RequisitionHeaderRequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderRequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderRequisitionNumber | ✅ |
| SUBMISSION_DATE | RequisitionHeaderSubmissionDate | — |

### [[transferorderdistributionpvo|TransferOrderDistributionPVO]] (OTHER · BICC: 1/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | — |
| DOCUMENT_STATUS | DocumentStatus | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[transferorderlinepvo|TransferOrderLinePVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | — |
| DOCUMENT_STATUS | DocumentStatus | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[transferorderlinerefpvo|TransferOrderLineRefPVO]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | — |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | — |
| DOCUMENT_STATUS | DocumentStatus | — |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | — |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | — |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | — |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[wooperationspvo|WOOperationsPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |

### [[wooperationsrefpvo|WOOperationsRefPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |

### [[woprocurementpopvo|WOProcurementPOPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[woprocurementreceiptpvo|WOProcurementReceiptPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

### [[woprocurementreqpvo|WOProcurementReqPVO]] (OTHER · BICC: 6/49)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ACTIVE_REQUISITION_FLAG | RequisitionHeaderPEOActiveRequisitionFlag | — |
| APPROVAL_INSTANCE_ID | RequisitionHeaderPEOApprovalInstanceId | — |
| APPROVED_DATE | RequisitionHeaderPEOApprovedDate | ✅ |
| BUDGET_CONTROL_ENABLED_FLAG | RequisitionHeaderPEOBudgetControlEnabledFlag | — |
| CHANGE_PENDING_FLAG | RequisitionHeaderPEOChangePendingFlag | — |
| CREATED_BY | RequisitionHeaderPEOCreatedBy | — |
| CREATION_DATE | RequisitionHeaderPEOCreationDate | — |
| DEFAULT_TAXATION_COUNTRY | RequisitionHeaderPEODefaultTaxationCountry | — |
| DESCRIPTION | RequisitionHeaderPEODescription | ✅ |
| DOCUMENT_STATUS | RequisitionHeaderPEODocumentStatus | ✅ |
| DOCUMENT_SUB_TYPE | RequisitionHeaderPEODocumentSubType | — |
| EMERGENCY_PO_NUMBER | RequisitionHeaderPEOEmergencyPoNumber | — |
| EMERGENCY_REQ_FLAG | RequisitionHeaderPEOEmergencyReqFlag | — |
| EXTERNALLY_MANAGED_FLAG | RequisitionHeaderPEOExternallyManagedFlag | — |
| FUNDS_CHK_FAIL_WARN_FLAG | RequisitionHeaderPEOFundsChkFailWarnFlag | — |
| FUNDS_OVERRIDE_APPROVER_ID | RequisitionHeaderPEOFundsOverrideApproverId | — |
| FUNDS_STATUS | RequisitionHeaderPEOFundsStatus | — |
| HAS_CANCELED_LINES | RequisitionHeaderPEOHasCanceledLines | — |
| HAS_INCOMPLETE_LINES | RequisitionHeaderPEOHasIncompleteLines | — |
| HAS_PENDING_APPR_LINES | RequisitionHeaderPEOHasPendingApprLines | — |
| HAS_REJECTED_LINES | RequisitionHeaderPEOHasRejectedLines | — |
| HAS_RETURNED_LINES | RequisitionHeaderPEOHasReturnedLines | — |
| HAS_WITHDRAWN_LINES | RequisitionHeaderPEOHasWithdrawnLines | — |
| INSUFFICIENT_FUNDS_FLAG | RequisitionHeaderPEOInsufficientFundsFlag | — |
| INTERFACE_SOURCE_CODE | RequisitionHeaderPEOInterfaceSourceCode | — |
| INTERFACE_SOURCE_LINE_ID | RequisitionHeaderPEOInterfaceSourceLineId | — |
| INTERNAL_TRANSFER_REQ_FLAG | RequisitionHeaderPEOInternalTransferReqFlag | — |
| JOB_DEFINITION_NAME | RequisitionHeaderPEOJobDefinitionName | — |
| JOB_DEFINITION_PACKAGE | RequisitionHeaderPEOJobDefinitionPackage | — |
| JUSTIFICATION | RequisitionHeaderPEOJustification | ✅ |
| LAST_UPDATE_DATE | RequisitionHeaderPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RequisitionHeaderPEOLastUpdateLogin | — |
| LAST_UPDATED_BY | RequisitionHeaderPEOLastUpdatedBy | — |
| LINE_GROUP | RequisitionHeaderPEOLineGroup | — |
| LOCKED_BY_BUYER_FLAG | RequisitionHeaderPEOLockedByBuyerFlag | — |
| MODIFYING_APPROVER_ID | RequisitionHeaderPEOModifyingApproverId | — |
| OBJECT_VERSION_NUMBER | RequisitionHeaderPEOObjectVersionNumber | — |
| OVERRIDING_APPROVER_ID | RequisitionHeaderPEOOverridingApproverId | — |
| PCARD_ID | RequisitionHeaderPEOPcardId | — |
| PRC_BU_ID | RequisitionHeaderPEOPrcBuId | — |
| PREPARER_ID | RequisitionHeaderPEOPreparerId | — |
| REQ_BU_ID | RequisitionHeaderPEOReqBuId | — |
| REQ_IMPORT_APPROVER_ID | RequisitionHeaderPEOReqImportApproverId | — |
| REQUEST_ID | RequisitionHeaderPEORequestId | — |
| REQUISITION_HEADER_ID | RequisitionHeaderPEORequisitionHeaderId | — |
| REQUISITION_NUMBER | RequisitionHeaderPEORequisitionNumber | ✅ |
| SOLDTO_LE_ID | RequisitionHeaderPEOSoldtoLeId | — |
| SUBMISSION_DATE | RequisitionHeaderPEOSubmissionDate | — |
| TAX_USER_OVERRIDE_HDR_FLAG | RequisitionHeaderPEOTaxUserOverrideHdrFlag | — |

---

## 📚 Referências

- [Oracle Docs — POR_REQUISITION_HEADERS_ALL](https://docs.oracle.com/en/cloud/saas/procurement/25a/oedmf/porrequisitionheadersall.html)
- [[po-module-data-dictionary]] — Dossiê do módulo Procurement
