---
id: DOC-OTHER-PVO-RelatedContractP
doc_type: system-doc
title: "RelatedContractP — PVO Cross-Module"
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
  - RelatedContractP
  - relatedcontractp
source_format: markdown
conversion_pipeline: json-to-md-v1
conversion_quality: 100
qa_score: 0
qa_status: not_reviewed
created_at: 2026-03-31
updated_at: 2026-03-31
---

# RelatedContractP

## 📌 Visão Geral

View Object para extração BICC de dados de Related Contract P. Acessa as tabelas: HZ_PARTIES, OKC_K_HEADERS_ALL_B, OKC_K_HEADERS_TL (+2).

**Caminho:** `FscmTopModelAM.ContractsCoreAM.RelatedContractP`

| Atributos | Tabelas | PKs | BICC | BICC % |
|-----------|---------|-----|------|--------|
| 21 | 5 | 2 | 21 | 100% |

---

## 🔗 Tabelas Relacionadas

- [[hz_parties|HZ_PARTIES]] — 2 atributos (2 BICC)
- [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]] — 6 atributos (1 PKs, 6 BICC)
- [[okc_k_headers_tl|OKC_K_HEADERS_TL]] — 4 atributos (4 BICC)
- [[okc_k_party_roles_vl|OKC_K_PARTY_ROLES_VL]] — 3 atributos (3 BICC)
- [[okc_k_rel_objs|OKC_K_REL_OBJS]] — 6 atributos (1 PKs, 6 BICC)

---

## ⚙️ Atributos

### [[hz_parties|HZ_PARTIES]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | PartyName | PARTY_NAME | — | ✅ |
| 2 | PartyPEOPartyId | PARTY_ID | — | ✅ |

### [[okc_k_headers_all_b|OKC_K_HEADERS_ALL_B]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | BuyOrSell | BUY_OR_SELL | — | ✅ |
| 2 | ContractHeaderBasePEOId | ID | — | ✅ |
| 3 | ContractHeaderBasePEOVersionType | VERSION_TYPE | — | ✅ |
| 4 | ContractNumber | CONTRACT_NUMBER | — | ✅ |
| 5 | ContractTypeId | CONTRACT_TYPE_ID | — | ✅ |
| 6 | MajorVersion | MAJOR_VERSION | 🔑 | ✅ |

### [[okc_k_headers_tl|OKC_K_HEADERS_TL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractHeaderTanslationPEOCognomen | COGNOMEN | — | ✅ |
| 2 | ContractHeaderTranslationPEOId | ID | — | ✅ |
| 3 | ContractHeaderTranslationPEOLanguage | LANGUAGE | — | ✅ |
| 4 | ContractHeaderTranslationPEOMajorVersion | MAJOR_VERSION | — | ✅ |

### [[okc_k_party_roles_vl|OKC_K_PARTY_ROLES_VL]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ContractPartyPEOId | ID | — | ✅ |
| 2 | ContractPartyPEOMajorVersion | MAJOR_VERSION | — | ✅ |
| 3 | PrimaryYn | PRIMARY_YN | — | ✅ |

### [[okc_k_rel_objs|OKC_K_REL_OBJS]]

| # | Atributo | Coluna | PK | BICC |
|---|----------|--------|----|------|
| 1 | ChrId | CHR_ID | — | ✅ |
| 2 | Object1Id1 | OBJECT1_ID1 | — | ✅ |
| 3 | ObjectVersionNumber | OBJECT_VERSION_NUMBER | — | ✅ |
| 4 | RelatedDocumentPEOId | ID | 🔑 | ✅ |
| 5 | RelatedDocumentPEOJtotObject1Code | JTOT_OBJECT1_CODE | — | ✅ |
| 6 | RtyCode | RTY_CODE | — | ✅ |

---

## 📚 Referências

- [[other-module-data-dictionary]] — Dossiê do módulo OTHER
