---
id: DOC-OTHER-PVO-FndDocumentTranslationExtractPVO
doc_type: system-doc
title: "FndDocumentTranslationExtractPVO — PVO Cross-Module"
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
  - FndDocumentTranslationExtractPVO
  - fnddocumenttranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FndDocumentTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fnd Document Translation Extract. Acessa as tabelas: FND_DOCUMENTS_TL.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HCMExtractAM.CommonBiccExtractAM.FndDocumentTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 36 | 1 | 3 | 36 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fnd_documents_tl|FND_DOCUMENTS_TL]] — 36 atributos (3 PKs, 36 BICC)

---

## ⚙️ Atributos

### [[fnd_documents_tl|FND_DOCUMENTS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CecFileId | CEC_FILE_ID | — | ✅ |
| 2 | CecParentId | CEC_PARENT_ID | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | DmDocumentId | DM_DOCUMENT_ID | — | ✅ |
| 7 | DmFolderPath | DM_FOLDER_PATH | — | ✅ |
| 8 | DmNode | DM_NODE | — | ✅ |
| 9 | DmRepository | DM_REPOSITORY | — | ✅ |
| 10 | DmType | DM_TYPE | — | ✅ |
| 11 | DmVersionNumber | DM_VERSION_NUMBER | — | ✅ |
| 12 | DocumentId | DOCUMENT_ID | 🔑 | ✅ |
| 13 | DownloadStatus | DOWNLOAD_STATUS | — | ✅ |
| 14 | EntAppShortName | ENT_APP_SHORT_NAME | — | ✅ |
| 15 | EnterpriseId | ENTERPRISE_ID | 🔑 | ✅ |
| 16 | FileName | FILE_NAME | — | ✅ |
| 17 | Language | LANGUAGE | 🔑 | ✅ |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ObjectBucket | OBJECT_BUCKET | — | ✅ |
| 22 | ObjectContentType | OBJECT_CONTENT_TYPE | — | ✅ |
| 23 | ObjectName | OBJECT_NAME | — | ✅ |
| 24 | ObjectSize | OBJECT_SIZE | — | ✅ |
| 25 | ProgramApplicationId | PROGRAM_APPLICATION_ID | — | ✅ |
| 26 | ProgramId | PROGRAM_ID | — | ✅ |
| 27 | ProgramUpdateDate | PROGRAM_UPDATE_DATE | — | ✅ |
| 28 | RequestId | REQUEST_ID | — | ✅ |
| 29 | SourceContentType | SOURCE_CONTENT_TYPE | — | ✅ |
| 30 | SourceLang | SOURCE_LANG | — | ✅ |
| 31 | Status | STATUS | — | ✅ |
| 32 | Title | TITLE | — | ✅ |
| 33 | TrackerId | TRACKER_ID | — | ✅ |
| 34 | TrustedFlag | TRUSTED_FLAG | — | ✅ |
| 35 | Uri | URI | — | ✅ |
| 36 | Url | URL | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
