---
id: DOC-PO-PVO-QuestionnaireExtractPVO
doc_type: system-doc
title: "QuestionnaireExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - QuestionnaireExtractPVO
  - questionnaireextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireExtractPVO

## 📌 Visão Geral

Extrai questionários completos de qualificação para carga BICC, com estrutura de seções, perguntas e critérios. Alimenta análises de completude e eficácia dos instrumentos de avaliação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 19 | 1 | 1 | 18 | 95% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaires_vl|POQ_QUESTNAIRES_VL]] — 19 atributos (1 PKs, 18 BICC)

---

## ⚙️ Atributos

### [[poq_questnaires_vl|POQ_QUESTNAIRES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AutoCreateQualFlag | AUTO_CREATE_QUAL_FLAG | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DueDate | DUE_DATE | — | ✅ |
| 5 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 6 | Introduction | INTRODUCTION | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PrcBuId | PRC_BU_ID | — | ✅ |
| 12 | QuestnaireCustom | QUESTNAIRE_CUSTOM | — | ✅ |
| 13 | QuestnaireId | QUESTNAIRE_ID | 🔑 | ✅ |
| 14 | QuestnaireStatus | QUESTNAIRE_STATUS | — | ✅ |
| 15 | QuestnaireTitle | QUESTNAIRE_TITLE | — | ✅ |
| 16 | QuestnaireType | QUESTNAIRE_TYPE | — | ✅ |
| 17 | QuestnaireUsageCode | QUESTNAIRE_USAGE_CODE | — | — |
| 18 | SupplierRegId | SUPPLIER_REG_ID | — | ✅ |
| 19 | UseQuestionBranchFlag | USE_QUESTION_BRANCH_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
