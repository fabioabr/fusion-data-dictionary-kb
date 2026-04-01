---
id: DOC-OTHER-PVO-ProjectGateApproverExtractPVO
doc_type: system-doc
title: "ProjectGateApproverExtractPVO — PVO Cross-Module"
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
  - ProjectGateApproverExtractPVO
  - projectgateapproverextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectGateApproverExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Gate Approver Extract. Acessa as tabelas: PJT_GATE_APPROVERS_B, PJT_GATE_APPROVERS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectGateApproverExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 2 | 1 | 24 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_gate_approvers_b|PJT_GATE_APPROVERS_B]] — 14 atributos (1 PKs, 14 BICC)
- [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]] — 10 atributos (10 BICC)

---

## ⚙️ Atributos

### [[pjt_gate_approvers_b|PJT_GATE_APPROVERS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtGateApproversBasePEOApprovalDecisionDate | APPROVAL_DECISION_DATE | — | ✅ |
| 2 | PjtGateApproversBasePEOApprovalId | APPROVAL_ID | 🔑 | ✅ |
| 3 | PjtGateApproversBasePEOApprovalInitDate | APPROVAL_INIT_DATE | — | ✅ |
| 4 | PjtGateApproversBasePEOApprovalResourceId | APPROVAL_RESOURCE_ID | — | ✅ |
| 5 | PjtGateApproversBasePEOApprovalStatus | APPROVAL_STATUS | — | ✅ |
| 6 | PjtGateApproversBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 7 | PjtGateApproversBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 8 | PjtGateApproversBasePEOGateElementId | GATE_ELEMENT_ID | — | ✅ |
| 9 | PjtGateApproversBasePEOLastReviewedById | LAST_REVIEWED_BY_ID | — | ✅ |
| 10 | PjtGateApproversBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | PjtGateApproversBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | PjtGateApproversBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | PjtGateApproversBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | PjtGateApproversBasePEOProjectId | PROJECT_ID | — | ✅ |

### [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtGateApproversTranslationPEOApprovalId | APPROVAL_ID | — | ✅ |
| 2 | PjtGateApproversTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PjtGateApproversTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PjtGateApproversTranslationPEODecisionComments | DECISION_COMMENTS | — | ✅ |
| 5 | PjtGateApproversTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 6 | PjtGateApproversTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PjtGateApproversTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PjtGateApproversTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PjtGateApproversTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PjtGateApproversTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
