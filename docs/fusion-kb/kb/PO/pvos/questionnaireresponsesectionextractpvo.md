---
id: DOC-PO-PVO-QuestionnaireResponseSectionExtractPVO
doc_type: system-doc
title: "QuestionnaireResponseSectionExtractPVO — PVO Purchasing"
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
  - QuestionnaireResponseSectionExtractPVO
  - questionnaireresponsesectionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireResponseSectionExtractPVO

## 📌 Visão Geral

Extrai respostas por seção de questionários para carga BICC, com status de completude por área temática. Permite identificação de lacunas e seções pendentes de preenchimento.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireResponseSectionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_resp_sections|POQ_QUESTNAIRE_RESP_SECTIONS]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_resp_sections|POQ_QUESTNAIRE_RESP_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | QuestnaireRespHeaderId | QUESTNAIRE_RESP_HEADER_ID | — | ✅ |
| 8 | QuestnaireRespSectionId | QUESTNAIRE_RESP_SECTION_ID | 🔑 | ✅ |
| 9 | QuestnaireSectionId | QUESTNAIRE_SECTION_ID | — | ✅ |
| 10 | SectionCompletedFlag | SECTION_COMPLETED_FLAG | — | ✅ |
| 11 | SectionDisplayedFlag | SECTION_DISPLAYED_FLAG | — | ✅ |
| 12 | SectionGeneratedFlag | SECTION_GENERATED_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
