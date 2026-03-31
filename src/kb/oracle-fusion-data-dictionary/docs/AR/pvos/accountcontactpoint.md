---
id: DOC-AR-PVO-AccountContactPoint
doc_type: system-doc
title: "AccountContactPoint — PVO Accounts Receivable"
system: Oracle Fusion Cloud ERP
module: Accounts Receivable
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - ar
  - data-dictionary
  - pvo
  - bicc
aliases:
  - AccountContactPoint
  - accountcontactpoint
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AccountContactPoint

## 📌 Visão Geral

Extrai os pontos de contato (telefone, e-mail, endereço) associados aos contatos de contas de clientes. Garante que as comunicações de cobrança e notificações de recebíveis alcancem os destinatários corretos.

**Caminho:** `FscmTopModelAM.FinArCustomersPublicModelAM.AccountContactPoint`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 59 | 3 | 1 | 8 | 14% |

---

## 🔗 Tabelas Relacionadas

- [[hz_contact_points|HZ_CONTACT_POINTS]] — 21 atributos (1 PKs, 5 BICC)
- [[hz_relationships|HZ_RELATIONSHIPS]] — 20 atributos (1 BICC)
- [[hz_relationship_types|HZ_RELATIONSHIP_TYPES]] — 18 atributos (2 BICC)

---

## ⚙️ Atributos

### [[hz_contact_points|HZ_CONTACT_POINTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContactPointActualContentSource | ACTUAL_CONTENT_SOURCE | — | — |
| 2 | ContactPointContactPointPurpose | CONTACT_POINT_PURPOSE | — | ✅ |
| 3 | ContactPointContactPointType | CONTACT_POINT_TYPE | — | ✅ |
| 4 | ContactPointCreatedBy | CREATED_BY | — | — |
| 5 | ContactPointCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | ContactPointCreationDate | CREATION_DATE | — | — |
| 7 | ContactPointEndDate | END_DATE | — | — |
| 8 | ContactPointId | CONTACT_POINT_ID | 🔑 | ✅ |
| 9 | ContactPointLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | ContactPointLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | ContactPointLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | ContactPointOrigSystemReference | ORIG_SYSTEM_REFERENCE | — | — |
| 13 | ContactPointOverallPrimaryFlag | OVERALL_PRIMARY_FLAG | — | — |
| 14 | ContactPointOwnerTableId | OWNER_TABLE_ID | — | — |
| 15 | ContactPointOwnerTableName | OWNER_TABLE_NAME | — | — |
| 16 | ContactPointPartyUsageCode | PARTY_USAGE_CODE | — | — |
| 17 | ContactPointPrimaryByPurpose | PRIMARY_BY_PURPOSE | — | — |
| 18 | ContactPointPrimaryFlag | PRIMARY_FLAG | — | ✅ |
| 19 | ContactPointRelationshipId | RELATIONSHIP_ID | — | — |
| 20 | ContactPointStartDate | START_DATE | — | — |
| 21 | ContactPointStatus | STATUS | — | — |

### [[hz_relationships|HZ_RELATIONSHIPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipHeadOfHouseholdFlag | HEAD_OF_HOUSEHOLD_FLAG | — | — |
| 2 | RelationshipLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 3 | RelationshipLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 4 | RelationshipLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 5 | RelationshipObjectId | OBJECT_ID | — | — |
| 6 | RelationshipObjectTableName | OBJECT_TABLE_NAME | — | — |
| 7 | RelationshipObjectType | OBJECT_TYPE | — | — |
| 8 | RelationshipObjectUsageCode | OBJECT_USAGE_CODE | — | — |
| 9 | RelationshipObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | RelationshipPercentageOwnership | PERCENTAGE_OWNERSHIP | — | — |
| 11 | RelationshipRelationshipCode | RELATIONSHIP_CODE | — | — |
| 12 | RelationshipRelationshipId | RELATIONSHIP_ID | — | — |
| 13 | RelationshipRelationshipRecId | RELATIONSHIP_REC_ID | — | — |
| 14 | RelationshipRelationshipType | RELATIONSHIP_TYPE | — | — |
| 15 | RelationshipStartDate | START_DATE | — | — |
| 16 | RelationshipStatus | STATUS | — | — |
| 17 | RelationshipSubjectId | SUBJECT_ID | — | — |
| 18 | RelationshipSubjectTableName | SUBJECT_TABLE_NAME | — | — |
| 19 | RelationshipSubjectType | SUBJECT_TYPE | — | — |
| 20 | RelationshipSubjectUsageCode | SUBJECT_USAGE_CODE | — | — |

### [[hz_relationship_types|HZ_RELATIONSHIP_TYPES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | RelationshipTypeAllowCircularRelationships | ALLOW_CIRCULAR_RELATIONSHIPS | — | — |
| 2 | RelationshipTypeAllowRelateToSelfFlag | ALLOW_RELATE_TO_SELF_FLAG | — | — |
| 3 | RelationshipTypeBackwardRelCode | BACKWARD_REL_CODE | — | — |
| 4 | RelationshipTypeCreatedBy | CREATED_BY | — | — |
| 5 | RelationshipTypeCreatedByModule | CREATED_BY_MODULE | — | — |
| 6 | RelationshipTypeCreationDate | CREATION_DATE | — | — |
| 7 | RelationshipTypeDirectionCode | DIRECTION_CODE | — | — |
| 8 | RelationshipTypeForwardRelCode | FORWARD_REL_CODE | — | — |
| 9 | RelationshipTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | RelationshipTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 11 | RelationshipTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 12 | RelationshipTypeObjectType | OBJECT_TYPE | — | — |
| 13 | RelationshipTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | RelationshipTypeRelationshipType | RELATIONSHIP_TYPE | — | — |
| 15 | RelationshipTypeRelationshipTypeId | RELATIONSHIP_TYPE_ID | — | — |
| 16 | RelationshipTypeRole | ROLE | — | ✅ |
| 17 | RelationshipTypeStatus | STATUS | — | — |
| 18 | RelationshipTypeSubjectType | SUBJECT_TYPE | — | — |

---

## 📚 Referências

- [[ar-module-data-dictionary]] — Dossiê do módulo AR
