---
id: DOC-OTHER-PVO-InstitutionTranslationPVO
doc_type: system-doc
title: "InstitutionTranslationPVO — PVO Cross-Module"
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
  - InstitutionTranslationPVO
  - institutiontranslationpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# InstitutionTranslationPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Institution Translation. Acessa as tabelas: GMS_INSTITUTIONS_TL.

**Caminho:** `FscmTopModelAM.GmsSetupAM.InstitutionTranslationPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 11 | 1 | 2 | 11 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_institutions_tl|GMS_INSTITUTIONS_TL]] — 11 atributos (2 PKs, 11 BICC)

---

## ⚙️ Atributos

### [[gms_institutions_tl|GMS_INSTITUTIONS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | InstitutionId | INSTITUTION_ID | 🔑 | ✅ |
| 2 | InstitutionTranslationPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | InstitutionTranslationPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | InstitutionTranslationPEODescription | DESCRIPTION | — | ✅ |
| 5 | InstitutionTranslationPEOInstitutionName | INSTITUTION_NAME | — | ✅ |
| 6 | InstitutionTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | InstitutionTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | InstitutionTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | InstitutionTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | InstitutionTranslationPEOSourceLang | SOURCE_LANG | — | ✅ |
| 11 | Language | LANGUAGE | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
