---
id: DOC-OTHER-PVO-GroupRuleUsageExtractPVO
doc_type: system-doc
title: "GroupRuleUsageExtractPVO — PVO Cross-Module"
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
  - GroupRuleUsageExtractPVO
  - groupruleusageextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# GroupRuleUsageExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Group Rule Usage Extract. Acessa as tabelas: CSE_GROUP_RULE_USAGES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CseBiccExtractAM.GroupRuleUsageExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cse_group_rule_usages|CSE_GROUP_RULE_USAGES]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[cse_group_rule_usages|CSE_GROUP_RULE_USAGES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | RuleId | RULE_ID | — | ✅ |
| 8 | RuleUsageId | RULE_USAGE_ID | 🔑 | ✅ |
| 9 | UsageCode | USAGE_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
