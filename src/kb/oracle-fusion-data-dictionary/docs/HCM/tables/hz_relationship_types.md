---
id: DOC-HCM-507
doc_type: system-doc
title: "HZ_RELATIONSHIP_TYPES — (título a preencher)"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - human-capital-management
  - data-dictionary
aliases:
  - HZ_RELATIONSHIP_TYPES
  - hz_relationship_types
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_RELATIONSHIP_TYPES

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | ALLOW_CIRCULAR_RELATIONSHIPS | — | — | — | — | — | — |
| 2 | ALLOW_RELATE_TO_SELF_FLAG | — | — | — | — | — | — |
| 3 | BACKWARD_REL_CODE | — | — | — | — | — | — |
| 4 | CREATED_BY | — | — | — | — | — | — |
| 5 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 6 | CREATION_DATE | — | — | — | — | — | — |
| 7 | DIRECTION_CODE | — | — | — | — | — | — |
| 8 | FORWARD_REL_CODE | — | — | — | — | — | — |
| 9 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 10 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 11 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 12 | OBJECT_TYPE | — | — | — | — | — | — |
| 13 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 14 | RELATIONSHIP_TYPE | — | — | — | — | — | — |
| 15 | RELATIONSHIP_TYPE_ID | — | — | — | — | — | — |
| 16 | ROLE | — | — | — | — | — | — |
| 17 | STATUS | — | — | — | — | — | — |
| 18 | SUBJECT_TYPE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[accountcontactpoint|AccountContactPoint]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_CIRCULAR_RELATIONSHIPS | RelationshipTypeAllowCircularRelationships | — |
| ALLOW_RELATE_TO_SELF_FLAG | RelationshipTypeAllowRelateToSelfFlag | — |
| BACKWARD_REL_CODE | RelationshipTypeBackwardRelCode | — |
| CREATED_BY | RelationshipTypeCreatedBy | — |
| CREATED_BY_MODULE | RelationshipTypeCreatedByModule | — |
| CREATION_DATE | RelationshipTypeCreationDate | — |
| DIRECTION_CODE | RelationshipTypeDirectionCode | — |
| FORWARD_REL_CODE | RelationshipTypeForwardRelCode | — |
| LAST_UPDATE_DATE | RelationshipTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RelationshipTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | RelationshipTypeLastUpdatedBy | — |
| OBJECT_TYPE | RelationshipTypeObjectType | — |
| OBJECT_VERSION_NUMBER | RelationshipTypeObjectVersionNumber | — |
| RELATIONSHIP_TYPE | RelationshipTypeRelationshipType | — |
| RELATIONSHIP_TYPE_ID | RelationshipTypeRelationshipTypeId | — |
| ROLE | RelationshipTypeRole | ✅ |
| STATUS | RelationshipTypeStatus | — |
| SUBJECT_TYPE | RelationshipTypeSubjectType | — |

### [[relationship|Relationship]] (OTHER · BICC: 1/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BACKWARD_REL_CODE | RelTypeBackwardRelCode | — |
| DIRECTION_CODE | RelTypeDirectionCode | — |
| FORWARD_REL_CODE | RelTypeForwardRelCode | — |
| OBJECT_TYPE | RelTypeObjectType | — |
| RELATIONSHIP_TYPE_ID | RelTypeRelationshipTypeId | — |
| ROLE | RelTypeRole | ✅ |
| STATUS | RelTypeStatus | — |
| SUBJECT_TYPE | RelTypeSubjectType | — |

### [[sitecontactpoint|SiteContactPoint]] (AR · BICC: 2/18)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| ALLOW_CIRCULAR_RELATIONSHIPS | RelationshipTypeAllowCircularRelationships | — |
| ALLOW_RELATE_TO_SELF_FLAG | RelationshipTypeAllowRelateToSelfFlag | — |
| BACKWARD_REL_CODE | RelationshipTypeBackwardRelCode | — |
| CREATED_BY | RelationshipTypeCreatedBy | — |
| CREATED_BY_MODULE | RelationshipTypeCreatedByModule | — |
| CREATION_DATE | RelationshipTypeCreationDate | — |
| DIRECTION_CODE | RelationshipTypeDirectionCode | — |
| FORWARD_REL_CODE | RelationshipTypeForwardRelCode | — |
| LAST_UPDATE_DATE | RelationshipTypeLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | RelationshipTypeLastUpdateLogin | — |
| LAST_UPDATED_BY | RelationshipTypeLastUpdatedBy | — |
| OBJECT_TYPE | RelationshipTypeObjectType | — |
| OBJECT_VERSION_NUMBER | RelationshipTypeObjectVersionNumber | — |
| RELATIONSHIP_TYPE | RelationshipTypeRelationshipType | — |
| RELATIONSHIP_TYPE_ID | RelationshipTypeRelationshipTypeId | — |
| ROLE | RelationshipTypeRole | ✅ |
| STATUS | RelationshipTypeStatus | — |
| SUBJECT_TYPE | RelationshipTypeSubjectType | — |
