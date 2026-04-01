---
id: DOC-OTHER-PVO-InvGradePVO
doc_type: system-doc
title: "InvGradePVO — PVO Cross-Module"
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
  - InvGradePVO
  - invgradepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InvGradePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Inv Grade. Acessa as tabelas: INV_GRADES_B, INV_GRADES_TL.

**Caminho:** `FscmTopModelAM.InventoryAM.InvGradePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 18 | 2 | 1 | 3 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[inv_grades_b|INV_GRADES_B]] — 8 atributos (1 PKs, 2 BICC)
- [[inv_grades_tl|INV_GRADES_TL]] — 10 atributos (1 BICC)

---

## ⚙️ Atributos

### [[inv_grades_b|INV_GRADES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GradeCode | GRADE_CODE | 🔑 | ✅ |
| 2 | InvGradeBPEOCreatedBy | CREATED_BY | — | — |
| 3 | InvGradeBPEOCreationDate | CREATION_DATE | — | — |
| 4 | InvGradeBPEODisableFlag | DISABLE_FLAG | — | — |
| 5 | InvGradeBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | InvGradeBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | InvGradeBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | InvGradeBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[inv_grades_tl|INV_GRADES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InvGradeTLPEOCreatedBy | CREATED_BY | — | — |
| 2 | InvGradeTLPEOCreationDate | CREATION_DATE | — | — |
| 3 | InvGradeTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | InvGradeTLPEOGradeCode | GRADE_CODE | — | — |
| 5 | InvGradeTLPEOLanguage | LANGUAGE | — | — |
| 6 | InvGradeTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | InvGradeTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | InvGradeTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | InvGradeTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | InvGradeTLPEOSourceLang | SOURCE_LANG | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
