---
id: DOC-OTHER-PVO-ResourceTranslationExtractPVO
doc_type: system-doc
title: "ResourceTranslationExtractPVO — PVO Cross-Module"
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
  - ResourceTranslationExtractPVO
  - resourcetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ResourceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Resource Translation Extract. Acessa as tabelas: WIS_RESOURCES_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.WisBiccExtractAM.ResourceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[wis_resources_tl|WIS_RESOURCES_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[wis_resources_tl|WIS_RESOURCES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | CreatedBy | CREATED_BY | — | ✅ |
| 2 | CreationDate | CREATION_DATE | — | ✅ |
| 3 | Language | LANGUAGE | 🔑 | ✅ |
| 4 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 5 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 6 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 7 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 8 | ResourceDescription | RESOURCE_DESCRIPTION | — | ✅ |
| 9 | ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 10 | ResourceName | RESOURCE_NAME | — | ✅ |
| 11 | SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
