---
id: DOC-OTHER-PVO-CstRollupGroupDetailsExtractPVO
doc_type: system-doc
title: "CstRollupGroupDetailsExtractPVO — PVO Cross-Module"
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
  - CstRollupGroupDetailsExtractPVO
  - cstrollupgroupdetailsextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CstRollupGroupDetailsExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Cst Rollup Group Details Extract. Acessa as tabelas: CST_ROLLUP_GROUPS, CST_ROLLUP_GROUP_DTLS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.CstBiccExtractAM.CstRollupGroupDetailsExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 2 | 1 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[cst_rollup_groups|CST_ROLLUP_GROUPS]] — 3 atributos (3 BICC)
- [[cst_rollup_group_dtls|CST_ROLLUP_GROUP_DTLS]] — 8 atributos (1 PKs, 8 BICC)

---

## ⚙️ Atributos

### [[cst_rollup_groups|CST_ROLLUP_GROUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstRollupGroupsPEORollupGroupDesc | ROLLUP_GROUP_DESC | — | ✅ |
| 2 | CstRollupGroupsPEORollupGroupId | ROLLUP_GROUP_ID | — | ✅ |
| 3 | CstRollupGroupsPEORollupGroupName | ROLLUP_GROUP_NAME | — | ✅ |

### [[cst_rollup_group_dtls|CST_ROLLUP_GROUP_DTLS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CstRollupGroupDetailsPEOCostBookId | COST_BOOK_ID | — | ✅ |
| 2 | CstRollupGroupDetailsPEOCostOrgId | COST_ORG_ID | — | ✅ |
| 3 | CstRollupGroupDetailsPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | CstRollupGroupDetailsPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | CstRollupGroupDetailsPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | CstRollupGroupDetailsPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | CstRollupGroupDetailsPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | CstRollupGroupDetailsPEORollupGroupDtlId | ROLLUP_GROUP_DTL_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
