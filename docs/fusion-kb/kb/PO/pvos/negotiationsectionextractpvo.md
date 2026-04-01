---
id: DOC-PO-PVO-NegotiationSectionExtractPVO
doc_type: system-doc
title: "NegotiationSectionExtractPVO — PVO Purchasing"
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
  - NegotiationSectionExtractPVO
  - negotiationsectionextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# NegotiationSectionExtractPVO

## 📌 Visão Geral

Extrai as seções de negociações de sourcing para carga BICC, organizando requisitos em grupos lógicos (lotes). Suporta análise de estratégia de loteamento e estrutura do evento.

**Caminho:** `FscmTopModelAM.PrcExtractAM.PonBiccExtractAM.NegotiationSectionExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 17 | 1 | 1 | 17 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]] — 17 atributos (1 PKs, 17 BICC)

---

## ⚙️ Atributos

### [[pon_requirement_sections|PON_REQUIREMENT_SECTIONS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | AuctionHeaderId | AUCTION_HEADER_ID | — | ✅ |
| 2 | CreatedBy | CREATED_BY | — | ✅ |
| 3 | CreationDate | CREATION_DATE | — | ✅ |
| 4 | DispSeqNumber | DISP_SEQ_NUMBER | — | ✅ |
| 5 | IsInternal | IS_INTERNAL | — | ✅ |
| 6 | LastAmendmentUpdate | LAST_AMENDMENT_UPDATE | — | ✅ |
| 7 | LastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 8 | LastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 9 | LastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 10 | ModifiedFlag | MODIFIED_FLAG | — | ✅ |
| 11 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | PreviousSectionId | PREVIOUS_SECTION_ID | — | ✅ |
| 13 | SectionDisplayNumber | SECTION_DISPLAY_NUMBER | — | ✅ |
| 14 | SectionId | SECTION_ID | 🔑 | ✅ |
| 15 | SectionLevel | SECTION_LEVEL | — | ✅ |
| 16 | SectionName | SECTION_NAME | — | ✅ |
| 17 | TwoPartSectionType | TWO_PART_SECTION_TYPE | — | ✅ |

---

## 📚 Referências

- [[po-module-data-dictionary]] — Dossiê do módulo PO
