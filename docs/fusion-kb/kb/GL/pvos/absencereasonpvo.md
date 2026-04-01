---
id: DOC-GL-PVO-AbsenceReasonPVO
doc_type: system-doc
title: "AbsenceReasonPVO — PVO General Ledger"
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
  - AbsenceReasonPVO
  - absencereasonpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsenceReasonPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Absence Reason. Acessa as tabelas: ANC_ABSENCE_REASONS_F, ANC_ABSENCE_REASONS_F_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsenceReasonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 29 | 2 | 5 | 22 | 76% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_reasons_f|ANC_ABSENCE_REASONS_F]] — 14 atributos (2 PKs, 11 BICC)
- [[anc_absence_reasons_f_tl|ANC_ABSENCE_REASONS_F_TL]] — 15 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[anc_absence_reasons_f|ANC_ABSENCE_REASONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceReasonId | ABSENCE_REASON_ID | 🔑 | ✅ |
| 2 | AncAbsReasonsFAltcd | ANC_ABS_REASONS_F_ALTCD | — | — |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | LegislationCode | LEGISLATION_CODE | — | ✅ |
| 12 | ModuleId | MODULE_ID | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | Status | STATUS | — | ✅ |

### [[anc_absence_reasons_f_tl|ANC_ABSENCE_REASONS_F_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceReasonId1 | ABSENCE_REASON_ID | 🔑 | ✅ |
| 2 | CreatedBy1 | CREATED_BY | — | ✅ |
| 3 | CreationDate1 | CREATION_DATE | — | ✅ |
| 4 | Description | DESCRIPTION | — | ✅ |
| 5 | EffectiveEndDate1 | EFFECTIVE_END_DATE | — | ✅ |
| 6 | EffectiveStartDate1 | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | EnterpriseId1 | ENTERPRISE_ID | — | — |
| 8 | Language | LANGUAGE | 🔑 | ✅ |
| 9 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 10 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 11 | LastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 12 | ModuleId1 | MODULE_ID | — | — |
| 13 | Name | NAME | — | ✅ |
| 14 | ObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 15 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
