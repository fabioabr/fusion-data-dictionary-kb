---
id: DOC-OTHER-PVO-ProjCostCollExclusionsExtractPVO
doc_type: system-doc
title: "ProjCostCollExclusionsExtractPVO — PVO Cross-Module"
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
  - ProjCostCollExclusionsExtractPVO
  - projcostcollexclusionsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjCostCollExclusionsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Proj Cost Coll Exclusions Extract. Acessa as tabelas: RCS_PROJ_COST_COLL_EXCLUSIONS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.ScmRcsBiccExtractAM.ProjCostCollExclusionsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 8 | 1 | 1 | 8 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[rcs_proj_cost_coll_exclusions|RCS_PROJ_COST_COLL_EXCLUSIONS]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[rcs_proj_cost_coll_exclusions|RCS_PROJ_COST_COLL_EXCLUSIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | ProjectTypeId | PROJECT_TYPE_ID | — | ✅ |
| 8 | ScmCostCollExclusionId | SCM_COST_COLL_EXCLUSION_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
