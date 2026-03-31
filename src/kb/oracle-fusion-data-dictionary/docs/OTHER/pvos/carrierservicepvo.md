---
id: DOC-OTHER-PVO-CarrierServicePVO
doc_type: system-doc
title: "CarrierServicePVO — PVO Cross-Module"
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
  - CarrierServicePVO
  - carrierservicepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CarrierServicePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Carrier Service. Acessa as tabelas: HZ_PARTIES, INV_ORGANIZATION_DEFINITIONS_V, WSH_ORG_CARRIER_SERVICES.

**Caminho:** `FscmTopModelAM.WshCarriersAM.CarrierServicePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 3 | 1 | 10 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 3 atributos (3 BICC)
- [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]] — 3 atributos (2 BICC)
- [[wsh_org_carrier_services|WSH_ORG_CARRIER_SERVICES]] — 52 atributos (1 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyPEOPartyId | PARTY_ID | — | ✅ |
| 2 | PartyPEOPartyName | PARTY_NAME | — | ✅ |
| 3 | PartyPEOPartyNumber | PARTY_NUMBER | — | ✅ |

### [[inv_organization_definitions_v|INV_ORGANIZATION_DEFINITIONS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | OrgOrganizationDefinitionsPEOOrganizationCode | ORGANIZATION_CODE | — | ✅ |
| 2 | OrgOrganizationDefinitionsPEOOrganizationId | ORGANIZATION_ID | — | — |
| 3 | OrgOrganizationDefinitionsPEOOrganizationName | ORGANIZATION_NAME | — | ✅ |

### [[wsh_org_carrier_services|WSH_ORG_CARRIER_SERVICES]]

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
| 37 | OrgCarrierServiceId | ORG_CARRIER_SERVICE_ID | 🔑 | ✅ |
| 38 | WshOrgCarrierServicesCarrierId | CARRIER_ID | — | — |
| 39 | WshOrgCarrierServicesCreatedBy | CREATED_BY | — | — |
| 40 | WshOrgCarrierServicesCreationDate | CREATION_DATE | — | — |
| 41 | WshOrgCarrierServicesEnabledFlag | ENABLED_FLAG | — | — |
| 42 | WshOrgCarrierServicesJobDefinitionName | JOB_DEFINITION_NAME | — | — |
| 43 | WshOrgCarrierServicesJobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | — |
| 44 | WshOrgCarrierServicesLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 45 | WshOrgCarrierServicesLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 46 | WshOrgCarrierServicesLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 47 | WshOrgCarrierServicesModeOfTransport | MODE_OF_TRANSPORT | — | ✅ |
| 48 | WshOrgCarrierServicesObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 49 | WshOrgCarrierServicesOrganizationId | ORGANIZATION_ID | — | — |
| 50 | WshOrgCarrierServicesRequestId | REQUEST_ID | — | — |
| 51 | WshOrgCarrierServicesServiceLevel | SERVICE_LEVEL | — | ✅ |
| 52 | WshOrgCarrierServicesShipMethodCode | SHIP_METHOD_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
