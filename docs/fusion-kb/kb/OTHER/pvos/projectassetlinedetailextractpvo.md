---
id: DOC-OTHER-PVO-ProjectAssetLineDetailExtractPVO
doc_type: system-doc
title: "ProjectAssetLineDetailExtractPVO — PVO Cross-Module"
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
  - ProjectAssetLineDetailExtractPVO
  - projectassetlinedetailextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectAssetLineDetailExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Asset Line Detail Extract. Acessa as tabelas: PJC_PRJ_ASSET_LN_DETS.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjcBiccExtractAM.ProjectAssetLineDetailExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjc_prj_asset_ln_dets|PJC_PRJ_ASSET_LN_DETS]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[pjc_prj_asset_ln_dets|PJC_PRJ_ASSET_LN_DETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PjcPrjAssetLnDetsCipCost | CIP_COST | — | ✅ |
| 2 | PjcPrjAssetLnDetsCreatedBy | CREATED_BY | — | ✅ |
| 3 | PjcPrjAssetLnDetsCreationDate | CREATION_DATE | — | ✅ |
| 4 | PjcPrjAssetLnDetsExpenditureItemId | EXPENDITURE_ITEM_ID | — | ✅ |
| 5 | PjcPrjAssetLnDetsJobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 6 | PjcPrjAssetLnDetsJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 7 | PjcPrjAssetLnDetsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PjcPrjAssetLnDetsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PjcPrjAssetLnDetsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PjcPrjAssetLnDetsLineNum | LINE_NUM | — | ✅ |
| 11 | PjcPrjAssetLnDetsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PjcPrjAssetLnDetsProjAssetLineDtlUniqId | PROJ_ASSET_LINE_DTL_UNIQ_ID | 🔑 | ✅ |
| 13 | PjcPrjAssetLnDetsProjectAssetLineDetailId | PROJECT_ASSET_LINE_DETAIL_ID | — | ✅ |
| 14 | PjcPrjAssetLnDetsRequestId | REQUEST_ID | — | ✅ |
| 15 | PjcPrjAssetLnDetsReversedFlag | REVERSED_FLAG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
