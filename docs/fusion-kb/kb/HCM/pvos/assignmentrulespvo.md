---
id: DOC-HCM-PVO-AssignmentRulesPVO
doc_type: system-doc
title: "AssignmentRulesPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AssignmentRulesPVO
  - assignmentrulespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AssignmentRulesPVO

## 📌 Visão Geral

Extrai regras de atribuicao de conteudo de aprendizagem (Learning) com habilitacao dinamica. Suporta automacao de assignment de treinamentos.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.ContentAM.AssignmentRulesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 24 | 1 | 1 | 14 | 58% |

---

## 🔗 Tabelas Relacionadas

- [[wlf_assignment_rules|WLF_ASSIGNMENT_RULES]] — 24 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[wlf_assignment_rules|WLF_ASSIGNMENT_RULES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssignmentRulePEOAssignmentRuleId | ASSIGNMENT_RULE_ID | 🔑 | ✅ |
| 2 | AssignmentRulePEOCreatedBy | CREATED_BY | — | — |
| 3 | AssignmentRulePEOCreationDate | CREATION_DATE | — | — |
| 4 | AssignmentRulePEODynDueDate | DYN_DUE_DATE | — | — |
| 5 | AssignmentRulePEODynDueDateOption | DYN_DUE_DATE_OPTION | — | — |
| 6 | AssignmentRulePEODynDueInDays | DYN_DUE_IN_DAYS | — | — |
| 7 | AssignmentRulePEODynEnabled | DYN_ENABLED | — | ✅ |
| 8 | AssignmentRulePEODynStopNewDate | DYN_STOP_NEW_DATE | — | — |
| 9 | AssignmentRulePEODynStopWithdrawDate | DYN_STOP_WITHDRAW_DATE | — | — |
| 10 | AssignmentRulePEODynWithdrawOption | DYN_WITHDRAW_OPTION | — | ✅ |
| 11 | AssignmentRulePEOExpiryDate | EXPIRY_DATE | — | ✅ |
| 12 | AssignmentRulePEOExpiryInDays | EXPIRY_IN_DAYS | — | ✅ |
| 13 | AssignmentRulePEOExpiryInNumYrs | EXPIRY_IN_NUM_YRS | — | ✅ |
| 14 | AssignmentRulePEOExpiryOption | EXPIRY_OPTION | — | ✅ |
| 15 | AssignmentRulePEOInitialDueDate | INITIAL_DUE_DATE | — | ✅ |
| 16 | AssignmentRulePEOInitialDueDateOption | INITIAL_DUE_DATE_OPTION | — | — |
| 17 | AssignmentRulePEOInitialDueInDays | INITIAL_DUE_IN_DAYS | — | ✅ |
| 18 | AssignmentRulePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | AssignmentRulePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 20 | AssignmentRulePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 21 | AssignmentRulePEOLearningItemEffectivity | LEARNING_ITEM_EFFECTIVITY | — | ✅ |
| 22 | AssignmentRulePEORenewalBeforeExpiryDays | RENEWAL_BEFORE_EXPIRY_DAYS | — | ✅ |
| 23 | AssignmentRulePEORenewalOptions | RENEWAL_OPTIONS | — | ✅ |
| 24 | AssignmentRulePEOValidityOption | VALIDITY_OPTION | — | ✅ |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
