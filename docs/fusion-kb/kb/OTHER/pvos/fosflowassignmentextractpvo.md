---
id: DOC-OTHER-PVO-FosFlowAssignmentExtractPVO
doc_type: system-doc
title: "FosFlowAssignmentExtractPVO — PVO Cross-Module"
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
  - FosFlowAssignmentExtractPVO
  - fosflowassignmentextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosFlowAssignmentExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Flow Assignment Extract. Acessa as tabelas: FOS_DOC_FLOW_ASSIGNMENT.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosFlowAssignmentExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 1 | 1 | 18 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_doc_flow_assignment|FOS_DOC_FLOW_ASSIGNMENT]] — 18 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[fos_doc_flow_assignment|FOS_DOC_FLOW_ASSIGNMENT]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | FlowAssignmentPEOActivationDate | ACTIVATION_DATE | — | ✅ |
| 2 | FlowAssignmentPEOAgreementPtrId | AGREEMENT_PTR_ID | — | ✅ |
| 3 | FlowAssignmentPEOAgreementType | AGREEMENT_TYPE | — | ✅ |
| 4 | FlowAssignmentPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | FlowAssignmentPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | FlowAssignmentPEODocumentFlowAssignmentId | DOCUMENT_FLOW_ASSIGNMENT_ID | 🔑 | ✅ |
| 7 | FlowAssignmentPEODocumentType | DOCUMENT_TYPE | — | ✅ |
| 8 | FlowAssignmentPEODropShipFlag | DROP_SHIP_FLAG | — | ✅ |
| 9 | FlowAssignmentPEOEffectiveDocumentDate | EFFECTIVE_DOCUMENT_DATE | — | ✅ |
| 10 | FlowAssignmentPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 11 | FlowAssignmentPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | FlowAssignmentPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 13 | FlowAssignmentPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 14 | FlowAssignmentPEOLinkToDocumentId | LINK_TO_DOCUMENT_ID | — | ✅ |
| 15 | FlowAssignmentPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 16 | FlowAssignmentPEOSourceDocumentId | SOURCE_DOCUMENT_ID | — | ✅ |
| 17 | FlowAssignmentPEOStatus | STATUS | — | ✅ |
| 18 | FlowAssignmentPEOSystemId | SYSTEM_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
