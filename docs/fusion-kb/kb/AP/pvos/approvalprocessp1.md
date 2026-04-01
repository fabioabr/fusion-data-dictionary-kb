---
id: DOC-AP-PVO-ApprovalProcessP1
doc_type: system-doc
title: "ApprovalProcessP1 — PVO Accounts Payable"
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
  - ApprovalProcessP1
  - approvalprocessp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ApprovalProcessP1

## 📌 Visão Geral

Extrai a configuração dos processos de aprovação de transações de RH, incluindo nome, descrição e status do processo. Fundamental para auditoria dos workflows de aprovação e mapeamento das regras de governança em processos de gestão de pessoas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmApprovalsReportingAM.ApprovalProcessP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 3 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[hrc_arm_process_vl|HRC_ARM_PROCESS_VL]] — 26 atributos (1 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hrc_arm_process_vl|HRC_ARM_PROCESS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalProcessPEOActive | ACTIVE | — | — |
| 2 | ApprovalProcessPEOAdditionalRestResource | ADDITIONAL_REST_RESOURCE | — | — |
| 3 | ApprovalProcessPEOBypassSupported | BYPASS_SUPPORTED | — | — |
| 4 | ApprovalProcessPEOCategoryCode | CATEGORY_CODE | — | — |
| 5 | ApprovalProcessPEOCategoryName | CATEGORY_NAME | — | — |
| 6 | ApprovalProcessPEOCompositeId | COMPOSITE_ID | — | — |
| 7 | ApprovalProcessPEOCreatedBy | CREATED_BY | — | — |
| 8 | ApprovalProcessPEOCreationDate | CREATION_DATE | — | — |
| 9 | ApprovalProcessPEODescription | DESCRIPTION | — | — |
| 10 | ApprovalProcessPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 11 | ApprovalProcessPEOFamily | FAMILY | — | — |
| 12 | ApprovalProcessPEOIsTxnFrameworkProcess | IS_TXN_FRAMEWORK_PROCESS | — | — |
| 13 | ApprovalProcessPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 14 | ApprovalProcessPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 15 | ApprovalProcessPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 16 | ApprovalProcessPEOModuleId | MODULE_ID | — | — |
| 17 | ApprovalProcessPEOName | NAME | — | ✅ |
| 18 | ApprovalProcessPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 19 | ApprovalProcessPEOProcessId | PROCESS_ID | 🔑 | ✅ |
| 20 | ApprovalProcessPEOResourceContextShortName | RESOURCE_CONTEXT_SHORT_NAME | — | — |
| 21 | ApprovalProcessPEORestResourceKey | REST_RESOURCE_KEY | — | — |
| 22 | ApprovalProcessPEORuleFileName | RULE_FILE_NAME | — | — |
| 23 | ApprovalProcessPEOSubcategoryCode | SUBCATEGORY_CODE | — | — |
| 24 | ApprovalProcessPEOSubcategoryName | SUBCATEGORY_NAME | — | — |
| 25 | ApprovalProcessPEOTaskFileName | TASK_FILE_NAME | — | ✅ |
| 26 | ApprovalProcessPEOTxnModuleIdentifier | TXN_MODULE_IDENTIFIER | — | — |

---

## 📚 Referências

- [[ap-module-data-dictionary]] — Dossiê do módulo AP
