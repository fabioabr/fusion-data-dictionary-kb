---
id: DOC-OTHER-PVO-ContractApprovalHistoryP1
doc_type: system-doc
title: "ContractApprovalHistoryP1 — PVO Cross-Module"
system: Oracle Fusion Cloud ERP
module: Cross-Module
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - other
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ContractApprovalHistoryP1
  - contractapprovalhistoryp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ContractApprovalHistoryP1

## 📌 Visão Geral

View Object para extração BICC de dados de Contract Approval History P1. Acessa as tabelas: OKC_K_APPROVAL_HISTORY_WF_V, OKC_K_HEADERS_ALL_B.

**Caminho:** `FscmTopModelAM.ContractsCoreAM.ContractApprovalHistoryP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 22 | 2 | 2 | 7 | 32% |

---

## 🔗 Tabelas Relacionadas

- [[okc_k_approval_history_wf_v|OKC_K_APPROVAL_HISTORY_WF_V]] — 19 atributos (2 PKs, 7 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 3 atributos

---

## ⚙️ Atributos

### [[okc_k_approval_history_wf_v|OKC_K_APPROVAL_HISTORY_WF_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Approvalhistdatesubmitted | APPROVALHISTDATESUBMITTED | — | ✅ |
| 2 | Approvalhistlastupdatedate | APPROVALHISTLASTUPDATEDATE | — | — |
| 3 | Approvalhistlastupdatedby | APPROVALHISTLASTUPDATEDBY | — | — |
| 4 | Approvalhistlastupdatelogin | APPROVALHISTLASTUPDATELOGIN | — | — |
| 5 | Approvalhistobjversionnum | APPROVALHISTOBJVERSIONNUM | — | — |
| 6 | Approvalhistorycreatedby | APPROVALHISTORYCREATEDBY | — | — |
| 7 | Approvalhistorycreationdate | APPROVALHISTORYCREATIONDATE | — | — |
| 8 | Approvalhistoryid | APPROVALHISTORYID | 🔑 | ✅ |
| 9 | Approvalhistorymajorversion | APPROVALHISTORYMAJORVERSION | 🔑 | ✅ |
| 10 | Approvalhistorytaskid | APPROVALHISTORYTASKID | — | — |
| 11 | Approvalhistoryversiontype | APPROVALHISTORYVERSIONTYPE | — | — |
| 12 | Wftaskassigneddate | WFTASKASSIGNEDDATE | — | ✅ |
| 13 | Wftaskassignees | WFTASKASSIGNEES | — | — |
| 14 | Wftaskassigneesdisplayname | WFTASKASSIGNEESDISPLAYNAME | — | ✅ |
| 15 | Wftaskenddate | WFTASKENDDATE | — | ✅ |
| 16 | Wftaskoutcome | WFTASKOUTCOME | — | ✅ |
| 17 | Wftaskstate | WFTASKSTATE | — | — |
| 18 | Wftasktaskid | WFTASKTASKID | — | — |
| 19 | Wftaskupdatedate | WFTASKUPDATEDATE | — | — |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderBasePEOId | ID | — | — |
| 2 | ContractHeaderBasePEOMajorVersion | MAJOR_VERSION | — | — |
| 3 | ContractHeaderBasePEOStsCode | STS_CODE | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
