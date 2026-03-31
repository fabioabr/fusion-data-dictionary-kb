---
id: DOC-GL-PVO-TimeStatusDefTranslationPVO
doc_type: system-doc
title: "TimeStatusDefTranslationPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - TimeStatusDefTranslationPVO
  - timestatusdeftranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeStatusDefTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Status Def Translation. Acessa as tabelas: HWM_TM_STATUS_DEF_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.StatusAM.TimeStatusDefTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 3 | 25% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_status_def_tl|HWM_TM_STATUS_DEF_TL]] — 12 atributos (2 PKs, 3 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_status_def_tl|HWM_TM_STATUS_DEF_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | — |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Description | DESCRIPTION | — | — |
| 4 | EnterpriseId | ENTERPRISE_ID | — | — |
| 5 | Language | LANGUAGE | 🔑 | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SourceLang | SOURCE_LANG | — | — |
| 11 | TimeStatusDefId | TM_STATUS_DEF_ID | 🔑 | ✅ |
| 12 | TimeStatusName | TM_STATUS_NAME | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
