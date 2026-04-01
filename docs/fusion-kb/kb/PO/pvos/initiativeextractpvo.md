---
id: DOC-PO-PVO-InitiativeExtractPVO
doc_type: system-doc
title: "InitiativeExtractPVO — PVO Purchasing"
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
  - InitiativeExtractPVO
  - initiativeextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InitiativeExtractPVO

## 📌 Visão Geral

Extrai iniciativas de qualificação de fornecedores para carga BICC, com escopo, cronograma e status. Alimenta análises de desempenho de programas de homologação e onboarding.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.InitiativeExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 80 | 1 | 1 | 28 | 35% |

---

## 🔗 Tabelas Relacionadas

- [[poq_initiatives|POQ_INITIATIVES]] — 80 atributos (1 PKs, 28 BICC)

---

## ⚙️ Atributos

### [[poq_initiatives|POQ_INITIATIVES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AssessmentEvalDueDate | ASSESSMENT_EVAL_DUE_DATE | — | ✅ |
| 2 | AssessmentOwnerId | ASSESSMENT_OWNER_ID | — | ✅ |
| 3 | Attribute1 | ATTRIBUTE1 | — | — |
| 4 | Attribute10 | ATTRIBUTE10 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute16 | ATTRIBUTE16 | — | — |
| 11 | Attribute17 | ATTRIBUTE17 | — | — |
| 12 | Attribute18 | ATTRIBUTE18 | — | — |
| 13 | Attribute19 | ATTRIBUTE19 | — | — |
| 14 | Attribute2 | ATTRIBUTE2 | — | — |
| 15 | Attribute20 | ATTRIBUTE20 | — | — |
| 16 | Attribute3 | ATTRIBUTE3 | — | — |
| 17 | Attribute4 | ATTRIBUTE4 | — | — |
| 18 | Attribute5 | ATTRIBUTE5 | — | — |
| 19 | Attribute6 | ATTRIBUTE6 | — | — |
| 20 | Attribute7 | ATTRIBUTE7 | — | — |
| 21 | Attribute8 | ATTRIBUTE8 | — | — |
| 22 | Attribute9 | ATTRIBUTE9 | — | — |
| 23 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 24 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 25 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 26 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 27 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 28 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 29 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 30 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 31 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 32 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 33 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 34 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 35 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 36 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 37 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 38 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 39 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 40 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 41 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 42 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 43 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 44 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 45 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 46 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 47 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 48 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 49 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 50 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 51 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 52 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 53 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 54 | AutoAcceptResponsesFlag | AUTO_ACCEPT_RESPONSES_FLAG | — | ✅ |
| 55 | AutoPopulateResponsesFlag | AUTO_POPULATE_RESPONSES_FLAG | — | ✅ |
| 56 | CanceledBy | CANCELED_BY | — | ✅ |
| 57 | CanceledDate | CANCELED_DATE | — | ✅ |
| 58 | CanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 59 | CompletedDate | COMPLETED_DATE | — | ✅ |
| 60 | CreatedBy | CREATED_BY | — | ✅ |
| 61 | CreationDate | CREATION_DATE | — | ✅ |
| 62 | CreationSource | CREATION_SOURCE | — | ✅ |
| 63 | Description | DESCRIPTION | — | ✅ |
| 64 | InitiativeId | INITIATIVE_ID | 🔑 | ✅ |
| 65 | InitiativeNumber | INITIATIVE_NUMBER | — | ✅ |
| 66 | InitiativeUsageCode | INITIATIVE_USAGE_CODE | — | — |
| 67 | InternalNote | INTERNAL_NOTE | — | ✅ |
| 68 | LastOverdueReminderDate | LAST_OVERDUE_REMINDER_DATE | — | ✅ |
| 69 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 70 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 71 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 72 | LaunchDate | LAUNCH_DATE | — | ✅ |
| 73 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 74 | OwnerId | OWNER_ID | — | ✅ |
| 75 | PrcBuId | PRC_BU_ID | — | ✅ |
| 76 | QualModelId | QUAL_MODEL_ID | — | ✅ |
| 77 | ReuseActiveQualFlag | REUSE_ACTIVE_QUAL_FLAG | — | ✅ |
| 78 | Status | STATUS | — | ✅ |
| 79 | Title | TITLE | — | ✅ |
| 80 | Type | TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
