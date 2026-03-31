---
id: DOC-OTHER-PVO-PjtGateApproverP1
doc_type: system-doc
title: "PjtGateApproverP1 — PVO Cross-Module"
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
  - PjtGateApproverP1
  - pjtgateapproverp1
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PjtGateApproverP1

## 📌 Visão Geral

View Object para extração BICC de dados de Pjt Gate Approver P1. Acessa as tabelas: PJT_GATE_APPROVERS_B, PJT_GATE_APPROVERS_TL, PJT_PRJ_ENTERPRISE_RESOURCE_B (+1).

**Caminho:** `FscmTopModelAM.PjtProjectPlanAM.PjtGateApproverP1`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 25 | 4 | 1 | 14 | 56% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_gate_approvers_b|PJT_GATE_APPROVERS_B]] — 12 atributos (1 PKs, 9 BICC)
- [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]] — 3 atributos (1 BICC)
- [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]] — 4 atributos (2 BICC)
- [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]] — 6 atributos (2 BICC)

---

## ⚙️ Atributos

### [[pjt_gate_approvers_b|PJT_GATE_APPROVERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtGateApproversBasePEOApprovalID | APPROVAL_ID | 🔑 | ✅ |
| 2 | PjtGateApproversBasePEOApprovalInitDate | APPROVAL_INIT_DATE | — | ✅ |
| 3 | PjtGateApproversBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 4 | PjtGateApproversBasePEOApproverID | APPROVAL_RESOURCE_ID | — | — |
| 5 | PjtGateApproversBasePEOApproverUpdatedDate | APPROVAL_DECISION_DATE | — | ✅ |
| 6 | PjtGateApproversBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PjtGateApproversBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PjtGateApproversBasePEOGateElementID | GATE_ELEMENT_ID | — | ✅ |
| 9 | PjtGateApproversBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | PjtGateApproversBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | PjtGateApproversBasePEOProjectID | PROJECT_ID | — | — |
| 12 | PjtGateApproversBasePEOReviewerID | LAST_REVIEWED_BY_ID | — | — |

### [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalId | APPROVAL_ID | — | — |
| 2 | Language | LANGUAGE | — | — |
| 3 | PjtGateApproversTranslationPEOApproverComments | DECISION_COMMENTS | — | ✅ |

### [[pjt_prj_enterprise_resource_b|PJT_PRJ_ENTERPRISE_RESOURCE_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceBasePEO1ReviewerEmail | EMAIL | — | ✅ |
| 2 | PrjEnterpriseResourceBasePEOApproverEmail | EMAIL | — | ✅ |
| 3 | PrjEnterpriseResourceBasePEOResourceId | RESOURCE_ID | — | — |
| 4 | ResourceId | RESOURCE_ID | — | — |

### [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceTransla1Language | LANGUAGE | — | — |
| 2 | PrjEnterpriseResourceTransla1ResourceId | RESOURCE_ID | — | — |
| 3 | PrjEnterpriseResourceTransla2Language | LANGUAGE | — | — |
| 4 | PrjEnterpriseResourceTransla2ResourceId | RESOURCE_ID | — | — |
| 5 | PrjEnterpriseResourceTranslationPEOApproverName | DISPLAY_NAME | — | ✅ |
| 6 | PrjEnterpriseResourceTranslationPEOP1ReviewerName | DISPLAY_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
