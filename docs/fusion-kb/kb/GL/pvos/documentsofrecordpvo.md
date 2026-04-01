---
id: DOC-GL-PVO-DocumentsOfRecordPVO
doc_type: system-doc
title: "DocumentsOfRecordPVO — PVO General Ledger"
system: Oracle Fusion Cloud ERP
module: General Ledger
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - gl
  - data-dictionary
  - pvo
  - bicc
aliases:
  - DocumentsOfRecordPVO
  - documentsofrecordpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# DocumentsOfRecordPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Documents Of Record. Acessa as tabelas: HR_DOR_REPORTING_LIST_V.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.DocumentOfRecordsAM.DocumentsOfRecordPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 192 | 1 | 1 | 22 | 11% |

---

## 🔗 Tabelas Relacionadas

- [[hr_dor_reporting_list_v|HR_DOR_REPORTING_LIST_V]] — 192 atributos (1 PKs, 22 BICC)

---

## ⚙️ Atributos

### [[hr_dor_reporting_list_v|HR_DOR_REPORTING_LIST_V]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DocumentsOfRecordId | DOCUMENTS_OF_RECORD_ID | 🔑 | ✅ |
| 2 | DocumentsOfRecordPEOAssignmentId | ASSIGNMENT_ID | — | — |
| 3 | DocumentsOfRecordPEOComments | COMMENTS | — | ✅ |
| 4 | DocumentsOfRecordPEOCreatedBy | CREATED_BY | — | ✅ |
| 5 | DocumentsOfRecordPEOCreationDate | CREATION_DATE | — | ✅ |
| 6 | DocumentsOfRecordPEOCreationSource | CREATION_SOURCE | — | — |
| 7 | DocumentsOfRecordPEODateFrom | DATE_FROM | — | ✅ |
| 8 | DocumentsOfRecordPEODateTo | DATE_TO | — | ✅ |
| 9 | DocumentsOfRecordPEODeiAttribute1 | DEI_ATTRIBUTE1 | — | — |
| 10 | DocumentsOfRecordPEODeiAttribute10 | DEI_ATTRIBUTE10 | — | — |
| 11 | DocumentsOfRecordPEODeiAttribute11 | DEI_ATTRIBUTE11 | — | — |
| 12 | DocumentsOfRecordPEODeiAttribute12 | DEI_ATTRIBUTE12 | — | — |
| 13 | DocumentsOfRecordPEODeiAttribute13 | DEI_ATTRIBUTE13 | — | — |
| 14 | DocumentsOfRecordPEODeiAttribute14 | DEI_ATTRIBUTE14 | — | — |
| 15 | DocumentsOfRecordPEODeiAttribute15 | DEI_ATTRIBUTE15 | — | — |
| 16 | DocumentsOfRecordPEODeiAttribute16 | DEI_ATTRIBUTE16 | — | — |
| 17 | DocumentsOfRecordPEODeiAttribute17 | DEI_ATTRIBUTE17 | — | — |
| 18 | DocumentsOfRecordPEODeiAttribute18 | DEI_ATTRIBUTE18 | — | — |
| 19 | DocumentsOfRecordPEODeiAttribute19 | DEI_ATTRIBUTE19 | — | — |
| 20 | DocumentsOfRecordPEODeiAttribute2 | DEI_ATTRIBUTE2 | — | — |
| 21 | DocumentsOfRecordPEODeiAttribute20 | DEI_ATTRIBUTE20 | — | — |
| 22 | DocumentsOfRecordPEODeiAttribute21 | DEI_ATTRIBUTE21 | — | — |
| 23 | DocumentsOfRecordPEODeiAttribute22 | DEI_ATTRIBUTE22 | — | — |
| 24 | DocumentsOfRecordPEODeiAttribute23 | DEI_ATTRIBUTE23 | — | — |
| 25 | DocumentsOfRecordPEODeiAttribute24 | DEI_ATTRIBUTE24 | — | — |
| 26 | DocumentsOfRecordPEODeiAttribute25 | DEI_ATTRIBUTE25 | — | — |
| 27 | DocumentsOfRecordPEODeiAttribute26 | DEI_ATTRIBUTE26 | — | — |
| 28 | DocumentsOfRecordPEODeiAttribute27 | DEI_ATTRIBUTE27 | — | — |
| 29 | DocumentsOfRecordPEODeiAttribute28 | DEI_ATTRIBUTE28 | — | — |
| 30 | DocumentsOfRecordPEODeiAttribute29 | DEI_ATTRIBUTE29 | — | — |
| 31 | DocumentsOfRecordPEODeiAttribute3 | DEI_ATTRIBUTE3 | — | — |
| 32 | DocumentsOfRecordPEODeiAttribute30 | DEI_ATTRIBUTE30 | — | — |
| 33 | DocumentsOfRecordPEODeiAttribute31 | DEI_ATTRIBUTE31 | — | — |
| 34 | DocumentsOfRecordPEODeiAttribute32 | DEI_ATTRIBUTE32 | — | — |
| 35 | DocumentsOfRecordPEODeiAttribute33 | DEI_ATTRIBUTE33 | — | — |
| 36 | DocumentsOfRecordPEODeiAttribute34 | DEI_ATTRIBUTE34 | — | — |
| 37 | DocumentsOfRecordPEODeiAttribute35 | DEI_ATTRIBUTE35 | — | — |
| 38 | DocumentsOfRecordPEODeiAttribute36 | DEI_ATTRIBUTE36 | — | — |
| 39 | DocumentsOfRecordPEODeiAttribute37 | DEI_ATTRIBUTE37 | — | — |
| 40 | DocumentsOfRecordPEODeiAttribute38 | DEI_ATTRIBUTE38 | — | — |
| 41 | DocumentsOfRecordPEODeiAttribute39 | DEI_ATTRIBUTE39 | — | — |
| 42 | DocumentsOfRecordPEODeiAttribute4 | DEI_ATTRIBUTE4 | — | — |
| 43 | DocumentsOfRecordPEODeiAttribute40 | DEI_ATTRIBUTE40 | — | — |
| 44 | DocumentsOfRecordPEODeiAttribute5 | DEI_ATTRIBUTE5 | — | — |
| 45 | DocumentsOfRecordPEODeiAttribute6 | DEI_ATTRIBUTE6 | — | — |
| 46 | DocumentsOfRecordPEODeiAttribute7 | DEI_ATTRIBUTE7 | — | — |
| 47 | DocumentsOfRecordPEODeiAttribute8 | DEI_ATTRIBUTE8 | — | — |
| 48 | DocumentsOfRecordPEODeiAttribute9 | DEI_ATTRIBUTE9 | — | — |
| 49 | DocumentsOfRecordPEODeiAttributeCategory | DEI_ATTRIBUTE_CATEGORY | — | — |
| 50 | DocumentsOfRecordPEODeiAttributeDate1 | DEI_ATTRIBUTE_DATE1 | — | — |
| 51 | DocumentsOfRecordPEODeiAttributeDate10 | DEI_ATTRIBUTE_DATE10 | — | — |
| 52 | DocumentsOfRecordPEODeiAttributeDate11 | DEI_ATTRIBUTE_DATE11 | — | — |
| 53 | DocumentsOfRecordPEODeiAttributeDate12 | DEI_ATTRIBUTE_DATE12 | — | — |
| 54 | DocumentsOfRecordPEODeiAttributeDate13 | DEI_ATTRIBUTE_DATE13 | — | — |
| 55 | DocumentsOfRecordPEODeiAttributeDate14 | DEI_ATTRIBUTE_DATE14 | — | — |
| 56 | DocumentsOfRecordPEODeiAttributeDate15 | DEI_ATTRIBUTE_DATE15 | — | — |
| 57 | DocumentsOfRecordPEODeiAttributeDate2 | DEI_ATTRIBUTE_DATE2 | — | — |
| 58 | DocumentsOfRecordPEODeiAttributeDate3 | DEI_ATTRIBUTE_DATE3 | — | — |
| 59 | DocumentsOfRecordPEODeiAttributeDate4 | DEI_ATTRIBUTE_DATE4 | — | — |
| 60 | DocumentsOfRecordPEODeiAttributeDate5 | DEI_ATTRIBUTE_DATE5 | — | — |
| 61 | DocumentsOfRecordPEODeiAttributeDate6 | DEI_ATTRIBUTE_DATE6 | — | — |
| 62 | DocumentsOfRecordPEODeiAttributeDate7 | DEI_ATTRIBUTE_DATE7 | — | — |
| 63 | DocumentsOfRecordPEODeiAttributeDate8 | DEI_ATTRIBUTE_DATE8 | — | — |
| 64 | DocumentsOfRecordPEODeiAttributeDate9 | DEI_ATTRIBUTE_DATE9 | — | — |
| 65 | DocumentsOfRecordPEODeiAttributeNumber1 | DEI_ATTRIBUTE_NUMBER1 | — | — |
| 66 | DocumentsOfRecordPEODeiAttributeNumber10 | DEI_ATTRIBUTE_NUMBER10 | — | — |
| 67 | DocumentsOfRecordPEODeiAttributeNumber11 | DEI_ATTRIBUTE_NUMBER11 | — | — |
| 68 | DocumentsOfRecordPEODeiAttributeNumber12 | DEI_ATTRIBUTE_NUMBER12 | — | — |
| 69 | DocumentsOfRecordPEODeiAttributeNumber13 | DEI_ATTRIBUTE_NUMBER13 | — | — |
| 70 | DocumentsOfRecordPEODeiAttributeNumber14 | DEI_ATTRIBUTE_NUMBER14 | — | — |
| 71 | DocumentsOfRecordPEODeiAttributeNumber15 | DEI_ATTRIBUTE_NUMBER15 | — | — |
| 72 | DocumentsOfRecordPEODeiAttributeNumber16 | DEI_ATTRIBUTE_NUMBER16 | — | — |
| 73 | DocumentsOfRecordPEODeiAttributeNumber17 | DEI_ATTRIBUTE_NUMBER17 | — | — |
| 74 | DocumentsOfRecordPEODeiAttributeNumber18 | DEI_ATTRIBUTE_NUMBER18 | — | — |
| 75 | DocumentsOfRecordPEODeiAttributeNumber19 | DEI_ATTRIBUTE_NUMBER19 | — | — |
| 76 | DocumentsOfRecordPEODeiAttributeNumber2 | DEI_ATTRIBUTE_NUMBER2 | — | — |
| 77 | DocumentsOfRecordPEODeiAttributeNumber20 | DEI_ATTRIBUTE_NUMBER20 | — | — |
| 78 | DocumentsOfRecordPEODeiAttributeNumber3 | DEI_ATTRIBUTE_NUMBER3 | — | — |
| 79 | DocumentsOfRecordPEODeiAttributeNumber4 | DEI_ATTRIBUTE_NUMBER4 | — | — |
| 80 | DocumentsOfRecordPEODeiAttributeNumber5 | DEI_ATTRIBUTE_NUMBER5 | — | — |
| 81 | DocumentsOfRecordPEODeiAttributeNumber6 | DEI_ATTRIBUTE_NUMBER6 | — | — |
| 82 | DocumentsOfRecordPEODeiAttributeNumber7 | DEI_ATTRIBUTE_NUMBER7 | — | — |
| 83 | DocumentsOfRecordPEODeiAttributeNumber8 | DEI_ATTRIBUTE_NUMBER8 | — | — |
| 84 | DocumentsOfRecordPEODeiAttributeNumber9 | DEI_ATTRIBUTE_NUMBER9 | — | — |
| 85 | DocumentsOfRecordPEODeiAttributeTimestamp1 | DEI_ATTRIBUTE_TIMESTAMP1 | — | — |
| 86 | DocumentsOfRecordPEODeiAttributeTimestamp2 | DEI_ATTRIBUTE_TIMESTAMP2 | — | — |
| 87 | DocumentsOfRecordPEODeiAttributeTimestamp3 | DEI_ATTRIBUTE_TIMESTAMP3 | — | — |
| 88 | DocumentsOfRecordPEODeiAttributeTimestamp4 | DEI_ATTRIBUTE_TIMESTAMP4 | — | — |
| 89 | DocumentsOfRecordPEODeiAttributeTimestamp5 | DEI_ATTRIBUTE_TIMESTAMP5 | — | — |
| 90 | DocumentsOfRecordPEODeiInformation1 | DEI_INFORMATION1 | — | — |
| 91 | DocumentsOfRecordPEODeiInformation10 | DEI_INFORMATION10 | — | — |
| 92 | DocumentsOfRecordPEODeiInformation11 | DEI_INFORMATION11 | — | — |
| 93 | DocumentsOfRecordPEODeiInformation12 | DEI_INFORMATION12 | — | — |
| 94 | DocumentsOfRecordPEODeiInformation13 | DEI_INFORMATION13 | — | — |
| 95 | DocumentsOfRecordPEODeiInformation14 | DEI_INFORMATION14 | — | — |
| 96 | DocumentsOfRecordPEODeiInformation15 | DEI_INFORMATION15 | — | — |
| 97 | DocumentsOfRecordPEODeiInformation16 | DEI_INFORMATION16 | — | — |
| 98 | DocumentsOfRecordPEODeiInformation17 | DEI_INFORMATION17 | — | — |
| 99 | DocumentsOfRecordPEODeiInformation18 | DEI_INFORMATION18 | — | — |
| 100 | DocumentsOfRecordPEODeiInformation19 | DEI_INFORMATION19 | — | — |
| 101 | DocumentsOfRecordPEODeiInformation2 | DEI_INFORMATION2 | — | — |
| 102 | DocumentsOfRecordPEODeiInformation20 | DEI_INFORMATION20 | — | — |
| 103 | DocumentsOfRecordPEODeiInformation21 | DEI_INFORMATION21 | — | — |
| 104 | DocumentsOfRecordPEODeiInformation22 | DEI_INFORMATION22 | — | — |
| 105 | DocumentsOfRecordPEODeiInformation23 | DEI_INFORMATION23 | — | — |
| 106 | DocumentsOfRecordPEODeiInformation24 | DEI_INFORMATION24 | — | — |
| 107 | DocumentsOfRecordPEODeiInformation25 | DEI_INFORMATION25 | — | — |
| 108 | DocumentsOfRecordPEODeiInformation26 | DEI_INFORMATION26 | — | — |
| 109 | DocumentsOfRecordPEODeiInformation27 | DEI_INFORMATION27 | — | — |
| 110 | DocumentsOfRecordPEODeiInformation28 | DEI_INFORMATION28 | — | — |
| 111 | DocumentsOfRecordPEODeiInformation29 | DEI_INFORMATION29 | — | — |
| 112 | DocumentsOfRecordPEODeiInformation3 | DEI_INFORMATION3 | — | — |
| 113 | DocumentsOfRecordPEODeiInformation30 | DEI_INFORMATION30 | — | — |
| 114 | DocumentsOfRecordPEODeiInformation31 | DEI_INFORMATION31 | — | — |
| 115 | DocumentsOfRecordPEODeiInformation32 | DEI_INFORMATION32 | — | — |
| 116 | DocumentsOfRecordPEODeiInformation33 | DEI_INFORMATION33 | — | — |
| 117 | DocumentsOfRecordPEODeiInformation34 | DEI_INFORMATION34 | — | — |
| 118 | DocumentsOfRecordPEODeiInformation35 | DEI_INFORMATION35 | — | — |
| 119 | DocumentsOfRecordPEODeiInformation36 | DEI_INFORMATION36 | — | — |
| 120 | DocumentsOfRecordPEODeiInformation37 | DEI_INFORMATION37 | — | — |
| 121 | DocumentsOfRecordPEODeiInformation38 | DEI_INFORMATION38 | — | — |
| 122 | DocumentsOfRecordPEODeiInformation39 | DEI_INFORMATION39 | — | — |
| 123 | DocumentsOfRecordPEODeiInformation4 | DEI_INFORMATION4 | — | — |
| 124 | DocumentsOfRecordPEODeiInformation40 | DEI_INFORMATION40 | — | — |
| 125 | DocumentsOfRecordPEODeiInformation5 | DEI_INFORMATION5 | — | — |
| 126 | DocumentsOfRecordPEODeiInformation6 | DEI_INFORMATION6 | — | — |
| 127 | DocumentsOfRecordPEODeiInformation7 | DEI_INFORMATION7 | — | — |
| 128 | DocumentsOfRecordPEODeiInformation8 | DEI_INFORMATION8 | — | — |
| 129 | DocumentsOfRecordPEODeiInformation9 | DEI_INFORMATION9 | — | — |
| 130 | DocumentsOfRecordPEODeiInformationCategory | DEI_INFORMATION_CATEGORY | — | — |
| 131 | DocumentsOfRecordPEODeiInformationDate1 | DEI_INFORMATION_DATE1 | — | — |
| 132 | DocumentsOfRecordPEODeiInformationDate10 | DEI_INFORMATION_DATE10 | — | — |
| 133 | DocumentsOfRecordPEODeiInformationDate11 | DEI_INFORMATION_DATE11 | — | — |
| 134 | DocumentsOfRecordPEODeiInformationDate12 | DEI_INFORMATION_DATE12 | — | — |
| 135 | DocumentsOfRecordPEODeiInformationDate13 | DEI_INFORMATION_DATE13 | — | — |
| 136 | DocumentsOfRecordPEODeiInformationDate14 | DEI_INFORMATION_DATE14 | — | — |
| 137 | DocumentsOfRecordPEODeiInformationDate15 | DEI_INFORMATION_DATE15 | — | — |
| 138 | DocumentsOfRecordPEODeiInformationDate2 | DEI_INFORMATION_DATE2 | — | — |
| 139 | DocumentsOfRecordPEODeiInformationDate3 | DEI_INFORMATION_DATE3 | — | — |
| 140 | DocumentsOfRecordPEODeiInformationDate4 | DEI_INFORMATION_DATE4 | — | — |
| 141 | DocumentsOfRecordPEODeiInformationDate5 | DEI_INFORMATION_DATE5 | — | — |
| 142 | DocumentsOfRecordPEODeiInformationDate6 | DEI_INFORMATION_DATE6 | — | — |
| 143 | DocumentsOfRecordPEODeiInformationDate7 | DEI_INFORMATION_DATE7 | — | — |
| 144 | DocumentsOfRecordPEODeiInformationDate8 | DEI_INFORMATION_DATE8 | — | — |
| 145 | DocumentsOfRecordPEODeiInformationDate9 | DEI_INFORMATION_DATE9 | — | — |
| 146 | DocumentsOfRecordPEODeiInformationNumber1 | DEI_INFORMATION_NUMBER1 | — | — |
| 147 | DocumentsOfRecordPEODeiInformationNumber10 | DEI_INFORMATION_NUMBER10 | — | — |
| 148 | DocumentsOfRecordPEODeiInformationNumber11 | DEI_INFORMATION_NUMBER11 | — | — |
| 149 | DocumentsOfRecordPEODeiInformationNumber12 | DEI_INFORMATION_NUMBER12 | — | — |
| 150 | DocumentsOfRecordPEODeiInformationNumber13 | DEI_INFORMATION_NUMBER13 | — | — |
| 151 | DocumentsOfRecordPEODeiInformationNumber14 | DEI_INFORMATION_NUMBER14 | — | — |
| 152 | DocumentsOfRecordPEODeiInformationNumber15 | DEI_INFORMATION_NUMBER15 | — | — |
| 153 | DocumentsOfRecordPEODeiInformationNumber16 | DEI_INFORMATION_NUMBER16 | — | — |
| 154 | DocumentsOfRecordPEODeiInformationNumber17 | DEI_INFORMATION_NUMBER17 | — | — |
| 155 | DocumentsOfRecordPEODeiInformationNumber18 | DEI_INFORMATION_NUMBER18 | — | — |
| 156 | DocumentsOfRecordPEODeiInformationNumber19 | DEI_INFORMATION_NUMBER19 | — | — |
| 157 | DocumentsOfRecordPEODeiInformationNumber2 | DEI_INFORMATION_NUMBER2 | — | — |
| 158 | DocumentsOfRecordPEODeiInformationNumber20 | DEI_INFORMATION_NUMBER20 | — | — |
| 159 | DocumentsOfRecordPEODeiInformationNumber3 | DEI_INFORMATION_NUMBER3 | — | — |
| 160 | DocumentsOfRecordPEODeiInformationNumber4 | DEI_INFORMATION_NUMBER4 | — | — |
| 161 | DocumentsOfRecordPEODeiInformationNumber5 | DEI_INFORMATION_NUMBER5 | — | — |
| 162 | DocumentsOfRecordPEODeiInformationNumber6 | DEI_INFORMATION_NUMBER6 | — | — |
| 163 | DocumentsOfRecordPEODeiInformationNumber7 | DEI_INFORMATION_NUMBER7 | — | — |
| 164 | DocumentsOfRecordPEODeiInformationNumber8 | DEI_INFORMATION_NUMBER8 | — | — |
| 165 | DocumentsOfRecordPEODeiInformationNumber9 | DEI_INFORMATION_NUMBER9 | — | — |
| 166 | DocumentsOfRecordPEODeiInformationTimestamp1 | DEI_INFORMATION_TIMESTAMP1 | — | — |
| 167 | DocumentsOfRecordPEODeiInformationTimestamp2 | DEI_INFORMATION_TIMESTAMP2 | — | — |
| 168 | DocumentsOfRecordPEODeiInformationTimestamp3 | DEI_INFORMATION_TIMESTAMP3 | — | — |
| 169 | DocumentsOfRecordPEODeiInformationTimestamp4 | DEI_INFORMATION_TIMESTAMP4 | — | — |
| 170 | DocumentsOfRecordPEODeiInformationTimestamp5 | DEI_INFORMATION_TIMESTAMP5 | — | — |
| 171 | DocumentsOfRecordPEODocumentCode | DOCUMENT_CODE | — | ✅ |
| 172 | DocumentsOfRecordPEODocumentName | DOCUMENT_NAME | — | ✅ |
| 173 | DocumentsOfRecordPEODocumentNumber | DOCUMENT_NUMBER | — | ✅ |
| 174 | DocumentsOfRecordPEODocumentTypeId | DOCUMENT_TYPE_ID | — | — |
| 175 | DocumentsOfRecordPEOEnterpriseId | ENTERPRISE_ID | — | — |
| 176 | DocumentsOfRecordPEOIssuedDate | ISSUED_DATE | — | ✅ |
| 177 | DocumentsOfRecordPEOIssuingAuthority | ISSUING_AUTHORITY | — | ✅ |
| 178 | DocumentsOfRecordPEOIssuingCountry | ISSUING_COUNTRY | — | ✅ |
| 179 | DocumentsOfRecordPEOIssuingLocation | ISSUING_LOCATION | — | ✅ |
| 180 | DocumentsOfRecordPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 181 | DocumentsOfRecordPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 182 | DocumentsOfRecordPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 183 | DocumentsOfRecordPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 184 | DocumentsOfRecordPEOPersonId | PERSON_ID | — | — |
| 185 | DocumentsOfRecordPEOPublish | PUBLISH | — | — |
| 186 | DocumentsOfRecordPEOPublishDate | PUBLISH_DATE | — | ✅ |
| 187 | DocumentsOfRecordPEORelatedObjectId | RELATED_OBJECT_ID | — | ✅ |
| 188 | DocumentsOfRecordPEORelatedObjectIdCol | RELATED_OBJECT_ID_COL | — | ✅ |
| 189 | DocumentsOfRecordPEORelatedObjectName | RELATED_OBJECT_NAME | — | ✅ |
| 190 | DocumentsOfRecordPEOStatus | STATUS | — | ✅ |
| 191 | DocumentsOfRecordPEOVerifiedBy | VERIFIED_BY | — | ✅ |
| 192 | DocumentsOfRecordPEOVerifiedDate | VERIFIED_DATE | — | ✅ |

---

## 📚 Referências

- [[gl-module-data-dictionary]] — Dossiê do módulo GL
