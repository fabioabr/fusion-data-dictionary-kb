---
id: DOC-PO-PVO-NegotiationStyleDocumentTypePVO
doc_type: system-doc
title: "NegotiationStyleDocumentTypePVO — PVO Purchasing"
system: Oracle Fusion Cloud ERP
module: Purchasing
domain: Técnico
owner: fabio.patria
team: dados
status: draft
confidentiality: internal
tags:
  - oracle-fusion
  - po
  - data-dictionary
  - pvo
  - bicc
aliases:
  - NegotiationStyleDocumentTypePVO
  - negotiationstyledocumenttypepvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationStyleDocumentTypePVO

## 📌 Visão Geral

Extrai os tipos de documentos associados a estilos de negociação, determinando quais documentos de compra (PO, BPA, CPA) podem ser gerados a partir de cada tipo de evento de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationStyleDocumentTypePVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 61 | 3 | 2 | 10 | 16% |

---

## 🔗 Tabelas Relacionadas

- [[pon_auc_doctypes_b|PON_AUC_DOCTYPES_B]] — 11 atributos (2 BICC)
- [[pon_doctype_styles_b|PON_DOCTYPE_STYLES_B]] — 18 atributos (2 PKs, 7 BICC)
- [[pon_negotiation_styles_b|PON_NEGOTIATION_STYLES_B]] — 32 atributos (1 BICC)

---

## ⚙️ Atributos

### [[pon_auc_doctypes_b|PON_AUC_DOCTYPES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationDocumentTypeCreatedBy | CREATED_BY | — | — |
| 2 | NegotiationDocumentTypeCreationDate | CREATION_DATE | — | — |
| 3 | NegotiationDocumentTypeDoctypeGroupName | DOCTYPE_GROUP_NAME | — | ✅ |
| 4 | NegotiationDocumentTypeDoctypeId | DOCTYPE_ID | — | — |
| 5 | NegotiationDocumentTypeDocumentSubtype | DOCUMENT_SUBTYPE | — | — |
| 6 | NegotiationDocumentTypeDocumentTypeCode | DOCUMENT_TYPE_CODE | — | — |
| 7 | NegotiationDocumentTypeInternalName | INTERNAL_NAME | — | — |
| 8 | NegotiationDocumentTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 9 | NegotiationDocumentTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 10 | NegotiationDocumentTypeLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 11 | NegotiationDocumentTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |

### [[pon_doctype_styles_b|PON_DOCTYPE_STYLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | DoctypeId | DOCTYPE_ID | 🔑 | ✅ |
| 2 | NegotiationStyleDocTranslationCreatedBy | CREATED_BY | — | — |
| 3 | NegotiationStyleDocTranslationCreationDate | CREATION_DATE | — | — |
| 4 | NegotiationStyleDocTranslationDoctypeId | DOCTYPE_ID | — | — |
| 5 | NegotiationStyleDocTranslationEnabledFlag | ENABLED_FLAG | — | — |
| 6 | NegotiationStyleDocTranslationLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | NegotiationStyleDocTranslationLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 8 | NegotiationStyleDocTranslationLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 9 | NegotiationStyleDocTranslationObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 10 | NegotiationStyleDocTranslationStyleId | STYLE_ID | — | — |
| 11 | NegotiationStyleDocumentTypeCreatedBy | CREATED_BY | — | ✅ |
| 12 | NegotiationStyleDocumentTypeCreationDate | CREATION_DATE | — | ✅ |
| 13 | NegotiationStyleDocumentTypeEnabledFlag | ENABLED_FLAG | — | — |
| 14 | NegotiationStyleDocumentTypeLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 15 | NegotiationStyleDocumentTypeLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 16 | NegotiationStyleDocumentTypeLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 17 | NegotiationStyleDocumentTypeObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 18 | StyleId | STYLE_ID | 🔑 | ✅ |

### [[pon_negotiation_styles_b|PON_NEGOTIATION_STYLES_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationStyleAbstractEnabledFlag | ABSTRACT_ENABLED_FLAG | — | — |
| 2 | NegotiationStyleAutoExtendEnabledFlag | AUTO_EXTEND_ENABLED_FLAG | — | — |
| 3 | NegotiationStyleContermsEnabledFlag | CONTERMS_ENABLED_FLAG | — | — |
| 4 | NegotiationStyleCoverPageEnabledFlag | COVER_PAGE_ENABLED_FLAG | — | — |
| 5 | NegotiationStyleCreatedBy | CREATED_BY | — | — |
| 6 | NegotiationStyleCreationDate | CREATION_DATE | — | — |
| 7 | NegotiationStyleGeneralIntroEnabledFlag | GENERAL_INTRO_ENABLED_FLAG | — | — |
| 8 | NegotiationStyleGroupEnabledFlag | GROUP_ENABLED_FLAG | — | — |
| 9 | NegotiationStyleHdrAttributeEnabledFlag | HDR_ATTRIBUTE_ENABLED_FLAG | — | — |
| 10 | NegotiationStyleLargeNegEnabledFlag | LARGE_NEG_ENABLED_FLAG | — | — |
| 11 | NegotiationStyleLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 12 | NegotiationStyleLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 13 | NegotiationStyleLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 14 | NegotiationStyleLineAttributeEnabledFlag | LINE_ATTRIBUTE_ENABLED_FLAG | — | — |
| 15 | NegotiationStyleLineMasEnabledFlag | LINE_MAS_ENABLED_FLAG | — | — |
| 16 | NegotiationStyleLinesInstrEnabledFlag | LINES_INSTR_ENABLED_FLAG | — | — |
| 17 | NegotiationStyleLotEnabledFlag | LOT_ENABLED_FLAG | — | — |
| 18 | NegotiationStyleNegTeamEnabledFlag | NEG_TEAM_ENABLED_FLAG | — | — |
| 19 | NegotiationStyleObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 20 | NegotiationStylePowerBiddingEnabledFlag | POWER_BIDDING_ENABLED_FLAG | — | — |
| 21 | NegotiationStylePriceElementEnabledFlag | PRICE_ELEMENT_ENABLED_FLAG | — | — |
| 22 | NegotiationStyleProxyBiddingEnabledFlag | PROXY_BIDDING_ENABLED_FLAG | — | — |
| 23 | NegotiationStyleQtyPriceTiersEnabledFlag | QTY_PRICE_TIERS_ENABLED_FLAG | — | — |
| 24 | NegotiationStyleReqmntsInstrEnabledFlag | REQMNTS_INSTR_ENABLED_FLAG | — | — |
| 25 | NegotiationStyleRfiLineEnabledFlag | RFI_LINE_ENABLED_FLAG | — | — |
| 26 | NegotiationStyleStagCloseEnabledFlag | STAG_CLOSE_ENABLED_FLAG | — | — |
| 27 | NegotiationStyleStatus | STATUS | — | — |
| 28 | NegotiationStyleStyleId | STYLE_ID | — | — |
| 29 | NegotiationStyleSystemFlag | SYSTEM_FLAG | — | — |
| 30 | NegotiationStyleTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 31 | NegotiationStyleTermsInstrEnabledFlag | TERMS_INSTR_ENABLED_FLAG | — | — |
| 32 | NegotiationStyleTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
