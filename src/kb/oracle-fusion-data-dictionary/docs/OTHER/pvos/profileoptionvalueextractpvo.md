---
id: DOC-OTHER-PVO-ProfileOptionValueExtractPVO
doc_type: system-doc
title: "ProfileOptionValueExtractPVO — PVO Cross-Module"
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
  - ProfileOptionValueExtractPVO
  - profileoptionvalueextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProfileOptionValueExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Profile Option Value Extract. Acessa as tabelas: FND_PROFILE_OPTION_VALUES.

**Caminho:** `FscmTopModelAM.FinExtractAM.AnalyticsExtractServiceAM.ProfileOptionValueExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 10 | 1 | 4 | 10 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_profile_option_values|FND_PROFILE_OPTION_VALUES]] — 10 atributos (4 PKs, 10 BICC)

---

## ⚙️ Atributos

### [[fnd_profile_option_values|FND_PROFILE_OPTION_VALUES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApplicationId | APPLICATION_ID | 🔑 | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | LevelName | LEVEL_NAME | 🔑 | ✅ |
| 8 | LevelValue | LEVEL_VALUE | 🔑 | ✅ |
| 9 | ProfileOptionId | PROFILE_OPTION_ID | 🔑 | ✅ |
| 10 | ProfileOptionValue | PROFILE_OPTION_VALUE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
