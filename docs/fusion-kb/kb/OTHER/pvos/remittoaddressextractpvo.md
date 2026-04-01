---
id: DOC-OTHER-PVO-RemitToAddressExtractPVO
doc_type: system-doc
title: "RemitToAddressExtractPVO — PVO Cross-Module"
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
  - RemitToAddressExtractPVO
  - remittoaddressextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RemitToAddressExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Remit To Address Extract. Acessa as tabelas: RA_REMIT_TOS_ALL.

**Caminho:** `FscmTopModelAM.FinExtractAM.ArBiccExtractAM.RemitToAddressExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 32 | 1 | 1 | 16 | 50% |

---

## 🔗 Tabelas Relacionadas

- [[ra_remit_tos_all|RA_REMIT_TOS_ALL]] — 32 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[ra_remit_tos_all|RA_REMIT_TOS_ALL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RaRemitToAddressId | ADDRESS_ID | — | ✅ |
| 2 | RaRemitToAddressLocSeqId | ADDRESS_LOC_SEQ_ID | — | ✅ |
| 3 | RaRemitToAddressSeqId | ADDRESS_SEQ_ID | 🔑 | ✅ |
| 4 | RaRemitToAttribute1 | ATTRIBUTE1 | — | — |
| 5 | RaRemitToAttribute10 | ATTRIBUTE10 | — | — |
| 6 | RaRemitToAttribute11 | ATTRIBUTE11 | — | — |
| 7 | RaRemitToAttribute12 | ATTRIBUTE12 | — | — |
| 8 | RaRemitToAttribute13 | ATTRIBUTE13 | — | — |
| 9 | RaRemitToAttribute14 | ATTRIBUTE14 | — | — |
| 10 | RaRemitToAttribute15 | ATTRIBUTE15 | — | — |
| 11 | RaRemitToAttribute2 | ATTRIBUTE2 | — | — |
| 12 | RaRemitToAttribute3 | ATTRIBUTE3 | — | — |
| 13 | RaRemitToAttribute4 | ATTRIBUTE4 | — | — |
| 14 | RaRemitToAttribute5 | ATTRIBUTE5 | — | — |
| 15 | RaRemitToAttribute6 | ATTRIBUTE6 | — | — |
| 16 | RaRemitToAttribute7 | ATTRIBUTE7 | — | — |
| 17 | RaRemitToAttribute8 | ATTRIBUTE8 | — | — |
| 18 | RaRemitToAttribute9 | ATTRIBUTE9 | — | — |
| 19 | RaRemitToAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 20 | RaRemitToCountry | COUNTRY | — | ✅ |
| 21 | RaRemitToCreatedBy | CREATED_BY | — | ✅ |
| 22 | RaRemitToCreationDate | CREATION_DATE | — | ✅ |
| 23 | RaRemitToLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 24 | RaRemitToLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 25 | RaRemitToLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 26 | RaRemitToObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 27 | RaRemitToOrgId | ORG_ID | — | ✅ |
| 28 | RaRemitToPostalCodeHigh | POSTAL_CODE_HIGH | — | ✅ |
| 29 | RaRemitToPostalCodeLow | POSTAL_CODE_LOW | — | ✅ |
| 30 | RaRemitToSetId | SET_ID | — | ✅ |
| 31 | RaRemitToState | STATE | — | ✅ |
| 32 | RaRemitToStatus | STATUS | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
