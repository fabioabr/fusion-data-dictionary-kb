---
id: DOC-OTHER-PVO-LegalEntityBSVAssgmtExtractPVO
doc_type: system-doc
title: "LegalEntityBSVAssgmtExtractPVO — PVO Cross-Module"
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
  - LegalEntityBSVAssgmtExtractPVO
  - legalentitybsvassgmtextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# LegalEntityBSVAssgmtExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Legal Entity BSVAssgmt Extract. Acessa as tabelas: GL_LEGAL_ENTITIES_BSVS.

**Caminho:** `FscmTopModelAM.FinExtractAM.GlBiccExtractAM.LegalEntityBSVAssgmtExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 3 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gl_legal_entities_bsvs|GL_LEGAL_ENTITIES_BSVS]] — 11 atributos (3 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gl_legal_entities_bsvs|GL_LEGAL_ENTITIES_BSVS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | GlLegalEntitiesBsvsCreatedBy | CREATED_BY | — | ✅ |
| 2 | GlLegalEntitiesBsvsCreationDate | CREATION_DATE | — | ✅ |
| 3 | GlLegalEntitiesBsvsEndDate | END_DATE | — | ✅ |
| 4 | GlLegalEntitiesBsvsFlexSegmentValue | FLEX_SEGMENT_VALUE | 🔑 | ✅ |
| 5 | GlLegalEntitiesBsvsFlexValueSetId | FLEX_VALUE_SET_ID | 🔑 | ✅ |
| 6 | GlLegalEntitiesBsvsLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | GlLegalEntitiesBsvsLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | GlLegalEntitiesBsvsLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | GlLegalEntitiesBsvsLegalEntityId | LEGAL_ENTITY_ID | 🔑 | ✅ |
| 10 | GlLegalEntitiesBsvsObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | GlLegalEntitiesBsvsStartDate | START_DATE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
