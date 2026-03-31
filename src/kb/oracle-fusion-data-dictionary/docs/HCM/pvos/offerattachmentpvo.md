---
id: DOC-HCM-PVO-OfferAttachmentPVO
doc_type: system-doc
title: "OfferAttachmentPVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - OfferAttachmentPVO
  - offerattachmentpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# OfferAttachmentPVO

## 📌 Visão Geral

Extrai documentos anexados a ofertas de emprego no processo de recrutamento, incluindo tipo e categoria. Suporta rastreabilidade documental de propostas de contratação.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecruitingCommonAM.OfferAttachmentPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 184 | 2 | 1 | 11 | 6% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]] — 153 atributos (1 PKs, 4 BICC)
- [[fnd_documents_vl|FND_DOCUMENTS_VL]] — 31 atributos (7 BICC)

---

## ⚙️ Atributos

### [[fnd_attached_documents|FND_ATTACHED_DOCUMENTS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AttachedDocumentId | ATTACHED_DOCUMENT_ID | 🔑 | ✅ |
| 2 | Attribute1 | ATTRIBUTE1 | — | — |
| 3 | Attribute10 | ATTRIBUTE10 | — | — |
| 4 | Attribute100 | ATTRIBUTE100 | — | — |
| 5 | Attribute11 | ATTRIBUTE11 | — | — |
| 6 | Attribute12 | ATTRIBUTE12 | — | — |
| 7 | Attribute13 | ATTRIBUTE13 | — | — |
| 8 | Attribute14 | ATTRIBUTE14 | — | — |
| 9 | Attribute15 | ATTRIBUTE15 | — | — |
| 10 | Attribute16 | ATTRIBUTE16 | — | — |
| 11 | Attribute17 | ATTRIBUTE17 | — | — |
| 12 | Attribute18 | ATTRIBUTE18 | — | — |
| 13 | Attribute19 | ATTRIBUTE19 | — | — |
| 14 | Attribute2 | ATTRIBUTE2 | — | — |
| 15 | Attribute20 | ATTRIBUTE20 | — | — |
| 16 | Attribute21 | ATTRIBUTE21 | — | — |
| 17 | Attribute22 | ATTRIBUTE22 | — | — |
| 18 | Attribute23 | ATTRIBUTE23 | — | — |
| 19 | Attribute24 | ATTRIBUTE24 | — | — |
| 20 | Attribute25 | ATTRIBUTE25 | — | — |
| 21 | Attribute26 | ATTRIBUTE26 | — | — |
| 22 | Attribute27 | ATTRIBUTE27 | — | — |
| 23 | Attribute28 | ATTRIBUTE28 | — | — |
| 24 | Attribute29 | ATTRIBUTE29 | — | — |
| 25 | Attribute3 | ATTRIBUTE3 | — | — |
| 26 | Attribute30 | ATTRIBUTE30 | — | — |
| 27 | Attribute31 | ATTRIBUTE31 | — | — |
| 28 | Attribute32 | ATTRIBUTE32 | — | — |
| 29 | Attribute33 | ATTRIBUTE33 | — | — |
| 30 | Attribute34 | ATTRIBUTE34 | — | — |
| 31 | Attribute35 | ATTRIBUTE35 | — | — |
| 32 | Attribute36 | ATTRIBUTE36 | — | — |
| 33 | Attribute37 | ATTRIBUTE37 | — | — |
| 34 | Attribute38 | ATTRIBUTE38 | — | — |
| 35 | Attribute39 | ATTRIBUTE39 | — | — |
| 36 | Attribute4 | ATTRIBUTE4 | — | — |
| 37 | Attribute40 | ATTRIBUTE40 | — | — |
| 38 | Attribute41 | ATTRIBUTE41 | — | — |
| 39 | Attribute42 | ATTRIBUTE42 | — | — |
| 40 | Attribute43 | ATTRIBUTE43 | — | — |
| 41 | Attribute44 | ATTRIBUTE44 | — | — |
| 42 | Attribute45 | ATTRIBUTE45 | — | — |
| 43 | Attribute46 | ATTRIBUTE46 | — | — |
| 44 | Attribute47 | ATTRIBUTE47 | — | — |
| 45 | Attribute48 | ATTRIBUTE48 | — | — |
| 46 | Attribute49 | ATTRIBUTE49 | — | — |
| 47 | Attribute5 | ATTRIBUTE5 | — | — |
| 48 | Attribute50 | ATTRIBUTE50 | — | — |
| 49 | Attribute51 | ATTRIBUTE51 | — | — |
| 50 | Attribute52 | ATTRIBUTE52 | — | — |
| 51 | Attribute53 | ATTRIBUTE53 | — | — |
| 52 | Attribute54 | ATTRIBUTE54 | — | — |
| 53 | Attribute55 | ATTRIBUTE55 | — | — |
| 54 | Attribute56 | ATTRIBUTE56 | — | — |
| 55 | Attribute57 | ATTRIBUTE57 | — | — |
| 56 | Attribute58 | ATTRIBUTE58 | — | — |
| 57 | Attribute59 | ATTRIBUTE59 | — | — |
| 58 | Attribute6 | ATTRIBUTE6 | — | — |
| 59 | Attribute60 | ATTRIBUTE60 | — | — |
| 60 | Attribute61 | ATTRIBUTE61 | — | — |
| 61 | Attribute62 | ATTRIBUTE62 | — | — |
| 62 | Attribute63 | ATTRIBUTE63 | — | — |
| 63 | Attribute64 | ATTRIBUTE64 | — | — |
| 64 | Attribute65 | ATTRIBUTE65 | — | — |
| 65 | Attribute66 | ATTRIBUTE66 | — | — |
| 66 | Attribute67 | ATTRIBUTE67 | — | — |
| 67 | Attribute68 | ATTRIBUTE68 | — | — |
| 68 | Attribute69 | ATTRIBUTE69 | — | — |
| 69 | Attribute7 | ATTRIBUTE7 | — | — |
| 70 | Attribute70 | ATTRIBUTE70 | — | — |
| 71 | Attribute71 | ATTRIBUTE71 | — | — |
| 72 | Attribute72 | ATTRIBUTE72 | — | — |
| 73 | Attribute73 | ATTRIBUTE73 | — | — |
| 74 | Attribute74 | ATTRIBUTE74 | — | — |
| 75 | Attribute75 | ATTRIBUTE75 | — | — |
| 76 | Attribute76 | ATTRIBUTE76 | — | — |
| 77 | Attribute77 | ATTRIBUTE77 | — | — |
| 78 | Attribute78 | ATTRIBUTE78 | — | — |
| 79 | Attribute79 | ATTRIBUTE79 | — | — |
| 80 | Attribute8 | ATTRIBUTE8 | — | — |
| 81 | Attribute80 | ATTRIBUTE80 | — | — |
| 82 | Attribute81 | ATTRIBUTE81 | — | — |
| 83 | Attribute82 | ATTRIBUTE82 | — | — |
| 84 | Attribute83 | ATTRIBUTE83 | — | — |
| 85 | Attribute84 | ATTRIBUTE84 | — | — |
| 86 | Attribute85 | ATTRIBUTE85 | — | — |
| 87 | Attribute86 | ATTRIBUTE86 | — | — |
| 88 | Attribute87 | ATTRIBUTE87 | — | — |
| 89 | Attribute88 | ATTRIBUTE88 | — | — |
| 90 | Attribute89 | ATTRIBUTE89 | — | — |
| 91 | Attribute9 | ATTRIBUTE9 | — | — |
| 92 | Attribute90 | ATTRIBUTE90 | — | — |
| 93 | Attribute91 | ATTRIBUTE91 | — | — |
| 94 | Attribute92 | ATTRIBUTE92 | — | — |
| 95 | Attribute93 | ATTRIBUTE93 | — | — |
| 96 | Attribute94 | ATTRIBUTE94 | — | — |
| 97 | Attribute95 | ATTRIBUTE95 | — | — |
| 98 | Attribute96 | ATTRIBUTE96 | — | — |
| 99 | Attribute97 | ATTRIBUTE97 | — | — |
| 100 | Attribute98 | ATTRIBUTE98 | — | — |
| 101 | Attribute99 | ATTRIBUTE99 | — | — |
| 102 | AttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 103 | AttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 104 | AttributeDate10 | ATTRIBUTE_DATE10 | — | — |
| 105 | AttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 106 | AttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 107 | AttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 108 | AttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 109 | AttributeDate6 | ATTRIBUTE_DATE6 | — | — |
| 110 | AttributeDate7 | ATTRIBUTE_DATE7 | — | — |
| 111 | AttributeDate8 | ATTRIBUTE_DATE8 | — | — |
| 112 | AttributeDate9 | ATTRIBUTE_DATE9 | — | — |
| 113 | AttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 114 | AttributeNumber10 | ATTRIBUTE_NUMBER10 | — | — |
| 115 | AttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 116 | AttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 117 | AttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 118 | AttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 119 | AttributeNumber6 | ATTRIBUTE_NUMBER6 | — | — |
| 120 | AttributeNumber7 | ATTRIBUTE_NUMBER7 | — | — |
| 121 | AttributeNumber8 | ATTRIBUTE_NUMBER8 | — | — |
| 122 | AttributeNumber9 | ATTRIBUTE_NUMBER9 | — | — |
| 123 | AttributeTimestamp1 | ATTRIBUTE_TIMESTAMP1 | — | — |
| 124 | AttributeTimestamp10 | ATTRIBUTE_TIMESTAMP10 | — | — |
| 125 | AttributeTimestamp2 | ATTRIBUTE_TIMESTAMP2 | — | — |
| 126 | AttributeTimestamp3 | ATTRIBUTE_TIMESTAMP3 | — | — |
| 127 | AttributeTimestamp4 | ATTRIBUTE_TIMESTAMP4 | — | — |
| 128 | AttributeTimestamp5 | ATTRIBUTE_TIMESTAMP5 | — | — |
| 129 | AttributeTimestamp6 | ATTRIBUTE_TIMESTAMP6 | — | — |
| 130 | AttributeTimestamp7 | ATTRIBUTE_TIMESTAMP7 | — | — |
| 131 | AttributeTimestamp8 | ATTRIBUTE_TIMESTAMP8 | — | — |
| 132 | AttributeTimestamp9 | ATTRIBUTE_TIMESTAMP9 | — | — |
| 133 | CategoryName | CATEGORY_NAME | — | ✅ |
| 134 | CreatedBy | CREATED_BY | — | ✅ |
| 135 | CreationDate | CREATION_DATE | — | — |
| 136 | DocumentId | DOCUMENT_ID | — | — |
| 137 | EntityAttributes | ENTITY_ATTRIBUTES | — | — |
| 138 | EntityName | ENTITY_NAME | — | — |
| 139 | ExpirationDate | EXPIRATION_DATE | — | — |
| 140 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 141 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 142 | LastUpdatedBy | LAST_UPDATED_BY | — | — |
| 143 | Pk1Value | PK1_VALUE | — | — |
| 144 | Pk2Value | PK2_VALUE | — | — |
| 145 | Pk3Value | PK3_VALUE | — | — |
| 146 | Pk4Value | PK4_VALUE | — | — |
| 147 | Pk5Value | PK5_VALUE | — | — |
| 148 | PrimaryCategoryFlag | PRIMARY_CATEGORY_FLAG | — | — |
| 149 | ProgramApplicationId | PROGRAM_APPLICATION_ID | — | — |
| 150 | ProgramId | PROGRAM_ID | — | — |
| 151 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | — |
| 152 | RequestId | REQUEST_ID | — | — |
| 153 | SeqNum | SEQ_NUM | — | — |

### [[fnd_documents_vl|FND_DOCUMENTS_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BaseDocumentId | BASE_DOCUMENT_ID | — | — |
| 2 | CreatedBy1 | CREATED_BY | — | — |
| 3 | CreationDate1 | CREATION_DATE | — | — |
| 4 | DatatypeCode | DATATYPE_CODE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | DmDocumentId | DM_DOCUMENT_ID | — | — |
| 7 | DmFolderPath | DM_FOLDER_PATH | — | — |
| 8 | DmNode | DM_NODE | — | — |
| 9 | DmRepository | DM_REPOSITORY | — | — |
| 10 | DmType | DM_TYPE | — | — |
| 11 | DmVersionNumber | DM_VERSION_NUMBER | — | — |
| 12 | DocumentAttributes | DOCUMENT_ATTRIBUTES | — | — |
| 13 | DocumentId1 | DOCUMENT_ID | — | — |
| 14 | DownloadStatus | DOWNLOAD_STATUS | — | — |
| 15 | EndDateActive | END_DATE_ACTIVE | — | — |
| 16 | EntAppShortName | ENT_APP_SHORT_NAME | — | — |
| 17 | FileName | FILE_NAME | — | ✅ |
| 18 | LastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 20 | LastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 21 | ProgramApplicationId1 | PROGRAM_APPLICATION_ID | — | — |
| 22 | ProgramId1 | PROGRAM_ID | — | — |
| 23 | ProgramUpdateDate1 | PROGRAM_UPDATE_DATE | — | — |
| 24 | RequestId1 | REQUEST_ID | — | — |
| 25 | StartDateActive | START_DATE_ACTIVE | — | — |
| 26 | Status | STATUS | — | — |
| 27 | Title | TITLE | — | ✅ |
| 28 | TrustedFlag | TRUSTED_FLAG | — | — |
| 29 | Uri | URI | — | ✅ |
| 30 | Url | URL | — | ✅ |
| 31 | UsageType | USAGE_TYPE | — | — |

---

## 📚 Referências

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
