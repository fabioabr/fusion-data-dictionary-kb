---
id: DOC-PO-PVO-ActivityTypeExtractPVO
doc_type: system-doc
title: "ActivityTypeExtractPVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - ActivityTypeExtractPVO
  - activitytypeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ActivityTypeExtractPVO

## 📌 Visão Geral

Extrai os tipos de atividades configurados para rastreamento de sustentabilidade em compras (transporte, energia, resíduos). Define as categorias de monitoramento ambiental da cadeia de suprimentos.

**Caminho:** `FscmTopModelAM.PrcExtractAM.SusBiccExtractAM.ActivityTypeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 1 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[sus_activity_types|SUS_ACTIVITY_TYPES]] — 12 atributos (1 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[sus_activity_types|SUS_ACTIVITY_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActivityTypeCode | ACTIVITY_TYPE_CODE | — | ✅ |
| 2 | ActivityTypeId | ACTIVITY_TYPE_ID | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | EndDate | END_DATE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | ScopeCategoryCode | SCOPE_CATEGORY_CODE | — | ✅ |
| 11 | ScopeCode | SCOPE_CODE | — | ✅ |
| 12 | StartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
