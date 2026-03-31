---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureElementNameExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureElementNameExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureElementNameExtractPVO
  - projectresourcebreakdownstructureelementnameextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureElementNameExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Element Name Extract. Acessa as tabelas: PJF_RBS_ELEMENT_NAMES_B, PJF_RBS_ELEMENT_NAMES_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureElementNameExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 2 | 1 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_element_names_b|PJF_RBS_ELEMENT_NAMES_B]] — 10 atributos (1 PKs, 10 BICC)
- [[pjf_rbs_element_names_tl|PJF_RBS_ELEMENT_NAMES_TL]] — 11 atributos (11 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_element_names_b|PJF_RBS_ELEMENT_NAMES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSElementNameBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSElementNameBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSElementNameBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PRBSElementNameBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PRBSElementNameBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PRBSElementNameBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PRBSElementNameBasePEORbsElementNameId | RBS_ELEMENT_NAME_ID | 🔑 | ✅ |
| 8 | PRBSElementNameBasePEOResourceSourceId | RESOURCE_SOURCE_ID | — | ✅ |
| 9 | PRBSElementNameBasePEOResourceTypeId | RESOURCE_TYPE_ID | — | ✅ |
| 10 | PRBSElementNameBasePEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |

### [[pjf_rbs_element_names_tl|PJF_RBS_ELEMENT_NAMES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSElementNameTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSElementNameTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSElementNameTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | PRBSElementNameTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | PRBSElementNameTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | PRBSElementNameTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | PRBSElementNameTranslationPEOName | NAME | — | ✅ |
| 8 | PRBSElementNameTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 9 | PRBSElementNameTranslationPEORbsElementNameId | RBS_ELEMENT_NAME_ID | — | ✅ |
| 10 | PRBSElementNameTranslationPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 11 | PRBSElementNameTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
