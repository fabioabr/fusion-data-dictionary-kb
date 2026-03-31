---
id: DOC-OTHER-PVO-ProjectGateApproverTranslationExtractPVO
doc_type: system-doc
title: "ProjectGateApproverTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectGateApproverTranslationExtractPVO
  - projectgateapprovertranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectGateApproverTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Gate Approver Translation Extract. Acessa as tabelas: PJT_GATE_APPROVERS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectGateApproverTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[pjt_gate_approvers_tl|PJT_GATE_APPROVERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjtGateApproversTranslationPEOApprovalId | APPROVAL_ID | 🔑 | ✅ |
| 2 | PjtGateApproversTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | PjtGateApproversTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | PjtGateApproversTranslationPEODecisionComments | DECISION_COMMENTS | — | ✅ |
| 5 | PjtGateApproversTranslationPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 6 | PjtGateApproversTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | PjtGateApproversTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | PjtGateApproversTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | PjtGateApproversTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PjtGateApproversTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
