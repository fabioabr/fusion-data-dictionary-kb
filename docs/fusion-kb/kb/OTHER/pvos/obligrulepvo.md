---
id: DOC-OTHER-PVO-ObligRulePVO
doc_type: system-doc
title: "ObligRulePVO — PVO Cross-Module"
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
  - ObligRulePVO
  - obligrulepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ObligRulePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Oblig Rule. Acessa as tabelas: PER_PERSON_NAMES_F_V, PER_USERS, VRM_PERF_OBLIG_GRP_RULES_B (+1).

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ObligRulePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 75 | 4 | 2 | 16 | 21% |

---

## 🔗 Tabelas Relacionadas

- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 10 atributos
- [[per_users|PER_USERS]] — 8 atributos
- [[vrm_perf_oblig_grp_rules_b|VRM_PERF_OBLIG_GRP_RULES_B]] — 46 atributos (11 BICC)
- [[vrm_perf_oblig_grp_rules_tl|VRM_PERF_OBLIG_GRP_RULES_TL]] — 11 atributos (2 PKs, 5 BICC)

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
| 3 | UserCreatedByUserId | USER_ID | — | — |
| 4 | UserCreatedByUsername | USERNAME | — | — |
| 5 | UserUpdatedByObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 6 | UserUpdatedByPersonId | PERSON_ID | — | — |
| 7 | UserUpdatedByUserId | USER_ID | — | — |
| 8 | UserUpdatedByUsername | USERNAME | — | — |

### [[vrm_perf_oblig_grp_rules_b|VRM_PERF_OBLIG_GRP_RULES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObligRuleBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ObligRuleBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ObligRuleBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ObligRuleBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ObligRuleBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ObligRuleBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ObligRuleBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ObligRuleBaseAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ObligRuleBaseAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ObligRuleBaseAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ObligRuleBaseAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ObligRuleBaseAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ObligRuleBaseAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ObligRuleBaseAttribute3 | ATTRIBUTE3 | — | — |
| 15 | ObligRuleBaseAttribute4 | ATTRIBUTE4 | — | — |
| 16 | ObligRuleBaseAttribute5 | ATTRIBUTE5 | — | — |
| 17 | ObligRuleBaseAttribute6 | ATTRIBUTE6 | — | — |
| 18 | ObligRuleBaseAttribute7 | ATTRIBUTE7 | — | — |
| 19 | ObligRuleBaseAttribute8 | ATTRIBUTE8 | — | — |
| 20 | ObligRuleBaseAttribute9 | ATTRIBUTE9 | — | — |
| 21 | ObligRuleBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | ObligRuleBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | ObligRuleBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | ObligRuleBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | ObligRuleBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | ObligRuleBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | ObligRuleBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | ObligRuleBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | ObligRuleBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | ObligRuleBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | ObligRuleBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | ObligRuleBaseClassificationCode | CLASSIFICATION_CODE | — | ✅ |
| 33 | ObligRuleBaseCreatedBy1 | CREATED_BY | — | ✅ |
| 34 | ObligRuleBaseCreatedFrom | CREATED_FROM | — | — |
| 35 | ObligRuleBaseCreationDate1 | CREATION_DATE | — | ✅ |
| 36 | ObligRuleBaseDevolvePoFlag | DEVOLVE_PO_FLAG | — | ✅ |
| 37 | ObligRuleBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 38 | ObligRuleBaseExemptedFromAllocationFlag | EXEMPTED_FROM_ALLOCATION_FLAG | — | ✅ |
| 39 | ObligRuleBaseInUseFlag | IN_USE_FLAG | — | ✅ |
| 40 | ObligRuleBaseLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 41 | ObligRuleBaseLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 42 | ObligRuleBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | ✅ |
| 43 | ObligRuleBaseObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 44 | ObligRuleBasePerfObligationGroupRuleId1 | PERF_OBLIGATION_GROUP_RULE_ID | — | — |
| 45 | ObligRuleBasePriority | PRIORITY | — | ✅ |
| 46 | ObligRuleBaseSatisfactionMethod | SATISFACTION_METHOD | — | ✅ |

### [[vrm_perf_oblig_grp_rules_tl|VRM_PERF_OBLIG_GRP_RULES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ObligRuleTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ObligRuleTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ObligRuleTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | ObligRuleTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ObligRuleTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ObligRuleTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObligRuleTranslationName | NAME | — | ✅ |
| 9 | ObligRuleTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ObligRuleTranslationSourceLang | SOURCE_LANG | — | — |
| 11 | PerfObligationGroupRuleId | PERF_OBLIGATION_GROUP_RULE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
