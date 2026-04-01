---
id: DOC-OTHER-PVO-MntWorkRequirementTranslationExtractPVO
doc_type: system-doc
title: "MntWorkRequirementTranslationExtractPVO — PVO Cross-Module"
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
  - MntWorkRequirementTranslationExtractPVO
  - mntworkrequirementtranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# MntWorkRequirementTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Mnt Work Requirement Translation Extract. Acessa as tabelas: MNT_WORK_REQUIREMENTS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.MntWorkRequirementTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 2 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]] — 10 atributos (2 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[mnt_work_requirements_tl|MNT_WORK_REQUIREMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 9 | RequirementName | REQUIREMENT_NAME | — | ✅ |
| 10 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
