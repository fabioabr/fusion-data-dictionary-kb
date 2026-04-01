---
id: DOC-GL-PVO-BalanceTypeTranslation
doc_type: system-doc
title: "BalanceTypeTranslation — PVO General Ledger"
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
  - BalanceTypeTranslation
  - balancetypetranslation
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# BalanceTypeTranslation

## 📌 Visão Geral

View Object para extração BICC de dados de Balance Type Translation. Acessa as tabelas: PAY_BALANCE_TYPES_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmPayBalanceAM.BalanceTypeTranslation`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 8 | 73% |

---

## 🔗 Tabelas Relacionadas

- [[pay_balance_types_tl|PAY_BALANCE_TYPES_TL]] — 11 atributos (2 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[pay_balance_types_tl|PAY_BALANCE_TYPES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BalanceTypeId | BALANCE_TYPE_ID | 🔑 | ✅ |
| 2 | BalanceTypeTranslationPEOBalanceName | BALANCE_NAME | — | ✅ |
| 3 | BalanceTypeTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | BalanceTypeTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | BalanceTypeTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | BalanceTypeTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | BalanceTypeTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | BalanceTypeTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | BalanceTypeTranslationPEOReportingName | REPORTING_NAME | — | — |
| 10 | BalanceTypeTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
