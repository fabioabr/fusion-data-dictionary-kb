---
id: DOC-HCM-505
doc_type: system-doc
title: "HZ_PARTY_USG_ASSIGNMENTS — (título a preencher)"
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
  - HZ_PARTY_USG_ASSIGNMENTS
  - hz_party_usg_assignments
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# HZ_PARTY_USG_ASSIGNMENTS

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | COMMENTS | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATED_BY_MODULE | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | EFFECTIVE_END_DATE | — | — | — | — | — | — |
| 6 | EFFECTIVE_START_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 8 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 9 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 10 | OWNER_TABLE_ID | — | — | — | — | — | — |
| 11 | OWNER_TABLE_NAME | — | — | — | — | — | — |
| 12 | PARTY_ID | — | — | — | — | — | — |
| 13 | PARTY_USAGE_CODE | — | — | — | — | — | — |
| 14 | PARTY_USG_ASSIGNMENT_ID | — | — | — | — | — | — |
| 15 | STATUS_FLAG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[customer|Customer]] (HCM)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | Comments1 | — |
| CREATED_BY | CreatedBy1 | — |
| CREATED_BY_MODULE | CreatedByModule1 | — |
| CREATION_DATE | CreationDate1 | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | — |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| OWNER_TABLE_ID | OwnerTableId | — |
| OWNER_TABLE_NAME | OwnerTableName | — |
| PARTY_USAGE_CODE | PartyUsageCode | — |
| PARTY_USG_ASSIGNMENT_ID | PartyUsgAssignmentId | — |
| STATUS_FLAG | StatusFlag | — |

### [[partyusage|PartyUsage]] (HCM · BICC: 3/14)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| COMMENTS | PartyAssignmentComments | — |
| CREATED_BY_MODULE | PartyAssignmentCreatedByModule | — |
| CREATION_DATE | PartyAssignmentCreationDate | — |
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | ✅ |
| LAST_UPDATE_DATE | PartyAssignmentLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | PartyAssignmentLastUpdateLogin | — |
| LAST_UPDATED_BY | PartyAssignmentLastUpdatedBy | — |
| OWNER_TABLE_ID | OwnerTableId | — |
| OWNER_TABLE_NAME | OwnerTableName | — |
| PARTY_ID | PartyAssignmentPartyId | — |
| PARTY_USAGE_CODE | PartyUsageCode | — |
| PARTY_USG_ASSIGNMENT_ID | PartyUsgAssignmentId | ✅ |
| STATUS_FLAG | PartyEOStatusFlag | — |

### [[persondetailsrefpvo|PersonDetailsRefPVO]] (OTHER · BICC: 2/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| EFFECTIVE_END_DATE | EffectiveEndDate | — |
| EFFECTIVE_START_DATE | EffectiveStartDate | — |
| PARTY_USAGE_CODE | USGAssPEOPartyUsageCode | ✅ |
| PARTY_USG_ASSIGNMENT_ID | USGAssPEOPartyUsgAssignmentId | ✅ |
| STATUS_FLAG | StatusFlag | — |

### [[resourcep|ResourceP]] (OTHER · BICC: 4/4)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARTY_ID | PartyUsageAssignmentPEOPartyId | ✅ |
| PARTY_USAGE_CODE | PartyUsageCode | ✅ |
| PARTY_USG_ASSIGNMENT_ID | PartyUsgAssignmentId | ✅ |
| STATUS_FLAG | StatusFlag | ✅ |

### [[resourcepartnerpvo|ResourcePartnerPVO]] (OTHER · BICC: 1/2)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| PARTY_USAGE_CODE | PartyUsageCode | — |
| PARTY_USG_ASSIGNMENT_ID | PartyUsgAssignmentId | ✅ |
