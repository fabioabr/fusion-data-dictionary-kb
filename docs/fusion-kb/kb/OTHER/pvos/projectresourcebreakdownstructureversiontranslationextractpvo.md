---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureVersionTranslationExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureVersionTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureVersionTranslationExtractPVO
  - projectresourcebreakdownstructureversiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureVersionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Version Translation Extract. Acessa as tabelas: PJF_RBS_VERSIONS_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureVersionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_versions_tl|PJF_RBS_VERSIONS_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_versions_tl|PJF_RBS_VERSIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSVersionTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSVersionTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSVersionTLPEODescription | DESCRIPTION | — | ✅ |
| 4 | PRBSVersionTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 5 | PRBSVersionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | PRBSVersionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 7 | PRBSVersionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 8 | PRBSVersionTLPEOName | NAME | — | ✅ |
| 9 | PRBSVersionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PRBSVersionTLPEORbsVersionId | RBS_VERSION_ID | 🔑 | ✅ |
| 11 | PRBSVersionTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 12 | PRBSVersionTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
