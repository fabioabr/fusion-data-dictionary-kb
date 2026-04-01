---
id: DOC-PO-PVO-NegotiationTeamBidScoresExtractPVO
doc_type: system-doc
title: "NegotiationTeamBidScoresExtractPVO — PVO Purchasing"
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
  - NegotiationTeamBidScoresExtractPVO
  - negotiationteambidscoresextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationTeamBidScoresExtractPVO

## 📌 Visão Geral

Extrai as pontuações atribuídas pela equipe avaliadora aos lances/propostas em negociações. Permite análise de critérios de seleção, calibração de avaliadores e transparência na adjudicação.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationTeamBidScoresExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 2 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_team_bid_scores|PON_TEAM_BID_SCORES]] — 13 atributos (2 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pon_team_bid_scores|PON_TEAM_BID_SCORES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | InternalNote | INTERNAL_NOTE | — | ✅ |
| 6 | LastScoringDate | LAST_SCORING_DATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 11 | PersonId | PERSON_ID | 🔑 | ✅ |
| 12 | ScoringStatus | SCORING_STATUS | — | ✅ |
| 13 | TechnicalScoringStatus | TECHNICAL_SCORING_STATUS | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
