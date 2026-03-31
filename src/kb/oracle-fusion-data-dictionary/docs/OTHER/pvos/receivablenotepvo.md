---
id: DOC-OTHER-PVO-ReceivableNotePVO
doc_type: system-doc
title: "ReceivableNotePVO — PVO Cross-Module"
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
  - ReceivableNotePVO
  - receivablenotepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ReceivableNotePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Receivable Note. Acessa as tabelas: HZ_PARTIES, ZMM_NOTES.

**Caminho:** `FscmTopModelAM.NoteAM.ReceivableNotePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 71 | 2 | 1 | 7 | 10% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 2 atributos (1 BICC)
- [[zmm_notes|ZMM_NOTES]] — 69 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NoteCreatedByParty | PARTY_NAME | — | ✅ |
| 2 | NoteCreatedByPartyId | PARTY_ID | — | — |

### [[zmm_notes|ZMM_NOTES]]

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
| 14 | Attribute21 | ATTRIBUTE21 | — | — |
| 15 | Attribute22 | ATTRIBUTE22 | — | — |
| 16 | Attribute23 | ATTRIBUTE23 | — | — |
| 17 | Attribute24 | ATTRIBUTE24 | — | — |
| 18 | Attribute25 | ATTRIBUTE25 | — | — |
| 19 | Attribute26 | ATTRIBUTE26 | — | — |
| 20 | Attribute27 | ATTRIBUTE27 | — | — |
| 21 | Attribute28 | ATTRIBUTE28 | — | — |
| 22 | Attribute29 | ATTRIBUTE29 | — | — |
| 23 | Attribute3 | ATTRIBUTE3 | — | — |
| 24 | Attribute30 | ATTRIBUTE30 | — | — |
| 25 | Attribute4 | ATTRIBUTE4 | — | — |
| 26 | Attribute5 | ATTRIBUTE5 | — | — |
| 27 | Attribute6 | ATTRIBUTE6 | — | — |
| 28 | Attribute7 | ATTRIBUTE7 | — | — |
| 29 | Attribute8 | ATTRIBUTE8 | — | — |
| 30 | Attribute9 | ATTRIBUTE9 | — | — |
| 31 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 32 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 33 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 34 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 35 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 36 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 37 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 38 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 39 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 40 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 41 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 42 | ConflictId | CONFLICT_ID | — | — |
| 43 | ContactRelationshipId | CONTACT_RELATIONSHIP_ID | — | — |
| 44 | CorpCurrencyCode | CORP_CURRENCY_CODE | — | — |
| 45 | CreatedBy | CREATED_BY | — | — |
| 46 | CreationDate | CREATION_DATE | — | ✅ |
| 47 | CreatorPartyId | CREATOR_PARTY_ID | — | — |
| 48 | CurcyConvRateType | CURCY_CONV_RATE_TYPE | — | — |
| 49 | CurrencyCode | CURRENCY_CODE | — | — |
| 50 | LastUpdateDate | LAST_UPDATE_DATE | — | — |
| 51 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 52 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 53 | NoteAttributeCategory | NOTE_ATTRIBUTE_CATEGORY | — | — |
| 54 | NoteAttributeUid1 | NOTE_ATTRIBUTE_UID1 | — | — |
| 55 | NoteAttributeUid2 | NOTE_ATTRIBUTE_UID2 | — | — |
| 56 | NoteAttributeUid3 | NOTE_ATTRIBUTE_UID3 | — | — |
| 57 | NoteAttributeUid4 | NOTE_ATTRIBUTE_UID4 | — | — |
| 58 | NoteAttributeUid5 | NOTE_ATTRIBUTE_UID5 | — | — |
| 59 | NoteId | NOTE_ID | 🔑 | ✅ |
| 60 | NoteNumber | NOTE_NUMBER | — | — |
| 61 | NoteTitle | NOTE_TITLE | — | — |
| 62 | NoteTxt | NOTE_TXT | — | ✅ |
| 63 | NoteTypeCode | NOTE_TYPE_CODE | — | ✅ |
| 64 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 65 | ParentNoteId | PARENT_NOTE_ID | — | — |
| 66 | SourceObjectCode | SOURCE_OBJECT_CODE | — | — |
| 67 | SourceObjectUid | SOURCE_OBJECT_UID | — | — |
| 68 | UserLastUpdateDate | USER_LAST_UPDATE_DATE | — | ✅ |
| 69 | VisibilityCode | VISIBILITY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
