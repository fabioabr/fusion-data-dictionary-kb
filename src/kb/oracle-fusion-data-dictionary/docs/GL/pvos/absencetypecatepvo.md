---
id: DOC-GL-PVO-AbsenceTypeCatePVO
doc_type: system-doc
title: "AbsenceTypeCatePVO — PVO General Ledger"
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
  - AbsenceTypeCatePVO
  - absencetypecatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceTypeCatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence Type Cate. Acessa as tabelas: ANC_ABSENCE_TYPE_CATE_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsenceTypeCatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 3 | 4 | 29% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_type_cate_f|ANC_ABSENCE_TYPE_CATE_F]] — 14 atributos (3 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[anc_absence_type_cate_f|ANC_ABSENCE_TYPE_CATE_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceCategoryId | ABSENCE_CATEGORY_ID | — | — |
| 2 | AbsenceTypeCateId | ABSENCE_TYPE_CATE_ID | 🔑 | ✅ |
| 3 | AbsenceTypeId | ABSENCE_TYPE_ID | — | — |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | EffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 7 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 8 | EnterpriseId | ENTERPRISE_ID | — | — |
| 9 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ModuleId | MODULE_ID | — | — |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | Status | STATUS | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
