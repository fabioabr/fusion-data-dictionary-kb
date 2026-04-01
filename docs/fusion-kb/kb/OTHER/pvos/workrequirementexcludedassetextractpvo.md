---
id: DOC-OTHER-PVO-WorkRequirementExcludedAssetExtractPVO
doc_type: system-doc
title: "WorkRequirementExcludedAssetExtractPVO — PVO Cross-Module"
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
  - WorkRequirementExcludedAssetExtractPVO
  - workrequirementexcludedassetextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WorkRequirementExcludedAssetExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Work Requirement Excluded Asset Extract. Acessa as tabelas: MNT_WR_EXCLUDED_ASSETS.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.WorkRequirementExcludedAssetExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_wr_excluded_assets|MNT_WR_EXCLUDED_ASSETS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[mnt_wr_excluded_assets|MNT_WR_EXCLUDED_ASSETS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssetId | ASSET_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | ExclusionId | EXCLUSION_ID | 🔑 | ✅ |
| 5 | ItemId | ITEM_ID | — | ✅ |
| 6 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 7 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 8 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 10 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 13 | RequestId | REQUEST_ID | — | ✅ |
| 14 | RequirementId | REQUIREMENT_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
