---
id: DOC-OTHER-PVO-PartnerHierarchyBICVO
doc_type: system-doc
title: "PartnerHierarchyBICVO — PVO Cross-Module"
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
  - PartnerHierarchyBICVO
  - partnerhierarchybicvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# PartnerHierarchyBICVO

## 📌 Visão Geral

View Object para extração BICC de dados de Partner Hierarchy BICVO. Acessa as tabelas: HZ_PARTIES, ZCA_BI_PARTNER_HIERARCHIES_V, ZPM_PARTNER_PROFILES.

**Caminho:** `FscmTopModelAM.PartnerCenterAnalyticsAM.PartnerHierarchyBICVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 3 | 4 | 36 | 42% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 39 atributos (17 BICC)
- [[zca_bi_partner_hierarchies_v|ZCA_BI_PARTNER_HIERARCHIES_V]] — 26 atributos (4 PKs, 9 BICC)
- [[zpm_partner_profiles|ZPM_PARTNER_PROFILES]] — 20 atributos (10 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DSDEP0PartyId2 | PARTY_ID | — | — |
| 2 | DSDEP9PartyId2 | PARTY_ID | — | — |
| 3 | Dep0IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 4 | Dep0PartyName | PARTY_NAME | — | ✅ |
| 5 | Dep0PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 6 | Dep1IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 7 | Dep1PartyId | PARTY_ID | — | ✅ |
| 8 | Dep1PartyName | PARTY_NAME | — | ✅ |
| 9 | Dep1PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 10 | Dep2IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 11 | Dep2PartyId | PARTY_ID | — | ✅ |
| 12 | Dep2PartyName | PARTY_NAME | — | ✅ |
| 13 | Dep2PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 14 | Dep3IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 15 | Dep3PartyId | PARTY_ID | — | ✅ |
| 16 | Dep3PartyName | PARTY_NAME | — | ✅ |
| 17 | Dep3PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 18 | Dep4IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 19 | Dep4PartyId | PARTY_ID | — | ✅ |
| 20 | Dep4PartyName | PARTY_NAME | — | ✅ |
| 21 | Dep4PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 22 | Dep5IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 23 | Dep5PartyId | PARTY_ID | — | ✅ |
| 24 | Dep5PartyName | PARTY_NAME | — | ✅ |
| 25 | Dep5PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 26 | Dep6IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 27 | Dep6PartyId | PARTY_ID | — | ✅ |
| 28 | Dep6PartyName | PARTY_NAME | — | ✅ |
| 29 | Dep6PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 30 | Dep7IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 31 | Dep7PartyId | PARTY_ID | — | ✅ |
| 32 | Dep7PartyName | PARTY_NAME | — | ✅ |
| 33 | Dep7PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 34 | Dep8IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 35 | Dep8PartyId | PARTY_ID | — | ✅ |
| 36 | Dep8PartyName | PARTY_NAME | — | ✅ |
| 37 | Dep8PartyUniqueName | PARTY_UNIQUE_NAME | — | — |
| 38 | Dep9IdenAddrLocationId | IDEN_ADDR_LOCATION_ID | — | — |
| 39 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[zca_bi_partner_hierarchies_v|ZCA_BI_PARTNER_HIERARCHIES_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CfTreeNodeId | CF_TREE_NODE_ID | 🔑 | ✅ |
| 2 | CreationDate | CREATION_DATE | — | — |
| 3 | Dep0PartyId | DEP0_PK1_VALUE | — | — |
| 4 | Dep0Pk1Value | DEP0_PK1_VALUE | — | ✅ |
| 5 | Dep1Pk1Value | DEP1_PK1_VALUE | — | — |
| 6 | Dep2Pk1Value | DEP2_PK1_VALUE | — | — |
| 7 | Dep3Pk1Value | DEP3_PK1_VALUE | — | — |
| 8 | Dep4Pk1Value | DEP4_PK1_VALUE | — | — |
| 9 | Dep5Pk1Value | DEP5_PK1_VALUE | — | — |
| 10 | Dep6Pk1Value | DEP6_PK1_VALUE | — | — |
| 11 | Dep7Pk1Value | DEP7_PK1_VALUE | — | — |
| 12 | Dep8Pk1Value | DEP8_PK1_VALUE | — | — |
| 13 | Dep9PartyId | DEP9_PARTY_ID | — | ✅ |
| 14 | Dep9PartyName | DEP9_PARTY_NAME | — | ✅ |
| 15 | Dep9PartyUniqueName | DEP9_PARTY_UNIQUE_NAME | — | — |
| 16 | Dep9Pk1Value | DEP9_PK1_VALUE | — | — |
| 17 | Distance | DISTANCE | — | — |
| 18 | EffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 19 | EffectiveStartDate | EFFECTIVE_START_DATE | — | ✅ |
| 20 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 21 | TreeCode | TREE_CODE | 🔑 | ✅ |
| 22 | TreeStructureCode | TREE_STRUCTURE_CODE | 🔑 | ✅ |
| 23 | TreeVersionId | TREE_VERSION_ID | 🔑 | ✅ |
| 24 | TreeVersionTreeCode | TREE_CODE | — | — |
| 25 | TreeVersionTreeStructureCode | TREE_STRUCTURE_CODE | — | — |
| 26 | TreeVersionTreeVersionId | TREE_VERSION_ID | — | — |

### [[zpm_partner_profiles|ZPM_PARTNER_PROFILES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PPDEP3PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 2 | PPDEP4PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 3 | PPDEP5PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 4 | PPDEP6PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 5 | PPDEP7PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 6 | PPDep0PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 7 | PPDep0PartyId | PARTY_ID | — | — |
| 8 | PPDep1PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 9 | PPDep1PartyId | PARTY_ID | — | — |
| 10 | PPDep2PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 11 | PPDep2PartyId | PARTY_ID | — | — |
| 12 | PPDep3PartyId | PARTY_ID | — | — |
| 13 | PPDep4PartyId | PARTY_ID | — | — |
| 14 | PPDep5PartyId | PARTY_ID | — | — |
| 15 | PPDep6PartyId | PARTY_ID | — | — |
| 16 | PPDep7PartyId | PARTY_ID | — | — |
| 17 | PPDep8PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 18 | PPDep8PartyId | PARTY_ID | — | — |
| 19 | PPDep9PartnerNumber | COMPANY_NUMBER | — | ✅ |
| 20 | PPDep9PartyId | PARTY_ID | — | — |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
