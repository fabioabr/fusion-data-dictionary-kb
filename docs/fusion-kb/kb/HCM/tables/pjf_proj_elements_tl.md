---
id: DOC-HCM-836
doc_type: system-doc
title: "PJF_PROJ_ELEMENTS_TL — (título a preencher)"
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
  - PJF_PROJ_ELEMENTS_TL
  - pjf_proj_elements_tl
source_format: markdown
conversion_pipeline: extract_tables-v1
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-26
updated_at: 2026-03-26
---

# PJF_PROJ_ELEMENTS_TL

## 📌 Visão Geral

(a ser preenchido na etapa 03)

---

## ⚙️ Colunas Principais

| # | Coluna | Tipo | Nulo? | Categoria | Descrição | FK | Confiança |
|---|--------|------|-------|-----------|-----------|-----|-----------|
| 1 | CREATED_BY | — | — | — | — | — | — |
| 2 | CREATION_DATE | — | — | — | — | — | — |
| 3 | DESCRIPTION | — | — | — | — | — | — |
| 4 | LANGUAGE | — | — | — | — | — | — |
| 5 | LAST_UPDATED_BY | — | — | — | — | — | — |
| 6 | LAST_UPDATE_DATE | — | — | — | — | — | — |
| 7 | LAST_UPDATE_LOGIN | — | — | — | — | — | — |
| 8 | NAME | — | — | — | — | — | — |
| 9 | OBJECT_VERSION_NUMBER | — | — | — | — | — | — |
| 10 | PROJECT_ID | — | — | — | — | — | — |
| 11 | PROJ_ELEMENT_ID | — | — | — | — | — | — |
| 12 | SOURCE_LANG | — | — | — | — | — | — |

---

## 🔗 Relacionamentos

### Tabelas-pai (FK de entrada)

### Tabelas-filha (FK de saída)

---

## 📎 Uso Típico

(a ser preenchido na etapa 03)

---

## 🔗 PVOs Relacionados

### [[contractheaderlinesall|ContractHeaderLinesAll]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| NAME | TaskStructureTranslationPEOName | — |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |

### [[contractheaderlinesallunsec|ContractHeaderLinesAllUnsec]] (OTHER)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| NAME | TaskStructureTranslationPEOName | — |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |

### [[contractheaderlinesp|ContractHeaderLinesP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| NAME | TaskStructureTranslationPEOName | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |

### [[contractheaderlinesrefp|ContractHeaderLinesRefP]] (OTHER · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| NAME | TaskStructureTranslationPEOName | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |

### [[invoicelinepvo|InvoiceLinePVO]] (AP · BICC: 1/3)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | TaskStructureTLLanguage | — |
| NAME | TaskStructureName | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTLProjElementId | — |

### [[pjftaskhierarchybicvo|PjfTaskHierarchyBICVO]] (OTHER · BICC: 20/63)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| LANGUAGE | Dep0Language | — |
| LANGUAGE | Dep10Language | — |
| LANGUAGE | Dep11Language | — |
| LANGUAGE | Dep12Language | — |
| LANGUAGE | Dep13Language | — |
| LANGUAGE | Dep14Language | — |
| LANGUAGE | Dep15Language | — |
| LANGUAGE | Dep16Language | — |
| LANGUAGE | Dep17Language | — |
| LANGUAGE | Dep18Language | — |
| LANGUAGE | Dep19Language | — |
| LANGUAGE | Dep1Language | — |
| LANGUAGE | Dep20Language | — |
| LANGUAGE | Dep2Language | — |
| LANGUAGE | Dep3Language | — |
| LANGUAGE | Dep4Language | — |
| LANGUAGE | Dep5Language | — |
| LANGUAGE | Dep6Language | — |
| LANGUAGE | Dep7Language | — |
| LANGUAGE | Dep8Language | — |
| LANGUAGE | Dep9Language | — |
| NAME | Dep0Name | ✅ |
| NAME | Dep10Name | ✅ |
| NAME | Dep11Name | ✅ |
| NAME | Dep12Name | ✅ |
| NAME | Dep13Name | ✅ |
| NAME | Dep14Name | ✅ |
| NAME | Dep15Name | ✅ |
| NAME | Dep16Name | ✅ |
| NAME | Dep17Name | ✅ |
| NAME | Dep18Name | ✅ |
| NAME | Dep19Name | ✅ |
| NAME | Dep1Name | ✅ |
| NAME | Dep20Name | — |
| NAME | Dep2Name | ✅ |
| NAME | Dep3Name | ✅ |
| NAME | Dep4Name | ✅ |
| NAME | Dep5Name | ✅ |
| NAME | Dep6Name | ✅ |
| NAME | Dep7Name | ✅ |
| NAME | Dep8Name | ✅ |
| NAME | Dep9Name | ✅ |
| PROJ_ELEMENT_ID | Dep0TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep10TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep11TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep12TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep13TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep14TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep15TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep16TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep17TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep18TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep19TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep1TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep20TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep2TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep3TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep4TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep5TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep6TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep7TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep8TLProjElementId | — |
| PROJ_ELEMENT_ID | Dep9TLProjElementId | — |

### [[taskmspvo|TaskMSPVO]] (OTHER · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaskStructureTranslationPEOCreatedBy | — |
| DESCRIPTION | TaskStructureTranslationPEODescription | ✅ |
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| LAST_UPDATED_BY | TaskStructureTranslationPEOLastUpdatedBy | — |
| NAME | TaskStructureTranslationPEOName | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |
| PROJECT_ID | TaskStructureTranslationPEOProjectId | — |
| SOURCE_LANG | TaskStructureTranslationPEOSourceLang | — |

### [[taskrefpvo|TaskRefPVO]] (OTHER · BICC: 2/8)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaskStructureTranslationPEOCreatedBy | — |
| DESCRIPTION | TaskStructureTranslationPEODescription | ✅ |
| LANGUAGE | TaskStructureTranslationPEOLanguage | — |
| LAST_UPDATED_BY | TaskStructureTranslationPEOLastUpdatedBy | — |
| NAME | TaskStructureTranslationPEOName | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | — |
| PROJECT_ID | TaskStructureTranslationPEOProjectId | — |
| SOURCE_LANG | TaskStructureTranslationPEOSourceLang | — |

### [[taskstructureextractpvo|TaskStructureExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaskStructureTransLangPEOCreatedBy | ✅ |
| CREATION_DATE | TaskStructureTransLangPEOCreationDate | ✅ |
| DESCRIPTION | TaskStructureTransLangPEODescription | ✅ |
| LANGUAGE | TaskStructureTransLangPEOLanguage | ✅ |
| LAST_UPDATE_DATE | TaskStructureTransLangPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaskStructureTransLangPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaskStructureTransLangPEOLastUpdatedBy | ✅ |
| NAME | TaskStructureTransLangPEOName | ✅ |
| OBJECT_VERSION_NUMBER | TaskStructureTransLangPEOObjectVersionNumber | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTransLangPEOProjElementId | ✅ |
| PROJECT_ID | TaskStructureTransLangPEOProjectId | ✅ |
| SOURCE_LANG | TaskStructureTransLangPEOSourceLang | ✅ |

### [[taskstructuretranslationextractpvo|TaskStructureTranslationExtractPVO]] (OTHER · BICC: 12/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | TaskStructureTranslationPEOCreatedBy | ✅ |
| CREATION_DATE | TaskStructureTranslationPEOCreationDate | ✅ |
| DESCRIPTION | TaskStructureTranslationPEODescription | ✅ |
| LANGUAGE | TaskStructureTranslationPEOLanguage | ✅ |
| LAST_UPDATE_DATE | TaskStructureTranslationPEOLastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | TaskStructureTranslationPEOLastUpdateLogin | ✅ |
| LAST_UPDATED_BY | TaskStructureTranslationPEOLastUpdatedBy | ✅ |
| NAME | TaskStructureTranslationPEOName | ✅ |
| OBJECT_VERSION_NUMBER | TaskStructureTranslationPEOObjectVersionNumber | ✅ |
| PROJ_ELEMENT_ID | TaskStructureTranslationPEOProjElementId | ✅ |
| PROJECT_ID | TaskStructureTranslationPEOProjectId | ✅ |
| SOURCE_LANG | TaskStructureTranslationPEOSourceLang | ✅ |

### [[tasktranslationpvo|TaskTranslationPVO]] (OTHER · BICC: 9/12)

| Coluna da Tabela | Atributo do PVO | BICC |
|------------------|-----------------|------|
| CREATED_BY | CreatedBy | ✅ |
| CREATION_DATE | CreationDate | ✅ |
| DESCRIPTION | Description | ✅ |
| LANGUAGE | Language | ✅ |
| LAST_UPDATE_DATE | LastUpdateDate | ✅ |
| LAST_UPDATE_LOGIN | LastUpdateLogin | — |
| LAST_UPDATED_BY | LastUpdatedBy | ✅ |
| NAME | Name | ✅ |
| OBJECT_VERSION_NUMBER | ObjectVersionNumber | — |
| PROJ_ELEMENT_ID | ProjElementId | ✅ |
| PROJECT_ID | ProjectId | — |
| SOURCE_LANG | SourceLang | ✅ |
