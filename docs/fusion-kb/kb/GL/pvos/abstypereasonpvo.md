---
id: DOC-GL-PVO-AbsTypeReasonPVO
doc_type: system-doc
title: "AbsTypeReasonPVO — PVO General Ledger"
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
  - AbsTypeReasonPVO
  - abstypereasonpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbsTypeReasonPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abs Type Reason. Acessa as tabelas: ANC_ABSENCE_TYPE_REASONS_F.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.GlobalAbsencesAM.AbsTypeReasonPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 2 | 8 | 53% |

---

## 🔗 Tabelas Relacionadas

- [[anc_absence_type_reasons_f|ANC_ABSENCE_TYPE_REASONS_F]] — 15 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[anc_absence_type_reasons_f|ANC_ABSENCE_TYPE_REASONS_F]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbsenceReasonId | ABSENCE_REASON_ID | — | ✅ |
| 2 | AbsenceTypeId | ABSENCE_TYPE_ID | — | ✅ |
| 3 | AbsenceTypeReasonId | ABSENCE_TYPE_REASON_ID | 🔑 | ✅ |
| 4 | CreatedBy | CREATED_BY | — | — |
| 5 | CreationDate | CREATION_DATE | — | — |
| 6 | DefaultFlag | DEFAULT_FLAG | — | ✅ |
| 7 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 8 | EffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 9 | EnterpriseId | ENTERPRISE_ID | — | — |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | LinkageReasonFlag | LINKAGE_REASON_FLAG | — | ✅ |
| 14 | ModuleId | MODULE_ID | — | — |
| 15 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
