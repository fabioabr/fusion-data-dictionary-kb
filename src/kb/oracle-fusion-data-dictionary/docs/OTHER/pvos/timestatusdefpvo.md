---
id: DOC-OTHER-PVO-TimeStatusDefPVO
doc_type: system-doc
title: "TimeStatusDefPVO — PVO Cross-Module"
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
  - TimeStatusDefPVO
  - timestatusdefpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TimeStatusDefPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Time Status Def. Acessa as tabelas: HWM_TM_STATUS_DEF_B.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.StatusAM.TimeStatusDefPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 1 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hwm_tm_status_def_b|HWM_TM_STATUS_DEF_B]] — 21 atributos (1 PKs, 21 BICC)

---

## ⚙️ Atributos

### [[hwm_tm_status_def_b|HWM_TM_STATUS_DEF_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AllowableValues | ALLOWABLE_VALUES | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | Definitioncode | DEFINITIONCODE | — | ✅ |
| 5 | EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | FalseValue | FALSE_VALUE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ModuleId | MODULE_ID | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | RepositoryType | REPOSITORY_TYPE | — | ✅ |
| 13 | Scope | SCOPE | — | ✅ |
| 14 | StatusDefCd | STATUS_DEF_CD | — | ✅ |
| 15 | TimeConsumerSetId | TCSMRS_ID | — | ✅ |
| 16 | TimeStatusDefId | TM_STATUS_DEF_ID | 🔑 | ✅ |
| 17 | TimeStatusType | TM_STATUS_TYPE | — | ✅ |
| 18 | TrueValue | TRUE_VALUE | — | ✅ |
| 19 | ValueDerivedFlag | VALUE_DERIVED_FLAG | — | ✅ |
| 20 | ValueIfFalse | VALUE_IF_FALSE | — | ✅ |
| 21 | ValueIfTrue | VALUE_IF_TRUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
