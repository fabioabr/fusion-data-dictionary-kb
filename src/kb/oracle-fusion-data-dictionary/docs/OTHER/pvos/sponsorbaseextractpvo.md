---
id: DOC-OTHER-PVO-SponsorBaseExtractPVO
doc_type: system-doc
title: "SponsorBaseExtractPVO — PVO Cross-Module"
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
  - SponsorBaseExtractPVO
  - sponsorbaseextractpvo
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# SponsorBaseExtractPVO

## 📌 Visão Geral

View Object para extração BICC de dados de Sponsor Base Extract. Acessa as tabelas: GMS_SPONSORS_B.

**Caminho:** `FscmTopModelAM.PrjExtractAM.GmsBiccExtractAM.SponsorBaseExtractPVO`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 16 | 1 | 1 | 16 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[gms_sponsors_b|GMS_SPONSORS_B]] — 16 atributos (1 PKs, 16 BICC)

---

## ⚙️ Atributos

### [[gms_sponsors_b|GMS_SPONSORS_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | SponsorBasePEOBillToSponsor | BILL_TO_SPONSOR | — | ✅ |
| 2 | SponsorBasePEOCreatedBy | CREATED_BY | — | ✅ |
| 3 | SponsorBasePEOCreationDate | CREATION_DATE | — | ✅ |
| 4 | SponsorBasePEOFederalFlag | FEDERAL_FLAG | — | ✅ |
| 5 | SponsorBasePEOIndRateSchId | IND_RATE_SCH_ID | — | ✅ |
| 6 | SponsorBasePEOLastUpdateDate | LAST_UPDATE_DATE | — | ✅ |
| 7 | SponsorBasePEOLastUpdateLogin | LAST_UPDATE_LOGIN | — | ✅ |
| 8 | SponsorBasePEOLastUpdatedBy | LAST_UPDATED_BY | — | ✅ |
| 9 | SponsorBasePEOLocFlag | LOC_FLAG | — | ✅ |
| 10 | SponsorBasePEOLocNumber | LOC_NUMBER | — | ✅ |
| 11 | SponsorBasePEOObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 12 | SponsorBasePEOPartyId | PARTY_ID | — | ✅ |
| 13 | SponsorBasePEORelatedSponsorAcctId | RELATED_SPONSOR_ACCT_ID | — | ✅ |
| 14 | SponsorBasePEOSponsorAcctId | SPONSOR_ACCT_ID | — | ✅ |
| 15 | SponsorBasePEOSponsorId | SPONSOR_ID | 🔑 | ✅ |
| 16 | SponsorBasePEOStatusCode | STATUS_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
