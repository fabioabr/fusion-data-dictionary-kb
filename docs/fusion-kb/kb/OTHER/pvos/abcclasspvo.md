---
id: DOC-OTHER-PVO-AbcClassPVO
doc_type: system-doc
title: "AbcClassPVO — PVO Cross-Module"
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
  - AbcClassPVO
  - abcclasspvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# AbcClassPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Abc Class. Acessa as tabelas: INV_ABC_CLASSES.

**Caminho:** `FscmTopModelAM.ScmExtractAM.InvBiccExtractAM.AbcClassPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 15 | 1 | 1 | 15 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[inv_abc_classes|INV_ABC_CLASSES]] — 15 atributos (1 PKs, 15 BICC)

---

## ⚙️ Atributos

### [[inv_abc_classes|INV_ABC_CLASSES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AbcClassId | ABC_CLASS_ID | 🔑 | ✅ |
| 2 | AbcClassName | ABC_CLASS_NAME | — | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | Description | DESCRIPTION | — | ✅ |
| 6 | DisableDate | DISABLE_DATE | — | ✅ |
| 7 | EnableDate | ENABLE_DATE | — | ✅ |
| 8 | JobDefinitionName | JOB_DEFINITION_NAME | — | ✅ |
| 9 | JobDefinitionPackage | JOB_DEFINITION_PACKAGE | — | ✅ |
| 10 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 11 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 12 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 13 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 14 | OrganizationId | ORGANIZATION_ID | — | ✅ |
| 15 | RequestId | REQUEST_ID | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
