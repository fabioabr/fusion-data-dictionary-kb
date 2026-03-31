---
id: DOC-OTHER-PVO-FosAgreementDefinitionTranslationExtractPVO
doc_type: system-doc
title: "FosAgreementDefinitionTranslationExtractPVO — PVO Cross-Module"
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
  - FosAgreementDefinitionTranslationExtractPVO
  - fosagreementdefinitiontranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# FosAgreementDefinitionTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Fos Agreement Definition Translation Extract. Acessa as tabelas: FOS_AGREEMENT_DEFINITION_TL.

**Caminho:** `FscmTopModelAM.ScmExtractAM.FosBiccExtractAM.FosAgreementDefinitionTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 14 | 1 | 4 | 14 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[fos_agreement_definition_tl|FOS_AGREEMENT_DEFINITION_TL]] — 14 atributos (4 PKs, 14 BICC)

---

## ⚙️ Atributos

### [[fos_agreement_definition_tl|FOS_AGREEMENT_DEFINITION_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AgreementDefinitionTLPEOAgreementId | AGREEMENT_ID | 🔑 | ✅ |
| 2 | AgreementDefinitionTLPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | AgreementDefinitionTLPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | AgreementDefinitionTLPEODescription | DESCRIPTION | — | ✅ |
| 5 | AgreementDefinitionTLPEOEffectiveEndDate | EFFECTIVE_END_DATE | 🔑 | ✅ |
| 6 | AgreementDefinitionTLPEOEffectiveStartDate | EFFECTIVE_START_DATE | 🔑 | ✅ |
| 7 | AgreementDefinitionTLPEOEnterpriseId | ENTERPRISE_ID | — | ✅ |
| 8 | AgreementDefinitionTLPEOLanguage | LANGUAGE | 🔑 | ✅ |
| 9 | AgreementDefinitionTLPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 10 | AgreementDefinitionTLPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 11 | AgreementDefinitionTLPEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 12 | AgreementDefinitionTLPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 13 | AgreementDefinitionTLPEOSeedDataSource | SEED_DATA_SOURCE | — | ✅ |
| 14 | AgreementDefinitionTLPEOSourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
