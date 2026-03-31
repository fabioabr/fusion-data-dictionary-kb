---
id: DOC-OTHER-PVO-ObligTemplatePVO
doc_type: system-doc
title: "ObligTemplatePVO — PVO Cross-Module"
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
  - ObligTemplatePVO
  - obligtemplatepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# ObligTemplatePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Oblig Template. Acessa as tabelas: VRM_PERF_OBLIG_TEMPLATES_B, VRM_PERF_OBLIG_TEMPLATES_TL.

**Caminho:** `FscmTopModelAM.FinVrmRRSharedPublicModelAM.ObligTemplatePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 55 | 2 | 2 | 11 | 20% |

---

## 🔗 Tabelas Relacionadas

- [[vrm_perf_oblig_templates_b|VRM_PERF_OBLIG_TEMPLATES_B]] — 44 atributos (6 BICC)
- [[vrm_perf_oblig_templates_tl|VRM_PERF_OBLIG_TEMPLATES_TL]] — 11 atributos (2 PKs, 5 BICC)

---

## ⚙️ Atributos

### [[vrm_perf_oblig_templates_b|VRM_PERF_OBLIG_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObligTemplateBaseAttribute1 | ATTRIBUTE1 | — | — |
| 2 | ObligTemplateBaseAttribute10 | ATTRIBUTE10 | — | — |
| 3 | ObligTemplateBaseAttribute11 | ATTRIBUTE11 | — | — |
| 4 | ObligTemplateBaseAttribute12 | ATTRIBUTE12 | — | — |
| 5 | ObligTemplateBaseAttribute13 | ATTRIBUTE13 | — | — |
| 6 | ObligTemplateBaseAttribute14 | ATTRIBUTE14 | — | — |
| 7 | ObligTemplateBaseAttribute15 | ATTRIBUTE15 | — | — |
| 8 | ObligTemplateBaseAttribute16 | ATTRIBUTE16 | — | — |
| 9 | ObligTemplateBaseAttribute17 | ATTRIBUTE17 | — | — |
| 10 | ObligTemplateBaseAttribute18 | ATTRIBUTE18 | — | — |
| 11 | ObligTemplateBaseAttribute19 | ATTRIBUTE19 | — | — |
| 12 | ObligTemplateBaseAttribute2 | ATTRIBUTE2 | — | — |
| 13 | ObligTemplateBaseAttribute20 | ATTRIBUTE20 | — | — |
| 14 | ObligTemplateBaseAttribute3 | ATTRIBUTE3 | — | — |
| 15 | ObligTemplateBaseAttribute4 | ATTRIBUTE4 | — | — |
| 16 | ObligTemplateBaseAttribute5 | ATTRIBUTE5 | — | — |
| 17 | ObligTemplateBaseAttribute6 | ATTRIBUTE6 | — | — |
| 18 | ObligTemplateBaseAttribute7 | ATTRIBUTE7 | — | — |
| 19 | ObligTemplateBaseAttribute8 | ATTRIBUTE8 | — | — |
| 20 | ObligTemplateBaseAttribute9 | ATTRIBUTE9 | — | — |
| 21 | ObligTemplateBaseAttributeCategory | ATTRIBUTE_CATEGORY | — | — |
| 22 | ObligTemplateBaseAttributeDate1 | ATTRIBUTE_DATE1 | — | — |
| 23 | ObligTemplateBaseAttributeDate2 | ATTRIBUTE_DATE2 | — | — |
| 24 | ObligTemplateBaseAttributeDate3 | ATTRIBUTE_DATE3 | — | — |
| 25 | ObligTemplateBaseAttributeDate4 | ATTRIBUTE_DATE4 | — | — |
| 26 | ObligTemplateBaseAttributeDate5 | ATTRIBUTE_DATE5 | — | — |
| 27 | ObligTemplateBaseAttributeNumber1 | ATTRIBUTE_NUMBER1 | — | — |
| 28 | ObligTemplateBaseAttributeNumber2 | ATTRIBUTE_NUMBER2 | — | — |
| 29 | ObligTemplateBaseAttributeNumber3 | ATTRIBUTE_NUMBER3 | — | — |
| 30 | ObligTemplateBaseAttributeNumber4 | ATTRIBUTE_NUMBER4 | — | — |
| 31 | ObligTemplateBaseAttributeNumber5 | ATTRIBUTE_NUMBER5 | — | — |
| 32 | ObligTemplateBaseCreatedBy1 | CREATED_BY | — | — |
| 33 | ObligTemplateBaseCreatedFrom | CREATED_FROM | — | — |
| 34 | ObligTemplateBaseCreationDate1 | CREATION_DATE | — | — |
| 35 | ObligTemplateBaseDerivePdcFlag | DERIVE_PDC_FLAG | — | ✅ |
| 36 | ObligTemplateBaseEnabledFlag | ENABLED_FLAG | — | ✅ |
| 37 | ObligTemplateBaseInUseFlag | IN_USE_FLAG | — | ✅ |
| 38 | ObligTemplateBaseLastUpdateDate1 | LAST_UPDATE_DATE | — | ✅ |
| 39 | ObligTemplateBaseLastUpdateLogin1 | LAST_UPDATE_LOGIN | — | — |
| 40 | ObligTemplateBaseLastUpdatedBy1 | LAST_UPDATED_BY | — | — |
| 41 | ObligTemplateBaseObjectVersionNumber1 | OBJECT_VERSION_NUMBER | — | — |
| 42 | ObligTemplateBasePerfObligationTemplateId1 | PERF_OBLIGATION_TEMPLATE_ID | — | — |
| 43 | ObligTemplateBasePriority | PRIORITY | — | ✅ |
| 44 | ObligTemplateBaseSatisfactionMethod | SATISFACTION_METHOD | — | ✅ |

### [[vrm_perf_oblig_templates_tl|VRM_PERF_OBLIG_TEMPLATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | Language | LANGUAGE | 🔑 | ✅ |
| 2 | ObligTemplateTranslationCreatedBy | CREATED_BY | — | — |
| 3 | ObligTemplateTranslationCreationDate | CREATION_DATE | — | — |
| 4 | ObligTemplateTranslationDescription | DESCRIPTION | — | ✅ |
| 5 | ObligTemplateTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | ObligTemplateTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | ObligTemplateTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | ObligTemplateTranslationName | NAME | — | ✅ |
| 9 | ObligTemplateTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | ObligTemplateTranslationSourceLang | SOURCE_LANG | — | — |
| 11 | PerfObligationTemplateId | PERF_OBLIGATION_TEMPLATE_ID | 🔑 | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
