---
id: DOC-PO-PVO-NegotiationTeamRequirementScoresExtractPVO
doc_type: system-doc
title: "NegotiationTeamRequirementScoresExtractPVO — PVO Purchasing"
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
  - NegotiationTeamRequirementScoresExtractPVO
  - negotiationteamrequirementscoresextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationTeamRequirementScoresExtractPVO

## 📌 Visão Geral

Extrai as pontuações por requisito atribuídas pela equipe de negociação a cada proposta. Suporta análise de desempenho dos fornecedores em critérios técnicos e comerciais individuais.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationTeamRequirementScoresExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 13 | 1 | 3 | 13 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_team_requirement_scores|PON_TEAM_REQUIREMENT_SCORES]] — 13 atributos (3 PKs, 13 BICC)

---

## ⚙️ Atributos

### [[pon_team_requirement_scores|PON_TEAM_REQUIREMENT_SCORES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | BidNumber | BID_NUMBER | 🔑 | ✅ |
| 3 | CreatedBy | CREATED_BY | — | ✅ |
| 4 | CreationDate | CREATION_DATE | — | ✅ |
| 5 | InternalNote | INTERNAL_NOTE | — | ✅ |
| 6 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 10 | PersonId | PERSON_ID | 🔑 | ✅ |
| 11 | RequirementId | REQUIREMENT_ID | 🔑 | ✅ |
| 12 | Score | SCORE | — | ✅ |
| 13 | SectionId | SECTION_ID | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
