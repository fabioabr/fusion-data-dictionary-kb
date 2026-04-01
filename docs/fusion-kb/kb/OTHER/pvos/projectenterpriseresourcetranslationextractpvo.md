---
id: DOC-OTHER-PVO-ProjectEnterpriseResourceTranslationExtractPVO
doc_type: system-doc
title: "ProjectEnterpriseResourceTranslationExtractPVO — PVO Cross-Module"
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
  - ProjectEnterpriseResourceTranslationExtractPVO
  - projectenterpriseresourcetranslationextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ProjectEnterpriseResourceTranslationExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Project Enterprise Resource Translation Extract. Acessa as tabelas: PJT_PRJ_ENTERPRISE_RESOURCE_TL.

**Caminho:** `FscmTopModelAM.PrjExtractAM.PjtBiccExtractAM.ProjectEnterpriseResourceTranslationExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 12 | 1 | 2 | 12 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]] — 12 atributos (2 PKs, 12 BICC)

---

## ⚙️ Atributos

### [[pjt_prj_enterprise_resource_tl|PJT_PRJ_ENTERPRISE_RESOURCE_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PrjEnterpriseResourceTransla1CreatedBy | CREATED_BY | — | ✅ |
| 2 | PrjEnterpriseResourceTransla1CreationDate | CREATION_DATE | — | ✅ |
| 3 | PrjEnterpriseResourceTransla1Description | DESCRIPTION | — | ✅ |
| 4 | PrjEnterpriseResourceTransla1DisplayName | DISPLAY_NAME | — | ✅ |
| 5 | PrjEnterpriseResourceTransla1EnterpriseId | ENTERPRISE_ID | — | ✅ |
| 6 | PrjEnterpriseResourceTransla1Language | LANGUAGE | 🔑 | ✅ |
| 7 | PrjEnterpriseResourceTransla1LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | PrjEnterpriseResourceTransla1LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | PrjEnterpriseResourceTransla1LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | PrjEnterpriseResourceTransla1ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PrjEnterpriseResourceTransla1ResourceId | RESOURCE_ID | 🔑 | ✅ |
| 12 | PrjEnterpriseResourceTransla1SourceLang | SOURCE_LANG | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
