---
id: DOC-OTHER-PVO-ProjectResourceBreakdownStructureElememtMapExtractPVO
doc_type: system-doc
title: "ProjectResourceBreakdownStructureElememtMapExtractPVO — PVO Cross-Module"
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
  - ProjectResourceBreakdownStructureElememtMapExtractPVO
  - projectresourcebreakdownstructureelememtmapextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectResourceBreakdownStructureElememtMapExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Resource Breakdown Structure Elememt Map Extract. Acessa as tabelas: PJF_RBS_ELEMENT_MAP.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjfBiccExtractAM.ProjectResourceBreakdownStructureElememtMapExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 9 | 1 | 1 | 9 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjf_rbs_element_map|PJF_RBS_ELEMENT_MAP]] — 9 atributos (1 PKs, 9 BICC)

---

## ⚙️ Atributos

### [[pjf_rbs_element_map|PJF_RBS_ELEMENT_MAP]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PRBSElememtMapPEOCreatedBy | CREATED_BY | — | ✅ |
| 2 | PRBSElememtMapPEOCreationDate | CREATION_DATE | — | ✅ |
| 3 | PRBSElememtMapPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 4 | PRBSElememtMapPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 5 | PRBSElememtMapPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 6 | PRBSElememtMapPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 7 | PRBSElememtMapPEOResourceId | RESOURCE_ID | 🔑 | ✅ |
| 8 | PRBSElememtMapPEOResourceName | RESOURCE_NAME | — | ✅ |
| 9 | PRBSElememtMapPEOResourceTypeId | RESOURCE_TYPE_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
