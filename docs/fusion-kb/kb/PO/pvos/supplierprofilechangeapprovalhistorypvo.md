---
id: DOC-PO-PVO-SupplierProfileChangeApprovalHistoryPVO
doc_type: system-doc
title: "SupplierProfileChangeApprovalHistoryPVO — PVO Purchasing"
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
  - SupplierProfileChangeApprovalHistoryPVO
  - supplierprofilechangeapprovalhistorypvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SupplierProfileChangeApprovalHistoryPVO

## 📌 Visão Geral

Extrai o histórico de aprovações de alterações de perfil de fornecedores, com aprovador, data e comentários. Garante auditoria completa de quem autorizou cada mudança nos dados cadastrais.

**Caminho:** `FscmTopModelAM.PrcPozPublicViewAM.SupplierProfileChangeApprovalHistoryPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 47 | 5 | 1 | 8 | 17% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_lookups|FND_LOOKUPS]] — 10 atributos (1 BICC)
- [[hz_parties|HZ_PARTIES]] — 7 atributos
- [[per_person_names_f_v|PER_PERSON_NAMES_F_V]] — 9 atributos
- [[poz_approval_history|POZ_APPROVAL_HISTORY]] — 17 atributos (1 PKs, 7 BICC)
- [[poz_bi_appr_user_comments_v|POZ_BI_APPR_USER_COMMENTS_V]] — 4 atributos

---

## ⚙️ Atributos

### [[fnd_lookups|FND_LOOKUPS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActionLookupPEODescription | DESCRIPTION | — | — |
| 2 | ActionLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 3 | ActionLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 4 | ActionLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 5 | ActionLookupPEOMeaning | MEANING | — | ✅ |
| 6 | PerformerTypeLookupPEODescription | DESCRIPTION | — | — |
| 7 | PerformerTypeLookupPEOEnabledFlag | ENABLED_FLAG | — | — |
| 8 | PerformerTypeLookupPEOLookupCode | LOOKUP_CODE | — | — |
| 9 | PerformerTypeLookupPEOLookupType | LOOKUP_TYPE | — | — |
| 10 | PerformerTypeLookupPEOMeaning | MEANING | — | — |

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerformedByPartyPEOPartyId | PARTY_ID | — | — |
| 2 | PerformedByPartyPEOPartyName | PARTY_NAME | — | — |
| 3 | PerformedByPartyPEOPartyNumber | PARTY_NUMBER | — | — |
| 4 | PerformedByPartyPEOPartyType | PARTY_TYPE | — | — |
| 5 | PerformedByPartyPEOPersonFirstName | PERSON_FIRST_NAME | — | — |
| 6 | PerformedByPartyPEOPersonLastName | PERSON_LAST_NAME | — | — |
| 7 | PerformedByPartyPEOStatus | STATUS | — | — |

### [[per_person_names_f_v|PER_PERSON_NAMES_F_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PerformedByPersonNamePEODisplayName | DISPLAY_NAME | — | — |
| 2 | PerformedByPersonNamePEOEffectiveEndDate | EFFECTIVE_END_DATE | — | — |
| 3 | PerformedByPersonNamePEOEffectiveStartDate | EFFECTIVE_START_DATE | — | — |
| 4 | PerformedByPersonNamePEOFirstName | FIRST_NAME | — | — |
| 5 | PerformedByPersonNamePEOFullName | FULL_NAME | — | — |
| 6 | PerformedByPersonNamePEOLastName | LAST_NAME | — | — |
| 7 | PerformedByPersonNamePEOListName | LIST_NAME | — | — |
| 8 | PerformedByPersonNamePEOPersonId | PERSON_ID | — | — |
| 9 | PerformedByPersonNamePEOPersonNameId | PERSON_NAME_ID | — | — |

### [[poz_approval_history|POZ_APPROVAL_HISTORY]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalHistoryPEOActionCode | ACTION_CODE | — | ✅ |
| 2 | ApprovalHistoryPEOActionDate | ACTION_DATE | — | ✅ |
| 3 | ApprovalHistoryPEOAdditionalInfo | ADDITIONAL_INFO | — | ✅ |
| 4 | ApprovalHistoryPEOAmxIdentificationKey | AMX_IDENTIFICATION_KEY | — | — |
| 5 | ApprovalHistoryPEOApprovalFlowCode | APPROVAL_FLOW_CODE | — | ✅ |
| 6 | ApprovalHistoryPEOApprovalHistoryId | APPROVAL_HISTORY_ID | 🔑 | ✅ |
| 7 | ApprovalHistoryPEOCreatedBy | CREATED_BY | — | — |
| 8 | ApprovalHistoryPEOCreationDate | CREATION_DATE | — | — |
| 9 | ApprovalHistoryPEOFlowObjectId | FLOW_OBJECT_ID | — | ✅ |
| 10 | ApprovalHistoryPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 11 | ApprovalHistoryPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 12 | ApprovalHistoryPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 13 | ApprovalHistoryPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 14 | ApprovalHistoryPEOPerformerId | PERFORMER_ID | — | — |
| 15 | ApprovalHistoryPEOPerformerType | PERFORMER_TYPE | — | — |
| 16 | ApprovalHistoryPEOSequenceNum | SEQUENCE_NUM | — | ✅ |
| 17 | ApprovalHistoryPEOVendorId | VENDOR_ID | — | — |

### [[poz_bi_appr_user_comments_v|POZ_BI_APPR_USER_COMMENTS_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ApprovalUserCommentPEOActionSeqNum | ACTION_SEQ_NUM | — | — |
| 2 | ApprovalUserCommentPEOAmxIdentificationKey | AMX_IDENTIFICATION_KEY | — | — |
| 3 | ApprovalUserCommentPEOLatestComment | LATEST_COMMENT | — | — |
| 4 | ApprovalUserCommentPEOPerformerId | PERFORMER_ID | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
