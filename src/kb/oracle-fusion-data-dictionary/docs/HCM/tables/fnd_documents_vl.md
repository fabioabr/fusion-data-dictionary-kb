---
id: DOC-HCM-128
doc_type: system-doc
title: "FND_DOCUMENTS_VL — (título a preencher)"
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
  - FND_DOCUMENTS_VL
  - fnd_documents_vl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DOCUMENTS_VL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | BASE_DOCUMENT_ID | — | — | — | — | — | — |
| 2 | CREATED_BY | — | — | — | — | — | — |
| 3 | CREATION_DATE | — | — | — | — | — | — |
| 4 | DATATYPE_CODE | — | — | — | — | — | — |
| 5 | DESCRIPTION | — | — | — | — | — | — |
| 6 | DM_DOCUMENT_ID | — | — | — | — | — | — |
| 7 | DM_FOLDER_PATH | — | — | — | — | — | — |
| 8 | DM_NODE | — | — | — | — | — | — |
| 9 | DM_REPOSITORY | — | — | — | — | — | — |
| 10 | DM_TYPE | — | — | — | — | — | — |
| 11 | DM_VERSION_NUMBER | — | — | — | — | — | — |
| 12 | DOCUMENT_ATTRIBUTES | — | — | — | — | — | — |
| 13 | DOCUMENT_ID | — | — | — | — | — | — |
| 14 | DOWNLOAD_STATUS | — | — | — | — | — | — |
| 15 | END_DATE_ACTIVE | — | — | — | — | — | — |
| 16 | ENT_APP_SHORT_NAME | — | — | — | — | — | — |
| 17 | FILE_NAME | — | — | — | — | — | — |
| 18 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 19 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 20 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 21 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 22 | PROGRAM_ID | — | — | — | — | — | — |
| 23 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 24 | REQUEST_ID | — | — | — | — | — | — |
| 25 | START_DATE_ACTIVE | — | — | — | — | — | — |
| 26 | STATUS | — | — | — | — | — | — |
| 27 | TITLE | — | — | — | — | — | — |
| 28 | TRUSTED_FLAG | — | — | — | — | — | — |
| 29 | URI | — | — | — | — | — | — |
| 30 | URL | — | — | — | — | — | — |
| 31 | USAGE_TYPE | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[contentlibattachmentpvo|ContentLibAttachmentPVO]] (HCM · BICC: 2/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_DOCUMENT_ID | BaseDocumentId | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATATYPE_CODE | DatatypeCode | — |
| DESCRIPTION | Description | — |
| DM_DOCUMENT_ID | DmDocumentId | — |
| DM_FOLDER_PATH | DmFolderPath | — |
| DM_NODE | DmNode | — |
| DM_REPOSITORY | DmRepository | — |
| DM_TYPE | DmType | — |
| DM_VERSION_NUMBER | DmVersionNumber | — |
| DOCUMENT_ATTRIBUTES | DocumentAttributes | — |
| DOCUMENT_ID | DocumentId1 | — |
| DOWNLOAD_STATUS | DownloadStatus | — |
| END_DATE_ACTIVE | EndDateActive | — |
| ENT_APP_SHORT_NAME | EntAppShortName | — |
| FILE_NAME | FileName | — |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| PROGRAM_APPLICATION_ID | ProgramApplicationId1 | — |
| PROGRAM_ID | ProgramId1 | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate1 | — |
| REQUEST_ID | RequestId1 | — |
| START_DATE_ACTIVE | StartDateActive | — |
| STATUS | Status | — |
| TITLE | Title | ✅ |
| TRUSTED_FLAG | TrustedFlag | — |
| URI | Uri | — |
| URL | Url | — |
| USAGE_TYPE | UsageType | — |

### [[itemimageattachmentspvo|ItemImageAttachmentsPVO]] (OTHER · BICC: 5/6)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DATATYPE_CODE | DatatypeCode | — |
| DATATYPE_CODE | Type | ✅ |
| DESCRIPTION | Description | ✅ |
| DM_FOLDER_PATH | DmFolderPath | ✅ |
| DOCUMENT_ID | DocumentId | ✅ |
| TITLE | Title | ✅ |

### [[offerattachmentpvo|OfferAttachmentPVO]] (HCM · BICC: 7/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_DOCUMENT_ID | BaseDocumentId | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATATYPE_CODE | DatatypeCode | ✅ |
| DESCRIPTION | Description | ✅ |
| DM_DOCUMENT_ID | DmDocumentId | — |
| DM_FOLDER_PATH | DmFolderPath | — |
| DM_NODE | DmNode | — |
| DM_REPOSITORY | DmRepository | — |
| DM_TYPE | DmType | — |
| DM_VERSION_NUMBER | DmVersionNumber | — |
| DOCUMENT_ATTRIBUTES | DocumentAttributes | — |
| DOCUMENT_ID | DocumentId1 | — |
| DOWNLOAD_STATUS | DownloadStatus | — |
| END_DATE_ACTIVE | EndDateActive | — |
| ENT_APP_SHORT_NAME | EntAppShortName | — |
| FILE_NAME | FileName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| PROGRAM_APPLICATION_ID | ProgramApplicationId1 | — |
| PROGRAM_ID | ProgramId1 | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate1 | — |
| REQUEST_ID | RequestId1 | — |
| START_DATE_ACTIVE | StartDateActive | — |
| STATUS | Status | — |
| TITLE | Title | ✅ |
| TRUSTED_FLAG | TrustedFlag | — |
| URI | Uri | ✅ |
| URL | Url | ✅ |
| USAGE_TYPE | UsageType | — |

### [[requisitionattachmentpvo|RequisitionAttachmentPVO]] (HCM · BICC: 3/31)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| BASE_DOCUMENT_ID | BaseDocumentId | — |
| CREATED_BY | CreatedBy1 | — |
| CREATION_DATE | CreationDate1 | — |
| DATATYPE_CODE | DatatypeCode | — |
| DESCRIPTION | Description | — |
| DM_DOCUMENT_ID | DmDocumentId | — |
| DM_FOLDER_PATH | DmFolderPath | — |
| DM_NODE | DmNode | — |
| DM_REPOSITORY | DmRepository | — |
| DM_TYPE | DmType | — |
| DM_VERSION_NUMBER | DmVersionNumber | — |
| DOCUMENT_ATTRIBUTES | DocumentAttributes | — |
| DOCUMENT_ID | DocumentId1 | — |
| DOWNLOAD_STATUS | DownloadStatus | — |
| END_DATE_ACTIVE | EndDateActive | — |
| ENT_APP_SHORT_NAME | EntAppShortName | — |
| FILE_NAME | FileName | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate1 | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin1 | — |
| LAST_UPDATED_BY | LastUpdatedBy1 | — |
| PROGRAM_APPLICATION_ID | ProgramApplicationId1 | — |
| PROGRAM_ID | ProgramId1 | — |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate1 | — |
| REQUEST_ID | RequestId1 | — |
| START_DATE_ACTIVE | StartDateActive | — |
| STATUS | Status | — |
| TITLE | Title | ✅ |
| TRUSTED_FLAG | TrustedFlag | — |
| URI | Uri | — |
| URL | Url | — |
| USAGE_TYPE | UsageType | — |
