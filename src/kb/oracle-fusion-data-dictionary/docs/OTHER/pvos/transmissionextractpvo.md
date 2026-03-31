---
id: DOC-OTHER-PVO-TransmissionExtractPVO
doc_type: system-doc
title: "TransmissionExtractPVO — PVO Cross-Module"
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
  - TransmissionExtractPVO
  - transmissionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# TransmissionExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Transmission Extract. Acessa as tabelas: AR_TRANSMISSIONS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.TransmissionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 1 | 1 | 27 | 63% |

---

## 🔗 Tabelas Relacionadas

- [[ar_transmissions_all|AR_TRANSMISSIONS_ALL]] — 43 atributos (1 PKs, 27 BICC)

---

## ⚙️ Atributos

### [[ar_transmissions_all|AR_TRANSMISSIONS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ArTransmissionAmount | AMOUNT | — | ✅ |
| 2 | ArTransmissionAttribute1 | ATTRIBUTE1 | — | — |
| 3 | ArTransmissionAttribute10 | ATTRIBUTE10 | — | — |
| 4 | ArTransmissionAttribute11 | ATTRIBUTE11 | — | — |
| 5 | ArTransmissionAttribute12 | ATTRIBUTE12 | — | — |
| 6 | ArTransmissionAttribute13 | ATTRIBUTE13 | — | — |
| 7 | ArTransmissionAttribute14 | ATTRIBUTE14 | — | — |
| 8 | ArTransmissionAttribute15 | ATTRIBUTE15 | — | — |
| 9 | ArTransmissionAttribute2 | ATTRIBUTE2 | — | — |
| 10 | ArTransmissionAttribute3 | ATTRIBUTE3 | — | — |
| 11 | ArTransmissionAttribute4 | ATTRIBUTE4 | — | — |
| 12 | ArTransmissionAttribute5 | ATTRIBUTE5 | — | — |
| 13 | ArTransmissionAttribute6 | ATTRIBUTE6 | — | — |
| 14 | ArTransmissionAttribute7 | ATTRIBUTE7 | — | — |
| 15 | ArTransmissionAttribute8 | ATTRIBUTE8 | — | — |
| 16 | ArTransmissionAttribute9 | ATTRIBUTE9 | — | — |
| 17 | ArTransmissionAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 18 | ArTransmissionComments | COMMENTS | — | ✅ |
| 19 | ArTransmissionCount1 | COUNT | — | ✅ |
| 20 | ArTransmissionCreatedBy | CREATED_BY | — | ✅ |
| 21 | ArTransmissionCreationDate | CREATION_DATE | — | ✅ |
| 22 | ArTransmissionDestination | DESTINATION | — | ✅ |
| 23 | ArTransmissionErrorCount | ERROR_COUNT | — | ✅ |
| 24 | ArTransmissionLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 25 | ArTransmissionLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 26 | ArTransmissionLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 27 | ArTransmissionLatestRequestId | LATEST_REQUEST_ID | — | ✅ |
| 28 | ArTransmissionObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 29 | ArTransmissionOrgId | ORG_ID | — | ✅ |
| 30 | ArTransmissionOrigin | ORIGIN | — | ✅ |
| 31 | ArTransmissionRequestedGlDate | REQUESTED_GL_DATE | — | ✅ |
| 32 | ArTransmissionRequestedLockboxId | REQUESTED_LOCKBOX_ID | — | ✅ |
| 33 | ArTransmissionRequestedTransFormatId | REQUESTED_TRANS_FORMAT_ID | — | ✅ |
| 34 | ArTransmissionScoringModelId | SCORING_MODEL_ID | — | ✅ |
| 35 | ArTransmissionSourceTypeFlag | SOURCE_TYPE_FLAG | — | ✅ |
| 36 | ArTransmissionStatus | STATUS | — | ✅ |
| 37 | ArTransmissionTime | TIME | — | ✅ |
| 38 | ArTransmissionTransDate | TRANS_DATE | — | ✅ |
| 39 | ArTransmissionTransmissionId | TRANSMISSION_ID | 🔑 | ✅ |
| 40 | ArTransmissionTransmissionName | TRANSMISSION_NAME | — | ✅ |
| 41 | ArTransmissionTransmissionRequestId | TRANSMISSION_REQUEST_ID | — | ✅ |
| 42 | ArTransmissionValidatedAmount | VALIDATED_AMOUNT | — | ✅ |
| 43 | ArTransmissionValidatedCount | VALIDATED_COUNT | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
