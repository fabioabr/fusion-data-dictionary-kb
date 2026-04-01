---
id: DOC-HCM-127
doc_type: system-doc
title: "FND_DOCUMENTS_TL — (título a preencher)"
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
  - FND_DOCUMENTS_TL
  - fnd_documents_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# FND_DOCUMENTS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CEC_FILE_ID | — | — | — | — | — | — |
| 2 | CEC_PARENT_ID | — | — | — | — | — | — |
| 3 | CREATED_BY | — | — | — | — | — | — |
| 4 | CREATION_DATE | — | — | — | — | — | — |
| 5 | DESCRIPTION | — | — | — | — | — | — |
| 6 | DM_DOCUMENT_ID | — | — | — | — | — | — |
| 7 | DM_FOLDER_PATH | — | — | — | — | — | — |
| 8 | DM_NODE | — | — | — | — | — | — |
| 9 | DM_REPOSITORY | — | — | — | — | — | — |
| 10 | DM_TYPE | — | — | — | — | — | — |
| 11 | DM_VERSION_NUMBER | — | — | — | — | — | — |
| 12 | DOCUMENT_ID | — | — | — | — | — | — |
| 13 | DOWNLOAD_STATUS | — | — | — | — | — | — |
| 14 | ENTERPRISE_ID | — | — | — | — | — | — |
| 15 | ENT_APP_SHORT_NAME | — | — | — | — | — | — |
| 16 | FILE_NAME | — | — | — | — | — | — |
| 17 | LANGUAGE | — | — | — | — | — | — |
| 18 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 19 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 20 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 21 | OBJECT_BUCKET | — | — | — | — | — | — |
| 22 | OBJECT_CONTENT_TYPE | — | — | — | — | — | — |
| 23 | OBJECT_NAME | — | — | — | — | — | — |
| 24 | OBJECT_SIZE | — | — | — | — | — | — |
| 25 | PROGRAM_APPLICATION_ID | — | — | — | — | — | — |
| 26 | PROGRAM_ID | — | — | — | — | — | — |
| 27 | PROGRAM_UPDATE_DATE | — | — | — | — | — | — |
| 28 | REQUEST_ID | — | — | — | — | — | — |
| 29 | SOURCE_CONTENT_TYPE | — | — | — | — | — | — |
| 30 | SOURCE_LANG | — | — | — | — | — | — |
| 31 | STATUS | — | — | — | — | — | — |
| 32 | TITLE | — | — | — | — | — | — |
| 33 | TRACKER_ID | — | — | — | — | — | — |
| 34 | TRUSTED_FLAG | — | — | — | — | — | — |
| 35 | URI | — | — | — | — | — | — |
| 36 | URL | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[attacheddocumentspvo|AttachedDocumentsPVO]] (OTHER · BICC: 5/5)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| DESCRIPTION | Description1 | ✅ |
| DOCUMENT_ID | DocumentId2 | ✅ |
| FILE_NAME | FileName | ✅ |
| LANGUAGE | Language1 | ✅ |
| URL | Url | ✅ |

### [[fnddocumenttranslationextractpvo|FndDocumentTranslationExtractPVO]] (HCM · BICC: 36/36)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CEC_FILE_ID | CecFileId | ✅ |
| CEC_PARENT_ID | CecParentId | ✅ |
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| DM_DOCUMENT_ID | DmDocumentId | ✅ |
| DM_FOLDER_PATH | DmFolderPath | ✅ |
| DM_NODE | DmNode | ✅ |
| DM_REPOSITORY | DmRepository | ✅ |
| DM_TYPE | DmType | ✅ |
| DM_VERSION_NUMBER | DmVersionNumber | ✅ |
| DOCUMENT_ID | DocumentId | ✅ |
| DOWNLOAD_STATUS | DownloadStatus | ✅ |
| ENT_APP_SHORT_NAME | EntAppShortName | ✅ |
| ENTERPRISE_ID | EnterpriseId | ✅ |
| FILE_NAME | FileName | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | ✅ |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| OBJECT_BUCKET | ObjectBucket | ✅ |
| OBJECT_CONTENT_TYPE | ObjectContentType | ✅ |
| OBJECT_NAME | ObjectName | ✅ |
| OBJECT_SIZE | ObjectSize | ✅ |
| PROGRAM_APPLICATION_ID | ProgramApplicationId | ✅ |
| PROGRAM_ID | ProgramId | ✅ |
| PROGRAM_UPDATE_DATE | ProgramUpdateDate | ✅ |
| REQUEST_ID | RequestId | ✅ |
| SOURCE_CONTENT_TYPE | SourceContentType | ✅ |
| SOURCE_LANG | SourceLang | ✅ |
| STATUS | Status | ✅ |
| TITLE | Title | ✅ |
| TRACKER_ID | TrackerId | ✅ |
| TRUSTED_FLAG | TrustedFlag | ✅ |
| URI | Uri | ✅ |
| URL | Url | ✅ |
