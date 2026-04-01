---
id: DOC-PO-PVO-NegotiationStyleBPVO
doc_type: system-doc
title: "NegotiationStyleBPVO — PVO Purchasing"
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
  - NegotiationStyleBPVO
  - negotiationstylebpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationStyleBPVO

## 📌 Visão Geral

Extrai os estilos de negociação configurados (Large, Auction, RFP), com regras de precificação, pontuação e adjudicação. Define o comportamento e a experiência do usuário em cada tipo de evento de sourcing.

**Caminho:** `FscmTopModelAM.PrcPonPublicViewAM.NegotiationStyleBPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 43 | 2 | 1 | 5 | 12% |

---

## 🔗 Tabelas Relacionadas

- [[pon_negotiation_styles_b|PON_NEGOTIATION_STYLES_B]] — 32 atributos (1 PKs, 2 BICC)
- [[pon_negotiation_styles_tl|PON_NEGOTIATION_STYLES_TL]] — 11 atributos (3 BICC)

---

## ⚙️ Atributos

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
| 28 | NegotiationStyleSystemFlag | SYSTEM_FLAG | — | — |
| 29 | NegotiationStyleTeamScoringEnabledFlag | TEAM_SCORING_ENABLED_FLAG | — | — |
| 30 | NegotiationStyleTermsInstrEnabledFlag | TERMS_INSTR_ENABLED_FLAG | — | — |
| 31 | NegotiationStyleTwostageEvalEnabledFlag | TWOSTAGE_EVAL_ENABLED_FLAG | — | — |
| 32 | StyleId | STYLE_ID | 🔑 | ✅ |

### [[pon_negotiation_styles_tl|PON_NEGOTIATION_STYLES_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | NegotiationStyleTranslatedCreatedBy | CREATED_BY | — | — |
| 2 | NegotiationStyleTranslatedCreationDate | CREATION_DATE | — | — |
| 3 | NegotiationStyleTranslatedDescription | DESCRIPTION | — | ✅ |
| 4 | NegotiationStyleTranslatedLanguage | LANGUAGE | — | — |
| 5 | NegotiationStyleTranslatedLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 6 | NegotiationStyleTranslatedLastUpdateLogin | LAST_UPDATE_LOGIN | — | — |
| 7 | NegotiationStyleTranslatedLastUpdatedBy | LAST_UPDATED_BY | — | — |
| 8 | NegotiationStyleTranslatedObjectVersionNumber | OBJECT_VERSION_NUMBER | — | — |
| 9 | NegotiationStyleTranslatedSourceLang | SOURCE_LANG | — | — |
| 10 | NegotiationStyleTranslatedStyleId | STYLE_ID | — | — |
| 11 | NegotiationStyleTranslatedStyleName | STYLE_NAME | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
