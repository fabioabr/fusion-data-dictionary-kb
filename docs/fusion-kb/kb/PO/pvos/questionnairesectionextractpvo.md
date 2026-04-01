---
id: DOC-PO-PVO-QuestionnaireSectionExtractPVO
doc_type: system-doc
title: "QuestionnaireSectionExtractPVO — PVO Purchasing"
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
  - QuestionnaireSectionExtractPVO
  - questionnairesectionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QuestionnaireSectionExtractPVO

## 📌 Visão Geral

Extrai as seções de questionários de qualificação para carga BICC, organizando perguntas em grupos temáticos. Suporta análise de estrutura e cobertura dos instrumentos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QuestionnaireSectionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_questnaire_sections_vl|POQ_QUESTNAIRE_SECTIONS_VL]] — 11 atributos (1 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[poq_questnaire_sections_vl|POQ_QUESTNAIRE_SECTIONS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | Instructions | INSTRUCTIONS | — | ✅ |
| 5 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | QuestnaireId | QUESTNAIRE_ID | — | ✅ |
| 10 | QuestnaireSectionId | QUESTNAIRE_SECTION_ID | 🔑 | ✅ |
| 11 | SectionName | SECTION_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
