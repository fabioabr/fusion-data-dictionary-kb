---
id: DOC-OTHER-PVO-WorkCenterTranslationExtractPVO
doc_type: system-doc
title: "WorkCenterTranslationExtractPVO — PVO Cross-Module"
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
  - WorkCenterTranslationExtractPVO
  - workcentertranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkCenterTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Center Translation Extract. Acessa as tabelas: WIS_WORK_CENTERS_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.WorkCenterTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_work_centers_tl|WIS_WORK_CENTERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | SourceLang | SOURCE_LANG | — | ✅ |
| 9 | WorkCenterDescription | WORK_CENTER_DESCRIPTION | — | ✅ |
| 10 | WorkCenterId | WORK_CENTER_ID | 🔑 | ✅ |
| 11 | WorkCenterName | WORK_CENTER_NAME | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
