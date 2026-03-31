---
id: DOC-PO-PVO-QualificationExtractPVO
doc_type: system-doc
title: "QualificationExtractPVO — PVO Purchasing"
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
  - QualificationExtractPVO
  - qualificationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# QualificationExtractPVO

## 📌 Visão Geral

Extrai dados de qualificações de fornecedores para carga BICC, incluindo status, modelo utilizado, datas e resultados. Alimenta dashboards de gestão do programa de qualificação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PoqBiccExtractAM.QualificationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 99 | 1 | 1 | 48 | 48% |

---

## 🔗 Tabelas Relacionadas

- [[poq_qualifications|POQ_QUALIFICATIONS]] — 99 atributos (1 PKs, 48 BICC)

---

## ⚙️ Atributos

### [[poq_qualifications|POQ_QUALIFICATIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute16 | ATTRIBUTE16 | — | — |
| 9 | Attribute17 | ATTRIBUTE17 | — | — |
| 10 | Attribute18 | ATTRIBUTE18 | — | — |
| 11 | Attribute19 | ATTRIBUTE19 | — | — |
| 12 | Attribute2 | ATTRIBUTE2 | — | — |
| 13 | Attribute20 | ATTRIBUTE20 | — | — |
| 14 | Attribute3 | ATTRIBUTE3 | — | — |
| 15 | Attribute4 | ATTRIBUTE4 | — | — |
| 16 | Attribute5 | ATTRIBUTE5 | — | — |
| 17 | Attribute6 | ATTRIBUTE6 | — | — |
| 18 | Attribute7 | ATTRIBUTE7 | — | — |
| 19 | Attribute8 | ATTRIBUTE8 | — | — |
| 20 | Attribute9 | ATTRIBUTE9 | — | — |
| 21 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 24 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 25 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 26 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 27 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 28 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 29 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 30 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 31 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 32 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 33 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 34 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 35 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 36 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 37 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 38 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 39 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 40 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 41 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 42 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 43 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 44 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 45 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 46 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 47 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 48 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 49 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 50 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 51 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 52 | AutoEvaluatedFlag | AUTO_EVALUATED_FLAG | — | ✅ |
| 53 | CanceledBy | CANCELED_BY | — | ✅ |
| 54 | CanceledDate | CANCELED_DATE | — | ✅ |
| 55 | CanceledReasonCode | CANCELED_REASON_CODE | — | ✅ |
| 56 | CompletedDate | COMPLETED_DATE | — | ✅ |
| 57 | CreatedBy | CREATED_BY | — | ✅ |
| 58 | CreationDate | CREATION_DATE | — | ✅ |
| 59 | CreationSource | CREATION_SOURCE | — | ✅ |
| 60 | EffectiveEndDate | EFFECTIVE_END_DATE | — | ✅ |
| 61 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 62 | EvaluatedBy | EVALUATED_BY | — | ✅ |
| 63 | EvaluationDate | EVALUATION_DATE | — | ✅ |
| 64 | EvaluationDueDate | EVALUATION_DUE_DATE | — | ✅ |
| 65 | ExpirationReminderPeriod | EXPIRATION_REMINDER_PERIOD | — | ✅ |
| 66 | ExpirationReminderType | EXPIRATION_REMINDER_TYPE | — | ✅ |
| 67 | InitiativeId | INITIATIVE_ID | — | ✅ |
| 68 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 69 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 70 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 71 | LatestFlag | LATEST_FLAG | — | ✅ |
| 72 | MergeRequestId | MERGE_REQUEST_ID | — | ✅ |
| 73 | NoteToSupplier | NOTE_TO_SUPPLIER | — | ✅ |
| 74 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 75 | OrigQualificationOutcome | ORIG_QUALIFICATION_OUTCOME | — | ✅ |
| 76 | OrigQualificationScore | ORIG_QUALIFICATION_SCORE | — | ✅ |
| 77 | OverriddenBy | OVERRIDDEN_BY | — | ✅ |
| 78 | OverrideDate | OVERRIDE_DATE | — | ✅ |
| 79 | OverrideReason | OVERRIDE_REASON | — | ✅ |
| 80 | OwnerId | OWNER_ID | — | ✅ |
| 81 | PrcBuId | PRC_BU_ID | — | ✅ |
| 82 | QualAreaId | QUAL_AREA_ID | — | ✅ |
| 83 | QualificationComments | QUALIFICATION_COMMENTS | — | ✅ |
| 84 | QualificationId | QUALIFICATION_ID | 🔑 | ✅ |
| 85 | QualificationName | QUALIFICATION_NAME | — | ✅ |
| 86 | QualificationNumber | QUALIFICATION_NUMBER | — | ✅ |
| 87 | QualificationOutcome | QUALIFICATION_OUTCOME | — | ✅ |
| 88 | QualificationScore | QUALIFICATION_SCORE | — | ✅ |
| 89 | RequalifyExecutedFlag | REQUALIFY_EXECUTED_FLAG | — | ✅ |
| 90 | RequalifyExpirationFlag | REQUALIFY_EXPIRATION_FLAG | — | ✅ |
| 91 | RequalifyResponseFlag | REQUALIFY_RESPONSE_FLAG | — | ✅ |
| 92 | RequestId | REQUEST_ID | — | ✅ |
| 93 | ShowQualInterRespFlag | SHOW_QUAL_INTER_RESP_FLAG | — | ✅ |
| 94 | ShowQualSuppRespFlag | SHOW_QUAL_SUPP_RESP_FLAG | — | ✅ |
| 95 | ShowQualToSupplierFlag | SHOW_QUAL_TO_SUPPLIER_FLAG | — | ✅ |
| 96 | Status | STATUS | — | ✅ |
| 97 | SuppContactPartyId | SUPP_CONTACT_PARTY_ID | — | ✅ |
| 98 | SupplierId | SUPPLIER_ID | — | ✅ |
| 99 | SupplierSiteId | SUPPLIER_SITE_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
