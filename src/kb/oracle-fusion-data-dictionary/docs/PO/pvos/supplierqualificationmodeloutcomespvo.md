---
id: DOC-PO-PVO-SupplierQualificationModelOutcomesPVO
doc_type: system-doc
title: "SupplierQualificationModelOutcomesPVO — PVO Purchasing"
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
  - SupplierQualificationModelOutcomesPVO
  - supplierqualificationmodeloutcomespvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierQualificationModelOutcomesPVO

## 📌 Visão Geral

Extrai os resultados finais de modelos de qualificação por fornecedor, consolidando outcomes de todas as áreas avaliadas. Permite visão executiva do status de homologação e tomada de decisão.

**Caminho:** `FscmTopModelAM.PrcPoqPublicViewAM.SupplierQualificationModelOutcomesPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 1 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qual_model_outcomes|POQ_QUAL_MODEL_OUTCOMES]] — 14 atributos (1 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[poq_qual_model_outcomes|POQ_QUAL_MODEL_OUTCOMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | DisplaySequence | DISPLAY_SEQUENCE | — | ✅ |
| 4 | FromScore | FROM_SCORE | — | ✅ |
| 5 | KnockoutOutcomeFlag | KNOCKOUT_OUTCOME_FLAG | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | NotificationFlag | NOTIFICATION_FLAG | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | OutcomeName | OUTCOME_NAME | — | ✅ |
| 12 | QualModelId | QUAL_MODEL_ID | — | ✅ |
| 13 | QualModelOutcomeId | QUAL_MODEL_OUTCOME_ID | 🔑 | ✅ |
| 14 | ToScore | TO_SCORE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
