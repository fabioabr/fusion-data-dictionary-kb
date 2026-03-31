---
id: DOC-OTHER-PVO-WoDocumentReferenceExtractPVO
doc_type: system-doc
title: "WoDocumentReferenceExtractPVO — PVO Cross-Module"
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
  - WoDocumentReferenceExtractPVO
  - wodocumentreferenceextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# WoDocumentReferenceExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Wo Document Reference Extract. Acessa as tabelas: MNT_WO_DOC_REFERENCES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.MntBiccExtractAM.WoDocumentReferenceExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 26 | 1 | 1 | 26 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[mnt_wo_doc_references|MNT_WO_DOC_REFERENCES]] — 26 atributos (1 PKs, 26 BICC)

---

## ⚙️ Atributos

### [[mnt_wo_doc_references|MNT_WO_DOC_REFERENCES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ActiveEndDate | ACTIVE_END_DATE | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DocHeaderId | DOC_HEADER_ID | — | ✅ |
| 5 | DocLineId | DOC_LINE_ID | — | ✅ |
| 6 | DocLineNumber | DOC_LINE_NUMBER | — | ✅ |
| 7 | DocNumber | DOC_NUMBER | — | ✅ |
| 8 | DocRefId | DOC_REF_ID | 🔑 | ✅ |
| 9 | DocSubLineId | DOC_SUB_LINE_ID | — | ✅ |
| 10 | DocSubLineLvl1Id | DOC_SUB_LINE_LVL1_ID | — | ✅ |
| 11 | DocSubLineLvl1Number | DOC_SUB_LINE_LVL1_NUMBER | — | ✅ |
| 12 | DocSubLineLvl2Id | DOC_SUB_LINE_LVL2_ID | — | ✅ |
| 13 | DocSubLineLvl2Number | DOC_SUB_LINE_LVL2_NUMBER | — | ✅ |
| 14 | DocSubLineNumber | DOC_SUB_LINE_NUMBER | — | ✅ |
| 15 | DocTypeCode | DOC_TYPE_CODE | — | ✅ |
| 16 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 17 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 18 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 19 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 20 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 21 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 22 | RequestId | REQUEST_ID | — | ✅ |
| 23 | SrcRefId | SRC_REF_ID | — | ✅ |
| 24 | SrcSystemId | SRC_SYSTEM_ID | — | ✅ |
| 25 | SrcSystemTypeCode | SRC_SYSTEM_TYPE_CODE | — | ✅ |
| 26 | WorkOrderId | WORK_ORDER_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
