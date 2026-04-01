---
id: DOC-AP-PVO-TransactionConsoleP1
doc_type: system-doc
title: "TransactionConsoleP1 — PVO Accounts Payable"
system: Oracle Fusion Cloud ERP
module: Accounts Payable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ap
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TransactionConsoleP1
  - transactionconsolep1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransactionConsoleP1

## 📌 Visão Geral

Extrai os dados do console de transações de RH, incluindo transações, ocorrências, atribuições de responsáveis, processos de aprovação e detalhes de erro. Permite monitorar e resolver problemas em transações de gestão de pessoas de forma centralizada.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.TransactionConsoleP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 184 | 7 | 1 | 20 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_console_issue|FND_CONSOLE_ISSUE]] — 31 atributos (3 BICC)
- [[fnd_console_transaction_info|FND_CONSOLE_TRANSACTION_INFO]] — 38 atributos (1 BICC)
- [[hrc_arm_process_vl|HRC_ARM_PROCESS_VL]] — 16 atributos (2 BICC)
- [[hrc_console_issue_assignment|HRC_CONSOLE_ISSUE_ASSIGNMENT]] — 13 atributos (1 BICC)
- [[hrc_txn_console_entry|HRC_TXN_CONSOLE_ENTRY]] — 18 atributos (4 BICC)
- [[hrc_txn_data|HRC_TXN_DATA]] — 48 atributos (5 BICC)
- [[hrc_txn_header|HRC_TXN_HEADER]] — 20 atributos (1 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[fnd_console_issue|FND_CONSOLE_ISSUE]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndConsoleIssuePEOAttribute10Varchar21 | ATTRIBUTE10_VARCHAR2 | — | — |
| 2 | FndConsoleIssuePEOAttribute11Varchar21 | ATTRIBUTE11_VARCHAR2 | — | — |
| 3 | FndConsoleIssuePEOAttribute12Varchar21 | ATTRIBUTE12_VARCHAR2 | — | — |
| 4 | FndConsoleIssuePEOAttribute13Varchar21 | ATTRIBUTE13_VARCHAR2 | — | — |
| 5 | FndConsoleIssuePEOAttribute14Varchar21 | ATTRIBUTE14_VARCHAR2 | — | — |
| 6 | FndConsoleIssuePEOAttribute15Varchar21 | ATTRIBUTE15_VARCHAR2 | — | — |
| 7 | FndConsoleIssuePEOAttribute1Varchar21 | ATTRIBUTE1_VARCHAR2 | — | — |
| 8 | FndConsoleIssuePEOAttribute2Varchar21 | ATTRIBUTE2_VARCHAR2 | — | — |
| 9 | FndConsoleIssuePEOAttribute3Varchar21 | ATTRIBUTE3_VARCHAR2 | — | — |
| 10 | FndConsoleIssuePEOAttribute4Varchar21 | ATTRIBUTE4_VARCHAR2 | — | — |
| 11 | FndConsoleIssuePEOAttribute5Varchar21 | ATTRIBUTE5_VARCHAR2 | — | — |
| 12 | FndConsoleIssuePEOAttribute6Varchar21 | ATTRIBUTE6_VARCHAR2 | — | — |
| 13 | FndConsoleIssuePEOAttribute7Varchar21 | ATTRIBUTE7_VARCHAR2 | — | — |
| 14 | FndConsoleIssuePEOAttribute8Varchar21 | ATTRIBUTE8_VARCHAR2 | — | — |
| 15 | FndConsoleIssuePEOAttribute9Varchar21 | ATTRIBUTE9_VARCHAR2 | — | — |
| 16 | FndConsoleIssuePEOAttributeCategory2 | ATTRIBUTE_CATEGORY | — | — |
| 17 | FndConsoleIssuePEOConsoleTransactionId1 | CONSOLE_TRANSACTION_ID | — | — |
| 18 | FndConsoleIssuePEOCreatedBy5 | CREATED_BY | — | — |
| 19 | FndConsoleIssuePEOCreationDate3 | CREATION_DATE | — | — |
| 20 | FndConsoleIssuePEOErrorCode | ERROR_CODE | — | — |
| 21 | FndConsoleIssuePEOFaultCode | FAULT_CODE | — | — |
| 22 | FndConsoleIssuePEOFaultId | FAULT_ID | — | — |
| 23 | FndConsoleIssuePEOFaultPayload | FAULT_PAYLOAD | — | — |
| 24 | FndConsoleIssuePEOIssueActionCode | ISSUE_ACTION_CODE | — | — |
| 25 | FndConsoleIssuePEOIssueId | ISSUE_ID | — | ✅ |
| 26 | FndConsoleIssuePEOIssueStatusCode | ISSUE_STATUS_CODE | — | ✅ |
| 27 | FndConsoleIssuePEOIssueTitle | ISSUE_TITLE | — | — |
| 28 | FndConsoleIssuePEOIssueTypeCode | ISSUE_TYPE_CODE | — | — |
| 29 | FndConsoleIssuePEOLastUpdateDate4 | LAST_UPDATE_DATE | — | ✅ |
| 30 | FndConsoleIssuePEOLastUpdateLogin4 | LAST_UPDATE_LOGIN | — | — |
| 31 | FndConsoleIssuePEOLastUpdatedBy4 | LAST_UPDATED_BY | — | — |

### [[fnd_console_transaction_info|FND_CONSOLE_TRANSACTION_INFO]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FndConsoleTransactionInfoPEOAttribute10Varchar2 | ATTRIBUTE10_VARCHAR2 | — | — |
| 2 | FndConsoleTransactionInfoPEOAttribute11Varchar2 | ATTRIBUTE11_VARCHAR2 | — | — |
| 3 | FndConsoleTransactionInfoPEOAttribute12Varchar2 | ATTRIBUTE12_VARCHAR2 | — | — |
| 4 | FndConsoleTransactionInfoPEOAttribute13Varchar2 | ATTRIBUTE13_VARCHAR2 | — | — |
| 5 | FndConsoleTransactionInfoPEOAttribute14Varchar2 | ATTRIBUTE14_VARCHAR2 | — | — |
| 6 | FndConsoleTransactionInfoPEOAttribute15Varchar2 | ATTRIBUTE15_VARCHAR2 | — | — |
| 7 | FndConsoleTransactionInfoPEOAttribute1Varchar2 | ATTRIBUTE1_VARCHAR2 | — | — |
| 8 | FndConsoleTransactionInfoPEOAttribute2Varchar2 | ATTRIBUTE2_VARCHAR2 | — | — |
| 9 | FndConsoleTransactionInfoPEOAttribute3Varchar2 | ATTRIBUTE3_VARCHAR2 | — | — |
| 10 | FndConsoleTransactionInfoPEOAttribute4Varchar2 | ATTRIBUTE4_VARCHAR2 | — | — |
| 11 | FndConsoleTransactionInfoPEOAttribute5Varchar2 | ATTRIBUTE5_VARCHAR2 | — | — |
| 12 | FndConsoleTransactionInfoPEOAttribute6Varchar2 | ATTRIBUTE6_VARCHAR2 | — | — |
| 13 | FndConsoleTransactionInfoPEOAttribute7Varchar2 | ATTRIBUTE7_VARCHAR2 | — | — |
| 14 | FndConsoleTransactionInfoPEOAttribute8Varchar2 | ATTRIBUTE8_VARCHAR2 | — | — |
| 15 | FndConsoleTransactionInfoPEOAttribute9Varchar2 | ATTRIBUTE9_VARCHAR2 | — | — |
| 16 | FndConsoleTransactionInfoPEOAttributeCategory1 | ATTRIBUTE_CATEGORY | — | — |
| 17 | FndConsoleTransactionInfoPEOConsoleTransactionId | CONSOLE_TRANSACTION_ID | — | — |
| 18 | FndConsoleTransactionInfoPEOCreatedBy2 | CREATED_BY | — | — |
| 19 | FndConsoleTransactionInfoPEOCreationDate2 | CREATION_DATE | — | — |
| 20 | FndConsoleTransactionInfoPEOCustomAbortFlag | CUSTOM_ABORT_FLAG | — | — |
| 21 | FndConsoleTransactionInfoPEODomainName | DOMAIN_NAME | — | — |
| 22 | FndConsoleTransactionInfoPEOEcid | ECID | — | — |
| 23 | FndConsoleTransactionInfoPEOFamily | FAMILY | — | — |
| 24 | FndConsoleTransactionInfoPEOLastUpdateDate2 | LAST_UPDATE_DATE | — | ✅ |
| 25 | FndConsoleTransactionInfoPEOLastUpdateLogin2 | LAST_UPDATE_LOGIN | — | — |
| 26 | FndConsoleTransactionInfoPEOLastUpdatedBy2 | LAST_UPDATED_BY | — | — |
| 27 | FndConsoleTransactionInfoPEOModuleComponentInstanceId | MODULE_COMPONENT_INSTANCE_ID | — | — |
| 28 | FndConsoleTransactionInfoPEOModuleComponentName | MODULE_COMPONENT_NAME | — | — |
| 29 | FndConsoleTransactionInfoPEOModuleComponentType | MODULE_COMPONENT_TYPE | — | — |
| 30 | FndConsoleTransactionInfoPEOModuleInstanceDesc | MODULE_INSTANCE_DESC | — | — |
| 31 | FndConsoleTransactionInfoPEOModuleInstanceId | MODULE_INSTANCE_ID | — | — |
| 32 | FndConsoleTransactionInfoPEOModuleName | MODULE_NAME | — | — |
| 33 | FndConsoleTransactionInfoPEOModuleRevision | MODULE_REVISION | — | — |
| 34 | FndConsoleTransactionInfoPEOModuleType | MODULE_TYPE | — | — |
| 35 | FndConsoleTransactionInfoPEOTransactionId2 | TRANSACTION_ID | — | — |
| 36 | FndConsoleTransactionInfoPEOTransactionSequence | TRANSACTION_SEQUENCE | — | — |
| 37 | FndConsoleTransactionInfoPEOTransactionTypeCode | TRANSACTION_TYPE_CODE | — | — |
| 38 | FndConsoleTransactionInfoPEOTransactionUserKey | TRANSACTION_USER_KEY | — | — |

### [[hrc_arm_process_vl|HRC_ARM_PROCESS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalProcessPEOActive | ACTIVE | — | — |
| 2 | ApprovalProcessPEOCompositeId | COMPOSITE_ID | — | — |
| 3 | ApprovalProcessPEOCreatedBy3 | CREATED_BY | — | — |
| 4 | ApprovalProcessPEOCreationDate4 | CREATION_DATE | — | — |
| 5 | ApprovalProcessPEODescription | DESCRIPTION | — | — |
| 6 | ApprovalProcessPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 7 | ApprovalProcessPEOLastUpdateDate3 | LAST_UPDATE_DATE | — | ✅ |
| 8 | ApprovalProcessPEOLastUpdateLogin3 | LAST_UPDATE_LOGIN | — | — |
| 9 | ApprovalProcessPEOLastUpdatedBy3 | LAST_UPDATED_BY | — | — |
| 10 | ApprovalProcessPEOModuleId | MODULE_ID | — | — |
| 11 | ApprovalProcessPEOName | NAME | — | ✅ |
| 12 | ApprovalProcessPEOObjectVersionNumber2 | OBJECT_VERSION_NUMBER | — | — |
| 13 | ApprovalProcessPEOProcessId | PROCESS_ID | — | — |
| 14 | ApprovalProcessPEORuleFileName | RULE_FILE_NAME | — | — |
| 15 | ApprovalProcessPEOTaskFileName | TASK_FILE_NAME | — | — |
| 16 | ApprovalProcessPEOTxnModuleIdentifier | TXN_MODULE_IDENTIFIER | — | — |

### [[hrc_console_issue_assignment|HRC_CONSOLE_ISSUE_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsoleIssueAssignmentPEOAssignedTo | ASSIGNED_TO | — | ✅ |
| 2 | ConsoleIssueAssignmentPEOConsoleTransactionId | CONSOLE_TRANSACTION_ID | — | — |
| 3 | ConsoleIssueAssignmentPEOCreatedBy | CREATED_BY | — | — |
| 4 | ConsoleIssueAssignmentPEOCreationDate | CREATION_DATE | — | — |
| 5 | ConsoleIssueAssignmentPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 6 | ConsoleIssueAssignmentPEOIssueAssignmentId | ISSUE_ASSIGNMENT_ID | — | — |
| 7 | ConsoleIssueAssignmentPEOIssueId | ISSUE_ID | — | — |
| 8 | ConsoleIssueAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | ConsoleIssueAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | ConsoleIssueAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | ConsoleIssueAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 12 | ConsoleIssueAssignmentPEOPriority | PRIORITY | — | — |
| 13 | ConsoleIssueAssignmentPEOTransactionId | TRANSACTION_ID | — | — |

### [[hrc_txn_console_entry|HRC_TXN_CONSOLE_ENTRY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ConsoleEntryPEOChangeEffectiveDate | CHANGE_EFFECTIVE_DATE | — | ✅ |
| 2 | ConsoleEntryPEOConsoleEntryId | CONSOLE_ENTRY_ID | — | — |
| 3 | ConsoleEntryPEOConsoleTxnStatus | CONSOLE_TXN_STATUS | — | ✅ |
| 4 | ConsoleEntryPEOCreatedBy | CREATED_BY | — | — |
| 5 | ConsoleEntryPEOCreationDate | CREATION_DATE | — | — |
| 6 | ConsoleEntryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | ConsoleEntryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | ConsoleEntryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ConsoleEntryPEOObjectName | OBJECT_NAME | — | — |
| 10 | ConsoleEntryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 11 | ConsoleEntryPEOProcessCategory | PROCESS_CATEGORY | — | ✅ |
| 12 | ConsoleEntryPEOSrNumber | SR_NUMBER | — | — |
| 13 | ConsoleEntryPEOStatusCategory | STATUS_CATEGORY | — | ✅ |
| 14 | ConsoleEntryPEOTaskApprovers | TASK_APPROVERS | — | — |
| 15 | ConsoleEntryPEOTaskId | TASK_ID | — | — |
| 16 | ConsoleEntryPEOTaskOutcome | TASK_OUTCOME | — | — |
| 17 | ConsoleEntryPEOTaskState | TASK_STATE | — | — |
| 18 | ConsoleEntryPEOTransactionId | TRANSACTION_ID | — | — |

### [[hrc_txn_data|HRC_TXN_DATA]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HrcTxnDataPEOAttribute1 | ATTRIBUTE1 | — | — |
| 2 | HrcTxnDataPEOAttribute10 | ATTRIBUTE10 | — | — |
| 3 | HrcTxnDataPEOAttribute11 | ATTRIBUTE11 | — | — |
| 4 | HrcTxnDataPEOAttribute12 | ATTRIBUTE12 | — | — |
| 5 | HrcTxnDataPEOAttribute13 | ATTRIBUTE13 | — | — |
| 6 | HrcTxnDataPEOAttribute14 | ATTRIBUTE14 | — | — |
| 7 | HrcTxnDataPEOAttribute15 | ATTRIBUTE15 | — | — |
| 8 | HrcTxnDataPEOAttribute16 | ATTRIBUTE16 | — | — |
| 9 | HrcTxnDataPEOAttribute17 | ATTRIBUTE17 | — | — |
| 10 | HrcTxnDataPEOAttribute18 | ATTRIBUTE18 | — | — |
| 11 | HrcTxnDataPEOAttribute19 | ATTRIBUTE19 | — | — |
| 12 | HrcTxnDataPEOAttribute2 | ATTRIBUTE2 | — | — |
| 13 | HrcTxnDataPEOAttribute20 | ATTRIBUTE20 | — | — |
| 14 | HrcTxnDataPEOAttribute21 | ATTRIBUTE21 | — | — |
| 15 | HrcTxnDataPEOAttribute22 | ATTRIBUTE22 | — | — |
| 16 | HrcTxnDataPEOAttribute23 | ATTRIBUTE23 | — | — |
| 17 | HrcTxnDataPEOAttribute24 | ATTRIBUTE24 | — | — |
| 18 | HrcTxnDataPEOAttribute25 | ATTRIBUTE25 | — | — |
| 19 | HrcTxnDataPEOAttribute26 | ATTRIBUTE26 | — | — |
| 20 | HrcTxnDataPEOAttribute27 | ATTRIBUTE27 | — | — |
| 21 | HrcTxnDataPEOAttribute28 | ATTRIBUTE28 | — | — |
| 22 | HrcTxnDataPEOAttribute29 | ATTRIBUTE29 | — | — |
| 23 | HrcTxnDataPEOAttribute3 | ATTRIBUTE3 | — | — |
| 24 | HrcTxnDataPEOAttribute30 | ATTRIBUTE30 | — | — |
| 25 | HrcTxnDataPEOAttribute4 | ATTRIBUTE4 | — | — |
| 26 | HrcTxnDataPEOAttribute5 | ATTRIBUTE5 | — | — |
| 27 | HrcTxnDataPEOAttribute6 | ATTRIBUTE6 | — | — |
| 28 | HrcTxnDataPEOAttribute7 | ATTRIBUTE7 | — | — |
| 29 | HrcTxnDataPEOAttribute8 | ATTRIBUTE8 | — | — |
| 30 | HrcTxnDataPEOAttribute9 | ATTRIBUTE9 | — | — |
| 31 | HrcTxnDataPEOAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | HrcTxnDataPEOCompletedDate | COMPLETED_DATE | — | ✅ |
| 33 | HrcTxnDataPEOCreatedBy1 | CREATED_BY | — | — |
| 34 | HrcTxnDataPEOCreationDate1 | CREATION_DATE | — | — |
| 35 | HrcTxnDataPEOCurrentApprover | CURRENT_APPROVER | — | — |
| 36 | HrcTxnDataPEOEcid | ECID | — | — |
| 37 | HrcTxnDataPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 38 | HrcTxnDataPEOLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 39 | HrcTxnDataPEOLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 40 | HrcTxnDataPEOLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 41 | HrcTxnDataPEOObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 42 | HrcTxnDataPEOState | STATE | — | ✅ |
| 43 | HrcTxnDataPEOStatus | STATUS | — | ✅ |
| 44 | HrcTxnDataPEOSubmittedBy | SUBMITTED_BY | — | ✅ |
| 45 | HrcTxnDataPEOSubmittedDate | SUBMITTED_DATE | — | — |
| 46 | HrcTxnDataPEOTaskId | TASK_ID | — | — |
| 47 | HrcTxnDataPEOTransactionDataId | TRANSACTION_DATA_ID | — | — |
| 48 | HrcTxnDataPEOTransactionId1 | TRANSACTION_ID | — | — |

### [[hrc_txn_header|HRC_TXN_HEADER]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | HrcTxnHeaderPEOApplicationId | APPLICATION_ID | — | — |
| 2 | HrcTxnHeaderPEOCreatedBy | CREATED_BY | — | — |
| 3 | HrcTxnHeaderPEOCreationDate | CREATION_DATE | — | — |
| 4 | HrcTxnHeaderPEOInitiatorUserId | INITIATOR_USER_ID | — | — |
| 5 | HrcTxnHeaderPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | HrcTxnHeaderPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | HrcTxnHeaderPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | HrcTxnHeaderPEOModuleGroup | MODULE_GROUP | — | — |
| 9 | HrcTxnHeaderPEOModuleIdentifier | MODULE_IDENTIFIER | — | — |
| 10 | HrcTxnHeaderPEOObject | OBJECT | — | — |
| 11 | HrcTxnHeaderPEOObjectId | OBJECT_ID | — | ✅ |
| 12 | HrcTxnHeaderPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 13 | HrcTxnHeaderPEOParentTransactionId | PARENT_TRANSACTION_ID | — | — |
| 14 | HrcTxnHeaderPEOProcessId | PROCESS_ID | — | — |
| 15 | HrcTxnHeaderPEOProcessOwner | PROCESS_OWNER | — | — |
| 16 | HrcTxnHeaderPEOReentryFunction | REENTRY_FUNCTION | — | — |
| 17 | HrcTxnHeaderPEOSectionDisplayName | SECTION_DISPLAY_NAME | — | — |
| 18 | HrcTxnHeaderPEOSubject | SUBJECT | — | — |
| 19 | HrcTxnHeaderPEOSubjectId | SUBJECT_ID | — | ✅ |
| 20 | HrcTxnHeaderPEOTransactionId | TRANSACTION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
