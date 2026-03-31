---
id: DOC-HCM-PVO-CareerSitePagePVO
doc_type: system-doc
title: "CareerSitePagePVO — PVO Human Capital Management"
system: Oracle Fusion Cloud ERP
module: Human Capital Management
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - hcm
  - data-dictionary
  - pvo
  - bicc
aliases:
  - CareerSitePagePVO
  - careersitepagepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# CareerSitePagePVO

## 📌 Visão Geral

Extrai paginas de career sites com templates e configuracoes de exibicao. Suporta personalizacao da experiencia do candidato em portais de vagas.

**Caminho:** `HcmTopModelAnalyticsGlobalAM.HcmRecCandidateExpSetupAM.CareerSitePagePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 85 | 7 | 1 | 24 | 28% |

---

## 🔗 Tabelas Relacionadas

- [[irc_cx_pages_b|IRC_CX_PAGES_B]] — 14 atributos (7 BICC)
- [[irc_cx_pages_tl|IRC_CX_PAGES_TL]] — 13 atributos (1 BICC)
- [[irc_cx_sites_b|IRC_CX_SITES_B]] — 13 atributos (1 PKs, 9 BICC)
- [[irc_cx_sites_tl|IRC_CX_SITES_TL]] — 10 atributos (1 BICC)
- [[irc_cx_site_templates_b|IRC_CX_SITE_TEMPLATES_B]] — 11 atributos (2 BICC)
- [[irc_cx_site_templates_tl|IRC_CX_SITE_TEMPLATES_TL]] — 12 atributos (1 BICC)
- [[irc_cx_site_themes|IRC_CX_SITE_THEMES]] — 12 atributos (3 BICC)

---

## ⚙️ Atributos

### [[irc_cx_pages_b|IRC_CX_PAGES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PageId | PAGE_ID | — | ✅ |
| 2 | SitePageBPEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | SitePageBPEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | SitePageBPEOElementId | ELEMENT_ID | — | — |
| 5 | SitePageBPEOElementType | ELEMENT_TYPE | — | — |
| 6 | SitePageBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SitePageBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SitePageBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SitePageBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SitePageBPEOPageCode | PAGE_CODE | — | ✅ |
| 11 | SitePageBPEOPublishedDate | PUBLISHED_DATE | — | ✅ |
| 12 | SitePageBPEOSiteCode | SITE_CODE | — | — |
| 13 | SitePageBPEOSiteNumber | SITE_NUMBER | — | — |
| 14 | SitePageBPEOStatusCode | STATUS_CODE | — | ✅ |

### [[irc_cx_pages_tl|IRC_CX_PAGES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ObjectVersionNumber6 | OBJECT_VERSION_NUMBER | — | — |
| 2 | PageId1 | PAGE_ID | — | — |
| 3 | SitePageTranslationPEOCreatedBy | CREATED_BY | — | — |
| 4 | SitePageTranslationPEOCreationDate | CREATION_DATE | — | — |
| 5 | SitePageTranslationPEOLanguage | LANGUAGE | — | — |
| 6 | SitePageTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 7 | SitePageTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SitePageTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SitePageTranslationPEOOgDescription | OG_DESCRIPTION | — | — |
| 10 | SitePageTranslationPEOOgImageSrc | OG_IMAGE_SRC | — | — |
| 11 | SitePageTranslationPEOSeoDescription | SEO_DESCRIPTION | — | — |
| 12 | SitePageTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 13 | SitePageTranslationPEOTitle | TITLE | — | ✅ |

### [[irc_cx_sites_b|IRC_CX_SITES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteId | SITE_ID | 🔑 | ✅ |
| 2 | SitesBPEOActiveThemeId | ACTIVE_THEME_ID | — | — |
| 3 | SitesBPEOCreatedBy | CREATED_BY | — | ✅ |
| 4 | SitesBPEOCreationDate | CREATION_DATE | — | ✅ |
| 5 | SitesBPEODefaultLang | DEFAULT_LANG | — | ✅ |
| 6 | SitesBPEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SitesBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | SitesBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | SitesBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | SitesBPEOSequenceNumber | SEQUENCE_NUMBER | — | ✅ |
| 11 | SitesBPEOSiteCode | SITE_CODE | — | ✅ |
| 12 | SitesBPEOSiteNumber | SITE_NUMBER | — | ✅ |
| 13 | SitesBPEOStatusCode | STATUS_CODE | — | ✅ |

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
| 1 | SiteTemplateBPEOCreatedBy | CREATED_BY | — | — |
| 2 | SiteTemplateBPEOCreationDate | CREATION_DATE | — | — |
| 3 | SiteTemplateBPEOIsActiveFlag | IS_ACTIVE_FLAG | — | — |
| 4 | SiteTemplateBPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 5 | SiteTemplateBPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 6 | SiteTemplateBPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 7 | SiteTemplateBPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 8 | SiteTemplateBPEOSiteNumber | SITE_NUMBER | — | — |
| 9 | SiteTemplateBPEOSplashPageNumber | SPLASH_PAGE_NUMBER | — | — |
| 10 | SiteTemplateBPEOTemplateId | TEMPLATE_ID | — | ✅ |
| 11 | SiteTemplateBPEOTemplateNumber | TEMPLATE_NUMBER | — | ✅ |

### [[irc_cx_site_templates_tl|IRC_CX_SITE_TEMPLATES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SiteTemplateThemeTranslationPEOSourceLang | SOURCE_LANG | — | — |
| 2 | SiteTemplateThemeTranslationPEOTemplateId | TEMPLATE_ID | — | — |
| 3 | SiteTemplateThemeTranslationPEOTemplateName | TEMPLATE_NAME | — | ✅ |
| 4 | SiteTemplateThemeTranslationPEOWelcomeText | WELCOME_TEXT | — | — |
| 5 | SiteTemplateTranslationPEOCreatedBy | CREATED_BY | — | — |
| 6 | SiteTemplateTranslationPEOCreationDate | CREATION_DATE | — | — |
| 7 | SiteTemplateTranslationPEOLanguage | LANGUAGE | — | — |
| 8 | SiteTemplateTranslationPEOLastUpdateDate | LAST_UPDATE_DATE | — | — |
| 9 | SiteTemplateTranslationPEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | SiteTemplateTranslationPEOLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | SiteTemplateTranslationPEOMainCallForAction | MAIN_CALL_FOR_ACTION | — | — |
| 12 | SiteTemplateTranslationPEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

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

- [[hcm-module-data-dictionary]] — Dossiê do módulo HCM
