---
id: DOC-OTHER-PVO-CareerSitePVO
doc_type: system-doc
title: "CareerSitePVO — PVO Cross-Module"
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
  - CareerSitePVO
  - careersitepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CareerSitePVO

## 📌 Visão Geral

View Object para extração BICC de dados de Career Site. Acessa as tabelas: IRC_CX_SITES_B, IRC_CX_SITES_TL, IRC_CX_SITE_TEMPLATES_B (+2).

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidateExpSetupAM.CareerSitePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 58 | 5 | 1 | 16 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[irc_cx_sites_b|IRC_CX_SITES_B]] — 13 atributos (1 PKs, 9 BICC)
- [[irc_cx_sites_tl|IRC_CX_SITES_TL]] — 10 atributos (1 BICC)
- [[irc_cx_site_templates_b|IRC_CX_SITE_TEMPLATES_B]] — 11 atributos (2 BICC)
- [[irc_cx_site_templates_tl|IRC_CX_SITE_TEMPLATES_TL]] — 12 atributos (1 BICC)
- [[irc_cx_site_themes|IRC_CX_SITE_THEMES]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_cx_sites_b|IRC_CX_SITES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteBPEOActiveThemeId | ACTIVE_THEME_ID | — | — |
| 2 | SiteBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | SiteBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | SiteBPEODefaultLang | DEFAULT_LANG | — | ✅ |
| 5 | SiteBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | SiteBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SiteBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SiteBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SiteBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 10 | SiteBPEOSiteCode | SITE_CODE | — | ✅ |
| 11 | SiteBPEOSiteNumber | SITE_NUMBER | — | ✅ |
| 12 | SiteBPEOStatusCode | STATUS_CODE | — | ✅ |
| 13 | SiteId | SITE_ID | 🔑 | ✅ |

### [[irc_cx_sites_tl|IRC_CX_SITES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | SiteTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | SiteTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | SiteTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | SiteTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SiteTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SiteTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SiteTranslationPEOSiteId | SITE_ID | — | — |
| 9 | SiteTranslationPEOSiteName | SITE_NAME | — | ✅ |
| 10 | SiteTranslationPEOSourceLang | SOURCE_LANG | — | — |

### [[irc_cx_site_templates_b|IRC_CX_SITE_TEMPLATES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteTemplatePEOCreatedBy | CREATED_BY | — | — |
| 2 | SiteTemplatePEOCreationDate | CREATION_DATE | — | — |
| 3 | SiteTemplatePEOIsActiveFlag | IS_ACTIVE_FLAG | — | — |
| 4 | SiteTemplatePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | SiteTemplatePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SiteTemplatePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SiteTemplatePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SiteTemplatePEOSiteNumber | SITE_NUMBER | — | — |
| 9 | SiteTemplatePEOSplashPageNumber | SPLASH_PAGE_NUMBER | — | — |
| 10 | SiteTemplatePEOTemplateId | TEMPLATE_ID | — | ✅ |
| 11 | SiteTemplatePEOTemplateNumber | TEMPLATE_NUMBER | — | ✅ |

### [[irc_cx_site_templates_tl|IRC_CX_SITE_TEMPLATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteTemplateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 2 | SiteTemplateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 3 | SiteTemplateTranslationPEOLanguage | LANGUAGE | — | — |
| 4 | SiteTemplateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | SiteTemplateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SiteTemplateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SiteTemplateTranslationPEOMainCallForAction | MAIN_CALL_FOR_ACTION | — | — |
| 8 | SiteTemplateTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SiteTemplateTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 10 | SiteTemplateTranslationPEOTemplateId | TEMPLATE_ID | — | — |
| 11 | SiteTemplateTranslationPEOTemplateName | TEMPLATE_NAME | — | ✅ |
| 12 | SiteTemplateTranslationPEOWelcomeText | WELCOME_TEXT | — | — |

### [[irc_cx_site_themes|IRC_CX_SITE_THEMES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteThemePEOCreatedBy | CREATED_BY | — | — |
| 2 | SiteThemePEOCreationDate | CREATION_DATE | — | — |
| 3 | SiteThemePEOFooterMode | FOOTER_MODE | — | — |
| 4 | SiteThemePEOHeaderMode | HEADER_MODE | — | — |
| 5 | SiteThemePEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 6 | SiteThemePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | SiteThemePEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | SiteThemePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | SiteThemePEOTemplateId | TEMPLATE_ID | — | — |
| 10 | SiteThemePEOThemeId | THEME_ID | — | ✅ |
| 11 | SiteThemePEOThemeName | THEME_NAME | — | ✅ |
| 12 | SiteThemePEOThemeNumber | THEME_NUMBER | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
