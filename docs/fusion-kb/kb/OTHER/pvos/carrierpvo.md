---
id: DOC-OTHER-PVO-CarrierPVO
doc_type: system-doc
title: "CarrierPVO — PVO Cross-Module"
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
  - CarrierPVO
  - carrierpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CarrierPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Carrier. Acessa as tabelas: HZ_PARTIES, WSH_CARRIERS.

**Caminho:** `FscmTopModelAM.WshCarriersAM.CarrierPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 64 | 2 | 1 | 17 | 27% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 16 atributos (15 BICC)
- [[wsh_carriers|WSH_CARRIERS]] — 48 atributos (1 PKs, 2 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOAddress1 | ADDRESS1 | — | ✅ |
| 2 | PartyPEOAddress2 | ADDRESS2 | — | ✅ |
| 3 | PartyPEOAddress3 | ADDRESS3 | — | ✅ |
| 4 | PartyPEOAddress4 | ADDRESS4 | — | ✅ |
| 5 | PartyPEOCity | CITY | — | ✅ |
| 6 | PartyPEOCountry | COUNTRY | — | ✅ |
| 7 | PartyPEOCounty | COUNTY | — | ✅ |
| 8 | PartyPEOPartyId | PARTY_ID | — | — |
| 9 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 10 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |
| 11 | PartyPEOPostalCode | POSTAL_CODE | — | ✅ |
| 12 | PartyPEOPreferredContactPersonId | PREFERRED_CONTACT_PERSON_ID | — | ✅ |
| 13 | PartyPEOPreferredName | PREFERRED_NAME | — | ✅ |
| 14 | PartyPEOProvince | PROVINCE | — | ✅ |
| 15 | PartyPEOState | STATE | — | ✅ |
| 16 | PartyPEOStatus | STATUS | — | ✅ |

### [[wsh_carriers|WSH_CARRIERS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Attribute1 | ATTRIBUTE1 | — | — |
| 2 | Attribute10 | ATTRIBUTE10 | — | — |
| 3 | Attribute11 | ATTRIBUTE11 | — | — |
| 4 | Attribute12 | ATTRIBUTE12 | — | — |
| 5 | Attribute13 | ATTRIBUTE13 | — | — |
| 6 | Attribute14 | ATTRIBUTE14 | — | — |
| 7 | Attribute15 | ATTRIBUTE15 | — | — |
| 8 | Attribute2 | ATTRIBUTE2 | — | — |
| 9 | Attribute3 | ATTRIBUTE3 | — | — |
| 10 | Attribute4 | ATTRIBUTE4 | — | — |
| 11 | Attribute5 | ATTRIBUTE5 | — | — |
| 12 | Attribute6 | ATTRIBUTE6 | — | — |
| 13 | Attribute7 | ATTRIBUTE7 | — | — |
| 14 | Attribute8 | ATTRIBUTE8 | — | — |
| 15 | Attribute9 | ATTRIBUTE9 | — | — |
| 16 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 17 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 18 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 19 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 20 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 21 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 22 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 23 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 24 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 25 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 26 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 27 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 28 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 29 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 30 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 31 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 32 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 33 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 34 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 35 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 36 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 37 | CarrierId | CARRIER_ID | 🔑 | ✅ |
| 38 | CarrierPEOCreatedBy | CREATED_BY | — | — |
| 39 | CarrierPEOCreationDate | CREATION_DATE | — | — |
| 40 | CarrierPEOEnabledFlag | ENABLED_FLAG | — | — |
| 41 | CarrierPEOJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 42 | CarrierPEOJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 43 | CarrierPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 44 | CarrierPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 45 | CarrierPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 46 | CarrierPEOManifestingEnabledFlag | MANIFESTING_ENABLED_FLAG | — | — |
| 47 | CarrierPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 48 | CarrierPEORequestId | REQUEST_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
