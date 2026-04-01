---
id: DOC-PO-PVO-InitiativeQualAreaExtractPVO
doc_type: system-doc
title: "InitiativeQualAreaExtractPVO — PVO Purchasing"
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
  - InitiativeQualAreaExtractPVO
  - initiativequalareaextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativeQualAreaExtractPVO

## 📌 Visão Geral

Extrai as áreas de qualificação associadas a cada iniciativa, definindo quais dimensões (financeira, técnica, compliance) são avaliadas. Suporta planejamento e escopo de campanhas de homologação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.InitiativeQualAreaExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_init_qual_areas|POQ_INIT_QUAL_AREAS]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[poq_init_qual_areas|POQ_INIT_QUAL_AREAS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | EvaluationDueDate | EVALUATION_DUE_DATE | — | ✅ |
| 5 | InitQualAreaId | INIT_QUAL_AREA_ID | 🔑 | ✅ |
| 6 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OriginalQualAreaId | ORIGINAL_QUAL_AREA_ID | — | ✅ |
| 12 | OwnerId | OWNER_ID | — | ✅ |
| 13 | QualAreaId | QUAL_AREA_ID | — | ✅ |
| 14 | SyncCheckFlag | SYNC_CHECK_FLAG | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
