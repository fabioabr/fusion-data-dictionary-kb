---
id: DOC-OTHER-PVO-EffectivePricePeriodPVO
doc_type: system-doc
title: "EffectivePricePeriodPVO — PVO Cross-Module"
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
  - EffectivePricePeriodPVO
  - effectivepriceperiodpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# EffectivePricePeriodPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Effective Price Period. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, VRM_PRICE_EFF_PERIODS_B (+1).

**Caminho:** `FscmTopModelAM.FinVrmShrdSetupPublicModelAM.EffectivePricePeriodPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 40 | 4 | 3 | 12 | 30% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 10 atributos
- [[vrm_price_eff_periods_b|VRM_PRICE_EFF_PERIODS_B]] — 10 atributos (1 PKs, 8 BICC)
- [[vrm_price_eff_periods_tl|VRM_PRICE_EFF_PERIODS_TL]] — 10 atributos (2 PKs, 4 BICC)

---

## ⚙️ Atributos

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PersonCreatedByDisplayName | DISPLAY_NAME | — | — |
| 2 | PersonCreatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PersonCreatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PersonCreatedByPersonId | PERSON_ID | — | — |
| 5 | PersonCreatedByPersonNameId | PERSON_NAME_ID | — | — |
| 6 | PersonUpdatedByDisplayName | DISPLAY_NAME | — | — |
| 7 | PersonUpdatedByEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 8 | PersonUpdatedByEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 9 | PersonUpdatedByPersonId | PERSON_ID | — | — |
| 10 | PersonUpdatedByPersonNameId | PERSON_NAME_ID | — | — |

### [[per_users|PER_USERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | UserCreatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 2 | UserCreatedByPersonId | PERSON_ID | — | — |
| 3 | UserCreatedByUserGuid | USER_GUID | — | — |
| 4 | UserCreatedByUserId | USER_ID | — | — |
| 5 | UserCreatedByUsername | USERNAME | — | — |
| 6 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 7 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 8 | UserUpdatedByUserGuid | USER_GUID | — | — |
| 9 | UserUpdatedByUserId | USER_ID | — | — |
| 10 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_price_eff_periods_b|VRM_PRICE_EFF_PERIODS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectivePeriodBaseCreatedBy1 | CREATED_BY | — | ✅ |
| 2 | EffectivePeriodBaseCreationDate | CREATION_DATE | — | ✅ |
| 3 | EffectivePeriodBaseEndDate | END_DATE | — | ✅ |
| 4 | EffectivePeriodBaseInUse | IN_USE | — | ✅ |
| 5 | EffectivePeriodBaseLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | EffectivePeriodBaseLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | EffectivePeriodBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 8 | EffectivePeriodBaseObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | EffectivePeriodBaseStartDate | START_DATE | — | ✅ |
| 10 | PriceEffPeriodId | PRICE_EFF_PERIOD_ID | 🔑 | ✅ |

### [[vrm_price_eff_periods_tl|VRM_PRICE_EFF_PERIODS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | EffectivePeriodTranslationCreatedBy | CREATED_BY | — | — |
| 2 | EffectivePeriodTranslationCreationDate | CREATION_DATE | — | — |
| 3 | EffectivePeriodTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | EffectivePeriodTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 5 | EffectivePeriodTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 6 | EffectivePeriodTranslationName | NAME | — | ✅ |
| 7 | EffectivePeriodTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | EffectivePeriodTranslationPriceEffPeriodId | PRICE_EFF_PERIOD_ID | 🔑 | ✅ |
| 9 | EffectivePeriodTranslationSourceLang | SOURCE_LANG | — | — |
| 10 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
